# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.mapping_job import MappingJob
from openapi_server.models.mapping_job_result import MappingJobResult
from openapi_server.models.mapping_values_key_get200_response import MappingValuesKeyGet200Response


pytestmark = pytest.mark.asyncio

async def test_mapping_post(client):
    """Test case for mapping_post

    
    """
    body = {"idType":"ID_ISIN","coupon":[6.027456183070403,6.027456183070403],"maturity":["2000-01-23","2000-01-23"],"strike":[1.4658129805029452,1.4658129805029452],"idValue":"MappingJob_idValue","exchCode":"exchCode","optionType":"Put","micCode":"micCode","securityType":"securityType","securityType2":"securityType2","includeUnlistedEquities":True,"contractSize":[0.8008281904610115,0.8008281904610115],"currency":"currency","expiration":["2000-01-23","2000-01-23"],"stateCode":"AB","marketSecDes":"marketSecDes"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/mapping',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mapping_values_key_get(client):
    """Test case for mapping_values_key_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/mapping/values/{key}'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

