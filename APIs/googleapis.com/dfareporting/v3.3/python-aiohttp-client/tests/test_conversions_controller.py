# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.conversions_batch_insert_request import ConversionsBatchInsertRequest
from openapi_server.models.conversions_batch_insert_response import ConversionsBatchInsertResponse
from openapi_server.models.conversions_batch_update_request import ConversionsBatchUpdateRequest
from openapi_server.models.conversions_batch_update_response import ConversionsBatchUpdateResponse


pytestmark = pytest.mark.asyncio

async def test_dfareporting_conversions_batchinsert(client):
    """Test case for dfareporting_conversions_batchinsert

    
    """
    body = {"encryptionInfo":{"encryptionEntityType":"ENCRYPTION_ENTITY_TYPE_UNKNOWN","kind":"kind","encryptionEntityId":"encryptionEntityId","encryptionSource":"ENCRYPTION_SCOPE_UNKNOWN"},"conversions":[{"nonPersonalizedAd":True,"quantity":"quantity","kind":"kind","customVariables":[{"kind":"kind","type":"U1","value":"value"},{"kind":"kind","type":"U1","value":"value"}],"timestampMicros":"timestampMicros","encryptedUserIdCandidates":["encryptedUserIdCandidates","encryptedUserIdCandidates"],"floodlightConfigurationId":"floodlightConfigurationId","limitAdTracking":True,"gclid":"gclid","mobileDeviceId":"mobileDeviceId","childDirectedTreatment":True,"floodlightActivityId":"floodlightActivityId","encryptedUserId":"encryptedUserId","treatmentForUnderage":True,"value":0.8008281904610115,"matchId":"matchId","ordinal":"ordinal"},{"nonPersonalizedAd":True,"quantity":"quantity","kind":"kind","customVariables":[{"kind":"kind","type":"U1","value":"value"},{"kind":"kind","type":"U1","value":"value"}],"timestampMicros":"timestampMicros","encryptedUserIdCandidates":["encryptedUserIdCandidates","encryptedUserIdCandidates"],"floodlightConfigurationId":"floodlightConfigurationId","limitAdTracking":True,"gclid":"gclid","mobileDeviceId":"mobileDeviceId","childDirectedTreatment":True,"floodlightActivityId":"floodlightActivityId","encryptedUserId":"encryptedUserId","treatmentForUnderage":True,"value":0.8008281904610115,"matchId":"matchId","ordinal":"ordinal"}],"kind":"kind"}
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
        path='/dfareporting/v3.3/userprofiles/{profile_id}/conversions/batchinsert'.format(profile_id='profile_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfareporting_conversions_batchupdate(client):
    """Test case for dfareporting_conversions_batchupdate

    
    """
    body = {"encryptionInfo":{"encryptionEntityType":"ENCRYPTION_ENTITY_TYPE_UNKNOWN","kind":"kind","encryptionEntityId":"encryptionEntityId","encryptionSource":"ENCRYPTION_SCOPE_UNKNOWN"},"conversions":[{"nonPersonalizedAd":True,"quantity":"quantity","kind":"kind","customVariables":[{"kind":"kind","type":"U1","value":"value"},{"kind":"kind","type":"U1","value":"value"}],"timestampMicros":"timestampMicros","encryptedUserIdCandidates":["encryptedUserIdCandidates","encryptedUserIdCandidates"],"floodlightConfigurationId":"floodlightConfigurationId","limitAdTracking":True,"gclid":"gclid","mobileDeviceId":"mobileDeviceId","childDirectedTreatment":True,"floodlightActivityId":"floodlightActivityId","encryptedUserId":"encryptedUserId","treatmentForUnderage":True,"value":0.8008281904610115,"matchId":"matchId","ordinal":"ordinal"},{"nonPersonalizedAd":True,"quantity":"quantity","kind":"kind","customVariables":[{"kind":"kind","type":"U1","value":"value"},{"kind":"kind","type":"U1","value":"value"}],"timestampMicros":"timestampMicros","encryptedUserIdCandidates":["encryptedUserIdCandidates","encryptedUserIdCandidates"],"floodlightConfigurationId":"floodlightConfigurationId","limitAdTracking":True,"gclid":"gclid","mobileDeviceId":"mobileDeviceId","childDirectedTreatment":True,"floodlightActivityId":"floodlightActivityId","encryptedUserId":"encryptedUserId","treatmentForUnderage":True,"value":0.8008281904610115,"matchId":"matchId","ordinal":"ordinal"}],"kind":"kind"}
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
        path='/dfareporting/v3.3/userprofiles/{profile_id}/conversions/batchupdate'.format(profile_id='profile_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

