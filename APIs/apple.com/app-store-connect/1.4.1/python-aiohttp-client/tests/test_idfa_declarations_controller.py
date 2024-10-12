# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.idfa_declaration_create_request import IdfaDeclarationCreateRequest
from openapi_server.models.idfa_declaration_response import IdfaDeclarationResponse
from openapi_server.models.idfa_declaration_update_request import IdfaDeclarationUpdateRequest


pytestmark = pytest.mark.asyncio

async def test_idfa_declarations_create_instance(client):
    """Test case for idfa_declarations_create_instance

    
    """
    body = {"data":{"relationships":{"appStoreVersion":{"data":{"id":"id","type":"appStoreVersions"}}},"attributes":{"attributesAppInstallationToPreviousAd":True,"attributesActionWithPreviousAd":True,"servesAds":True,"honorsLimitedAdTracking":True},"type":"idfaDeclarations"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/idfaDeclarations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_idfa_declarations_delete_instance(client):
    """Test case for idfa_declarations_delete_instance

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/idfaDeclarations/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_idfa_declarations_update_instance(client):
    """Test case for idfa_declarations_update_instance

    
    """
    body = {"data":{"attributes":{"attributesAppInstallationToPreviousAd":True,"attributesActionWithPreviousAd":True,"servesAds":True,"honorsLimitedAdTracking":True},"id":"id","type":"idfaDeclarations"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/idfaDeclarations/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

