import unittest
from unittest.mock import patch
from reddit_user import RedditUser

class TestRedditUser(unittest.TestCase):
    def setUp(self):
        self.reddit_user = RedditUser("test_user")

    @patch("requests.get")
    def test_get_submissions(self, mock_get):
        # Mock the response from the requests.get method
        mock_response = {
            "data": {
                "children": [
                    {
                        "data": {
                            "id": "123",
                            "subreddit": "test_subreddit",
                            "selftext": "test_text",
                            "created_utc": 1625000000,
                            "score": 10,
                            "permalink": "http://www.reddit.com/test_permalink",
                            "url": "http://www.test.com",
                            "title": "test_title",
                            "is_self": True,
                            "gilded": 0,
                            "domain": "test_domain"
                        }
                    }
                ],
                "after": None
            }
        }
        mock_get.return_value.json.return_value = mock_response

        # Call the method under test
        submissions = self.reddit_user.get_submissions()

        # Assert the expected results
        self.assertEqual(len(submissions), 1)
        self.assertEqual(submissions[0].id, "123")
        self.assertEqual(submissions[0].subreddit, "test_subreddit")
        self.assertEqual(submissions[0].text, "test_text")
        self.assertEqual(submissions[0].created_utc, 1625000000)
        self.assertEqual(submissions[0].score, 10)
        self.assertEqual(submissions[0].permalink, "http://www.reddit.com/test_permalink")
        self.assertEqual(submissions[0].url, "http://www.test.com")
        self.assertEqual(submissions[0].title, "test_title")
        self.assertEqual(submissions[0].is_self, True)
        self.assertEqual(submissions[0].gilded, 0)
        self.assertEqual(submissions[0].domain, "test_domain")

if __name__ == "__main__":
    unittest.main()