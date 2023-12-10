from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTest(SimpleTestCase):

    def test_home_page_status_code_fail(self):
        resp = self.client.get(reverse("home"))
        self.assertNotEqual(resp.status_code, 404)
    def test_home_page_status_code(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)

    def test_home_page_template_fail(self):
        resp = self.client.get(reverse("home"))
        self.assertTemplateNotUsed(resp, "about.html")

    def test_home_page_template(self):
        resp = self.client.get(reverse("home"))
        self.assertTemplateUsed(resp, "home.html")

    def test_home_page_template_parentage(self):
        resp = self.client.get(reverse("home"))
        self.assertTemplateUsed(resp, "base.html")

    def test_about_page_status_code_fail(self):
        resp = self.client.get(reverse("about"))
        self.assertNotEqual(resp.status_code, 404)

    def test_about_page_status_code(self):
        resp = self.client.get(reverse("about"))
        self.assertEqual(resp.status_code, 200)

    def test_about_page_template_fail(self):
        resp = self.client.get(reverse("about"))
        self.assertTemplateNotUsed(resp, "home.html")

    def test_about_page_template(self):
        resp = self.client.get(reverse("about"))
        self.assertTemplateUsed(resp, "about.html")


    def test_about_page_template_parentage(self):
        resp = self.client.get(reverse("about"))
        self.assertTemplateUsed(resp, "base.html")



