# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.holding_asset_classification_list_response import HoldingAssetClassificationListResponse
from openapi_server.models.holding_response import HoldingResponse
from openapi_server.models.holding_securities_response import HoldingSecuritiesResponse
from openapi_server.models.holding_type_list_response import HoldingTypeListResponse
from openapi_server.models.yodlee_error import YodleeError


pytestmark = pytest.mark.asyncio

async def test_get_asset_classification_list(client):
    """Test case for get_asset_classification_list

    Get Asset Classification List
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/holdings/assetClassificationList',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_holding_type_list(client):
    """Test case for get_holding_type_list

    Get Holding Type List
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/holdings/holdingTypeList',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_holdings(client):
    """Test case for get_holdings

    Get Holdings
    """
    params = [('accountId', 'account_id_example'),
                    ('assetClassification.classificationType', 'asset_classification_classification_type_example'),
                    ('classificationValue', 'classification_value_example'),
                    ('include', 'include_example'),
                    ('providerAccountId', 'provider_account_id_example')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/holdings',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_securities(client):
    """Test case for get_securities

    Get Security Details
    """
    params = [('holdingId', 'holding_id_example')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/holdings/securities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

