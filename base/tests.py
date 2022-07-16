# from datetime import timezone
#
# from django.test import TestCase

# Create your tests here.
# from base.models import Product


# class productrTest(TestCase):
#
#     def create_product(self, title="only a test", body="yes, this is only a test"):
#         return Product.objects.create(
#             title=title, body=body, created_at=timezone.now())
#
#     def test_whatever_creation(self):
#         w = self.create_product()
#         self.assertTrue(isinstance(w, Product))
#         self.assertEqual(w.__unicode__(), w.title)