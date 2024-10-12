# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.delete_fleets_fleet_id_members_member_id_not_found import DeleteFleetsFleetIdMembersMemberIdNotFound
from openapi_server.models.delete_fleets_fleet_id_squads_squad_id_not_found import DeleteFleetsFleetIdSquadsSquadIdNotFound
from openapi_server.models.delete_fleets_fleet_id_wings_wing_id_not_found import DeleteFleetsFleetIdWingsWingIdNotFound
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_characters_character_id_fleet_not_found import GetCharactersCharacterIdFleetNotFound
from openapi_server.models.get_characters_character_id_fleet_ok import GetCharactersCharacterIdFleetOk
from openapi_server.models.get_fleets_fleet_id_members200_ok import GetFleetsFleetIdMembers200Ok
from openapi_server.models.get_fleets_fleet_id_members_not_found import GetFleetsFleetIdMembersNotFound
from openapi_server.models.get_fleets_fleet_id_not_found import GetFleetsFleetIdNotFound
from openapi_server.models.get_fleets_fleet_id_ok import GetFleetsFleetIdOk
from openapi_server.models.get_fleets_fleet_id_wings200_ok import GetFleetsFleetIdWings200Ok
from openapi_server.models.get_fleets_fleet_id_wings_not_found import GetFleetsFleetIdWingsNotFound
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.post_fleets_fleet_id_members_invitation import PostFleetsFleetIdMembersInvitation
from openapi_server.models.post_fleets_fleet_id_members_not_found import PostFleetsFleetIdMembersNotFound
from openapi_server.models.post_fleets_fleet_id_members_unprocessable_entity import PostFleetsFleetIdMembersUnprocessableEntity
from openapi_server.models.post_fleets_fleet_id_wings_created import PostFleetsFleetIdWingsCreated
from openapi_server.models.post_fleets_fleet_id_wings_not_found import PostFleetsFleetIdWingsNotFound
from openapi_server.models.post_fleets_fleet_id_wings_wing_id_squads_created import PostFleetsFleetIdWingsWingIdSquadsCreated
from openapi_server.models.post_fleets_fleet_id_wings_wing_id_squads_not_found import PostFleetsFleetIdWingsWingIdSquadsNotFound
from openapi_server.models.put_fleets_fleet_id_members_member_id_movement import PutFleetsFleetIdMembersMemberIdMovement
from openapi_server.models.put_fleets_fleet_id_members_member_id_not_found import PutFleetsFleetIdMembersMemberIdNotFound
from openapi_server.models.put_fleets_fleet_id_members_member_id_unprocessable_entity import PutFleetsFleetIdMembersMemberIdUnprocessableEntity
from openapi_server.models.put_fleets_fleet_id_new_settings import PutFleetsFleetIdNewSettings
from openapi_server.models.put_fleets_fleet_id_not_found import PutFleetsFleetIdNotFound
from openapi_server.models.put_fleets_fleet_id_squads_squad_id_naming import PutFleetsFleetIdSquadsSquadIdNaming
from openapi_server.models.put_fleets_fleet_id_squads_squad_id_not_found import PutFleetsFleetIdSquadsSquadIdNotFound
from openapi_server.models.put_fleets_fleet_id_wings_wing_id_naming import PutFleetsFleetIdWingsWingIdNaming
from openapi_server.models.put_fleets_fleet_id_wings_wing_id_not_found import PutFleetsFleetIdWingsWingIdNotFound
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server.models.unauthorized import Unauthorized


pytestmark = pytest.mark.asyncio

async def test_delete_fleets_fleet_id_members_member_id(client):
    """Test case for delete_fleets_fleet_id_members_member_id

    Kick fleet member
    """
    params = [('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/latest/fleets/{fleet_id}/members/{member_id}'.format(fleet_id=56, member_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_fleets_fleet_id_squads_squad_id(client):
    """Test case for delete_fleets_fleet_id_squads_squad_id

    Delete fleet squad
    """
    params = [('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/latest/fleets/{fleet_id}/squads/{squad_id}'.format(fleet_id=56, squad_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_fleets_fleet_id_wings_wing_id(client):
    """Test case for delete_fleets_fleet_id_wings_wing_id

    Delete fleet wing
    """
    params = [('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/latest/fleets/{fleet_id}/wings/{wing_id}'.format(fleet_id=56, wing_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_characters_character_id_fleet(client):
    """Test case for get_characters_character_id_fleet

    Get character fleet info
    """
    params = [('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/latest/characters/{character_id}/fleet'.format(character_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_fleets_fleet_id(client):
    """Test case for get_fleets_fleet_id

    Get fleet information
    """
    params = [('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/latest/fleets/{fleet_id}'.format(fleet_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_fleets_fleet_id_members(client):
    """Test case for get_fleets_fleet_id_members

    Get fleet members
    """
    params = [('datasource', tranquility),
                    ('language', en-us),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': en-us,
        'if_none_match': 'if_none_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/latest/fleets/{fleet_id}/members'.format(fleet_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_fleets_fleet_id_wings(client):
    """Test case for get_fleets_fleet_id_wings

    Get fleet wings
    """
    params = [('datasource', tranquility),
                    ('language', en-us),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': en-us,
        'if_none_match': 'if_none_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/latest/fleets/{fleet_id}/wings'.format(fleet_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_fleets_fleet_id_members(client):
    """Test case for post_fleets_fleet_id_members

    Create fleet invitation
    """
    invitation = openapi_server.PostFleetsFleetIdMembersInvitation()
    params = [('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/latest/fleets/{fleet_id}/members'.format(fleet_id=56),
        headers=headers,
        json=invitation,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_fleets_fleet_id_wings(client):
    """Test case for post_fleets_fleet_id_wings

    Create fleet wing
    """
    params = [('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/latest/fleets/{fleet_id}/wings'.format(fleet_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_fleets_fleet_id_wings_wing_id_squads(client):
    """Test case for post_fleets_fleet_id_wings_wing_id_squads

    Create fleet squad
    """
    params = [('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/latest/fleets/{fleet_id}/wings/{wing_id}/squads'.format(fleet_id=56, wing_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_fleets_fleet_id(client):
    """Test case for put_fleets_fleet_id

    Update fleet
    """
    new_settings = openapi_server.PutFleetsFleetIdNewSettings()
    params = [('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/latest/fleets/{fleet_id}'.format(fleet_id=56),
        headers=headers,
        json=new_settings,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_fleets_fleet_id_members_member_id(client):
    """Test case for put_fleets_fleet_id_members_member_id

    Move fleet member
    """
    movement = openapi_server.PutFleetsFleetIdMembersMemberIdMovement()
    params = [('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/latest/fleets/{fleet_id}/members/{member_id}'.format(fleet_id=56, member_id=56),
        headers=headers,
        json=movement,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_fleets_fleet_id_squads_squad_id(client):
    """Test case for put_fleets_fleet_id_squads_squad_id

    Rename fleet squad
    """
    naming = openapi_server.PutFleetsFleetIdSquadsSquadIdNaming()
    params = [('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/latest/fleets/{fleet_id}/squads/{squad_id}'.format(fleet_id=56, squad_id=56),
        headers=headers,
        json=naming,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_fleets_fleet_id_wings_wing_id(client):
    """Test case for put_fleets_fleet_id_wings_wing_id

    Rename fleet wing
    """
    naming = openapi_server.PutFleetsFleetIdWingsWingIdNaming()
    params = [('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/latest/fleets/{fleet_id}/wings/{wing_id}'.format(fleet_id=56, wing_id=56),
        headers=headers,
        json=naming,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

