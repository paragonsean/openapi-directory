# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.getaccountconfig200_response import Getaccountconfig200Response
from openapi_server.models.getauto_approvevaluefromconfig200_response import GetautoApprovevaluefromconfig200Response
from openapi_server.models.putselleraccountconfig_request import PutselleraccountconfigRequest
from openapi_server.models.saveaccountconfig200_response import Saveaccountconfig200Response
from openapi_server.models.saveaccountconfig_request import SaveaccountconfigRequest
from openapi_server.models.saveautoapproveforaccount200_response import Saveautoapproveforaccount200Response
from openapi_server.models.saveautoapproveforaccount_request import SaveautoapproveforaccountRequest
from openapi_server.models.saveautoapproveforaccountseller_request import SaveautoapproveforaccountsellerRequest


pytestmark = pytest.mark.asyncio

async def test_getaccountconfig(client):
    """Test case for getaccountconfig

    Get Account's Approval Settings
    """
    params = [('accountName', 'apiexamples')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/suggestions/configuration',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getauto_approvevaluefromconfig(client):
    """Test case for getauto_approvevaluefromconfig

    Get autoApprove Status in Account Settings
    """
    params = [('sellerId', 'seller123'),
                    ('accountName', 'apiexamples')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/suggestions/configuration/autoapproval/toggle',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getselleraccountconfig(client):
    """Test case for getselleraccountconfig

    Get Seller's Approval Settings
    """
    params = [('accountName', 'apiexamples')]
    headers = { 
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/suggestions/configuration/seller/{seller_id}'.format(seller_id='seller123'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_putselleraccountconfig(client):
    """Test case for putselleraccountconfig

    Save Seller's Approval Settings
    """
    body = {"mapping":"{}","sellerId":"seller123","matchFlux":"autoApprove"}
    params = [('accountName', 'apiexamples')]
    headers = { 
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/suggestions/configuration/seller/{seller_id}'.format(seller_id='seller123'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_saveaccountconfig(client):
    """Test case for saveaccountconfig

    Save Account's Approval Settings
    """
    body = {"MatchFlux":"AutoApprove","Matchers":[{"Description":null,"IsActive":True,"MatcherId":"vtex-matcher","UpdatesNotificationEndpoint":null,"hook-base-address":"http://simple-suggestion-matcher.vtex.com.br"}],"Score":{"Approve":80,"Reject":30},"SpecificationsMapping":[]}
    params = [('accountName', 'apiexamples')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/suggestions/configuration',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_saveautoapproveforaccount(client):
    """Test case for saveautoapproveforaccount

    Activate autoApprove in Marketplace's Account
    """
    body = {"Enabled":True}
    params = [('accountName', 'apiexamples')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/suggestions/configuration/autoapproval/toggle',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_saveautoapproveforaccountseller(client):
    """Test case for saveautoapproveforaccountseller

    Activate autoApprove Setting for a Seller
    """
    body = {"Enabled":True}
    params = [('accountName', 'apiexamples')]
    headers = { 
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/suggestions/configuration/autoapproval/toggle/seller/{seller_id}'.format(seller_id='seller123'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

