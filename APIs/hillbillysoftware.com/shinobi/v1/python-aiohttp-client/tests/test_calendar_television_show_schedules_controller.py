# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.country import Country
from openapi_server.models.networks import Networks
from openapi_server.models.schedule import Schedule
from openapi_server.models.show_seasons import ShowSeasons


pytestmark = pytest.mark.asyncio

async def test_calendar_by_show_name_get(client):
    """Test case for calendar_by_show_name_get

    Will return show schedule for queried showname and year
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Calendar/Show/{access_token}/{name}/{year}'.format(access_token='access_token_example', name='name_example', year='year_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calendar_countries_get(client):
    """Test case for calendar_countries_get

    Returns list of available countries in calendar database
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Calendar/Countries/{access_token}'.format(access_token='access_token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calendar_networks_get(client):
    """Test case for calendar_networks_get

    Gets a list of available networks
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Calendar/Networks/{access_token}'.format(access_token='access_token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calendar_show_seasons_get(client):
    """Test case for calendar_show_seasons_get

    Returns list of seasons available in the calendar for show
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Calendar/Seasons/{access_token}/{name}'.format(access_token='access_token_example', name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calendar_today_get(client):
    """Test case for calendar_today_get

    Will return show schedule for today for all countries in database
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Calendar/Today/{access_token}'.format(access_token='access_token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calendarby_showname_season_get(client):
    """Test case for calendarby_showname_season_get

    Get Calendar by showname and season
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Calendar/Show/Season/{access_token}/{name}/{season}'.format(access_token='access_token_example', name='name_example', season='season_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedule_by_date_get(client):
    """Test case for schedule_by_date_get

    Gets TV Schedule for selected data
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Calendar/ByDate/{access_token}/{_date}/{country}'.format(access_token='access_token_example', _date='_date_example', country='country_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

