# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.business_line import BusinessLine
from openapi_server.models.business_line_info import BusinessLineInfo
from openapi_server.models.service_error import ServiceError


pytestmark = pytest.mark.asyncio

async def test_delete_business_lines_id(client):
    """Test case for delete_business_lines_id

    Delete a business line
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/lem/v1/businessLines/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_business_lines_id(client):
    """Test case for get_business_lines_id

    Get a business line
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/lem/v1/businessLines/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_business_lines(client):
    """Test case for post_business_lines

    Create a business line
    """
    body = {"salesChannels":["salesChannels","salesChannels"],"capability":"receivePayments","legalEntityId":"legalEntityId","webDataExemption":{"reason":"noOnlinePresence"},"sourceOfFunds":{"description":"description","adyenProcessedFunds":True,"type":"business","acquiringBusinessLineId":"acquiringBusinessLineId"},"webData":[{"webAddressId":"webAddressId","webAddress":"webAddress"},{"webAddressId":"webAddressId","webAddress":"webAddress"}],"industryCode":"industryCode"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/lem/v1/businessLines',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

