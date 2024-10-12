# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_name_availability_input import CheckNameAvailabilityInput
from openapi_server.models.check_name_availability_output import CheckNameAvailabilityOutput
from openapi_server.models.communication_details import CommunicationDetails
from openapi_server.models.communications_list_result import CommunicationsListResult
from openapi_server.models.exception_response import ExceptionResponse


pytestmark = pytest.mark.asyncio

async def test_communications_check_name_availability(client):
    """Test case for communications_check_name_availability

    
    """
    check_name_availability_input = {"name":"name","type":"Microsoft.Support/supportTickets"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Support/supportTickets/{support_ticket_name}/checkNameAvailability'.format(support_ticket_name='support_ticket_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=check_name_availability_input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_communications_create(client):
    """Test case for communications_create

    
    """
    create_communication_parameters = {"name":"name","id":"id","type":"type","properties":{"createdDate":"2000-01-23T04:56:07.000+00:00","sender":"sender","subject":"subject","communicationType":"web","body":"body","communicationDirection":"inbound"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Support/supportTickets/{support_ticket_name}/communications/{communication_name}'.format(support_ticket_name='support_ticket_name_example', communication_name='communication_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=create_communication_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_communications_get(client):
    """Test case for communications_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Support/supportTickets/{support_ticket_name}/communications/{communication_name}'.format(support_ticket_name='support_ticket_name_example', communication_name='communication_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_communications_list(client):
    """Test case for communications_list

    
    """
    params = [('$top', 56),
                    ('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Support/supportTickets/{support_ticket_name}/communications'.format(support_ticket_name='support_ticket_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

