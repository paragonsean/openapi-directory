# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.artifact import Artifact
from openapi_server.models.definition_templates import DefinitionTemplates
from openapi_server.models.filter import Filter
from openapi_server.models.gallery_item_properties_icon_file_uris import GalleryItemPropertiesIconFileUris
from openapi_server.models.image_group import ImageGroup
from openapi_server.models.link_properties import LinkProperties
from openapi_server.models.marketing_material import MarketingMaterial
from openapi_server.models.open_property import OpenProperty
from openapi_server.models.product import Product
from openapi_server import util


class GalleryItemProperties(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, additional_properties: Dict[str, str]=None, artifacts: List[Artifact]=None, category_ids: List[str]=None, changed_time: datetime=None, created_time: datetime=None, definition_templates: DefinitionTemplates=None, description: str=None, filters: List[Filter]=None, icon_file_uris: GalleryItemPropertiesIconFileUris=None, identity: str=None, images: List[ImageGroup]=None, item_display_name: str=None, item_name: str=None, item_type: str=None, links: List[LinkProperties]=None, long_summary: str=None, marketing_material: MarketingMaterial=None, metadata: OpenProperty=None, products: List[Product]=None, properties: Dict[str, str]=None, publisher: str=None, publisher_display_name: str=None, resource_group_name: str=None, screenshot_uris: List[str]=None, summary: str=None, ui_definition_uri: str=None, version: str=None):
        """GalleryItemProperties - a model defined in OpenAPI

        :param additional_properties: The additional_properties of this GalleryItemProperties.
        :param artifacts: The artifacts of this GalleryItemProperties.
        :param category_ids: The category_ids of this GalleryItemProperties.
        :param changed_time: The changed_time of this GalleryItemProperties.
        :param created_time: The created_time of this GalleryItemProperties.
        :param definition_templates: The definition_templates of this GalleryItemProperties.
        :param description: The description of this GalleryItemProperties.
        :param filters: The filters of this GalleryItemProperties.
        :param icon_file_uris: The icon_file_uris of this GalleryItemProperties.
        :param identity: The identity of this GalleryItemProperties.
        :param images: The images of this GalleryItemProperties.
        :param item_display_name: The item_display_name of this GalleryItemProperties.
        :param item_name: The item_name of this GalleryItemProperties.
        :param item_type: The item_type of this GalleryItemProperties.
        :param links: The links of this GalleryItemProperties.
        :param long_summary: The long_summary of this GalleryItemProperties.
        :param marketing_material: The marketing_material of this GalleryItemProperties.
        :param metadata: The metadata of this GalleryItemProperties.
        :param products: The products of this GalleryItemProperties.
        :param properties: The properties of this GalleryItemProperties.
        :param publisher: The publisher of this GalleryItemProperties.
        :param publisher_display_name: The publisher_display_name of this GalleryItemProperties.
        :param resource_group_name: The resource_group_name of this GalleryItemProperties.
        :param screenshot_uris: The screenshot_uris of this GalleryItemProperties.
        :param summary: The summary of this GalleryItemProperties.
        :param ui_definition_uri: The ui_definition_uri of this GalleryItemProperties.
        :param version: The version of this GalleryItemProperties.
        """
        self.openapi_types = {
            'additional_properties': Dict[str, str],
            'artifacts': List[Artifact],
            'category_ids': List[str],
            'changed_time': datetime,
            'created_time': datetime,
            'definition_templates': DefinitionTemplates,
            'description': str,
            'filters': List[Filter],
            'icon_file_uris': GalleryItemPropertiesIconFileUris,
            'identity': str,
            'images': List[ImageGroup],
            'item_display_name': str,
            'item_name': str,
            'item_type': str,
            'links': List[LinkProperties],
            'long_summary': str,
            'marketing_material': MarketingMaterial,
            'metadata': OpenProperty,
            'products': List[Product],
            'properties': Dict[str, str],
            'publisher': str,
            'publisher_display_name': str,
            'resource_group_name': str,
            'screenshot_uris': List[str],
            'summary': str,
            'ui_definition_uri': str,
            'version': str
        }

        self.attribute_map = {
            'additional_properties': 'additionalProperties',
            'artifacts': 'artifacts',
            'category_ids': 'categoryIds',
            'changed_time': 'changedTime',
            'created_time': 'createdTime',
            'definition_templates': 'definitionTemplates',
            'description': 'description',
            'filters': 'filters',
            'icon_file_uris': 'iconFileUris',
            'identity': 'identity',
            'images': 'images',
            'item_display_name': 'itemDisplayName',
            'item_name': 'itemName',
            'item_type': 'itemType',
            'links': 'links',
            'long_summary': 'longSummary',
            'marketing_material': 'marketingMaterial',
            'metadata': 'metadata',
            'products': 'products',
            'properties': 'properties',
            'publisher': 'publisher',
            'publisher_display_name': 'publisherDisplayName',
            'resource_group_name': 'resourceGroupName',
            'screenshot_uris': 'screenshotUris',
            'summary': 'summary',
            'ui_definition_uri': 'uiDefinitionUri',
            'version': 'version'
        }

        self._additional_properties = additional_properties
        self._artifacts = artifacts
        self._category_ids = category_ids
        self._changed_time = changed_time
        self._created_time = created_time
        self._definition_templates = definition_templates
        self._description = description
        self._filters = filters
        self._icon_file_uris = icon_file_uris
        self._identity = identity
        self._images = images
        self._item_display_name = item_display_name
        self._item_name = item_name
        self._item_type = item_type
        self._links = links
        self._long_summary = long_summary
        self._marketing_material = marketing_material
        self._metadata = metadata
        self._products = products
        self._properties = properties
        self._publisher = publisher
        self._publisher_display_name = publisher_display_name
        self._resource_group_name = resource_group_name
        self._screenshot_uris = screenshot_uris
        self._summary = summary
        self._ui_definition_uri = ui_definition_uri
        self._version = version

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GalleryItemProperties':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The GalleryItemProperties of this GalleryItemProperties.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def additional_properties(self):
        """Gets the additional_properties of this GalleryItemProperties.

        List of additional properties provided for the item.

        :return: The additional_properties of this GalleryItemProperties.
        :rtype: Dict[str, str]
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """Sets the additional_properties of this GalleryItemProperties.

        List of additional properties provided for the item.

        :param additional_properties: The additional_properties of this GalleryItemProperties.
        :type additional_properties: Dict[str, str]
        """

        self._additional_properties = additional_properties

    @property
    def artifacts(self):
        """Gets the artifacts of this GalleryItemProperties.

        List of artifacts for the gallery item.

        :return: The artifacts of this GalleryItemProperties.
        :rtype: List[Artifact]
        """
        return self._artifacts

    @artifacts.setter
    def artifacts(self, artifacts):
        """Sets the artifacts of this GalleryItemProperties.

        List of artifacts for the gallery item.

        :param artifacts: The artifacts of this GalleryItemProperties.
        :type artifacts: List[Artifact]
        """

        self._artifacts = artifacts

    @property
    def category_ids(self):
        """Gets the category_ids of this GalleryItemProperties.

        List of category IDs the gallery item belongs to.

        :return: The category_ids of this GalleryItemProperties.
        :rtype: List[str]
        """
        return self._category_ids

    @category_ids.setter
    def category_ids(self, category_ids):
        """Sets the category_ids of this GalleryItemProperties.

        List of category IDs the gallery item belongs to.

        :param category_ids: The category_ids of this GalleryItemProperties.
        :type category_ids: List[str]
        """

        self._category_ids = category_ids

    @property
    def changed_time(self):
        """Gets the changed_time of this GalleryItemProperties.

        Last update time of gallery item.

        :return: The changed_time of this GalleryItemProperties.
        :rtype: datetime
        """
        return self._changed_time

    @changed_time.setter
    def changed_time(self, changed_time):
        """Sets the changed_time of this GalleryItemProperties.

        Last update time of gallery item.

        :param changed_time: The changed_time of this GalleryItemProperties.
        :type changed_time: datetime
        """

        self._changed_time = changed_time

    @property
    def created_time(self):
        """Gets the created_time of this GalleryItemProperties.

        The date and time that the gallery item was created.

        :return: The created_time of this GalleryItemProperties.
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this GalleryItemProperties.

        The date and time that the gallery item was created.

        :param created_time: The created_time of this GalleryItemProperties.
        :type created_time: datetime
        """

        self._created_time = created_time

    @property
    def definition_templates(self):
        """Gets the definition_templates of this GalleryItemProperties.


        :return: The definition_templates of this GalleryItemProperties.
        :rtype: DefinitionTemplates
        """
        return self._definition_templates

    @definition_templates.setter
    def definition_templates(self, definition_templates):
        """Sets the definition_templates of this GalleryItemProperties.


        :param definition_templates: The definition_templates of this GalleryItemProperties.
        :type definition_templates: DefinitionTemplates
        """

        self._definition_templates = definition_templates

    @property
    def description(self):
        """Gets the description of this GalleryItemProperties.

        The description of the gallery item.

        :return: The description of this GalleryItemProperties.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GalleryItemProperties.

        The description of the gallery item.

        :param description: The description of this GalleryItemProperties.
        :type description: str
        """

        self._description = description

    @property
    def filters(self):
        """Gets the filters of this GalleryItemProperties.

        List of filters for the gallery item.

        :return: The filters of this GalleryItemProperties.
        :rtype: List[Filter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this GalleryItemProperties.

        List of filters for the gallery item.

        :param filters: The filters of this GalleryItemProperties.
        :type filters: List[Filter]
        """

        self._filters = filters

    @property
    def icon_file_uris(self):
        """Gets the icon_file_uris of this GalleryItemProperties.


        :return: The icon_file_uris of this GalleryItemProperties.
        :rtype: GalleryItemPropertiesIconFileUris
        """
        return self._icon_file_uris

    @icon_file_uris.setter
    def icon_file_uris(self, icon_file_uris):
        """Sets the icon_file_uris of this GalleryItemProperties.


        :param icon_file_uris: The icon_file_uris of this GalleryItemProperties.
        :type icon_file_uris: GalleryItemPropertiesIconFileUris
        """

        self._icon_file_uris = icon_file_uris

    @property
    def identity(self):
        """Gets the identity of this GalleryItemProperties.

        Identity of the gallery item.

        :return: The identity of this GalleryItemProperties.
        :rtype: str
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """Sets the identity of this GalleryItemProperties.

        Identity of the gallery item.

        :param identity: The identity of this GalleryItemProperties.
        :type identity: str
        """

        self._identity = identity

    @property
    def images(self):
        """Gets the images of this GalleryItemProperties.

        List of images.

        :return: The images of this GalleryItemProperties.
        :rtype: List[ImageGroup]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this GalleryItemProperties.

        List of images.

        :param images: The images of this GalleryItemProperties.
        :type images: List[ImageGroup]
        """

        self._images = images

    @property
    def item_display_name(self):
        """Gets the item_display_name of this GalleryItemProperties.

        Displayed name in the portal.

        :return: The item_display_name of this GalleryItemProperties.
        :rtype: str
        """
        return self._item_display_name

    @item_display_name.setter
    def item_display_name(self, item_display_name):
        """Sets the item_display_name of this GalleryItemProperties.

        Displayed name in the portal.

        :param item_display_name: The item_display_name of this GalleryItemProperties.
        :type item_display_name: str
        """

        self._item_display_name = item_display_name

    @property
    def item_name(self):
        """Gets the item_name of this GalleryItemProperties.

        The display name for the gallery item, for the locale of the request.

        :return: The item_name of this GalleryItemProperties.
        :rtype: str
        """
        return self._item_name

    @item_name.setter
    def item_name(self, item_name):
        """Sets the item_name of this GalleryItemProperties.

        The display name for the gallery item, for the locale of the request.

        :param item_name: The item_name of this GalleryItemProperties.
        :type item_name: str
        """

        self._item_name = item_name

    @property
    def item_type(self):
        """Gets the item_type of this GalleryItemProperties.

        Describes the type of the gallery item, either GalleryItem or ItemGroup.

        :return: The item_type of this GalleryItemProperties.
        :rtype: str
        """
        return self._item_type

    @item_type.setter
    def item_type(self, item_type):
        """Sets the item_type of this GalleryItemProperties.

        Describes the type of the gallery item, either GalleryItem or ItemGroup.

        :param item_type: The item_type of this GalleryItemProperties.
        :type item_type: str
        """
        allowed_values = ["GalleryItem", "ItemGroup"]  # noqa: E501
        if item_type not in allowed_values:
            raise ValueError(
                "Invalid value for `item_type` ({0}), must be one of {1}"
                .format(item_type, allowed_values)
            )

        self._item_type = item_type

    @property
    def links(self):
        """Gets the links of this GalleryItemProperties.

        Links provided for the item.

        :return: The links of this GalleryItemProperties.
        :rtype: List[LinkProperties]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this GalleryItemProperties.

        Links provided for the item.

        :param links: The links of this GalleryItemProperties.
        :type links: List[LinkProperties]
        """

        self._links = links

    @property
    def long_summary(self):
        """Gets the long_summary of this GalleryItemProperties.

        Long summary of the gallery item.

        :return: The long_summary of this GalleryItemProperties.
        :rtype: str
        """
        return self._long_summary

    @long_summary.setter
    def long_summary(self, long_summary):
        """Sets the long_summary of this GalleryItemProperties.

        Long summary of the gallery item.

        :param long_summary: The long_summary of this GalleryItemProperties.
        :type long_summary: str
        """

        self._long_summary = long_summary

    @property
    def marketing_material(self):
        """Gets the marketing_material of this GalleryItemProperties.


        :return: The marketing_material of this GalleryItemProperties.
        :rtype: MarketingMaterial
        """
        return self._marketing_material

    @marketing_material.setter
    def marketing_material(self, marketing_material):
        """Sets the marketing_material of this GalleryItemProperties.


        :param marketing_material: The marketing_material of this GalleryItemProperties.
        :type marketing_material: MarketingMaterial
        """

        self._marketing_material = marketing_material

    @property
    def metadata(self):
        """Gets the metadata of this GalleryItemProperties.


        :return: The metadata of this GalleryItemProperties.
        :rtype: OpenProperty
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this GalleryItemProperties.


        :param metadata: The metadata of this GalleryItemProperties.
        :type metadata: OpenProperty
        """

        self._metadata = metadata

    @property
    def products(self):
        """Gets the products of this GalleryItemProperties.

        List of products.

        :return: The products of this GalleryItemProperties.
        :rtype: List[Product]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this GalleryItemProperties.

        List of products.

        :param products: The products of this GalleryItemProperties.
        :type products: List[Product]
        """

        self._products = products

    @property
    def properties(self):
        """Gets the properties of this GalleryItemProperties.

        List of properties provided for the gallery item.

        :return: The properties of this GalleryItemProperties.
        :rtype: Dict[str, str]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this GalleryItemProperties.

        List of properties provided for the gallery item.

        :param properties: The properties of this GalleryItemProperties.
        :type properties: Dict[str, str]
        """

        self._properties = properties

    @property
    def publisher(self):
        """Gets the publisher of this GalleryItemProperties.

        The publisher of the gallery item.

        :return: The publisher of this GalleryItemProperties.
        :rtype: str
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this GalleryItemProperties.

        The publisher of the gallery item.

        :param publisher: The publisher of this GalleryItemProperties.
        :type publisher: str
        """

        self._publisher = publisher

    @property
    def publisher_display_name(self):
        """Gets the publisher_display_name of this GalleryItemProperties.

        Display name of the publisher.

        :return: The publisher_display_name of this GalleryItemProperties.
        :rtype: str
        """
        return self._publisher_display_name

    @publisher_display_name.setter
    def publisher_display_name(self, publisher_display_name):
        """Sets the publisher_display_name of this GalleryItemProperties.

        Display name of the publisher.

        :param publisher_display_name: The publisher_display_name of this GalleryItemProperties.
        :type publisher_display_name: str
        """

        self._publisher_display_name = publisher_display_name

    @property
    def resource_group_name(self):
        """Gets the resource_group_name of this GalleryItemProperties.

        Resource group name the gallery item belongs too.

        :return: The resource_group_name of this GalleryItemProperties.
        :rtype: str
        """
        return self._resource_group_name

    @resource_group_name.setter
    def resource_group_name(self, resource_group_name):
        """Sets the resource_group_name of this GalleryItemProperties.

        Resource group name the gallery item belongs too.

        :param resource_group_name: The resource_group_name of this GalleryItemProperties.
        :type resource_group_name: str
        """

        self._resource_group_name = resource_group_name

    @property
    def screenshot_uris(self):
        """Gets the screenshot_uris of this GalleryItemProperties.

        List of screenshot image URIs provided for the item.

        :return: The screenshot_uris of this GalleryItemProperties.
        :rtype: List[str]
        """
        return self._screenshot_uris

    @screenshot_uris.setter
    def screenshot_uris(self, screenshot_uris):
        """Sets the screenshot_uris of this GalleryItemProperties.

        List of screenshot image URIs provided for the item.

        :param screenshot_uris: The screenshot_uris of this GalleryItemProperties.
        :type screenshot_uris: List[str]
        """

        self._screenshot_uris = screenshot_uris

    @property
    def summary(self):
        """Gets the summary of this GalleryItemProperties.

        Short summary of the gallery item.

        :return: The summary of this GalleryItemProperties.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this GalleryItemProperties.

        Short summary of the gallery item.

        :param summary: The summary of this GalleryItemProperties.
        :type summary: str
        """

        self._summary = summary

    @property
    def ui_definition_uri(self):
        """Gets the ui_definition_uri of this GalleryItemProperties.

        The URL of the view definition object that defines the UI information that is used when an instance of the gallery item resource definition is created.

        :return: The ui_definition_uri of this GalleryItemProperties.
        :rtype: str
        """
        return self._ui_definition_uri

    @ui_definition_uri.setter
    def ui_definition_uri(self, ui_definition_uri):
        """Sets the ui_definition_uri of this GalleryItemProperties.

        The URL of the view definition object that defines the UI information that is used when an instance of the gallery item resource definition is created.

        :param ui_definition_uri: The ui_definition_uri of this GalleryItemProperties.
        :type ui_definition_uri: str
        """

        self._ui_definition_uri = ui_definition_uri

    @property
    def version(self):
        """Gets the version of this GalleryItemProperties.

        The version identifier of the gallery item, in Major.Minor.Build format.

        :return: The version of this GalleryItemProperties.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this GalleryItemProperties.

        The version identifier of the gallery item, in Major.Minor.Build format.

        :param version: The version of this GalleryItemProperties.
        :type version: str
        """

        self._version = version
