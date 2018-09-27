from django.test import TestCase

from rest_framework.test import APIClient

from .models import Company

client = APIClient()


class CompanyHeadquarterDetailViewTest(TestCase):
    """
    Tests for the /company/<id>/headquarter [GET] endpoint
    """
    fixtures = ['initial_data_tests.json']

    def test_ok(self):
        """
        Test if fields returned are exactly the ones we want
        """
        response = client.get('/api/company/1/headquarter/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(
            sorted(data.keys()),
            sorted(['street', 'postal_code', 'city', 'company_name'])
        )

    def test_put_not_allowed(self):
        """
        Test if other methods are accepted by this endpoint (it should be
        readonly)
        """
        pass



class CompanyDetailUpdateViewTest(TestCase):
    """
    Tests for the /company/<id>/ [PUT] endpoint
    """
    fixtures = ['initial_data_tests.json']

    def test_ok(self):
        """
        Test if fields returned are exactly the ones we want
        """
        response = client.put(
            '/api/company/1/', data={'headquarter': 2}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        # Check if it was changed on the response and also on the database
        self.assertEqual(data['headquarter'], 2)
        self.assertEqual(Company.objects.get(pk=1).headquarter.id, 2)

    def test_invalid_headquarter(self):
        """
        Test if other methods are accepted by this endpoint (it should be
        readonly)
        """
        response = client.put(
            '/api/company/1/', data={'headquarter': 99999}
        )
        self.assertEqual(response.status_code, 400)
