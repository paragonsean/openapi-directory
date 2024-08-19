# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.sas_portal_create_signed_device_request import SasPortalCreateSignedDeviceRequest
from openapi_server.models.sas_portal_deployment import SasPortalDeployment
from openapi_server.models.sas_portal_device import SasPortalDevice
from openapi_server.models.sas_portal_list_deployments_response import SasPortalListDeploymentsResponse
from openapi_server.models.sas_portal_list_devices_response import SasPortalListDevicesResponse
from openapi_server.models.sas_portal_list_nodes_response import SasPortalListNodesResponse
from openapi_server.models.sas_portal_move_node_request import SasPortalMoveNodeRequest
from openapi_server.models.sas_portal_node import SasPortalNode
from openapi_server.models.sas_portal_operation import SasPortalOperation
from openapi_server.models.sas_portal_sign_device_request import SasPortalSignDeviceRequest
from openapi_server.models.sas_portal_update_signed_device_request import SasPortalUpdateSignedDeviceRequest


pytestmark = pytest.mark.asyncio

async def test_sasportal_nodes_devices_sign_device(client):
    """Test case for sasportal_nodes_devices_sign_device

    
    """
    body = {"device":{"grants":[{"expireTime":"expireTime","grantId":"grantId","suspensionReason":["suspensionReason","suspensionReason"],"frequencyRange":{"highFrequencyMhz":4.145608029883936,"lowFrequencyMhz":7.386281948385884},"channelType":"CHANNEL_TYPE_UNSPECIFIED","lastHeartbeatTransmitExpireTime":"lastHeartbeatTransmitExpireTime","state":"GRANT_STATE_UNSPECIFIED","moveList":[{"dpaId":"dpaId","frequencyRange":{"highFrequencyMhz":4.145608029883936,"lowFrequencyMhz":7.386281948385884}},{"dpaId":"dpaId","frequencyRange":{"highFrequencyMhz":4.145608029883936,"lowFrequencyMhz":7.386281948385884}}],"maxEirp":6.84685269835264},{"expireTime":"expireTime","grantId":"grantId","suspensionReason":["suspensionReason","suspensionReason"],"frequencyRange":{"highFrequencyMhz":4.145608029883936,"lowFrequencyMhz":7.386281948385884},"channelType":"CHANNEL_TYPE_UNSPECIFIED","lastHeartbeatTransmitExpireTime":"lastHeartbeatTransmitExpireTime","state":"GRANT_STATE_UNSPECIFIED","moveList":[{"dpaId":"dpaId","frequencyRange":{"highFrequencyMhz":4.145608029883936,"lowFrequencyMhz":7.386281948385884}},{"dpaId":"dpaId","frequencyRange":{"highFrequencyMhz":4.145608029883936,"lowFrequencyMhz":7.386281948385884}}],"maxEirp":6.84685269835264}],"preloadedConfig":{"isSigned":True,"airInterface":{"supportedSpec":"supportedSpec","radioTechnology":"RADIO_TECHNOLOGY_UNSPECIFIED"},"installationParams":{"cpeCbsdIndication":True,"indoorDeployment":True,"antennaModel":"antennaModel","latitude":9.301444243932576,"antennaGain":5,"horizontalAccuracy":7.061401241503109,"heightType":"HEIGHT_TYPE_UNSPECIFIED","verticalAccuracy":2.027123023002322,"antennaBeamwidth":6,"antennaDowntilt":1,"antennaAzimuth":0,"eirpCapability":5,"height":2.3021358869347655,"longitude":3.616076749251911},"measurementCapabilities":["MEASUREMENT_CAPABILITY_UNSPECIFIED","MEASUREMENT_CAPABILITY_UNSPECIFIED"],"model":{"vendor":"vendor","name":"name","hardwareVersion":"hardwareVersion","firmwareVersion":"firmwareVersion","softwareVersion":"softwareVersion"},"updateTime":"updateTime","state":"DEVICE_CONFIG_STATE_UNSPECIFIED","category":"DEVICE_CATEGORY_UNSPECIFIED","userId":"userId","callSign":"callSign"},"serialNumber":"serialNumber","activeConfig":{"isSigned":True,"airInterface":{"supportedSpec":"supportedSpec","radioTechnology":"RADIO_TECHNOLOGY_UNSPECIFIED"},"installationParams":{"cpeCbsdIndication":True,"indoorDeployment":True,"antennaModel":"antennaModel","latitude":9.301444243932576,"antennaGain":5,"horizontalAccuracy":7.061401241503109,"heightType":"HEIGHT_TYPE_UNSPECIFIED","verticalAccuracy":2.027123023002322,"antennaBeamwidth":6,"antennaDowntilt":1,"antennaAzimuth":0,"eirpCapability":5,"height":2.3021358869347655,"longitude":3.616076749251911},"measurementCapabilities":["MEASUREMENT_CAPABILITY_UNSPECIFIED","MEASUREMENT_CAPABILITY_UNSPECIFIED"],"model":{"vendor":"vendor","name":"name","hardwareVersion":"hardwareVersion","firmwareVersion":"firmwareVersion","softwareVersion":"softwareVersion"},"updateTime":"updateTime","state":"DEVICE_CONFIG_STATE_UNSPECIFIED","category":"DEVICE_CATEGORY_UNSPECIFIED","userId":"userId","callSign":"callSign"},"displayName":"displayName","deviceMetadata":{"nrqzValidation":{"cpiId":"cpiId","caseId":"caseId","latitude":1.0246457001441578,"state":"STATE_UNSPECIFIED","longitude":1.4894159098541704},"commonChannelGroup":"commonChannelGroup","interferenceCoordinationGroup":"interferenceCoordinationGroup","nrqzValidated":True,"antennaModel":"antennaModel"},"name":"name","fccId":"fccId","grantRangeAllowlists":[{"highFrequencyMhz":4.145608029883936,"lowFrequencyMhz":7.386281948385884},{"highFrequencyMhz":4.145608029883936,"lowFrequencyMhz":7.386281948385884}],"state":"DEVICE_STATE_UNSPECIFIED","currentChannels":[{"score":1.2315135367772556,"frequencyRange":{"highFrequencyMhz":4.145608029883936,"lowFrequencyMhz":7.386281948385884}},{"score":1.2315135367772556,"frequencyRange":{"highFrequencyMhz":4.145608029883936,"lowFrequencyMhz":7.386281948385884}}]}}
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
        path='/v1alpha1/{namesign_devic}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sasportal_nodes_devices_update_signed(client):
    """Test case for sasportal_nodes_devices_update_signed

    
    """
    body = {"encodedDevice":"encodedDevice","installerId":"installerId"}
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
        method='PATCH',
        path='/v1alpha1/{nameupdate_signe}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sasportal_nodes_nodes_delete(client):
    """Test case for sasportal_nodes_nodes_delete

    
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
        path='/v1alpha1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sasportal_nodes_nodes_deployments_create(client):
    """Test case for sasportal_nodes_nodes_deployments_create

    
    """
    body = {"frns":["frns","frns"],"displayName":"displayName","name":"name","sasUserIds":["sasUserIds","sasUserIds"]}
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
        path='/v1alpha1/{parent}/deployments'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sasportal_nodes_nodes_deployments_list(client):
    """Test case for sasportal_nodes_nodes_deployments_list

    
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
        path='/v1alpha1/{parent}/deployments'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sasportal_nodes_nodes_devices_create(client):
    """Test case for sasportal_nodes_nodes_devices_create

    
    """
    body = {"grants":[{"expireTime":"expireTime","grantId":"grantId","suspensionReason":["suspensionReason","suspensionReason"],"frequencyRange":{"highFrequencyMhz":4.145608029883936,"lowFrequencyMhz":7.386281948385884},"channelType":"CHANNEL_TYPE_UNSPECIFIED","lastHeartbeatTransmitExpireTime":"lastHeartbeatTransmitExpireTime","state":"GRANT_STATE_UNSPECIFIED","moveList":[{"dpaId":"dpaId","frequencyRange":{"highFrequencyMhz":4.145608029883936,"lowFrequencyMhz":7.386281948385884}},{"dpaId":"dpaId","frequencyRange":{"highFrequencyMhz":4.145608029883936,"lowFrequencyMhz":7.386281948385884}}],"maxEirp":6.84685269835264},{"expireTime":"expireTime","grantId":"grantId","suspensionReason":["suspensionReason","suspensionReason"],"frequencyRange":{"highFrequencyMhz":4.145608029883936,"lowFrequencyMhz":7.386281948385884},"channelType":"CHANNEL_TYPE_UNSPECIFIED","lastHeartbeatTransmitExpireTime":"lastHeartbeatTransmitExpireTime","state":"GRANT_STATE_UNSPECIFIED","moveList":[{"dpaId":"dpaId","frequencyRange":{"highFrequencyMhz":4.145608029883936,"lowFrequencyMhz":7.386281948385884}},{"dpaId":"dpaId","frequencyRange":{"highFrequencyMhz":4.145608029883936,"lowFrequencyMhz":7.386281948385884}}],"maxEirp":6.84685269835264}],"preloadedConfig":{"isSigned":True,"airInterface":{"supportedSpec":"supportedSpec","radioTechnology":"RADIO_TECHNOLOGY_UNSPECIFIED"},"installationParams":{"cpeCbsdIndication":True,"indoorDeployment":True,"antennaModel":"antennaModel","latitude":9.301444243932576,"antennaGain":5,"horizontalAccuracy":7.061401241503109,"heightType":"HEIGHT_TYPE_UNSPECIFIED","verticalAccuracy":2.027123023002322,"antennaBeamwidth":6,"antennaDowntilt":1,"antennaAzimuth":0,"eirpCapability":5,"height":2.3021358869347655,"longitude":3.616076749251911},"measurementCapabilities":["MEASUREMENT_CAPABILITY_UNSPECIFIED","MEASUREMENT_CAPABILITY_UNSPECIFIED"],"model":{"vendor":"vendor","name":"name","hardwareVersion":"hardwareVersion","firmwareVersion":"firmwareVersion","softwareVersion":"softwareVersion"},"updateTime":"updateTime","state":"DEVICE_CONFIG_STATE_UNSPECIFIED","category":"DEVICE_CATEGORY_UNSPECIFIED","userId":"userId","callSign":"callSign"},"serialNumber":"serialNumber","activeConfig":{"isSigned":True,"airInterface":{"supportedSpec":"supportedSpec","radioTechnology":"RADIO_TECHNOLOGY_UNSPECIFIED"},"installationParams":{"cpeCbsdIndication":True,"indoorDeployment":True,"antennaModel":"antennaModel","latitude":9.301444243932576,"antennaGain":5,"horizontalAccuracy":7.061401241503109,"heightType":"HEIGHT_TYPE_UNSPECIFIED","verticalAccuracy":2.027123023002322,"antennaBeamwidth":6,"antennaDowntilt":1,"antennaAzimuth":0,"eirpCapability":5,"height":2.3021358869347655,"longitude":3.616076749251911},"measurementCapabilities":["MEASUREMENT_CAPABILITY_UNSPECIFIED","MEASUREMENT_CAPABILITY_UNSPECIFIED"],"model":{"vendor":"vendor","name":"name","hardwareVersion":"hardwareVersion","firmwareVersion":"firmwareVersion","softwareVersion":"softwareVersion"},"updateTime":"updateTime","state":"DEVICE_CONFIG_STATE_UNSPECIFIED","category":"DEVICE_CATEGORY_UNSPECIFIED","userId":"userId","callSign":"callSign"},"displayName":"displayName","deviceMetadata":{"nrqzValidation":{"cpiId":"cpiId","caseId":"caseId","latitude":1.0246457001441578,"state":"STATE_UNSPECIFIED","longitude":1.4894159098541704},"commonChannelGroup":"commonChannelGroup","interferenceCoordinationGroup":"interferenceCoordinationGroup","nrqzValidated":True,"antennaModel":"antennaModel"},"name":"name","fccId":"fccId","grantRangeAllowlists":[{"highFrequencyMhz":4.145608029883936,"lowFrequencyMhz":7.386281948385884},{"highFrequencyMhz":4.145608029883936,"lowFrequencyMhz":7.386281948385884}],"state":"DEVICE_STATE_UNSPECIFIED","currentChannels":[{"score":1.2315135367772556,"frequencyRange":{"highFrequencyMhz":4.145608029883936,"lowFrequencyMhz":7.386281948385884}},{"score":1.2315135367772556,"frequencyRange":{"highFrequencyMhz":4.145608029883936,"lowFrequencyMhz":7.386281948385884}}]}
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
        path='/v1alpha1/{parent}/devices'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sasportal_nodes_nodes_devices_create_signed(client):
    """Test case for sasportal_nodes_nodes_devices_create_signed

    
    """
    body = {"encodedDevice":"encodedDevice","installerId":"installerId"}
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
        path='/v1alpha1/{parent}/devices:createSigned'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sasportal_nodes_nodes_devices_list(client):
    """Test case for sasportal_nodes_nodes_devices_list

    
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
        path='/v1alpha1/{parent}/devices'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sasportal_nodes_nodes_get(client):
    """Test case for sasportal_nodes_nodes_get

    
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
        path='/v1alpha1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sasportal_nodes_nodes_move(client):
    """Test case for sasportal_nodes_nodes_move

    
    """
    body = {"destination":"destination"}
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
        path='/v1alpha1/{namemov}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sasportal_nodes_nodes_nodes_create(client):
    """Test case for sasportal_nodes_nodes_nodes_create

    
    """
    body = {"displayName":"displayName","name":"name","sasUserIds":["sasUserIds","sasUserIds"]}
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
        path='/v1alpha1/{parent}/nodes'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sasportal_nodes_nodes_nodes_list(client):
    """Test case for sasportal_nodes_nodes_nodes_list

    
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
        path='/v1alpha1/{parent}/nodes'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sasportal_nodes_nodes_patch(client):
    """Test case for sasportal_nodes_nodes_patch

    
    """
    body = {"displayName":"displayName","name":"name","sasUserIds":["sasUserIds","sasUserIds"]}
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
        path='/v1alpha1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

