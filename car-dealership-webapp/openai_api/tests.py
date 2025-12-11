from django.test import TestCase
from unittest.mock import patch, MagicMock
import os


class GetCarAIBioTests(TestCase):
    @patch.dict(os.environ, {"OPENAI_API_KEY": "test-key"}, clear=False)
    @patch("openai_api.client.OpenAI")
    def test_returns_output_text_and_calls_openai_with_expected_args(self, mock_openai):
        from openai_api.client import get_car_ai_bio

        # Arrange mock client and response
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.output_text = "Generated bio"
        mock_client.responses.create.return_value = mock_response
        mock_openai.return_value = mock_client

        # Act
        result = get_car_ai_bio("Civic", "Honda", 2021)

        # Assert
        self.assertEqual(result, "Generated bio")

        mock_openai.assert_called_once_with(api_key="test-key")
        mock_client.responses.create.assert_called_once()
        args, kwargs = mock_client.responses.create.call_args

        # Check key params passed to OpenAI
        self.assertEqual(kwargs.get("model"), "gpt-5-nano")
        self.assertIn("Civic", kwargs.get("input"))
        self.assertIn("Honda", kwargs.get("input"))
        self.assertIn("2021", kwargs.get("input"))
        self.assertIn("seller's person", kwargs.get("instructions"))

    @patch.dict(os.environ, {"OPENAI_API_KEY": "test-key"}, clear=False)
    @patch("openai_api.client.OpenAI")
    def test_handles_none_year_in_prompt(self, mock_openai):
        from openai_api.client import get_car_ai_bio

        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.output_text = "Bio without year"
        mock_client.responses.create.return_value = mock_response
        mock_openai.return_value = mock_client

        result = get_car_ai_bio("Model S", "Tesla", None)

        self.assertEqual(result, "Bio without year")
        # Ensure function still builds a prompt including 'None' or blank safely
        _, kwargs = mock_client.responses.create.call_args
        self.assertIn("Model S", kwargs.get("input"))
        self.assertIn("Tesla", kwargs.get("input"))

