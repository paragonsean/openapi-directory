# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.derived_holding_summary_response import DerivedHoldingSummaryResponse
from openapi_server.models.derived_networth_response import DerivedNetworthResponse
from openapi_server.models.derived_transaction_summary_response import DerivedTransactionSummaryResponse
from openapi_server.models.yodlee_error import YodleeError


pytestmark = pytest.mark.asyncio

async def test_get_holding_summary(client):
    """Test case for get_holding_summary

    Get Holding Summary
    """
    params = [('accountIds', 'account_ids_example'),
                    ('classificationType', 'classification_type_example'),
                    ('include', 'include_example')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/derived/holdingSummary',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_networth(client):
    """Test case for get_networth

    Get Networth Summary
    """
    params = [('accountIds', 'account_ids_example'),
                    ('container', 'container_example'),
                    ('fromDate', 'from_date_example'),
                    ('include', 'include_example'),
                    ('interval', 'interval_example'),
                    ('skip', 56),
                    ('toDate', 'to_date_example'),
                    ('top', 56)]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/derived/networth',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transaction_summary(client):
    """Test case for get_transaction_summary

    Get Transaction Summary
    """
    params = [('accountId', 'account_id_example'),
                    ('categoryId', 'category_id_example'),
                    ('categoryType', 'category_type_example'),
                    ('fromDate', 'from_date_example'),
                    ('groupBy', 'group_by_example'),
                    ('include', 'include_example'),
                    ('includeUserCategory', True),
                    ('interval', 'interval_example'),
                    ('toDate', 'to_date_example')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/derived/transactionSummary',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

