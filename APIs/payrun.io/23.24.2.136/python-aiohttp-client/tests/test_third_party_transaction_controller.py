# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link_collection import LinkCollection
from openapi_server.models.tag import Tag


pytestmark = pytest.mark.asyncio

async def test_delete_third_party_transaction_tag_0(client):
    """Test case for delete_third_party_transaction_tag_0

    Delete third party transaction tag
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/ThirdPartyTransaction/{third_party_transaction_id}/Tag/{tag_id}'.format(employer_id='employer_id_example', third_party_transaction_id='third_party_transaction_id_example', tag_id='tag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_third_party_transaction_tags_0(client):
    """Test case for get_all_third_party_transaction_tags_0

    Get all third party transaction tags
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/ThirdPartyTransactions/Tags'.format(employer_id='employer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_third_party_transactions_with_tag_0(client):
    """Test case for get_all_third_party_transactions_with_tag_0

    Get links to tagged third party transactions
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/ThirdPartyTransactions/Tag/{tag_id}'.format(employer_id='employer_id_example', tag_id='tag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tag_from_third_party_transaction_0(client):
    """Test case for get_tag_from_third_party_transaction_0

    Get third party transaction tag
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/ThirdPartyTransaction/{third_party_transaction_id}/Tag/{tag_id}'.format(employer_id='employer_id_example', third_party_transaction_id='third_party_transaction_id_example', tag_id='tag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tags_from_third_party_transaction_0(client):
    """Test case for get_tags_from_third_party_transaction_0

    Get tags from third party transaction
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/ThirdPartyTransaction/{third_party_transaction_id}/Tags'.format(employer_id='employer_id_example', third_party_transaction_id='third_party_transaction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_third_party_transaction_tag_0(client):
    """Test case for put_third_party_transaction_tag_0

    insert third party transaction tag
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='PUT',
        path='/Employer/{employer_id}/ThirdPartyTransaction/{third_party_transaction_id}/Tag/{tag_id}'.format(employer_id='employer_id_example', third_party_transaction_id='third_party_transaction_id_example', tag_id='tag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

