# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.age_range_assigned_targeting_option_details import AgeRangeAssignedTargetingOptionDetails
from openapi_server.models.app_assigned_targeting_option_details import AppAssignedTargetingOptionDetails
from openapi_server.models.app_category_assigned_targeting_option_details import AppCategoryAssignedTargetingOptionDetails
from openapi_server.models.audience_group_assigned_targeting_option_details import AudienceGroupAssignedTargetingOptionDetails
from openapi_server.models.audio_content_type_assigned_targeting_option_details import AudioContentTypeAssignedTargetingOptionDetails
from openapi_server.models.authorized_seller_status_assigned_targeting_option_details import AuthorizedSellerStatusAssignedTargetingOptionDetails
from openapi_server.models.browser_assigned_targeting_option_details import BrowserAssignedTargetingOptionDetails
from openapi_server.models.business_chain_assigned_targeting_option_details import BusinessChainAssignedTargetingOptionDetails
from openapi_server.models.carrier_and_isp_assigned_targeting_option_details import CarrierAndIspAssignedTargetingOptionDetails
from openapi_server.models.category_assigned_targeting_option_details import CategoryAssignedTargetingOptionDetails
from openapi_server.models.channel_assigned_targeting_option_details import ChannelAssignedTargetingOptionDetails
from openapi_server.models.content_duration_assigned_targeting_option_details import ContentDurationAssignedTargetingOptionDetails
from openapi_server.models.content_genre_assigned_targeting_option_details import ContentGenreAssignedTargetingOptionDetails
from openapi_server.models.content_instream_position_assigned_targeting_option_details import ContentInstreamPositionAssignedTargetingOptionDetails
from openapi_server.models.content_outstream_position_assigned_targeting_option_details import ContentOutstreamPositionAssignedTargetingOptionDetails
from openapi_server.models.content_stream_type_assigned_targeting_option_details import ContentStreamTypeAssignedTargetingOptionDetails
from openapi_server.models.day_and_time_assigned_targeting_option_details import DayAndTimeAssignedTargetingOptionDetails
from openapi_server.models.device_make_model_assigned_targeting_option_details import DeviceMakeModelAssignedTargetingOptionDetails
from openapi_server.models.device_type_assigned_targeting_option_details import DeviceTypeAssignedTargetingOptionDetails
from openapi_server.models.digital_content_label_assigned_targeting_option_details import DigitalContentLabelAssignedTargetingOptionDetails
from openapi_server.models.environment_assigned_targeting_option_details import EnvironmentAssignedTargetingOptionDetails
from openapi_server.models.exchange_assigned_targeting_option_details import ExchangeAssignedTargetingOptionDetails
from openapi_server.models.gender_assigned_targeting_option_details import GenderAssignedTargetingOptionDetails
from openapi_server.models.geo_region_assigned_targeting_option_details import GeoRegionAssignedTargetingOptionDetails
from openapi_server.models.household_income_assigned_targeting_option_details import HouseholdIncomeAssignedTargetingOptionDetails
from openapi_server.models.inventory_source_assigned_targeting_option_details import InventorySourceAssignedTargetingOptionDetails
from openapi_server.models.inventory_source_group_assigned_targeting_option_details import InventorySourceGroupAssignedTargetingOptionDetails
from openapi_server.models.keyword_assigned_targeting_option_details import KeywordAssignedTargetingOptionDetails
from openapi_server.models.language_assigned_targeting_option_details import LanguageAssignedTargetingOptionDetails
from openapi_server.models.native_content_position_assigned_targeting_option_details import NativeContentPositionAssignedTargetingOptionDetails
from openapi_server.models.negative_keyword_list_assigned_targeting_option_details import NegativeKeywordListAssignedTargetingOptionDetails
from openapi_server.models.omid_assigned_targeting_option_details import OmidAssignedTargetingOptionDetails
from openapi_server.models.on_screen_position_assigned_targeting_option_details import OnScreenPositionAssignedTargetingOptionDetails
from openapi_server.models.operating_system_assigned_targeting_option_details import OperatingSystemAssignedTargetingOptionDetails
from openapi_server.models.parental_status_assigned_targeting_option_details import ParentalStatusAssignedTargetingOptionDetails
from openapi_server.models.poi_assigned_targeting_option_details import PoiAssignedTargetingOptionDetails
from openapi_server.models.proximity_location_list_assigned_targeting_option_details import ProximityLocationListAssignedTargetingOptionDetails
from openapi_server.models.regional_location_list_assigned_targeting_option_details import RegionalLocationListAssignedTargetingOptionDetails
from openapi_server.models.sensitive_category_assigned_targeting_option_details import SensitiveCategoryAssignedTargetingOptionDetails
from openapi_server.models.session_position_assigned_targeting_option_details import SessionPositionAssignedTargetingOptionDetails
from openapi_server.models.sub_exchange_assigned_targeting_option_details import SubExchangeAssignedTargetingOptionDetails
from openapi_server.models.third_party_verifier_assigned_targeting_option_details import ThirdPartyVerifierAssignedTargetingOptionDetails
from openapi_server.models.url_assigned_targeting_option_details import UrlAssignedTargetingOptionDetails
from openapi_server.models.user_rewarded_content_assigned_targeting_option_details import UserRewardedContentAssignedTargetingOptionDetails
from openapi_server.models.video_player_size_assigned_targeting_option_details import VideoPlayerSizeAssignedTargetingOptionDetails
from openapi_server.models.viewability_assigned_targeting_option_details import ViewabilityAssignedTargetingOptionDetails
from openapi_server.models.youtube_channel_assigned_targeting_option_details import YoutubeChannelAssignedTargetingOptionDetails
from openapi_server.models.youtube_video_assigned_targeting_option_details import YoutubeVideoAssignedTargetingOptionDetails
from openapi_server import util


