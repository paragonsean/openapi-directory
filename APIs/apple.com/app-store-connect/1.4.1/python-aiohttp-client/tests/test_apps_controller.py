# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_apps_app_infos_get_to_many_related(client):
    """Test case for apps_app_infos_get_to_many_related

    
    """
    params = [('fields[ageRatingDeclarations]', ['fields_age_rating_declarations_example']),
                    ('fields[appInfos]', ['fields_app_infos_example']),
                    ('fields[appCategories]', ['fields_app_categories_example']),
                    ('fields[appInfoLocalizations]', ['fields_app_info_localizations_example']),
                    ('fields[apps]', ['fields_apps_example']),
                    ('limit', 56),
                    ('include', ['include_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/apps/{id}/appInfos'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_app_store_versions_get_to_many_related(client):
    """Test case for apps_app_store_versions_get_to_many_related

    
    """
    params = [('filter[appStoreState]', ['filter_app_store_state_example']),
                    ('filter[platform]', ['filter_platform_example']),
                    ('filter[versionString]', ['filter_version_string_example']),
                    ('filter[id]', ['filter_id_example']),
                    ('fields[idfaDeclarations]', ['fields_idfa_declarations_example']),
                    ('fields[appStoreVersionLocalizations]', ['fields_app_store_version_localizations_example']),
                    ('fields[routingAppCoverages]', ['fields_routing_app_coverages_example']),
                    ('fields[appStoreVersionPhasedReleases]', ['fields_app_store_version_phased_releases_example']),
                    ('fields[ageRatingDeclarations]', ['fields_age_rating_declarations_example']),
                    ('fields[appStoreReviewDetails]', ['fields_app_store_review_details_example']),
                    ('fields[appStoreVersions]', ['fields_app_store_versions_example']),
                    ('fields[builds]', ['fields_builds_example']),
                    ('fields[appStoreVersionSubmissions]', ['fields_app_store_version_submissions_example']),
                    ('fields[apps]', ['fields_apps_example']),
                    ('limit', 56),
                    ('include', ['include_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/apps/{id}/appStoreVersions'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_available_territories_get_to_many_related(client):
    """Test case for apps_available_territories_get_to_many_related

    
    """
    params = [('fields[territories]', ['fields_territories_example']),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/apps/{id}/availableTerritories'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_beta_app_localizations_get_to_many_related(client):
    """Test case for apps_beta_app_localizations_get_to_many_related

    
    """
    params = [('fields[betaAppLocalizations]', ['fields_beta_app_localizations_example']),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/apps/{id}/betaAppLocalizations'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_beta_app_review_detail_get_to_one_related(client):
    """Test case for apps_beta_app_review_detail_get_to_one_related

    
    """
    params = [('fields[betaAppReviewDetails]', ['fields_beta_app_review_details_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/apps/{id}/betaAppReviewDetail'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_beta_groups_get_to_many_related(client):
    """Test case for apps_beta_groups_get_to_many_related

    
    """
    params = [('fields[betaGroups]', ['fields_beta_groups_example']),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/apps/{id}/betaGroups'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_beta_license_agreement_get_to_one_related(client):
    """Test case for apps_beta_license_agreement_get_to_one_related

    
    """
    params = [('fields[betaLicenseAgreements]', ['fields_beta_license_agreements_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/apps/{id}/betaLicenseAgreement'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_beta_testers_delete_to_many_relationship(client):
    """Test case for apps_beta_testers_delete_to_many_relationship

    
    """
    body = {"data":[{"id":"id","type":"betaTesters"},{"id":"id","type":"betaTesters"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/apps/{id}/relationships/betaTesters'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_builds_get_to_many_related(client):
    """Test case for apps_builds_get_to_many_related

    
    """
    params = [('fields[builds]', ['fields_builds_example']),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/apps/{id}/builds'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_end_user_license_agreement_get_to_one_related(client):
    """Test case for apps_end_user_license_agreement_get_to_one_related

    
    """
    params = [('fields[endUserLicenseAgreements]', ['fields_end_user_license_agreements_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/apps/{id}/endUserLicenseAgreement'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_game_center_enabled_versions_get_to_many_related(client):
    """Test case for apps_game_center_enabled_versions_get_to_many_related

    
    """
    params = [('filter[platform]', ['filter_platform_example']),
                    ('filter[versionString]', ['filter_version_string_example']),
                    ('filter[id]', ['filter_id_example']),
                    ('sort', ['sort_example']),
                    ('fields[gameCenterEnabledVersions]', ['fields_game_center_enabled_versions_example']),
                    ('fields[apps]', ['fields_apps_example']),
                    ('limit', 56),
                    ('include', ['include_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/apps/{id}/gameCenterEnabledVersions'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_get_collection(client):
    """Test case for apps_get_collection

    
    """
    params = [('filter[appStoreVersions.appStoreState]', ['filter_app_store_versions_app_store_state_example']),
                    ('filter[appStoreVersions.platform]', ['filter_app_store_versions_platform_example']),
                    ('filter[bundleId]', ['filter_bundle_id_example']),
                    ('filter[name]', ['filter_name_example']),
                    ('filter[sku]', ['filter_sku_example']),
                    ('filter[appStoreVersions]', ['filter_app_store_versions_example']),
                    ('filter[id]', ['filter_id_example']),
                    ('exists[gameCenterEnabledVersions]', ['exists_game_center_enabled_versions_example']),
                    ('sort', ['sort_example']),
                    ('fields[apps]', ['fields_apps_example']),
                    ('limit', 56),
                    ('include', ['include_example']),
                    ('fields[betaGroups]', ['fields_beta_groups_example']),
                    ('fields[perfPowerMetrics]', ['fields_perf_power_metrics_example']),
                    ('fields[appInfos]', ['fields_app_infos_example']),
                    ('fields[appPreOrders]', ['fields_app_pre_orders_example']),
                    ('fields[preReleaseVersions]', ['fields_pre_release_versions_example']),
                    ('fields[appPrices]', ['fields_app_prices_example']),
                    ('fields[inAppPurchases]', ['fields_in_app_purchases_example']),
                    ('fields[betaAppReviewDetails]', ['fields_beta_app_review_details_example']),
                    ('fields[territories]', ['fields_territories_example']),
                    ('fields[gameCenterEnabledVersions]', ['fields_game_center_enabled_versions_example']),
                    ('fields[appStoreVersions]', ['fields_app_store_versions_example']),
                    ('fields[builds]', ['fields_builds_example']),
                    ('fields[betaAppLocalizations]', ['fields_beta_app_localizations_example']),
                    ('fields[betaLicenseAgreements]', ['fields_beta_license_agreements_example']),
                    ('fields[endUserLicenseAgreements]', ['fields_end_user_license_agreements_example']),
                    ('limit[appInfos]', 56),
                    ('limit[appStoreVersions]', 56),
                    ('limit[availableTerritories]', 56),
                    ('limit[betaAppLocalizations]', 56),
                    ('limit[betaGroups]', 56),
                    ('limit[builds]', 56),
                    ('limit[gameCenterEnabledVersions]', 56),
                    ('limit[inAppPurchases]', 56),
                    ('limit[preReleaseVersions]', 56),
                    ('limit[prices]', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/apps',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_get_instance(client):
    """Test case for apps_get_instance

    
    """
    params = [('fields[apps]', ['fields_apps_example']),
                    ('include', ['include_example']),
                    ('fields[betaGroups]', ['fields_beta_groups_example']),
                    ('fields[perfPowerMetrics]', ['fields_perf_power_metrics_example']),
                    ('fields[appInfos]', ['fields_app_infos_example']),
                    ('fields[appPreOrders]', ['fields_app_pre_orders_example']),
                    ('fields[preReleaseVersions]', ['fields_pre_release_versions_example']),
                    ('fields[appPrices]', ['fields_app_prices_example']),
                    ('fields[inAppPurchases]', ['fields_in_app_purchases_example']),
                    ('fields[betaAppReviewDetails]', ['fields_beta_app_review_details_example']),
                    ('fields[territories]', ['fields_territories_example']),
                    ('fields[gameCenterEnabledVersions]', ['fields_game_center_enabled_versions_example']),
                    ('fields[appStoreVersions]', ['fields_app_store_versions_example']),
                    ('fields[builds]', ['fields_builds_example']),
                    ('fields[betaAppLocalizations]', ['fields_beta_app_localizations_example']),
                    ('fields[betaLicenseAgreements]', ['fields_beta_license_agreements_example']),
                    ('fields[endUserLicenseAgreements]', ['fields_end_user_license_agreements_example']),
                    ('limit[appInfos]', 56),
                    ('limit[appStoreVersions]', 56),
                    ('limit[availableTerritories]', 56),
                    ('limit[betaAppLocalizations]', 56),
                    ('limit[betaGroups]', 56),
                    ('limit[builds]', 56),
                    ('limit[gameCenterEnabledVersions]', 56),
                    ('limit[inAppPurchases]', 56),
                    ('limit[preReleaseVersions]', 56),
                    ('limit[prices]', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/apps/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_in_app_purchases_get_to_many_related(client):
    """Test case for apps_in_app_purchases_get_to_many_related

    
    """
    params = [('filter[inAppPurchaseType]', ['filter_in_app_purchase_type_example']),
                    ('filter[canBeSubmitted]', ['filter_can_be_submitted_example']),
                    ('sort', ['sort_example']),
                    ('fields[inAppPurchases]', ['fields_in_app_purchases_example']),
                    ('fields[apps]', ['fields_apps_example']),
                    ('limit', 56),
                    ('include', ['include_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/apps/{id}/inAppPurchases'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_perf_power_metrics_get_to_many_related(client):
    """Test case for apps_perf_power_metrics_get_to_many_related

    
    """
    params = [('filter[deviceType]', ['filter_device_type_example']),
                    ('filter[metricType]', ['filter_metric_type_example']),
                    ('filter[platform]', ['filter_platform_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/apps/{id}/perfPowerMetrics'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_pre_order_get_to_one_related(client):
    """Test case for apps_pre_order_get_to_one_related

    
    """
    params = [('fields[appPreOrders]', ['fields_app_pre_orders_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/apps/{id}/preOrder'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_pre_release_versions_get_to_many_related(client):
    """Test case for apps_pre_release_versions_get_to_many_related

    
    """
    params = [('fields[preReleaseVersions]', ['fields_pre_release_versions_example']),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/apps/{id}/preReleaseVersions'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_prices_get_to_many_related(client):
    """Test case for apps_prices_get_to_many_related

    
    """
    params = [('fields[appPrices]', ['fields_app_prices_example']),
                    ('fields[appPriceTiers]', ['fields_app_price_tiers_example']),
                    ('fields[apps]', ['fields_apps_example']),
                    ('limit', 56),
                    ('include', ['include_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/apps/{id}/prices'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_update_instance(client):
    """Test case for apps_update_instance

    
    """
    body = {"data":{"relationships":{"availableTerritories":{"data":[{"id":"id","type":"territories"},{"id":"id","type":"territories"}]},"prices":{"data":[{"id":"id","type":"appPrices"},{"id":"id","type":"appPrices"}]}},"attributes":{"bundleId":"bundleId","availableInNewTerritories":True,"contentRightsDeclaration":"DOES_NOT_USE_THIRD_PARTY_CONTENT","primaryLocale":"primaryLocale"},"id":"id","type":"apps"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/apps/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

