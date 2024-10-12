# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error401 import Error401
from openapi_server.models.error404 import Error404
from openapi_server.models.error500 import Error500
from openapi_server.models.nh_artwork import NHArtwork
from openapi_server.models.nh_bug import NHBug
from openapi_server.models.nh_clothing import NHClothing
from openapi_server.models.nh_event import NHEvent
from openapi_server.models.nh_fish import NHFish
from openapi_server.models.nh_fossil_group import NHFossilGroup
from openapi_server.models.nh_fossil_group_with_individual_fossils import NHFossilGroupWithIndividualFossils
from openapi_server.models.nh_fossil_group_with_individual_fossils_no_matched import NHFossilGroupWithIndividualFossilsNoMatched
from openapi_server.models.nh_furniture import NHFurniture
from openapi_server.models.nh_individual_fossil import NHIndividualFossil
from openapi_server.models.nh_interior import NHInterior
from openapi_server.models.nh_item import NHItem
from openapi_server.models.nh_photo import NHPhoto
from openapi_server.models.nh_recipe import NHRecipe
from openapi_server.models.nh_sea_creature import NHSeaCreature
from openapi_server.models.nh_tool import NHTool
from openapi_server.models.villager import Villager


pytestmark = pytest.mark.asyncio

async def test_nh_art_artwork_get(client):
    """Test case for nh_art_artwork_get

    Single New Horizons artwork
    """
    params = [('thumbsize', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
        'accept_version': 'accept_version_example',
    }
    response = await client.request(
        method='GET',
        path='/nh/art/{artwork}'.format(artwork='artwork_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nh_art_get(client):
    """Test case for nh_art_get

    All New Horizons artwork
    """
    params = [('hasfake', 'hasfake_example'),
                    ('excludedetails', 'excludedetails_example'),
                    ('thumbsize', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
        'accept_version': 'accept_version_example',
    }
    response = await client.request(
        method='GET',
        path='/nh/art',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nh_bugs_bug_get(client):
    """Test case for nh_bugs_bug_get

    Single New Horizons bug
    """
    params = [('thumbsize', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
        'accept_version': 'accept_version_example',
    }
    response = await client.request(
        method='GET',
        path='/nh/bugs/{bug}'.format(bug='bug_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nh_bugs_get(client):
    """Test case for nh_bugs_get

    All New Horizons bugs
    """
    params = [('month', 'month_example'),
                    ('excludedetails', 'excludedetails_example'),
                    ('thumbsize', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
        'accept_version': 'accept_version_example',
    }
    response = await client.request(
        method='GET',
        path='/nh/bugs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nh_clothing_clothing_get(client):
    """Test case for nh_clothing_clothing_get

    Single New Horizons clothing
    """
    params = [('thumbsize', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
        'accept_version': 'accept_version_example',
    }
    response = await client.request(
        method='GET',
        path='/nh/clothing/{clothing}'.format(clothing='clothing_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nh_clothing_get(client):
    """Test case for nh_clothing_get

    All New Horizons clothing
    """
    params = [('category', 'category_example'),
                    ('color', ['color_example']),
                    ('style', ['style_example']),
                    ('labeltheme', 'labeltheme_example'),
                    ('excludedetails', 'excludedetails_example')]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
        'accept_version': 'accept_version_example',
    }
    response = await client.request(
        method='GET',
        path='/nh/clothing',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nh_events_get(client):
    """Test case for nh_events_get

    All New Horizons events
    """
    params = [('date', '_date_example'),
                    ('year', 'year_example'),
                    ('month', 'month_example'),
                    ('day', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
        'accept_version': 'accept_version_example',
    }
    response = await client.request(
        method='GET',
        path='/nh/events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nh_fish_fish_get(client):
    """Test case for nh_fish_fish_get

    Single New Horizons fish
    """
    params = [('thumbsize', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
        'accept_version': 'accept_version_example',
    }
    response = await client.request(
        method='GET',
        path='/nh/fish/{fish}'.format(fish='fish_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nh_fish_get(client):
    """Test case for nh_fish_get

    All New Horizons fish
    """
    params = [('month', 'month_example'),
                    ('excludedetails', 'excludedetails_example'),
                    ('thumbsize', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
        'accept_version': 'accept_version_example',
    }
    response = await client.request(
        method='GET',
        path='/nh/fish',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nh_fossils_all_fossil_get(client):
    """Test case for nh_fossils_all_fossil_get

    Single New Horizons fossil group with individual fossils
    """
    params = [('thumbsize', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
        'accept_version': 'accept_version_example',
    }
    response = await client.request(
        method='GET',
        path='/nh/fossils/all/{fossil}'.format(fossil='fossil_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nh_fossils_all_get(client):
    """Test case for nh_fossils_all_get

    All New Horizons fossil groups or individual fossil
    """
    params = [('thumbsize', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
        'accept_version': 'accept_version_example',
    }
    response = await client.request(
        method='GET',
        path='/nh/fossils/all',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nh_fossils_groups_fossil_group_get(client):
    """Test case for nh_fossils_groups_fossil_group_get

    Single New Horizons fossil group
    """
    params = [('thumbsize', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
        'accept_version': 'accept_version_example',
    }
    response = await client.request(
        method='GET',
        path='/nh/fossils/groups/{fossil_group}'.format(fossil_group='fossil_group_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nh_fossils_groups_get(client):
    """Test case for nh_fossils_groups_get

    All New Horizons fossil groups
    """
    params = [('thumbsize', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
        'accept_version': 'accept_version_example',
    }
    response = await client.request(
        method='GET',
        path='/nh/fossils/groups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nh_fossils_individuals_fossil_get(client):
    """Test case for nh_fossils_individuals_fossil_get

    Single New Horizons fossil
    """
    params = [('thumbsize', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
        'accept_version': 'accept_version_example',
    }
    response = await client.request(
        method='GET',
        path='/nh/fossils/individuals/{fossil}'.format(fossil='fossil_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nh_fossils_individuals_get(client):
    """Test case for nh_fossils_individuals_get

    All New Horizons fossils
    """
    params = [('thumbsize', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
        'accept_version': 'accept_version_example',
    }
    response = await client.request(
        method='GET',
        path='/nh/fossils/individuals',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nh_furniture_furniture_get(client):
    """Test case for nh_furniture_furniture_get

    Single New Horizons furniture
    """
    params = [('thumbsize', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
        'accept_version': 'accept_version_example',
    }
    response = await client.request(
        method='GET',
        path='/nh/furniture/{furniture}'.format(furniture='furniture_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nh_furniture_get(client):
    """Test case for nh_furniture_get

    All New Horizons furniture
    """
    params = [('category', 'category_example'),
                    ('color', ['color_example']),
                    ('excludedetails', 'excludedetails_example')]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
        'accept_version': 'accept_version_example',
    }
    response = await client.request(
        method='GET',
        path='/nh/furniture',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nh_interior_get(client):
    """Test case for nh_interior_get

    All New Horizons interior items
    """
    params = [('color', ['color_example']),
                    ('excludedetails', 'excludedetails_example')]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
        'accept_version': 'accept_version_example',
    }
    response = await client.request(
        method='GET',
        path='/nh/interior',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nh_interior_item_get(client):
    """Test case for nh_interior_item_get

    Single New Horizons interior item
    """
    params = [('color', ['color_example']),
                    ('thumbsize', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
        'accept_version': 'accept_version_example',
    }
    response = await client.request(
        method='GET',
        path='/nh/interior/{item}'.format(item='item_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nh_items_get(client):
    """Test case for nh_items_get

    Miscellaneous New Horizons items
    """
    params = [('excludedetails', 'excludedetails_example')]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
        'accept_version': 'accept_version_example',
    }
    response = await client.request(
        method='GET',
        path='/nh/items',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nh_items_item_get(client):
    """Test case for nh_items_item_get

    Single New Horizons miscellaneous item
    """
    params = [('thumbsize', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
        'accept_version': 'accept_version_example',
    }
    response = await client.request(
        method='GET',
        path='/nh/items/{item}'.format(item='item_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nh_photos_get(client):
    """Test case for nh_photos_get

    All New Horizons photos and posters
    """
    params = [('excludedetails', 'excludedetails_example')]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
        'accept_version': 'accept_version_example',
    }
    response = await client.request(
        method='GET',
        path='/nh/photos',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nh_photos_item_get(client):
    """Test case for nh_photos_item_get

    Single New Horizons photo or poster
    """
    params = [('thumbsize', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
        'accept_version': 'accept_version_example',
    }
    response = await client.request(
        method='GET',
        path='/nh/photos/{item}'.format(item='item_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nh_recipes_get(client):
    """Test case for nh_recipes_get

    All New Horizons recipes
    """
    params = [('material', 'material_example'),
                    ('excludedetails', 'excludedetails_example'),
                    ('thumbsize', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
        'accept_version': 'accept_version_example',
    }
    response = await client.request(
        method='GET',
        path='/nh/recipes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nh_recipes_item_get(client):
    """Test case for nh_recipes_item_get

    Single New Horizons recipe
    """
    params = [('thumbsize', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
        'accept_version': 'accept_version_example',
    }
    response = await client.request(
        method='GET',
        path='/nh/recipes/{item}'.format(item='item_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nh_sea_get(client):
    """Test case for nh_sea_get

    All New Horizons sea creatures
    """
    params = [('month', 'month_example'),
                    ('excludedetails', 'excludedetails_example'),
                    ('thumbsize', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
        'accept_version': 'accept_version_example',
    }
    response = await client.request(
        method='GET',
        path='/nh/sea',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nh_sea_sea_creature_get(client):
    """Test case for nh_sea_sea_creature_get

    Single New Horizons sea creature
    """
    params = [('thumbsize', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
        'accept_version': 'accept_version_example',
    }
    response = await client.request(
        method='GET',
        path='/nh/sea/{sea_creature}'.format(sea_creature='sea_creature_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nh_tools_get(client):
    """Test case for nh_tools_get

    All New Horizons tools
    """
    params = [('excludedetails', 'excludedetails_example')]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
        'accept_version': 'accept_version_example',
    }
    response = await client.request(
        method='GET',
        path='/nh/tools',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nh_tools_tool_get(client):
    """Test case for nh_tools_tool_get

    Single New Horizons tool
    """
    params = [('thumbsize', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
        'accept_version': 'accept_version_example',
    }
    response = await client.request(
        method='GET',
        path='/nh/tools/{tool}'.format(tool='tool_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_villagers_get(client):
    """Test case for villagers_get

    Villagers
    """
    params = [('name', 'name_example'),
                    ('species', 'species_example'),
                    ('personality', 'personality_example'),
                    ('game', ['game_example']),
                    ('birthmonth', 'birthmonth_example'),
                    ('birthday', 'birthday_example'),
                    ('nhdetails', 'nhdetails_example'),
                    ('excludedetails', 'excludedetails_example'),
                    ('thumbsize', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
        'accept_version': 'accept_version_example',
    }
    response = await client.request(
        method='GET',
        path='/villagers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

