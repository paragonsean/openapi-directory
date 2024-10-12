# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_api_http_body import GoogleApiHttpBody
from openapi_server.models.google_cloud_recommendationengine_v1beta1_catalog_item import GoogleCloudRecommendationengineV1beta1CatalogItem
from openapi_server.models.google_cloud_recommendationengine_v1beta1_create_prediction_api_key_registration_request import GoogleCloudRecommendationengineV1beta1CreatePredictionApiKeyRegistrationRequest
from openapi_server.models.google_cloud_recommendationengine_v1beta1_import_catalog_items_request import GoogleCloudRecommendationengineV1beta1ImportCatalogItemsRequest
from openapi_server.models.google_cloud_recommendationengine_v1beta1_import_user_events_request import GoogleCloudRecommendationengineV1beta1ImportUserEventsRequest
from openapi_server.models.google_cloud_recommendationengine_v1beta1_list_catalog_items_response import GoogleCloudRecommendationengineV1beta1ListCatalogItemsResponse
from openapi_server.models.google_cloud_recommendationengine_v1beta1_list_catalogs_response import GoogleCloudRecommendationengineV1beta1ListCatalogsResponse
from openapi_server.models.google_cloud_recommendationengine_v1beta1_list_prediction_api_key_registrations_response import GoogleCloudRecommendationengineV1beta1ListPredictionApiKeyRegistrationsResponse
from openapi_server.models.google_cloud_recommendationengine_v1beta1_list_user_events_response import GoogleCloudRecommendationengineV1beta1ListUserEventsResponse
from openapi_server.models.google_cloud_recommendationengine_v1beta1_predict_request import GoogleCloudRecommendationengineV1beta1PredictRequest
from openapi_server.models.google_cloud_recommendationengine_v1beta1_predict_response import GoogleCloudRecommendationengineV1beta1PredictResponse
from openapi_server.models.google_cloud_recommendationengine_v1beta1_prediction_api_key_registration import GoogleCloudRecommendationengineV1beta1PredictionApiKeyRegistration
from openapi_server.models.google_cloud_recommendationengine_v1beta1_purge_user_events_request import GoogleCloudRecommendationengineV1beta1PurgeUserEventsRequest
from openapi_server.models.google_cloud_recommendationengine_v1beta1_rejoin_user_events_request import GoogleCloudRecommendationengineV1beta1RejoinUserEventsRequest
from openapi_server.models.google_cloud_recommendationengine_v1beta1_user_event import GoogleCloudRecommendationengineV1beta1UserEvent
from openapi_server.models.google_longrunning_list_operations_response import GoogleLongrunningListOperationsResponse
from openapi_server.models.google_longrunning_operation import GoogleLongrunningOperation


pytestmark = pytest.mark.asyncio

