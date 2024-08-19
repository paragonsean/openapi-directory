# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.body_query_datacenter_prefix_information_v1_datacenter_prefix_post import BodyQueryDatacenterPrefixInformationV1DatacenterPrefixPost
from openapi_server.models.datacenter_output import DatacenterOutput
from openapi_server.models.datacenter_prefix_output import DatacenterPrefixOutput
from openapi_server.models.datacenter_prefixes_output import DatacenterPrefixesOutput
from openapi_server.models.http_validation_error import HTTPValidationError


pytestmark = pytest.mark.asyncio

async def test_query_datacenter_prefix_information_v1_datacenter_prefix_post(client):
    """Test case for query_datacenter_prefix_information_v1_datacenter_prefix_post

    Get the IPv4 or IPv6 prefix of the CIDR given.
    """
    body = openapi_server.BodyQueryDatacenterPrefixInformationV1DatacenterPrefixPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/datacenter/prefix',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_datacenter_prefixes_list_v1_datacenter_datacenter_id_prefixes_get(client):
    """Test case for query_datacenter_prefixes_list_v1_datacenter_datacenter_id_prefixes_get

    Get the list of IPv4 and IPv6 prefixes of the Datacenter given.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/datacenter/{datacenter_id}/prefixes'.format(datacenter_id='datacenter_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_datacenter_v1_datacenter_datacenter_id_get(client):
    """Test case for query_datacenter_v1_datacenter_datacenter_id_get

    Get the Datacenter details of datacente given.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/datacenter/{datacenter_id}'.format(datacenter_id='datacenter_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_ip_address_network_information_v1_datacenter_ip_ip_address_get(client):
    """Test case for query_ip_address_network_information_v1_datacenter_ip_ip_address_get

    Get the IPv4 or IPv6 prefix of the IP address given.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/datacenter/ip/{ip_address}'.format(ip_address='ip_address_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

