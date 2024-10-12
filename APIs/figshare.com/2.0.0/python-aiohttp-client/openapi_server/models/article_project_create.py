# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.custom_article_field_add import CustomArticleFieldAdd
from openapi_server.models.funding_create import FundingCreate
from openapi_server.models.timeline_update import TimelineUpdate
from openapi_server import util


class ArticleProjectCreate(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, authors: List[object]=[], categories: List[int]=[], categories_by_source_id: List[str]=[], custom_fields: object=None, custom_fields_list: List[CustomArticleFieldAdd]=None, defined_type: str=None, description: str='', doi: str='', funding: str='', funding_list: List[FundingCreate]=None, handle: str='', keywords: List[str]=[], license: int=0, references: List[str]=[], resource_doi: str='', resource_title: str='', tags: List[str]=[], timeline: TimelineUpdate=None, title: str=None):
        """ArticleProjectCreate - a model defined in OpenAPI

        :param authors: The authors of this ArticleProjectCreate.
        :param categories: The categories of this ArticleProjectCreate.
        :param categories_by_source_id: The categories_by_source_id of this ArticleProjectCreate.
        :param custom_fields: The custom_fields of this ArticleProjectCreate.
        :param custom_fields_list: The custom_fields_list of this ArticleProjectCreate.
        :param defined_type: The defined_type of this ArticleProjectCreate.
        :param description: The description of this ArticleProjectCreate.
        :param doi: The doi of this ArticleProjectCreate.
        :param funding: The funding of this ArticleProjectCreate.
        :param funding_list: The funding_list of this ArticleProjectCreate.
        :param handle: The handle of this ArticleProjectCreate.
        :param keywords: The keywords of this ArticleProjectCreate.
        :param license: The license of this ArticleProjectCreate.
        :param references: The references of this ArticleProjectCreate.
        :param resource_doi: The resource_doi of this ArticleProjectCreate.
        :param resource_title: The resource_title of this ArticleProjectCreate.
        :param tags: The tags of this ArticleProjectCreate.
        :param timeline: The timeline of this ArticleProjectCreate.
        :param title: The title of this ArticleProjectCreate.
        """
        self.openapi_types = {
            'authors': List[object],
            'categories': List[int],
            'categories_by_source_id': List[str],
            'custom_fields': object,
            'custom_fields_list': List[CustomArticleFieldAdd],
            'defined_type': str,
            'description': str,
            'doi': str,
            'funding': str,
            'funding_list': List[FundingCreate],
            'handle': str,
            'keywords': List[str],
            'license': int,
            'references': List[str],
            'resource_doi': str,
            'resource_title': str,
            'tags': List[str],
            'timeline': TimelineUpdate,
            'title': str
        }

        self.attribute_map = {
            'authors': 'authors',
            'categories': 'categories',
            'categories_by_source_id': 'categories_by_source_id',
            'custom_fields': 'custom_fields',
            'custom_fields_list': 'custom_fields_list',
            'defined_type': 'defined_type',
            'description': 'description',
            'doi': 'doi',
            'funding': 'funding',
            'funding_list': 'funding_list',
            'handle': 'handle',
            'keywords': 'keywords',
            'license': 'license',
            'references': 'references',
            'resource_doi': 'resource_doi',
            'resource_title': 'resource_title',
            'tags': 'tags',
            'timeline': 'timeline',
            'title': 'title'
        }

        self._authors = authors
        self._categories = categories
        self._categories_by_source_id = categories_by_source_id
        self._custom_fields = custom_fields
        self._custom_fields_list = custom_fields_list
        self._defined_type = defined_type
        self._description = description
        self._doi = doi
        self._funding = funding
        self._funding_list = funding_list
        self._handle = handle
        self._keywords = keywords
        self._license = license
        self._references = references
        self._resource_doi = resource_doi
        self._resource_title = resource_title
        self._tags = tags
        self._timeline = timeline
        self._title = title

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ArticleProjectCreate':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ArticleProjectCreate of this ArticleProjectCreate.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def authors(self):
        """Gets the authors of this ArticleProjectCreate.

        List of authors to be associated with the article. The list can contain the following fields: id, name, first_name, last_name, email, orcid_id. If an id is supplied, it will take priority and everything else will be ignored. No more than 10 authors. For adding more authors use the specific authors endpoint.

        :return: The authors of this ArticleProjectCreate.
        :rtype: List[object]
        """
        return self._authors

    @authors.setter
    def authors(self, authors):
        """Sets the authors of this ArticleProjectCreate.

        List of authors to be associated with the article. The list can contain the following fields: id, name, first_name, last_name, email, orcid_id. If an id is supplied, it will take priority and everything else will be ignored. No more than 10 authors. For adding more authors use the specific authors endpoint.

        :param authors: The authors of this ArticleProjectCreate.
        :type authors: List[object]
        """

        self._authors = authors

    @property
    def categories(self):
        """Gets the categories of this ArticleProjectCreate.

        List of category ids to be associated with the article(e.g [1, 23, 33, 66])

        :return: The categories of this ArticleProjectCreate.
        :rtype: List[int]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this ArticleProjectCreate.

        List of category ids to be associated with the article(e.g [1, 23, 33, 66])

        :param categories: The categories of this ArticleProjectCreate.
        :type categories: List[int]
        """

        self._categories = categories

    @property
    def categories_by_source_id(self):
        """Gets the categories_by_source_id of this ArticleProjectCreate.

        List of category source ids to be associated with the article, supersedes the categories property

        :return: The categories_by_source_id of this ArticleProjectCreate.
        :rtype: List[str]
        """
        return self._categories_by_source_id

    @categories_by_source_id.setter
    def categories_by_source_id(self, categories_by_source_id):
        """Sets the categories_by_source_id of this ArticleProjectCreate.

        List of category source ids to be associated with the article, supersedes the categories property

        :param categories_by_source_id: The categories_by_source_id of this ArticleProjectCreate.
        :type categories_by_source_id: List[str]
        """

        self._categories_by_source_id = categories_by_source_id

    @property
    def custom_fields(self):
        """Gets the custom_fields of this ArticleProjectCreate.

        List of key, values pairs to be associated with the article

        :return: The custom_fields of this ArticleProjectCreate.
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this ArticleProjectCreate.

        List of key, values pairs to be associated with the article

        :param custom_fields: The custom_fields of this ArticleProjectCreate.
        :type custom_fields: object
        """

        self._custom_fields = custom_fields

    @property
    def custom_fields_list(self):
        """Gets the custom_fields_list of this ArticleProjectCreate.

        List of custom fields values, supersedes custom_fields parameter

        :return: The custom_fields_list of this ArticleProjectCreate.
        :rtype: List[CustomArticleFieldAdd]
        """
        return self._custom_fields_list

    @custom_fields_list.setter
    def custom_fields_list(self, custom_fields_list):
        """Sets the custom_fields_list of this ArticleProjectCreate.

        List of custom fields values, supersedes custom_fields parameter

        :param custom_fields_list: The custom_fields_list of this ArticleProjectCreate.
        :type custom_fields_list: List[CustomArticleFieldAdd]
        """

        self._custom_fields_list = custom_fields_list

    @property
    def defined_type(self):
        """Gets the defined_type of this ArticleProjectCreate.

        <b>One of:</b> <code>figure</code> <code>online resource</code> <code>preprint</code> <code>book</code> <code>conference contribution</code> <code>media</code> <code>dataset</code> <code>poster</code> <code>journal contribution</code> <code>presentation</code> <code>thesis</code> <code>software</code>

        :return: The defined_type of this ArticleProjectCreate.
        :rtype: str
        """
        return self._defined_type

    @defined_type.setter
    def defined_type(self, defined_type):
        """Sets the defined_type of this ArticleProjectCreate.

        <b>One of:</b> <code>figure</code> <code>online resource</code> <code>preprint</code> <code>book</code> <code>conference contribution</code> <code>media</code> <code>dataset</code> <code>poster</code> <code>journal contribution</code> <code>presentation</code> <code>thesis</code> <code>software</code>

        :param defined_type: The defined_type of this ArticleProjectCreate.
        :type defined_type: str
        """

        self._defined_type = defined_type

    @property
    def description(self):
        """Gets the description of this ArticleProjectCreate.

        The article description. In a publisher case, usually this is the remote article description

        :return: The description of this ArticleProjectCreate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ArticleProjectCreate.

        The article description. In a publisher case, usually this is the remote article description

        :param description: The description of this ArticleProjectCreate.
        :type description: str
        """
        if description is not None and len(description) > 10000:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `10000`")

        self._description = description

    @property
    def doi(self):
        """Gets the doi of this ArticleProjectCreate.

        Not applicable for regular users. In an institutional case, make sure your group supports setting DOIs. This setting is applied by figshare via opening a ticket through our support/helpdesk system.

        :return: The doi of this ArticleProjectCreate.
        :rtype: str
        """
        return self._doi

    @doi.setter
    def doi(self, doi):
        """Sets the doi of this ArticleProjectCreate.

        Not applicable for regular users. In an institutional case, make sure your group supports setting DOIs. This setting is applied by figshare via opening a ticket through our support/helpdesk system.

        :param doi: The doi of this ArticleProjectCreate.
        :type doi: str
        """

        self._doi = doi

    @property
    def funding(self):
        """Gets the funding of this ArticleProjectCreate.

        Grant number or funding authority

        :return: The funding of this ArticleProjectCreate.
        :rtype: str
        """
        return self._funding

    @funding.setter
    def funding(self, funding):
        """Sets the funding of this ArticleProjectCreate.

        Grant number or funding authority

        :param funding: The funding of this ArticleProjectCreate.
        :type funding: str
        """

        self._funding = funding

    @property
    def funding_list(self):
        """Gets the funding_list of this ArticleProjectCreate.

        Funding creation / update items

        :return: The funding_list of this ArticleProjectCreate.
        :rtype: List[FundingCreate]
        """
        return self._funding_list

    @funding_list.setter
    def funding_list(self, funding_list):
        """Sets the funding_list of this ArticleProjectCreate.

        Funding creation / update items

        :param funding_list: The funding_list of this ArticleProjectCreate.
        :type funding_list: List[FundingCreate]
        """

        self._funding_list = funding_list

    @property
    def handle(self):
        """Gets the handle of this ArticleProjectCreate.

        Not applicable for regular users. In an institutional case, make sure your group supports setting Handles. This setting is applied by figshare via opening a ticket through our support/helpdesk system.

        :return: The handle of this ArticleProjectCreate.
        :rtype: str
        """
        return self._handle

    @handle.setter
    def handle(self, handle):
        """Sets the handle of this ArticleProjectCreate.

        Not applicable for regular users. In an institutional case, make sure your group supports setting Handles. This setting is applied by figshare via opening a ticket through our support/helpdesk system.

        :param handle: The handle of this ArticleProjectCreate.
        :type handle: str
        """

        self._handle = handle

    @property
    def keywords(self):
        """Gets the keywords of this ArticleProjectCreate.

        List of tags to be associated with the article. Tags can be used instead

        :return: The keywords of this ArticleProjectCreate.
        :rtype: List[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this ArticleProjectCreate.

        List of tags to be associated with the article. Tags can be used instead

        :param keywords: The keywords of this ArticleProjectCreate.
        :type keywords: List[str]
        """

        self._keywords = keywords

    @property
    def license(self):
        """Gets the license of this ArticleProjectCreate.

        License id for this article.

        :return: The license of this ArticleProjectCreate.
        :rtype: int
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this ArticleProjectCreate.

        License id for this article.

        :param license: The license of this ArticleProjectCreate.
        :type license: int
        """

        self._license = license

    @property
    def references(self):
        """Gets the references of this ArticleProjectCreate.

        List of links to be associated with the article (e.g [\"http://link1\", \"http://link2\", \"http://link3\"])

        :return: The references of this ArticleProjectCreate.
        :rtype: List[str]
        """
        return self._references

    @references.setter
    def references(self, references):
        """Sets the references of this ArticleProjectCreate.

        List of links to be associated with the article (e.g [\"http://link1\", \"http://link2\", \"http://link3\"])

        :param references: The references of this ArticleProjectCreate.
        :type references: List[str]
        """

        self._references = references

    @property
    def resource_doi(self):
        """Gets the resource_doi of this ArticleProjectCreate.

        Not applicable to regular users. In a publisher case, this is the publisher article DOI.

        :return: The resource_doi of this ArticleProjectCreate.
        :rtype: str
        """
        return self._resource_doi

    @resource_doi.setter
    def resource_doi(self, resource_doi):
        """Sets the resource_doi of this ArticleProjectCreate.

        Not applicable to regular users. In a publisher case, this is the publisher article DOI.

        :param resource_doi: The resource_doi of this ArticleProjectCreate.
        :type resource_doi: str
        """

        self._resource_doi = resource_doi

    @property
    def resource_title(self):
        """Gets the resource_title of this ArticleProjectCreate.

        Not applicable to regular users. In a publisher case, this is the publisher article title.

        :return: The resource_title of this ArticleProjectCreate.
        :rtype: str
        """
        return self._resource_title

    @resource_title.setter
    def resource_title(self, resource_title):
        """Sets the resource_title of this ArticleProjectCreate.

        Not applicable to regular users. In a publisher case, this is the publisher article title.

        :param resource_title: The resource_title of this ArticleProjectCreate.
        :type resource_title: str
        """

        self._resource_title = resource_title

    @property
    def tags(self):
        """Gets the tags of this ArticleProjectCreate.

        List of tags to be associated with the article. Keywords can be used instead

        :return: The tags of this ArticleProjectCreate.
        :rtype: List[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ArticleProjectCreate.

        List of tags to be associated with the article. Keywords can be used instead

        :param tags: The tags of this ArticleProjectCreate.
        :type tags: List[str]
        """

        self._tags = tags

    @property
    def timeline(self):
        """Gets the timeline of this ArticleProjectCreate.


        :return: The timeline of this ArticleProjectCreate.
        :rtype: TimelineUpdate
        """
        return self._timeline

    @timeline.setter
    def timeline(self, timeline):
        """Sets the timeline of this ArticleProjectCreate.


        :param timeline: The timeline of this ArticleProjectCreate.
        :type timeline: TimelineUpdate
        """

        self._timeline = timeline

    @property
    def title(self):
        """Gets the title of this ArticleProjectCreate.

        Title of article

        :return: The title of this ArticleProjectCreate.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ArticleProjectCreate.

        Title of article

        :param title: The title of this ArticleProjectCreate.
        :type title: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")
        if title is not None and len(title) > 1000:
            raise ValueError("Invalid value for `title`, length must be less than or equal to `1000`")
        if title is not None and len(title) < 3:
            raise ValueError("Invalid value for `title`, length must be greater than or equal to `3`")

        self._title = title
