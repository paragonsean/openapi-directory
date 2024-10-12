# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dependent_hosted_number_order_enum_status import DependentHostedNumberOrderEnumStatus
from openapi_server.models.list_dependent_hosted_number_order_response import ListDependentHostedNumberOrderResponse


pytestmark = pytest.mark.asyncio

async def test_list_dependent_hosted_number_order(client):
    """Test case for list_dependent_hosted_number_order

    
    """
    params = [('Status', openapi_server.DependentHostedNumberOrderEnumStatus()),
                    ('PhoneNumber', 'phone_number_example'),
                    ('IncomingPhoneNumberSid', 'incoming_phone_number_sid_example'),
                    ('FriendlyName', 'friendly_name_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/HostedNumber/AuthorizationDocuments/{signing_document_sid}/DependentHostedNumberOrders'.format(signing_document_sid='signing_document_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

