# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.conversion_list import ConversionList
from openapi_server.models.update_availability_request import UpdateAvailabilityRequest
from openapi_server.models.update_availability_response import UpdateAvailabilityResponse


pytestmark = pytest.mark.asyncio

async def test_doubleclicksearch_conversion_get(client):
    """Test case for doubleclicksearch_conversion_get

    
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
                    ('endDate', 56),
                    ('rowCount', 56),
                    ('startDate', 56),
                    ('startRow', 56),
                    ('adGroupId', 'ad_group_id_example'),
                    ('adId', 'ad_id_example'),
                    ('campaignId', 'campaign_id_example'),
                    ('criterionId', 'criterion_id_example'),
                    ('customerId', 'customer_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/doubleclicksearch/v2/agency/{agency_id}/advertiser/{advertiser_id}/engine/{engine_account_id}/conversion'.format(agency_id='agency_id_example', advertiser_id='advertiser_id_example', engine_account_id='engine_account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_doubleclicksearch_conversion_get_by_customer_id(client):
    """Test case for doubleclicksearch_conversion_get_by_customer_id

    
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
                    ('endDate', 56),
                    ('rowCount', 56),
                    ('startDate', 56),
                    ('startRow', 56),
                    ('adGroupId', 'ad_group_id_example'),
                    ('adId', 'ad_id_example'),
                    ('advertiserId', 'advertiser_id_example'),
                    ('agencyId', 'agency_id_example'),
                    ('campaignId', 'campaign_id_example'),
                    ('criterionId', 'criterion_id_example'),
                    ('engineAccountId', 'engine_account_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/doubleclicksearch/v2/customer/{customer_id}/conversion'.format(customer_id='customer_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_doubleclicksearch_conversion_insert(client):
    """Test case for doubleclicksearch_conversion_insert

    
    """
    body = {"kind":"kind","conversion":[{"inventoryAccountId":"inventoryAccountId","criterionId":"criterionId","channel":"channel","productGroupId":"productGroupId","clickId":"clickId","agencyId":"agencyId","floodlightOrderId":"floodlightOrderId","customMetric":[{"name":"name","value":0.8008281904610115},{"name":"name","value":0.8008281904610115}],"segmentationName":"segmentationName","type":"type","adGroupId":"adGroupId","adUserDataConsent":"UNKNOWN","dsConversionId":"dsConversionId","customerId":"customerId","conversionModifiedTimestamp":"conversionModifiedTimestamp","customDimension":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"state":"state","conversionId":"conversionId","segmentationId":"segmentationId","quantityMillis":"quantityMillis","deviceType":"deviceType","productId":"productId","campaignId":"campaignId","storeId":"storeId","advertiserId":"advertiserId","attributionModel":"attributionModel","adId":"adId","productLanguage":"productLanguage","countMillis":"countMillis","segmentationType":"segmentationType","engineAccountId":"engineAccountId","productCountry":"productCountry","currencyCode":"currencyCode","revenueMicros":"revenueMicros","conversionTimestamp":"conversionTimestamp"},{"inventoryAccountId":"inventoryAccountId","criterionId":"criterionId","channel":"channel","productGroupId":"productGroupId","clickId":"clickId","agencyId":"agencyId","floodlightOrderId":"floodlightOrderId","customMetric":[{"name":"name","value":0.8008281904610115},{"name":"name","value":0.8008281904610115}],"segmentationName":"segmentationName","type":"type","adGroupId":"adGroupId","adUserDataConsent":"UNKNOWN","dsConversionId":"dsConversionId","customerId":"customerId","conversionModifiedTimestamp":"conversionModifiedTimestamp","customDimension":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"state":"state","conversionId":"conversionId","segmentationId":"segmentationId","quantityMillis":"quantityMillis","deviceType":"deviceType","productId":"productId","campaignId":"campaignId","storeId":"storeId","advertiserId":"advertiserId","attributionModel":"attributionModel","adId":"adId","productLanguage":"productLanguage","countMillis":"countMillis","segmentationType":"segmentationType","engineAccountId":"engineAccountId","productCountry":"productCountry","currencyCode":"currencyCode","revenueMicros":"revenueMicros","conversionTimestamp":"conversionTimestamp"}]}
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
        path='/doubleclicksearch/v2/conversion',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_doubleclicksearch_conversion_update(client):
    """Test case for doubleclicksearch_conversion_update

    
    """
    body = {"kind":"kind","conversion":[{"inventoryAccountId":"inventoryAccountId","criterionId":"criterionId","channel":"channel","productGroupId":"productGroupId","clickId":"clickId","agencyId":"agencyId","floodlightOrderId":"floodlightOrderId","customMetric":[{"name":"name","value":0.8008281904610115},{"name":"name","value":0.8008281904610115}],"segmentationName":"segmentationName","type":"type","adGroupId":"adGroupId","adUserDataConsent":"UNKNOWN","dsConversionId":"dsConversionId","customerId":"customerId","conversionModifiedTimestamp":"conversionModifiedTimestamp","customDimension":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"state":"state","conversionId":"conversionId","segmentationId":"segmentationId","quantityMillis":"quantityMillis","deviceType":"deviceType","productId":"productId","campaignId":"campaignId","storeId":"storeId","advertiserId":"advertiserId","attributionModel":"attributionModel","adId":"adId","productLanguage":"productLanguage","countMillis":"countMillis","segmentationType":"segmentationType","engineAccountId":"engineAccountId","productCountry":"productCountry","currencyCode":"currencyCode","revenueMicros":"revenueMicros","conversionTimestamp":"conversionTimestamp"},{"inventoryAccountId":"inventoryAccountId","criterionId":"criterionId","channel":"channel","productGroupId":"productGroupId","clickId":"clickId","agencyId":"agencyId","floodlightOrderId":"floodlightOrderId","customMetric":[{"name":"name","value":0.8008281904610115},{"name":"name","value":0.8008281904610115}],"segmentationName":"segmentationName","type":"type","adGroupId":"adGroupId","adUserDataConsent":"UNKNOWN","dsConversionId":"dsConversionId","customerId":"customerId","conversionModifiedTimestamp":"conversionModifiedTimestamp","customDimension":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"state":"state","conversionId":"conversionId","segmentationId":"segmentationId","quantityMillis":"quantityMillis","deviceType":"deviceType","productId":"productId","campaignId":"campaignId","storeId":"storeId","advertiserId":"advertiserId","attributionModel":"attributionModel","adId":"adId","productLanguage":"productLanguage","countMillis":"countMillis","segmentationType":"segmentationType","engineAccountId":"engineAccountId","productCountry":"productCountry","currencyCode":"currencyCode","revenueMicros":"revenueMicros","conversionTimestamp":"conversionTimestamp"}]}
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
        method='PUT',
        path='/doubleclicksearch/v2/conversion',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_doubleclicksearch_conversion_update_availability(client):
    """Test case for doubleclicksearch_conversion_update_availability

    
    """
    body = {"availabilities":[{"availabilityTimestamp":"availabilityTimestamp","customerId":"customerId","segmentationType":"segmentationType","agencyId":"agencyId","segmentationName":"segmentationName","segmentationId":"segmentationId","advertiserId":"advertiserId"},{"availabilityTimestamp":"availabilityTimestamp","customerId":"customerId","segmentationType":"segmentationType","agencyId":"agencyId","segmentationName":"segmentationName","segmentationId":"segmentationId","advertiserId":"advertiserId"}]}
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
        path='/doubleclicksearch/v2/conversion/updateAvailability',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

