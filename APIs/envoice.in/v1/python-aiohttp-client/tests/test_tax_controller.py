# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.tax_create_api_model import TaxCreateApiModel
from openapi_server.models.tax_delete_api_model import TaxDeleteApiModel
from openapi_server.models.tax_details_api_model import TaxDetailsApiModel
from openapi_server.models.tax_update_api_model import TaxUpdateApiModel


pytestmark = pytest.mark.asyncio

async def test_tax_api_all(client):
    """Test case for tax_api_all

    Return all taxes for the account
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='GET',
        path='/api/tax/all',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_tax_api_delete(client):
    """Test case for tax_api_delete

    Delete an existing tax
    """
    body = {"Id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='POST',
        path='/api/tax/delete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_tax_api_new(client):
    """Test case for tax_api_new

    Create a tax
    """
    body = {"Percentage":0.8008281904610115,"Name":"Name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='POST',
        path='/api/tax/new',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_tax_api_update(client):
    """Test case for tax_api_update

    Update an existing tax
    """
    body = {"Percentage":6.027456183070403,"Id":0,"Name":"Name"}
    headers = { 
        'Content-Type': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='POST',
        path='/api/tax/update',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

