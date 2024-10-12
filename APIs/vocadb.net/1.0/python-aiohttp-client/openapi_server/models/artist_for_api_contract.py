# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.artist_contract import ArtistContract
from openapi_server.models.artist_for_artist_for_api_contract import ArtistForArtistForApiContract
from openapi_server.models.artist_relations_for_api import ArtistRelationsForApi
from openapi_server.models.artist_type import ArtistType
from openapi_server.models.content_language_selection import ContentLanguageSelection
from openapi_server.models.entry_status import EntryStatus
from openapi_server.models.entry_thumb_for_api_contract import EntryThumbForApiContract
from openapi_server.models.localized_string_contract import LocalizedStringContract
from openapi_server.models.tag_usage_for_api_contract import TagUsageForApiContract
from openapi_server.models.web_link_for_api_contract import WebLinkForApiContract
from openapi_server import util


class ArtistForApiContract(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, additional_names: str=None, artist_links: List[ArtistForArtistForApiContract]=None, artist_links_reverse: List[ArtistForArtistForApiContract]=None, artist_type: ArtistType=None, base_voicebank: ArtistContract=None, create_date: datetime=None, default_name: str=None, default_name_language: ContentLanguageSelection=None, deleted: bool=None, description: str=None, id: int=None, main_picture: EntryThumbForApiContract=None, merged_to: int=None, name: str=None, names: List[LocalizedStringContract]=None, picture_mime: str=None, relations: ArtistRelationsForApi=None, release_date: datetime=None, status: EntryStatus=None, tags: List[TagUsageForApiContract]=None, version: int=None, web_links: List[WebLinkForApiContract]=None):
        """ArtistForApiContract - a model defined in OpenAPI

        :param additional_names: The additional_names of this ArtistForApiContract.
        :param artist_links: The artist_links of this ArtistForApiContract.
        :param artist_links_reverse: The artist_links_reverse of this ArtistForApiContract.
        :param artist_type: The artist_type of this ArtistForApiContract.
        :param base_voicebank: The base_voicebank of this ArtistForApiContract.
        :param create_date: The create_date of this ArtistForApiContract.
        :param default_name: The default_name of this ArtistForApiContract.
        :param default_name_language: The default_name_language of this ArtistForApiContract.
        :param deleted: The deleted of this ArtistForApiContract.
        :param description: The description of this ArtistForApiContract.
        :param id: The id of this ArtistForApiContract.
        :param main_picture: The main_picture of this ArtistForApiContract.
        :param merged_to: The merged_to of this ArtistForApiContract.
        :param name: The name of this ArtistForApiContract.
        :param names: The names of this ArtistForApiContract.
        :param picture_mime: The picture_mime of this ArtistForApiContract.
        :param relations: The relations of this ArtistForApiContract.
        :param release_date: The release_date of this ArtistForApiContract.
        :param status: The status of this ArtistForApiContract.
        :param tags: The tags of this ArtistForApiContract.
        :param version: The version of this ArtistForApiContract.
        :param web_links: The web_links of this ArtistForApiContract.
        """
        self.openapi_types = {
            'additional_names': str,
            'artist_links': List[ArtistForArtistForApiContract],
            'artist_links_reverse': List[ArtistForArtistForApiContract],
            'artist_type': ArtistType,
            'base_voicebank': ArtistContract,
            'create_date': datetime,
            'default_name': str,
            'default_name_language': ContentLanguageSelection,
            'deleted': bool,
            'description': str,
            'id': int,
            'main_picture': EntryThumbForApiContract,
            'merged_to': int,
            'name': str,
            'names': List[LocalizedStringContract],
            'picture_mime': str,
            'relations': ArtistRelationsForApi,
            'release_date': datetime,
            'status': EntryStatus,
            'tags': List[TagUsageForApiContract],
            'version': int,
            'web_links': List[WebLinkForApiContract]
        }

        self.attribute_map = {
            'additional_names': 'additionalNames',
            'artist_links': 'artistLinks',
            'artist_links_reverse': 'artistLinksReverse',
            'artist_type': 'artistType',
            'base_voicebank': 'baseVoicebank',
            'create_date': 'createDate',
            'default_name': 'defaultName',
            'default_name_language': 'defaultNameLanguage',
            'deleted': 'deleted',
            'description': 'description',
            'id': 'id',
            'main_picture': 'mainPicture',
            'merged_to': 'mergedTo',
            'name': 'name',
            'names': 'names',
            'picture_mime': 'pictureMime',
            'relations': 'relations',
            'release_date': 'releaseDate',
            'status': 'status',
            'tags': 'tags',
            'version': 'version',
            'web_links': 'webLinks'
        }

        self._additional_names = additional_names
        self._artist_links = artist_links
        self._artist_links_reverse = artist_links_reverse
        self._artist_type = artist_type
        self._base_voicebank = base_voicebank
        self._create_date = create_date
        self._default_name = default_name
        self._default_name_language = default_name_language
        self._deleted = deleted
        self._description = description
        self._id = id
        self._main_picture = main_picture
        self._merged_to = merged_to
        self._name = name
        self._names = names
        self._picture_mime = picture_mime
        self._relations = relations
        self._release_date = release_date
        self._status = status
        self._tags = tags
        self._version = version
        self._web_links = web_links

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ArtistForApiContract':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ArtistForApiContract of this ArtistForApiContract.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def additional_names(self):
        """Gets the additional_names of this ArtistForApiContract.


        :return: The additional_names of this ArtistForApiContract.
        :rtype: str
        """
        return self._additional_names

    @additional_names.setter
    def additional_names(self, additional_names):
        """Sets the additional_names of this ArtistForApiContract.


        :param additional_names: The additional_names of this ArtistForApiContract.
        :type additional_names: str
        """

        self._additional_names = additional_names

    @property
    def artist_links(self):
        """Gets the artist_links of this ArtistForApiContract.


        :return: The artist_links of this ArtistForApiContract.
        :rtype: List[ArtistForArtistForApiContract]
        """
        return self._artist_links

    @artist_links.setter
    def artist_links(self, artist_links):
        """Sets the artist_links of this ArtistForApiContract.


        :param artist_links: The artist_links of this ArtistForApiContract.
        :type artist_links: List[ArtistForArtistForApiContract]
        """

        self._artist_links = artist_links

    @property
    def artist_links_reverse(self):
        """Gets the artist_links_reverse of this ArtistForApiContract.


        :return: The artist_links_reverse of this ArtistForApiContract.
        :rtype: List[ArtistForArtistForApiContract]
        """
        return self._artist_links_reverse

    @artist_links_reverse.setter
    def artist_links_reverse(self, artist_links_reverse):
        """Sets the artist_links_reverse of this ArtistForApiContract.


        :param artist_links_reverse: The artist_links_reverse of this ArtistForApiContract.
        :type artist_links_reverse: List[ArtistForArtistForApiContract]
        """

        self._artist_links_reverse = artist_links_reverse

    @property
    def artist_type(self):
        """Gets the artist_type of this ArtistForApiContract.


        :return: The artist_type of this ArtistForApiContract.
        :rtype: ArtistType
        """
        return self._artist_type

    @artist_type.setter
    def artist_type(self, artist_type):
        """Sets the artist_type of this ArtistForApiContract.


        :param artist_type: The artist_type of this ArtistForApiContract.
        :type artist_type: ArtistType
        """

        self._artist_type = artist_type

    @property
    def base_voicebank(self):
        """Gets the base_voicebank of this ArtistForApiContract.


        :return: The base_voicebank of this ArtistForApiContract.
        :rtype: ArtistContract
        """
        return self._base_voicebank

    @base_voicebank.setter
    def base_voicebank(self, base_voicebank):
        """Sets the base_voicebank of this ArtistForApiContract.


        :param base_voicebank: The base_voicebank of this ArtistForApiContract.
        :type base_voicebank: ArtistContract
        """

        self._base_voicebank = base_voicebank

    @property
    def create_date(self):
        """Gets the create_date of this ArtistForApiContract.


        :return: The create_date of this ArtistForApiContract.
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this ArtistForApiContract.


        :param create_date: The create_date of this ArtistForApiContract.
        :type create_date: datetime
        """

        self._create_date = create_date

    @property
    def default_name(self):
        """Gets the default_name of this ArtistForApiContract.


        :return: The default_name of this ArtistForApiContract.
        :rtype: str
        """
        return self._default_name

    @default_name.setter
    def default_name(self, default_name):
        """Sets the default_name of this ArtistForApiContract.


        :param default_name: The default_name of this ArtistForApiContract.
        :type default_name: str
        """

        self._default_name = default_name

    @property
    def default_name_language(self):
        """Gets the default_name_language of this ArtistForApiContract.


        :return: The default_name_language of this ArtistForApiContract.
        :rtype: ContentLanguageSelection
        """
        return self._default_name_language

    @default_name_language.setter
    def default_name_language(self, default_name_language):
        """Sets the default_name_language of this ArtistForApiContract.


        :param default_name_language: The default_name_language of this ArtistForApiContract.
        :type default_name_language: ContentLanguageSelection
        """

        self._default_name_language = default_name_language

    @property
    def deleted(self):
        """Gets the deleted of this ArtistForApiContract.


        :return: The deleted of this ArtistForApiContract.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this ArtistForApiContract.


        :param deleted: The deleted of this ArtistForApiContract.
        :type deleted: bool
        """

        self._deleted = deleted

    @property
    def description(self):
        """Gets the description of this ArtistForApiContract.


        :return: The description of this ArtistForApiContract.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ArtistForApiContract.


        :param description: The description of this ArtistForApiContract.
        :type description: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this ArtistForApiContract.


        :return: The id of this ArtistForApiContract.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ArtistForApiContract.


        :param id: The id of this ArtistForApiContract.
        :type id: int
        """

        self._id = id

    @property
    def main_picture(self):
        """Gets the main_picture of this ArtistForApiContract.


        :return: The main_picture of this ArtistForApiContract.
        :rtype: EntryThumbForApiContract
        """
        return self._main_picture

    @main_picture.setter
    def main_picture(self, main_picture):
        """Sets the main_picture of this ArtistForApiContract.


        :param main_picture: The main_picture of this ArtistForApiContract.
        :type main_picture: EntryThumbForApiContract
        """

        self._main_picture = main_picture

    @property
    def merged_to(self):
        """Gets the merged_to of this ArtistForApiContract.


        :return: The merged_to of this ArtistForApiContract.
        :rtype: int
        """
        return self._merged_to

    @merged_to.setter
    def merged_to(self, merged_to):
        """Sets the merged_to of this ArtistForApiContract.


        :param merged_to: The merged_to of this ArtistForApiContract.
        :type merged_to: int
        """

        self._merged_to = merged_to

    @property
    def name(self):
        """Gets the name of this ArtistForApiContract.


        :return: The name of this ArtistForApiContract.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ArtistForApiContract.


        :param name: The name of this ArtistForApiContract.
        :type name: str
        """

        self._name = name

    @property
    def names(self):
        """Gets the names of this ArtistForApiContract.


        :return: The names of this ArtistForApiContract.
        :rtype: List[LocalizedStringContract]
        """
        return self._names

    @names.setter
    def names(self, names):
        """Sets the names of this ArtistForApiContract.


        :param names: The names of this ArtistForApiContract.
        :type names: List[LocalizedStringContract]
        """

        self._names = names

    @property
    def picture_mime(self):
        """Gets the picture_mime of this ArtistForApiContract.


        :return: The picture_mime of this ArtistForApiContract.
        :rtype: str
        """
        return self._picture_mime

    @picture_mime.setter
    def picture_mime(self, picture_mime):
        """Sets the picture_mime of this ArtistForApiContract.


        :param picture_mime: The picture_mime of this ArtistForApiContract.
        :type picture_mime: str
        """

        self._picture_mime = picture_mime

    @property
    def relations(self):
        """Gets the relations of this ArtistForApiContract.


        :return: The relations of this ArtistForApiContract.
        :rtype: ArtistRelationsForApi
        """
        return self._relations

    @relations.setter
    def relations(self, relations):
        """Sets the relations of this ArtistForApiContract.


        :param relations: The relations of this ArtistForApiContract.
        :type relations: ArtistRelationsForApi
        """

        self._relations = relations

    @property
    def release_date(self):
        """Gets the release_date of this ArtistForApiContract.


        :return: The release_date of this ArtistForApiContract.
        :rtype: datetime
        """
        return self._release_date

    @release_date.setter
    def release_date(self, release_date):
        """Sets the release_date of this ArtistForApiContract.


        :param release_date: The release_date of this ArtistForApiContract.
        :type release_date: datetime
        """

        self._release_date = release_date

    @property
    def status(self):
        """Gets the status of this ArtistForApiContract.


        :return: The status of this ArtistForApiContract.
        :rtype: EntryStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ArtistForApiContract.


        :param status: The status of this ArtistForApiContract.
        :type status: EntryStatus
        """

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this ArtistForApiContract.


        :return: The tags of this ArtistForApiContract.
        :rtype: List[TagUsageForApiContract]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ArtistForApiContract.


        :param tags: The tags of this ArtistForApiContract.
        :type tags: List[TagUsageForApiContract]
        """

        self._tags = tags

    @property
    def version(self):
        """Gets the version of this ArtistForApiContract.


        :return: The version of this ArtistForApiContract.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ArtistForApiContract.


        :param version: The version of this ArtistForApiContract.
        :type version: int
        """

        self._version = version

    @property
    def web_links(self):
        """Gets the web_links of this ArtistForApiContract.


        :return: The web_links of this ArtistForApiContract.
        :rtype: List[WebLinkForApiContract]
        """
        return self._web_links

    @web_links.setter
    def web_links(self, web_links):
        """Sets the web_links of this ArtistForApiContract.


        :param web_links: The web_links of this ArtistForApiContract.
        :type web_links: List[WebLinkForApiContract]
        """

        self._web_links = web_links
