# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.google_ads_searchads360_v0_common_metrics import GoogleAdsSearchads360V0CommonMetrics
from openapi_server.models.google_ads_searchads360_v0_common_segments import GoogleAdsSearchads360V0CommonSegments
from openapi_server.models.google_ads_searchads360_v0_common_value import GoogleAdsSearchads360V0CommonValue
from openapi_server.models.google_ads_searchads360_v0_resources_ad_group import GoogleAdsSearchads360V0ResourcesAdGroup
from openapi_server.models.google_ads_searchads360_v0_resources_ad_group_ad import GoogleAdsSearchads360V0ResourcesAdGroupAd
from openapi_server.models.google_ads_searchads360_v0_resources_ad_group_ad_label import GoogleAdsSearchads360V0ResourcesAdGroupAdLabel
from openapi_server.models.google_ads_searchads360_v0_resources_ad_group_asset import GoogleAdsSearchads360V0ResourcesAdGroupAsset
from openapi_server.models.google_ads_searchads360_v0_resources_ad_group_asset_set import GoogleAdsSearchads360V0ResourcesAdGroupAssetSet
from openapi_server.models.google_ads_searchads360_v0_resources_ad_group_audience_view import GoogleAdsSearchads360V0ResourcesAdGroupAudienceView
from openapi_server.models.google_ads_searchads360_v0_resources_ad_group_bid_modifier import GoogleAdsSearchads360V0ResourcesAdGroupBidModifier
from openapi_server.models.google_ads_searchads360_v0_resources_ad_group_criterion import GoogleAdsSearchads360V0ResourcesAdGroupCriterion
from openapi_server.models.google_ads_searchads360_v0_resources_ad_group_criterion_label import GoogleAdsSearchads360V0ResourcesAdGroupCriterionLabel
from openapi_server.models.google_ads_searchads360_v0_resources_ad_group_label import GoogleAdsSearchads360V0ResourcesAdGroupLabel
from openapi_server.models.google_ads_searchads360_v0_resources_age_range_view import GoogleAdsSearchads360V0ResourcesAgeRangeView
from openapi_server.models.google_ads_searchads360_v0_resources_asset import GoogleAdsSearchads360V0ResourcesAsset
from openapi_server.models.google_ads_searchads360_v0_resources_asset_group import GoogleAdsSearchads360V0ResourcesAssetGroup
from openapi_server.models.google_ads_searchads360_v0_resources_asset_group_asset import GoogleAdsSearchads360V0ResourcesAssetGroupAsset
from openapi_server.models.google_ads_searchads360_v0_resources_asset_group_listing_group_filter import GoogleAdsSearchads360V0ResourcesAssetGroupListingGroupFilter
from openapi_server.models.google_ads_searchads360_v0_resources_asset_group_signal import GoogleAdsSearchads360V0ResourcesAssetGroupSignal
from openapi_server.models.google_ads_searchads360_v0_resources_asset_group_top_combination_view import GoogleAdsSearchads360V0ResourcesAssetGroupTopCombinationView
from openapi_server.models.google_ads_searchads360_v0_resources_asset_set import GoogleAdsSearchads360V0ResourcesAssetSet
from openapi_server.models.google_ads_searchads360_v0_resources_asset_set_asset import GoogleAdsSearchads360V0ResourcesAssetSetAsset
from openapi_server.models.google_ads_searchads360_v0_resources_audience import GoogleAdsSearchads360V0ResourcesAudience
from openapi_server.models.google_ads_searchads360_v0_resources_bidding_strategy import GoogleAdsSearchads360V0ResourcesBiddingStrategy
from openapi_server.models.google_ads_searchads360_v0_resources_campaign import GoogleAdsSearchads360V0ResourcesCampaign
from openapi_server.models.google_ads_searchads360_v0_resources_campaign_asset import GoogleAdsSearchads360V0ResourcesCampaignAsset
from openapi_server.models.google_ads_searchads360_v0_resources_campaign_asset_set import GoogleAdsSearchads360V0ResourcesCampaignAssetSet
from openapi_server.models.google_ads_searchads360_v0_resources_campaign_audience_view import GoogleAdsSearchads360V0ResourcesCampaignAudienceView
from openapi_server.models.google_ads_searchads360_v0_resources_campaign_budget import GoogleAdsSearchads360V0ResourcesCampaignBudget
from openapi_server.models.google_ads_searchads360_v0_resources_campaign_criterion import GoogleAdsSearchads360V0ResourcesCampaignCriterion
from openapi_server.models.google_ads_searchads360_v0_resources_campaign_label import GoogleAdsSearchads360V0ResourcesCampaignLabel
from openapi_server.models.google_ads_searchads360_v0_resources_cart_data_sales_view import GoogleAdsSearchads360V0ResourcesCartDataSalesView
from openapi_server.models.google_ads_searchads360_v0_resources_conversion import GoogleAdsSearchads360V0ResourcesConversion
from openapi_server.models.google_ads_searchads360_v0_resources_conversion_action import GoogleAdsSearchads360V0ResourcesConversionAction
from openapi_server.models.google_ads_searchads360_v0_resources_conversion_custom_variable import GoogleAdsSearchads360V0ResourcesConversionCustomVariable
from openapi_server.models.google_ads_searchads360_v0_resources_customer import GoogleAdsSearchads360V0ResourcesCustomer
from openapi_server.models.google_ads_searchads360_v0_resources_customer_asset import GoogleAdsSearchads360V0ResourcesCustomerAsset
from openapi_server.models.google_ads_searchads360_v0_resources_customer_asset_set import GoogleAdsSearchads360V0ResourcesCustomerAssetSet
from openapi_server.models.google_ads_searchads360_v0_resources_customer_client import GoogleAdsSearchads360V0ResourcesCustomerClient
from openapi_server.models.google_ads_searchads360_v0_resources_customer_manager_link import GoogleAdsSearchads360V0ResourcesCustomerManagerLink
from openapi_server.models.google_ads_searchads360_v0_resources_dynamic_search_ads_search_term_view import GoogleAdsSearchads360V0ResourcesDynamicSearchAdsSearchTermView
from openapi_server.models.google_ads_searchads360_v0_resources_gender_view import GoogleAdsSearchads360V0ResourcesGenderView
from openapi_server.models.google_ads_searchads360_v0_resources_geo_target_constant import GoogleAdsSearchads360V0ResourcesGeoTargetConstant
from openapi_server.models.google_ads_searchads360_v0_resources_keyword_view import GoogleAdsSearchads360V0ResourcesKeywordView
from openapi_server.models.google_ads_searchads360_v0_resources_label import GoogleAdsSearchads360V0ResourcesLabel
from openapi_server.models.google_ads_searchads360_v0_resources_language_constant import GoogleAdsSearchads360V0ResourcesLanguageConstant
from openapi_server.models.google_ads_searchads360_v0_resources_location_view import GoogleAdsSearchads360V0ResourcesLocationView
from openapi_server.models.google_ads_searchads360_v0_resources_product_bidding_category_constant import GoogleAdsSearchads360V0ResourcesProductBiddingCategoryConstant
from openapi_server.models.google_ads_searchads360_v0_resources_product_group_view import GoogleAdsSearchads360V0ResourcesProductGroupView
from openapi_server.models.google_ads_searchads360_v0_resources_shopping_performance_view import GoogleAdsSearchads360V0ResourcesShoppingPerformanceView
from openapi_server.models.google_ads_searchads360_v0_resources_user_list import GoogleAdsSearchads360V0ResourcesUserList
from openapi_server.models.google_ads_searchads360_v0_resources_visit import GoogleAdsSearchads360V0ResourcesVisit
from openapi_server.models.google_ads_searchads360_v0_resources_webpage_view import GoogleAdsSearchads360V0ResourcesWebpageView
from openapi_server import util


