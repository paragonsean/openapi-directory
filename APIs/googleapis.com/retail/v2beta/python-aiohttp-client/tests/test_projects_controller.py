# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_api_http_body import GoogleApiHttpBody
from openapi_server.models.google_cloud_retail_v2beta_add_catalog_attribute_request import GoogleCloudRetailV2betaAddCatalogAttributeRequest
from openapi_server.models.google_cloud_retail_v2beta_add_control_request import GoogleCloudRetailV2betaAddControlRequest
from openapi_server.models.google_cloud_retail_v2beta_add_fulfillment_places_request import GoogleCloudRetailV2betaAddFulfillmentPlacesRequest
from openapi_server.models.google_cloud_retail_v2beta_add_local_inventories_request import GoogleCloudRetailV2betaAddLocalInventoriesRequest
from openapi_server.models.google_cloud_retail_v2beta_attributes_config import GoogleCloudRetailV2betaAttributesConfig
from openapi_server.models.google_cloud_retail_v2beta_batch_remove_catalog_attributes_request import GoogleCloudRetailV2betaBatchRemoveCatalogAttributesRequest
from openapi_server.models.google_cloud_retail_v2beta_batch_remove_catalog_attributes_response import GoogleCloudRetailV2betaBatchRemoveCatalogAttributesResponse
from openapi_server.models.google_cloud_retail_v2beta_complete_query_response import GoogleCloudRetailV2betaCompleteQueryResponse
from openapi_server.models.google_cloud_retail_v2beta_control import GoogleCloudRetailV2betaControl
from openapi_server.models.google_cloud_retail_v2beta_export_analytics_metrics_request import GoogleCloudRetailV2betaExportAnalyticsMetricsRequest
from openapi_server.models.google_cloud_retail_v2beta_get_default_branch_response import GoogleCloudRetailV2betaGetDefaultBranchResponse
from openapi_server.models.google_cloud_retail_v2beta_import_completion_data_request import GoogleCloudRetailV2betaImportCompletionDataRequest
from openapi_server.models.google_cloud_retail_v2beta_import_products_request import GoogleCloudRetailV2betaImportProductsRequest
from openapi_server.models.google_cloud_retail_v2beta_import_user_events_request import GoogleCloudRetailV2betaImportUserEventsRequest
from openapi_server.models.google_cloud_retail_v2beta_list_catalogs_response import GoogleCloudRetailV2betaListCatalogsResponse
from openapi_server.models.google_cloud_retail_v2beta_list_controls_response import GoogleCloudRetailV2betaListControlsResponse
from openapi_server.models.google_cloud_retail_v2beta_list_models_response import GoogleCloudRetailV2betaListModelsResponse
from openapi_server.models.google_cloud_retail_v2beta_list_products_response import GoogleCloudRetailV2betaListProductsResponse
from openapi_server.models.google_cloud_retail_v2beta_list_serving_configs_response import GoogleCloudRetailV2betaListServingConfigsResponse
from openapi_server.models.google_cloud_retail_v2beta_model import GoogleCloudRetailV2betaModel
from openapi_server.models.google_cloud_retail_v2beta_predict_request import GoogleCloudRetailV2betaPredictRequest
from openapi_server.models.google_cloud_retail_v2beta_predict_response import GoogleCloudRetailV2betaPredictResponse
from openapi_server.models.google_cloud_retail_v2beta_product import GoogleCloudRetailV2betaProduct
from openapi_server.models.google_cloud_retail_v2beta_purge_products_request import GoogleCloudRetailV2betaPurgeProductsRequest
from openapi_server.models.google_cloud_retail_v2beta_purge_user_events_request import GoogleCloudRetailV2betaPurgeUserEventsRequest
from openapi_server.models.google_cloud_retail_v2beta_rejoin_user_events_request import GoogleCloudRetailV2betaRejoinUserEventsRequest
from openapi_server.models.google_cloud_retail_v2beta_remove_catalog_attribute_request import GoogleCloudRetailV2betaRemoveCatalogAttributeRequest
from openapi_server.models.google_cloud_retail_v2beta_remove_control_request import GoogleCloudRetailV2betaRemoveControlRequest
from openapi_server.models.google_cloud_retail_v2beta_remove_fulfillment_places_request import GoogleCloudRetailV2betaRemoveFulfillmentPlacesRequest
from openapi_server.models.google_cloud_retail_v2beta_remove_local_inventories_request import GoogleCloudRetailV2betaRemoveLocalInventoriesRequest
from openapi_server.models.google_cloud_retail_v2beta_replace_catalog_attribute_request import GoogleCloudRetailV2betaReplaceCatalogAttributeRequest
from openapi_server.models.google_cloud_retail_v2beta_search_request import GoogleCloudRetailV2betaSearchRequest
from openapi_server.models.google_cloud_retail_v2beta_search_response import GoogleCloudRetailV2betaSearchResponse
from openapi_server.models.google_cloud_retail_v2beta_serving_config import GoogleCloudRetailV2betaServingConfig
from openapi_server.models.google_cloud_retail_v2beta_set_default_branch_request import GoogleCloudRetailV2betaSetDefaultBranchRequest
from openapi_server.models.google_cloud_retail_v2beta_set_inventory_request import GoogleCloudRetailV2betaSetInventoryRequest
from openapi_server.models.google_cloud_retail_v2beta_user_event import GoogleCloudRetailV2betaUserEvent
from openapi_server.models.google_longrunning_list_operations_response import GoogleLongrunningListOperationsResponse
from openapi_server.models.google_longrunning_operation import GoogleLongrunningOperation


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_attributes_config_add_catalog_attribute(client):
    """Test case for retail_projects_locations_catalogs_attributes_config_add_catalog_attribute

    
    """
    body = {"catalogAttribute":{"retrievableOption":"RETRIEVABLE_OPTION_UNSPECIFIED","inUse":True,"searchableOption":"SEARCHABLE_OPTION_UNSPECIFIED","indexableOption":"INDEXABLE_OPTION_UNSPECIFIED","recommendationsFilteringOption":"RECOMMENDATIONS_FILTERING_OPTION_UNSPECIFIED","type":"UNKNOWN","exactSearchableOption":"EXACT_SEARCHABLE_OPTION_UNSPECIFIED","dynamicFacetableOption":"DYNAMIC_FACETABLE_OPTION_UNSPECIFIED","facetConfig":{"facetIntervals":[{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}],"mergedFacetValues":[{"values":["values","values"],"mergedValue":"mergedValue"},{"values":["values","values"],"mergedValue":"mergedValue"}],"mergedFacet":{"mergedFacetValues":[{"values":["values","values"],"mergedValue":"mergedValue"},{"values":["values","values"],"mergedValue":"mergedValue"}],"mergedFacetKey":"mergedFacetKey"},"ignoredFacetValues":[{"values":["values","values"],"startTime":"startTime","endTime":"endTime"},{"values":["values","values"],"startTime":"startTime","endTime":"endTime"}],"rerankConfig":{"rerankFacet":True,"facetValues":["facetValues","facetValues"]}},"key":"key"}}
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
        path='/v2beta/{attributes_configadd_catalog_attribut}'.format(attributes_config='attributes_config_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_attributes_config_batch_remove_catalog_attributes(client):
    """Test case for retail_projects_locations_catalogs_attributes_config_batch_remove_catalog_attributes

    
    """
    body = {"attributeKeys":["attributeKeys","attributeKeys"]}
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
        path='/v2beta/{attributes_configbatch_remove_catalog_attribute}'.format(attributes_config='attributes_config_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_attributes_config_remove_catalog_attribute(client):
    """Test case for retail_projects_locations_catalogs_attributes_config_remove_catalog_attribute

    
    """
    body = {"key":"key"}
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
        path='/v2beta/{attributes_configremove_catalog_attribut}'.format(attributes_config='attributes_config_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_attributes_config_replace_catalog_attribute(client):
    """Test case for retail_projects_locations_catalogs_attributes_config_replace_catalog_attribute

    
    """
    body = {"catalogAttribute":{"retrievableOption":"RETRIEVABLE_OPTION_UNSPECIFIED","inUse":True,"searchableOption":"SEARCHABLE_OPTION_UNSPECIFIED","indexableOption":"INDEXABLE_OPTION_UNSPECIFIED","recommendationsFilteringOption":"RECOMMENDATIONS_FILTERING_OPTION_UNSPECIFIED","type":"UNKNOWN","exactSearchableOption":"EXACT_SEARCHABLE_OPTION_UNSPECIFIED","dynamicFacetableOption":"DYNAMIC_FACETABLE_OPTION_UNSPECIFIED","facetConfig":{"facetIntervals":[{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}],"mergedFacetValues":[{"values":["values","values"],"mergedValue":"mergedValue"},{"values":["values","values"],"mergedValue":"mergedValue"}],"mergedFacet":{"mergedFacetValues":[{"values":["values","values"],"mergedValue":"mergedValue"},{"values":["values","values"],"mergedValue":"mergedValue"}],"mergedFacetKey":"mergedFacetKey"},"ignoredFacetValues":[{"values":["values","values"],"startTime":"startTime","endTime":"endTime"},{"values":["values","values"],"startTime":"startTime","endTime":"endTime"}],"rerankConfig":{"rerankFacet":True,"facetValues":["facetValues","facetValues"]}},"key":"key"},"updateMask":"updateMask"}
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
        path='/v2beta/{attributes_configreplace_catalog_attribut}'.format(attributes_config='attributes_config_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_branches_products_add_fulfillment_places(client):
    """Test case for retail_projects_locations_catalogs_branches_products_add_fulfillment_places

    
    """
    body = {"addTime":"addTime","allowMissing":True,"type":"type","placeIds":["placeIds","placeIds"]}
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
        path='/v2beta/{productadd_fulfillment_place}'.format(product='product_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_branches_products_add_local_inventories(client):
    """Test case for retail_projects_locations_catalogs_branches_products_add_local_inventories

    
    """
    body = {"addTime":"addTime","allowMissing":True,"addMask":"addMask","localInventories":[{"priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"placeId":"placeId","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"fulfillmentTypes":["fulfillmentTypes","fulfillmentTypes"]},{"priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"placeId":"placeId","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"fulfillmentTypes":["fulfillmentTypes","fulfillmentTypes"]}]}
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
        path='/v2beta/{productadd_local_inventorie}'.format(product='product_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_branches_products_create(client):
    """Test case for retail_projects_locations_catalogs_branches_products_create

    
    """
    body = {"rating":{"ratingHistogram":[3,3],"averageRating":7.0614014,"ratingCount":9},"description":"description","availability":"AVAILABILITY_UNSPECIFIED","variants":[null,null],"title":"title","type":"TYPE_UNSPECIFIED","priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"availableTime":"availableTime","collectionMemberIds":["collectionMemberIds","collectionMemberIds"],"sizes":["sizes","sizes"],"retrievableFields":"retrievableFields","categories":["categories","categories"],"id":"id","fulfillmentInfo":[{"type":"type","placeIds":["placeIds","placeIds"]},{"type":"type","placeIds":["placeIds","placeIds"]}],"availableQuantity":0,"publishTime":"publishTime","audience":{"genders":["genders","genders"],"ageGroups":["ageGroups","ageGroups"]},"gtin":"gtin","images":[{"width":1,"uri":"uri","height":6},{"width":1,"uri":"uri","height":6}],"brands":["brands","brands"],"patterns":["patterns","patterns"],"languageCode":"languageCode","ttl":"ttl","uri":"uri","localInventories":[{"priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"placeId":"placeId","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"fulfillmentTypes":["fulfillmentTypes","fulfillmentTypes"]},{"priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"placeId":"placeId","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"fulfillmentTypes":["fulfillmentTypes","fulfillmentTypes"]}],"primaryProductId":"primaryProductId","tags":["tags","tags"],"promotions":[{"promotionId":"promotionId"},{"promotionId":"promotionId"}],"expireTime":"expireTime","materials":["materials","materials"],"name":"name","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"colorInfo":{"colorFamilies":["colorFamilies","colorFamilies"],"colors":["colors","colors"]},"conditions":["conditions","conditions"]}
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
                    ('productId', 'product_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2beta/{parent}/products'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_branches_products_import(client):
    """Test case for retail_projects_locations_catalogs_branches_products_import

    
    """
    body = {"inputConfig":{"productInlineSource":{"products":[{"rating":{"ratingHistogram":[3,3],"averageRating":7.0614014,"ratingCount":9},"description":"description","availability":"AVAILABILITY_UNSPECIFIED","variants":[null,null],"title":"title","type":"TYPE_UNSPECIFIED","priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"availableTime":"availableTime","collectionMemberIds":["collectionMemberIds","collectionMemberIds"],"sizes":["sizes","sizes"],"retrievableFields":"retrievableFields","categories":["categories","categories"],"id":"id","fulfillmentInfo":[{"type":"type","placeIds":["placeIds","placeIds"]},{"type":"type","placeIds":["placeIds","placeIds"]}],"availableQuantity":0,"publishTime":"publishTime","audience":{"genders":["genders","genders"],"ageGroups":["ageGroups","ageGroups"]},"gtin":"gtin","images":[{"width":1,"uri":"uri","height":6},{"width":1,"uri":"uri","height":6}],"brands":["brands","brands"],"patterns":["patterns","patterns"],"languageCode":"languageCode","ttl":"ttl","uri":"uri","localInventories":[{"priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"placeId":"placeId","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"fulfillmentTypes":["fulfillmentTypes","fulfillmentTypes"]},{"priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"placeId":"placeId","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"fulfillmentTypes":["fulfillmentTypes","fulfillmentTypes"]}],"primaryProductId":"primaryProductId","tags":["tags","tags"],"promotions":[{"promotionId":"promotionId"},{"promotionId":"promotionId"}],"expireTime":"expireTime","materials":["materials","materials"],"name":"name","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"colorInfo":{"colorFamilies":["colorFamilies","colorFamilies"],"colors":["colors","colors"]},"conditions":["conditions","conditions"]},{"rating":{"ratingHistogram":[3,3],"averageRating":7.0614014,"ratingCount":9},"description":"description","availability":"AVAILABILITY_UNSPECIFIED","variants":[null,null],"title":"title","type":"TYPE_UNSPECIFIED","priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"availableTime":"availableTime","collectionMemberIds":["collectionMemberIds","collectionMemberIds"],"sizes":["sizes","sizes"],"retrievableFields":"retrievableFields","categories":["categories","categories"],"id":"id","fulfillmentInfo":[{"type":"type","placeIds":["placeIds","placeIds"]},{"type":"type","placeIds":["placeIds","placeIds"]}],"availableQuantity":0,"publishTime":"publishTime","audience":{"genders":["genders","genders"],"ageGroups":["ageGroups","ageGroups"]},"gtin":"gtin","images":[{"width":1,"uri":"uri","height":6},{"width":1,"uri":"uri","height":6}],"brands":["brands","brands"],"patterns":["patterns","patterns"],"languageCode":"languageCode","ttl":"ttl","uri":"uri","localInventories":[{"priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"placeId":"placeId","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"fulfillmentTypes":["fulfillmentTypes","fulfillmentTypes"]},{"priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"placeId":"placeId","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"fulfillmentTypes":["fulfillmentTypes","fulfillmentTypes"]}],"primaryProductId":"primaryProductId","tags":["tags","tags"],"promotions":[{"promotionId":"promotionId"},{"promotionId":"promotionId"}],"expireTime":"expireTime","materials":["materials","materials"],"name":"name","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"colorInfo":{"colorFamilies":["colorFamilies","colorFamilies"],"colors":["colors","colors"]},"conditions":["conditions","conditions"]}]},"bigQuerySource":{"dataSchema":"dataSchema","datasetId":"datasetId","partitionDate":{"month":6,"year":1,"day":0},"tableId":"tableId","projectId":"projectId","gcsStagingDir":"gcsStagingDir"},"gcsSource":{"dataSchema":"dataSchema","inputUris":["inputUris","inputUris"]}},"requestId":"requestId","errorsConfig":{"gcsPrefix":"gcsPrefix"},"notificationPubsubTopic":"notificationPubsubTopic","updateMask":"updateMask","reconciliationMode":"RECONCILIATION_MODE_UNSPECIFIED"}
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
        path='/v2beta/{parent}/products:import'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_branches_products_list(client):
    """Test case for retail_projects_locations_catalogs_branches_products_list

    
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
                    ('pageToken', 'page_token_example'),
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2beta/{parent}/products'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_branches_products_purge(client):
    """Test case for retail_projects_locations_catalogs_branches_products_purge

    
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
        path='/v2beta/{parent}/products:purge'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_branches_products_remove_fulfillment_places(client):
    """Test case for retail_projects_locations_catalogs_branches_products_remove_fulfillment_places

    
    """
    body = {"allowMissing":True,"removeTime":"removeTime","type":"type","placeIds":["placeIds","placeIds"]}
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
        path='/v2beta/{productremove_fulfillment_place}'.format(product='product_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_branches_products_remove_local_inventories(client):
    """Test case for retail_projects_locations_catalogs_branches_products_remove_local_inventories

    
    """
    body = {"allowMissing":True,"removeTime":"removeTime","placeIds":["placeIds","placeIds"]}
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
        path='/v2beta/{productremove_local_inventorie}'.format(product='product_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_branches_products_set_inventory(client):
    """Test case for retail_projects_locations_catalogs_branches_products_set_inventory

    
    """
    body = {"setMask":"setMask","allowMissing":True,"inventory":{"rating":{"ratingHistogram":[3,3],"averageRating":7.0614014,"ratingCount":9},"description":"description","availability":"AVAILABILITY_UNSPECIFIED","variants":[null,null],"title":"title","type":"TYPE_UNSPECIFIED","priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"availableTime":"availableTime","collectionMemberIds":["collectionMemberIds","collectionMemberIds"],"sizes":["sizes","sizes"],"retrievableFields":"retrievableFields","categories":["categories","categories"],"id":"id","fulfillmentInfo":[{"type":"type","placeIds":["placeIds","placeIds"]},{"type":"type","placeIds":["placeIds","placeIds"]}],"availableQuantity":0,"publishTime":"publishTime","audience":{"genders":["genders","genders"],"ageGroups":["ageGroups","ageGroups"]},"gtin":"gtin","images":[{"width":1,"uri":"uri","height":6},{"width":1,"uri":"uri","height":6}],"brands":["brands","brands"],"patterns":["patterns","patterns"],"languageCode":"languageCode","ttl":"ttl","uri":"uri","localInventories":[{"priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"placeId":"placeId","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"fulfillmentTypes":["fulfillmentTypes","fulfillmentTypes"]},{"priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"placeId":"placeId","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"fulfillmentTypes":["fulfillmentTypes","fulfillmentTypes"]}],"primaryProductId":"primaryProductId","tags":["tags","tags"],"promotions":[{"promotionId":"promotionId"},{"promotionId":"promotionId"}],"expireTime":"expireTime","materials":["materials","materials"],"name":"name","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"colorInfo":{"colorFamilies":["colorFamilies","colorFamilies"],"colors":["colors","colors"]},"conditions":["conditions","conditions"]},"setTime":"setTime"}
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
        path='/v2beta/{nameset_inventor}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_complete_query(client):
    """Test case for retail_projects_locations_catalogs_complete_query

    
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
                    ('dataset', 'dataset_example'),
                    ('deviceType', 'device_type_example'),
                    ('entity', 'entity_example'),
                    ('languageCodes', ['language_codes_example']),
                    ('maxSuggestions', 56),
                    ('query', 'query_example'),
                    ('visitorId', 'visitor_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2beta/{catalogcomplete_quer}'.format(catalog='catalog_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_completion_data_import(client):
    """Test case for retail_projects_locations_catalogs_completion_data_import

    
    """
    body = {"inputConfig":{"bigQuerySource":{"dataSchema":"dataSchema","datasetId":"datasetId","partitionDate":{"month":6,"year":1,"day":0},"tableId":"tableId","projectId":"projectId","gcsStagingDir":"gcsStagingDir"}},"notificationPubsubTopic":"notificationPubsubTopic"}
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
        path='/v2beta/{parent}/completionData:import'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_controls_create(client):
    """Test case for retail_projects_locations_catalogs_controls_create

    
    """
    body = {"facetSpec":{"facetKey":{"contains":["contains","contains"],"intervals":[{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}],"prefixes":["prefixes","prefixes"],"restrictedValues":["restrictedValues","restrictedValues"],"returnMinMax":True,"query":"query","caseInsensitive":True,"orderBy":"orderBy","key":"key"},"enableDynamicPosition":True,"limit":0,"excludedFilterKeys":["excludedFilterKeys","excludedFilterKeys"]},"associatedServingConfigIds":["associatedServingConfigIds","associatedServingConfigIds"],"displayName":"displayName","name":"name","rule":{"condition":{"pageCategories":["pageCategories","pageCategories"],"activeTimeRange":[{"startTime":"startTime","endTime":"endTime"},{"startTime":"startTime","endTime":"endTime"}],"queryTerms":[{"fullMatch":True,"value":"value"},{"fullMatch":True,"value":"value"}]},"ignoreAction":{"ignoreTerms":["ignoreTerms","ignoreTerms"]},"redirectAction":{"redirectUri":"redirectUri"},"boostAction":{"boost":6.0274563,"productsFilter":"productsFilter"},"twowaySynonymsAction":{"synonyms":["synonyms","synonyms"]},"doNotAssociateAction":{"doNotAssociateTerms":["doNotAssociateTerms","doNotAssociateTerms"],"terms":["terms","terms"],"queryTerms":["queryTerms","queryTerms"]},"replacementAction":{"replacementTerm":"replacementTerm","queryTerms":["queryTerms","queryTerms"],"term":"term"},"filterAction":{"filter":"filter"},"onewaySynonymsAction":{"synonyms":["synonyms","synonyms"],"onewayTerms":["onewayTerms","onewayTerms"],"queryTerms":["queryTerms","queryTerms"]},"removeFacetAction":{"attributeNames":["attributeNames","attributeNames"]},"forceReturnFacetAction":{"facetPositionAdjustments":[{"attributeName":"attributeName","position":1},{"attributeName":"attributeName","position":1}]}},"solutionTypes":["SOLUTION_TYPE_UNSPECIFIED","SOLUTION_TYPE_UNSPECIFIED"],"searchSolutionUseCase":["SEARCH_SOLUTION_USE_CASE_UNSPECIFIED","SEARCH_SOLUTION_USE_CASE_UNSPECIFIED"]}
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
                    ('controlId', 'control_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2beta/{parent}/controls'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_controls_list(client):
    """Test case for retail_projects_locations_catalogs_controls_list

    
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
        path='/v2beta/{parent}/controls'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_export_analytics_metrics(client):
    """Test case for retail_projects_locations_catalogs_export_analytics_metrics

    
    """
    body = {"filter":"filter","outputConfig":{"gcsDestination":{"outputUriPrefix":"outputUriPrefix"},"bigqueryDestination":{"tableType":"tableType","datasetId":"datasetId","tableIdPrefix":"tableIdPrefix"}}}
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
        path='/v2beta/{catalogexport_analytics_metric}'.format(catalog='catalog_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_get_default_branch(client):
    """Test case for retail_projects_locations_catalogs_get_default_branch

    
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
        path='/v2beta/{catalogget_default_branc}'.format(catalog='catalog_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_list(client):
    """Test case for retail_projects_locations_catalogs_list

    
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
        path='/v2beta/{parent}/catalogs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_models_create(client):
    """Test case for retail_projects_locations_catalogs_models_create

    
    """
    body = {"servingConfigLists":[{"servingConfigIds":["servingConfigIds","servingConfigIds"]},{"servingConfigIds":["servingConfigIds","servingConfigIds"]}],"filteringOption":"RECOMMENDATIONS_FILTERING_OPTION_UNSPECIFIED","tuningOperation":"tuningOperation","optimizationObjective":"optimizationObjective","displayName":"displayName","dataState":"DATA_STATE_UNSPECIFIED","trainingState":"TRAINING_STATE_UNSPECIFIED","updateTime":"updateTime","type":"type","createTime":"createTime","modelFeaturesConfig":{"frequentlyBoughtTogetherConfig":{"contextProductsType":"CONTEXT_PRODUCTS_TYPE_UNSPECIFIED"}},"name":"name","lastTuneTime":"lastTuneTime","periodicTuningState":"PERIODIC_TUNING_STATE_UNSPECIFIED","servingState":"SERVING_STATE_UNSPECIFIED"}
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
                    ('dryRun', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2beta/{parent}/models'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_models_list(client):
    """Test case for retail_projects_locations_catalogs_models_list

    
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
        path='/v2beta/{parent}/models'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_models_pause(client):
    """Test case for retail_projects_locations_catalogs_models_pause

    
    """
    body = None
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
        path='/v2beta/{namepaus}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_models_resume(client):
    """Test case for retail_projects_locations_catalogs_models_resume

    
    """
    body = None
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
        path='/v2beta/{nameresum}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_models_tune(client):
    """Test case for retail_projects_locations_catalogs_models_tune

    
    """
    body = None
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
        path='/v2beta/{nametun}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_serving_configs_add_control(client):
    """Test case for retail_projects_locations_catalogs_serving_configs_add_control

    
    """
    body = {"controlId":"controlId"}
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
        path='/v2beta/{serving_configadd_contro}'.format(serving_config='serving_config_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_serving_configs_create(client):
    """Test case for retail_projects_locations_catalogs_serving_configs_create

    
    """
    body = {"enableCategoryFilterLevel":"enableCategoryFilterLevel","personalizationSpec":{"mode":"MODE_UNSPECIFIED"},"modelId":"modelId","displayName":"displayName","replacementControlIds":["replacementControlIds","replacementControlIds"],"boostControlIds":["boostControlIds","boostControlIds"],"doNotAssociateControlIds":["doNotAssociateControlIds","doNotAssociateControlIds"],"solutionTypes":["SOLUTION_TYPE_UNSPECIFIED","SOLUTION_TYPE_UNSPECIFIED"],"priceRerankingLevel":"priceRerankingLevel","diversityType":"DIVERSITY_TYPE_UNSPECIFIED","twowaySynonymsControlIds":["twowaySynonymsControlIds","twowaySynonymsControlIds"],"ignoreControlIds":["ignoreControlIds","ignoreControlIds"],"name":"name","onewaySynonymsControlIds":["onewaySynonymsControlIds","onewaySynonymsControlIds"],"filterControlIds":["filterControlIds","filterControlIds"],"facetControlIds":["facetControlIds","facetControlIds"],"redirectControlIds":["redirectControlIds","redirectControlIds"],"diversityLevel":"diversityLevel","dynamicFacetSpec":{"mode":"MODE_UNSPECIFIED"}}
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
                    ('servingConfigId', 'serving_config_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2beta/{parent}/servingConfigs'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_serving_configs_delete(client):
    """Test case for retail_projects_locations_catalogs_serving_configs_delete

    
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
        path='/v2beta/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_serving_configs_list(client):
    """Test case for retail_projects_locations_catalogs_serving_configs_list

    
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
        path='/v2beta/{parent}/servingConfigs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_serving_configs_patch(client):
    """Test case for retail_projects_locations_catalogs_serving_configs_patch

    
    """
    body = {"enableCategoryFilterLevel":"enableCategoryFilterLevel","personalizationSpec":{"mode":"MODE_UNSPECIFIED"},"modelId":"modelId","displayName":"displayName","replacementControlIds":["replacementControlIds","replacementControlIds"],"boostControlIds":["boostControlIds","boostControlIds"],"doNotAssociateControlIds":["doNotAssociateControlIds","doNotAssociateControlIds"],"solutionTypes":["SOLUTION_TYPE_UNSPECIFIED","SOLUTION_TYPE_UNSPECIFIED"],"priceRerankingLevel":"priceRerankingLevel","diversityType":"DIVERSITY_TYPE_UNSPECIFIED","twowaySynonymsControlIds":["twowaySynonymsControlIds","twowaySynonymsControlIds"],"ignoreControlIds":["ignoreControlIds","ignoreControlIds"],"name":"name","onewaySynonymsControlIds":["onewaySynonymsControlIds","onewaySynonymsControlIds"],"filterControlIds":["filterControlIds","filterControlIds"],"facetControlIds":["facetControlIds","facetControlIds"],"redirectControlIds":["redirectControlIds","redirectControlIds"],"diversityLevel":"diversityLevel","dynamicFacetSpec":{"mode":"MODE_UNSPECIFIED"}}
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
        path='/v2beta/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_serving_configs_predict(client):
    """Test case for retail_projects_locations_catalogs_serving_configs_predict

    
    """
    body = {"filter":"filter","userEvent":{"userInfo":{"directUserRequest":True,"ipAddress":"ipAddress","userAgent":"userAgent","userId":"userId"},"experimentIds":["experimentIds","experimentIds"],"offset":6,"attributionToken":"attributionToken","cartId":"cartId","orderBy":"orderBy","eventType":"eventType","sessionId":"sessionId","productDetails":[{"product":{"rating":{"ratingHistogram":[3,3],"averageRating":7.0614014,"ratingCount":9},"description":"description","availability":"AVAILABILITY_UNSPECIFIED","variants":[null,null],"title":"title","type":"TYPE_UNSPECIFIED","priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"availableTime":"availableTime","collectionMemberIds":["collectionMemberIds","collectionMemberIds"],"sizes":["sizes","sizes"],"retrievableFields":"retrievableFields","categories":["categories","categories"],"id":"id","fulfillmentInfo":[{"type":"type","placeIds":["placeIds","placeIds"]},{"type":"type","placeIds":["placeIds","placeIds"]}],"availableQuantity":0,"publishTime":"publishTime","audience":{"genders":["genders","genders"],"ageGroups":["ageGroups","ageGroups"]},"gtin":"gtin","images":[{"width":1,"uri":"uri","height":6},{"width":1,"uri":"uri","height":6}],"brands":["brands","brands"],"patterns":["patterns","patterns"],"languageCode":"languageCode","ttl":"ttl","uri":"uri","localInventories":[{"priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"placeId":"placeId","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"fulfillmentTypes":["fulfillmentTypes","fulfillmentTypes"]},{"priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"placeId":"placeId","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"fulfillmentTypes":["fulfillmentTypes","fulfillmentTypes"]}],"primaryProductId":"primaryProductId","tags":["tags","tags"],"promotions":[{"promotionId":"promotionId"},{"promotionId":"promotionId"}],"expireTime":"expireTime","materials":["materials","materials"],"name":"name","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"colorInfo":{"colorFamilies":["colorFamilies","colorFamilies"],"colors":["colors","colors"]},"conditions":["conditions","conditions"]},"quantity":1},{"product":{"rating":{"ratingHistogram":[3,3],"averageRating":7.0614014,"ratingCount":9},"description":"description","availability":"AVAILABILITY_UNSPECIFIED","variants":[null,null],"title":"title","type":"TYPE_UNSPECIFIED","priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"availableTime":"availableTime","collectionMemberIds":["collectionMemberIds","collectionMemberIds"],"sizes":["sizes","sizes"],"retrievableFields":"retrievableFields","categories":["categories","categories"],"id":"id","fulfillmentInfo":[{"type":"type","placeIds":["placeIds","placeIds"]},{"type":"type","placeIds":["placeIds","placeIds"]}],"availableQuantity":0,"publishTime":"publishTime","audience":{"genders":["genders","genders"],"ageGroups":["ageGroups","ageGroups"]},"gtin":"gtin","images":[{"width":1,"uri":"uri","height":6},{"width":1,"uri":"uri","height":6}],"brands":["brands","brands"],"patterns":["patterns","patterns"],"languageCode":"languageCode","ttl":"ttl","uri":"uri","localInventories":[{"priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"placeId":"placeId","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"fulfillmentTypes":["fulfillmentTypes","fulfillmentTypes"]},{"priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"placeId":"placeId","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"fulfillmentTypes":["fulfillmentTypes","fulfillmentTypes"]}],"primaryProductId":"primaryProductId","tags":["tags","tags"],"promotions":[{"promotionId":"promotionId"},{"promotionId":"promotionId"}],"expireTime":"expireTime","materials":["materials","materials"],"name":"name","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"colorInfo":{"colorFamilies":["colorFamilies","colorFamilies"],"colors":["colors","colors"]},"conditions":["conditions","conditions"]},"quantity":1}],"uri":"uri","filter":"filter","purchaseTransaction":{"revenue":5.637377,"cost":5.962134,"tax":2.302136,"id":"id","currencyCode":"currencyCode"},"pageCategories":["pageCategories","pageCategories"],"referrerUri":"referrerUri","searchQuery":"searchQuery","eventTime":"eventTime","pageViewId":"pageViewId","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"completionDetail":{"completionAttributionToken":"completionAttributionToken","selectedSuggestion":"selectedSuggestion","selectedPosition":0},"entity":"entity","visitorId":"visitorId"},"validateOnly":True,"pageSize":0,"pageToken":"pageToken","params":{"key":""},"labels":{"key":"labels"}}
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
        path='/v2beta/{placementpredic}'.format(placement='placement_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_serving_configs_remove_control(client):
    """Test case for retail_projects_locations_catalogs_serving_configs_remove_control

    
    """
    body = {"controlId":"controlId"}
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
        path='/v2beta/{serving_configremove_contro}'.format(serving_config='serving_config_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_serving_configs_search(client):
    """Test case for retail_projects_locations_catalogs_serving_configs_search

    
    """
    body = {"queryExpansionSpec":{"condition":"CONDITION_UNSPECIFIED","pinUnexpandedResults":True},"userInfo":{"directUserRequest":True,"ipAddress":"ipAddress","userAgent":"userAgent","userId":"userId"},"personalizationSpec":{"mode":"MODE_UNSPECIFIED"},"offset":0,"query":"query","searchMode":"SEARCH_MODE_UNSPECIFIED","orderBy":"orderBy","pageSize":6,"branch":"branch","boostSpec":{"skipBoostSpecValidation":True,"conditionBoostSpecs":[{"condition":"condition","boost":1.4658129},{"condition":"condition","boost":1.4658129}]},"labels":{"key":"labels"},"filter":"filter","spellCorrectionSpec":{"mode":"MODE_UNSPECIFIED"},"variantRollupKeys":["variantRollupKeys","variantRollupKeys"],"pageCategories":["pageCategories","pageCategories"],"facetSpecs":[{"facetKey":{"contains":["contains","contains"],"intervals":[{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}],"prefixes":["prefixes","prefixes"],"restrictedValues":["restrictedValues","restrictedValues"],"returnMinMax":True,"query":"query","caseInsensitive":True,"orderBy":"orderBy","key":"key"},"enableDynamicPosition":True,"limit":0,"excludedFilterKeys":["excludedFilterKeys","excludedFilterKeys"]},{"facetKey":{"contains":["contains","contains"],"intervals":[{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}],"prefixes":["prefixes","prefixes"],"restrictedValues":["restrictedValues","restrictedValues"],"returnMinMax":True,"query":"query","caseInsensitive":True,"orderBy":"orderBy","key":"key"},"enableDynamicPosition":True,"limit":0,"excludedFilterKeys":["excludedFilterKeys","excludedFilterKeys"]}],"pageToken":"pageToken","dynamicFacetSpec":{"mode":"MODE_UNSPECIFIED"},"canonicalFilter":"canonicalFilter","entity":"entity","visitorId":"visitorId"}
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
        path='/v2beta/{placementsearc}'.format(placement='placement_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_set_default_branch(client):
    """Test case for retail_projects_locations_catalogs_set_default_branch

    
    """
    body = {"branchId":"branchId","note":"note","force":True}
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
        path='/v2beta/{catalogset_default_branc}'.format(catalog='catalog_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_user_events_collect(client):
    """Test case for retail_projects_locations_catalogs_user_events_collect

    
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
                    ('prebuiltRule', 'prebuilt_rule_example'),
                    ('rawJson', 'raw_json_example'),
                    ('uri', 'uri_example'),
                    ('userEvent', 'user_event_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2beta/{parent}/userEvents:collect'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_user_events_import(client):
    """Test case for retail_projects_locations_catalogs_user_events_import

    
    """
    body = {"inputConfig":{"userEventInlineSource":{"userEvents":[{"userInfo":{"directUserRequest":True,"ipAddress":"ipAddress","userAgent":"userAgent","userId":"userId"},"experimentIds":["experimentIds","experimentIds"],"offset":6,"attributionToken":"attributionToken","cartId":"cartId","orderBy":"orderBy","eventType":"eventType","sessionId":"sessionId","productDetails":[{"product":{"rating":{"ratingHistogram":[3,3],"averageRating":7.0614014,"ratingCount":9},"description":"description","availability":"AVAILABILITY_UNSPECIFIED","variants":[null,null],"title":"title","type":"TYPE_UNSPECIFIED","priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"availableTime":"availableTime","collectionMemberIds":["collectionMemberIds","collectionMemberIds"],"sizes":["sizes","sizes"],"retrievableFields":"retrievableFields","categories":["categories","categories"],"id":"id","fulfillmentInfo":[{"type":"type","placeIds":["placeIds","placeIds"]},{"type":"type","placeIds":["placeIds","placeIds"]}],"availableQuantity":0,"publishTime":"publishTime","audience":{"genders":["genders","genders"],"ageGroups":["ageGroups","ageGroups"]},"gtin":"gtin","images":[{"width":1,"uri":"uri","height":6},{"width":1,"uri":"uri","height":6}],"brands":["brands","brands"],"patterns":["patterns","patterns"],"languageCode":"languageCode","ttl":"ttl","uri":"uri","localInventories":[{"priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"placeId":"placeId","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"fulfillmentTypes":["fulfillmentTypes","fulfillmentTypes"]},{"priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"placeId":"placeId","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"fulfillmentTypes":["fulfillmentTypes","fulfillmentTypes"]}],"primaryProductId":"primaryProductId","tags":["tags","tags"],"promotions":[{"promotionId":"promotionId"},{"promotionId":"promotionId"}],"expireTime":"expireTime","materials":["materials","materials"],"name":"name","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"colorInfo":{"colorFamilies":["colorFamilies","colorFamilies"],"colors":["colors","colors"]},"conditions":["conditions","conditions"]},"quantity":1},{"product":{"rating":{"ratingHistogram":[3,3],"averageRating":7.0614014,"ratingCount":9},"description":"description","availability":"AVAILABILITY_UNSPECIFIED","variants":[null,null],"title":"title","type":"TYPE_UNSPECIFIED","priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"availableTime":"availableTime","collectionMemberIds":["collectionMemberIds","collectionMemberIds"],"sizes":["sizes","sizes"],"retrievableFields":"retrievableFields","categories":["categories","categories"],"id":"id","fulfillmentInfo":[{"type":"type","placeIds":["placeIds","placeIds"]},{"type":"type","placeIds":["placeIds","placeIds"]}],"availableQuantity":0,"publishTime":"publishTime","audience":{"genders":["genders","genders"],"ageGroups":["ageGroups","ageGroups"]},"gtin":"gtin","images":[{"width":1,"uri":"uri","height":6},{"width":1,"uri":"uri","height":6}],"brands":["brands","brands"],"patterns":["patterns","patterns"],"languageCode":"languageCode","ttl":"ttl","uri":"uri","localInventories":[{"priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"placeId":"placeId","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"fulfillmentTypes":["fulfillmentTypes","fulfillmentTypes"]},{"priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"placeId":"placeId","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"fulfillmentTypes":["fulfillmentTypes","fulfillmentTypes"]}],"primaryProductId":"primaryProductId","tags":["tags","tags"],"promotions":[{"promotionId":"promotionId"},{"promotionId":"promotionId"}],"expireTime":"expireTime","materials":["materials","materials"],"name":"name","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"colorInfo":{"colorFamilies":["colorFamilies","colorFamilies"],"colors":["colors","colors"]},"conditions":["conditions","conditions"]},"quantity":1}],"uri":"uri","filter":"filter","purchaseTransaction":{"revenue":5.637377,"cost":5.962134,"tax":2.302136,"id":"id","currencyCode":"currencyCode"},"pageCategories":["pageCategories","pageCategories"],"referrerUri":"referrerUri","searchQuery":"searchQuery","eventTime":"eventTime","pageViewId":"pageViewId","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"completionDetail":{"completionAttributionToken":"completionAttributionToken","selectedSuggestion":"selectedSuggestion","selectedPosition":0},"entity":"entity","visitorId":"visitorId"},{"userInfo":{"directUserRequest":True,"ipAddress":"ipAddress","userAgent":"userAgent","userId":"userId"},"experimentIds":["experimentIds","experimentIds"],"offset":6,"attributionToken":"attributionToken","cartId":"cartId","orderBy":"orderBy","eventType":"eventType","sessionId":"sessionId","productDetails":[{"product":{"rating":{"ratingHistogram":[3,3],"averageRating":7.0614014,"ratingCount":9},"description":"description","availability":"AVAILABILITY_UNSPECIFIED","variants":[null,null],"title":"title","type":"TYPE_UNSPECIFIED","priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"availableTime":"availableTime","collectionMemberIds":["collectionMemberIds","collectionMemberIds"],"sizes":["sizes","sizes"],"retrievableFields":"retrievableFields","categories":["categories","categories"],"id":"id","fulfillmentInfo":[{"type":"type","placeIds":["placeIds","placeIds"]},{"type":"type","placeIds":["placeIds","placeIds"]}],"availableQuantity":0,"publishTime":"publishTime","audience":{"genders":["genders","genders"],"ageGroups":["ageGroups","ageGroups"]},"gtin":"gtin","images":[{"width":1,"uri":"uri","height":6},{"width":1,"uri":"uri","height":6}],"brands":["brands","brands"],"patterns":["patterns","patterns"],"languageCode":"languageCode","ttl":"ttl","uri":"uri","localInventories":[{"priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"placeId":"placeId","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"fulfillmentTypes":["fulfillmentTypes","fulfillmentTypes"]},{"priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"placeId":"placeId","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"fulfillmentTypes":["fulfillmentTypes","fulfillmentTypes"]}],"primaryProductId":"primaryProductId","tags":["tags","tags"],"promotions":[{"promotionId":"promotionId"},{"promotionId":"promotionId"}],"expireTime":"expireTime","materials":["materials","materials"],"name":"name","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"colorInfo":{"colorFamilies":["colorFamilies","colorFamilies"],"colors":["colors","colors"]},"conditions":["conditions","conditions"]},"quantity":1},{"product":{"rating":{"ratingHistogram":[3,3],"averageRating":7.0614014,"ratingCount":9},"description":"description","availability":"AVAILABILITY_UNSPECIFIED","variants":[null,null],"title":"title","type":"TYPE_UNSPECIFIED","priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"availableTime":"availableTime","collectionMemberIds":["collectionMemberIds","collectionMemberIds"],"sizes":["sizes","sizes"],"retrievableFields":"retrievableFields","categories":["categories","categories"],"id":"id","fulfillmentInfo":[{"type":"type","placeIds":["placeIds","placeIds"]},{"type":"type","placeIds":["placeIds","placeIds"]}],"availableQuantity":0,"publishTime":"publishTime","audience":{"genders":["genders","genders"],"ageGroups":["ageGroups","ageGroups"]},"gtin":"gtin","images":[{"width":1,"uri":"uri","height":6},{"width":1,"uri":"uri","height":6}],"brands":["brands","brands"],"patterns":["patterns","patterns"],"languageCode":"languageCode","ttl":"ttl","uri":"uri","localInventories":[{"priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"placeId":"placeId","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"fulfillmentTypes":["fulfillmentTypes","fulfillmentTypes"]},{"priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"placeId":"placeId","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"fulfillmentTypes":["fulfillmentTypes","fulfillmentTypes"]}],"primaryProductId":"primaryProductId","tags":["tags","tags"],"promotions":[{"promotionId":"promotionId"},{"promotionId":"promotionId"}],"expireTime":"expireTime","materials":["materials","materials"],"name":"name","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"colorInfo":{"colorFamilies":["colorFamilies","colorFamilies"],"colors":["colors","colors"]},"conditions":["conditions","conditions"]},"quantity":1}],"uri":"uri","filter":"filter","purchaseTransaction":{"revenue":5.637377,"cost":5.962134,"tax":2.302136,"id":"id","currencyCode":"currencyCode"},"pageCategories":["pageCategories","pageCategories"],"referrerUri":"referrerUri","searchQuery":"searchQuery","eventTime":"eventTime","pageViewId":"pageViewId","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"completionDetail":{"completionAttributionToken":"completionAttributionToken","selectedSuggestion":"selectedSuggestion","selectedPosition":0},"entity":"entity","visitorId":"visitorId"}]},"bigQuerySource":{"dataSchema":"dataSchema","datasetId":"datasetId","partitionDate":{"month":6,"year":1,"day":0},"tableId":"tableId","projectId":"projectId","gcsStagingDir":"gcsStagingDir"},"gcsSource":{"dataSchema":"dataSchema","inputUris":["inputUris","inputUris"]}},"errorsConfig":{"gcsPrefix":"gcsPrefix"}}
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
        path='/v2beta/{parent}/userEvents:import'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_user_events_purge(client):
    """Test case for retail_projects_locations_catalogs_user_events_purge

    
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
        path='/v2beta/{parent}/userEvents:purge'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_user_events_rejoin(client):
    """Test case for retail_projects_locations_catalogs_user_events_rejoin

    
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
        path='/v2beta/{parent}/userEvents:rejoin'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_locations_catalogs_user_events_write(client):
    """Test case for retail_projects_locations_catalogs_user_events_write

    
    """
    body = {"userInfo":{"directUserRequest":True,"ipAddress":"ipAddress","userAgent":"userAgent","userId":"userId"},"experimentIds":["experimentIds","experimentIds"],"offset":6,"attributionToken":"attributionToken","cartId":"cartId","orderBy":"orderBy","eventType":"eventType","sessionId":"sessionId","productDetails":[{"product":{"rating":{"ratingHistogram":[3,3],"averageRating":7.0614014,"ratingCount":9},"description":"description","availability":"AVAILABILITY_UNSPECIFIED","variants":[null,null],"title":"title","type":"TYPE_UNSPECIFIED","priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"availableTime":"availableTime","collectionMemberIds":["collectionMemberIds","collectionMemberIds"],"sizes":["sizes","sizes"],"retrievableFields":"retrievableFields","categories":["categories","categories"],"id":"id","fulfillmentInfo":[{"type":"type","placeIds":["placeIds","placeIds"]},{"type":"type","placeIds":["placeIds","placeIds"]}],"availableQuantity":0,"publishTime":"publishTime","audience":{"genders":["genders","genders"],"ageGroups":["ageGroups","ageGroups"]},"gtin":"gtin","images":[{"width":1,"uri":"uri","height":6},{"width":1,"uri":"uri","height":6}],"brands":["brands","brands"],"patterns":["patterns","patterns"],"languageCode":"languageCode","ttl":"ttl","uri":"uri","localInventories":[{"priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"placeId":"placeId","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"fulfillmentTypes":["fulfillmentTypes","fulfillmentTypes"]},{"priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"placeId":"placeId","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"fulfillmentTypes":["fulfillmentTypes","fulfillmentTypes"]}],"primaryProductId":"primaryProductId","tags":["tags","tags"],"promotions":[{"promotionId":"promotionId"},{"promotionId":"promotionId"}],"expireTime":"expireTime","materials":["materials","materials"],"name":"name","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"colorInfo":{"colorFamilies":["colorFamilies","colorFamilies"],"colors":["colors","colors"]},"conditions":["conditions","conditions"]},"quantity":1},{"product":{"rating":{"ratingHistogram":[3,3],"averageRating":7.0614014,"ratingCount":9},"description":"description","availability":"AVAILABILITY_UNSPECIFIED","variants":[null,null],"title":"title","type":"TYPE_UNSPECIFIED","priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"availableTime":"availableTime","collectionMemberIds":["collectionMemberIds","collectionMemberIds"],"sizes":["sizes","sizes"],"retrievableFields":"retrievableFields","categories":["categories","categories"],"id":"id","fulfillmentInfo":[{"type":"type","placeIds":["placeIds","placeIds"]},{"type":"type","placeIds":["placeIds","placeIds"]}],"availableQuantity":0,"publishTime":"publishTime","audience":{"genders":["genders","genders"],"ageGroups":["ageGroups","ageGroups"]},"gtin":"gtin","images":[{"width":1,"uri":"uri","height":6},{"width":1,"uri":"uri","height":6}],"brands":["brands","brands"],"patterns":["patterns","patterns"],"languageCode":"languageCode","ttl":"ttl","uri":"uri","localInventories":[{"priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"placeId":"placeId","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"fulfillmentTypes":["fulfillmentTypes","fulfillmentTypes"]},{"priceInfo":{"cost":5.962134,"priceEffectiveTime":"priceEffectiveTime","originalPrice":5.637377,"price":2.302136,"priceExpireTime":"priceExpireTime","currencyCode":"currencyCode","priceRange":{"originalPrice":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182},"price":{"exclusiveMaximum":0.8008281904610115,"maximum":1.4658129805029452,"exclusiveMinimum":6.027456183070403,"minimum":5.962133916683182}}},"placeId":"placeId","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"fulfillmentTypes":["fulfillmentTypes","fulfillmentTypes"]}],"primaryProductId":"primaryProductId","tags":["tags","tags"],"promotions":[{"promotionId":"promotionId"},{"promotionId":"promotionId"}],"expireTime":"expireTime","materials":["materials","materials"],"name":"name","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"colorInfo":{"colorFamilies":["colorFamilies","colorFamilies"],"colors":["colors","colors"]},"conditions":["conditions","conditions"]},"quantity":1}],"uri":"uri","filter":"filter","purchaseTransaction":{"revenue":5.637377,"cost":5.962134,"tax":2.302136,"id":"id","currencyCode":"currencyCode"},"pageCategories":["pageCategories","pageCategories"],"referrerUri":"referrerUri","searchQuery":"searchQuery","eventTime":"eventTime","pageViewId":"pageViewId","attributes":{"key":{"indexable":True,"numbers":[0.8008281904610115,0.8008281904610115],"text":["text","text"],"searchable":True}},"completionDetail":{"completionAttributionToken":"completionAttributionToken","selectedSuggestion":"selectedSuggestion","selectedPosition":0},"entity":"entity","visitorId":"visitorId"}
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
                    ('writeAsync', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2beta/{parent}/userEvents:write'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_operations_get(client):
    """Test case for retail_projects_operations_get

    
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
        path='/v2beta/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retail_projects_operations_list(client):
    """Test case for retail_projects_operations_list

    
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
        path='/v2beta/{name}/operations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

