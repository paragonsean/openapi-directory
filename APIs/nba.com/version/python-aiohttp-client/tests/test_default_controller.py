# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_allstarballotpredictor_get(client):
    """Test case for allstarballotpredictor_get

    
    """
    params = [('PointCap', 'point_cap_example'),
                    ('WestPlayer1', 'west_player1_example'),
                    ('WestPlayer2', 'west_player2_example'),
                    ('WestPlayer3', 'west_player3_example'),
                    ('WestPlayer4', 'west_player4_example'),
                    ('WestPlayer5', 'west_player5_example'),
                    ('EastPlayer1', 'east_player1_example'),
                    ('EastPlayer2', 'east_player2_example'),
                    ('EastPlayer3', 'east_player3_example'),
                    ('EastPlayer4', 'east_player4_example'),
                    ('EastPlayer5', 'east_player5_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/allstarballotpredictor',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_boxscore_get(client):
    """Test case for boxscore_get

    
    """
    params = [('GameID', 'game_id_example'),
                    ('StartPeriod', 'start_period_example'),
                    ('EndPeriod', 'end_period_example'),
                    ('StartRange', 'start_range_example'),
                    ('EndRange', 'end_range_example'),
                    ('RangeType', 'range_type_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/boxscore',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_boxscoreadvanced_get(client):
    """Test case for boxscoreadvanced_get

    
    """
    params = [('GameID', 'game_id_example'),
                    ('StartPeriod', 'start_period_example'),
                    ('EndPeriod', 'end_period_example'),
                    ('StartRange', 'start_range_example'),
                    ('EndRange', 'end_range_example'),
                    ('RangeType', 'range_type_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/boxscoreadvanced',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_boxscoreadvancedv2_get(client):
    """Test case for boxscoreadvancedv2_get

    
    """
    params = [('GameID', 'game_id_example'),
                    ('StartPeriod', 'start_period_example'),
                    ('EndPeriod', 'end_period_example'),
                    ('StartRange', 'start_range_example'),
                    ('EndRange', 'end_range_example'),
                    ('RangeType', 'range_type_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/boxscoreadvancedv2',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_boxscorefourfactors_get(client):
    """Test case for boxscorefourfactors_get

    
    """
    params = [('GameID', 'game_id_example'),
                    ('StartPeriod', 'start_period_example'),
                    ('EndPeriod', 'end_period_example'),
                    ('StartRange', 'start_range_example'),
                    ('EndRange', 'end_range_example'),
                    ('RangeType', 'range_type_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/boxscorefourfactors',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_boxscorefourfactorsv2_get(client):
    """Test case for boxscorefourfactorsv2_get

    
    """
    params = [('GameID', 'game_id_example'),
                    ('StartPeriod', 'start_period_example'),
                    ('EndPeriod', 'end_period_example'),
                    ('StartRange', 'start_range_example'),
                    ('EndRange', 'end_range_example'),
                    ('RangeType', 'range_type_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/boxscorefourfactorsv2',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_boxscoremisc_get(client):
    """Test case for boxscoremisc_get

    
    """
    params = [('GameID', 'game_id_example'),
                    ('StartPeriod', 'start_period_example'),
                    ('EndPeriod', 'end_period_example'),
                    ('StartRange', 'start_range_example'),
                    ('EndRange', 'end_range_example'),
                    ('RangeType', 'range_type_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/boxscoremisc',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_boxscoremiscv2_get(client):
    """Test case for boxscoremiscv2_get

    
    """
    params = [('GameID', 'game_id_example'),
                    ('StartPeriod', 'start_period_example'),
                    ('EndPeriod', 'end_period_example'),
                    ('StartRange', 'start_range_example'),
                    ('EndRange', 'end_range_example'),
                    ('RangeType', 'range_type_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/boxscoremiscv2',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_boxscoreplayertrackv2_get(client):
    """Test case for boxscoreplayertrackv2_get

    
    """
    params = [('GameID', 'game_id_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/boxscoreplayertrackv2',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_boxscorescoring_get(client):
    """Test case for boxscorescoring_get

    
    """
    params = [('GameID', 'game_id_example'),
                    ('StartPeriod', 'start_period_example'),
                    ('EndPeriod', 'end_period_example'),
                    ('StartRange', 'start_range_example'),
                    ('EndRange', 'end_range_example'),
                    ('RangeType', 'range_type_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/boxscorescoring',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_boxscorescoringv2_get(client):
    """Test case for boxscorescoringv2_get

    
    """
    params = [('GameID', 'game_id_example'),
                    ('StartPeriod', 'start_period_example'),
                    ('EndPeriod', 'end_period_example'),
                    ('StartRange', 'start_range_example'),
                    ('EndRange', 'end_range_example'),
                    ('RangeType', 'range_type_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/boxscorescoringv2',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_boxscoresummaryv2_get(client):
    """Test case for boxscoresummaryv2_get

    
    """
    params = [('GameID', 'game_id_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/boxscoresummaryv2',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_boxscoretraditionalv2_get(client):
    """Test case for boxscoretraditionalv2_get

    
    """
    params = [('GameID', 'game_id_example'),
                    ('StartPeriod', 'start_period_example'),
                    ('EndPeriod', 'end_period_example'),
                    ('StartRange', 'start_range_example'),
                    ('EndRange', 'end_range_example'),
                    ('RangeType', 'range_type_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/boxscoretraditionalv2',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_boxscoreusage_get(client):
    """Test case for boxscoreusage_get

    
    """
    params = [('GameID', 'game_id_example'),
                    ('StartPeriod', 'start_period_example'),
                    ('EndPeriod', 'end_period_example'),
                    ('StartRange', 'start_range_example'),
                    ('EndRange', 'end_range_example'),
                    ('RangeType', 'range_type_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/boxscoreusage',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_boxscoreusagev2_get(client):
    """Test case for boxscoreusagev2_get

    
    """
    params = [('GameID', 'game_id_example'),
                    ('StartPeriod', 'start_period_example'),
                    ('EndPeriod', 'end_period_example'),
                    ('StartRange', 'start_range_example'),
                    ('EndRange', 'end_range_example'),
                    ('RangeType', 'range_type_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/boxscoreusagev2',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_common_team_years_get(client):
    """Test case for common_team_years_get

    
    """
    params = [('LeagueID', 'league_id_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/commonTeamYears',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_commonallplayers_get(client):
    """Test case for commonallplayers_get

    
    """
    params = [('LeagueID', 'league_id_example'),
                    ('Season', 'season_example'),
                    ('IsOnlyCurrentSeason', 'is_only_current_season_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/commonallplayers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_commonplayerinfo_get(client):
    """Test case for commonplayerinfo_get

    
    """
    params = [('PlayerID', 'player_id_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/commonplayerinfo',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_commonplayoffseries_get(client):
    """Test case for commonplayoffseries_get

    
    """
    params = [('LeagueID', 'league_id_example'),
                    ('Season', 'season_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/commonplayoffseries',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_commonteamroster_get(client):
    """Test case for commonteamroster_get

    
    """
    params = [('Season', 'season_example'),
                    ('TeamID', 'team_id_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/commonteamroster',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_draftcombinedrillresults_get(client):
    """Test case for draftcombinedrillresults_get

    
    """
    params = [('LeagueID', 'league_id_example'),
                    ('SeasonYear', 'season_year_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/draftcombinedrillresults',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_draftcombinenonstationaryshooting_get(client):
    """Test case for draftcombinenonstationaryshooting_get

    
    """
    params = [('LeagueID', 'league_id_example'),
                    ('SeasonYear', 'season_year_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/draftcombinenonstationaryshooting',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_draftcombineplayeranthro_get(client):
    """Test case for draftcombineplayeranthro_get

    
    """
    params = [('LeagueID', 'league_id_example'),
                    ('SeasonYear', 'season_year_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/draftcombineplayeranthro',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_draftcombinespotshooting_get(client):
    """Test case for draftcombinespotshooting_get

    
    """
    params = [('LeagueID', 'league_id_example'),
                    ('SeasonYear', 'season_year_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/draftcombinespotshooting',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_draftcombinestats_get(client):
    """Test case for draftcombinestats_get

    
    """
    params = [('LeagueID', 'league_id_example'),
                    ('SeasonYear', 'season_year_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/draftcombinestats',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drafthistory_get(client):
    """Test case for drafthistory_get

    
    """
    params = [('LeagueID', 'league_id_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/drafthistory',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_franchisehistory_get(client):
    """Test case for franchisehistory_get

    
    """
    params = [('LeagueID', 'league_id_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/franchisehistory',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_homepageleaders_get(client):
    """Test case for homepageleaders_get

    
    """
    params = [('StatCategory', 'stat_category_example'),
                    ('LeagueID', 'league_id_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('PlayerOrTeam', 'player_or_team_example'),
                    ('Game', 'game_example'),
                    ('Player', 'player_example'),
                    ('PlayerScope', 'player_scope_example'),
                    ('GameScope', 'game_scope_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/homepageleaders',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_homepagev2_get(client):
    """Test case for homepagev2_get

    
    """
    params = [('StatType', 'stat_type_example'),
                    ('LeagueID', 'league_id_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('PlayerOrTeam', 'player_or_team_example'),
                    ('Game', 'game_example'),
                    ('Player', 'player_example'),
                    ('PlayerScope', 'player_scope_example'),
                    ('GameScope', 'game_scope_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/homepagev2',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_leaderstiles_get(client):
    """Test case for leaderstiles_get

    
    """
    params = [('Stat', 'stat_example'),
                    ('LeagueID', 'league_id_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('PlayerOrTeam', 'player_or_team_example'),
                    ('Game', 'game_example'),
                    ('Player', 'player_example'),
                    ('PlayerScope', 'player_scope_example'),
                    ('GameScope', 'game_scope_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/leaderstiles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_leaguedashlineups_get(client):
    """Test case for leaguedashlineups_get

    
    """
    params = [('GroupQuantity', 'group_quantity_example'),
                    ('SeasonType', 'season_type_example'),
                    ('MeasureType', 'measure_type_example'),
                    ('PerMode', 'per_mode_example'),
                    ('PlusMinus', 'plus_minus_example'),
                    ('PaceAdjust', 'pace_adjust_example'),
                    ('Rank', 'rank_example'),
                    ('Season', 'season_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/leaguedashlineups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_leaguedashplayerbiostats_get(client):
    """Test case for leaguedashplayerbiostats_get

    
    """
    params = [('PerMode', 'per_mode_example'),
                    ('LeagueID', 'league_id_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/leaguedashplayerbiostats',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_leaguedashplayerclutch_get(client):
    """Test case for leaguedashplayerclutch_get

    
    """
    params = [('ClutchTime', 'clutch_time_example'),
                    ('AheadBehind', 'ahead_behind_example'),
                    ('PointDiff', 'point_diff_example'),
                    ('GameScope', 'game_scope_example'),
                    ('PlayerExperience', 'player_experience_example'),
                    ('PlayerPosition', 'player_position_example'),
                    ('StarterBench', 'starter_bench_example'),
                    ('MeasureType', 'measure_type_example'),
                    ('PerMode', 'per_mode_example'),
                    ('PlusMinus', 'plus_minus_example'),
                    ('PaceAdjust', 'pace_adjust_example'),
                    ('Rank', 'rank_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/leaguedashplayerclutch',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_leaguedashplayerptshot_get(client):
    """Test case for leaguedashplayerptshot_get

    
    """
    params = [('LeagueID', 'league_id_example'),
                    ('PerMode', 'per_mode_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/leaguedashplayerptshot',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_leaguedashplayershotlocations_get(client):
    """Test case for leaguedashplayershotlocations_get

    
    """
    params = [('MeasureType', 'measure_type_example'),
                    ('PerMode', 'per_mode_example'),
                    ('PlusMinus', 'plus_minus_example'),
                    ('PaceAdjust', 'pace_adjust_example'),
                    ('Rank', 'rank_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example'),
                    ('DistanceRange', 'distance_range_example'),
                    ('GameScope', 'game_scope_example'),
                    ('PlayerExperience', 'player_experience_example'),
                    ('PlayerPosition', 'player_position_example'),
                    ('StarterBench', 'starter_bench_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/leaguedashplayershotlocations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_leaguedashplayerstats_get(client):
    """Test case for leaguedashplayerstats_get

    
    """
    params = [('GameScope', 'game_scope_example'),
                    ('PlayerExperience', 'player_experience_example'),
                    ('PlayerPosition', 'player_position_example'),
                    ('StarterBench', 'starter_bench_example'),
                    ('MeasureType', 'measure_type_example'),
                    ('PerMode', 'per_mode_example'),
                    ('PlusMinus', 'plus_minus_example'),
                    ('PaceAdjust', 'pace_adjust_example'),
                    ('Rank', 'rank_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/leaguedashplayerstats',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_leaguedashptdefend_get(client):
    """Test case for leaguedashptdefend_get

    
    """
    params = [('LeagueID', 'league_id_example'),
                    ('PerMode', 'per_mode_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('DefenseCategory', 'defense_category_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/leaguedashptdefend',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_leaguedashptteamdefend_get(client):
    """Test case for leaguedashptteamdefend_get

    
    """
    params = [('LeagueID', 'league_id_example'),
                    ('PerMode', 'per_mode_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('DefenseCategory', 'defense_category_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/leaguedashptteamdefend',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_leaguedashteamclutch_get(client):
    """Test case for leaguedashteamclutch_get

    
    """
    params = [('ClutchTime', 'clutch_time_example'),
                    ('AheadBehind', 'ahead_behind_example'),
                    ('PointDiff', 'point_diff_example'),
                    ('GameScope', 'game_scope_example'),
                    ('PlayerExperience', 'player_experience_example'),
                    ('PlayerPosition', 'player_position_example'),
                    ('StarterBench', 'starter_bench_example'),
                    ('MeasureType', 'measure_type_example'),
                    ('PerMode', 'per_mode_example'),
                    ('PlusMinus', 'plus_minus_example'),
                    ('PaceAdjust', 'pace_adjust_example'),
                    ('Rank', 'rank_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/leaguedashteamclutch',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_leaguedashteamptshot_get(client):
    """Test case for leaguedashteamptshot_get

    
    """
    params = [('LeagueID', 'league_id_example'),
                    ('PerMode', 'per_mode_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/leaguedashteamptshot',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_leaguedashteamshotlocations_get(client):
    """Test case for leaguedashteamshotlocations_get

    
    """
    params = [('MeasureType', 'measure_type_example'),
                    ('PerMode', 'per_mode_example'),
                    ('PlusMinus', 'plus_minus_example'),
                    ('PaceAdjust', 'pace_adjust_example'),
                    ('Rank', 'rank_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example'),
                    ('DistanceRange', 'distance_range_example'),
                    ('GameScope', 'game_scope_example'),
                    ('PlayerExperience', 'player_experience_example'),
                    ('PlayerPosition', 'player_position_example'),
                    ('StarterBench', 'starter_bench_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/leaguedashteamshotlocations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_leaguedashteamstats_get(client):
    """Test case for leaguedashteamstats_get

    
    """
    params = [('MeasureType', 'measure_type_example'),
                    ('PerMode', 'per_mode_example'),
                    ('PlusMinus', 'plus_minus_example'),
                    ('PaceAdjust', 'pace_adjust_example'),
                    ('Rank', 'rank_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/leaguedashteamstats',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_leagueleaders_get(client):
    """Test case for leagueleaders_get

    
    """
    params = [('LeagueID', 'league_id_example'),
                    ('PerMode', 'per_mode_example'),
                    ('StatCategory', 'stat_category_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('Scope', 'scope_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/leagueleaders',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_playbyplay_get(client):
    """Test case for playbyplay_get

    
    """
    params = [('GameID', 'game_id_example'),
                    ('StartPeriod', 'start_period_example'),
                    ('EndPeriod', 'end_period_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/playbyplay',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_playbyplayv2_get(client):
    """Test case for playbyplayv2_get

    
    """
    params = [('GameID', 'game_id_example'),
                    ('StartPeriod', 'start_period_example'),
                    ('EndPeriod', 'end_period_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/playbyplayv2',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_playercareerstats_get(client):
    """Test case for playercareerstats_get

    
    """
    params = [('PerMode', 'per_mode_example'),
                    ('PlayerID', 'player_id_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/playercareerstats',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_playercompare_get(client):
    """Test case for playercompare_get

    
    """
    params = [('PlayerIDList', 'player_id_list_example'),
                    ('VsPlayerIDList', 'vs_player_id_list_example'),
                    ('SeasonType', 'season_type_example'),
                    ('MeasureType', 'measure_type_example'),
                    ('PerMode', 'per_mode_example'),
                    ('PlusMinus', 'plus_minus_example'),
                    ('PaceAdjust', 'pace_adjust_example'),
                    ('Rank', 'rank_example'),
                    ('Season', 'season_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/playercompare',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_playerdashboardbyclutch_get(client):
    """Test case for playerdashboardbyclutch_get

    
    """
    params = [('MeasureType', 'measure_type_example'),
                    ('PerMode', 'per_mode_example'),
                    ('PlusMinus', 'plus_minus_example'),
                    ('PaceAdjust', 'pace_adjust_example'),
                    ('Rank', 'rank_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('PlayerID', 'player_id_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/playerdashboardbyclutch',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_playerdashboardbygamesplits_get(client):
    """Test case for playerdashboardbygamesplits_get

    
    """
    params = [('MeasureType', 'measure_type_example'),
                    ('PerMode', 'per_mode_example'),
                    ('PlusMinus', 'plus_minus_example'),
                    ('PaceAdjust', 'pace_adjust_example'),
                    ('Rank', 'rank_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('PlayerID', 'player_id_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/playerdashboardbygamesplits',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_playerdashboardbygeneralsplits_get(client):
    """Test case for playerdashboardbygeneralsplits_get

    
    """
    params = [('MeasureType', 'measure_type_example'),
                    ('PerMode', 'per_mode_example'),
                    ('PlusMinus', 'plus_minus_example'),
                    ('PaceAdjust', 'pace_adjust_example'),
                    ('Rank', 'rank_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('PlayerID', 'player_id_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/playerdashboardbygeneralsplits',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_playerdashboardbylastngames_get(client):
    """Test case for playerdashboardbylastngames_get

    
    """
    params = [('MeasureType', 'measure_type_example'),
                    ('PerMode', 'per_mode_example'),
                    ('PlusMinus', 'plus_minus_example'),
                    ('PaceAdjust', 'pace_adjust_example'),
                    ('Rank', 'rank_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('PlayerID', 'player_id_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/playerdashboardbylastngames',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_playerdashboardbyopponent_get(client):
    """Test case for playerdashboardbyopponent_get

    
    """
    params = [('MeasureType', 'measure_type_example'),
                    ('PerMode', 'per_mode_example'),
                    ('PlusMinus', 'plus_minus_example'),
                    ('PaceAdjust', 'pace_adjust_example'),
                    ('Rank', 'rank_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('PlayerID', 'player_id_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/playerdashboardbyopponent',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_playerdashboardbyshootingsplits_get(client):
    """Test case for playerdashboardbyshootingsplits_get

    
    """
    params = [('MeasureType', 'measure_type_example'),
                    ('PerMode', 'per_mode_example'),
                    ('PlusMinus', 'plus_minus_example'),
                    ('PaceAdjust', 'pace_adjust_example'),
                    ('Rank', 'rank_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('PlayerID', 'player_id_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/playerdashboardbyshootingsplits',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_playerdashboardbyteamperformance_get(client):
    """Test case for playerdashboardbyteamperformance_get

    
    """
    params = [('MeasureType', 'measure_type_example'),
                    ('PerMode', 'per_mode_example'),
                    ('PlusMinus', 'plus_minus_example'),
                    ('PaceAdjust', 'pace_adjust_example'),
                    ('Rank', 'rank_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('PlayerID', 'player_id_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/playerdashboardbyteamperformance',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_playerdashboardbyyearoveryear_get(client):
    """Test case for playerdashboardbyyearoveryear_get

    
    """
    params = [('MeasureType', 'measure_type_example'),
                    ('PerMode', 'per_mode_example'),
                    ('PlusMinus', 'plus_minus_example'),
                    ('PaceAdjust', 'pace_adjust_example'),
                    ('Rank', 'rank_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('PlayerID', 'player_id_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/playerdashboardbyyearoveryear',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_playerdashptpass_get(client):
    """Test case for playerdashptpass_get

    
    """
    params = [('PerMode', 'per_mode_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('PlayerID', 'player_id_example'),
                    ('TeamID', 'team_id_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/playerdashptpass',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_playerdashptreb_get(client):
    """Test case for playerdashptreb_get

    
    """
    params = [('PerMode', 'per_mode_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('PlayerID', 'player_id_example'),
                    ('TeamID', 'team_id_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/playerdashptreb',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_playerdashptreboundlogs_get(client):
    """Test case for playerdashptreboundlogs_get

    
    """
    params = [('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('PlayerID', 'player_id_example'),
                    ('TeamID', 'team_id_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/playerdashptreboundlogs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_playerdashptshotdefend_get(client):
    """Test case for playerdashptshotdefend_get

    
    """
    params = [('PerMode', 'per_mode_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('PlayerID', 'player_id_example'),
                    ('TeamID', 'team_id_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/playerdashptshotdefend',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_playerdashptshotlog_get(client):
    """Test case for playerdashptshotlog_get

    
    """
    params = [('LeagueID', 'league_id_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('PlayerID', 'player_id_example'),
                    ('TeamID', 'team_id_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/playerdashptshotlog',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_playerdashptshots_get(client):
    """Test case for playerdashptshots_get

    
    """
    params = [('PerMode', 'per_mode_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('PlayerID', 'player_id_example'),
                    ('TeamID', 'team_id_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/playerdashptshots',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_playergamelog_get(client):
    """Test case for playergamelog_get

    
    """
    params = [('PlayerID', 'player_id_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/playergamelog',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_playerprofile_get(client):
    """Test case for playerprofile_get

    
    """
    params = [('LeagueID', 'league_id_example'),
                    ('PlayerID', 'player_id_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('GraphStartSeason', 'graph_start_season_example'),
                    ('GraphEndSeason', 'graph_end_season_example'),
                    ('GraphStat', 'graph_stat_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/playerprofile',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_playerprofilev2_get(client):
    """Test case for playerprofilev2_get

    
    """
    params = [('PerMode', 'per_mode_example'),
                    ('PlayerID', 'player_id_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/playerprofilev2',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_playersvsplayers_get(client):
    """Test case for playersvsplayers_get

    
    """
    params = [('PlayerTeamID', 'player_team_id_example'),
                    ('PlayerID1', 'player_id1_example'),
                    ('PlayerID2', 'player_id2_example'),
                    ('PlayerID3', 'player_id3_example'),
                    ('PlayerID4', 'player_id4_example'),
                    ('PlayerID5', 'player_id5_example'),
                    ('VsTeamID', 'vs_team_id_example'),
                    ('VsPlayerID1', 'vs_player_id1_example'),
                    ('VsPlayerID2', 'vs_player_id2_example'),
                    ('VsPlayerID3', 'vs_player_id3_example'),
                    ('VsPlayerID4', 'vs_player_id4_example'),
                    ('VsPlayerID5', 'vs_player_id5_example'),
                    ('SeasonType', 'season_type_example'),
                    ('MeasureType', 'measure_type_example'),
                    ('PerMode', 'per_mode_example'),
                    ('PlusMinus', 'plus_minus_example'),
                    ('PaceAdjust', 'pace_adjust_example'),
                    ('Rank', 'rank_example'),
                    ('Season', 'season_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/playersvsplayers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_playervsplayer_get(client):
    """Test case for playervsplayer_get

    
    """
    params = [('PlayerID', 'player_id_example'),
                    ('VsPlayerID', 'vs_player_id_example'),
                    ('SeasonType', 'season_type_example'),
                    ('MeasureType', 'measure_type_example'),
                    ('PerMode', 'per_mode_example'),
                    ('PlusMinus', 'plus_minus_example'),
                    ('PaceAdjust', 'pace_adjust_example'),
                    ('Rank', 'rank_example'),
                    ('Season', 'season_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/playervsplayer',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_playoffpicture_get(client):
    """Test case for playoffpicture_get

    
    """
    params = [('LeagueID', 'league_id_example'),
                    ('SeasonID', 'season_id_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/playoffpicture',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_scoreboard_get(client):
    """Test case for scoreboard_get

    
    """
    params = [('GameDate', 'game_date_example'),
                    ('LeagueID', 'league_id_example'),
                    ('DayOffset', 'day_offset_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/scoreboard',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_scoreboard_v2_get(client):
    """Test case for scoreboard_v2_get

    
    """
    params = [('GameDate', 'game_date_example'),
                    ('LeagueID', 'league_id_example'),
                    ('DayOffset', 'day_offset_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/scoreboardV2',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shotchartdetail_get(client):
    """Test case for shotchartdetail_get

    
    """
    params = [('SeasonType', 'season_type_example'),
                    ('TeamID', 'team_id_example'),
                    ('PlayerID', 'player_id_example'),
                    ('GameID', 'game_id_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('Position', 'position_example'),
                    ('RookieYear', 'rookie_year_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example'),
                    ('ContextMeasure', 'context_measure_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/shotchartdetail',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shotchartlineupdetail_get(client):
    """Test case for shotchartlineupdetail_get

    
    """
    params = [('LeagueID', 'league_id_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('TeamID', 'team_id_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example'),
                    ('GameID', 'game_id_example'),
                    ('GROUP_ID', 'group_id_example'),
                    ('ContextMeasure', 'context_measure_example'),
                    ('ContextFilter', 'context_filter_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/shotchartlineupdetail',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teamdashboardbyclutch_get(client):
    """Test case for teamdashboardbyclutch_get

    
    """
    params = [('TeamID', 'team_id_example'),
                    ('MeasureType', 'measure_type_example'),
                    ('PerMode', 'per_mode_example'),
                    ('PlusMinus', 'plus_minus_example'),
                    ('PaceAdjust', 'pace_adjust_example'),
                    ('Rank', 'rank_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/teamdashboardbyclutch',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teamdashboardbygamesplits_get(client):
    """Test case for teamdashboardbygamesplits_get

    
    """
    params = [('TeamID', 'team_id_example'),
                    ('MeasureType', 'measure_type_example'),
                    ('PerMode', 'per_mode_example'),
                    ('PlusMinus', 'plus_minus_example'),
                    ('PaceAdjust', 'pace_adjust_example'),
                    ('Rank', 'rank_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/teamdashboardbygamesplits',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teamdashboardbygeneralsplits_get(client):
    """Test case for teamdashboardbygeneralsplits_get

    
    """
    params = [('SeasonType', 'season_type_example'),
                    ('TeamID', 'team_id_example'),
                    ('MeasureType', 'measure_type_example'),
                    ('PerMode', 'per_mode_example'),
                    ('PlusMinus', 'plus_minus_example'),
                    ('PaceAdjust', 'pace_adjust_example'),
                    ('Rank', 'rank_example'),
                    ('Season', 'season_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/teamdashboardbygeneralsplits',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teamdashboardbylastngames_get(client):
    """Test case for teamdashboardbylastngames_get

    
    """
    params = [('TeamID', 'team_id_example'),
                    ('MeasureType', 'measure_type_example'),
                    ('PerMode', 'per_mode_example'),
                    ('PlusMinus', 'plus_minus_example'),
                    ('PaceAdjust', 'pace_adjust_example'),
                    ('Rank', 'rank_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/teamdashboardbylastngames',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teamdashboardbyopponent_get(client):
    """Test case for teamdashboardbyopponent_get

    
    """
    params = [('TeamID', 'team_id_example'),
                    ('MeasureType', 'measure_type_example'),
                    ('PerMode', 'per_mode_example'),
                    ('PlusMinus', 'plus_minus_example'),
                    ('PaceAdjust', 'pace_adjust_example'),
                    ('Rank', 'rank_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/teamdashboardbyopponent',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teamdashboardbyshootingsplits_get(client):
    """Test case for teamdashboardbyshootingsplits_get

    
    """
    params = [('TeamID', 'team_id_example'),
                    ('MeasureType', 'measure_type_example'),
                    ('PerMode', 'per_mode_example'),
                    ('PlusMinus', 'plus_minus_example'),
                    ('PaceAdjust', 'pace_adjust_example'),
                    ('Rank', 'rank_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/teamdashboardbyshootingsplits',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teamdashboardbyteamperformance_get(client):
    """Test case for teamdashboardbyteamperformance_get

    
    """
    params = [('TeamID', 'team_id_example'),
                    ('MeasureType', 'measure_type_example'),
                    ('PerMode', 'per_mode_example'),
                    ('PlusMinus', 'plus_minus_example'),
                    ('PaceAdjust', 'pace_adjust_example'),
                    ('Rank', 'rank_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/teamdashboardbyteamperformance',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teamdashboardbyyearoveryear_get(client):
    """Test case for teamdashboardbyyearoveryear_get

    
    """
    params = [('TeamID', 'team_id_example'),
                    ('MeasureType', 'measure_type_example'),
                    ('PerMode', 'per_mode_example'),
                    ('PlusMinus', 'plus_minus_example'),
                    ('PaceAdjust', 'pace_adjust_example'),
                    ('Rank', 'rank_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/teamdashboardbyyearoveryear',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teamdashlineups_get(client):
    """Test case for teamdashlineups_get

    
    """
    params = [('GroupQuantity', 'group_quantity_example'),
                    ('GameID', 'game_id_example'),
                    ('SeasonType', 'season_type_example'),
                    ('TeamID', 'team_id_example'),
                    ('MeasureType', 'measure_type_example'),
                    ('PerMode', 'per_mode_example'),
                    ('PlusMinus', 'plus_minus_example'),
                    ('PaceAdjust', 'pace_adjust_example'),
                    ('Rank', 'rank_example'),
                    ('Season', 'season_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/teamdashlineups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teamdashptpass_get(client):
    """Test case for teamdashptpass_get

    
    """
    params = [('PerMode', 'per_mode_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('TeamID', 'team_id_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/teamdashptpass',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teamdashptreb_get(client):
    """Test case for teamdashptreb_get

    
    """
    params = [('PerMode', 'per_mode_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('TeamID', 'team_id_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/teamdashptreb',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teamdashptshots_get(client):
    """Test case for teamdashptshots_get

    
    """
    params = [('PerMode', 'per_mode_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('TeamID', 'team_id_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/teamdashptshots',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teamgamelog_get(client):
    """Test case for teamgamelog_get

    
    """
    params = [('TeamID', 'team_id_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/teamgamelog',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teaminfocommon_get(client):
    """Test case for teaminfocommon_get

    
    """
    params = [('Season', 'season_example'),
                    ('TeamID', 'team_id_example'),
                    ('LeagueID', 'league_id_example'),
                    ('SeasonType', 'season_type_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/teaminfocommon',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teamplayerdashboard_get(client):
    """Test case for teamplayerdashboard_get

    
    """
    params = [('SeasonType', 'season_type_example'),
                    ('TeamID', 'team_id_example'),
                    ('MeasureType', 'measure_type_example'),
                    ('PerMode', 'per_mode_example'),
                    ('PlusMinus', 'plus_minus_example'),
                    ('PaceAdjust', 'pace_adjust_example'),
                    ('Rank', 'rank_example'),
                    ('Season', 'season_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/teamplayerdashboard',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teamplayeronoffdetails_get(client):
    """Test case for teamplayeronoffdetails_get

    
    """
    params = [('TeamID', 'team_id_example'),
                    ('MeasureType', 'measure_type_example'),
                    ('PerMode', 'per_mode_example'),
                    ('PlusMinus', 'plus_minus_example'),
                    ('PaceAdjust', 'pace_adjust_example'),
                    ('Rank', 'rank_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/teamplayeronoffdetails',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teamplayeronoffsummary_get(client):
    """Test case for teamplayeronoffsummary_get

    
    """
    params = [('TeamID', 'team_id_example'),
                    ('MeasureType', 'measure_type_example'),
                    ('PerMode', 'per_mode_example'),
                    ('PlusMinus', 'plus_minus_example'),
                    ('PaceAdjust', 'pace_adjust_example'),
                    ('Rank', 'rank_example'),
                    ('Season', 'season_example'),
                    ('SeasonType', 'season_type_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/teamplayeronoffsummary',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teamvsplayer_get(client):
    """Test case for teamvsplayer_get

    
    """
    params = [('TeamID', 'team_id_example'),
                    ('VsPlayerID', 'vs_player_id_example'),
                    ('SeasonType', 'season_type_example'),
                    ('MeasureType', 'measure_type_example'),
                    ('PerMode', 'per_mode_example'),
                    ('PlusMinus', 'plus_minus_example'),
                    ('PaceAdjust', 'pace_adjust_example'),
                    ('Rank', 'rank_example'),
                    ('Season', 'season_example'),
                    ('Outcome', 'outcome_example'),
                    ('Location', 'location_example'),
                    ('Month', 'month_example'),
                    ('SeasonSegment', 'season_segment_example'),
                    ('DateFrom', 'date_from_example'),
                    ('DateTo', 'date_to_example'),
                    ('OpponentTeamID', 'opponent_team_id_example'),
                    ('VsConference', 'vs_conference_example'),
                    ('VsDivision', 'vs_division_example'),
                    ('GameSegment', 'game_segment_example'),
                    ('Period', 'period_example'),
                    ('LastNGames', 'last_n_games_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/teamvsplayer',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teamyearbyyearstats_get(client):
    """Test case for teamyearbyyearstats_get

    
    """
    params = [('LeagueID', 'league_id_example'),
                    ('SeasonType', 'season_type_example'),
                    ('PerMode', 'per_mode_example'),
                    ('TeamID', 'team_id_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/teamyearbyyearstats',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_video_status_get(client):
    """Test case for video_status_get

    
    """
    params = [('LeagueID', 'league_id_example'),
                    ('GameDate', 'game_date_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/videoStatus',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

