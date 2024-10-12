# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.delete_address import DeleteAddress
from openapi_server.models.delete_address_request import DeleteAddressRequest
from openapi_server.models.export_address import ExportAddress
from openapi_server.models.export_address_request import ExportAddressRequest
from openapi_server.models.import_address import ImportAddress
from openapi_server.models.import_address_request import ImportAddressRequest
from openapi_server.models.list_addresses import ListAddresses
from openapi_server.models.new_address import NewAddress
from openapi_server.models.new_address_request import NewAddressRequest


pytestmark = pytest.mark.asyncio

async def test_delete_address(client):
    """Test case for delete_address

    deleteAddress
    """
    body = {"ethereumaddress":"0x71892689ed0d79d88ab6ea3783b571b8ece9bee3","password":"padN39QkRA2hJ"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m',
    }
    response = await client.request(
        method='POST',
        path='/v1/deleteAddress',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_address(client):
    """Test case for export_address

    exportAddress
    """
    body = {"ethaddress":"0x71892889ed4d79d88ab6ea3783b571b8ece9bef4","password":"padN39QkRA2hJ"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m',
    }
    response = await client.request(
        method='POST',
        path='/v1/exportAddress',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_import_address(client):
    """Test case for import_address

    importAddress
    """
    body = {"content":{"address":"71892889ed4d79d88ab6ea3783b571b8ece9bef4","crypto":{"cipher":"aes-128-ctr","cipherparams":{"iv":"76e6f2497b9f2a8e024fc752a5418a6d"},"ciphertext":"9d74262517b984f9b0560b8f23b5e3340f7be0f56b70cd91ff445dcaf5b1968f","kdf":"scrypt","kdfparams":{"dklen":32,"n":131072,"p":1,"r":8,"salt":"d11d996a7cc4bfad730d4c9b9057eff2c0fb3940b5bfc59db62ae218c14a54f4"},"mac":"dcc342bbbbb8eea97c89b47bafc23de568fc1a48e0bd21ae8d776a95c4704ac9"},"id":"85b790ff-408e-42b8-b123-bec9523964dc","version":3},"filename":"UTC--2020-09-19T10-42-26.196Z--71892889ed4d79d88ab6ea3783b571b8ece9bef4","password":"padN39QkRA2hJ"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m',
    }
    response = await client.request(
        method='POST',
        path='/v1/importAddress',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_addresses(client):
    """Test case for list_addresses

    listAddresses
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'authorization': 'q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m',
    }
    response = await client.request(
        method='POST',
        path='/v1/listAddresses',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_new_address(client):
    """Test case for new_address

    newAddress
    """
    body = {"password":"padN39QkRA2hJ"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m',
    }
    response = await client.request(
        method='POST',
        path='/v1/newAddress',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

