# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.fetch_email_histories_response import FetchEmailHistoriesResponse
from openapi_server.models.fetch_email_history_response import FetchEmailHistoryResponse
from openapi_server.models.fetch_error_response import FetchErrorResponse


pytestmark = pytest.mark.asyncio

async def test_fetch_email_histories(client):
    """Test case for fetch_email_histories

    List email histories
    """
    params = [('filter[receiver]', 'filter_receiver_example'),
                    ('filter[sender]', 'filter_sender_example'),
                    ('filter[emailType]', 'filter_email_type_example'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/email_history',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_email_history(client):
    """Test case for fetch_email_history

    Get an email history
    """
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/email_history/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

