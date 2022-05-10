from django.urls import resolve
from django.test import TestCase
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string

class HomePageTest(TestCase):
    # def test_root_url_resolve_to_home_page_view(self):
    #     found = resolve('/')
    #     self.assertEqual(found.func,home_page)

    # def test_home_page_returns_correct_html(self):
    #     # request = HttpRequest()# 1
    #     # response = home_page(request) # 2
    #     # html = response.content.decode('utf8')# 3
    #     # # self.assertTrue(html.startswith('<html>'))# 4
    #     # # self.assertIn('<title>To-Do lists</title>', html) # 5
    #     # # self.assertTrue(html.endswith('</html>'))#4
    #     # expected_html=render_to_string('home.html')
    #     # self.assertEqual(html,expected_html)
    #     response=self.client.get('/') #1

    #     html = response.content.decode('utf8')#2
    #     self.assertTrue(html.startswith('<html>'))#3
    #     self.assertIn('<title>To-Do lists</title>', html)
    #     self.assertTrue(html.strip().endswith('</html>'))

    #     self.assertTemplateUsed(response,'wrong.html') #3
    def test_uses_home_template(self):
        response=self.client.get('/')
        self.assertTemplateUsed(response,'home.html')
    
    def test_can_sace_a_POST_request(self):
        response =self.client.post('/',data={'item_text':'A new list item'})
        self.assertIn('A new list item',response.content.decode())
        self.assertTemplateUsed(response,'home.html')

# Create your tests here.
