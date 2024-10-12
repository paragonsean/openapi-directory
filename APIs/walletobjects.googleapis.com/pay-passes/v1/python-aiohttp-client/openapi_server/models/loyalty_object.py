# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.app_link_data import AppLinkData
from openapi_server.models.barcode import Barcode
from openapi_server.models.grouping_info import GroupingInfo
from openapi_server.models.image import Image
from openapi_server.models.image_module_data import ImageModuleData
from openapi_server.models.info_module_data import InfoModuleData
from openapi_server.models.lat_long_point import LatLongPoint
from openapi_server.models.links_module_data import LinksModuleData
from openapi_server.models.loyalty_class import LoyaltyClass
from openapi_server.models.loyalty_points import LoyaltyPoints
from openapi_server.models.message import Message
from openapi_server.models.pass_constraints import PassConstraints
from openapi_server.models.rotating_barcode import RotatingBarcode
from openapi_server.models.text_module_data import TextModuleData
from openapi_server.models.time_interval import TimeInterval
from openapi_server import util


class LoyaltyObject(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, account_id: str=None, account_name: str=None, app_link_data: AppLinkData=None, barcode: Barcode=None, class_id: str=None, class_reference: LoyaltyClass=None, disable_expiration_notification: bool=None, grouping_info: GroupingInfo=None, has_linked_device: bool=None, has_users: bool=None, hero_image: Image=None, id: str=None, image_modules_data: List[ImageModuleData]=None, info_module_data: InfoModuleData=None, kind: str=None, linked_offer_ids: List[str]=None, links_module_data: LinksModuleData=None, locations: List[LatLongPoint]=None, loyalty_points: LoyaltyPoints=None, messages: List[Message]=None, pass_constraints: PassConstraints=None, rotating_barcode: RotatingBarcode=None, secondary_loyalty_points: LoyaltyPoints=None, smart_tap_redemption_value: str=None, state: str=None, text_modules_data: List[TextModuleData]=None, valid_time_interval: TimeInterval=None, version: str=None):
        """LoyaltyObject - a model defined in OpenAPI

        :param account_id: The account_id of this LoyaltyObject.
        :param account_name: The account_name of this LoyaltyObject.
        :param app_link_data: The app_link_data of this LoyaltyObject.
        :param barcode: The barcode of this LoyaltyObject.
        :param class_id: The class_id of this LoyaltyObject.
        :param class_reference: The class_reference of this LoyaltyObject.
        :param disable_expiration_notification: The disable_expiration_notification of this LoyaltyObject.
        :param grouping_info: The grouping_info of this LoyaltyObject.
        :param has_linked_device: The has_linked_device of this LoyaltyObject.
        :param has_users: The has_users of this LoyaltyObject.
        :param hero_image: The hero_image of this LoyaltyObject.
        :param id: The id of this LoyaltyObject.
        :param image_modules_data: The image_modules_data of this LoyaltyObject.
        :param info_module_data: The info_module_data of this LoyaltyObject.
        :param kind: The kind of this LoyaltyObject.
        :param linked_offer_ids: The linked_offer_ids of this LoyaltyObject.
        :param links_module_data: The links_module_data of this LoyaltyObject.
        :param locations: The locations of this LoyaltyObject.
        :param loyalty_points: The loyalty_points of this LoyaltyObject.
        :param messages: The messages of this LoyaltyObject.
        :param pass_constraints: The pass_constraints of this LoyaltyObject.
        :param rotating_barcode: The rotating_barcode of this LoyaltyObject.
        :param secondary_loyalty_points: The secondary_loyalty_points of this LoyaltyObject.
        :param smart_tap_redemption_value: The smart_tap_redemption_value of this LoyaltyObject.
        :param state: The state of this LoyaltyObject.
        :param text_modules_data: The text_modules_data of this LoyaltyObject.
        :param valid_time_interval: The valid_time_interval of this LoyaltyObject.
        :param version: The version of this LoyaltyObject.
        """
        self.openapi_types = {
            'account_id': str,
            'account_name': str,
            'app_link_data': AppLinkData,
            'barcode': Barcode,
            'class_id': str,
            'class_reference': LoyaltyClass,
            'disable_expiration_notification': bool,
            'grouping_info': GroupingInfo,
            'has_linked_device': bool,
            'has_users': bool,
            'hero_image': Image,
            'id': str,
            'image_modules_data': List[ImageModuleData],
            'info_module_data': InfoModuleData,
            'kind': str,
            'linked_offer_ids': List[str],
            'links_module_data': LinksModuleData,
            'locations': List[LatLongPoint],
            'loyalty_points': LoyaltyPoints,
            'messages': List[Message],
            'pass_constraints': PassConstraints,
            'rotating_barcode': RotatingBarcode,
            'secondary_loyalty_points': LoyaltyPoints,
            'smart_tap_redemption_value': str,
            'state': str,
            'text_modules_data': List[TextModuleData],
            'valid_time_interval': TimeInterval,
            'version': str
        }

        self.attribute_map = {
            'account_id': 'accountId',
            'account_name': 'accountName',
            'app_link_data': 'appLinkData',
            'barcode': 'barcode',
            'class_id': 'classId',
            'class_reference': 'classReference',
            'disable_expiration_notification': 'disableExpirationNotification',
            'grouping_info': 'groupingInfo',
            'has_linked_device': 'hasLinkedDevice',
            'has_users': 'hasUsers',
            'hero_image': 'heroImage',
            'id': 'id',
            'image_modules_data': 'imageModulesData',
            'info_module_data': 'infoModuleData',
            'kind': 'kind',
            'linked_offer_ids': 'linkedOfferIds',
            'links_module_data': 'linksModuleData',
            'locations': 'locations',
            'loyalty_points': 'loyaltyPoints',
            'messages': 'messages',
            'pass_constraints': 'passConstraints',
            'rotating_barcode': 'rotatingBarcode',
            'secondary_loyalty_points': 'secondaryLoyaltyPoints',
            'smart_tap_redemption_value': 'smartTapRedemptionValue',
            'state': 'state',
            'text_modules_data': 'textModulesData',
            'valid_time_interval': 'validTimeInterval',
            'version': 'version'
        }

        self._account_id = account_id
        self._account_name = account_name
        self._app_link_data = app_link_data
        self._barcode = barcode
        self._class_id = class_id
        self._class_reference = class_reference
        self._disable_expiration_notification = disable_expiration_notification
        self._grouping_info = grouping_info
        self._has_linked_device = has_linked_device
        self._has_users = has_users
        self._hero_image = hero_image
        self._id = id
        self._image_modules_data = image_modules_data
        self._info_module_data = info_module_data
        self._kind = kind
        self._linked_offer_ids = linked_offer_ids
        self._links_module_data = links_module_data
        self._locations = locations
        self._loyalty_points = loyalty_points
        self._messages = messages
        self._pass_constraints = pass_constraints
        self._rotating_barcode = rotating_barcode
        self._secondary_loyalty_points = secondary_loyalty_points
        self._smart_tap_redemption_value = smart_tap_redemption_value
        self._state = state
        self._text_modules_data = text_modules_data
        self._valid_time_interval = valid_time_interval
        self._version = version

    @classmethod
    def from_dict(cls, dikt: dict) -> 'LoyaltyObject':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The LoyaltyObject of this LoyaltyObject.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def account_id(self):
        """Gets the account_id of this LoyaltyObject.

        The loyalty account identifier. Recommended maximum length is 20 characters.

        :return: The account_id of this LoyaltyObject.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this LoyaltyObject.

        The loyalty account identifier. Recommended maximum length is 20 characters.

        :param account_id: The account_id of this LoyaltyObject.
        :type account_id: str
        """

        self._account_id = account_id

    @property
    def account_name(self):
        """Gets the account_name of this LoyaltyObject.

        The loyalty account holder name, such as \"John Smith.\" Recommended maximum length is 20 characters to ensure full string is displayed on smaller screens.

        :return: The account_name of this LoyaltyObject.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this LoyaltyObject.

        The loyalty account holder name, such as \"John Smith.\" Recommended maximum length is 20 characters to ensure full string is displayed on smaller screens.

        :param account_name: The account_name of this LoyaltyObject.
        :type account_name: str
        """

        self._account_name = account_name

    @property
    def app_link_data(self):
        """Gets the app_link_data of this LoyaltyObject.


        :return: The app_link_data of this LoyaltyObject.
        :rtype: AppLinkData
        """
        return self._app_link_data

    @app_link_data.setter
    def app_link_data(self, app_link_data):
        """Sets the app_link_data of this LoyaltyObject.


        :param app_link_data: The app_link_data of this LoyaltyObject.
        :type app_link_data: AppLinkData
        """

        self._app_link_data = app_link_data

    @property
    def barcode(self):
        """Gets the barcode of this LoyaltyObject.


        :return: The barcode of this LoyaltyObject.
        :rtype: Barcode
        """
        return self._barcode

    @barcode.setter
    def barcode(self, barcode):
        """Sets the barcode of this LoyaltyObject.


        :param barcode: The barcode of this LoyaltyObject.
        :type barcode: Barcode
        """

        self._barcode = barcode

    @property
    def class_id(self):
        """Gets the class_id of this LoyaltyObject.

        Required. The class associated with this object. The class must be of the same type as this object, must already exist, and must be approved. Class IDs should follow the format issuer ID.identifier where the former is issued by Google and latter is chosen by you.

        :return: The class_id of this LoyaltyObject.
        :rtype: str
        """
        return self._class_id

    @class_id.setter
    def class_id(self, class_id):
        """Sets the class_id of this LoyaltyObject.

        Required. The class associated with this object. The class must be of the same type as this object, must already exist, and must be approved. Class IDs should follow the format issuer ID.identifier where the former is issued by Google and latter is chosen by you.

        :param class_id: The class_id of this LoyaltyObject.
        :type class_id: str
        """

        self._class_id = class_id

    @property
    def class_reference(self):
        """Gets the class_reference of this LoyaltyObject.


        :return: The class_reference of this LoyaltyObject.
        :rtype: LoyaltyClass
        """
        return self._class_reference

    @class_reference.setter
    def class_reference(self, class_reference):
        """Sets the class_reference of this LoyaltyObject.


        :param class_reference: The class_reference of this LoyaltyObject.
        :type class_reference: LoyaltyClass
        """

        self._class_reference = class_reference

    @property
    def disable_expiration_notification(self):
        """Gets the disable_expiration_notification of this LoyaltyObject.

        Indicates if notifications should explicitly be suppressed. If this field is set to true, regardless of the `messages` field, expiration notifications to the user will be suppressed. By default, this field is set to false. Currently, this can only be set for offers.

        :return: The disable_expiration_notification of this LoyaltyObject.
        :rtype: bool
        """
        return self._disable_expiration_notification

    @disable_expiration_notification.setter
    def disable_expiration_notification(self, disable_expiration_notification):
        """Sets the disable_expiration_notification of this LoyaltyObject.

        Indicates if notifications should explicitly be suppressed. If this field is set to true, regardless of the `messages` field, expiration notifications to the user will be suppressed. By default, this field is set to false. Currently, this can only be set for offers.

        :param disable_expiration_notification: The disable_expiration_notification of this LoyaltyObject.
        :type disable_expiration_notification: bool
        """

        self._disable_expiration_notification = disable_expiration_notification

    @property
    def grouping_info(self):
        """Gets the grouping_info of this LoyaltyObject.


        :return: The grouping_info of this LoyaltyObject.
        :rtype: GroupingInfo
        """
        return self._grouping_info

    @grouping_info.setter
    def grouping_info(self, grouping_info):
        """Sets the grouping_info of this LoyaltyObject.


        :param grouping_info: The grouping_info of this LoyaltyObject.
        :type grouping_info: GroupingInfo
        """

        self._grouping_info = grouping_info

    @property
    def has_linked_device(self):
        """Gets the has_linked_device of this LoyaltyObject.

        Whether this object is currently linked to a single device. This field is set by the platform when a user saves the object, linking it to their device. Intended for use by select partners. Contact support for additional information.

        :return: The has_linked_device of this LoyaltyObject.
        :rtype: bool
        """
        return self._has_linked_device

    @has_linked_device.setter
    def has_linked_device(self, has_linked_device):
        """Sets the has_linked_device of this LoyaltyObject.

        Whether this object is currently linked to a single device. This field is set by the platform when a user saves the object, linking it to their device. Intended for use by select partners. Contact support for additional information.

        :param has_linked_device: The has_linked_device of this LoyaltyObject.
        :type has_linked_device: bool
        """

        self._has_linked_device = has_linked_device

    @property
    def has_users(self):
        """Gets the has_users of this LoyaltyObject.

        Indicates if the object has users. This field is set by the platform.

        :return: The has_users of this LoyaltyObject.
        :rtype: bool
        """
        return self._has_users

    @has_users.setter
    def has_users(self, has_users):
        """Sets the has_users of this LoyaltyObject.

        Indicates if the object has users. This field is set by the platform.

        :param has_users: The has_users of this LoyaltyObject.
        :type has_users: bool
        """

        self._has_users = has_users

    @property
    def hero_image(self):
        """Gets the hero_image of this LoyaltyObject.


        :return: The hero_image of this LoyaltyObject.
        :rtype: Image
        """
        return self._hero_image

    @hero_image.setter
    def hero_image(self, hero_image):
        """Sets the hero_image of this LoyaltyObject.


        :param hero_image: The hero_image of this LoyaltyObject.
        :type hero_image: Image
        """

        self._hero_image = hero_image

    @property
    def id(self):
        """Gets the id of this LoyaltyObject.

        Required. The unique identifier for an object. This ID must be unique across all objects from an issuer. This value should follow the format issuer ID.identifier where the former is issued by Google and latter is chosen by you. The unique identifier should only include alphanumeric characters, '.', '_', or '-'.

        :return: The id of this LoyaltyObject.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LoyaltyObject.

        Required. The unique identifier for an object. This ID must be unique across all objects from an issuer. This value should follow the format issuer ID.identifier where the former is issued by Google and latter is chosen by you. The unique identifier should only include alphanumeric characters, '.', '_', or '-'.

        :param id: The id of this LoyaltyObject.
        :type id: str
        """

        self._id = id

    @property
    def image_modules_data(self):
        """Gets the image_modules_data of this LoyaltyObject.

        Image module data. The maximum number of these fields displayed is 1 from object level and 1 for class object level.

        :return: The image_modules_data of this LoyaltyObject.
        :rtype: List[ImageModuleData]
        """
        return self._image_modules_data

    @image_modules_data.setter
    def image_modules_data(self, image_modules_data):
        """Sets the image_modules_data of this LoyaltyObject.

        Image module data. The maximum number of these fields displayed is 1 from object level and 1 for class object level.

        :param image_modules_data: The image_modules_data of this LoyaltyObject.
        :type image_modules_data: List[ImageModuleData]
        """

        self._image_modules_data = image_modules_data

    @property
    def info_module_data(self):
        """Gets the info_module_data of this LoyaltyObject.


        :return: The info_module_data of this LoyaltyObject.
        :rtype: InfoModuleData
        """
        return self._info_module_data

    @info_module_data.setter
    def info_module_data(self, info_module_data):
        """Sets the info_module_data of this LoyaltyObject.


        :param info_module_data: The info_module_data of this LoyaltyObject.
        :type info_module_data: InfoModuleData
        """

        self._info_module_data = info_module_data

    @property
    def kind(self):
        """Gets the kind of this LoyaltyObject.

        Identifies what kind of resource this is. Value: the fixed string `\"walletobjects#loyaltyObject\"`.

        :return: The kind of this LoyaltyObject.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this LoyaltyObject.

        Identifies what kind of resource this is. Value: the fixed string `\"walletobjects#loyaltyObject\"`.

        :param kind: The kind of this LoyaltyObject.
        :type kind: str
        """

        self._kind = kind

    @property
    def linked_offer_ids(self):
        """Gets the linked_offer_ids of this LoyaltyObject.

        A list of offer objects linked to this loyalty card. The offer objects must already exist. Offer object IDs should follow the format issuer ID. identifier where the former is issued by Google and latter is chosen by you.

        :return: The linked_offer_ids of this LoyaltyObject.
        :rtype: List[str]
        """
        return self._linked_offer_ids

    @linked_offer_ids.setter
    def linked_offer_ids(self, linked_offer_ids):
        """Sets the linked_offer_ids of this LoyaltyObject.

        A list of offer objects linked to this loyalty card. The offer objects must already exist. Offer object IDs should follow the format issuer ID. identifier where the former is issued by Google and latter is chosen by you.

        :param linked_offer_ids: The linked_offer_ids of this LoyaltyObject.
        :type linked_offer_ids: List[str]
        """

        self._linked_offer_ids = linked_offer_ids

    @property
    def links_module_data(self):
        """Gets the links_module_data of this LoyaltyObject.


        :return: The links_module_data of this LoyaltyObject.
        :rtype: LinksModuleData
        """
        return self._links_module_data

    @links_module_data.setter
    def links_module_data(self, links_module_data):
        """Sets the links_module_data of this LoyaltyObject.


        :param links_module_data: The links_module_data of this LoyaltyObject.
        :type links_module_data: LinksModuleData
        """

        self._links_module_data = links_module_data

    @property
    def locations(self):
        """Gets the locations of this LoyaltyObject.

        Note: This field is currently not supported to trigger geo notifications.

        :return: The locations of this LoyaltyObject.
        :rtype: List[LatLongPoint]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """Sets the locations of this LoyaltyObject.

        Note: This field is currently not supported to trigger geo notifications.

        :param locations: The locations of this LoyaltyObject.
        :type locations: List[LatLongPoint]
        """

        self._locations = locations

    @property
    def loyalty_points(self):
        """Gets the loyalty_points of this LoyaltyObject.


        :return: The loyalty_points of this LoyaltyObject.
        :rtype: LoyaltyPoints
        """
        return self._loyalty_points

    @loyalty_points.setter
    def loyalty_points(self, loyalty_points):
        """Sets the loyalty_points of this LoyaltyObject.


        :param loyalty_points: The loyalty_points of this LoyaltyObject.
        :type loyalty_points: LoyaltyPoints
        """

        self._loyalty_points = loyalty_points

    @property
    def messages(self):
        """Gets the messages of this LoyaltyObject.

        An array of messages displayed in the app. All users of this object will receive its associated messages. The maximum number of these fields is 10.

        :return: The messages of this LoyaltyObject.
        :rtype: List[Message]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this LoyaltyObject.

        An array of messages displayed in the app. All users of this object will receive its associated messages. The maximum number of these fields is 10.

        :param messages: The messages of this LoyaltyObject.
        :type messages: List[Message]
        """

        self._messages = messages

    @property
    def pass_constraints(self):
        """Gets the pass_constraints of this LoyaltyObject.


        :return: The pass_constraints of this LoyaltyObject.
        :rtype: PassConstraints
        """
        return self._pass_constraints

    @pass_constraints.setter
    def pass_constraints(self, pass_constraints):
        """Sets the pass_constraints of this LoyaltyObject.


        :param pass_constraints: The pass_constraints of this LoyaltyObject.
        :type pass_constraints: PassConstraints
        """

        self._pass_constraints = pass_constraints

    @property
    def rotating_barcode(self):
        """Gets the rotating_barcode of this LoyaltyObject.


        :return: The rotating_barcode of this LoyaltyObject.
        :rtype: RotatingBarcode
        """
        return self._rotating_barcode

    @rotating_barcode.setter
    def rotating_barcode(self, rotating_barcode):
        """Sets the rotating_barcode of this LoyaltyObject.


        :param rotating_barcode: The rotating_barcode of this LoyaltyObject.
        :type rotating_barcode: RotatingBarcode
        """

        self._rotating_barcode = rotating_barcode

    @property
    def secondary_loyalty_points(self):
        """Gets the secondary_loyalty_points of this LoyaltyObject.


        :return: The secondary_loyalty_points of this LoyaltyObject.
        :rtype: LoyaltyPoints
        """
        return self._secondary_loyalty_points

    @secondary_loyalty_points.setter
    def secondary_loyalty_points(self, secondary_loyalty_points):
        """Sets the secondary_loyalty_points of this LoyaltyObject.


        :param secondary_loyalty_points: The secondary_loyalty_points of this LoyaltyObject.
        :type secondary_loyalty_points: LoyaltyPoints
        """

        self._secondary_loyalty_points = secondary_loyalty_points

    @property
    def smart_tap_redemption_value(self):
        """Gets the smart_tap_redemption_value of this LoyaltyObject.

        The value that will be transmitted to a Smart Tap certified terminal over NFC for this object. The class level fields `enableSmartTap` and `redemptionIssuers` must also be set up correctly in order for the pass to support Smart Tap. Only ASCII characters are supported. If this value is not set but the class level fields `enableSmartTap` and `redemptionIssuers` are set up correctly, the `barcode.value` or the `accountId` fields are used as fallback if present.

        :return: The smart_tap_redemption_value of this LoyaltyObject.
        :rtype: str
        """
        return self._smart_tap_redemption_value

    @smart_tap_redemption_value.setter
    def smart_tap_redemption_value(self, smart_tap_redemption_value):
        """Sets the smart_tap_redemption_value of this LoyaltyObject.

        The value that will be transmitted to a Smart Tap certified terminal over NFC for this object. The class level fields `enableSmartTap` and `redemptionIssuers` must also be set up correctly in order for the pass to support Smart Tap. Only ASCII characters are supported. If this value is not set but the class level fields `enableSmartTap` and `redemptionIssuers` are set up correctly, the `barcode.value` or the `accountId` fields are used as fallback if present.

        :param smart_tap_redemption_value: The smart_tap_redemption_value of this LoyaltyObject.
        :type smart_tap_redemption_value: str
        """

        self._smart_tap_redemption_value = smart_tap_redemption_value

    @property
    def state(self):
        """Gets the state of this LoyaltyObject.

        Required. The state of the object. This field is used to determine how an object is displayed in the app. For example, an `inactive` object is moved to the \"Expired passes\" section.

        :return: The state of this LoyaltyObject.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this LoyaltyObject.

        Required. The state of the object. This field is used to determine how an object is displayed in the app. For example, an `inactive` object is moved to the \"Expired passes\" section.

        :param state: The state of this LoyaltyObject.
        :type state: str
        """
        allowed_values = ["STATE_UNSPECIFIED", "ACTIVE", "active", "COMPLETED", "completed", "EXPIRED", "expired", "INACTIVE", "inactive"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def text_modules_data(self):
        """Gets the text_modules_data of this LoyaltyObject.

        Text module data. If text module data is also defined on the class, both will be displayed. The maximum number of these fields displayed is 10 from the object and 10 from the class.

        :return: The text_modules_data of this LoyaltyObject.
        :rtype: List[TextModuleData]
        """
        return self._text_modules_data

    @text_modules_data.setter
    def text_modules_data(self, text_modules_data):
        """Sets the text_modules_data of this LoyaltyObject.

        Text module data. If text module data is also defined on the class, both will be displayed. The maximum number of these fields displayed is 10 from the object and 10 from the class.

        :param text_modules_data: The text_modules_data of this LoyaltyObject.
        :type text_modules_data: List[TextModuleData]
        """

        self._text_modules_data = text_modules_data

    @property
    def valid_time_interval(self):
        """Gets the valid_time_interval of this LoyaltyObject.


        :return: The valid_time_interval of this LoyaltyObject.
        :rtype: TimeInterval
        """
        return self._valid_time_interval

    @valid_time_interval.setter
    def valid_time_interval(self, valid_time_interval):
        """Sets the valid_time_interval of this LoyaltyObject.


        :param valid_time_interval: The valid_time_interval of this LoyaltyObject.
        :type valid_time_interval: TimeInterval
        """

        self._valid_time_interval = valid_time_interval

    @property
    def version(self):
        """Gets the version of this LoyaltyObject.

        Deprecated

        :return: The version of this LoyaltyObject.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this LoyaltyObject.

        Deprecated

        :param version: The version of this LoyaltyObject.
        :type version: str
        """

        self._version = version
