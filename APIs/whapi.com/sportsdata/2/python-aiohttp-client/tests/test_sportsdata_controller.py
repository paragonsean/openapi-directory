# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.classes_wrapper import ClassesWrapper
from openapi_server.models.competition import Competition
from openapi_server.models.competitions_wrapper import CompetitionsWrapper
from openapi_server.models.errors_wrapper import ErrorsWrapper
from openapi_server.models.events_wrapper import EventsWrapper
from openapi_server.models.market_groups_wrapper import MarketGroupsWrapper
from openapi_server.models.markets_wrapper import MarketsWrapper
from openapi_server.models.selections_wrapper import SelectionsWrapper
from openapi_server.models.sports_wrapper import SportsWrapper
from openapi_server.models.top_bets_wrapper import TopBetsWrapper


pytestmark = pytest.mark.asyncio

async def test_get_classes_for_sport(client):
    """Test case for get_classes_for_sport

    Retrieves a list of classes for a given sport id.
    """
    params = [('isPublished', 'true'),
                    ('fields', ['fields_example']),
                    ('include', ['include_example']),
                    ('exclude', ['exclude_example']),
                    ('displayed', 'true'),
                    ('channel', 'channel_example'),
                    ('status', 'status_example'),
                    ('sort', 'id,asc'),
                    ('offset', 0),
                    ('limit', 100),
                    ('culture', 'culture_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/sportsdata/sports/{sport_id}/classes'.format(sport_id='sport_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_competition(client):
    """Test case for get_competition

    Retrieves a specific competition
    """
    params = [('fields', ['fields_example']),
                    ('include', ['include_example']),
                    ('exclude', ['exclude_example']),
                    ('culture', 'culture_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/sportsdata/competitions/{competition_id}'.format(competition_id='competition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_competitions_for_class(client):
    """Test case for get_competitions_for_class

    Retrieves a list of competitions for a given class id.
    """
    params = [('isPublished', 'true'),
                    ('fields', ['fields_example']),
                    ('include', ['include_example']),
                    ('exclude', ['exclude_example']),
                    ('displayed', 'true'),
                    ('channel', 'channel_example'),
                    ('status', 'status_example'),
                    ('sort', 'id,asc'),
                    ('offset', 0),
                    ('limit', 100),
                    ('culture', 'culture_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/sportsdata/classes/{class_id}/competitions'.format(class_id='class_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_competitions_for_sport(client):
    """Test case for get_competitions_for_sport

    Retrieves a list of competitions for a given sport id.
    """
    params = [('isPublished', 'true'),
                    ('fields', ['fields_example']),
                    ('include', ['include_example']),
                    ('exclude', ['exclude_example']),
                    ('displayed', 'true'),
                    ('channel', 'channel_example'),
                    ('status', 'status_example'),
                    ('sort', 'id,asc'),
                    ('offset', 0),
                    ('limit', 100),
                    ('culture', 'culture_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/sportsdata/sports/{sport_id}/competitions'.format(sport_id='sport_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_event(client):
    """Test case for get_event

    Retrieves a single event by ID.
    """
    params = [('includeAllDescendants', False),
                    ('fields', ['fields_example']),
                    ('include', ['include_example']),
                    ('exclude', ['exclude_example']),
                    ('headlineSummary', False),
                    ('marketCount', 1),
                    ('marketIds', ['market_ids_example']),
                    ('includeEmpty', True),
                    ('culture', 'culture_example'),
                    ('marketPublished', 'true'),
                    ('marketStatus', 'market_status_example'),
                    ('marketDisplayed', 'true'),
                    ('marketChannel', 'market_channel_example'),
                    ('marketSort', 'market_sort_example'),
                    ('marketEW', 'market_ew_example'),
                    ('selectionStatus', 'selection_status_example'),
                    ('selectionChannel', 'selection_channel_example'),
                    ('selectionPublished', 'true')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/sportsdata/events/{event_id}'.format(event_id='event_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_events(client):
    """Test case for get_events

    Retrieves a list of events for the provided IDs.
    """
    params = [('ids', ['ids_example']),
                    ('isPublished', 'true'),
                    ('includeAllDescendants', False),
                    ('fields', ['fields_example']),
                    ('include', ['include_example']),
                    ('exclude', ['exclude_example']),
                    ('channel', 'channel_example'),
                    ('settled', True),
                    ('includeEmpty', True),
                    ('headlineSummary', False),
                    ('marketCount', 1),
                    ('sort', 'id,asc'),
                    ('offset', 0),
                    ('limit', 100),
                    ('marketIds', ['market_ids_example']),
                    ('culture', 'culture_example'),
                    ('marketPublished', 'true'),
                    ('marketStatus', 'market_status_example'),
                    ('marketDisplayed', 'true'),
                    ('marketChannel', 'market_channel_example'),
                    ('marketSort', 'market_sort_example'),
                    ('marketEW', 'market_ew_example'),
                    ('selectionStatus', 'selection_status_example'),
                    ('selectionChannel', 'selection_channel_example'),
                    ('selectionPublished', 'true')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/sportsdata/events/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_events_for_class(client):
    """Test case for get_events_for_class

    Retrieves a list of events for a given class id.
    """
    params = [('isPublished', 'true'),
                    ('fields', ['fields_example']),
                    ('include', ['include_example']),
                    ('exclude', ['exclude_example']),
                    ('displayed', 'true'),
                    ('channel', 'channel_example'),
                    ('settled', True),
                    ('includeEmpty', True),
                    ('status', 'status_example'),
                    ('sort', 'id,asc'),
                    ('offset', 0),
                    ('limit', 100),
                    ('headlineSummary', False),
                    ('includeAllDescendants', False),
                    ('isInPlay', True),
                    ('marketCount', 1),
                    ('date', '_date_example'),
                    ('dateFrom', 'date_from_example'),
                    ('dateTo', 'date_to_example'),
                    ('eventSort', 'event_sort_example'),
                    ('culture', 'culture_example'),
                    ('marketPublished', 'true'),
                    ('marketStatus', 'market_status_example'),
                    ('marketDisplayed', 'true'),
                    ('marketChannel', 'market_channel_example'),
                    ('marketSort', 'market_sort_example'),
                    ('marketEW', 'market_ew_example'),
                    ('selectionStatus', 'selection_status_example'),
                    ('selectionChannel', 'selection_channel_example'),
                    ('selectionPublished', 'true')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/sportsdata/classes/{class_id}/events'.format(class_id='class_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_events_for_competition(client):
    """Test case for get_events_for_competition

    Retrieves a list of events for a given competition id.
    """
    params = [('isPublished', 'true'),
                    ('fields', ['fields_example']),
                    ('include', ['include_example']),
                    ('exclude', ['exclude_example']),
                    ('displayed', 'true'),
                    ('channel', 'channel_example'),
                    ('settled', True),
                    ('includeEmpty', True),
                    ('status', 'status_example'),
                    ('sort', 'id,asc'),
                    ('offset', 0),
                    ('limit', 100),
                    ('headlineSummary', False),
                    ('includeAllDescendants', False),
                    ('isInPlay', True),
                    ('marketCount', 1),
                    ('date', '_date_example'),
                    ('dateFrom', 'date_from_example'),
                    ('dateTo', 'date_to_example'),
                    ('marketGroupId', 'market_group_id_example'),
                    ('eventSort', 'event_sort_example'),
                    ('culture', 'culture_example'),
                    ('marketPublished', 'true'),
                    ('marketStatus', 'market_status_example'),
                    ('marketDisplayed', 'true'),
                    ('marketChannel', 'market_channel_example'),
                    ('marketSort', 'market_sort_example'),
                    ('marketEW', 'market_ew_example'),
                    ('selectionStatus', 'selection_status_example'),
                    ('selectionChannel', 'selection_channel_example'),
                    ('selectionPublished', 'true')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/sportsdata/competitions/{competition_id}/events'.format(competition_id='competition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_market_groups_for_competition(client):
    """Test case for get_market_groups_for_competition

    Retrieves a list of market groups for a given competition id
    """
    params = [('fields', ['fields_example']),
                    ('include', ['include_example']),
                    ('exclude', ['exclude_example']),
                    ('sort', 'id,asc'),
                    ('offset', 0),
                    ('limit', 100),
                    ('culture', 'culture_example'),
                    ('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/sportsdata/competitions/{competition_id}/marketgroups'.format(competition_id='competition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_markets(client):
    """Test case for get_markets

    Gets one or more specific markets
    """
    params = [('ids', ['ids_example']),
                    ('includeAllDescendants', False),
                    ('fields', ['fields_example']),
                    ('include', ['include_example']),
                    ('exclude', ['exclude_example']),
                    ('includeEmpty', True),
                    ('culture', 'culture_example'),
                    ('marketPublished', 'true'),
                    ('marketStatus', 'market_status_example'),
                    ('marketDisplayed', 'true'),
                    ('marketChannel', 'market_channel_example'),
                    ('marketSort', 'market_sort_example'),
                    ('marketEW', 'market_ew_example'),
                    ('selectionStatus', 'selection_status_example'),
                    ('selectionChannel', 'selection_channel_example'),
                    ('selectionPublished', 'true')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/sportsdata/events/{event_id}/markets'.format(event_id='event_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_markets_by_group_id(client):
    """Test case for get_markets_by_group_id

    Retrieves a list of events/markets/selections where markets within said event match selected sort/groupId
    """
    params = [('fields', ['fields_example']),
                    ('include', ['include_example']),
                    ('exclude', ['exclude_example']),
                    ('marketSort', 'market_sort_example'),
                    ('marketGroupId', 'market_group_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/sportsdata/competitions/{competition_id}/marketsByGroupid'.format(competition_id='competition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_selections(client):
    """Test case for get_selections

    Gets one or more selections for a market
    """
    params = [('ids', ['ids_example']),
                    ('fields', ['fields_example']),
                    ('include', ['include_example']),
                    ('exclude', ['exclude_example']),
                    ('culture', 'culture_example'),
                    ('selectionStatus', 'selection_status_example'),
                    ('selectionChannel', 'selection_channel_example'),
                    ('selectionPublished', 'true')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/sportsdata/events/{event_id}/markets/{market_id}/selections'.format(event_id='event_id_example', market_id='market_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sports(client):
    """Test case for get_sports

    Gets a list of all sports
    """
    params = [('sort', 'id,asc'),
                    ('offset', 0),
                    ('isPublished', 'true'),
                    ('limit', 100),
                    ('fields', ['fields_example']),
                    ('include', ['include_example']),
                    ('exclude', ['exclude_example']),
                    ('culture', 'culture_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/sportsdata/sports/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_top_bets(client):
    """Test case for get_top_bets

    Retrieves a weighted list of Selections.
    """
    params = [('sportIds', ['sport_ids_example']),
                    ('competitionIds', ['competition_ids_example']),
                    ('limit', 100),
                    ('fields', ['fields_example']),
                    ('include', ['include_example']),
                    ('exclude', ['exclude_example']),
                    ('param_topBetEventId', 'param_top_bet_event_id_example'),
                    ('sortName', 'sort_name_example'),
                    ('culture', 'culture_example'),
                    ('Locale', 'locale_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/sportsdata/topbets/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

