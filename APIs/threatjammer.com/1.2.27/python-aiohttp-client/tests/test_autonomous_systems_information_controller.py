# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.autonomous_system_output import AutonomousSystemOutput
from openapi_server.models.autonomous_system_prefix_output import AutonomousSystemPrefixOutput
from openapi_server.models.autonomous_system_prefixes_output import AutonomousSystemPrefixesOutput
from openapi_server.models.autonomous_system_registry_output import AutonomousSystemRegistryOutput
from openapi_server.models.autonomous_system_status_output import AutonomousSystemStatusOutput
from openapi_server.models.body_query_asn_prefix_information_v1_asn_prefix_post import BodyQueryAsnPrefixInformationV1AsnPrefixPost
from openapi_server.models.http_validation_error import HTTPValidationError


pytestmark = pytest.mark.asyncio

async def test_query_asn_prefix_information_v1_asn_prefix_post(client):
    """Test case for query_asn_prefix_information_v1_asn_prefix_post

    Get the IPv4 or IPv6 prefix of the CIDR given.
    """
    body = openapi_server.BodyQueryAsnPrefixInformationV1AsnPrefixPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/asn/prefix',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_asn_prefixes_list_v1_asn_number_prefixes_get(client):
    """Test case for query_asn_prefixes_list_v1_asn_number_prefixes_get

    Get the list of IPv4 and IPv6 prefixes of the AS number given.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/asn/{number}/prefixes'.format(number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_asn_v1_asn_number_get(client):
    """Test case for query_asn_v1_asn_number_get

    Get the Autonomous System details of the AS number given.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/asn/{number}'.format(number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_ip_address_network_information_v1_asn_ip_ip_address_get(client):
    """Test case for query_ip_address_network_information_v1_asn_ip_ip_address_get

    Get the IPv4 or IPv6 prefix of the IP address given.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/asn/ip/{ip_address}'.format(ip_address='ip_address_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_registry_by_the_name_v1_asn_registry_code_get(client):
    """Test case for query_registry_by_the_name_v1_asn_registry_code_get

    Get the information of a Regional Internet Registries (RIRs) given.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/asn/registry/{code}'.format(code='code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_registry_names_v1_asn_registry_all_get(client):
    """Test case for query_registry_names_v1_asn_registry_all_get

    Get the list of the Regional Internet Registries (RIRs) entities worldwide.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/asn/registry/all',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_status_by_the_name_v1_asn_status_code_get(client):
    """Test case for query_status_by_the_name_v1_asn_status_code_get

    Get the information of a status given.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/asn/status/{code}'.format(code='code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_status_names_v1_asn_status_all_get(client):
    """Test case for query_status_names_v1_asn_status_all_get

    Get the list of status of an object in a registry.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/asn/status/all',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

