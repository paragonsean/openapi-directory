# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.ip_log_collection_output import IPLogCollectionOutput
from openapi_server.models.ip_log_output import IPLogOutput


pytestmark = pytest.mark.asyncio

async def test_log_change_id_v1_log_ip_id_logchange_id_get(client):
    """Test case for log_change_id_v1_log_ip_id_logchange_id_get

    Get a log event.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/log/ip/id/{logchange_id}'.format(logchange_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logchanges_ip_v1_log_ip_ip_address_get(client):
    """Test case for logchanges_ip_v1_log_ip_ip_address_get

    Get the changes logged in the different datasets of an IP address.
    """
    params = [('dataset', 'dataset_example'),
                    ('logged_after', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/log/ip/{ip_address}'.format(ip_address='ip_address_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

