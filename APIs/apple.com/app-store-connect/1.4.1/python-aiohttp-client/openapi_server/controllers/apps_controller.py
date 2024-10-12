from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_beta_testers_linkages_request import AppBetaTestersLinkagesRequest
from openapi_server.models.app_infos_response import AppInfosResponse
from openapi_server.models.app_pre_order_response import AppPreOrderResponse
from openapi_server.models.app_prices_response import AppPricesResponse
from openapi_server.models.app_response import AppResponse
from openapi_server.models.app_store_versions_response import AppStoreVersionsResponse
from openapi_server.models.app_update_request import AppUpdateRequest
from openapi_server.models.apps_response import AppsResponse
from openapi_server.models.beta_app_localizations_response import BetaAppLocalizationsResponse
from openapi_server.models.beta_app_review_detail_response import BetaAppReviewDetailResponse
from openapi_server.models.beta_groups_response import BetaGroupsResponse
from openapi_server.models.beta_license_agreement_response import BetaLicenseAgreementResponse
from openapi_server.models.builds_response import BuildsResponse
from openapi_server.models.end_user_license_agreement_response import EndUserLicenseAgreementResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.game_center_enabled_versions_response import GameCenterEnabledVersionsResponse
from openapi_server.models.in_app_purchases_response import InAppPurchasesResponse
from openapi_server.models.perf_power_metrics_response import PerfPowerMetricsResponse
from openapi_server.models.pre_release_versions_response import PreReleaseVersionsResponse
from openapi_server.models.territories_response import TerritoriesResponse
from openapi_server import util


async def apps_app_infos_get_to_many_related(request: web.Request, id, fields_age_rating_declarations=None, fields_app_infos=None, fields_app_categories=None, fields_app_info_localizations=None, fields_apps=None, limit=None, include=None) -> web.Response:
    """apps_app_infos_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_age_rating_declarations: the fields to include for returned resources of type ageRatingDeclarations
    :type fields_age_rating_declarations: List[str]
    :param fields_app_infos: the fields to include for returned resources of type appInfos
    :type fields_app_infos: List[str]
    :param fields_app_categories: the fields to include for returned resources of type appCategories
    :type fields_app_categories: List[str]
    :param fields_app_info_localizations: the fields to include for returned resources of type appInfoLocalizations
    :type fields_app_info_localizations: List[str]
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]
    :param limit: maximum resources per page
    :type limit: int
    :param include: comma-separated list of relationships to include
    :type include: List[str]

    """
    return web.Response(status=200)


async def apps_app_store_versions_get_to_many_related(request: web.Request, id, filter_app_store_state=None, filter_platform=None, filter_version_string=None, filter_id=None, fields_idfa_declarations=None, fields_app_store_version_localizations=None, fields_routing_app_coverages=None, fields_app_store_version_phased_releases=None, fields_age_rating_declarations=None, fields_app_store_review_details=None, fields_app_store_versions=None, fields_builds=None, fields_app_store_version_submissions=None, fields_apps=None, limit=None, include=None) -> web.Response:
    """apps_app_store_versions_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param filter_app_store_state: filter by attribute &#39;appStoreState&#39;
    :type filter_app_store_state: List[str]
    :param filter_platform: filter by attribute &#39;platform&#39;
    :type filter_platform: List[str]
    :param filter_version_string: filter by attribute &#39;versionString&#39;
    :type filter_version_string: List[str]
    :param filter_id: filter by id(s)
    :type filter_id: List[str]
    :param fields_idfa_declarations: the fields to include for returned resources of type idfaDeclarations
    :type fields_idfa_declarations: List[str]
    :param fields_app_store_version_localizations: the fields to include for returned resources of type appStoreVersionLocalizations
    :type fields_app_store_version_localizations: List[str]
    :param fields_routing_app_coverages: the fields to include for returned resources of type routingAppCoverages
    :type fields_routing_app_coverages: List[str]
    :param fields_app_store_version_phased_releases: the fields to include for returned resources of type appStoreVersionPhasedReleases
    :type fields_app_store_version_phased_releases: List[str]
    :param fields_age_rating_declarations: the fields to include for returned resources of type ageRatingDeclarations
    :type fields_age_rating_declarations: List[str]
    :param fields_app_store_review_details: the fields to include for returned resources of type appStoreReviewDetails
    :type fields_app_store_review_details: List[str]
    :param fields_app_store_versions: the fields to include for returned resources of type appStoreVersions
    :type fields_app_store_versions: List[str]
    :param fields_builds: the fields to include for returned resources of type builds
    :type fields_builds: List[str]
    :param fields_app_store_version_submissions: the fields to include for returned resources of type appStoreVersionSubmissions
    :type fields_app_store_version_submissions: List[str]
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]
    :param limit: maximum resources per page
    :type limit: int
    :param include: comma-separated list of relationships to include
    :type include: List[str]

    """
    return web.Response(status=200)


