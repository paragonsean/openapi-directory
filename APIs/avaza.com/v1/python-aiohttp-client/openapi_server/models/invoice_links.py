# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class InvoiceLinks(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, client_view: str=None, edit: str=None, view: str=None):
        """InvoiceLinks - a model defined in OpenAPI

        :param client_view: The client_view of this InvoiceLinks.
        :param edit: The edit of this InvoiceLinks.
        :param view: The view of this InvoiceLinks.
        """
        self.openapi_types = {
            'client_view': str,
            'edit': str,
            'view': str
        }

        self.attribute_map = {
            'client_view': 'ClientView',
            'edit': 'Edit',
            'view': 'View'
        }

        self._client_view = client_view
        self._edit = edit
        self._view = view

    @classmethod
    def from_dict(cls, dikt: dict) -> 'InvoiceLinks':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The InvoiceLinks of this InvoiceLinks.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def client_view(self):
        """Gets the client_view of this InvoiceLinks.


        :return: The client_view of this InvoiceLinks.
        :rtype: str
        """
        return self._client_view

    @client_view.setter
    def client_view(self, client_view):
        """Sets the client_view of this InvoiceLinks.


        :param client_view: The client_view of this InvoiceLinks.
        :type client_view: str
        """

        self._client_view = client_view

    @property
    def edit(self):
        """Gets the edit of this InvoiceLinks.


        :return: The edit of this InvoiceLinks.
        :rtype: str
        """
        return self._edit

    @edit.setter
    def edit(self, edit):
        """Sets the edit of this InvoiceLinks.


        :param edit: The edit of this InvoiceLinks.
        :type edit: str
        """

        self._edit = edit

    @property
    def view(self):
        """Gets the view of this InvoiceLinks.


        :return: The view of this InvoiceLinks.
        :rtype: str
        """
        return self._view

    @view.setter
    def view(self, view):
        """Sets the view of this InvoiceLinks.


        :param view: The view of this InvoiceLinks.
        :type view: str
        """

        self._view = view
