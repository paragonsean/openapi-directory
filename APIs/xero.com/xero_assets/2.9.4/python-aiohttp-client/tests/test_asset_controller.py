# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.asset import Asset
from openapi_server.models.asset_status_query_param import AssetStatusQueryParam
from openapi_server.models.asset_type import AssetType
from openapi_server.models.assets import Assets
from openapi_server.models.setting import Setting


pytestmark = pytest.mark.asyncio

async def test_create_asset(client):
    """Test case for create_asset

    adds a fixed asset
    """
    body = {"purchaseDate":"2000-01-23","serialNumber":"ca4c6b39-4f4f-43e8-98da-5e1f350a6694","assetTypeId":"3b5b3a38-5649-495f-87a1-14a4e5918634","purchasePrice":1000.0,"isDeleteEnabledForDate":True,"assetNumber":"FA-0013","bookDepreciationSetting":{"depreciableObjectId":"68f17094-af97-4f1b-b36b-013b45b6ad3c","averagingMethod":"ActualDays","effectiveLifeYears":5,"depreciationMethod":"StraightLine","depreciableObjectType":"Asset","bookEffectiveDateOfChangeId":"68f17094-af97-4f1b-b36b-013b45b6ad3c","depreciationCalculationMethod":"None","depreciationRate":0.05},"warrantyExpiryDate":"ca4c6b39-4f4f-43e8-98da-5e1f350a6694","accountingBookValue":0,"assetId":"3b5b3a38-5649-495f-87a1-14a4e5918634","canRollback":True,"disposalDate":"2000-01-23","assetName":"Awesome Truck 3","disposalPrice":1.0,"assetStatus":"Draft","bookDepreciationDetail":{"currentCapitalGain":5.25,"costLimit":9000,"depreciationStartDate":"2000-01-23","priorAccumDepreciationAmount":0.45,"currentAccumDepreciationAmount":5,"currentGainLoss":10.5,"residualValue":10000}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'xero_tenant_id': 'YOUR_XERO_TENANT_ID',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/assets.xro/1.0/Assets',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_asset_type(client):
    """Test case for create_asset_type

    adds a fixed asset type
    """
    body = {"assetTypeId":"5da209c5-5e19-4a43-b925-71b776c49ced","bookDepreciationSetting":{"depreciableObjectId":"68f17094-af97-4f1b-b36b-013b45b6ad3c","averagingMethod":"ActualDays","effectiveLifeYears":5,"depreciationMethod":"StraightLine","depreciableObjectType":"Asset","bookEffectiveDateOfChangeId":"68f17094-af97-4f1b-b36b-013b45b6ad3c","depreciationCalculationMethod":"None","depreciationRate":0.05},"assetTypeName":"Computer Equipment","depreciationExpenseAccountId":"b23fc79b-d66b-44b0-a240-e138e086fcbc","accumulatedDepreciationAccountId":"ca4c6b39-4f4f-43e8-98da-5e1f350a6694","fixedAssetAccountId":"24e260f1-bfc4-4766-ad7f-8a8ce01de879","locks":33}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'xero_tenant_id': 'YOUR_XERO_TENANT_ID',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/assets.xro/1.0/AssetTypes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_asset_by_id(client):
    """Test case for get_asset_by_id

    Retrieves fixed asset by id
    """
    headers = { 
        'Accept': 'application/json',
        'xero_tenant_id': 'YOUR_XERO_TENANT_ID',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/assets.xro/1.0/Assets/{id}'.format(id='4f7bcdcb-5ec1-4258-9558-19f662fccdfe'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_asset_settings(client):
    """Test case for get_asset_settings

    searches fixed asset settings
    """
    headers = { 
        'Accept': 'application/json',
        'xero_tenant_id': 'YOUR_XERO_TENANT_ID',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/assets.xro/1.0/Settings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_asset_types(client):
    """Test case for get_asset_types

    searches fixed asset types
    """
    headers = { 
        'Accept': 'application/json',
        'xero_tenant_id': 'YOUR_XERO_TENANT_ID',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/assets.xro/1.0/AssetTypes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_assets(client):
    """Test case for get_assets

    searches fixed asset
    """
    params = [('status', openapi_server.AssetStatusQueryParam()),
                    ('page', 1),
                    ('pageSize', 5),
                    ('orderBy', 'AssetName'),
                    ('sortDirection', 'ASC'),
                    ('filterBy', 'Company Car')]
    headers = { 
        'Accept': 'application/json',
        'xero_tenant_id': 'YOUR_XERO_TENANT_ID',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/assets.xro/1.0/Assets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

