# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.transaction_categorization_rule import TransactionCategorizationRule
from openapi_server.models.transaction_categorization_rule_request import TransactionCategorizationRuleRequest
from openapi_server.models.transaction_categorization_rule_response import TransactionCategorizationRuleResponse
from openapi_server.models.transaction_category_request import TransactionCategoryRequest
from openapi_server.models.transaction_category_response import TransactionCategoryResponse
from openapi_server.models.transaction_count_response import TransactionCountResponse
from openapi_server.models.transaction_request import TransactionRequest
from openapi_server.models.transaction_response import TransactionResponse
from openapi_server.models.update_category_request import UpdateCategoryRequest
from openapi_server.models.yodlee_error import YodleeError


pytestmark = pytest.mark.asyncio

async def test_create_or_run_transaction_categorization_rules(client):
    """Test case for create_or_run_transaction_categorization_rules

    Create or Run Transaction Categorization Rule
    """
    params = [('action', 'action_example'),
                    ('ruleParam', 'rule_param_example')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='POST',
        path='/transactions/categories/rules',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_transaction_category(client):
    """Test case for create_transaction_category

    Create Category
    """
    body = {"parentCategoryId":1,"source":"source","categoryName":"categoryName"}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/transactions/categories',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_transaction_categorization_rule(client):
    """Test case for delete_transaction_categorization_rule

    Delete Transaction Categorization Rule
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='DELETE',
        path='/transactions/categories/rules/{rule_id}'.format(rule_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_transaction_category(client):
    """Test case for delete_transaction_category

    Delete Category
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='DELETE',
        path='/transactions/categories/{category_id}'.format(category_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transaction_categories(client):
    """Test case for get_transaction_categories

    Get Transaction Category List
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/transactions/categories',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transaction_categorization_rules(client):
    """Test case for get_transaction_categorization_rules

    Get Transaction Categorization Rules
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/transactions/categories/txnRules',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transaction_categorization_rules_deprecated(client):
    """Test case for get_transaction_categorization_rules_deprecated

    Get Transaction Categorization Rules
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/transactions/categories/rules',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transactions(client):
    """Test case for get_transactions

    Get Transactions
    """
    params = [('accountId', 'account_id_example'),
                    ('baseType', 'base_type_example'),
                    ('categoryId', 'category_id_example'),
                    ('categoryType', 'category_type_example'),
                    ('container', 'container_example'),
                    ('detailCategoryId', 'detail_category_id_example'),
                    ('fromDate', 'from_date_example'),
                    ('highLevelCategoryId', 'high_level_category_id_example'),
                    ('keyword', 'keyword_example'),
                    ('skip', 56),
                    ('toDate', 'to_date_example'),
                    ('top', 56),
                    ('type', 'type_example')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/transactions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transactions_count(client):
    """Test case for get_transactions_count

    Get Transactions Count
    """
    params = [('accountId', 'account_id_example'),
                    ('baseType', 'base_type_example'),
                    ('categoryId', 'category_id_example'),
                    ('categoryType', 'category_type_example'),
                    ('container', 'container_example'),
                    ('detailCategoryId', 'detail_category_id_example'),
                    ('fromDate', 'from_date_example'),
                    ('highLevelCategoryId', 'high_level_category_id_example'),
                    ('keyword', 'keyword_example'),
                    ('toDate', 'to_date_example'),
                    ('type', 'type_example')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/transactions/count',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_transaction_categorization_rule(client):
    """Test case for run_transaction_categorization_rule

    Run Transaction Categorization Rule
    """
    params = [('action', run)]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='POST',
        path='/transactions/categories/rules/{rule_id}'.format(rule_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_transaction(client):
    """Test case for update_transaction

    Update Transaction
    """
    body = {"transaction":{"categorySource":"SYSTEM","container":"bank","description":{"security":"security","original":"original","simple":"simple","consumer":"consumer"},"memo":"memo","categoryId":0}}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/transactions/{transaction_id}'.format(transaction_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_transaction_categorization_rule(client):
    """Test case for update_transaction_categorization_rule

    Update Transaction Categorization Rule
    """
    body = {"rule":{"ruleClause":[{"field":"amount","operation":"numberEquals","value":"{}"},{"field":"amount","operation":"numberEquals","value":"{}"}],"source":"SYSTEM","priority":6,"categoryId":0}}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/transactions/categories/rules/{rule_id}'.format(rule_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_transaction_category(client):
    """Test case for update_transaction_category

    Update Category
    """
    body = {"highLevelCategoryName":"highLevelCategoryName","id":1,"source":"SYSTEM","categoryName":"categoryName"}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/transactions/categories',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