async def apps_available_territories_get_to_many_related(request: web.Request, id, fields_territories=None, limit=None) -> web.Response:
    """apps_available_territories_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_territories: the fields to include for returned resources of type territories
    :type fields_territories: List[str]
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)


async def apps_beta_app_localizations_get_to_many_related(request: web.Request, id, fields_beta_app_localizations=None, limit=None) -> web.Response:
    """apps_beta_app_localizations_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_beta_app_localizations: the fields to include for returned resources of type betaAppLocalizations
    :type fields_beta_app_localizations: List[str]
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)


async def apps_beta_app_review_detail_get_to_one_related(request: web.Request, id, fields_beta_app_review_details=None) -> web.Response:
    """apps_beta_app_review_detail_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_beta_app_review_details: the fields to include for returned resources of type betaAppReviewDetails
    :type fields_beta_app_review_details: List[str]

    """
    return web.Response(status=200)


async def apps_beta_groups_get_to_many_related(request: web.Request, id, fields_beta_groups=None, limit=None) -> web.Response:
    """apps_beta_groups_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_beta_groups: the fields to include for returned resources of type betaGroups
    :type fields_beta_groups: List[str]
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)


async def apps_beta_license_agreement_get_to_one_related(request: web.Request, id, fields_beta_license_agreements=None) -> web.Response:
    """apps_beta_license_agreement_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_beta_license_agreements: the fields to include for returned resources of type betaLicenseAgreements
    :type fields_beta_license_agreements: List[str]

    """
    return web.Response(status=200)


async def apps_beta_testers_delete_to_many_relationship(request: web.Request, id, body) -> web.Response:
    """apps_beta_testers_delete_to_many_relationship

    

    :param id: the id of the requested resource
    :type id: str
    :param body: List of related linkages
    :type body: dict | bytes

    """
    body = AppBetaTestersLinkagesRequest.from_dict(body)
    return web.Response(status=200)


async def apps_builds_get_to_many_related(request: web.Request, id, fields_builds=None, limit=None) -> web.Response:
    """apps_builds_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_builds: the fields to include for returned resources of type builds
    :type fields_builds: List[str]
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)


async def apps_end_user_license_agreement_get_to_one_related(request: web.Request, id, fields_end_user_license_agreements=None) -> web.Response:
    """apps_end_user_license_agreement_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_end_user_license_agreements: the fields to include for returned resources of type endUserLicenseAgreements
    :type fields_end_user_license_agreements: List[str]

    """
    return web.Response(status=200)


async def apps_game_center_enabled_versions_get_to_many_related(request: web.Request, id, filter_platform=None, filter_version_string=None, filter_id=None, sort=None, fields_game_center_enabled_versions=None, fields_apps=None, limit=None, include=None) -> web.Response:
    """apps_game_center_enabled_versions_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param filter_platform: filter by attribute &#39;platform&#39;
    :type filter_platform: List[str]
    :param filter_version_string: filter by attribute &#39;versionString&#39;
    :type filter_version_string: List[str]
    :param filter_id: filter by id(s)
    :type filter_id: List[str]
    :param sort: comma-separated list of sort expressions; resources will be sorted as specified
    :type sort: List[str]
    :param fields_game_center_enabled_versions: the fields to include for returned resources of type gameCenterEnabledVersions
    :type fields_game_center_enabled_versions: List[str]
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]
    :param limit: maximum resources per page
    :type limit: int
    :param include: comma-separated list of relationships to include
    :type include: List[str]

    """
    return web.Response(status=200)


