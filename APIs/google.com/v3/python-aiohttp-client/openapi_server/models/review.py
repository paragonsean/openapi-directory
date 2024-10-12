# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.rating import Rating
from openapi_server import util


class Review(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, author: str=None, body: str=None, language_code: str=None, link: str=None, rating: List[Rating]=None, review_time: str=None, title: str=None, type: str=None, visit_time: str=None):
        """Review - a model defined in OpenAPI

        :param author: The author of this Review.
        :param body: The body of this Review.
        :param language_code: The language_code of this Review.
        :param link: The link of this Review.
        :param rating: The rating of this Review.
        :param review_time: The review_time of this Review.
        :param title: The title of this Review.
        :param type: The type of this Review.
        :param visit_time: The visit_time of this Review.
        """
        self.openapi_types = {
            'author': str,
            'body': str,
            'language_code': str,
            'link': str,
            'rating': List[Rating],
            'review_time': str,
            'title': str,
            'type': str,
            'visit_time': str
        }

        self.attribute_map = {
            'author': 'author',
            'body': 'body',
            'language_code': 'languageCode',
            'link': 'link',
            'rating': 'rating',
            'review_time': 'reviewTime',
            'title': 'title',
            'type': 'type',
            'visit_time': 'visitTime'
        }

        self._author = author
        self._body = body
        self._language_code = language_code
        self._link = link
        self._rating = rating
        self._review_time = review_time
        self._title = title
        self._type = type
        self._visit_time = visit_time

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Review':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Review of this Review.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def author(self):
        """Gets the author of this Review.

        The author of the review.

        :return: The author of this Review.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this Review.

        The author of the review.

        :param author: The author of this Review.
        :type author: str
        """

        self._author = author

    @property
    def body(self):
        """Gets the body of this Review.

        The body of the review.

        :return: The body of this Review.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this Review.

        The body of the review.

        :param body: The body of this Review.
        :type body: str
        """

        self._body = body

    @property
    def language_code(self):
        """Gets the language_code of this Review.

        Language of the review, such as \"en\", \"de\", etc.

        :return: The language_code of this Review.
        :rtype: str
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """Sets the language_code of this Review.

        Language of the review, such as \"en\", \"de\", etc.

        :param language_code: The language_code of this Review.
        :type language_code: str
        """

        self._language_code = language_code

    @property
    def link(self):
        """Gets the link of this Review.

        The url of the review.

        :return: The link of this Review.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this Review.

        The url of the review.

        :param link: The link of this Review.
        :type link: str
        """

        self._link = link

    @property
    def rating(self):
        """Gets the rating of this Review.

        Any ratings associated with this review. This is repeated because reviews can include ratings on different aspects of a listing, e.g. location, cleanliness, etc.

        :return: The rating of this Review.
        :rtype: List[Rating]
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        """Sets the rating of this Review.

        Any ratings associated with this review. This is repeated because reviews can include ratings on different aspects of a listing, e.g. location, cleanliness, etc.

        :param rating: The rating of this Review.
        :type rating: List[Rating]
        """

        self._rating = rating

    @property
    def review_time(self):
        """Gets the review_time of this Review.

        Unix timestamp (in seconds) of the review, in UTC+0.

        :return: The review_time of this Review.
        :rtype: str
        """
        return self._review_time

    @review_time.setter
    def review_time(self, review_time):
        """Sets the review_time of this Review.

        Unix timestamp (in seconds) of the review, in UTC+0.

        :param review_time: The review_time of this Review.
        :type review_time: str
        """

        self._review_time = review_time

    @property
    def title(self):
        """Gets the title of this Review.

        The title of the review, for example: Great three bedrooms.

        :return: The title of this Review.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Review.

        The title of the review, for example: Great three bedrooms.

        :param title: The title of this Review.
        :type title: str
        """

        self._title = title

    @property
    def type(self):
        """Gets the type of this Review.

        The type of the review.

        :return: The type of this Review.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Review.

        The type of the review.

        :param type: The type of this Review.
        :type type: str
        """
        allowed_values = ["UNKNOWN", "EDITORIAL", "USER"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def visit_time(self):
        """Gets the visit_time of this Review.

        Unix timestamp (in seconds) of when the stay was, in UTC+0.

        :return: The visit_time of this Review.
        :rtype: str
        """
        return self._visit_time

    @visit_time.setter
    def visit_time(self, visit_time):
        """Sets the visit_time of this Review.

        Unix timestamp (in seconds) of when the stay was, in UTC+0.

        :param visit_time: The visit_time of this Review.
        :type visit_time: str
        """

        self._visit_time = visit_time
