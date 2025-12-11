from django.test import TestCase
from django.db.models.deletion import ProtectedError
from unittest.mock import patch

from .models import Brand, Car, CarInventory


class BrandModelTests(TestCase):
    def test_str_returns_name(self):
        brand = Brand.objects.create(name="Toyota")
        self.assertEqual(str(brand), "Toyota")


class CarModelTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls._ai_bio_patcher = patch('cars.signals.get_car_ai_bio', return_value='AI BIO (mock)')
        cls._ai_bio_patcher.start()

    @classmethod
    def tearDownClass(cls):
        cls._ai_bio_patcher.stop()
        super().tearDownClass()

    def setUp(self):
        self.brand = Brand.objects.create(name="Honda")

    def test_create_car_and_str(self):
        car = Car.objects.create(
            model="Civic",
            brand=self.brand,
            factory_year=2020,
            model_year=2021,
            plate="ABC1D23",
            value=95000.0,
        )
        self.assertEqual(str(car), "Civic")
        self.assertEqual(car.brand, self.brand)
        self.assertEqual(car.factory_year, 2020)
        self.assertEqual(car.model_year, 2021)
        self.assertEqual(car.plate, "ABC1D23")
        self.assertEqual(car.value, 95000.0)

    def test_optional_fields_can_be_null(self):
        car = Car.objects.create(model="Fit", brand=self.brand)
        self.assertIsNone(car.factory_year)
        self.assertIsNone(car.model_year)
        self.assertIsNone(car.plate)
        self.assertIsNone(car.value)
        self.assertIsNone(car.photo.name)
        # bio é preenchido pelo signal via OpenAI; aqui deve vir do mock
        self.assertEqual(car.bio, 'AI BIO (mock)')

    def test_brand_on_delete_protect(self):
        car = Car.objects.create(model="City", brand=self.brand)
        with self.assertRaises(ProtectedError):
            self.brand.delete()
        # Ensure the car still exists
        self.assertTrue(Car.objects.filter(pk=car.pk).exists())


class CarInventoryModelTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls._ai_bio_patcher = patch('cars.signals.get_car_ai_bio', return_value='AI BIO (mock)')
        cls._ai_bio_patcher.start()

    @classmethod
    def tearDownClass(cls):
        cls._ai_bio_patcher.stop()
        super().tearDownClass()

    def test_str_and_fields(self):
        inv = CarInventory.objects.create(cars_count=10, cars_value=123456.78)
        self.assertEqual(str(inv), "10 - 123456.78")

    def test_ordering_by_created_at_desc(self):
        first = CarInventory.objects.create(cars_count=1, cars_value=100.0)
        second = CarInventory.objects.create(cars_count=2, cars_value=200.0)
        third = CarInventory.objects.create(cars_count=3, cars_value=300.0)

        qs = list(CarInventory.objects.all())
        self.assertEqual(qs[0], third)
        self.assertEqual(qs[1], second)
        self.assertEqual(qs[2], first)