async def apps_get_collection(request: web.Request, filter_app_store_versions_app_store_state=None, filter_app_store_versions_platform=None, filter_bundle_id=None, filter_name=None, filter_sku=None, filter_app_store_versions=None, filter_id=None, exists_game_center_enabled_versions=None, sort=None, fields_apps=None, limit=None, include=None, fields_beta_groups=None, fields_perf_power_metrics=None, fields_app_infos=None, fields_app_pre_orders=None, fields_pre_release_versions=None, fields_app_prices=None, fields_in_app_purchases=None, fields_beta_app_review_details=None, fields_territories=None, fields_game_center_enabled_versions=None, fields_app_store_versions=None, fields_builds=None, fields_beta_app_localizations=None, fields_beta_license_agreements=None, fields_end_user_license_agreements=None, limit_app_infos=None, limit_app_store_versions=None, limit_available_territories=None, limit_beta_app_localizations=None, limit_beta_groups=None, limit_builds=None, limit_game_center_enabled_versions=None, limit_in_app_purchases=None, limit_pre_release_versions=None, limit_prices=None) -> web.Response:
    """apps_get_collection

    

    :param filter_app_store_versions_app_store_state: filter by attribute &#39;appStoreVersions.appStoreState&#39;
    :type filter_app_store_versions_app_store_state: List[str]
    :param filter_app_store_versions_platform: filter by attribute &#39;appStoreVersions.platform&#39;
    :type filter_app_store_versions_platform: List[str]
    :param filter_bundle_id: filter by attribute &#39;bundleId&#39;
    :type filter_bundle_id: List[str]
    :param filter_name: filter by attribute &#39;name&#39;
    :type filter_name: List[str]
    :param filter_sku: filter by attribute &#39;sku&#39;
    :type filter_sku: List[str]
    :param filter_app_store_versions: filter by id(s) of related &#39;appStoreVersions&#39;
    :type filter_app_store_versions: List[str]
    :param filter_id: filter by id(s)
    :type filter_id: List[str]
    :param exists_game_center_enabled_versions: filter by existence or non-existence of related &#39;gameCenterEnabledVersions&#39;
    :type exists_game_center_enabled_versions: List[str]
    :param sort: comma-separated list of sort expressions; resources will be sorted as specified
    :type sort: List[str]
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]
    :param limit: maximum resources per page
    :type limit: int
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_beta_groups: the fields to include for returned resources of type betaGroups
    :type fields_beta_groups: List[str]
    :param fields_perf_power_metrics: the fields to include for returned resources of type perfPowerMetrics
    :type fields_perf_power_metrics: List[str]
    :param fields_app_infos: the fields to include for returned resources of type appInfos
    :type fields_app_infos: List[str]
    :param fields_app_pre_orders: the fields to include for returned resources of type appPreOrders
    :type fields_app_pre_orders: List[str]
    :param fields_pre_release_versions: the fields to include for returned resources of type preReleaseVersions
    :type fields_pre_release_versions: List[str]
    :param fields_app_prices: the fields to include for returned resources of type appPrices
    :type fields_app_prices: List[str]
    :param fields_in_app_purchases: the fields to include for returned resources of type inAppPurchases
    :type fields_in_app_purchases: List[str]
    :param fields_beta_app_review_details: the fields to include for returned resources of type betaAppReviewDetails
    :type fields_beta_app_review_details: List[str]
    :param fields_territories: the fields to include for returned resources of type territories
    :type fields_territories: List[str]
    :param fields_game_center_enabled_versions: the fields to include for returned resources of type gameCenterEnabledVersions
    :type fields_game_center_enabled_versions: List[str]
    :param fields_app_store_versions: the fields to include for returned resources of type appStoreVersions
    :type fields_app_store_versions: List[str]
    :param fields_builds: the fields to include for returned resources of type builds
    :type fields_builds: List[str]
    :param fields_beta_app_localizations: the fields to include for returned resources of type betaAppLocalizations
    :type fields_beta_app_localizations: List[str]
    :param fields_beta_license_agreements: the fields to include for returned resources of type betaLicenseAgreements
    :type fields_beta_license_agreements: List[str]
    :param fields_end_user_license_agreements: the fields to include for returned resources of type endUserLicenseAgreements
    :type fields_end_user_license_agreements: List[str]
    :param limit_app_infos: maximum number of related appInfos returned (when they are included)
    :type limit_app_infos: int
    :param limit_app_store_versions: maximum number of related appStoreVersions returned (when they are included)
    :type limit_app_store_versions: int
    :param limit_available_territories: maximum number of related availableTerritories returned (when they are included)
    :type limit_available_territories: int
    :param limit_beta_app_localizations: maximum number of related betaAppLocalizations returned (when they are included)
    :type limit_beta_app_localizations: int
    :param limit_beta_groups: maximum number of related betaGroups returned (when they are included)
    :type limit_beta_groups: int
    :param limit_builds: maximum number of related builds returned (when they are included)
    :type limit_builds: int
    :param limit_game_center_enabled_versions: maximum number of related gameCenterEnabledVersions returned (when they are included)
    :type limit_game_center_enabled_versions: int
    :param limit_in_app_purchases: maximum number of related inAppPurchases returned (when they are included)
    :type limit_in_app_purchases: int
    :param limit_pre_release_versions: maximum number of related preReleaseVersions returned (when they are included)
    :type limit_pre_release_versions: int
    :param limit_prices: maximum number of related prices returned (when they are included)
    :type limit_prices: int

    """
    return web.Response(status=200)


