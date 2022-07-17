from django.test import TestCase
from objective_harmony.models import Spectrum


class SpectrumTestCase(TestCase):
    def setup(self):
        self.name = '12-tet'
        return Spectrum.objects.create(name=self.name)

    def test_spectrum_creation(self):
        assert isinstance(self.setup(), Spectrum)

    def test_db_column_name(self):
        assert type(self.setup().name) is str
