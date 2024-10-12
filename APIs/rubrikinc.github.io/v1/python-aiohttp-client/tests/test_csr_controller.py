# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.csr_summary import CsrSummary
from openapi_server.models.csr_summary_list_response import CsrSummaryListResponse
from openapi_server.models.generic_csr_request import GenericCsrRequest


pytestmark = pytest.mark.asyncio

async def test_delete_csr(client):
    """Test case for delete_csr

    Delete a certificate signing request
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/csr/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_generate_csr(client):
    """Test case for generate_csr

    Generate a new private key and return a certificate signing request
    """
    body = {"name":"name","csrRequest":{"country":"country","uid":"uid","emailAddress":"emailAddress","city":"city","surname":"surname","organization":"organization","hostnames":["hostnames","hostnames"],"organizationUnit":"organizationUnit","state":"state"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/csr',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_csrs(client):
    """Test case for get_all_csrs

    Get all certificate signing requests
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/csr',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

