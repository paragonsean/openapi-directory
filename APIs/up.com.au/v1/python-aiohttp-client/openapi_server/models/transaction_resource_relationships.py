# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.category_resource_relationships_parent import CategoryResourceRelationshipsParent
from openapi_server.models.transaction_resource_relationships_account import TransactionResourceRelationshipsAccount
from openapi_server.models.transaction_resource_relationships_category import TransactionResourceRelationshipsCategory
from openapi_server.models.transaction_resource_relationships_tags import TransactionResourceRelationshipsTags
from openapi_server.models.transaction_resource_relationships_transfer_account import TransactionResourceRelationshipsTransferAccount
from openapi_server import util


class TransactionResourceRelationships(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, account: TransactionResourceRelationshipsAccount=None, category: TransactionResourceRelationshipsCategory=None, parent_category: CategoryResourceRelationshipsParent=None, tags: TransactionResourceRelationshipsTags=None, transfer_account: TransactionResourceRelationshipsTransferAccount=None):
        """TransactionResourceRelationships - a model defined in OpenAPI

        :param account: The account of this TransactionResourceRelationships.
        :param category: The category of this TransactionResourceRelationships.
        :param parent_category: The parent_category of this TransactionResourceRelationships.
        :param tags: The tags of this TransactionResourceRelationships.
        :param transfer_account: The transfer_account of this TransactionResourceRelationships.
        """
        self.openapi_types = {
            'account': TransactionResourceRelationshipsAccount,
            'category': TransactionResourceRelationshipsCategory,
            'parent_category': CategoryResourceRelationshipsParent,
            'tags': TransactionResourceRelationshipsTags,
            'transfer_account': TransactionResourceRelationshipsTransferAccount
        }

        self.attribute_map = {
            'account': 'account',
            'category': 'category',
            'parent_category': 'parentCategory',
            'tags': 'tags',
            'transfer_account': 'transferAccount'
        }

        self._account = account
        self._category = category
        self._parent_category = parent_category
        self._tags = tags
        self._transfer_account = transfer_account

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TransactionResourceRelationships':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TransactionResource_relationships of this TransactionResourceRelationships.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def account(self):
        """Gets the account of this TransactionResourceRelationships.


        :return: The account of this TransactionResourceRelationships.
        :rtype: TransactionResourceRelationshipsAccount
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this TransactionResourceRelationships.


        :param account: The account of this TransactionResourceRelationships.
        :type account: TransactionResourceRelationshipsAccount
        """
        if account is None:
            raise ValueError("Invalid value for `account`, must not be `None`")

        self._account = account

    @property
    def category(self):
        """Gets the category of this TransactionResourceRelationships.


        :return: The category of this TransactionResourceRelationships.
        :rtype: TransactionResourceRelationshipsCategory
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this TransactionResourceRelationships.


        :param category: The category of this TransactionResourceRelationships.
        :type category: TransactionResourceRelationshipsCategory
        """
        if category is None:
            raise ValueError("Invalid value for `category`, must not be `None`")

        self._category = category

    @property
    def parent_category(self):
        """Gets the parent_category of this TransactionResourceRelationships.


        :return: The parent_category of this TransactionResourceRelationships.
        :rtype: CategoryResourceRelationshipsParent
        """
        return self._parent_category

    @parent_category.setter
    def parent_category(self, parent_category):
        """Sets the parent_category of this TransactionResourceRelationships.


        :param parent_category: The parent_category of this TransactionResourceRelationships.
        :type parent_category: CategoryResourceRelationshipsParent
        """
        if parent_category is None:
            raise ValueError("Invalid value for `parent_category`, must not be `None`")

        self._parent_category = parent_category

    @property
    def tags(self):
        """Gets the tags of this TransactionResourceRelationships.


        :return: The tags of this TransactionResourceRelationships.
        :rtype: TransactionResourceRelationshipsTags
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TransactionResourceRelationships.


        :param tags: The tags of this TransactionResourceRelationships.
        :type tags: TransactionResourceRelationshipsTags
        """
        if tags is None:
            raise ValueError("Invalid value for `tags`, must not be `None`")

        self._tags = tags

    @property
    def transfer_account(self):
        """Gets the transfer_account of this TransactionResourceRelationships.


        :return: The transfer_account of this TransactionResourceRelationships.
        :rtype: TransactionResourceRelationshipsTransferAccount
        """
        return self._transfer_account

    @transfer_account.setter
    def transfer_account(self, transfer_account):
        """Sets the transfer_account of this TransactionResourceRelationships.


        :param transfer_account: The transfer_account of this TransactionResourceRelationships.
        :type transfer_account: TransactionResourceRelationshipsTransferAccount
        """
        if transfer_account is None:
            raise ValueError("Invalid value for `transfer_account`, must not be `None`")

        self._transfer_account = transfer_account