class GoogleAdsSearchads360V0ServicesSearchAds360Row(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ad_group: GoogleAdsSearchads360V0ResourcesAdGroup=None, ad_group_ad: GoogleAdsSearchads360V0ResourcesAdGroupAd=None, ad_group_ad_label: GoogleAdsSearchads360V0ResourcesAdGroupAdLabel=None, ad_group_asset: GoogleAdsSearchads360V0ResourcesAdGroupAsset=None, ad_group_asset_set: GoogleAdsSearchads360V0ResourcesAdGroupAssetSet=None, ad_group_audience_view: GoogleAdsSearchads360V0ResourcesAdGroupAudienceView=None, ad_group_bid_modifier: GoogleAdsSearchads360V0ResourcesAdGroupBidModifier=None, ad_group_criterion: GoogleAdsSearchads360V0ResourcesAdGroupCriterion=None, ad_group_criterion_label: GoogleAdsSearchads360V0ResourcesAdGroupCriterionLabel=None, ad_group_label: GoogleAdsSearchads360V0ResourcesAdGroupLabel=None, age_range_view: GoogleAdsSearchads360V0ResourcesAgeRangeView=None, asset: GoogleAdsSearchads360V0ResourcesAsset=None, asset_group: GoogleAdsSearchads360V0ResourcesAssetGroup=None, asset_group_asset: GoogleAdsSearchads360V0ResourcesAssetGroupAsset=None, asset_group_listing_group_filter: GoogleAdsSearchads360V0ResourcesAssetGroupListingGroupFilter=None, asset_group_signal: GoogleAdsSearchads360V0ResourcesAssetGroupSignal=None, asset_group_top_combination_view: GoogleAdsSearchads360V0ResourcesAssetGroupTopCombinationView=None, asset_set: GoogleAdsSearchads360V0ResourcesAssetSet=None, asset_set_asset: GoogleAdsSearchads360V0ResourcesAssetSetAsset=None, audience: GoogleAdsSearchads360V0ResourcesAudience=None, bidding_strategy: GoogleAdsSearchads360V0ResourcesBiddingStrategy=None, campaign: GoogleAdsSearchads360V0ResourcesCampaign=None, campaign_asset: GoogleAdsSearchads360V0ResourcesCampaignAsset=None, campaign_asset_set: GoogleAdsSearchads360V0ResourcesCampaignAssetSet=None, campaign_audience_view: GoogleAdsSearchads360V0ResourcesCampaignAudienceView=None, campaign_budget: GoogleAdsSearchads360V0ResourcesCampaignBudget=None, campaign_criterion: GoogleAdsSearchads360V0ResourcesCampaignCriterion=None, campaign_label: GoogleAdsSearchads360V0ResourcesCampaignLabel=None, cart_data_sales_view: GoogleAdsSearchads360V0ResourcesCartDataSalesView=None, conversion: GoogleAdsSearchads360V0ResourcesConversion=None, conversion_action: GoogleAdsSearchads360V0ResourcesConversionAction=None, conversion_custom_variable: GoogleAdsSearchads360V0ResourcesConversionCustomVariable=None, custom_columns: List[GoogleAdsSearchads360V0CommonValue]=None, customer: GoogleAdsSearchads360V0ResourcesCustomer=None, customer_asset: GoogleAdsSearchads360V0ResourcesCustomerAsset=None, customer_asset_set: GoogleAdsSearchads360V0ResourcesCustomerAssetSet=None, customer_client: GoogleAdsSearchads360V0ResourcesCustomerClient=None, customer_manager_link: GoogleAdsSearchads360V0ResourcesCustomerManagerLink=None, dynamic_search_ads_search_term_view: GoogleAdsSearchads360V0ResourcesDynamicSearchAdsSearchTermView=None, gender_view: GoogleAdsSearchads360V0ResourcesGenderView=None, geo_target_constant: GoogleAdsSearchads360V0ResourcesGeoTargetConstant=None, keyword_view: GoogleAdsSearchads360V0ResourcesKeywordView=None, label: GoogleAdsSearchads360V0ResourcesLabel=None, language_constant: GoogleAdsSearchads360V0ResourcesLanguageConstant=None, location_view: GoogleAdsSearchads360V0ResourcesLocationView=None, metrics: GoogleAdsSearchads360V0CommonMetrics=None, product_bidding_category_constant: GoogleAdsSearchads360V0ResourcesProductBiddingCategoryConstant=None, product_group_view: GoogleAdsSearchads360V0ResourcesProductGroupView=None, segments: GoogleAdsSearchads360V0CommonSegments=None, shopping_performance_view: GoogleAdsSearchads360V0ResourcesShoppingPerformanceView=None, user_list: GoogleAdsSearchads360V0ResourcesUserList=None, visit: GoogleAdsSearchads360V0ResourcesVisit=None, webpage_view: GoogleAdsSearchads360V0ResourcesWebpageView=None):
        """GoogleAdsSearchads360V0ServicesSearchAds360Row - a model defined in OpenAPI

        :param ad_group: The ad_group of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param ad_group_ad: The ad_group_ad of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param ad_group_ad_label: The ad_group_ad_label of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param ad_group_asset: The ad_group_asset of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param ad_group_asset_set: The ad_group_asset_set of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param ad_group_audience_view: The ad_group_audience_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param ad_group_bid_modifier: The ad_group_bid_modifier of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param ad_group_criterion: The ad_group_criterion of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param ad_group_criterion_label: The ad_group_criterion_label of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param ad_group_label: The ad_group_label of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param age_range_view: The age_range_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param asset: The asset of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param asset_group: The asset_group of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param asset_group_asset: The asset_group_asset of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param asset_group_listing_group_filter: The asset_group_listing_group_filter of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param asset_group_signal: The asset_group_signal of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param asset_group_top_combination_view: The asset_group_top_combination_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param asset_set: The asset_set of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param asset_set_asset: The asset_set_asset of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param audience: The audience of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param bidding_strategy: The bidding_strategy of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param campaign: The campaign of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param campaign_asset: The campaign_asset of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param campaign_asset_set: The campaign_asset_set of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param campaign_audience_view: The campaign_audience_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param campaign_budget: The campaign_budget of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param campaign_criterion: The campaign_criterion of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param campaign_label: The campaign_label of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param cart_data_sales_view: The cart_data_sales_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param conversion: The conversion of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param conversion_action: The conversion_action of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param conversion_custom_variable: The conversion_custom_variable of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param custom_columns: The custom_columns of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param customer: The customer of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param customer_asset: The customer_asset of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param customer_asset_set: The customer_asset_set of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param customer_client: The customer_client of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param customer_manager_link: The customer_manager_link of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param dynamic_search_ads_search_term_view: The dynamic_search_ads_search_term_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param gender_view: The gender_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param geo_target_constant: The geo_target_constant of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param keyword_view: The keyword_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param label: The label of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param language_constant: The language_constant of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param location_view: The location_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param metrics: The metrics of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param product_bidding_category_constant: The product_bidding_category_constant of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param product_group_view: The product_group_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param segments: The segments of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param shopping_performance_view: The shopping_performance_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param user_list: The user_list of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param visit: The visit of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :param webpage_view: The webpage_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        """
        self.openapi_types = {
            'ad_group': GoogleAdsSearchads360V0ResourcesAdGroup,
            'ad_group_ad': GoogleAdsSearchads360V0ResourcesAdGroupAd,
            'ad_group_ad_label': GoogleAdsSearchads360V0ResourcesAdGroupAdLabel,
            'ad_group_asset': GoogleAdsSearchads360V0ResourcesAdGroupAsset,
            'ad_group_asset_set': GoogleAdsSearchads360V0ResourcesAdGroupAssetSet,
            'ad_group_audience_view': GoogleAdsSearchads360V0ResourcesAdGroupAudienceView,
            'ad_group_bid_modifier': GoogleAdsSearchads360V0ResourcesAdGroupBidModifier,
            'ad_group_criterion': GoogleAdsSearchads360V0ResourcesAdGroupCriterion,
            'ad_group_criterion_label': GoogleAdsSearchads360V0ResourcesAdGroupCriterionLabel,
            'ad_group_label': GoogleAdsSearchads360V0ResourcesAdGroupLabel,
            'age_range_view': GoogleAdsSearchads360V0ResourcesAgeRangeView,
            'asset': GoogleAdsSearchads360V0ResourcesAsset,
            'asset_group': GoogleAdsSearchads360V0ResourcesAssetGroup,
            'asset_group_asset': GoogleAdsSearchads360V0ResourcesAssetGroupAsset,
            'asset_group_listing_group_filter': GoogleAdsSearchads360V0ResourcesAssetGroupListingGroupFilter,
            'asset_group_signal': GoogleAdsSearchads360V0ResourcesAssetGroupSignal,
            'asset_group_top_combination_view': GoogleAdsSearchads360V0ResourcesAssetGroupTopCombinationView,
            'asset_set': GoogleAdsSearchads360V0ResourcesAssetSet,
            'asset_set_asset': GoogleAdsSearchads360V0ResourcesAssetSetAsset,
            'audience': GoogleAdsSearchads360V0ResourcesAudience,
            'bidding_strategy': GoogleAdsSearchads360V0ResourcesBiddingStrategy,
            'campaign': GoogleAdsSearchads360V0ResourcesCampaign,
            'campaign_asset': GoogleAdsSearchads360V0ResourcesCampaignAsset,
            'campaign_asset_set': GoogleAdsSearchads360V0ResourcesCampaignAssetSet,
            'campaign_audience_view': GoogleAdsSearchads360V0ResourcesCampaignAudienceView,
            'campaign_budget': GoogleAdsSearchads360V0ResourcesCampaignBudget,
            'campaign_criterion': GoogleAdsSearchads360V0ResourcesCampaignCriterion,
            'campaign_label': GoogleAdsSearchads360V0ResourcesCampaignLabel,
            'cart_data_sales_view': GoogleAdsSearchads360V0ResourcesCartDataSalesView,
            'conversion': GoogleAdsSearchads360V0ResourcesConversion,
            'conversion_action': GoogleAdsSearchads360V0ResourcesConversionAction,
            'conversion_custom_variable': GoogleAdsSearchads360V0ResourcesConversionCustomVariable,
            'custom_columns': List[GoogleAdsSearchads360V0CommonValue],
            'customer': GoogleAdsSearchads360V0ResourcesCustomer,
            'customer_asset': GoogleAdsSearchads360V0ResourcesCustomerAsset,
            'customer_asset_set': GoogleAdsSearchads360V0ResourcesCustomerAssetSet,
            'customer_client': GoogleAdsSearchads360V0ResourcesCustomerClient,
            'customer_manager_link': GoogleAdsSearchads360V0ResourcesCustomerManagerLink,
            'dynamic_search_ads_search_term_view': GoogleAdsSearchads360V0ResourcesDynamicSearchAdsSearchTermView,
            'gender_view': GoogleAdsSearchads360V0ResourcesGenderView,
            'geo_target_constant': GoogleAdsSearchads360V0ResourcesGeoTargetConstant,
            'keyword_view': GoogleAdsSearchads360V0ResourcesKeywordView,
            'label': GoogleAdsSearchads360V0ResourcesLabel,
            'language_constant': GoogleAdsSearchads360V0ResourcesLanguageConstant,
            'location_view': GoogleAdsSearchads360V0ResourcesLocationView,
            'metrics': GoogleAdsSearchads360V0CommonMetrics,
            'product_bidding_category_constant': GoogleAdsSearchads360V0ResourcesProductBiddingCategoryConstant,
            'product_group_view': GoogleAdsSearchads360V0ResourcesProductGroupView,
            'segments': GoogleAdsSearchads360V0CommonSegments,
            'shopping_performance_view': GoogleAdsSearchads360V0ResourcesShoppingPerformanceView,
            'user_list': GoogleAdsSearchads360V0ResourcesUserList,
            'visit': GoogleAdsSearchads360V0ResourcesVisit,
            'webpage_view': GoogleAdsSearchads360V0ResourcesWebpageView
        }

        self.attribute_map = {
            'ad_group': 'adGroup',
            'ad_group_ad': 'adGroupAd',
            'ad_group_ad_label': 'adGroupAdLabel',
            'ad_group_asset': 'adGroupAsset',
            'ad_group_asset_set': 'adGroupAssetSet',
            'ad_group_audience_view': 'adGroupAudienceView',
            'ad_group_bid_modifier': 'adGroupBidModifier',
            'ad_group_criterion': 'adGroupCriterion',
            'ad_group_criterion_label': 'adGroupCriterionLabel',
            'ad_group_label': 'adGroupLabel',
            'age_range_view': 'ageRangeView',
            'asset': 'asset',
            'asset_group': 'assetGroup',
            'asset_group_asset': 'assetGroupAsset',
            'asset_group_listing_group_filter': 'assetGroupListingGroupFilter',
            'asset_group_signal': 'assetGroupSignal',
            'asset_group_top_combination_view': 'assetGroupTopCombinationView',
            'asset_set': 'assetSet',
            'asset_set_asset': 'assetSetAsset',
            'audience': 'audience',
            'bidding_strategy': 'biddingStrategy',
            'campaign': 'campaign',
            'campaign_asset': 'campaignAsset',
            'campaign_asset_set': 'campaignAssetSet',
            'campaign_audience_view': 'campaignAudienceView',
            'campaign_budget': 'campaignBudget',
            'campaign_criterion': 'campaignCriterion',
            'campaign_label': 'campaignLabel',
            'cart_data_sales_view': 'cartDataSalesView',
            'conversion': 'conversion',
            'conversion_action': 'conversionAction',
            'conversion_custom_variable': 'conversionCustomVariable',
            'custom_columns': 'customColumns',
            'customer': 'customer',
            'customer_asset': 'customerAsset',
            'customer_asset_set': 'customerAssetSet',
            'customer_client': 'customerClient',
            'customer_manager_link': 'customerManagerLink',
            'dynamic_search_ads_search_term_view': 'dynamicSearchAdsSearchTermView',
            'gender_view': 'genderView',
            'geo_target_constant': 'geoTargetConstant',
            'keyword_view': 'keywordView',
            'label': 'label',
            'language_constant': 'languageConstant',
            'location_view': 'locationView',
            'metrics': 'metrics',
            'product_bidding_category_constant': 'productBiddingCategoryConstant',
            'product_group_view': 'productGroupView',
            'segments': 'segments',
            'shopping_performance_view': 'shoppingPerformanceView',
            'user_list': 'userList',
            'visit': 'visit',
            'webpage_view': 'webpageView'
        }

        self._ad_group = ad_group
        self._ad_group_ad = ad_group_ad
        self._ad_group_ad_label = ad_group_ad_label
        self._ad_group_asset = ad_group_asset
        self._ad_group_asset_set = ad_group_asset_set
        self._ad_group_audience_view = ad_group_audience_view
        self._ad_group_bid_modifier = ad_group_bid_modifier
        self._ad_group_criterion = ad_group_criterion
        self._ad_group_criterion_label = ad_group_criterion_label
        self._ad_group_label = ad_group_label
        self._age_range_view = age_range_view
        self._asset = asset
        self._asset_group = asset_group
        self._asset_group_asset = asset_group_asset
        self._asset_group_listing_group_filter = asset_group_listing_group_filter
        self._asset_group_signal = asset_group_signal
        self._asset_group_top_combination_view = asset_group_top_combination_view
        self._asset_set = asset_set
        self._asset_set_asset = asset_set_asset
        self._audience = audience
        self._bidding_strategy = bidding_strategy
        self._campaign = campaign
        self._campaign_asset = campaign_asset
        self._campaign_asset_set = campaign_asset_set
        self._campaign_audience_view = campaign_audience_view
        self._campaign_budget = campaign_budget
        self._campaign_criterion = campaign_criterion
        self._campaign_label = campaign_label
        self._cart_data_sales_view = cart_data_sales_view
        self._conversion = conversion
        self._conversion_action = conversion_action
        self._conversion_custom_variable = conversion_custom_variable
        self._custom_columns = custom_columns
        self._customer = customer
        self._customer_asset = customer_asset
        self._customer_asset_set = customer_asset_set
        self._customer_client = customer_client
        self._customer_manager_link = customer_manager_link
        self._dynamic_search_ads_search_term_view = dynamic_search_ads_search_term_view
        self._gender_view = gender_view
        self._geo_target_constant = geo_target_constant
        self._keyword_view = keyword_view
        self._label = label
        self._language_constant = language_constant
        self._location_view = location_view
        self._metrics = metrics
        self._product_bidding_category_constant = product_bidding_category_constant
        self._product_group_view = product_group_view
        self._segments = segments
        self._shopping_performance_view = shopping_performance_view
        self._user_list = user_list
        self._visit = visit
        self._webpage_view = webpage_view

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GoogleAdsSearchads360V0ServicesSearchAds360Row':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The GoogleAdsSearchads360V0Services__SearchAds360Row of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ad_group(self):
        """Gets the ad_group of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The ad_group of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesAdGroup
        """
        return self._ad_group

    @ad_group.setter
    def ad_group(self, ad_group):
        """Sets the ad_group of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param ad_group: The ad_group of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type ad_group: GoogleAdsSearchads360V0ResourcesAdGroup
        """

        self._ad_group = ad_group

    @property
    def ad_group_ad(self):
        """Gets the ad_group_ad of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The ad_group_ad of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesAdGroupAd
        """
        return self._ad_group_ad

    @ad_group_ad.setter
    def ad_group_ad(self, ad_group_ad):
        """Sets the ad_group_ad of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param ad_group_ad: The ad_group_ad of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type ad_group_ad: GoogleAdsSearchads360V0ResourcesAdGroupAd
        """

        self._ad_group_ad = ad_group_ad

    @property
    def ad_group_ad_label(self):
        """Gets the ad_group_ad_label of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The ad_group_ad_label of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesAdGroupAdLabel
        """
        return self._ad_group_ad_label

    @ad_group_ad_label.setter
    def ad_group_ad_label(self, ad_group_ad_label):
        """Sets the ad_group_ad_label of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param ad_group_ad_label: The ad_group_ad_label of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type ad_group_ad_label: GoogleAdsSearchads360V0ResourcesAdGroupAdLabel
        """

        self._ad_group_ad_label = ad_group_ad_label

    @property
    def ad_group_asset(self):
        """Gets the ad_group_asset of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The ad_group_asset of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesAdGroupAsset
        """
        return self._ad_group_asset

    @ad_group_asset.setter
    def ad_group_asset(self, ad_group_asset):
        """Sets the ad_group_asset of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param ad_group_asset: The ad_group_asset of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type ad_group_asset: GoogleAdsSearchads360V0ResourcesAdGroupAsset
        """

        self._ad_group_asset = ad_group_asset

    @property
    def ad_group_asset_set(self):
        """Gets the ad_group_asset_set of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The ad_group_asset_set of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesAdGroupAssetSet
        """
        return self._ad_group_asset_set

    @ad_group_asset_set.setter
    def ad_group_asset_set(self, ad_group_asset_set):
        """Sets the ad_group_asset_set of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param ad_group_asset_set: The ad_group_asset_set of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type ad_group_asset_set: GoogleAdsSearchads360V0ResourcesAdGroupAssetSet
        """

        self._ad_group_asset_set = ad_group_asset_set

    @property
    def ad_group_audience_view(self):
        """Gets the ad_group_audience_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The ad_group_audience_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesAdGroupAudienceView
        """
        return self._ad_group_audience_view

    @ad_group_audience_view.setter
    def ad_group_audience_view(self, ad_group_audience_view):
        """Sets the ad_group_audience_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param ad_group_audience_view: The ad_group_audience_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type ad_group_audience_view: GoogleAdsSearchads360V0ResourcesAdGroupAudienceView
        """

        self._ad_group_audience_view = ad_group_audience_view

    @property
    def ad_group_bid_modifier(self):
        """Gets the ad_group_bid_modifier of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The ad_group_bid_modifier of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesAdGroupBidModifier
        """
        return self._ad_group_bid_modifier

    @ad_group_bid_modifier.setter
    def ad_group_bid_modifier(self, ad_group_bid_modifier):
        """Sets the ad_group_bid_modifier of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param ad_group_bid_modifier: The ad_group_bid_modifier of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type ad_group_bid_modifier: GoogleAdsSearchads360V0ResourcesAdGroupBidModifier
        """

        self._ad_group_bid_modifier = ad_group_bid_modifier

    @property
    def ad_group_criterion(self):
        """Gets the ad_group_criterion of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The ad_group_criterion of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesAdGroupCriterion
        """
        return self._ad_group_criterion

    @ad_group_criterion.setter
    def ad_group_criterion(self, ad_group_criterion):
        """Sets the ad_group_criterion of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param ad_group_criterion: The ad_group_criterion of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type ad_group_criterion: GoogleAdsSearchads360V0ResourcesAdGroupCriterion
        """

        self._ad_group_criterion = ad_group_criterion

    @property
    def ad_group_criterion_label(self):
        """Gets the ad_group_criterion_label of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The ad_group_criterion_label of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesAdGroupCriterionLabel
        """
        return self._ad_group_criterion_label

    @ad_group_criterion_label.setter
    def ad_group_criterion_label(self, ad_group_criterion_label):
        """Sets the ad_group_criterion_label of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param ad_group_criterion_label: The ad_group_criterion_label of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type ad_group_criterion_label: GoogleAdsSearchads360V0ResourcesAdGroupCriterionLabel
        """

        self._ad_group_criterion_label = ad_group_criterion_label

    @property
    def ad_group_label(self):
        """Gets the ad_group_label of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The ad_group_label of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesAdGroupLabel
        """
        return self._ad_group_label

    @ad_group_label.setter
    def ad_group_label(self, ad_group_label):
        """Sets the ad_group_label of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param ad_group_label: The ad_group_label of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type ad_group_label: GoogleAdsSearchads360V0ResourcesAdGroupLabel
        """

        self._ad_group_label = ad_group_label

    @property
    def age_range_view(self):
        """Gets the age_range_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The age_range_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesAgeRangeView
        """
        return self._age_range_view

    @age_range_view.setter
    def age_range_view(self, age_range_view):
        """Sets the age_range_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param age_range_view: The age_range_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type age_range_view: GoogleAdsSearchads360V0ResourcesAgeRangeView
        """

        self._age_range_view = age_range_view

    @property
    def asset(self):
        """Gets the asset of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The asset of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesAsset
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param asset: The asset of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type asset: GoogleAdsSearchads360V0ResourcesAsset
        """

        self._asset = asset

    @property
    def asset_group(self):
        """Gets the asset_group of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The asset_group of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesAssetGroup
        """
        return self._asset_group

    @asset_group.setter
    def asset_group(self, asset_group):
        """Sets the asset_group of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param asset_group: The asset_group of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type asset_group: GoogleAdsSearchads360V0ResourcesAssetGroup
        """

        self._asset_group = asset_group

    @property
    def asset_group_asset(self):
        """Gets the asset_group_asset of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The asset_group_asset of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesAssetGroupAsset
        """
        return self._asset_group_asset

    @asset_group_asset.setter
    def asset_group_asset(self, asset_group_asset):
        """Sets the asset_group_asset of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param asset_group_asset: The asset_group_asset of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type asset_group_asset: GoogleAdsSearchads360V0ResourcesAssetGroupAsset
        """

        self._asset_group_asset = asset_group_asset

    @property
    def asset_group_listing_group_filter(self):
        """Gets the asset_group_listing_group_filter of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The asset_group_listing_group_filter of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesAssetGroupListingGroupFilter
        """
        return self._asset_group_listing_group_filter

    @asset_group_listing_group_filter.setter
    def asset_group_listing_group_filter(self, asset_group_listing_group_filter):
        """Sets the asset_group_listing_group_filter of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param asset_group_listing_group_filter: The asset_group_listing_group_filter of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type asset_group_listing_group_filter: GoogleAdsSearchads360V0ResourcesAssetGroupListingGroupFilter
        """

        self._asset_group_listing_group_filter = asset_group_listing_group_filter

    @property
    def asset_group_signal(self):
        """Gets the asset_group_signal of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The asset_group_signal of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesAssetGroupSignal
        """
        return self._asset_group_signal

    @asset_group_signal.setter
    def asset_group_signal(self, asset_group_signal):
        """Sets the asset_group_signal of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param asset_group_signal: The asset_group_signal of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type asset_group_signal: GoogleAdsSearchads360V0ResourcesAssetGroupSignal
        """

        self._asset_group_signal = asset_group_signal

    @property
    def asset_group_top_combination_view(self):
        """Gets the asset_group_top_combination_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The asset_group_top_combination_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesAssetGroupTopCombinationView
        """
        return self._asset_group_top_combination_view

    @asset_group_top_combination_view.setter
    def asset_group_top_combination_view(self, asset_group_top_combination_view):
        """Sets the asset_group_top_combination_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param asset_group_top_combination_view: The asset_group_top_combination_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type asset_group_top_combination_view: GoogleAdsSearchads360V0ResourcesAssetGroupTopCombinationView
        """

        self._asset_group_top_combination_view = asset_group_top_combination_view

    @property
    def asset_set(self):
        """Gets the asset_set of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The asset_set of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesAssetSet
        """
        return self._asset_set

    @asset_set.setter
    def asset_set(self, asset_set):
        """Sets the asset_set of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param asset_set: The asset_set of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type asset_set: GoogleAdsSearchads360V0ResourcesAssetSet
        """

        self._asset_set = asset_set

    @property
    def asset_set_asset(self):
        """Gets the asset_set_asset of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The asset_set_asset of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesAssetSetAsset
        """
        return self._asset_set_asset

    @asset_set_asset.setter
    def asset_set_asset(self, asset_set_asset):
        """Sets the asset_set_asset of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param asset_set_asset: The asset_set_asset of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type asset_set_asset: GoogleAdsSearchads360V0ResourcesAssetSetAsset
        """

        self._asset_set_asset = asset_set_asset

    @property
    def audience(self):
        """Gets the audience of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The audience of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesAudience
        """
        return self._audience

    @audience.setter
    def audience(self, audience):
        """Sets the audience of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param audience: The audience of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type audience: GoogleAdsSearchads360V0ResourcesAudience
        """

        self._audience = audience

    @property
    def bidding_strategy(self):
        """Gets the bidding_strategy of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The bidding_strategy of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesBiddingStrategy
        """
        return self._bidding_strategy

    @bidding_strategy.setter
    def bidding_strategy(self, bidding_strategy):
        """Sets the bidding_strategy of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param bidding_strategy: The bidding_strategy of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type bidding_strategy: GoogleAdsSearchads360V0ResourcesBiddingStrategy
        """

        self._bidding_strategy = bidding_strategy

    @property
    def campaign(self):
        """Gets the campaign of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The campaign of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesCampaign
        """
        return self._campaign

    @campaign.setter
    def campaign(self, campaign):
        """Sets the campaign of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param campaign: The campaign of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type campaign: GoogleAdsSearchads360V0ResourcesCampaign
        """

        self._campaign = campaign

    @property
    def campaign_asset(self):
        """Gets the campaign_asset of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The campaign_asset of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesCampaignAsset
        """
        return self._campaign_asset

    @campaign_asset.setter
    def campaign_asset(self, campaign_asset):
        """Sets the campaign_asset of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param campaign_asset: The campaign_asset of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type campaign_asset: GoogleAdsSearchads360V0ResourcesCampaignAsset
        """

        self._campaign_asset = campaign_asset

    @property
    def campaign_asset_set(self):
        """Gets the campaign_asset_set of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The campaign_asset_set of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesCampaignAssetSet
        """
        return self._campaign_asset_set

    @campaign_asset_set.setter
    def campaign_asset_set(self, campaign_asset_set):
        """Sets the campaign_asset_set of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param campaign_asset_set: The campaign_asset_set of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type campaign_asset_set: GoogleAdsSearchads360V0ResourcesCampaignAssetSet
        """

        self._campaign_asset_set = campaign_asset_set

    @property
    def campaign_audience_view(self):
        """Gets the campaign_audience_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The campaign_audience_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesCampaignAudienceView
        """
        return self._campaign_audience_view

    @campaign_audience_view.setter
    def campaign_audience_view(self, campaign_audience_view):
        """Sets the campaign_audience_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param campaign_audience_view: The campaign_audience_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type campaign_audience_view: GoogleAdsSearchads360V0ResourcesCampaignAudienceView
        """

        self._campaign_audience_view = campaign_audience_view

    @property
    def campaign_budget(self):
        """Gets the campaign_budget of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The campaign_budget of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesCampaignBudget
        """
        return self._campaign_budget

    @campaign_budget.setter
    def campaign_budget(self, campaign_budget):
        """Sets the campaign_budget of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param campaign_budget: The campaign_budget of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type campaign_budget: GoogleAdsSearchads360V0ResourcesCampaignBudget
        """

        self._campaign_budget = campaign_budget

    @property
    def campaign_criterion(self):
        """Gets the campaign_criterion of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The campaign_criterion of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesCampaignCriterion
        """
        return self._campaign_criterion

    @campaign_criterion.setter
    def campaign_criterion(self, campaign_criterion):
        """Sets the campaign_criterion of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param campaign_criterion: The campaign_criterion of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type campaign_criterion: GoogleAdsSearchads360V0ResourcesCampaignCriterion
        """

        self._campaign_criterion = campaign_criterion

    @property
    def campaign_label(self):
        """Gets the campaign_label of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The campaign_label of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesCampaignLabel
        """
        return self._campaign_label

    @campaign_label.setter
    def campaign_label(self, campaign_label):
        """Sets the campaign_label of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param campaign_label: The campaign_label of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type campaign_label: GoogleAdsSearchads360V0ResourcesCampaignLabel
        """

        self._campaign_label = campaign_label

    @property
    def cart_data_sales_view(self):
        """Gets the cart_data_sales_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The cart_data_sales_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesCartDataSalesView
        """
        return self._cart_data_sales_view

    @cart_data_sales_view.setter
    def cart_data_sales_view(self, cart_data_sales_view):
        """Sets the cart_data_sales_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param cart_data_sales_view: The cart_data_sales_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type cart_data_sales_view: GoogleAdsSearchads360V0ResourcesCartDataSalesView
        """

        self._cart_data_sales_view = cart_data_sales_view

    @property
    def conversion(self):
        """Gets the conversion of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The conversion of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesConversion
        """
        return self._conversion

    @conversion.setter
    def conversion(self, conversion):
        """Sets the conversion of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param conversion: The conversion of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type conversion: GoogleAdsSearchads360V0ResourcesConversion
        """

        self._conversion = conversion

    @property
    def conversion_action(self):
        """Gets the conversion_action of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The conversion_action of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesConversionAction
        """
        return self._conversion_action

    @conversion_action.setter
    def conversion_action(self, conversion_action):
        """Sets the conversion_action of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param conversion_action: The conversion_action of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type conversion_action: GoogleAdsSearchads360V0ResourcesConversionAction
        """

        self._conversion_action = conversion_action

    @property
    def conversion_custom_variable(self):
        """Gets the conversion_custom_variable of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The conversion_custom_variable of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesConversionCustomVariable
        """
        return self._conversion_custom_variable

    @conversion_custom_variable.setter
    def conversion_custom_variable(self, conversion_custom_variable):
        """Sets the conversion_custom_variable of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param conversion_custom_variable: The conversion_custom_variable of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type conversion_custom_variable: GoogleAdsSearchads360V0ResourcesConversionCustomVariable
        """

        self._conversion_custom_variable = conversion_custom_variable

    @property
    def custom_columns(self):
        """Gets the custom_columns of this GoogleAdsSearchads360V0ServicesSearchAds360Row.

        The custom columns.

        :return: The custom_columns of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: List[GoogleAdsSearchads360V0CommonValue]
        """
        return self._custom_columns

    @custom_columns.setter
    def custom_columns(self, custom_columns):
        """Sets the custom_columns of this GoogleAdsSearchads360V0ServicesSearchAds360Row.

        The custom columns.

        :param custom_columns: The custom_columns of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type custom_columns: List[GoogleAdsSearchads360V0CommonValue]
        """

        self._custom_columns = custom_columns

    @property
    def customer(self):
        """Gets the customer of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The customer of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesCustomer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param customer: The customer of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type customer: GoogleAdsSearchads360V0ResourcesCustomer
        """

        self._customer = customer

    @property
    def customer_asset(self):
        """Gets the customer_asset of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The customer_asset of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesCustomerAsset
        """
        return self._customer_asset

    @customer_asset.setter
    def customer_asset(self, customer_asset):
        """Sets the customer_asset of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param customer_asset: The customer_asset of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type customer_asset: GoogleAdsSearchads360V0ResourcesCustomerAsset
        """

        self._customer_asset = customer_asset

    @property
    def customer_asset_set(self):
        """Gets the customer_asset_set of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The customer_asset_set of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesCustomerAssetSet
        """
        return self._customer_asset_set

    @customer_asset_set.setter
    def customer_asset_set(self, customer_asset_set):
        """Sets the customer_asset_set of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param customer_asset_set: The customer_asset_set of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type customer_asset_set: GoogleAdsSearchads360V0ResourcesCustomerAssetSet
        """

        self._customer_asset_set = customer_asset_set

    @property
    def customer_client(self):
        """Gets the customer_client of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The customer_client of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesCustomerClient
        """
        return self._customer_client

    @customer_client.setter
    def customer_client(self, customer_client):
        """Sets the customer_client of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param customer_client: The customer_client of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type customer_client: GoogleAdsSearchads360V0ResourcesCustomerClient
        """

        self._customer_client = customer_client

    @property
    def customer_manager_link(self):
        """Gets the customer_manager_link of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The customer_manager_link of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesCustomerManagerLink
        """
        return self._customer_manager_link

    @customer_manager_link.setter
    def customer_manager_link(self, customer_manager_link):
        """Sets the customer_manager_link of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param customer_manager_link: The customer_manager_link of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type customer_manager_link: GoogleAdsSearchads360V0ResourcesCustomerManagerLink
        """

        self._customer_manager_link = customer_manager_link

    @property
    def dynamic_search_ads_search_term_view(self):
        """Gets the dynamic_search_ads_search_term_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The dynamic_search_ads_search_term_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesDynamicSearchAdsSearchTermView
        """
        return self._dynamic_search_ads_search_term_view

    @dynamic_search_ads_search_term_view.setter
    def dynamic_search_ads_search_term_view(self, dynamic_search_ads_search_term_view):
        """Sets the dynamic_search_ads_search_term_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param dynamic_search_ads_search_term_view: The dynamic_search_ads_search_term_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type dynamic_search_ads_search_term_view: GoogleAdsSearchads360V0ResourcesDynamicSearchAdsSearchTermView
        """

        self._dynamic_search_ads_search_term_view = dynamic_search_ads_search_term_view

    @property
    def gender_view(self):
        """Gets the gender_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The gender_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesGenderView
        """
        return self._gender_view

    @gender_view.setter
    def gender_view(self, gender_view):
        """Sets the gender_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param gender_view: The gender_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type gender_view: GoogleAdsSearchads360V0ResourcesGenderView
        """

        self._gender_view = gender_view

    @property
    def geo_target_constant(self):
        """Gets the geo_target_constant of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The geo_target_constant of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesGeoTargetConstant
        """
        return self._geo_target_constant

    @geo_target_constant.setter
    def geo_target_constant(self, geo_target_constant):
        """Sets the geo_target_constant of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param geo_target_constant: The geo_target_constant of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type geo_target_constant: GoogleAdsSearchads360V0ResourcesGeoTargetConstant
        """

        self._geo_target_constant = geo_target_constant

    @property
    def keyword_view(self):
        """Gets the keyword_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The keyword_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesKeywordView
        """
        return self._keyword_view

    @keyword_view.setter
    def keyword_view(self, keyword_view):
        """Sets the keyword_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param keyword_view: The keyword_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type keyword_view: GoogleAdsSearchads360V0ResourcesKeywordView
        """

        self._keyword_view = keyword_view

    @property
    def label(self):
        """Gets the label of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The label of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesLabel
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param label: The label of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type label: GoogleAdsSearchads360V0ResourcesLabel
        """

        self._label = label

    @property
    def language_constant(self):
        """Gets the language_constant of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The language_constant of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesLanguageConstant
        """
        return self._language_constant

    @language_constant.setter
    def language_constant(self, language_constant):
        """Sets the language_constant of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param language_constant: The language_constant of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type language_constant: GoogleAdsSearchads360V0ResourcesLanguageConstant
        """

        self._language_constant = language_constant

    @property
    def location_view(self):
        """Gets the location_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The location_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesLocationView
        """
        return self._location_view

    @location_view.setter
    def location_view(self, location_view):
        """Sets the location_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param location_view: The location_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type location_view: GoogleAdsSearchads360V0ResourcesLocationView
        """

        self._location_view = location_view

    @property
    def metrics(self):
        """Gets the metrics of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The metrics of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0CommonMetrics
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param metrics: The metrics of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type metrics: GoogleAdsSearchads360V0CommonMetrics
        """

        self._metrics = metrics

    @property
    def product_bidding_category_constant(self):
        """Gets the product_bidding_category_constant of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The product_bidding_category_constant of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesProductBiddingCategoryConstant
        """
        return self._product_bidding_category_constant

    @product_bidding_category_constant.setter
    def product_bidding_category_constant(self, product_bidding_category_constant):
        """Sets the product_bidding_category_constant of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param product_bidding_category_constant: The product_bidding_category_constant of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type product_bidding_category_constant: GoogleAdsSearchads360V0ResourcesProductBiddingCategoryConstant
        """

        self._product_bidding_category_constant = product_bidding_category_constant

    @property
    def product_group_view(self):
        """Gets the product_group_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The product_group_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesProductGroupView
        """
        return self._product_group_view

    @product_group_view.setter
    def product_group_view(self, product_group_view):
        """Sets the product_group_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param product_group_view: The product_group_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type product_group_view: GoogleAdsSearchads360V0ResourcesProductGroupView
        """

        self._product_group_view = product_group_view

    @property
    def segments(self):
        """Gets the segments of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The segments of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0CommonSegments
        """
        return self._segments

    @segments.setter
    def segments(self, segments):
        """Sets the segments of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param segments: The segments of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type segments: GoogleAdsSearchads360V0CommonSegments
        """

        self._segments = segments

    @property
    def shopping_performance_view(self):
        """Gets the shopping_performance_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The shopping_performance_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesShoppingPerformanceView
        """
        return self._shopping_performance_view

    @shopping_performance_view.setter
    def shopping_performance_view(self, shopping_performance_view):
        """Sets the shopping_performance_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param shopping_performance_view: The shopping_performance_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type shopping_performance_view: GoogleAdsSearchads360V0ResourcesShoppingPerformanceView
        """

        self._shopping_performance_view = shopping_performance_view

    @property
    def user_list(self):
        """Gets the user_list of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The user_list of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesUserList
        """
        return self._user_list

    @user_list.setter
    def user_list(self, user_list):
        """Sets the user_list of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param user_list: The user_list of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type user_list: GoogleAdsSearchads360V0ResourcesUserList
        """

        self._user_list = user_list

    @property
    def visit(self):
        """Gets the visit of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The visit of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesVisit
        """
        return self._visit

    @visit.setter
    def visit(self, visit):
        """Sets the visit of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param visit: The visit of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type visit: GoogleAdsSearchads360V0ResourcesVisit
        """

        self._visit = visit

    @property
    def webpage_view(self):
        """Gets the webpage_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :return: The webpage_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :rtype: GoogleAdsSearchads360V0ResourcesWebpageView
        """
        return self._webpage_view

    @webpage_view.setter
    def webpage_view(self, webpage_view):
        """Sets the webpage_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.


        :param webpage_view: The webpage_view of this GoogleAdsSearchads360V0ServicesSearchAds360Row.
        :type webpage_view: GoogleAdsSearchads360V0ResourcesWebpageView
        """

        self._webpage_view = webpage_view
