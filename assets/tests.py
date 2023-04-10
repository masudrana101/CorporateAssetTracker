# from django.urls import reverse
# from django.test import TestCase
# from rest_framework import status
# from rest_framework.test import APITestCase
# from authentications.models import UserAccount as User
# from .models import Company, Employee, Device, DeviceLog

# class CompanyTests(APITestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(
#             username='testuser@test.com', 
#             email='testuser@test.com',
#             phone='1234567890',
#             password='testpassword',
#             first_name='test',
#             last_name='user',
#         )
#         self.company = Company.objects.create(
#             name='test company',
#             address='test address',
#             company_license='test license',
#         )
#         self.client.force_authenticate(user=self.user)

#     def test_create_company(self):

#         url = reverse('company')
#         data = {
#             'name': 'test company',
#             'address': 'test address',
#             'company_license': 'test license',
#         }
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Company.objects.count(), 2)
#         self.assertEqual(Company.objects.get(pk=2).name, 'test company')

#     def test_get_company_list(self):
#         """
#         Ensure we can get company list.
#         """
#         url = reverse('company')
#         response = self.client.get(url, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)

#     def test_get_company_detail(self):
#         """
#         Ensure we can get company detail.
#         """
#         url = reverse('company', args=[self.company.pk])
#         response = self.client.get(url, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['name'], 'test company')

#     def test_update_company(self):
#         """
#         Ensure we can update a company object.
#         """
#         url = reverse('company', args=[self.company.pk])
#         data = {
#             'name': 'test company updated',
#             'address': 'test address updated',
#             'company_license': 'test license updated',
#         }
#         response = self.client.patch(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(Company.objects.get(pk=1).name, 'test company updated')

#     def test_delete_company(self):
#         """
#         Ensure we can delete a company object.
#         """
#         url = reverse('company', args=[self.company.pk])
#         response = self.client.delete(url, format='json')
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Company.objects.count(), 0)

        
        