# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_contact_in_mailing_list import CreateContactInMailingList
from openapi_server.models.create_distribution_links import CreateDistributionLinks
from openapi_server.models.distributions_response import DistributionsResponse
from openapi_server.models.event_subscriptions_response import EventSubscriptionsResponse
from openapi_server.models.retrieve_distribution_links_response import RetrieveDistributionLinksResponse
from openapi_server.models.subscribe_to_event_body import SubscribeToEventBody


pytestmark = pytest.mark.asyncio

async def test_create_contact_in_mailinglist(client):
    """Test case for create_contact_in_mailinglist

    Create contact in mailing list
    """
    body = {"firstName":"firstName","lastName":"lastName","unsubscribed":True,"email":"email"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/API/v3/directories/{directory_id}/mailinglists/{mailing_list_id}/contacts'.format(directory_id='directory_id_example', mailing_list_id='mailing_list_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_generate_distribution_links(client):
    """Test case for generate_distribution_links

    Generate distribution links
    """
    body = {"mailingListId":"mailingListId","surveyId":"surveyId","action":"CreateDistribution","description":"description","linkType":"linkType","expirationDate":"2021-01-21 00:00:00"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/API/v3/distributions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_distributions(client):
    """Test case for get_distributions

    Get distributions for survey
    """
    params = [('surveyId', 'survey_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/API/v3/distributions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_event_subscriptions(client):
    """Test case for get_event_subscriptions

    Get event subscriptions
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/API/v3/eventsubscriptions/{subscription_id}'.format(subscription_id='subscription_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_survey(client):
    """Test case for get_survey

    Get survey
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/API/v3/survey-definitions/{survey_id}'.format(survey_id='survey_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrievedistributionlinks(client):
    """Test case for retrievedistributionlinks

    Retrieve distribution links
    """
    params = [('surveyId', 'survey_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/API/v3/distributions/{distribution_id}/links'.format(distribution_id='distribution_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_webhook_delete(client):
    """Test case for webhook_delete

    Remove subscription to response event
    """
    body = {"encrypt":True,"topics":"surveyengine.completedResponse.<Insert SurveyID>","publicationUrl":"publicationUrl"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/API/v3/eventsubscriptions/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_when_a_response_is_received(client):
    """Test case for when_a_response_is_received

    Triggers when a response is submitted to a qualtrics survey
    """
    body = {"encrypt":True,"topics":"surveyengine.completedResponse.<Insert SurveyID>","publicationUrl":"publicationUrl"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/API/v3/eventsubscriptions/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

