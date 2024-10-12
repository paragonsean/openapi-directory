# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.match_request import MatchRequest


pytestmark = pytest.mark.asyncio

async def test_match(client):
    """Test case for match

    Match Received SKUs individually
    """
    body = {"matchType":"itemMatch","matcherId":"{{matcherid}}","product":{"brandId":1234567,"categoryId":12,"description":"Descricao exemplo","name":"Produto exemplo","specifications":null},"productRef":"{{productRef}}(should be specified when match is a product match)","score":"{{score}} (must be decimal)","sku":{"eans":["12345678901213"],"height":1,"images":[{"imagem1.jpg":"imageurl.example"}],"length":1,"measurementUnit":"un","name":"Sku exemplo","refId":null,"specifications":{"Embalagem":"3 kg"},"unitMultiplier":1,"weight":1,"width":1},"skuRef":"{{skuid}}(should be specifed when match is a sku match)"}
    params = [('accountName', 'apiexamples')]
    headers = { 
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/suggestions/{seller_id}/{sellerskuid}/versions/{version}/matches/{matchid}'.format(seller_id='seller123', sellerskuid='1234', version='09072021142808277', matchid='matchid_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_match_multiple(client):
    """Test case for match_multiple

    Match Multiple Received SKUs
    """
    body = None
    params = [('accountName', 'apiexamples')]
    headers = { 
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/suggestions/matches/action/{action_name}'.format(action_name='newprodcut'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

