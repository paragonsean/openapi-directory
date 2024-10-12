# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.pretargeting_config import PretargetingConfig
from openapi_server.models.pretargeting_config_list import PretargetingConfigList


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer_pretargeting_config_delete(client):
    """Test case for adexchangebuyer_pretargeting_config_delete

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/adexchangebuyer/v1.3/pretargetingconfigs/{account_id}/{config_id}'.format(account_id='account_id_example', config_id='config_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer_pretargeting_config_get(client):
    """Test case for adexchangebuyer_pretargeting_config_get

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/adexchangebuyer/v1.3/pretargetingconfigs/{account_id}/{config_id}'.format(account_id='account_id_example', config_id='config_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer_pretargeting_config_insert(client):
    """Test case for adexchangebuyer_pretargeting_config_insert

    
    """
    body = {"configName":"configName","billingId":"billingId","languages":["languages","languages"],"vendorTypes":["vendorTypes","vendorTypes"],"kind":"adexchangebuyer#pretargetingConfig","maximumQps":"maximumQps","userLists":["userLists","userLists"],"mobileCarriers":["mobileCarriers","mobileCarriers"],"placements":[{"type":"type","token":"token"},{"type":"type","token":"token"}],"isActive":True,"excludedPlacements":[{"type":"type","token":"token"},{"type":"type","token":"token"}],"verticals":["verticals","verticals"],"platforms":["platforms","platforms"],"excludedVerticals":["excludedVerticals","excludedVerticals"],"excludedContentLabels":["excludedContentLabels","excludedContentLabels"],"creativeType":["creativeType","creativeType"],"configId":"configId","mobileOperatingSystemVersions":["mobileOperatingSystemVersions","mobileOperatingSystemVersions"],"geoCriteriaIds":["geoCriteriaIds","geoCriteriaIds"],"mobileDevices":["mobileDevices","mobileDevices"],"supportedCreativeAttributes":["supportedCreativeAttributes","supportedCreativeAttributes"],"excludedGeoCriteriaIds":["excludedGeoCriteriaIds","excludedGeoCriteriaIds"],"dimensions":[{"width":"width","height":"height"},{"width":"width","height":"height"}],"excludedUserLists":["excludedUserLists","excludedUserLists"]}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/adexchangebuyer/v1.3/pretargetingconfigs/{account_id}'.format(account_id='account_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer_pretargeting_config_list(client):
    """Test case for adexchangebuyer_pretargeting_config_list

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/adexchangebuyer/v1.3/pretargetingconfigs/{account_id}'.format(account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer_pretargeting_config_patch(client):
    """Test case for adexchangebuyer_pretargeting_config_patch

    
    """
    body = {"configName":"configName","billingId":"billingId","languages":["languages","languages"],"vendorTypes":["vendorTypes","vendorTypes"],"kind":"adexchangebuyer#pretargetingConfig","maximumQps":"maximumQps","userLists":["userLists","userLists"],"mobileCarriers":["mobileCarriers","mobileCarriers"],"placements":[{"type":"type","token":"token"},{"type":"type","token":"token"}],"isActive":True,"excludedPlacements":[{"type":"type","token":"token"},{"type":"type","token":"token"}],"verticals":["verticals","verticals"],"platforms":["platforms","platforms"],"excludedVerticals":["excludedVerticals","excludedVerticals"],"excludedContentLabels":["excludedContentLabels","excludedContentLabels"],"creativeType":["creativeType","creativeType"],"configId":"configId","mobileOperatingSystemVersions":["mobileOperatingSystemVersions","mobileOperatingSystemVersions"],"geoCriteriaIds":["geoCriteriaIds","geoCriteriaIds"],"mobileDevices":["mobileDevices","mobileDevices"],"supportedCreativeAttributes":["supportedCreativeAttributes","supportedCreativeAttributes"],"excludedGeoCriteriaIds":["excludedGeoCriteriaIds","excludedGeoCriteriaIds"],"dimensions":[{"width":"width","height":"height"},{"width":"width","height":"height"}],"excludedUserLists":["excludedUserLists","excludedUserLists"]}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/adexchangebuyer/v1.3/pretargetingconfigs/{account_id}/{config_id}'.format(account_id='account_id_example', config_id='config_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer_pretargeting_config_update(client):
    """Test case for adexchangebuyer_pretargeting_config_update

    
    """
    body = {"configName":"configName","billingId":"billingId","languages":["languages","languages"],"vendorTypes":["vendorTypes","vendorTypes"],"kind":"adexchangebuyer#pretargetingConfig","maximumQps":"maximumQps","userLists":["userLists","userLists"],"mobileCarriers":["mobileCarriers","mobileCarriers"],"placements":[{"type":"type","token":"token"},{"type":"type","token":"token"}],"isActive":True,"excludedPlacements":[{"type":"type","token":"token"},{"type":"type","token":"token"}],"verticals":["verticals","verticals"],"platforms":["platforms","platforms"],"excludedVerticals":["excludedVerticals","excludedVerticals"],"excludedContentLabels":["excludedContentLabels","excludedContentLabels"],"creativeType":["creativeType","creativeType"],"configId":"configId","mobileOperatingSystemVersions":["mobileOperatingSystemVersions","mobileOperatingSystemVersions"],"geoCriteriaIds":["geoCriteriaIds","geoCriteriaIds"],"mobileDevices":["mobileDevices","mobileDevices"],"supportedCreativeAttributes":["supportedCreativeAttributes","supportedCreativeAttributes"],"excludedGeoCriteriaIds":["excludedGeoCriteriaIds","excludedGeoCriteriaIds"],"dimensions":[{"width":"width","height":"height"},{"width":"width","height":"height"}],"excludedUserLists":["excludedUserLists","excludedUserLists"]}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/adexchangebuyer/v1.3/pretargetingconfigs/{account_id}/{config_id}'.format(account_id='account_id_example', config_id='config_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

