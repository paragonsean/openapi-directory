# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.actor import Actor
from openapi_server.models.actor_post import ActorPost
from openapi_server.models.crew import Crew
from openapi_server.models.post_result import PostResult
from openapi_server.models.tv_show_actor import TVShowActor


pytestmark = pytest.mark.asyncio

async def test_actor_get(client):
    """Test case for actor_get

    Returns data on queried actor/actress. Result set limited to 5 records
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Actors/Search/{accesstoken}/{query}'.format(accesstoken='accesstoken_example', query='query_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actor_in_shows_get(client):
    """Test case for actor_in_shows_get

    Returns all shows queried actor/actress is or has been in
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Cast/ActorBySearch/{access_token}/{actor}'.format(access_token='access_token_example', actor='actor_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actors_in_tv_show_get(client):
    """Test case for actors_in_tv_show_get

    Returns all actors in queried tvshow
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Cast/ByTVShow/{accesstoken}/{show_name}'.format(accesstoken='accesstoken_example', show_name='show_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_add_actor_post(client):
    """Test case for add_actor_post

    Add new actor or actress to database
    """
    value = {"BirthYear":"BirthYear","PopularityIndex":"PopularityIndex","AccessToken":"AccessToken","DeathYear":"DeathYear","ProfileImage":"ProfileImage","Bio":"Bio","Gender":"Gender","Name":"Name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/AddActor',
        headers=headers,
        json=value,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cast_by_actor_get(client):
    """Test case for cast_by_actor_get

    Returns list of show actor is appearing in
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Cast/ByActor/{access_token}/{actor}'.format(access_token='access_token_example', actor='actor_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_crew_by_id_get(client):
    """Test case for crew_by_id_get

    Get crew list by ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Crew/ByID/{access_token}/{id}'.format(access_token='access_token_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_crew_by_person_get(client):
    """Test case for crew_by_person_get

    Gets list of productions searched person is/was involved in.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Crew/ByPerson/{access_token}/{person_name}'.format(access_token='access_token_example', person_name='person_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_crew_get(client):
    """Test case for crew_get

    Returns crew for queried show.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Crew/Search/{access_token}/{phrase}'.format(access_token='access_token_example', phrase='phrase_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_crewby_showname_get(client):
    """Test case for crewby_showname_get

    Get crew list by showname
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Crew/ByShowName/{access_token}/{show_name}'.format(access_token='access_token_example', show_name='show_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

