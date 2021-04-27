from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.

class BlogTests(TestCase):
    def setup(self):

        self.user = get_user_model().objects.create_user(

            username = "test_user",
            email = "test@email.com",
            password= "password"
        )

        self.post = Post.objects.create(
            title = 'The tiltle of the article',
            body = "The body of the  article is this",
            author = self.user
        )

    def test_string_representation(self):
        post = Post(title= 'A simple title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):

        self.assertEqual(f"{self.post.title}", "a good title")
        self.assertEqual(f"{self.post.author}", "test_user")
        self.assertEqual(f"{self.post.body}", "A nice body")

    def test_post_listing(self):
        reponse = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice Body')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000000000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'a good title')
        self.assertTemplateUsed(response, 'post_detail.html')



        