# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_halo5_company(client):
    """Test case for halo5_company

    Halo 5 - Company
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/h5/companies/{company_id}'.format(company_id='company_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_halo5_company_commendations(client):
    """Test case for halo5_company_commendations

    Halo 5 - Company Commendations
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/h5/companies/{company_id}/commendations'.format(company_id='company_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_halo5_leaderboard_player_csr(client):
    """Test case for halo5_leaderboard_player_csr

    Halo 5 - Leaderboard - Player CSR
    """
    params = [('count', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/h5/player-leaderboards/csr/{season_id}/{playlist_id}'.format(season_id='season_id_example', playlist_id='playlist_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_halo5_match_events(client):
    """Test case for halo5_match_events

    Halo 5 - Match Events
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/h5/matches/{match_id}/events'.format(match_id='match_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_halo5_match_result_arena(client):
    """Test case for halo5_match_result_arena

    Halo 5 - Match Result - Arena
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/h5/arena/matches/{match_id}'.format(match_id='match_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_halo5_match_result_campaign(client):
    """Test case for halo5_match_result_campaign

    Halo 5 - Match Result - Campaign
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/h5/campaign/matches/{match_id}'.format(match_id='match_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_halo5_match_result_custom(client):
    """Test case for halo5_match_result_custom

    Halo 5 - Match Result - Custom
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/h5/custom/matches/{match_id}'.format(match_id='match_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_halo5_match_result_custom_local(client):
    """Test case for halo5_match_result_custom_local

    Halo 5 - Match Result - Custom Local
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/h5/customlocal/matches/{match_id}'.format(match_id='match_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_halo5_match_result_warzone(client):
    """Test case for halo5_match_result_warzone

    Halo 5 - Match Result - Warzone
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/h5/warzone/matches/{match_id}'.format(match_id='match_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_halo5_pc_match_result_custom(client):
    """Test case for halo5_pc_match_result_custom

    Halo 5 PC - Match Result - Custom
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/h5pc/custom/matches/{match_id}'.format(match_id='match_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_halo5_pc_player_match_history(client):
    """Test case for halo5_pc_player_match_history

    Halo 5 PC - Player Match History
    """
    params = [('modes', 'modes_example'),
                    ('start', 3.4),
                    ('count', 3.4),
                    ('include-times', True)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/h5pc/players/{player}/matches'.format(player='player_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_halo5_pc_player_service_records_custom(client):
    """Test case for halo5_pc_player_service_records_custom

    Halo 5 PC - Player Service Records - Custom
    """
    params = [('players', 'players_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/h5pc/servicerecords/custom',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_halo5_player_commendations(client):
    """Test case for halo5_player_commendations

    Halo 5 - Player Commendations
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/h5/players/{player}/commendations'.format(player='player_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_halo5_player_match_history(client):
    """Test case for halo5_player_match_history

    Halo 5 - Player Match History
    """
    params = [('modes', 'modes_example'),
                    ('start', 3.4),
                    ('count', 3.4),
                    ('include-times', True)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/h5/players/{player}/matches'.format(player='player_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_halo5_player_service_records_arena(client):
    """Test case for halo5_player_service_records_arena

    Halo 5 - Player Service Records - Arena
    """
    params = [('players', 'players_example'),
                    ('seasonId', 'season_id_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/h5/servicerecords/arena',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_halo5_player_service_records_campaign(client):
    """Test case for halo5_player_service_records_campaign

    Halo 5 - Player Service Records - Campaign
    """
    params = [('players', 'players_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/h5/servicerecords/campaign',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_halo5_player_service_records_custom(client):
    """Test case for halo5_player_service_records_custom

    Halo 5 - Player Service Records - Custom
    """
    params = [('players', 'players_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/h5/servicerecords/custom',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_halo5_player_service_records_custom_local(client):
    """Test case for halo5_player_service_records_custom_local

    Halo 5 - Player Service Records - Custom Local
    """
    params = [('players', 'players_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/h5/servicerecords/customlocal',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_halo5_player_service_records_warzone(client):
    """Test case for halo5_player_service_records_warzone

    Halo 5 - Player Service Records - Warzone
    """
    params = [('players', 'players_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/h5/servicerecords/warzone',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_halo_wars2_leaderboard_player_csr(client):
    """Test case for halo_wars2_leaderboard_player_csr

    Halo Wars 2 - Leaderboard - Player CSR
    """
    params = [('count', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/hw2/player-leaderboards/csr/{season_id}/{playlist_id}'.format(season_id='season_id_example', playlist_id='playlist_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_halo_wars2_match_events(client):
    """Test case for halo_wars2_match_events

    Halo Wars 2 - Match Events
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/hw2/matches/{match_id}/events'.format(match_id='match_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_halo_wars2_match_result(client):
    """Test case for halo_wars2_match_result

    Halo Wars 2 - Match Result
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/hw2/matches/{match_id}'.format(match_id='match_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_halo_wars2_player_campaign_progress(client):
    """Test case for halo_wars2_player_campaign_progress

    Halo Wars 2 - Player Campaign Progress
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/hw2/players/{player}/campaign-progress'.format(player='player_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_halo_wars2_player_match_history(client):
    """Test case for halo_wars2_player_match_history

    Halo Wars 2 - Player Match History
    """
    params = [('matchType', 'match_type_example'),
                    ('start', 3.4),
                    ('count', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/hw2/players/{player}/matches'.format(player='player_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_halo_wars2_player_playlist_ratings(client):
    """Test case for halo_wars2_player_playlist_ratings

    Halo Wars 2 - Player Playlist Ratings
    """
    params = [('players', 'players_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/hw2/playlist/{playlist_id}/rating'.format(playlist_id='playlist_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_halo_wars2_player_season_stats_summary(client):
    """Test case for halo_wars2_player_season_stats_summary

    Halo Wars 2 - Player Season Stats Summary
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/hw2/players/{player}/stats/seasons/{season_id}'.format(player='player_example', season_id='season_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_halo_wars2_player_stats_summary(client):
    """Test case for halo_wars2_player_stats_summary

    Halo Wars 2 - Player Stats Summary
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/hw2/players/{player}/stats'.format(player='player_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_halo_wars2_player_xps(client):
    """Test case for halo_wars2_player_xps

    Halo Wars 2 - Player XPs
    """
    params = [('players', 'players_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/hw2/xp',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