async def apps_get_instance(request: web.Request, id, fields_apps=None, include=None, fields_beta_groups=None, fields_perf_power_metrics=None, fields_app_infos=None, fields_app_pre_orders=None, fields_pre_release_versions=None, fields_app_prices=None, fields_in_app_purchases=None, fields_beta_app_review_details=None, fields_territories=None, fields_game_center_enabled_versions=None, fields_app_store_versions=None, fields_builds=None, fields_beta_app_localizations=None, fields_beta_license_agreements=None, fields_end_user_license_agreements=None, limit_app_infos=None, limit_app_store_versions=None, limit_available_territories=None, limit_beta_app_localizations=None, limit_beta_groups=None, limit_builds=None, limit_game_center_enabled_versions=None, limit_in_app_purchases=None, limit_pre_release_versions=None, limit_prices=None) -> web.Response:
    """apps_get_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_beta_groups: the fields to include for returned resources of type betaGroups
    :type fields_beta_groups: List[str]
    :param fields_perf_power_metrics: the fields to include for returned resources of type perfPowerMetrics
    :type fields_perf_power_metrics: List[str]
    :param fields_app_infos: the fields to include for returned resources of type appInfos
    :type fields_app_infos: List[str]
    :param fields_app_pre_orders: the fields to include for returned resources of type appPreOrders
    :type fields_app_pre_orders: List[str]
    :param fields_pre_release_versions: the fields to include for returned resources of type preReleaseVersions
    :type fields_pre_release_versions: List[str]
    :param fields_app_prices: the fields to include for returned resources of type appPrices
    :type fields_app_prices: List[str]
    :param fields_in_app_purchases: the fields to include for returned resources of type inAppPurchases
    :type fields_in_app_purchases: List[str]
    :param fields_beta_app_review_details: the fields to include for returned resources of type betaAppReviewDetails
    :type fields_beta_app_review_details: List[str]
    :param fields_territories: the fields to include for returned resources of type territories
    :type fields_territories: List[str]
    :param fields_game_center_enabled_versions: the fields to include for returned resources of type gameCenterEnabledVersions
    :type fields_game_center_enabled_versions: List[str]
    :param fields_app_store_versions: the fields to include for returned resources of type appStoreVersions
    :type fields_app_store_versions: List[str]
    :param fields_builds: the fields to include for returned resources of type builds
    :type fields_builds: List[str]
    :param fields_beta_app_localizations: the fields to include for returned resources of type betaAppLocalizations
    :type fields_beta_app_localizations: List[str]
    :param fields_beta_license_agreements: the fields to include for returned resources of type betaLicenseAgreements
    :type fields_beta_license_agreements: List[str]
    :param fields_end_user_license_agreements: the fields to include for returned resources of type endUserLicenseAgreements
    :type fields_end_user_license_agreements: List[str]
    :param limit_app_infos: maximum number of related appInfos returned (when they are included)
    :type limit_app_infos: int
    :param limit_app_store_versions: maximum number of related appStoreVersions returned (when they are included)
    :type limit_app_store_versions: int
    :param limit_available_territories: maximum number of related availableTerritories returned (when they are included)
    :type limit_available_territories: int
    :param limit_beta_app_localizations: maximum number of related betaAppLocalizations returned (when they are included)
    :type limit_beta_app_localizations: int
    :param limit_beta_groups: maximum number of related betaGroups returned (when they are included)
    :type limit_beta_groups: int
    :param limit_builds: maximum number of related builds returned (when they are included)
    :type limit_builds: int
    :param limit_game_center_enabled_versions: maximum number of related gameCenterEnabledVersions returned (when they are included)
    :type limit_game_center_enabled_versions: int
    :param limit_in_app_purchases: maximum number of related inAppPurchases returned (when they are included)
    :type limit_in_app_purchases: int
    :param limit_pre_release_versions: maximum number of related preReleaseVersions returned (when they are included)
    :type limit_pre_release_versions: int
    :param limit_prices: maximum number of related prices returned (when they are included)
    :type limit_prices: int

    """
    return web.Response(status=200)


