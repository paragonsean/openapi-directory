# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.inbound_message_full_details_response import InboundMessageFullDetailsResponse
from openapi_server.models.inbound_search_response import InboundSearchResponse
from openapi_server.models.message_click_search_response import MessageClickSearchResponse
from openapi_server.models.message_open_search_response import MessageOpenSearchResponse
from openapi_server.models.outbound_message_details_response import OutboundMessageDetailsResponse
from openapi_server.models.outbound_message_dump_response import OutboundMessageDumpResponse
from openapi_server.models.outbound_search_response import OutboundSearchResponse
from openapi_server.models.standard_postmark_response import StandardPostmarkResponse


pytestmark = pytest.mark.asyncio

async def test_bypass_rules_for_inbound_message(client):
    """Test case for bypass_rules_for_inbound_message

    Bypass rules for a blocked inbound message
    """
    headers = { 
        'Accept': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='PUT',
        path='/messages/inbound/{messageid}/bypass'.format(messageid='messageid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_clicks_for_single_outbound_message(client):
    """Test case for get_clicks_for_single_outbound_message

    Retrieve Message Clicks
    """
    params = [('count', 1),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='GET',
        path='/messages/outbound/clicks/{messageid}'.format(messageid='messageid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_inbound_message_details(client):
    """Test case for get_inbound_message_details

    Inbound message details
    """
    headers = { 
        'Accept': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='GET',
        path='/messages/inbound/{messageid}/details'.format(messageid='messageid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_opens_for_single_outbound_message(client):
    """Test case for get_opens_for_single_outbound_message

    Retrieve Message Opens
    """
    params = [('count', 1),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='GET',
        path='/messages/outbound/opens/{messageid}'.format(messageid='messageid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_outbound_message_details(client):
    """Test case for get_outbound_message_details

    Outbound message details
    """
    headers = { 
        'Accept': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='GET',
        path='/messages/outbound/{messageid}/details'.format(messageid='messageid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_outbound_message_dump(client):
    """Test case for get_outbound_message_dump

    Outbound message dump
    """
    headers = { 
        'Accept': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='GET',
        path='/messages/outbound/{messageid}/dump'.format(messageid='messageid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retry_inbound_message_processing(client):
    """Test case for retry_inbound_message_processing

    Retry a failed inbound message for processing
    """
    headers = { 
        'Accept': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='PUT',
        path='/messages/inbound/{messageid}/retry'.format(messageid='messageid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_clicks_for_outbound_messages(client):
    """Test case for search_clicks_for_outbound_messages

    Clicks for a all messages
    """
    params = [('count', 56),
                    ('offset', 56),
                    ('recipient', 'recipient_example'),
                    ('tag', 'tag_example'),
                    ('client_name', 'client_name_example'),
                    ('client_company', 'client_company_example'),
                    ('client_family', 'client_family_example'),
                    ('os_name', 'os_name_example'),
                    ('os_family', 'os_family_example'),
                    ('os_company', 'os_company_example'),
                    ('platform', 'platform_example'),
                    ('country', 'country_example'),
                    ('region', 'region_example'),
                    ('city', 'city_example')]
    headers = { 
        'Accept': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='GET',
        path='/messages/outbound/clicks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_inbound_messages(client):
    """Test case for search_inbound_messages

    Inbound message search
    """
    params = [('count', 56),
                    ('offset', 56),
                    ('recipient', 'recipient_example'),
                    ('fromemail', 'fromemail_example'),
                    ('subject', 'subject_example'),
                    ('mailboxhash', 'mailboxhash_example'),
                    ('tag', 'tag_example'),
                    ('status', 'status_example'),
                    ('todate', '2013-10-20'),
                    ('fromdate', '2013-10-20')]
    headers = { 
        'Accept': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='GET',
        path='/messages/inbound',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_opens_for_outbound_messages(client):
    """Test case for search_opens_for_outbound_messages

    Opens for all messages
    """
    params = [('count', 56),
                    ('offset', 56),
                    ('recipient', 'recipient_example'),
                    ('tag', 'tag_example'),
                    ('client_name', 'client_name_example'),
                    ('client_company', 'client_company_example'),
                    ('client_family', 'client_family_example'),
                    ('os_name', 'os_name_example'),
                    ('os_family', 'os_family_example'),
                    ('os_company', 'os_company_example'),
                    ('platform', 'platform_example'),
                    ('country', 'country_example'),
                    ('region', 'region_example'),
                    ('city', 'city_example')]
    headers = { 
        'Accept': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='GET',
        path='/messages/outbound/opens',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_outbound_messages(client):
    """Test case for search_outbound_messages

    Outbound message search
    """
    params = [('count', 56),
                    ('offset', 56),
                    ('recipient', 'recipient_example'),
                    ('fromemail', 'fromemail_example'),
                    ('tag', 'tag_example'),
                    ('status', 'status_example'),
                    ('todate', '2013-10-20'),
                    ('fromdate', '2013-10-20')]
    headers = { 
        'Accept': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='GET',
        path='/messages/outbound',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

