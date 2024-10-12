# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.learner_progress_response import LearnerProgressResponse
from openapi_server.models.learner_response import LearnerResponse
from openapi_server.models.social_notes_response import SocialNotesResponse
from openapi_server.models.unit_reactions_analytics_response import UnitReactionsAnalyticsResponse
from openapi_server.models.users_all_progress_get200_response import UsersAllProgressGet200Response
from openapi_server.models.users_user_email_offerings_offering_id_progress_get200_response import UsersUserEmailOfferingsOfferingIdProgressGet200Response


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_analytics_learners_progress_get(client):
    """Test case for offerings_offering_id_analytics_learners_progress_get

    Find learner progress in a specified offering
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offerings/{offering_id}/analytics/learners-progress'.format(offering_id='offering_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_analytics_social_notes_get(client):
    """Test case for offerings_offering_id_analytics_social_notes_get

    Find shared social notes in an offering
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offerings/{offering_id}/analytics/social-notes'.format(offering_id='offering_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_analytics_unit_reactions_get(client):
    """Test case for offerings_offering_id_analytics_unit_reactions_get

    Find unit reactions
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offerings/{offering_id}/analytics/unit-reactions'.format(offering_id='offering_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_all_progress_get(client):
    """Test case for users_all_progress_get

    Find learner progress in all offerings
    """
    params = [('$top', '50'),
                    ('$orderby', 'orderby_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/users/all/progress',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_email_offerings_offering_id_progress_get(client):
    """Test case for users_user_email_offerings_offering_id_progress_get

    Find learner's progress in a specified offering
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/users/{user_email}/offerings/{offering_id}/progress'.format(user_email='user_email_example', offering_id='offering_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_email_progress_get(client):
    """Test case for users_user_email_progress_get

    Find learner's progress in offerings
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/users/{user_email}/progress'.format(user_email='user_email_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

