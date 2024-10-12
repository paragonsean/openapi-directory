# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_provisioning_quotas_response import ListProvisioningQuotasResponse
from openapi_server.models.provisioning_config import ProvisioningConfig
from openapi_server.models.submit_provisioning_config_request import SubmitProvisioningConfigRequest


pytestmark = pytest.mark.asyncio

async def test_baremetalsolution_projects_locations_submit_provisioning_config(client):
    """Test case for baremetalsolution_projects_locations_submit_provisioning_config

    
    """
    body = {"provisioningConfig":{"instances":[{"privateNetwork":{"address":"address","existingNetworkId":"existingNetworkId","networkId":"networkId"},"userNote":"userNote","instanceType":"instanceType","location":"location","id":"id","clientNetwork":{"address":"address","existingNetworkId":"existingNetworkId","networkId":"networkId"},"hyperthreading":True,"osImage":"osImage"},{"privateNetwork":{"address":"address","existingNetworkId":"existingNetworkId","networkId":"networkId"},"userNote":"userNote","instanceType":"instanceType","location":"location","id":"id","clientNetwork":{"address":"address","existingNetworkId":"existingNetworkId","networkId":"networkId"},"hyperthreading":True,"osImage":"osImage"}],"volumes":[{"sizeGb":1,"protocol":"PROTOCOL_UNSPECIFIED","lunRanges":[{"sizeGb":6,"quantity":0},{"sizeGb":6,"quantity":0}],"userNote":"userNote","machineIds":["machineIds","machineIds"],"snapshotsEnabled":True,"location":"location","id":"id","type":"TYPE_UNSPECIFIED","nfsExports":[{"machineId":"machineId","noRootSquash":True,"permissions":"PERMISSIONS_UNSPECIFIED","allowSuid":True,"cidr":"cidr","networkId":"networkId","allowDev":True},{"machineId":"machineId","noRootSquash":True,"permissions":"PERMISSIONS_UNSPECIFIED","allowSuid":True,"cidr":"cidr","networkId":"networkId","allowDev":True}]},{"sizeGb":1,"protocol":"PROTOCOL_UNSPECIFIED","lunRanges":[{"sizeGb":6,"quantity":0},{"sizeGb":6,"quantity":0}],"userNote":"userNote","machineIds":["machineIds","machineIds"],"snapshotsEnabled":True,"location":"location","id":"id","type":"TYPE_UNSPECIFIED","nfsExports":[{"machineId":"machineId","noRootSquash":True,"permissions":"PERMISSIONS_UNSPECIFIED","allowSuid":True,"cidr":"cidr","networkId":"networkId","allowDev":True},{"machineId":"machineId","noRootSquash":True,"permissions":"PERMISSIONS_UNSPECIFIED","allowSuid":True,"cidr":"cidr","networkId":"networkId","allowDev":True}]}],"networks":[{"vlanAttachments":[{"id":"id","pairingKey":"pairingKey"},{"id":"id","pairingKey":"pairingKey"}],"bandwidth":"BANDWIDTH_UNSPECIFIED","userNote":"userNote","cidr":"cidr","location":"location","id":"id","type":"TYPE_UNSPECIFIED","serviceCidr":"SERVICE_CIDR_UNSPECIFIED"},{"vlanAttachments":[{"id":"id","pairingKey":"pairingKey"},{"id":"id","pairingKey":"pairingKey"}],"bandwidth":"BANDWIDTH_UNSPECIFIED","userNote":"userNote","cidr":"cidr","location":"location","id":"id","type":"TYPE_UNSPECIFIED","serviceCidr":"SERVICE_CIDR_UNSPECIFIED"}],"ticketId":"ticketId"},"email":"email"}
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
        path='/v1alpha1/{project}/{locationsubmit_provisioning_confi}'.format(project='project_example', location='location_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baremetalsolution_projects_provisioning_quotas_list(client):
    """Test case for baremetalsolution_projects_provisioning_quotas_list

    
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
        path='/v1alpha1/{parent}/provisioningQuotas'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

