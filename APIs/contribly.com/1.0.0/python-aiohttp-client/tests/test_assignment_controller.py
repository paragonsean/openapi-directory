# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.assignment import Assignment
from openapi_server.models.assignment_submission import AssignmentSubmission
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_assignments_get(client):
    """Test case for assignments_get

    List assignments
    """
    params = [('ownedBy', 'owned_by_example'),
                    ('page', 56),
                    ('pageSize', 56),
                    ('q', 'q_example'),
                    ('urlWords', 'url_words_example'),
                    ('open', True),
                    ('alwaysOpen', True),
                    ('tag', 'tag_example'),
                    ('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/assignments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assignments_id_delete(client):
    """Test case for assignments_id_delete

    Delete this assignment and all of it's contributions
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/1/assignments/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assignments_id_get(client):
    """Test case for assignments_id_get

    Get a single assigment by id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/assignments/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assignments_post(client):
    """Test case for assignments_post

    Create a new assignment
    """
    body = {"featured":True,"urlWords":"urlWords","moderator":"moderator","description":"description","mediaRequired":True,"tags":[{"tagSet":{"name":"name","id":"id"},"colour":"#0061a6","urlWords":"urlWords","name":"name","id":"id"},{"tagSet":{"name":"name","id":"id"},"colour":"#0061a6","urlWords":"urlWords","name":"name","id":"id"}],"cover":{"id":"id","media":{"duration":5.962133916683182,"id":"id","place":{"country":"country","latLong":{"latitude":5.637376656633329,"longitude":2.3021358869347655},"geohash":"geohash","name":"name","osm":{"osmId":7.061401241503109,"osmType":"osmType"},"google":"google"},"type":"type"},"artifacts":[{"width":1.4658129805029452,"contentLength":0.8008281904610115,"label":"label","contentType":"contentType","url":"url","height":6.027456183070403},{"width":1.4658129805029452,"contentLength":0.8008281904610115,"label":"label","contentType":"contentType","url":"url","height":6.027456183070403}]},"receiptMessage":"receiptMessage","ends":"2000-01-23T04:56:07.000+00:00","allowsAnonymousContributions":True,"name":"name","embargo":"2000-01-23T04:56:07.000+00:00","id":"id","starts":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/1/assignments',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

