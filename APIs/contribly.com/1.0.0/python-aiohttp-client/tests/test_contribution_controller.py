# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.contribution import Contribution
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.export import Export
from openapi_server.models.export_summary import ExportSummary
from openapi_server.models.flag import Flag
from openapi_server.models.moderation_history_item_submission import ModerationHistoryItemSubmission


pytestmark = pytest.mark.asyncio

async def test_contribution_refinement_types_get(client):
    """Test case for contribution_refinement_types_get

    List valid contribution refinement types
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/contribution-refinement-types',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contribution_refinements_get(client):
    """Test case for contribution_refinements_get

    List contribution refinement options
    """
    params = [('assignment', 'assignment_example'),
                    ('country', 'country_example'),
                    ('createdBefore', '2013-10-20T19:20:30+01:00'),
                    ('createdAfter', '2013-10-20T19:20:30+01:00'),
                    ('geohash', 'geohash_example'),
                    ('hasLocation', True),
                    ('latLong', 'lat_long_example'),
                    ('radius', 3.4),
                    ('mediaType', 'media_type_example'),
                    ('ownedBy', 'owned_by_example'),
                    ('q', 'q_example'),
                    ('urlWords', 'url_words_example'),
                    ('user', 'user_example'),
                    ('refinements', 'refinements_example'),
                    ('refinementSize', 3.4)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/contribution-refinements',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contributions_get(client):
    """Test case for contributions_get

    List contributions
    """
    params = [('assignment', 'assignment_example'),
                    ('country', 'country_example'),
                    ('createdBefore', '2013-10-20T19:20:30+01:00'),
                    ('createdAfter', '2013-10-20T19:20:30+01:00'),
                    ('createdDay', '2013-10-20'),
                    ('createdMonth', 'created_month_example'),
                    ('geohash', 'geohash_example'),
                    ('hasLocation', True),
                    ('latLong', 'lat_long_example'),
                    ('radius', 3.4),
                    ('mediaType', 'media_type_example'),
                    ('ownedBy', 'owned_by_example'),
                    ('q', 'q_example'),
                    ('urlWords', 'url_words_example'),
                    ('user', 'user_example'),
                    ('ids', 'ids_example'),
                    ('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/contributions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contributions_id_delete(client):
    """Test case for contributions_id_delete

    Delete this contribution
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/1/contributions/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contributions_id_flag_post(client):
    """Test case for contributions_id_flag_post

    Raise a flag against this contribution
    """
    body = {"date":"2000-01-23T04:56:07.000+00:00","notes":"notes","id":"id","type":"type","email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/1/contributions/{id}/flag'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contributions_id_get(client):
    """Test case for contributions_id_get

    Get a single contribution by id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/contributions/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contributions_id_like_post(client):
    """Test case for contributions_id_like_post

    Allows a user to mark a contribution as liked
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/1/contributions/{id}/like'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contributions_id_likes_get(client):
    """Test case for contributions_id_likes_get

    List users who have liked this contributions
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/contributions/{id}/likes'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contributions_id_moderate_post(client):
    """Test case for contributions_id_moderate_post

    Perform a moderation action on this contribution
    """
    body = {"notes":"notes","action":{"resultingState":{"public":True,"id":"id","label":"label"},"id":"id","label":"label"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/1/contributions/{id}/moderate'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contributions_post(client):
    """Test case for contributions_post

    Create a new contribution
    """
    body = {"urlWords":"urlWords","assignment":{"featured":True,"urlWords":"urlWords","created":"2000-01-23T04:56:07.000+00:00","moderator":"moderator","description":"description","mediaRequired":True,"callToAction":"callToAction","tags":[{"tagSet":{"name":"name","id":"id"},"colour":"#0061a6","urlWords":"urlWords","name":"name","id":"id"},{"tagSet":{"name":"name","id":"id"},"colour":"#0061a6","urlWords":"urlWords","name":"name","id":"id"}],"cover":{"id":"id","media":{"duration":5.962133916683182,"id":"id","place":{"country":"country","latLong":{"latitude":5.637376656633329,"longitude":2.3021358869347655},"geohash":"geohash","name":"name","osm":{"osmId":7.061401241503109,"osmType":"osmType"},"google":"google"},"type":"type"},"artifacts":[{"width":1.4658129805029452,"contentLength":0.8008281904610115,"label":"label","contentType":"contentType","url":"url","height":6.027456183070403},{"width":1.4658129805029452,"contentLength":0.8008281904610115,"label":"label","contentType":"contentType","url":"url","height":6.027456183070403}]},"receiptMessage":"receiptMessage","webUrl":"webUrl","ends":"2000-01-23T04:56:07.000+00:00","allowsAnonymousContributions":True,"name":"name","embargo":"2000-01-23T04:56:07.000+00:00","id":"id","starts":"2000-01-23T04:56:07.000+00:00","open":True},"created":"2000-01-23T04:56:07.000+00:00","attribution":"attribution","moderationHistory":[{"date":"2000-01-23T04:56:07.000+00:00","notes":"notes","action":{"resultingState":{"public":True,"id":"id","label":"label"},"id":"id","label":"label"}},{"date":"2000-01-23T04:56:07.000+00:00","notes":"notes","action":{"resultingState":{"public":True,"id":"id","label":"label"},"id":"id","label":"label"}}],"id":"id","place":{"country":"country","latLong":{"latitude":5.637376656633329,"longitude":2.3021358869347655},"geohash":"geohash","name":"name","osm":{"osmId":7.061401241503109,"osmType":"osmType"},"google":"google"},"body":"body","headline":"headline","mediaUsages":[{"id":"id","media":{"duration":5.962133916683182,"id":"id","place":{"country":"country","latLong":{"latitude":5.637376656633329,"longitude":2.3021358869347655},"geohash":"geohash","name":"name","osm":{"osmId":7.061401241503109,"osmType":"osmType"},"google":"google"},"type":"type"},"artifacts":[{"width":1.4658129805029452,"contentLength":0.8008281904610115,"label":"label","contentType":"contentType","url":"url","height":6.027456183070403},{"width":1.4658129805029452,"contentLength":0.8008281904610115,"label":"label","contentType":"contentType","url":"url","height":6.027456183070403}]},{"id":"id","media":{"duration":5.962133916683182,"id":"id","place":{"country":"country","latLong":{"latitude":5.637376656633329,"longitude":2.3021358869347655},"geohash":"geohash","name":"name","osm":{"osmId":7.061401241503109,"osmType":"osmType"},"google":"google"},"type":"type"},"artifacts":[{"width":1.4658129805029452,"contentLength":0.8008281904610115,"label":"label","contentType":"contentType","url":"url","height":6.027456183070403},{"width":1.4658129805029452,"contentLength":0.8008281904610115,"label":"label","contentType":"contentType","url":"url","height":6.027456183070403}]}],"via":{"ipAddressPlace":{"country":"country","latLong":{"latitude":5.637376656633329,"longitude":2.3021358869347655},"geohash":"geohash","name":"name","osm":{"osmId":7.061401241503109,"osmType":"osmType"},"google":"google"},"authority":{"client":{"name":"name","id":"id"},"id":"id","user":{"displayName":"displayName","bio":"bio","registered":"2000-01-23T04:56:07.000+00:00","id":"id","username":"username"}},"ipAddress":"ipAddress"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/contributions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_post(client):
    """Test case for export_post

    Export contributions.
    """
    params = [('assignment', 'assignment_example'),
                    ('country', 'country_example'),
                    ('createdBefore', '2013-10-20T19:20:30+01:00'),
                    ('createdAfter', '2013-10-20T19:20:30+01:00'),
                    ('geohash', 'geohash_example'),
                    ('hasLocation', True),
                    ('latLong', 'lat_long_example'),
                    ('radius', 3.4),
                    ('mediaType', 'media_type_example'),
                    ('ownedBy', 'owned_by_example'),
                    ('q', 'q_example'),
                    ('urlWords', 'url_words_example'),
                    ('user', 'user_example'),
                    ('tagged', True),
                    ('combined', True),
                    ('individual', True),
                    ('format', 'format_example'),
                    ('json', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/1/export',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_summary_post(client):
    """Test case for export_summary_post

    Export contributions preflight summary.
    """
    params = [('assignment', 'assignment_example'),
                    ('country', 'country_example'),
                    ('createdBefore', '2013-10-20T19:20:30+01:00'),
                    ('createdAfter', '2013-10-20T19:20:30+01:00'),
                    ('geohash', 'geohash_example'),
                    ('hasLocation', True),
                    ('latLong', 'lat_long_example'),
                    ('radius', 3.4),
                    ('mediaType', 'media_type_example'),
                    ('ownedBy', 'owned_by_example'),
                    ('q', 'q_example'),
                    ('urlWords', 'url_words_example'),
                    ('user', 'user_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/1/export-summary',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_exports_id_get(client):
    """Test case for exports_id_get

    Get a single export job; poll to follow export progress.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/exports/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

