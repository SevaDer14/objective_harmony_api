from django.test import TestCase
from .models import Spectrum


class SpectrumTestCase(TestCase):
    def setup(self, name='12-tet'):
        return Spectrum.objects.create(name=name)

    def test_spectrum_creation(self):
        spectrum = self.setup()
        self.assertTrue(isinstance(spectrum, Spectrum))
        self.assertEqual(spectrum.__str__(), spectrum.name)