async def apps_in_app_purchases_get_to_many_related(request: web.Request, id, filter_in_app_purchase_type=None, filter_can_be_submitted=None, sort=None, fields_in_app_purchases=None, fields_apps=None, limit=None, include=None) -> web.Response:
    """apps_in_app_purchases_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param filter_in_app_purchase_type: filter by attribute &#39;inAppPurchaseType&#39;
    :type filter_in_app_purchase_type: List[str]
    :param filter_can_be_submitted: filter by canBeSubmitted
    :type filter_can_be_submitted: List[str]
    :param sort: comma-separated list of sort expressions; resources will be sorted as specified
    :type sort: List[str]
    :param fields_in_app_purchases: the fields to include for returned resources of type inAppPurchases
    :type fields_in_app_purchases: List[str]
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]
    :param limit: maximum resources per page
    :type limit: int
    :param include: comma-separated list of relationships to include
    :type include: List[str]

    """
    return web.Response(status=200)


async def apps_perf_power_metrics_get_to_many_related(request: web.Request, id, filter_device_type=None, filter_metric_type=None, filter_platform=None) -> web.Response:
    """apps_perf_power_metrics_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param filter_device_type: filter by attribute &#39;deviceType&#39;
    :type filter_device_type: List[str]
    :param filter_metric_type: filter by attribute &#39;metricType&#39;
    :type filter_metric_type: List[str]
    :param filter_platform: filter by attribute &#39;platform&#39;
    :type filter_platform: List[str]

    """
    return web.Response(status=200)


async def apps_pre_order_get_to_one_related(request: web.Request, id, fields_app_pre_orders=None) -> web.Response:
    """apps_pre_order_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_pre_orders: the fields to include for returned resources of type appPreOrders
    :type fields_app_pre_orders: List[str]

    """
    return web.Response(status=200)


async def apps_pre_release_versions_get_to_many_related(request: web.Request, id, fields_pre_release_versions=None, limit=None) -> web.Response:
    """apps_pre_release_versions_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_pre_release_versions: the fields to include for returned resources of type preReleaseVersions
    :type fields_pre_release_versions: List[str]
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)


async def apps_prices_get_to_many_related(request: web.Request, id, fields_app_prices=None, fields_app_price_tiers=None, fields_apps=None, limit=None, include=None) -> web.Response:
    """apps_prices_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_prices: the fields to include for returned resources of type appPrices
    :type fields_app_prices: List[str]
    :param fields_app_price_tiers: the fields to include for returned resources of type appPriceTiers
    :type fields_app_price_tiers: List[str]
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]
    :param limit: maximum resources per page
    :type limit: int
    :param include: comma-separated list of relationships to include
    :type include: List[str]

    """
    return web.Response(status=200)


async def apps_update_instance(request: web.Request, id, body) -> web.Response:
    """apps_update_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param body: App representation
    :type body: dict | bytes

    """
    body = AppUpdateRequest.from_dict(body)
    return web.Response(status=200)
