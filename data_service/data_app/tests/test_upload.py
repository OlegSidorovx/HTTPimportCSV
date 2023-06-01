from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

class FileUploadTestCase(TestCase):
    def test_file_upload(self):
        file = SimpleUploadedFile("test.csv", b"file_content", content_type="text/csv")
        response = self.client.post(reverse("upload_file"), {"file": file})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Файл загружен успешно!"})