async def test_recommendationengine_projects_locations_catalogs_catalog_items_create(client):
    """Test case for recommendationengine_projects_locations_catalogs_catalog_items_create

    
    """
    body = {"productMetadata":{"availableQuantity":"availableQuantity","costs":{"key":0.8008282},"images":[{"width":5,"uri":"uri","height":5},{"width":5,"uri":"uri","height":5}],"stockState":"STOCK_STATE_UNSPECIFIED","canonicalProductUri":"canonicalProductUri","currencyCode":"currencyCode","exactPrice":{"originalPrice":1.4658129,"displayPrice":6.0274563},"priceRange":{"min":7.0614014,"max":2.302136}},"itemAttributes":{"numericalFeatures":{"key":{"value":[6.0274563,6.0274563]}},"categoricalFeatures":{"key":{"value":["value","value"]}}},"categoryHierarchies":[{"categories":["categories","categories"]},{"categories":["categories","categories"]}],"description":"description","id":"id","languageCode":"languageCode","title":"title","itemGroupId":"itemGroupId","tags":["tags","tags"]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/catalogItems'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recommendationengine_projects_locations_catalogs_catalog_items_import(client):
    """Test case for recommendationengine_projects_locations_catalogs_catalog_items_import

    
    """
    body = {"inputConfig":{"userEventInlineSource":{"userEvents":[{"userInfo":{"directUserRequest":True,"ipAddress":"ipAddress","userAgent":"userAgent","userId":"userId","visitorId":"visitorId"},"eventSource":"EVENT_SOURCE_UNSPECIFIED","eventTime":"eventTime","productEventDetail":{"listId":"listId","purchaseTransaction":{"costs":{"key":7.0614014},"revenue":9.301444,"taxes":{"key":3.6160767},"id":"id","currencyCode":"currencyCode"},"pageCategories":[{"categories":["categories","categories"]},{"categories":["categories","categories"]}],"cartId":"cartId","searchQuery":"searchQuery","productDetails":[{"availableQuantity":1,"stockState":"STOCK_STATE_UNSPECIFIED","quantity":2,"originalPrice":5.637377,"displayPrice":5.962134,"itemAttributes":{"numericalFeatures":{"key":{"value":[6.0274563,6.0274563]}},"categoricalFeatures":{"key":{"value":["value","value"]}}},"id":"id","currencyCode":"currencyCode"},{"availableQuantity":1,"stockState":"STOCK_STATE_UNSPECIFIED","quantity":2,"originalPrice":5.637377,"displayPrice":5.962134,"itemAttributes":{"numericalFeatures":{"key":{"value":[6.0274563,6.0274563]}},"categoricalFeatures":{"key":{"value":["value","value"]}}},"id":"id","currencyCode":"currencyCode"}]},"eventType":"eventType","eventDetail":{"referrerUri":"referrerUri","eventAttributes":{"numericalFeatures":{"key":{"value":[6.0274563,6.0274563]}},"categoricalFeatures":{"key":{"value":["value","value"]}}},"experimentIds":["experimentIds","experimentIds"],"recommendationToken":"recommendationToken","pageViewId":"pageViewId","uri":"uri"}},{"userInfo":{"directUserRequest":True,"ipAddress":"ipAddress","userAgent":"userAgent","userId":"userId","visitorId":"visitorId"},"eventSource":"EVENT_SOURCE_UNSPECIFIED","eventTime":"eventTime","productEventDetail":{"listId":"listId","purchaseTransaction":{"costs":{"key":7.0614014},"revenue":9.301444,"taxes":{"key":3.6160767},"id":"id","currencyCode":"currencyCode"},"pageCategories":[{"categories":["categories","categories"]},{"categories":["categories","categories"]}],"cartId":"cartId","searchQuery":"searchQuery","productDetails":[{"availableQuantity":1,"stockState":"STOCK_STATE_UNSPECIFIED","quantity":2,"originalPrice":5.637377,"displayPrice":5.962134,"itemAttributes":{"numericalFeatures":{"key":{"value":[6.0274563,6.0274563]}},"categoricalFeatures":{"key":{"value":["value","value"]}}},"id":"id","currencyCode":"currencyCode"},{"availableQuantity":1,"stockState":"STOCK_STATE_UNSPECIFIED","quantity":2,"originalPrice":5.637377,"displayPrice":5.962134,"itemAttributes":{"numericalFeatures":{"key":{"value":[6.0274563,6.0274563]}},"categoricalFeatures":{"key":{"value":["value","value"]}}},"id":"id","currencyCode":"currencyCode"}]},"eventType":"eventType","eventDetail":{"referrerUri":"referrerUri","eventAttributes":{"numericalFeatures":{"key":{"value":[6.0274563,6.0274563]}},"categoricalFeatures":{"key":{"value":["value","value"]}}},"experimentIds":["experimentIds","experimentIds"],"recommendationToken":"recommendationToken","pageViewId":"pageViewId","uri":"uri"}}]},"bigQuerySource":{"dataSchema":"dataSchema","datasetId":"datasetId","tableId":"tableId","projectId":"projectId","gcsStagingDir":"gcsStagingDir"},"catalogInlineSource":{"catalogItems":[{"productMetadata":{"availableQuantity":"availableQuantity","costs":{"key":0.8008282},"images":[{"width":5,"uri":"uri","height":5},{"width":5,"uri":"uri","height":5}],"stockState":"STOCK_STATE_UNSPECIFIED","canonicalProductUri":"canonicalProductUri","currencyCode":"currencyCode","exactPrice":{"originalPrice":1.4658129,"displayPrice":6.0274563},"priceRange":{"min":7.0614014,"max":2.302136}},"itemAttributes":{"numericalFeatures":{"key":{"value":[6.0274563,6.0274563]}},"categoricalFeatures":{"key":{"value":["value","value"]}}},"categoryHierarchies":[{"categories":["categories","categories"]},{"categories":["categories","categories"]}],"description":"description","id":"id","languageCode":"languageCode","title":"title","itemGroupId":"itemGroupId","tags":["tags","tags"]},{"productMetadata":{"availableQuantity":"availableQuantity","costs":{"key":0.8008282},"images":[{"width":5,"uri":"uri","height":5},{"width":5,"uri":"uri","height":5}],"stockState":"STOCK_STATE_UNSPECIFIED","canonicalProductUri":"canonicalProductUri","currencyCode":"currencyCode","exactPrice":{"originalPrice":1.4658129,"displayPrice":6.0274563},"priceRange":{"min":7.0614014,"max":2.302136}},"itemAttributes":{"numericalFeatures":{"key":{"value":[6.0274563,6.0274563]}},"categoricalFeatures":{"key":{"value":["value","value"]}}},"categoryHierarchies":[{"categories":["categories","categories"]},{"categories":["categories","categories"]}],"description":"description","id":"id","languageCode":"languageCode","title":"title","itemGroupId":"itemGroupId","tags":["tags","tags"]}]},"gcsSource":{"jsonSchema":"jsonSchema","inputUris":["inputUris","inputUris"]}},"requestId":"requestId","errorsConfig":{"gcsPrefix":"gcsPrefix"},"updateMask":"updateMask"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/catalogItems:import'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recommendationengine_projects_locations_catalogs_catalog_items_list(client):
    """Test case for recommendationengine_projects_locations_catalogs_catalog_items_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/catalogItems'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recommendationengine_projects_locations_catalogs_catalog_items_patch(client):
    """Test case for recommendationengine_projects_locations_catalogs_catalog_items_patch

    
    """
    body = {"productMetadata":{"availableQuantity":"availableQuantity","costs":{"key":0.8008282},"images":[{"width":5,"uri":"uri","height":5},{"width":5,"uri":"uri","height":5}],"stockState":"STOCK_STATE_UNSPECIFIED","canonicalProductUri":"canonicalProductUri","currencyCode":"currencyCode","exactPrice":{"originalPrice":1.4658129,"displayPrice":6.0274563},"priceRange":{"min":7.0614014,"max":2.302136}},"itemAttributes":{"numericalFeatures":{"key":{"value":[6.0274563,6.0274563]}},"categoricalFeatures":{"key":{"value":["value","value"]}}},"categoryHierarchies":[{"categories":["categories","categories"]},{"categories":["categories","categories"]}],"description":"description","id":"id","languageCode":"languageCode","title":"title","itemGroupId":"itemGroupId","tags":["tags","tags"]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1beta1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recommendationengine_projects_locations_catalogs_event_stores_placements_predict(client):
    """Test case for recommendationengine_projects_locations_catalogs_event_stores_placements_predict

    
    """
    body = {"filter":"filter","userEvent":{"userInfo":{"directUserRequest":True,"ipAddress":"ipAddress","userAgent":"userAgent","userId":"userId","visitorId":"visitorId"},"eventSource":"EVENT_SOURCE_UNSPECIFIED","eventTime":"eventTime","productEventDetail":{"listId":"listId","purchaseTransaction":{"costs":{"key":7.0614014},"revenue":9.301444,"taxes":{"key":3.6160767},"id":"id","currencyCode":"currencyCode"},"pageCategories":[{"categories":["categories","categories"]},{"categories":["categories","categories"]}],"cartId":"cartId","searchQuery":"searchQuery","productDetails":[{"availableQuantity":1,"stockState":"STOCK_STATE_UNSPECIFIED","quantity":2,"originalPrice":5.637377,"displayPrice":5.962134,"itemAttributes":{"numericalFeatures":{"key":{"value":[6.0274563,6.0274563]}},"categoricalFeatures":{"key":{"value":["value","value"]}}},"id":"id","currencyCode":"currencyCode"},{"availableQuantity":1,"stockState":"STOCK_STATE_UNSPECIFIED","quantity":2,"originalPrice":5.637377,"displayPrice":5.962134,"itemAttributes":{"numericalFeatures":{"key":{"value":[6.0274563,6.0274563]}},"categoricalFeatures":{"key":{"value":["value","value"]}}},"id":"id","currencyCode":"currencyCode"}]},"eventType":"eventType","eventDetail":{"referrerUri":"referrerUri","eventAttributes":{"numericalFeatures":{"key":{"value":[6.0274563,6.0274563]}},"categoricalFeatures":{"key":{"value":["value","value"]}}},"experimentIds":["experimentIds","experimentIds"],"recommendationToken":"recommendationToken","pageViewId":"pageViewId","uri":"uri"}},"dryRun":True,"pageSize":0,"pageToken":"pageToken","params":{"key":""},"labels":{"key":"labels"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{namepredic}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recommendationengine_projects_locations_catalogs_event_stores_prediction_api_key_registrations_create(client):
    """Test case for recommendationengine_projects_locations_catalogs_event_stores_prediction_api_key_registrations_create

    
    """
    body = {"predictionApiKeyRegistration":{"apiKey":"apiKey"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/predictionApiKeyRegistrations'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recommendationengine_projects_locations_catalogs_event_stores_prediction_api_key_registrations_delete(client):
    """Test case for recommendationengine_projects_locations_catalogs_event_stores_prediction_api_key_registrations_delete

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1beta1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recommendationengine_projects_locations_catalogs_event_stores_prediction_api_key_registrations_list(client):
    """Test case for recommendationengine_projects_locations_catalogs_event_stores_prediction_api_key_registrations_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/predictionApiKeyRegistrations'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recommendationengine_projects_locations_catalogs_event_stores_user_events_collect(client):
    """Test case for recommendationengine_projects_locations_catalogs_event_stores_user_events_collect

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('ets', 'ets_example'),
                    ('uri', 'uri_example'),
                    ('userEvent', 'user_event_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/userEvents:collect'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recommendationengine_projects_locations_catalogs_event_stores_user_events_import(client):
    """Test case for recommendationengine_projects_locations_catalogs_event_stores_user_events_import

    
    """
    body = {"inputConfig":{"userEventInlineSource":{"userEvents":[{"userInfo":{"directUserRequest":True,"ipAddress":"ipAddress","userAgent":"userAgent","userId":"userId","visitorId":"visitorId"},"eventSource":"EVENT_SOURCE_UNSPECIFIED","eventTime":"eventTime","productEventDetail":{"listId":"listId","purchaseTransaction":{"costs":{"key":7.0614014},"revenue":9.301444,"taxes":{"key":3.6160767},"id":"id","currencyCode":"currencyCode"},"pageCategories":[{"categories":["categories","categories"]},{"categories":["categories","categories"]}],"cartId":"cartId","searchQuery":"searchQuery","productDetails":[{"availableQuantity":1,"stockState":"STOCK_STATE_UNSPECIFIED","quantity":2,"originalPrice":5.637377,"displayPrice":5.962134,"itemAttributes":{"numericalFeatures":{"key":{"value":[6.0274563,6.0274563]}},"categoricalFeatures":{"key":{"value":["value","value"]}}},"id":"id","currencyCode":"currencyCode"},{"availableQuantity":1,"stockState":"STOCK_STATE_UNSPECIFIED","quantity":2,"originalPrice":5.637377,"displayPrice":5.962134,"itemAttributes":{"numericalFeatures":{"key":{"value":[6.0274563,6.0274563]}},"categoricalFeatures":{"key":{"value":["value","value"]}}},"id":"id","currencyCode":"currencyCode"}]},"eventType":"eventType","eventDetail":{"referrerUri":"referrerUri","eventAttributes":{"numericalFeatures":{"key":{"value":[6.0274563,6.0274563]}},"categoricalFeatures":{"key":{"value":["value","value"]}}},"experimentIds":["experimentIds","experimentIds"],"recommendationToken":"recommendationToken","pageViewId":"pageViewId","uri":"uri"}},{"userInfo":{"directUserRequest":True,"ipAddress":"ipAddress","userAgent":"userAgent","userId":"userId","visitorId":"visitorId"},"eventSource":"EVENT_SOURCE_UNSPECIFIED","eventTime":"eventTime","productEventDetail":{"listId":"listId","purchaseTransaction":{"costs":{"key":7.0614014},"revenue":9.301444,"taxes":{"key":3.6160767},"id":"id","currencyCode":"currencyCode"},"pageCategories":[{"categories":["categories","categories"]},{"categories":["categories","categories"]}],"cartId":"cartId","searchQuery":"searchQuery","productDetails":[{"availableQuantity":1,"stockState":"STOCK_STATE_UNSPECIFIED","quantity":2,"originalPrice":5.637377,"displayPrice":5.962134,"itemAttributes":{"numericalFeatures":{"key":{"value":[6.0274563,6.0274563]}},"categoricalFeatures":{"key":{"value":["value","value"]}}},"id":"id","currencyCode":"currencyCode"},{"availableQuantity":1,"stockState":"STOCK_STATE_UNSPECIFIED","quantity":2,"originalPrice":5.637377,"displayPrice":5.962134,"itemAttributes":{"numericalFeatures":{"key":{"value":[6.0274563,6.0274563]}},"categoricalFeatures":{"key":{"value":["value","value"]}}},"id":"id","currencyCode":"currencyCode"}]},"eventType":"eventType","eventDetail":{"referrerUri":"referrerUri","eventAttributes":{"numericalFeatures":{"key":{"value":[6.0274563,6.0274563]}},"categoricalFeatures":{"key":{"value":["value","value"]}}},"experimentIds":["experimentIds","experimentIds"],"recommendationToken":"recommendationToken","pageViewId":"pageViewId","uri":"uri"}}]},"bigQuerySource":{"dataSchema":"dataSchema","datasetId":"datasetId","tableId":"tableId","projectId":"projectId","gcsStagingDir":"gcsStagingDir"},"catalogInlineSource":{"catalogItems":[{"productMetadata":{"availableQuantity":"availableQuantity","costs":{"key":0.8008282},"images":[{"width":5,"uri":"uri","height":5},{"width":5,"uri":"uri","height":5}],"stockState":"STOCK_STATE_UNSPECIFIED","canonicalProductUri":"canonicalProductUri","currencyCode":"currencyCode","exactPrice":{"originalPrice":1.4658129,"displayPrice":6.0274563},"priceRange":{"min":7.0614014,"max":2.302136}},"itemAttributes":{"numericalFeatures":{"key":{"value":[6.0274563,6.0274563]}},"categoricalFeatures":{"key":{"value":["value","value"]}}},"categoryHierarchies":[{"categories":["categories","categories"]},{"categories":["categories","categories"]}],"description":"description","id":"id","languageCode":"languageCode","title":"title","itemGroupId":"itemGroupId","tags":["tags","tags"]},{"productMetadata":{"availableQuantity":"availableQuantity","costs":{"key":0.8008282},"images":[{"width":5,"uri":"uri","height":5},{"width":5,"uri":"uri","height":5}],"stockState":"STOCK_STATE_UNSPECIFIED","canonicalProductUri":"canonicalProductUri","currencyCode":"currencyCode","exactPrice":{"originalPrice":1.4658129,"displayPrice":6.0274563},"priceRange":{"min":7.0614014,"max":2.302136}},"itemAttributes":{"numericalFeatures":{"key":{"value":[6.0274563,6.0274563]}},"categoricalFeatures":{"key":{"value":["value","value"]}}},"categoryHierarchies":[{"categories":["categories","categories"]},{"categories":["categories","categories"]}],"description":"description","id":"id","languageCode":"languageCode","title":"title","itemGroupId":"itemGroupId","tags":["tags","tags"]}]},"gcsSource":{"jsonSchema":"jsonSchema","inputUris":["inputUris","inputUris"]}},"requestId":"requestId","errorsConfig":{"gcsPrefix":"gcsPrefix"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/userEvents:import'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recommendationengine_projects_locations_catalogs_event_stores_user_events_list(client):
    """Test case for recommendationengine_projects_locations_catalogs_event_stores_user_events_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/userEvents'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recommendationengine_projects_locations_catalogs_event_stores_user_events_purge(client):
    """Test case for recommendationengine_projects_locations_catalogs_event_stores_user_events_purge

    
    """
    body = {"filter":"filter","force":True}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/userEvents:purge'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recommendationengine_projects_locations_catalogs_event_stores_user_events_rejoin(client):
    """Test case for recommendationengine_projects_locations_catalogs_event_stores_user_events_rejoin

    
    """
    body = {"userEventRejoinScope":"USER_EVENT_REJOIN_SCOPE_UNSPECIFIED"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/userEvents:rejoin'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recommendationengine_projects_locations_catalogs_event_stores_user_events_write(client):
    """Test case for recommendationengine_projects_locations_catalogs_event_stores_user_events_write

    
    """
    body = {"userInfo":{"directUserRequest":True,"ipAddress":"ipAddress","userAgent":"userAgent","userId":"userId","visitorId":"visitorId"},"eventSource":"EVENT_SOURCE_UNSPECIFIED","eventTime":"eventTime","productEventDetail":{"listId":"listId","purchaseTransaction":{"costs":{"key":7.0614014},"revenue":9.301444,"taxes":{"key":3.6160767},"id":"id","currencyCode":"currencyCode"},"pageCategories":[{"categories":["categories","categories"]},{"categories":["categories","categories"]}],"cartId":"cartId","searchQuery":"searchQuery","productDetails":[{"availableQuantity":1,"stockState":"STOCK_STATE_UNSPECIFIED","quantity":2,"originalPrice":5.637377,"displayPrice":5.962134,"itemAttributes":{"numericalFeatures":{"key":{"value":[6.0274563,6.0274563]}},"categoricalFeatures":{"key":{"value":["value","value"]}}},"id":"id","currencyCode":"currencyCode"},{"availableQuantity":1,"stockState":"STOCK_STATE_UNSPECIFIED","quantity":2,"originalPrice":5.637377,"displayPrice":5.962134,"itemAttributes":{"numericalFeatures":{"key":{"value":[6.0274563,6.0274563]}},"categoricalFeatures":{"key":{"value":["value","value"]}}},"id":"id","currencyCode":"currencyCode"}]},"eventType":"eventType","eventDetail":{"referrerUri":"referrerUri","eventAttributes":{"numericalFeatures":{"key":{"value":[6.0274563,6.0274563]}},"categoricalFeatures":{"key":{"value":["value","value"]}}},"experimentIds":["experimentIds","experimentIds"],"recommendationToken":"recommendationToken","pageViewId":"pageViewId","uri":"uri"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/userEvents:write'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recommendationengine_projects_locations_catalogs_list(client):
    """Test case for recommendationengine_projects_locations_catalogs_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/catalogs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recommendationengine_projects_locations_catalogs_operations_get(client):
    """Test case for recommendationengine_projects_locations_catalogs_operations_get

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recommendationengine_projects_locations_catalogs_operations_list(client):
    """Test case for recommendationengine_projects_locations_catalogs_operations_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{name}/operations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