class AssignedTargetingOption(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, age_range_details: AgeRangeAssignedTargetingOptionDetails=None, app_category_details: AppCategoryAssignedTargetingOptionDetails=None, app_details: AppAssignedTargetingOptionDetails=None, assigned_targeting_option_id: str=None, assigned_targeting_option_id_alias: str=None, audience_group_details: AudienceGroupAssignedTargetingOptionDetails=None, audio_content_type_details: AudioContentTypeAssignedTargetingOptionDetails=None, authorized_seller_status_details: AuthorizedSellerStatusAssignedTargetingOptionDetails=None, browser_details: BrowserAssignedTargetingOptionDetails=None, business_chain_details: BusinessChainAssignedTargetingOptionDetails=None, carrier_and_isp_details: CarrierAndIspAssignedTargetingOptionDetails=None, category_details: CategoryAssignedTargetingOptionDetails=None, channel_details: ChannelAssignedTargetingOptionDetails=None, content_duration_details: ContentDurationAssignedTargetingOptionDetails=None, content_genre_details: ContentGenreAssignedTargetingOptionDetails=None, content_instream_position_details: ContentInstreamPositionAssignedTargetingOptionDetails=None, content_outstream_position_details: ContentOutstreamPositionAssignedTargetingOptionDetails=None, content_stream_type_details: ContentStreamTypeAssignedTargetingOptionDetails=None, day_and_time_details: DayAndTimeAssignedTargetingOptionDetails=None, device_make_model_details: DeviceMakeModelAssignedTargetingOptionDetails=None, device_type_details: DeviceTypeAssignedTargetingOptionDetails=None, digital_content_label_exclusion_details: DigitalContentLabelAssignedTargetingOptionDetails=None, environment_details: EnvironmentAssignedTargetingOptionDetails=None, exchange_details: ExchangeAssignedTargetingOptionDetails=None, gender_details: GenderAssignedTargetingOptionDetails=None, geo_region_details: GeoRegionAssignedTargetingOptionDetails=None, household_income_details: HouseholdIncomeAssignedTargetingOptionDetails=None, inheritance: str=None, inventory_source_details: InventorySourceAssignedTargetingOptionDetails=None, inventory_source_group_details: InventorySourceGroupAssignedTargetingOptionDetails=None, keyword_details: KeywordAssignedTargetingOptionDetails=None, language_details: LanguageAssignedTargetingOptionDetails=None, name: str=None, native_content_position_details: NativeContentPositionAssignedTargetingOptionDetails=None, negative_keyword_list_details: NegativeKeywordListAssignedTargetingOptionDetails=None, omid_details: OmidAssignedTargetingOptionDetails=None, on_screen_position_details: OnScreenPositionAssignedTargetingOptionDetails=None, operating_system_details: OperatingSystemAssignedTargetingOptionDetails=None, parental_status_details: ParentalStatusAssignedTargetingOptionDetails=None, poi_details: PoiAssignedTargetingOptionDetails=None, proximity_location_list_details: ProximityLocationListAssignedTargetingOptionDetails=None, regional_location_list_details: RegionalLocationListAssignedTargetingOptionDetails=None, sensitive_category_exclusion_details: SensitiveCategoryAssignedTargetingOptionDetails=None, session_position_details: SessionPositionAssignedTargetingOptionDetails=None, sub_exchange_details: SubExchangeAssignedTargetingOptionDetails=None, targeting_type: str=None, third_party_verifier_details: ThirdPartyVerifierAssignedTargetingOptionDetails=None, url_details: UrlAssignedTargetingOptionDetails=None, user_rewarded_content_details: UserRewardedContentAssignedTargetingOptionDetails=None, video_player_size_details: VideoPlayerSizeAssignedTargetingOptionDetails=None, viewability_details: ViewabilityAssignedTargetingOptionDetails=None, youtube_channel_details: YoutubeChannelAssignedTargetingOptionDetails=None, youtube_video_details: YoutubeVideoAssignedTargetingOptionDetails=None):
        """AssignedTargetingOption - a model defined in OpenAPI

        :param age_range_details: The age_range_details of this AssignedTargetingOption.
        :param app_category_details: The app_category_details of this AssignedTargetingOption.
        :param app_details: The app_details of this AssignedTargetingOption.
        :param assigned_targeting_option_id: The assigned_targeting_option_id of this AssignedTargetingOption.
        :param assigned_targeting_option_id_alias: The assigned_targeting_option_id_alias of this AssignedTargetingOption.
        :param audience_group_details: The audience_group_details of this AssignedTargetingOption.
        :param audio_content_type_details: The audio_content_type_details of this AssignedTargetingOption.
        :param authorized_seller_status_details: The authorized_seller_status_details of this AssignedTargetingOption.
        :param browser_details: The browser_details of this AssignedTargetingOption.
        :param business_chain_details: The business_chain_details of this AssignedTargetingOption.
        :param carrier_and_isp_details: The carrier_and_isp_details of this AssignedTargetingOption.
        :param category_details: The category_details of this AssignedTargetingOption.
        :param channel_details: The channel_details of this AssignedTargetingOption.
        :param content_duration_details: The content_duration_details of this AssignedTargetingOption.
        :param content_genre_details: The content_genre_details of this AssignedTargetingOption.
        :param content_instream_position_details: The content_instream_position_details of this AssignedTargetingOption.
        :param content_outstream_position_details: The content_outstream_position_details of this AssignedTargetingOption.
        :param content_stream_type_details: The content_stream_type_details of this AssignedTargetingOption.
        :param day_and_time_details: The day_and_time_details of this AssignedTargetingOption.
        :param device_make_model_details: The device_make_model_details of this AssignedTargetingOption.
        :param device_type_details: The device_type_details of this AssignedTargetingOption.
        :param digital_content_label_exclusion_details: The digital_content_label_exclusion_details of this AssignedTargetingOption.
        :param environment_details: The environment_details of this AssignedTargetingOption.
        :param exchange_details: The exchange_details of this AssignedTargetingOption.
        :param gender_details: The gender_details of this AssignedTargetingOption.
        :param geo_region_details: The geo_region_details of this AssignedTargetingOption.
        :param household_income_details: The household_income_details of this AssignedTargetingOption.
        :param inheritance: The inheritance of this AssignedTargetingOption.
        :param inventory_source_details: The inventory_source_details of this AssignedTargetingOption.
        :param inventory_source_group_details: The inventory_source_group_details of this AssignedTargetingOption.
        :param keyword_details: The keyword_details of this AssignedTargetingOption.
        :param language_details: The language_details of this AssignedTargetingOption.
        :param name: The name of this AssignedTargetingOption.
        :param native_content_position_details: The native_content_position_details of this AssignedTargetingOption.
        :param negative_keyword_list_details: The negative_keyword_list_details of this AssignedTargetingOption.
        :param omid_details: The omid_details of this AssignedTargetingOption.
        :param on_screen_position_details: The on_screen_position_details of this AssignedTargetingOption.
        :param operating_system_details: The operating_system_details of this AssignedTargetingOption.
        :param parental_status_details: The parental_status_details of this AssignedTargetingOption.
        :param poi_details: The poi_details of this AssignedTargetingOption.
        :param proximity_location_list_details: The proximity_location_list_details of this AssignedTargetingOption.
        :param regional_location_list_details: The regional_location_list_details of this AssignedTargetingOption.
        :param sensitive_category_exclusion_details: The sensitive_category_exclusion_details of this AssignedTargetingOption.
        :param session_position_details: The session_position_details of this AssignedTargetingOption.
        :param sub_exchange_details: The sub_exchange_details of this AssignedTargetingOption.
        :param targeting_type: The targeting_type of this AssignedTargetingOption.
        :param third_party_verifier_details: The third_party_verifier_details of this AssignedTargetingOption.
        :param url_details: The url_details of this AssignedTargetingOption.
        :param user_rewarded_content_details: The user_rewarded_content_details of this AssignedTargetingOption.
        :param video_player_size_details: The video_player_size_details of this AssignedTargetingOption.
        :param viewability_details: The viewability_details of this AssignedTargetingOption.
        :param youtube_channel_details: The youtube_channel_details of this AssignedTargetingOption.
        :param youtube_video_details: The youtube_video_details of this AssignedTargetingOption.
        """
        self.openapi_types = {
            'age_range_details': AgeRangeAssignedTargetingOptionDetails,
            'app_category_details': AppCategoryAssignedTargetingOptionDetails,
            'app_details': AppAssignedTargetingOptionDetails,
            'assigned_targeting_option_id': str,
            'assigned_targeting_option_id_alias': str,
            'audience_group_details': AudienceGroupAssignedTargetingOptionDetails,
            'audio_content_type_details': AudioContentTypeAssignedTargetingOptionDetails,
            'authorized_seller_status_details': AuthorizedSellerStatusAssignedTargetingOptionDetails,
            'browser_details': BrowserAssignedTargetingOptionDetails,
            'business_chain_details': BusinessChainAssignedTargetingOptionDetails,
            'carrier_and_isp_details': CarrierAndIspAssignedTargetingOptionDetails,
            'category_details': CategoryAssignedTargetingOptionDetails,
            'channel_details': ChannelAssignedTargetingOptionDetails,
            'content_duration_details': ContentDurationAssignedTargetingOptionDetails,
            'content_genre_details': ContentGenreAssignedTargetingOptionDetails,
            'content_instream_position_details': ContentInstreamPositionAssignedTargetingOptionDetails,
            'content_outstream_position_details': ContentOutstreamPositionAssignedTargetingOptionDetails,
            'content_stream_type_details': ContentStreamTypeAssignedTargetingOptionDetails,
            'day_and_time_details': DayAndTimeAssignedTargetingOptionDetails,
            'device_make_model_details': DeviceMakeModelAssignedTargetingOptionDetails,
            'device_type_details': DeviceTypeAssignedTargetingOptionDetails,
            'digital_content_label_exclusion_details': DigitalContentLabelAssignedTargetingOptionDetails,
            'environment_details': EnvironmentAssignedTargetingOptionDetails,
            'exchange_details': ExchangeAssignedTargetingOptionDetails,
            'gender_details': GenderAssignedTargetingOptionDetails,
            'geo_region_details': GeoRegionAssignedTargetingOptionDetails,
            'household_income_details': HouseholdIncomeAssignedTargetingOptionDetails,
            'inheritance': str,
            'inventory_source_details': InventorySourceAssignedTargetingOptionDetails,
            'inventory_source_group_details': InventorySourceGroupAssignedTargetingOptionDetails,
            'keyword_details': KeywordAssignedTargetingOptionDetails,
            'language_details': LanguageAssignedTargetingOptionDetails,
            'name': str,
            'native_content_position_details': NativeContentPositionAssignedTargetingOptionDetails,
            'negative_keyword_list_details': NegativeKeywordListAssignedTargetingOptionDetails,
            'omid_details': OmidAssignedTargetingOptionDetails,
            'on_screen_position_details': OnScreenPositionAssignedTargetingOptionDetails,
            'operating_system_details': OperatingSystemAssignedTargetingOptionDetails,
            'parental_status_details': ParentalStatusAssignedTargetingOptionDetails,
            'poi_details': PoiAssignedTargetingOptionDetails,
            'proximity_location_list_details': ProximityLocationListAssignedTargetingOptionDetails,
            'regional_location_list_details': RegionalLocationListAssignedTargetingOptionDetails,
            'sensitive_category_exclusion_details': SensitiveCategoryAssignedTargetingOptionDetails,
            'session_position_details': SessionPositionAssignedTargetingOptionDetails,
            'sub_exchange_details': SubExchangeAssignedTargetingOptionDetails,
            'targeting_type': str,
            'third_party_verifier_details': ThirdPartyVerifierAssignedTargetingOptionDetails,
            'url_details': UrlAssignedTargetingOptionDetails,
            'user_rewarded_content_details': UserRewardedContentAssignedTargetingOptionDetails,
            'video_player_size_details': VideoPlayerSizeAssignedTargetingOptionDetails,
            'viewability_details': ViewabilityAssignedTargetingOptionDetails,
            'youtube_channel_details': YoutubeChannelAssignedTargetingOptionDetails,
            'youtube_video_details': YoutubeVideoAssignedTargetingOptionDetails
        }

        self.attribute_map = {
            'age_range_details': 'ageRangeDetails',
            'app_category_details': 'appCategoryDetails',
            'app_details': 'appDetails',
            'assigned_targeting_option_id': 'assignedTargetingOptionId',
            'assigned_targeting_option_id_alias': 'assignedTargetingOptionIdAlias',
            'audience_group_details': 'audienceGroupDetails',
            'audio_content_type_details': 'audioContentTypeDetails',
            'authorized_seller_status_details': 'authorizedSellerStatusDetails',
            'browser_details': 'browserDetails',
            'business_chain_details': 'businessChainDetails',
            'carrier_and_isp_details': 'carrierAndIspDetails',
            'category_details': 'categoryDetails',
            'channel_details': 'channelDetails',
            'content_duration_details': 'contentDurationDetails',
            'content_genre_details': 'contentGenreDetails',
            'content_instream_position_details': 'contentInstreamPositionDetails',
            'content_outstream_position_details': 'contentOutstreamPositionDetails',
            'content_stream_type_details': 'contentStreamTypeDetails',
            'day_and_time_details': 'dayAndTimeDetails',
            'device_make_model_details': 'deviceMakeModelDetails',
            'device_type_details': 'deviceTypeDetails',
            'digital_content_label_exclusion_details': 'digitalContentLabelExclusionDetails',
            'environment_details': 'environmentDetails',
            'exchange_details': 'exchangeDetails',
            'gender_details': 'genderDetails',
            'geo_region_details': 'geoRegionDetails',
            'household_income_details': 'householdIncomeDetails',
            'inheritance': 'inheritance',
            'inventory_source_details': 'inventorySourceDetails',
            'inventory_source_group_details': 'inventorySourceGroupDetails',
            'keyword_details': 'keywordDetails',
            'language_details': 'languageDetails',
            'name': 'name',
            'native_content_position_details': 'nativeContentPositionDetails',
            'negative_keyword_list_details': 'negativeKeywordListDetails',
            'omid_details': 'omidDetails',
            'on_screen_position_details': 'onScreenPositionDetails',
            'operating_system_details': 'operatingSystemDetails',
            'parental_status_details': 'parentalStatusDetails',
            'poi_details': 'poiDetails',
            'proximity_location_list_details': 'proximityLocationListDetails',
            'regional_location_list_details': 'regionalLocationListDetails',
            'sensitive_category_exclusion_details': 'sensitiveCategoryExclusionDetails',
            'session_position_details': 'sessionPositionDetails',
            'sub_exchange_details': 'subExchangeDetails',
            'targeting_type': 'targetingType',
            'third_party_verifier_details': 'thirdPartyVerifierDetails',
            'url_details': 'urlDetails',
            'user_rewarded_content_details': 'userRewardedContentDetails',
            'video_player_size_details': 'videoPlayerSizeDetails',
            'viewability_details': 'viewabilityDetails',
            'youtube_channel_details': 'youtubeChannelDetails',
            'youtube_video_details': 'youtubeVideoDetails'
        }

        self._age_range_details = age_range_details
        self._app_category_details = app_category_details
        self._app_details = app_details
        self._assigned_targeting_option_id = assigned_targeting_option_id
        self._assigned_targeting_option_id_alias = assigned_targeting_option_id_alias
        self._audience_group_details = audience_group_details
        self._audio_content_type_details = audio_content_type_details
        self._authorized_seller_status_details = authorized_seller_status_details
        self._browser_details = browser_details
        self._business_chain_details = business_chain_details
        self._carrier_and_isp_details = carrier_and_isp_details
        self._category_details = category_details
        self._channel_details = channel_details
        self._content_duration_details = content_duration_details
        self._content_genre_details = content_genre_details
        self._content_instream_position_details = content_instream_position_details
        self._content_outstream_position_details = content_outstream_position_details
        self._content_stream_type_details = content_stream_type_details
        self._day_and_time_details = day_and_time_details
        self._device_make_model_details = device_make_model_details
        self._device_type_details = device_type_details
        self._digital_content_label_exclusion_details = digital_content_label_exclusion_details
        self._environment_details = environment_details
        self._exchange_details = exchange_details
        self._gender_details = gender_details
        self._geo_region_details = geo_region_details
        self._household_income_details = household_income_details
        self._inheritance = inheritance
        self._inventory_source_details = inventory_source_details
        self._inventory_source_group_details = inventory_source_group_details
        self._keyword_details = keyword_details
        self._language_details = language_details
        self._name = name
        self._native_content_position_details = native_content_position_details
        self._negative_keyword_list_details = negative_keyword_list_details
        self._omid_details = omid_details
        self._on_screen_position_details = on_screen_position_details
        self._operating_system_details = operating_system_details
        self._parental_status_details = parental_status_details
        self._poi_details = poi_details
        self._proximity_location_list_details = proximity_location_list_details
        self._regional_location_list_details = regional_location_list_details
        self._sensitive_category_exclusion_details = sensitive_category_exclusion_details
        self._session_position_details = session_position_details
        self._sub_exchange_details = sub_exchange_details
        self._targeting_type = targeting_type
        self._third_party_verifier_details = third_party_verifier_details
        self._url_details = url_details
        self._user_rewarded_content_details = user_rewarded_content_details
        self._video_player_size_details = video_player_size_details
        self._viewability_details = viewability_details
        self._youtube_channel_details = youtube_channel_details
        self._youtube_video_details = youtube_video_details

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AssignedTargetingOption':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AssignedTargetingOption of this AssignedTargetingOption.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def age_range_details(self):
        """Gets the age_range_details of this AssignedTargetingOption.


        :return: The age_range_details of this AssignedTargetingOption.
        :rtype: AgeRangeAssignedTargetingOptionDetails
        """
        return self._age_range_details

    @age_range_details.setter
    def age_range_details(self, age_range_details):
        """Sets the age_range_details of this AssignedTargetingOption.


        :param age_range_details: The age_range_details of this AssignedTargetingOption.
        :type age_range_details: AgeRangeAssignedTargetingOptionDetails
        """

        self._age_range_details = age_range_details

    @property
    def app_category_details(self):
        """Gets the app_category_details of this AssignedTargetingOption.


        :return: The app_category_details of this AssignedTargetingOption.
        :rtype: AppCategoryAssignedTargetingOptionDetails
        """
        return self._app_category_details

    @app_category_details.setter
    def app_category_details(self, app_category_details):
        """Sets the app_category_details of this AssignedTargetingOption.


        :param app_category_details: The app_category_details of this AssignedTargetingOption.
        :type app_category_details: AppCategoryAssignedTargetingOptionDetails
        """

        self._app_category_details = app_category_details

    @property
    def app_details(self):
        """Gets the app_details of this AssignedTargetingOption.


        :return: The app_details of this AssignedTargetingOption.
        :rtype: AppAssignedTargetingOptionDetails
        """
        return self._app_details

    @app_details.setter
    def app_details(self, app_details):
        """Sets the app_details of this AssignedTargetingOption.


        :param app_details: The app_details of this AssignedTargetingOption.
        :type app_details: AppAssignedTargetingOptionDetails
        """

        self._app_details = app_details

    @property
    def assigned_targeting_option_id(self):
        """Gets the assigned_targeting_option_id of this AssignedTargetingOption.

        Output only. The unique ID of the assigned targeting option. The ID is only unique within a given resource and targeting type. It may be reused in other contexts.

        :return: The assigned_targeting_option_id of this AssignedTargetingOption.
        :rtype: str
        """
        return self._assigned_targeting_option_id

    @assigned_targeting_option_id.setter
    def assigned_targeting_option_id(self, assigned_targeting_option_id):
        """Sets the assigned_targeting_option_id of this AssignedTargetingOption.

        Output only. The unique ID of the assigned targeting option. The ID is only unique within a given resource and targeting type. It may be reused in other contexts.

        :param assigned_targeting_option_id: The assigned_targeting_option_id of this AssignedTargetingOption.
        :type assigned_targeting_option_id: str
        """

        self._assigned_targeting_option_id = assigned_targeting_option_id

    @property
    def assigned_targeting_option_id_alias(self):
        """Gets the assigned_targeting_option_id_alias of this AssignedTargetingOption.

        Output only. An alias for the assigned_targeting_option_id. This value can be used in place of `assignedTargetingOptionId` when retrieving or deleting existing targeting. This field will only be supported for all assigned targeting options of the following targeting types: * `TARGETING_TYPE_AGE_RANGE` * `TARGETING_TYPE_DEVICE_TYPE` * `TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION` * `TARGETING_TYPE_ENVIRONMENT` * `TARGETING_TYPE_EXCHANGE` * `TARGETING_TYPE_GENDER` * `TARGETING_TYPE_HOUSEHOLD_INCOME` * `TARGETING_TYPE_NATIVE_CONTENT_POSITION` * `TARGETING_TYPE_OMID` * `TARGETING_TYPE_PARENTAL_STATUS` * `TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION` * `TARGETING_TYPE_VIDEO_PLAYER_SIZE` * `TARGETING_TYPE_VIEWABILITY` This field is also supported for line item assigned targeting options of the following targeting types: * `TARGETING_TYPE_CONTENT_INSTREAM_POSITION` * `TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION`

        :return: The assigned_targeting_option_id_alias of this AssignedTargetingOption.
        :rtype: str
        """
        return self._assigned_targeting_option_id_alias

    @assigned_targeting_option_id_alias.setter
    def assigned_targeting_option_id_alias(self, assigned_targeting_option_id_alias):
        """Sets the assigned_targeting_option_id_alias of this AssignedTargetingOption.

        Output only. An alias for the assigned_targeting_option_id. This value can be used in place of `assignedTargetingOptionId` when retrieving or deleting existing targeting. This field will only be supported for all assigned targeting options of the following targeting types: * `TARGETING_TYPE_AGE_RANGE` * `TARGETING_TYPE_DEVICE_TYPE` * `TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION` * `TARGETING_TYPE_ENVIRONMENT` * `TARGETING_TYPE_EXCHANGE` * `TARGETING_TYPE_GENDER` * `TARGETING_TYPE_HOUSEHOLD_INCOME` * `TARGETING_TYPE_NATIVE_CONTENT_POSITION` * `TARGETING_TYPE_OMID` * `TARGETING_TYPE_PARENTAL_STATUS` * `TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION` * `TARGETING_TYPE_VIDEO_PLAYER_SIZE` * `TARGETING_TYPE_VIEWABILITY` This field is also supported for line item assigned targeting options of the following targeting types: * `TARGETING_TYPE_CONTENT_INSTREAM_POSITION` * `TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION`

        :param assigned_targeting_option_id_alias: The assigned_targeting_option_id_alias of this AssignedTargetingOption.
        :type assigned_targeting_option_id_alias: str
        """

        self._assigned_targeting_option_id_alias = assigned_targeting_option_id_alias

    @property
    def audience_group_details(self):
        """Gets the audience_group_details of this AssignedTargetingOption.


        :return: The audience_group_details of this AssignedTargetingOption.
        :rtype: AudienceGroupAssignedTargetingOptionDetails
        """
        return self._audience_group_details

    @audience_group_details.setter
    def audience_group_details(self, audience_group_details):
        """Sets the audience_group_details of this AssignedTargetingOption.


        :param audience_group_details: The audience_group_details of this AssignedTargetingOption.
        :type audience_group_details: AudienceGroupAssignedTargetingOptionDetails
        """

        self._audience_group_details = audience_group_details

    @property
    def audio_content_type_details(self):
        """Gets the audio_content_type_details of this AssignedTargetingOption.


        :return: The audio_content_type_details of this AssignedTargetingOption.
        :rtype: AudioContentTypeAssignedTargetingOptionDetails
        """
        return self._audio_content_type_details

    @audio_content_type_details.setter
    def audio_content_type_details(self, audio_content_type_details):
        """Sets the audio_content_type_details of this AssignedTargetingOption.


        :param audio_content_type_details: The audio_content_type_details of this AssignedTargetingOption.
        :type audio_content_type_details: AudioContentTypeAssignedTargetingOptionDetails
        """

        self._audio_content_type_details = audio_content_type_details

    @property
    def authorized_seller_status_details(self):
        """Gets the authorized_seller_status_details of this AssignedTargetingOption.


        :return: The authorized_seller_status_details of this AssignedTargetingOption.
        :rtype: AuthorizedSellerStatusAssignedTargetingOptionDetails
        """
        return self._authorized_seller_status_details

    @authorized_seller_status_details.setter
    def authorized_seller_status_details(self, authorized_seller_status_details):
        """Sets the authorized_seller_status_details of this AssignedTargetingOption.


        :param authorized_seller_status_details: The authorized_seller_status_details of this AssignedTargetingOption.
        :type authorized_seller_status_details: AuthorizedSellerStatusAssignedTargetingOptionDetails
        """

        self._authorized_seller_status_details = authorized_seller_status_details

    @property
    def browser_details(self):
        """Gets the browser_details of this AssignedTargetingOption.


        :return: The browser_details of this AssignedTargetingOption.
        :rtype: BrowserAssignedTargetingOptionDetails
        """
        return self._browser_details

    @browser_details.setter
    def browser_details(self, browser_details):
        """Sets the browser_details of this AssignedTargetingOption.


        :param browser_details: The browser_details of this AssignedTargetingOption.
        :type browser_details: BrowserAssignedTargetingOptionDetails
        """

        self._browser_details = browser_details

    @property
    def business_chain_details(self):
        """Gets the business_chain_details of this AssignedTargetingOption.


        :return: The business_chain_details of this AssignedTargetingOption.
        :rtype: BusinessChainAssignedTargetingOptionDetails
        """
        return self._business_chain_details

    @business_chain_details.setter
    def business_chain_details(self, business_chain_details):
        """Sets the business_chain_details of this AssignedTargetingOption.


        :param business_chain_details: The business_chain_details of this AssignedTargetingOption.
        :type business_chain_details: BusinessChainAssignedTargetingOptionDetails
        """

        self._business_chain_details = business_chain_details

    @property
    def carrier_and_isp_details(self):
        """Gets the carrier_and_isp_details of this AssignedTargetingOption.


        :return: The carrier_and_isp_details of this AssignedTargetingOption.
        :rtype: CarrierAndIspAssignedTargetingOptionDetails
        """
        return self._carrier_and_isp_details

    @carrier_and_isp_details.setter
    def carrier_and_isp_details(self, carrier_and_isp_details):
        """Sets the carrier_and_isp_details of this AssignedTargetingOption.


        :param carrier_and_isp_details: The carrier_and_isp_details of this AssignedTargetingOption.
        :type carrier_and_isp_details: CarrierAndIspAssignedTargetingOptionDetails
        """

        self._carrier_and_isp_details = carrier_and_isp_details

    @property
    def category_details(self):
        """Gets the category_details of this AssignedTargetingOption.


        :return: The category_details of this AssignedTargetingOption.
        :rtype: CategoryAssignedTargetingOptionDetails
        """
        return self._category_details

    @category_details.setter
    def category_details(self, category_details):
        """Sets the category_details of this AssignedTargetingOption.


        :param category_details: The category_details of this AssignedTargetingOption.
        :type category_details: CategoryAssignedTargetingOptionDetails
        """

        self._category_details = category_details

    @property
    def channel_details(self):
        """Gets the channel_details of this AssignedTargetingOption.


        :return: The channel_details of this AssignedTargetingOption.
        :rtype: ChannelAssignedTargetingOptionDetails
        """
        return self._channel_details

    @channel_details.setter
    def channel_details(self, channel_details):
        """Sets the channel_details of this AssignedTargetingOption.


        :param channel_details: The channel_details of this AssignedTargetingOption.
        :type channel_details: ChannelAssignedTargetingOptionDetails
        """

        self._channel_details = channel_details

    @property
    def content_duration_details(self):
        """Gets the content_duration_details of this AssignedTargetingOption.


        :return: The content_duration_details of this AssignedTargetingOption.
        :rtype: ContentDurationAssignedTargetingOptionDetails
        """
        return self._content_duration_details

    @content_duration_details.setter
    def content_duration_details(self, content_duration_details):
        """Sets the content_duration_details of this AssignedTargetingOption.


        :param content_duration_details: The content_duration_details of this AssignedTargetingOption.
        :type content_duration_details: ContentDurationAssignedTargetingOptionDetails
        """

        self._content_duration_details = content_duration_details

    @property
    def content_genre_details(self):
        """Gets the content_genre_details of this AssignedTargetingOption.


        :return: The content_genre_details of this AssignedTargetingOption.
        :rtype: ContentGenreAssignedTargetingOptionDetails
        """
        return self._content_genre_details

    @content_genre_details.setter
    def content_genre_details(self, content_genre_details):
        """Sets the content_genre_details of this AssignedTargetingOption.


        :param content_genre_details: The content_genre_details of this AssignedTargetingOption.
        :type content_genre_details: ContentGenreAssignedTargetingOptionDetails
        """

        self._content_genre_details = content_genre_details

    @property
    def content_instream_position_details(self):
        """Gets the content_instream_position_details of this AssignedTargetingOption.


        :return: The content_instream_position_details of this AssignedTargetingOption.
        :rtype: ContentInstreamPositionAssignedTargetingOptionDetails
        """
        return self._content_instream_position_details

    @content_instream_position_details.setter
    def content_instream_position_details(self, content_instream_position_details):
        """Sets the content_instream_position_details of this AssignedTargetingOption.


        :param content_instream_position_details: The content_instream_position_details of this AssignedTargetingOption.
        :type content_instream_position_details: ContentInstreamPositionAssignedTargetingOptionDetails
        """

        self._content_instream_position_details = content_instream_position_details

    @property
    def content_outstream_position_details(self):
        """Gets the content_outstream_position_details of this AssignedTargetingOption.


        :return: The content_outstream_position_details of this AssignedTargetingOption.
        :rtype: ContentOutstreamPositionAssignedTargetingOptionDetails
        """
        return self._content_outstream_position_details

    @content_outstream_position_details.setter
    def content_outstream_position_details(self, content_outstream_position_details):
        """Sets the content_outstream_position_details of this AssignedTargetingOption.


        :param content_outstream_position_details: The content_outstream_position_details of this AssignedTargetingOption.
        :type content_outstream_position_details: ContentOutstreamPositionAssignedTargetingOptionDetails
        """

        self._content_outstream_position_details = content_outstream_position_details

    @property
    def content_stream_type_details(self):
        """Gets the content_stream_type_details of this AssignedTargetingOption.


        :return: The content_stream_type_details of this AssignedTargetingOption.
        :rtype: ContentStreamTypeAssignedTargetingOptionDetails
        """
        return self._content_stream_type_details

    @content_stream_type_details.setter
    def content_stream_type_details(self, content_stream_type_details):
        """Sets the content_stream_type_details of this AssignedTargetingOption.


        :param content_stream_type_details: The content_stream_type_details of this AssignedTargetingOption.
        :type content_stream_type_details: ContentStreamTypeAssignedTargetingOptionDetails
        """

        self._content_stream_type_details = content_stream_type_details

    @property
    def day_and_time_details(self):
        """Gets the day_and_time_details of this AssignedTargetingOption.


        :return: The day_and_time_details of this AssignedTargetingOption.
        :rtype: DayAndTimeAssignedTargetingOptionDetails
        """
        return self._day_and_time_details

    @day_and_time_details.setter
    def day_and_time_details(self, day_and_time_details):
        """Sets the day_and_time_details of this AssignedTargetingOption.


        :param day_and_time_details: The day_and_time_details of this AssignedTargetingOption.
        :type day_and_time_details: DayAndTimeAssignedTargetingOptionDetails
        """

        self._day_and_time_details = day_and_time_details

    @property
    def device_make_model_details(self):
        """Gets the device_make_model_details of this AssignedTargetingOption.


        :return: The device_make_model_details of this AssignedTargetingOption.
        :rtype: DeviceMakeModelAssignedTargetingOptionDetails
        """
        return self._device_make_model_details

    @device_make_model_details.setter
    def device_make_model_details(self, device_make_model_details):
        """Sets the device_make_model_details of this AssignedTargetingOption.


        :param device_make_model_details: The device_make_model_details of this AssignedTargetingOption.
        :type device_make_model_details: DeviceMakeModelAssignedTargetingOptionDetails
        """

        self._device_make_model_details = device_make_model_details

    @property
    def device_type_details(self):
        """Gets the device_type_details of this AssignedTargetingOption.


        :return: The device_type_details of this AssignedTargetingOption.
        :rtype: DeviceTypeAssignedTargetingOptionDetails
        """
        return self._device_type_details

    @device_type_details.setter
    def device_type_details(self, device_type_details):
        """Sets the device_type_details of this AssignedTargetingOption.


        :param device_type_details: The device_type_details of this AssignedTargetingOption.
        :type device_type_details: DeviceTypeAssignedTargetingOptionDetails
        """

        self._device_type_details = device_type_details

    @property
    def digital_content_label_exclusion_details(self):
        """Gets the digital_content_label_exclusion_details of this AssignedTargetingOption.


        :return: The digital_content_label_exclusion_details of this AssignedTargetingOption.
        :rtype: DigitalContentLabelAssignedTargetingOptionDetails
        """
        return self._digital_content_label_exclusion_details

    @digital_content_label_exclusion_details.setter
    def digital_content_label_exclusion_details(self, digital_content_label_exclusion_details):
        """Sets the digital_content_label_exclusion_details of this AssignedTargetingOption.


        :param digital_content_label_exclusion_details: The digital_content_label_exclusion_details of this AssignedTargetingOption.
        :type digital_content_label_exclusion_details: DigitalContentLabelAssignedTargetingOptionDetails
        """

        self._digital_content_label_exclusion_details = digital_content_label_exclusion_details

    @property
    def environment_details(self):
        """Gets the environment_details of this AssignedTargetingOption.


        :return: The environment_details of this AssignedTargetingOption.
        :rtype: EnvironmentAssignedTargetingOptionDetails
        """
        return self._environment_details

    @environment_details.setter
    def environment_details(self, environment_details):
        """Sets the environment_details of this AssignedTargetingOption.


        :param environment_details: The environment_details of this AssignedTargetingOption.
        :type environment_details: EnvironmentAssignedTargetingOptionDetails
        """

        self._environment_details = environment_details

    @property
    def exchange_details(self):
        """Gets the exchange_details of this AssignedTargetingOption.


        :return: The exchange_details of this AssignedTargetingOption.
        :rtype: ExchangeAssignedTargetingOptionDetails
        """
        return self._exchange_details

    @exchange_details.setter
    def exchange_details(self, exchange_details):
        """Sets the exchange_details of this AssignedTargetingOption.


        :param exchange_details: The exchange_details of this AssignedTargetingOption.
        :type exchange_details: ExchangeAssignedTargetingOptionDetails
        """

        self._exchange_details = exchange_details

    @property
    def gender_details(self):
        """Gets the gender_details of this AssignedTargetingOption.


        :return: The gender_details of this AssignedTargetingOption.
        :rtype: GenderAssignedTargetingOptionDetails
        """
        return self._gender_details

    @gender_details.setter
    def gender_details(self, gender_details):
        """Sets the gender_details of this AssignedTargetingOption.


        :param gender_details: The gender_details of this AssignedTargetingOption.
        :type gender_details: GenderAssignedTargetingOptionDetails
        """

        self._gender_details = gender_details

    @property
    def geo_region_details(self):
        """Gets the geo_region_details of this AssignedTargetingOption.


        :return: The geo_region_details of this AssignedTargetingOption.
        :rtype: GeoRegionAssignedTargetingOptionDetails
        """
        return self._geo_region_details

    @geo_region_details.setter
    def geo_region_details(self, geo_region_details):
        """Sets the geo_region_details of this AssignedTargetingOption.


        :param geo_region_details: The geo_region_details of this AssignedTargetingOption.
        :type geo_region_details: GeoRegionAssignedTargetingOptionDetails
        """

        self._geo_region_details = geo_region_details

    @property
    def household_income_details(self):
        """Gets the household_income_details of this AssignedTargetingOption.


        :return: The household_income_details of this AssignedTargetingOption.
        :rtype: HouseholdIncomeAssignedTargetingOptionDetails
        """
        return self._household_income_details

    @household_income_details.setter
    def household_income_details(self, household_income_details):
        """Sets the household_income_details of this AssignedTargetingOption.


        :param household_income_details: The household_income_details of this AssignedTargetingOption.
        :type household_income_details: HouseholdIncomeAssignedTargetingOptionDetails
        """

        self._household_income_details = household_income_details

    @property
    def inheritance(self):
        """Gets the inheritance of this AssignedTargetingOption.

        Output only. The inheritance status of the assigned targeting option.

        :return: The inheritance of this AssignedTargetingOption.
        :rtype: str
        """
        return self._inheritance

    @inheritance.setter
    def inheritance(self, inheritance):
        """Sets the inheritance of this AssignedTargetingOption.

        Output only. The inheritance status of the assigned targeting option.

        :param inheritance: The inheritance of this AssignedTargetingOption.
        :type inheritance: str
        """
        allowed_values = ["INHERITANCE_UNSPECIFIED", "NOT_INHERITED", "INHERITED_FROM_PARTNER", "INHERITED_FROM_ADVERTISER"]  # noqa: E501
        if inheritance not in allowed_values:
            raise ValueError(
                "Invalid value for `inheritance` ({0}), must be one of {1}"
                .format(inheritance, allowed_values)
            )

        self._inheritance = inheritance

    @property
    def inventory_source_details(self):
        """Gets the inventory_source_details of this AssignedTargetingOption.


        :return: The inventory_source_details of this AssignedTargetingOption.
        :rtype: InventorySourceAssignedTargetingOptionDetails
        """
        return self._inventory_source_details

    @inventory_source_details.setter
    def inventory_source_details(self, inventory_source_details):
        """Sets the inventory_source_details of this AssignedTargetingOption.


        :param inventory_source_details: The inventory_source_details of this AssignedTargetingOption.
        :type inventory_source_details: InventorySourceAssignedTargetingOptionDetails
        """

        self._inventory_source_details = inventory_source_details

    @property
    def inventory_source_group_details(self):
        """Gets the inventory_source_group_details of this AssignedTargetingOption.


        :return: The inventory_source_group_details of this AssignedTargetingOption.
        :rtype: InventorySourceGroupAssignedTargetingOptionDetails
        """
        return self._inventory_source_group_details

    @inventory_source_group_details.setter
    def inventory_source_group_details(self, inventory_source_group_details):
        """Sets the inventory_source_group_details of this AssignedTargetingOption.


        :param inventory_source_group_details: The inventory_source_group_details of this AssignedTargetingOption.
        :type inventory_source_group_details: InventorySourceGroupAssignedTargetingOptionDetails
        """

        self._inventory_source_group_details = inventory_source_group_details

    @property
    def keyword_details(self):
        """Gets the keyword_details of this AssignedTargetingOption.


        :return: The keyword_details of this AssignedTargetingOption.
        :rtype: KeywordAssignedTargetingOptionDetails
        """
        return self._keyword_details

    @keyword_details.setter
    def keyword_details(self, keyword_details):
        """Sets the keyword_details of this AssignedTargetingOption.


        :param keyword_details: The keyword_details of this AssignedTargetingOption.
        :type keyword_details: KeywordAssignedTargetingOptionDetails
        """

        self._keyword_details = keyword_details

    @property
    def language_details(self):
        """Gets the language_details of this AssignedTargetingOption.


        :return: The language_details of this AssignedTargetingOption.
        :rtype: LanguageAssignedTargetingOptionDetails
        """
        return self._language_details

    @language_details.setter
    def language_details(self, language_details):
        """Sets the language_details of this AssignedTargetingOption.


        :param language_details: The language_details of this AssignedTargetingOption.
        :type language_details: LanguageAssignedTargetingOptionDetails
        """

        self._language_details = language_details

    @property
    def name(self):
        """Gets the name of this AssignedTargetingOption.

        Output only. The resource name for this assigned targeting option.

        :return: The name of this AssignedTargetingOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssignedTargetingOption.

        Output only. The resource name for this assigned targeting option.

        :param name: The name of this AssignedTargetingOption.
        :type name: str
        """

        self._name = name

    @property
    def native_content_position_details(self):
        """Gets the native_content_position_details of this AssignedTargetingOption.


        :return: The native_content_position_details of this AssignedTargetingOption.
        :rtype: NativeContentPositionAssignedTargetingOptionDetails
        """
        return self._native_content_position_details

    @native_content_position_details.setter
    def native_content_position_details(self, native_content_position_details):
        """Sets the native_content_position_details of this AssignedTargetingOption.


        :param native_content_position_details: The native_content_position_details of this AssignedTargetingOption.
        :type native_content_position_details: NativeContentPositionAssignedTargetingOptionDetails
        """

        self._native_content_position_details = native_content_position_details

    @property
    def negative_keyword_list_details(self):
        """Gets the negative_keyword_list_details of this AssignedTargetingOption.


        :return: The negative_keyword_list_details of this AssignedTargetingOption.
        :rtype: NegativeKeywordListAssignedTargetingOptionDetails
        """
        return self._negative_keyword_list_details

    @negative_keyword_list_details.setter
    def negative_keyword_list_details(self, negative_keyword_list_details):
        """Sets the negative_keyword_list_details of this AssignedTargetingOption.


        :param negative_keyword_list_details: The negative_keyword_list_details of this AssignedTargetingOption.
        :type negative_keyword_list_details: NegativeKeywordListAssignedTargetingOptionDetails
        """

        self._negative_keyword_list_details = negative_keyword_list_details

    @property
    def omid_details(self):
        """Gets the omid_details of this AssignedTargetingOption.


        :return: The omid_details of this AssignedTargetingOption.
        :rtype: OmidAssignedTargetingOptionDetails
        """
        return self._omid_details

    @omid_details.setter
    def omid_details(self, omid_details):
        """Sets the omid_details of this AssignedTargetingOption.


        :param omid_details: The omid_details of this AssignedTargetingOption.
        :type omid_details: OmidAssignedTargetingOptionDetails
        """

        self._omid_details = omid_details

    @property
    def on_screen_position_details(self):
        """Gets the on_screen_position_details of this AssignedTargetingOption.


        :return: The on_screen_position_details of this AssignedTargetingOption.
        :rtype: OnScreenPositionAssignedTargetingOptionDetails
        """
        return self._on_screen_position_details

    @on_screen_position_details.setter
    def on_screen_position_details(self, on_screen_position_details):
        """Sets the on_screen_position_details of this AssignedTargetingOption.


        :param on_screen_position_details: The on_screen_position_details of this AssignedTargetingOption.
        :type on_screen_position_details: OnScreenPositionAssignedTargetingOptionDetails
        """

        self._on_screen_position_details = on_screen_position_details

    @property
    def operating_system_details(self):
        """Gets the operating_system_details of this AssignedTargetingOption.


        :return: The operating_system_details of this AssignedTargetingOption.
        :rtype: OperatingSystemAssignedTargetingOptionDetails
        """
        return self._operating_system_details

    @operating_system_details.setter
    def operating_system_details(self, operating_system_details):
        """Sets the operating_system_details of this AssignedTargetingOption.


        :param operating_system_details: The operating_system_details of this AssignedTargetingOption.
        :type operating_system_details: OperatingSystemAssignedTargetingOptionDetails
        """

        self._operating_system_details = operating_system_details

    @property
    def parental_status_details(self):
        """Gets the parental_status_details of this AssignedTargetingOption.


        :return: The parental_status_details of this AssignedTargetingOption.
        :rtype: ParentalStatusAssignedTargetingOptionDetails
        """
        return self._parental_status_details

    @parental_status_details.setter
    def parental_status_details(self, parental_status_details):
        """Sets the parental_status_details of this AssignedTargetingOption.


        :param parental_status_details: The parental_status_details of this AssignedTargetingOption.
        :type parental_status_details: ParentalStatusAssignedTargetingOptionDetails
        """

        self._parental_status_details = parental_status_details

    @property
    def poi_details(self):
        """Gets the poi_details of this AssignedTargetingOption.


        :return: The poi_details of this AssignedTargetingOption.
        :rtype: PoiAssignedTargetingOptionDetails
        """
        return self._poi_details

    @poi_details.setter
    def poi_details(self, poi_details):
        """Sets the poi_details of this AssignedTargetingOption.


        :param poi_details: The poi_details of this AssignedTargetingOption.
        :type poi_details: PoiAssignedTargetingOptionDetails
        """

        self._poi_details = poi_details

    @property
    def proximity_location_list_details(self):
        """Gets the proximity_location_list_details of this AssignedTargetingOption.


        :return: The proximity_location_list_details of this AssignedTargetingOption.
        :rtype: ProximityLocationListAssignedTargetingOptionDetails
        """
        return self._proximity_location_list_details

    @proximity_location_list_details.setter
    def proximity_location_list_details(self, proximity_location_list_details):
        """Sets the proximity_location_list_details of this AssignedTargetingOption.


        :param proximity_location_list_details: The proximity_location_list_details of this AssignedTargetingOption.
        :type proximity_location_list_details: ProximityLocationListAssignedTargetingOptionDetails
        """

        self._proximity_location_list_details = proximity_location_list_details

    @property
    def regional_location_list_details(self):
        """Gets the regional_location_list_details of this AssignedTargetingOption.


        :return: The regional_location_list_details of this AssignedTargetingOption.
        :rtype: RegionalLocationListAssignedTargetingOptionDetails
        """
        return self._regional_location_list_details

    @regional_location_list_details.setter
    def regional_location_list_details(self, regional_location_list_details):
        """Sets the regional_location_list_details of this AssignedTargetingOption.


        :param regional_location_list_details: The regional_location_list_details of this AssignedTargetingOption.
        :type regional_location_list_details: RegionalLocationListAssignedTargetingOptionDetails
        """

        self._regional_location_list_details = regional_location_list_details

    @property
    def sensitive_category_exclusion_details(self):
        """Gets the sensitive_category_exclusion_details of this AssignedTargetingOption.


        :return: The sensitive_category_exclusion_details of this AssignedTargetingOption.
        :rtype: SensitiveCategoryAssignedTargetingOptionDetails
        """
        return self._sensitive_category_exclusion_details

    @sensitive_category_exclusion_details.setter
    def sensitive_category_exclusion_details(self, sensitive_category_exclusion_details):
        """Sets the sensitive_category_exclusion_details of this AssignedTargetingOption.


        :param sensitive_category_exclusion_details: The sensitive_category_exclusion_details of this AssignedTargetingOption.
        :type sensitive_category_exclusion_details: SensitiveCategoryAssignedTargetingOptionDetails
        """

        self._sensitive_category_exclusion_details = sensitive_category_exclusion_details

    @property
    def session_position_details(self):
        """Gets the session_position_details of this AssignedTargetingOption.


        :return: The session_position_details of this AssignedTargetingOption.
        :rtype: SessionPositionAssignedTargetingOptionDetails
        """
        return self._session_position_details

    @session_position_details.setter
    def session_position_details(self, session_position_details):
        """Sets the session_position_details of this AssignedTargetingOption.


        :param session_position_details: The session_position_details of this AssignedTargetingOption.
        :type session_position_details: SessionPositionAssignedTargetingOptionDetails
        """

        self._session_position_details = session_position_details

    @property
    def sub_exchange_details(self):
        """Gets the sub_exchange_details of this AssignedTargetingOption.


        :return: The sub_exchange_details of this AssignedTargetingOption.
        :rtype: SubExchangeAssignedTargetingOptionDetails
        """
        return self._sub_exchange_details

    @sub_exchange_details.setter
    def sub_exchange_details(self, sub_exchange_details):
        """Sets the sub_exchange_details of this AssignedTargetingOption.


        :param sub_exchange_details: The sub_exchange_details of this AssignedTargetingOption.
        :type sub_exchange_details: SubExchangeAssignedTargetingOptionDetails
        """

        self._sub_exchange_details = sub_exchange_details

    @property
    def targeting_type(self):
        """Gets the targeting_type of this AssignedTargetingOption.

        Output only. Identifies the type of this assigned targeting option.

        :return: The targeting_type of this AssignedTargetingOption.
        :rtype: str
        """
        return self._targeting_type

    @targeting_type.setter
    def targeting_type(self, targeting_type):
        """Sets the targeting_type of this AssignedTargetingOption.

        Output only. Identifies the type of this assigned targeting option.

        :param targeting_type: The targeting_type of this AssignedTargetingOption.
        :type targeting_type: str
        """
        allowed_values = ["TARGETING_TYPE_UNSPECIFIED", "TARGETING_TYPE_CHANNEL", "TARGETING_TYPE_APP_CATEGORY", "TARGETING_TYPE_APP", "TARGETING_TYPE_URL", "TARGETING_TYPE_DAY_AND_TIME", "TARGETING_TYPE_AGE_RANGE", "TARGETING_TYPE_REGIONAL_LOCATION_LIST", "TARGETING_TYPE_PROXIMITY_LOCATION_LIST", "TARGETING_TYPE_GENDER", "TARGETING_TYPE_VIDEO_PLAYER_SIZE", "TARGETING_TYPE_USER_REWARDED_CONTENT", "TARGETING_TYPE_PARENTAL_STATUS", "TARGETING_TYPE_CONTENT_INSTREAM_POSITION", "TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION", "TARGETING_TYPE_DEVICE_TYPE", "TARGETING_TYPE_AUDIENCE_GROUP", "TARGETING_TYPE_BROWSER", "TARGETING_TYPE_HOUSEHOLD_INCOME", "TARGETING_TYPE_ON_SCREEN_POSITION", "TARGETING_TYPE_THIRD_PARTY_VERIFIER", "TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION", "TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION", "TARGETING_TYPE_ENVIRONMENT", "TARGETING_TYPE_CARRIER_AND_ISP", "TARGETING_TYPE_OPERATING_SYSTEM", "TARGETING_TYPE_DEVICE_MAKE_MODEL", "TARGETING_TYPE_KEYWORD", "TARGETING_TYPE_NEGATIVE_KEYWORD_LIST", "TARGETING_TYPE_VIEWABILITY", "TARGETING_TYPE_CATEGORY", "TARGETING_TYPE_INVENTORY_SOURCE", "TARGETING_TYPE_LANGUAGE", "TARGETING_TYPE_AUTHORIZED_SELLER_STATUS", "TARGETING_TYPE_GEO_REGION", "TARGETING_TYPE_INVENTORY_SOURCE_GROUP", "TARGETING_TYPE_EXCHANGE", "TARGETING_TYPE_SUB_EXCHANGE", "TARGETING_TYPE_POI", "TARGETING_TYPE_BUSINESS_CHAIN", "TARGETING_TYPE_CONTENT_DURATION", "TARGETING_TYPE_CONTENT_STREAM_TYPE", "TARGETING_TYPE_NATIVE_CONTENT_POSITION", "TARGETING_TYPE_OMID", "TARGETING_TYPE_AUDIO_CONTENT_TYPE", "TARGETING_TYPE_CONTENT_GENRE", "TARGETING_TYPE_YOUTUBE_VIDEO", "TARGETING_TYPE_YOUTUBE_CHANNEL", "TARGETING_TYPE_SESSION_POSITION"]  # noqa: E501
        if targeting_type not in allowed_values:
            raise ValueError(
                "Invalid value for `targeting_type` ({0}), must be one of {1}"
                .format(targeting_type, allowed_values)
            )

        self._targeting_type = targeting_type

    @property
    def third_party_verifier_details(self):
        """Gets the third_party_verifier_details of this AssignedTargetingOption.


        :return: The third_party_verifier_details of this AssignedTargetingOption.
        :rtype: ThirdPartyVerifierAssignedTargetingOptionDetails
        """
        return self._third_party_verifier_details

    @third_party_verifier_details.setter
    def third_party_verifier_details(self, third_party_verifier_details):
        """Sets the third_party_verifier_details of this AssignedTargetingOption.


        :param third_party_verifier_details: The third_party_verifier_details of this AssignedTargetingOption.
        :type third_party_verifier_details: ThirdPartyVerifierAssignedTargetingOptionDetails
        """

        self._third_party_verifier_details = third_party_verifier_details

    @property
    def url_details(self):
        """Gets the url_details of this AssignedTargetingOption.


        :return: The url_details of this AssignedTargetingOption.
        :rtype: UrlAssignedTargetingOptionDetails
        """
        return self._url_details

    @url_details.setter
    def url_details(self, url_details):
        """Sets the url_details of this AssignedTargetingOption.


        :param url_details: The url_details of this AssignedTargetingOption.
        :type url_details: UrlAssignedTargetingOptionDetails
        """

        self._url_details = url_details

    @property
    def user_rewarded_content_details(self):
        """Gets the user_rewarded_content_details of this AssignedTargetingOption.


        :return: The user_rewarded_content_details of this AssignedTargetingOption.
        :rtype: UserRewardedContentAssignedTargetingOptionDetails
        """
        return self._user_rewarded_content_details

    @user_rewarded_content_details.setter
    def user_rewarded_content_details(self, user_rewarded_content_details):
        """Sets the user_rewarded_content_details of this AssignedTargetingOption.


        :param user_rewarded_content_details: The user_rewarded_content_details of this AssignedTargetingOption.
        :type user_rewarded_content_details: UserRewardedContentAssignedTargetingOptionDetails
        """

        self._user_rewarded_content_details = user_rewarded_content_details

    @property
    def video_player_size_details(self):
        """Gets the video_player_size_details of this AssignedTargetingOption.


        :return: The video_player_size_details of this AssignedTargetingOption.
        :rtype: VideoPlayerSizeAssignedTargetingOptionDetails
        """
        return self._video_player_size_details

    @video_player_size_details.setter
    def video_player_size_details(self, video_player_size_details):
        """Sets the video_player_size_details of this AssignedTargetingOption.


        :param video_player_size_details: The video_player_size_details of this AssignedTargetingOption.
        :type video_player_size_details: VideoPlayerSizeAssignedTargetingOptionDetails
        """

        self._video_player_size_details = video_player_size_details

    @property
    def viewability_details(self):
        """Gets the viewability_details of this AssignedTargetingOption.


        :return: The viewability_details of this AssignedTargetingOption.
        :rtype: ViewabilityAssignedTargetingOptionDetails
        """
        return self._viewability_details

    @viewability_details.setter
    def viewability_details(self, viewability_details):
        """Sets the viewability_details of this AssignedTargetingOption.


        :param viewability_details: The viewability_details of this AssignedTargetingOption.
        :type viewability_details: ViewabilityAssignedTargetingOptionDetails
        """

        self._viewability_details = viewability_details

    @property
    def youtube_channel_details(self):
        """Gets the youtube_channel_details of this AssignedTargetingOption.


        :return: The youtube_channel_details of this AssignedTargetingOption.
        :rtype: YoutubeChannelAssignedTargetingOptionDetails
        """
        return self._youtube_channel_details

    @youtube_channel_details.setter
    def youtube_channel_details(self, youtube_channel_details):
        """Sets the youtube_channel_details of this AssignedTargetingOption.


        :param youtube_channel_details: The youtube_channel_details of this AssignedTargetingOption.
        :type youtube_channel_details: YoutubeChannelAssignedTargetingOptionDetails
        """

        self._youtube_channel_details = youtube_channel_details

    @property
    def youtube_video_details(self):
        """Gets the youtube_video_details of this AssignedTargetingOption.


        :return: The youtube_video_details of this AssignedTargetingOption.
        :rtype: YoutubeVideoAssignedTargetingOptionDetails
        """
        return self._youtube_video_details

    @youtube_video_details.setter
    def youtube_video_details(self, youtube_video_details):
        """Sets the youtube_video_details of this AssignedTargetingOption.


        :param youtube_video_details: The youtube_video_details of this AssignedTargetingOption.
        :type youtube_video_details: YoutubeVideoAssignedTargetingOptionDetails
        """

        self._youtube_video_details = youtube_video_details
