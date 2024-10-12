# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.assessment_group_required import AssessmentGroupRequired
from openapi_server.models.assessment_group_response import AssessmentGroupResponse
from openapi_server.models.error import Error
from openapi_server.models.offerings_offering_id_groups_group_id_learners_post_request import OfferingsOfferingIdGroupsGroupIdLearnersPostRequest
from openapi_server.models.user_response import UserResponse


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_groups_get(client):
    """Test case for offerings_offering_id_groups_get

    Find assessment groups
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offerings/{offering_id}/groups'.format(offering_id='offering_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_groups_group_id_learners_get(client):
    """Test case for offerings_offering_id_groups_group_id_learners_get

    Find learners in an assessment group
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offerings/{offering_id}/groups/{group_id}/learners'.format(offering_id='offering_id_example', group_id='group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_groups_group_id_learners_post(client):
    """Test case for offerings_offering_id_groups_group_id_learners_post

    Add a learner to an assessment group
    """
    body = openapi_server.OfferingsOfferingIdGroupsGroupIdLearnersPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/offerings/{offering_id}/groups/{group_id}/learners'.format(offering_id='offering_id_example', group_id='group_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_groups_group_id_learners_user_email_delete(client):
    """Test case for offerings_offering_id_groups_group_id_learners_user_email_delete

    Remove a learner from an assessment group
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/offerings/{offering_id}/groups/{group_id}/learners/{user_email}'.format(offering_id='offering_id_example', group_id='group_id_example', user_email='user_email_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_groups_post(client):
    """Test case for offerings_offering_id_groups_post

    Add an assessment group
    """
    body = {"title":"title"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/offerings/{offering_id}/groups'.format(offering_id='offering_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

