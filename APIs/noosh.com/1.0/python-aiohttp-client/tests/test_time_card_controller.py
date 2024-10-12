# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.time_card_detail_vo import TimeCardDetailVO
from openapi_server.models.time_card_list_vo import TimeCardListVO
from openapi_server.models.time_card_received_detail_vo import TimeCardReceivedDetailVO


pytestmark = pytest.mark.asyncio

async def test_get_my_time_card(client):
    """Test case for get_my_time_card

    Get a specific my time cards
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/myTimeCards/{time_card_id}'.format(workgroup_id='workgroup_id_example', time_card_id='time_card_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_my_time_card_list(client):
    """Test case for get_my_time_card_list

    List my time cards
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/myTimeCards'.format(workgroup_id='workgroup_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_received_time_card(client):
    """Test case for get_received_time_card

    List a specific received time cards
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/receivedTimeCards/{time_card_id}'.format(workgroup_id='workgroup_id_example', time_card_id='time_card_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_received_time_card_list(client):
    """Test case for get_received_time_card_list

    List received time cards
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/receivedTimeCards'.format(workgroup_id='workgroup_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

