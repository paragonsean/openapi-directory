# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_name_availability_input import CheckNameAvailabilityInput
from openapi_server.models.check_name_availability_output import CheckNameAvailabilityOutput
from openapi_server.models.exception_response import ExceptionResponse
from openapi_server.models.support_ticket_details import SupportTicketDetails
from openapi_server.models.support_tickets_list_result import SupportTicketsListResult
from openapi_server.models.update_support_ticket import UpdateSupportTicket


pytestmark = pytest.mark.asyncio

async def test_support_tickets_check_name_availability(client):
    """Test case for support_tickets_check_name_availability

    
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
        path='/subscriptions/{subscription_id}/providers/Microsoft.Support/checkNameAvailability'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=check_name_availability_input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_support_tickets_create(client):
    """Test case for support_tickets_create

    
    """
    create_support_ticket_parameters = {"name":"name","id":"id","type":"type","properties":{"severity":"minimal","enrollmentId":"enrollmentId","problemStartTime":"2000-01-23T04:56:07.000+00:00","supportPlanType":"supportPlanType","supportEngineer":{"emailAddress":"emailAddress"},"description":"description","quotaTicketDetails":{"quotaChangeRequestSubType":"quotaChangeRequestSubType","quotaChangeRequestVersion":"quotaChangeRequestVersion","quotaChangeRequests":[{"payload":"payload","region":"region"},{"payload":"payload","region":"region"}]},"serviceDisplayName":"serviceDisplayName","serviceLevelAgreement":{"expirationTime":"2000-01-23T04:56:07.000+00:00","slaMinutes":0,"startTime":"2000-01-23T04:56:07.000+00:00"},"title":"title","contactDetails":{"preferredTimeZone":"preferredTimeZone","country":"country","firstName":"firstName","lastName":"lastName","phoneNumber":"phoneNumber","preferredContactMethod":"email","additionalEmailAddresses":["additionalEmailAddresses","additionalEmailAddresses"],"preferredSupportLanguage":"preferredSupportLanguage","primaryEmailAddress":"primaryEmailAddress"},"problemClassificationDisplayName":"problemClassificationDisplayName","createdDate":"2000-01-23T04:56:07.000+00:00","productionOutage":True,"require24X7Response":True,"technicalTicketDetails":{"resourceId":"resourceId"},"modifiedDate":"2000-01-23T04:56:07.000+00:00","problemClassificationId":"problemClassificationId","supportTicketId":"supportTicketId","serviceId":"serviceId","status":"status"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Support/supportTickets/{support_ticket_name}'.format(support_ticket_name='support_ticket_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=create_support_ticket_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_support_tickets_get(client):
    """Test case for support_tickets_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Support/supportTickets/{support_ticket_name}'.format(support_ticket_name='support_ticket_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_support_tickets_list(client):
    """Test case for support_tickets_list

    
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
        path='/subscriptions/{subscription_id}/providers/Microsoft.Support/supportTickets'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_support_tickets_update(client):
    """Test case for support_tickets_update

    
    """
    update_support_ticket = {"severity":"minimal","contactDetails":{"preferredTimeZone":"preferredTimeZone","country":"country","firstName":"firstName","lastName":"lastName","phoneNumber":"phoneNumber","preferredContactMethod":"email","additionalEmailAddresses":["additionalEmailAddresses","additionalEmailAddresses"],"preferredSupportLanguage":"preferredSupportLanguage","primaryEmailAddress":"primaryEmailAddress"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Support/supportTickets/{support_ticket_name}'.format(support_ticket_name='support_ticket_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=update_support_ticket,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

