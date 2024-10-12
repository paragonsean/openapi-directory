from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def allstarballotpredictor_get(request: web.Request, west_player1, west_player2, west_player3, west_player4, west_player5, east_player1, east_player2, east_player3, east_player4, east_player5, point_cap=None) -> web.Response:
    """allstarballotpredictor_get

    

    :param west_player1: 
    :type west_player1: str
    :param west_player2: 
    :type west_player2: str
    :param west_player3: 
    :type west_player3: str
    :param west_player4: 
    :type west_player4: str
    :param west_player5: 
    :type west_player5: str
    :param east_player1: 
    :type east_player1: str
    :param east_player2: 
    :type east_player2: str
    :param east_player3: 
    :type east_player3: str
    :param east_player4: 
    :type east_player4: str
    :param east_player5: 
    :type east_player5: str
    :param point_cap: 
    :type point_cap: str

    """
    return web.Response(status=200)


async def boxscore_get(request: web.Request, game_id=None, start_period=None, end_period=None, start_range=None, end_range=None, range_type=None) -> web.Response:
    """boxscore_get

    

    :param game_id: 
    :type game_id: str
    :param start_period: 
    :type start_period: str
    :param end_period: 
    :type end_period: str
    :param start_range: 
    :type start_range: str
    :param end_range: 
    :type end_range: str
    :param range_type: 
    :type range_type: str

    """
    return web.Response(status=200)


async def boxscoreadvanced_get(request: web.Request, game_id=None, start_period=None, end_period=None, start_range=None, end_range=None, range_type=None) -> web.Response:
    """boxscoreadvanced_get

    

    :param game_id: 
    :type game_id: str
    :param start_period: 
    :type start_period: str
    :param end_period: 
    :type end_period: str
    :param start_range: 
    :type start_range: str
    :param end_range: 
    :type end_range: str
    :param range_type: 
    :type range_type: str

    """
    return web.Response(status=200)


async def boxscoreadvancedv2_get(request: web.Request, game_id, start_period, end_period, start_range, end_range, range_type) -> web.Response:
    """boxscoreadvancedv2_get

    

    :param game_id: 
    :type game_id: str
    :param start_period: 
    :type start_period: str
    :param end_period: 
    :type end_period: str
    :param start_range: 
    :type start_range: str
    :param end_range: 
    :type end_range: str
    :param range_type: 
    :type range_type: str

    """
    return web.Response(status=200)


async def boxscorefourfactors_get(request: web.Request, game_id=None, start_period=None, end_period=None, start_range=None, end_range=None, range_type=None) -> web.Response:
    """boxscorefourfactors_get

    

    :param game_id: 
    :type game_id: str
    :param start_period: 
    :type start_period: str
    :param end_period: 
    :type end_period: str
    :param start_range: 
    :type start_range: str
    :param end_range: 
    :type end_range: str
    :param range_type: 
    :type range_type: str

    """
    return web.Response(status=200)


async def boxscorefourfactorsv2_get(request: web.Request, game_id, start_period, end_period, start_range, end_range, range_type) -> web.Response:
    """boxscorefourfactorsv2_get

    

    :param game_id: 
    :type game_id: str
    :param start_period: 
    :type start_period: str
    :param end_period: 
    :type end_period: str
    :param start_range: 
    :type start_range: str
    :param end_range: 
    :type end_range: str
    :param range_type: 
    :type range_type: str

    """
    return web.Response(status=200)


async def boxscoremisc_get(request: web.Request, game_id=None, start_period=None, end_period=None, start_range=None, end_range=None, range_type=None) -> web.Response:
    """boxscoremisc_get

    

    :param game_id: 
    :type game_id: str
    :param start_period: 
    :type start_period: str
    :param end_period: 
    :type end_period: str
    :param start_range: 
    :type start_range: str
    :param end_range: 
    :type end_range: str
    :param range_type: 
    :type range_type: str

    """
    return web.Response(status=200)


async def boxscoremiscv2_get(request: web.Request, game_id, start_period, end_period, start_range, end_range, range_type) -> web.Response:
    """boxscoremiscv2_get

    

    :param game_id: 
    :type game_id: str
    :param start_period: 
    :type start_period: str
    :param end_period: 
    :type end_period: str
    :param start_range: 
    :type start_range: str
    :param end_range: 
    :type end_range: str
    :param range_type: 
    :type range_type: str

    """
    return web.Response(status=200)


async def boxscoreplayertrackv2_get(request: web.Request, game_id) -> web.Response:
    """boxscoreplayertrackv2_get

    

    :param game_id: 
    :type game_id: str

    """
    return web.Response(status=200)


async def boxscorescoring_get(request: web.Request, game_id=None, start_period=None, end_period=None, start_range=None, end_range=None, range_type=None) -> web.Response:
    """boxscorescoring_get

    

    :param game_id: 
    :type game_id: str
    :param start_period: 
    :type start_period: str
    :param end_period: 
    :type end_period: str
    :param start_range: 
    :type start_range: str
    :param end_range: 
    :type end_range: str
    :param range_type: 
    :type range_type: str

    """
    return web.Response(status=200)


async def boxscorescoringv2_get(request: web.Request, game_id, start_period, end_period, start_range, end_range, range_type) -> web.Response:
    """boxscorescoringv2_get

    

    :param game_id: 
    :type game_id: str
    :param start_period: 
    :type start_period: str
    :param end_period: 
    :type end_period: str
    :param start_range: 
    :type start_range: str
    :param end_range: 
    :type end_range: str
    :param range_type: 
    :type range_type: str

    """
    return web.Response(status=200)


async def boxscoresummaryv2_get(request: web.Request, game_id) -> web.Response:
    """boxscoresummaryv2_get

    

    :param game_id: 
    :type game_id: str

    """
    return web.Response(status=200)


async def boxscoretraditionalv2_get(request: web.Request, game_id, start_period, end_period, start_range, end_range, range_type) -> web.Response:
    """boxscoretraditionalv2_get

    

    :param game_id: 
    :type game_id: str
    :param start_period: 
    :type start_period: str
    :param end_period: 
    :type end_period: str
    :param start_range: 
    :type start_range: str
    :param end_range: 
    :type end_range: str
    :param range_type: 
    :type range_type: str

    """
    return web.Response(status=200)


async def boxscoreusage_get(request: web.Request, game_id=None, start_period=None, end_period=None, start_range=None, end_range=None, range_type=None) -> web.Response:
    """boxscoreusage_get

    

    :param game_id: 
    :type game_id: str
    :param start_period: 
    :type start_period: str
    :param end_period: 
    :type end_period: str
    :param start_range: 
    :type start_range: str
    :param end_range: 
    :type end_range: str
    :param range_type: 
    :type range_type: str

    """
    return web.Response(status=200)


async def boxscoreusagev2_get(request: web.Request, game_id, start_period, end_period, start_range, end_range, range_type) -> web.Response:
    """boxscoreusagev2_get

    

    :param game_id: 
    :type game_id: str
    :param start_period: 
    :type start_period: str
    :param end_period: 
    :type end_period: str
    :param start_range: 
    :type start_range: str
    :param end_range: 
    :type end_range: str
    :param range_type: 
    :type range_type: str

    """
    return web.Response(status=200)


async def common_team_years_get(request: web.Request, league_id) -> web.Response:
    """common_team_years_get

    

    :param league_id: 
    :type league_id: str

    """
    return web.Response(status=200)


async def commonallplayers_get(request: web.Request, league_id, season, is_only_current_season) -> web.Response:
    """commonallplayers_get

    

    :param league_id: 
    :type league_id: str
    :param season: 
    :type season: str
    :param is_only_current_season: 
    :type is_only_current_season: str

    """
    return web.Response(status=200)


async def commonplayerinfo_get(request: web.Request, player_id) -> web.Response:
    """commonplayerinfo_get

    

    :param player_id: 
    :type player_id: str

    """
    return web.Response(status=200)


async def commonplayoffseries_get(request: web.Request, league_id, season) -> web.Response:
    """commonplayoffseries_get

    

    :param league_id: 
    :type league_id: str
    :param season: 
    :type season: str

    """
    return web.Response(status=200)


async def commonteamroster_get(request: web.Request, season, team_id) -> web.Response:
    """commonteamroster_get

    

    :param season: 
    :type season: str
    :param team_id: 
    :type team_id: str

    """
    return web.Response(status=200)


async def draftcombinedrillresults_get(request: web.Request, league_id, season_year) -> web.Response:
    """draftcombinedrillresults_get

    

    :param league_id: 
    :type league_id: str
    :param season_year: 
    :type season_year: str

    """
    return web.Response(status=200)


async def draftcombinenonstationaryshooting_get(request: web.Request, league_id, season_year) -> web.Response:
    """draftcombinenonstationaryshooting_get

    

    :param league_id: 
    :type league_id: str
    :param season_year: 
    :type season_year: str

    """
    return web.Response(status=200)


async def draftcombineplayeranthro_get(request: web.Request, league_id, season_year) -> web.Response:
    """draftcombineplayeranthro_get

    

    :param league_id: 
    :type league_id: str
    :param season_year: 
    :type season_year: str

    """
    return web.Response(status=200)


async def draftcombinespotshooting_get(request: web.Request, league_id, season_year) -> web.Response:
    """draftcombinespotshooting_get

    

    :param league_id: 
    :type league_id: str
    :param season_year: 
    :type season_year: str

    """
    return web.Response(status=200)


async def draftcombinestats_get(request: web.Request, league_id, season_year) -> web.Response:
    """draftcombinestats_get

    

    :param league_id: 
    :type league_id: str
    :param season_year: 
    :type season_year: str

    """
    return web.Response(status=200)


async def drafthistory_get(request: web.Request, league_id) -> web.Response:
    """drafthistory_get

    

    :param league_id: 
    :type league_id: str

    """
    return web.Response(status=200)


async def franchisehistory_get(request: web.Request, league_id) -> web.Response:
    """franchisehistory_get

    

    :param league_id: 
    :type league_id: str

    """
    return web.Response(status=200)


async def homepageleaders_get(request: web.Request, stat_category, league_id, season, season_type, player_or_team, player_scope, game_scope, game=None, player=None) -> web.Response:
    """homepageleaders_get

    

    :param stat_category: 
    :type stat_category: str
    :param league_id: 
    :type league_id: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param player_or_team: 
    :type player_or_team: str
    :param player_scope: 
    :type player_scope: str
    :param game_scope: 
    :type game_scope: str
    :param game: 
    :type game: str
    :param player: 
    :type player: str

    """
    return web.Response(status=200)


async def homepagev2_get(request: web.Request, stat_type, league_id, season, season_type, player_or_team, player_scope, game_scope, game=None, player=None) -> web.Response:
    """homepagev2_get

    

    :param stat_type: 
    :type stat_type: str
    :param league_id: 
    :type league_id: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param player_or_team: 
    :type player_or_team: str
    :param player_scope: 
    :type player_scope: str
    :param game_scope: 
    :type game_scope: str
    :param game: 
    :type game: str
    :param player: 
    :type player: str

    """
    return web.Response(status=200)


async def leaderstiles_get(request: web.Request, stat, league_id, season, season_type, player_or_team, player_scope, game_scope, game=None, player=None) -> web.Response:
    """leaderstiles_get

    

    :param stat: 
    :type stat: str
    :param league_id: 
    :type league_id: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param player_or_team: 
    :type player_or_team: str
    :param player_scope: 
    :type player_scope: str
    :param game_scope: 
    :type game_scope: str
    :param game: 
    :type game: str
    :param player: 
    :type player: str

    """
    return web.Response(status=200)


async def leaguedashlineups_get(request: web.Request, group_quantity, season_type, measure_type, per_mode, plus_minus, pace_adjust, rank, season, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games) -> web.Response:
    """leaguedashlineups_get

    

    :param group_quantity: 
    :type group_quantity: str
    :param season_type: 
    :type season_type: str
    :param measure_type: 
    :type measure_type: str
    :param per_mode: 
    :type per_mode: str
    :param plus_minus: 
    :type plus_minus: str
    :param pace_adjust: 
    :type pace_adjust: str
    :param rank: 
    :type rank: str
    :param season: 
    :type season: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def leaguedashplayerbiostats_get(request: web.Request, per_mode, league_id, season, season_type) -> web.Response:
    """leaguedashplayerbiostats_get

    

    :param per_mode: 
    :type per_mode: str
    :param league_id: 
    :type league_id: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str

    """
    return web.Response(status=200)


async def leaguedashplayerclutch_get(request: web.Request, clutch_time, ahead_behind, point_diff, game_scope, player_experience, player_position, starter_bench, measure_type, per_mode, plus_minus, pace_adjust, rank, season, season_type, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games) -> web.Response:
    """leaguedashplayerclutch_get

    

    :param clutch_time: 
    :type clutch_time: str
    :param ahead_behind: 
    :type ahead_behind: str
    :param point_diff: 
    :type point_diff: str
    :param game_scope: 
    :type game_scope: str
    :param player_experience: 
    :type player_experience: str
    :param player_position: 
    :type player_position: str
    :param starter_bench: 
    :type starter_bench: str
    :param measure_type: 
    :type measure_type: str
    :param per_mode: 
    :type per_mode: str
    :param plus_minus: 
    :type plus_minus: str
    :param pace_adjust: 
    :type pace_adjust: str
    :param rank: 
    :type rank: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def leaguedashplayerptshot_get(request: web.Request, league_id, per_mode, season, season_type) -> web.Response:
    """leaguedashplayerptshot_get

    

    :param league_id: 
    :type league_id: str
    :param per_mode: 
    :type per_mode: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str

    """
    return web.Response(status=200)


async def leaguedashplayershotlocations_get(request: web.Request, measure_type, per_mode, plus_minus, pace_adjust, rank, season, season_type, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games, distance_range, game_scope, player_experience, player_position, starter_bench) -> web.Response:
    """leaguedashplayershotlocations_get

    

    :param measure_type: 
    :type measure_type: str
    :param per_mode: 
    :type per_mode: str
    :param plus_minus: 
    :type plus_minus: str
    :param pace_adjust: 
    :type pace_adjust: str
    :param rank: 
    :type rank: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str
    :param distance_range: 
    :type distance_range: str
    :param game_scope: 
    :type game_scope: str
    :param player_experience: 
    :type player_experience: str
    :param player_position: 
    :type player_position: str
    :param starter_bench: 
    :type starter_bench: str

    """
    return web.Response(status=200)


async def leaguedashplayerstats_get(request: web.Request, game_scope, player_experience, player_position, starter_bench, measure_type, per_mode, plus_minus, pace_adjust, rank, season, season_type, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games) -> web.Response:
    """leaguedashplayerstats_get

    

    :param game_scope: 
    :type game_scope: str
    :param player_experience: 
    :type player_experience: str
    :param player_position: 
    :type player_position: str
    :param starter_bench: 
    :type starter_bench: str
    :param measure_type: 
    :type measure_type: str
    :param per_mode: 
    :type per_mode: str
    :param plus_minus: 
    :type plus_minus: str
    :param pace_adjust: 
    :type pace_adjust: str
    :param rank: 
    :type rank: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def leaguedashptdefend_get(request: web.Request, league_id, per_mode, season, season_type, defense_category) -> web.Response:
    """leaguedashptdefend_get

    

    :param league_id: 
    :type league_id: str
    :param per_mode: 
    :type per_mode: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param defense_category: 
    :type defense_category: str

    """
    return web.Response(status=200)


async def leaguedashptteamdefend_get(request: web.Request, league_id, per_mode, season, season_type, defense_category) -> web.Response:
    """leaguedashptteamdefend_get

    

    :param league_id: 
    :type league_id: str
    :param per_mode: 
    :type per_mode: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param defense_category: 
    :type defense_category: str

    """
    return web.Response(status=200)


async def leaguedashteamclutch_get(request: web.Request, clutch_time, ahead_behind, point_diff, game_scope, player_experience, player_position, starter_bench, measure_type, per_mode, plus_minus, pace_adjust, rank, season, season_type, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games) -> web.Response:
    """leaguedashteamclutch_get

    

    :param clutch_time: 
    :type clutch_time: str
    :param ahead_behind: 
    :type ahead_behind: str
    :param point_diff: 
    :type point_diff: str
    :param game_scope: 
    :type game_scope: str
    :param player_experience: 
    :type player_experience: str
    :param player_position: 
    :type player_position: str
    :param starter_bench: 
    :type starter_bench: str
    :param measure_type: 
    :type measure_type: str
    :param per_mode: 
    :type per_mode: str
    :param plus_minus: 
    :type plus_minus: str
    :param pace_adjust: 
    :type pace_adjust: str
    :param rank: 
    :type rank: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def leaguedashteamptshot_get(request: web.Request, league_id, per_mode, season, season_type) -> web.Response:
    """leaguedashteamptshot_get

    

    :param league_id: 
    :type league_id: str
    :param per_mode: 
    :type per_mode: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str

    """
    return web.Response(status=200)


async def leaguedashteamshotlocations_get(request: web.Request, measure_type, per_mode, plus_minus, pace_adjust, rank, season, season_type, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games, distance_range, game_scope, player_experience, player_position, starter_bench) -> web.Response:
    """leaguedashteamshotlocations_get

    

    :param measure_type: 
    :type measure_type: str
    :param per_mode: 
    :type per_mode: str
    :param plus_minus: 
    :type plus_minus: str
    :param pace_adjust: 
    :type pace_adjust: str
    :param rank: 
    :type rank: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str
    :param distance_range: 
    :type distance_range: str
    :param game_scope: 
    :type game_scope: str
    :param player_experience: 
    :type player_experience: str
    :param player_position: 
    :type player_position: str
    :param starter_bench: 
    :type starter_bench: str

    """
    return web.Response(status=200)


async def leaguedashteamstats_get(request: web.Request, measure_type, per_mode, plus_minus, pace_adjust, rank, season, season_type, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games) -> web.Response:
    """leaguedashteamstats_get

    

    :param measure_type: 
    :type measure_type: str
    :param per_mode: 
    :type per_mode: str
    :param plus_minus: 
    :type plus_minus: str
    :param pace_adjust: 
    :type pace_adjust: str
    :param rank: 
    :type rank: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def leagueleaders_get(request: web.Request, league_id, per_mode, season, season_type, scope, stat_category=None) -> web.Response:
    """leagueleaders_get

    

    :param league_id: 
    :type league_id: str
    :param per_mode: 
    :type per_mode: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param scope: 
    :type scope: str
    :param stat_category: 
    :type stat_category: str

    """
    return web.Response(status=200)


async def playbyplay_get(request: web.Request, game_id, start_period, end_period) -> web.Response:
    """playbyplay_get

    

    :param game_id: 
    :type game_id: str
    :param start_period: 
    :type start_period: str
    :param end_period: 
    :type end_period: str

    """
    return web.Response(status=200)


async def playbyplayv2_get(request: web.Request, game_id, start_period, end_period) -> web.Response:
    """playbyplayv2_get

    

    :param game_id: 
    :type game_id: str
    :param start_period: 
    :type start_period: str
    :param end_period: 
    :type end_period: str

    """
    return web.Response(status=200)


async def playercareerstats_get(request: web.Request, per_mode, player_id) -> web.Response:
    """playercareerstats_get

    

    :param per_mode: 
    :type per_mode: str
    :param player_id: 
    :type player_id: str

    """
    return web.Response(status=200)


async def playercompare_get(request: web.Request, player_id_list, vs_player_id_list, season_type, measure_type, per_mode, plus_minus, pace_adjust, rank, season, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games) -> web.Response:
    """playercompare_get

    

    :param player_id_list: 
    :type player_id_list: str
    :param vs_player_id_list: 
    :type vs_player_id_list: str
    :param season_type: 
    :type season_type: str
    :param measure_type: 
    :type measure_type: str
    :param per_mode: 
    :type per_mode: str
    :param plus_minus: 
    :type plus_minus: str
    :param pace_adjust: 
    :type pace_adjust: str
    :param rank: 
    :type rank: str
    :param season: 
    :type season: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def playerdashboardbyclutch_get(request: web.Request, measure_type, per_mode, plus_minus, pace_adjust, rank, season, season_type, player_id, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games) -> web.Response:
    """playerdashboardbyclutch_get

    

    :param measure_type: 
    :type measure_type: str
    :param per_mode: 
    :type per_mode: str
    :param plus_minus: 
    :type plus_minus: str
    :param pace_adjust: 
    :type pace_adjust: str
    :param rank: 
    :type rank: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param player_id: 
    :type player_id: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def playerdashboardbygamesplits_get(request: web.Request, measure_type, per_mode, plus_minus, pace_adjust, rank, season, season_type, player_id, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games) -> web.Response:
    """playerdashboardbygamesplits_get

    

    :param measure_type: 
    :type measure_type: str
    :param per_mode: 
    :type per_mode: str
    :param plus_minus: 
    :type plus_minus: str
    :param pace_adjust: 
    :type pace_adjust: str
    :param rank: 
    :type rank: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param player_id: 
    :type player_id: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def playerdashboardbygeneralsplits_get(request: web.Request, measure_type, per_mode, plus_minus, pace_adjust, rank, season, season_type, player_id, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games) -> web.Response:
    """playerdashboardbygeneralsplits_get

    

    :param measure_type: 
    :type measure_type: str
    :param per_mode: 
    :type per_mode: str
    :param plus_minus: 
    :type plus_minus: str
    :param pace_adjust: 
    :type pace_adjust: str
    :param rank: 
    :type rank: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param player_id: 
    :type player_id: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def playerdashboardbylastngames_get(request: web.Request, measure_type, per_mode, plus_minus, pace_adjust, rank, season, season_type, player_id, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games) -> web.Response:
    """playerdashboardbylastngames_get

    

    :param measure_type: 
    :type measure_type: str
    :param per_mode: 
    :type per_mode: str
    :param plus_minus: 
    :type plus_minus: str
    :param pace_adjust: 
    :type pace_adjust: str
    :param rank: 
    :type rank: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param player_id: 
    :type player_id: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def playerdashboardbyopponent_get(request: web.Request, measure_type, per_mode, plus_minus, pace_adjust, rank, season, season_type, player_id, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games) -> web.Response:
    """playerdashboardbyopponent_get

    

    :param measure_type: 
    :type measure_type: str
    :param per_mode: 
    :type per_mode: str
    :param plus_minus: 
    :type plus_minus: str
    :param pace_adjust: 
    :type pace_adjust: str
    :param rank: 
    :type rank: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param player_id: 
    :type player_id: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def playerdashboardbyshootingsplits_get(request: web.Request, measure_type, per_mode, plus_minus, pace_adjust, rank, season, season_type, player_id, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games) -> web.Response:
    """playerdashboardbyshootingsplits_get

    

    :param measure_type: 
    :type measure_type: str
    :param per_mode: 
    :type per_mode: str
    :param plus_minus: 
    :type plus_minus: str
    :param pace_adjust: 
    :type pace_adjust: str
    :param rank: 
    :type rank: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param player_id: 
    :type player_id: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def playerdashboardbyteamperformance_get(request: web.Request, measure_type, per_mode, plus_minus, pace_adjust, rank, season, season_type, player_id, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games) -> web.Response:
    """playerdashboardbyteamperformance_get

    

    :param measure_type: 
    :type measure_type: str
    :param per_mode: 
    :type per_mode: str
    :param plus_minus: 
    :type plus_minus: str
    :param pace_adjust: 
    :type pace_adjust: str
    :param rank: 
    :type rank: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param player_id: 
    :type player_id: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def playerdashboardbyyearoveryear_get(request: web.Request, measure_type, per_mode, plus_minus, pace_adjust, rank, season, season_type, player_id, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games) -> web.Response:
    """playerdashboardbyyearoveryear_get

    

    :param measure_type: 
    :type measure_type: str
    :param per_mode: 
    :type per_mode: str
    :param plus_minus: 
    :type plus_minus: str
    :param pace_adjust: 
    :type pace_adjust: str
    :param rank: 
    :type rank: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param player_id: 
    :type player_id: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def playerdashptpass_get(request: web.Request, per_mode, season, season_type, player_id, team_id, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, last_n_games) -> web.Response:
    """playerdashptpass_get

    

    :param per_mode: 
    :type per_mode: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param player_id: 
    :type player_id: str
    :param team_id: 
    :type team_id: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def playerdashptreb_get(request: web.Request, per_mode, season, season_type, player_id, team_id, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games) -> web.Response:
    """playerdashptreb_get

    

    :param per_mode: 
    :type per_mode: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param player_id: 
    :type player_id: str
    :param team_id: 
    :type team_id: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def playerdashptreboundlogs_get(request: web.Request, season=None, season_type=None, player_id=None, team_id=None, outcome=None, location=None, month=None, season_segment=None, date_from=None, date_to=None, opponent_team_id=None, vs_conference=None, vs_division=None, game_segment=None, period=None, last_n_games=None) -> web.Response:
    """playerdashptreboundlogs_get

    

    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param player_id: 
    :type player_id: str
    :param team_id: 
    :type team_id: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def playerdashptshotdefend_get(request: web.Request, per_mode, season, season_type, player_id, team_id, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games) -> web.Response:
    """playerdashptshotdefend_get

    

    :param per_mode: 
    :type per_mode: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param player_id: 
    :type player_id: str
    :param team_id: 
    :type team_id: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def playerdashptshotlog_get(request: web.Request, league_id=None, season=None, season_type=None, player_id=None, team_id=None) -> web.Response:
    """playerdashptshotlog_get

    

    :param league_id: 
    :type league_id: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param player_id: 
    :type player_id: str
    :param team_id: 
    :type team_id: str

    """
    return web.Response(status=200)


async def playerdashptshots_get(request: web.Request, per_mode, season, season_type, player_id, team_id, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games) -> web.Response:
    """playerdashptshots_get

    

    :param per_mode: 
    :type per_mode: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param player_id: 
    :type player_id: str
    :param team_id: 
    :type team_id: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def playergamelog_get(request: web.Request, player_id, season, season_type) -> web.Response:
    """playergamelog_get

    

    :param player_id: 
    :type player_id: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str

    """
    return web.Response(status=200)


async def playerprofile_get(request: web.Request, league_id, player_id, season, season_type, graph_start_season, graph_end_season, graph_stat) -> web.Response:
    """playerprofile_get

    

    :param league_id: 
    :type league_id: str
    :param player_id: 
    :type player_id: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param graph_start_season: 
    :type graph_start_season: str
    :param graph_end_season: 
    :type graph_end_season: str
    :param graph_stat: 
    :type graph_stat: str

    """
    return web.Response(status=200)


async def playerprofilev2_get(request: web.Request, per_mode, player_id) -> web.Response:
    """playerprofilev2_get

    

    :param per_mode: 
    :type per_mode: str
    :param player_id: 
    :type player_id: str

    """
    return web.Response(status=200)


async def playersvsplayers_get(request: web.Request, player_team_id, player_id1, player_id2, player_id3, player_id4, player_id5, vs_team_id, vs_player_id1, vs_player_id2, vs_player_id3, vs_player_id4, vs_player_id5, season_type, measure_type, per_mode, plus_minus, pace_adjust, rank, season, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games) -> web.Response:
    """playersvsplayers_get

    

    :param player_team_id: 
    :type player_team_id: str
    :param player_id1: 
    :type player_id1: str
    :param player_id2: 
    :type player_id2: str
    :param player_id3: 
    :type player_id3: str
    :param player_id4: 
    :type player_id4: str
    :param player_id5: 
    :type player_id5: str
    :param vs_team_id: 
    :type vs_team_id: str
    :param vs_player_id1: 
    :type vs_player_id1: str
    :param vs_player_id2: 
    :type vs_player_id2: str
    :param vs_player_id3: 
    :type vs_player_id3: str
    :param vs_player_id4: 
    :type vs_player_id4: str
    :param vs_player_id5: 
    :type vs_player_id5: str
    :param season_type: 
    :type season_type: str
    :param measure_type: 
    :type measure_type: str
    :param per_mode: 
    :type per_mode: str
    :param plus_minus: 
    :type plus_minus: str
    :param pace_adjust: 
    :type pace_adjust: str
    :param rank: 
    :type rank: str
    :param season: 
    :type season: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def playervsplayer_get(request: web.Request, player_id, vs_player_id, season_type, measure_type, per_mode, plus_minus, pace_adjust, rank, season, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games) -> web.Response:
    """playervsplayer_get

    

    :param player_id: 
    :type player_id: str
    :param vs_player_id: 
    :type vs_player_id: str
    :param season_type: 
    :type season_type: str
    :param measure_type: 
    :type measure_type: str
    :param per_mode: 
    :type per_mode: str
    :param plus_minus: 
    :type plus_minus: str
    :param pace_adjust: 
    :type pace_adjust: str
    :param rank: 
    :type rank: str
    :param season: 
    :type season: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def playoffpicture_get(request: web.Request, league_id, season_id) -> web.Response:
    """playoffpicture_get

    

    :param league_id: 
    :type league_id: str
    :param season_id: 
    :type season_id: str

    """
    return web.Response(status=200)


async def scoreboard_get(request: web.Request, game_date, league_id, day_offset) -> web.Response:
    """scoreboard_get

    

    :param game_date: 
    :type game_date: str
    :param league_id: 
    :type league_id: str
    :param day_offset: 
    :type day_offset: str

    """
    return web.Response(status=200)


async def scoreboard_v2_get(request: web.Request, game_date, league_id, day_offset) -> web.Response:
    """scoreboard_v2_get

    

    :param game_date: 
    :type game_date: str
    :param league_id: 
    :type league_id: str
    :param day_offset: 
    :type day_offset: str

    """
    return web.Response(status=200)


async def shotchartdetail_get(request: web.Request, season_type, team_id, player_id, game_id, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, position, rookie_year, game_segment, period, last_n_games, context_measure) -> web.Response:
    """shotchartdetail_get

    

    :param season_type: 
    :type season_type: str
    :param team_id: 
    :type team_id: str
    :param player_id: 
    :type player_id: str
    :param game_id: 
    :type game_id: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param position: 
    :type position: str
    :param rookie_year: 
    :type rookie_year: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str
    :param context_measure: 
    :type context_measure: str

    """
    return web.Response(status=200)


async def shotchartlineupdetail_get(request: web.Request, league_id, season, season_type, team_id, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games, game_id, group_id, context_measure, context_filter) -> web.Response:
    """shotchartlineupdetail_get

    

    :param league_id: 
    :type league_id: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param team_id: 
    :type team_id: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str
    :param game_id: 
    :type game_id: str
    :param group_id: 
    :type group_id: str
    :param context_measure: 
    :type context_measure: str
    :param context_filter: 
    :type context_filter: str

    """
    return web.Response(status=200)


async def teamdashboardbyclutch_get(request: web.Request, team_id, measure_type, per_mode, plus_minus, pace_adjust, rank, season, season_type, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games) -> web.Response:
    """teamdashboardbyclutch_get

    

    :param team_id: 
    :type team_id: str
    :param measure_type: 
    :type measure_type: str
    :param per_mode: 
    :type per_mode: str
    :param plus_minus: 
    :type plus_minus: str
    :param pace_adjust: 
    :type pace_adjust: str
    :param rank: 
    :type rank: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def teamdashboardbygamesplits_get(request: web.Request, team_id, measure_type, per_mode, plus_minus, pace_adjust, rank, season, season_type, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games) -> web.Response:
    """teamdashboardbygamesplits_get

    

    :param team_id: 
    :type team_id: str
    :param measure_type: 
    :type measure_type: str
    :param per_mode: 
    :type per_mode: str
    :param plus_minus: 
    :type plus_minus: str
    :param pace_adjust: 
    :type pace_adjust: str
    :param rank: 
    :type rank: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def teamdashboardbygeneralsplits_get(request: web.Request, season_type, team_id, measure_type, per_mode, plus_minus, pace_adjust, rank, season, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games) -> web.Response:
    """teamdashboardbygeneralsplits_get

    

    :param season_type: 
    :type season_type: str
    :param team_id: 
    :type team_id: str
    :param measure_type: 
    :type measure_type: str
    :param per_mode: 
    :type per_mode: str
    :param plus_minus: 
    :type plus_minus: str
    :param pace_adjust: 
    :type pace_adjust: str
    :param rank: 
    :type rank: str
    :param season: 
    :type season: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def teamdashboardbylastngames_get(request: web.Request, team_id, measure_type, per_mode, plus_minus, pace_adjust, rank, season, season_type, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games) -> web.Response:
    """teamdashboardbylastngames_get

    

    :param team_id: 
    :type team_id: str
    :param measure_type: 
    :type measure_type: str
    :param per_mode: 
    :type per_mode: str
    :param plus_minus: 
    :type plus_minus: str
    :param pace_adjust: 
    :type pace_adjust: str
    :param rank: 
    :type rank: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def teamdashboardbyopponent_get(request: web.Request, team_id, measure_type, per_mode, plus_minus, pace_adjust, rank, season, season_type, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games) -> web.Response:
    """teamdashboardbyopponent_get

    

    :param team_id: 
    :type team_id: str
    :param measure_type: 
    :type measure_type: str
    :param per_mode: 
    :type per_mode: str
    :param plus_minus: 
    :type plus_minus: str
    :param pace_adjust: 
    :type pace_adjust: str
    :param rank: 
    :type rank: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def teamdashboardbyshootingsplits_get(request: web.Request, team_id, measure_type, per_mode, plus_minus, pace_adjust, rank, season, season_type, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games) -> web.Response:
    """teamdashboardbyshootingsplits_get

    

    :param team_id: 
    :type team_id: str
    :param measure_type: 
    :type measure_type: str
    :param per_mode: 
    :type per_mode: str
    :param plus_minus: 
    :type plus_minus: str
    :param pace_adjust: 
    :type pace_adjust: str
    :param rank: 
    :type rank: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def teamdashboardbyteamperformance_get(request: web.Request, team_id, measure_type, per_mode, plus_minus, pace_adjust, rank, season, season_type, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games) -> web.Response:
    """teamdashboardbyteamperformance_get

    

    :param team_id: 
    :type team_id: str
    :param measure_type: 
    :type measure_type: str
    :param per_mode: 
    :type per_mode: str
    :param plus_minus: 
    :type plus_minus: str
    :param pace_adjust: 
    :type pace_adjust: str
    :param rank: 
    :type rank: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def teamdashboardbyyearoveryear_get(request: web.Request, team_id, measure_type, per_mode, plus_minus, pace_adjust, rank, season, season_type, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games) -> web.Response:
    """teamdashboardbyyearoveryear_get

    

    :param team_id: 
    :type team_id: str
    :param measure_type: 
    :type measure_type: str
    :param per_mode: 
    :type per_mode: str
    :param plus_minus: 
    :type plus_minus: str
    :param pace_adjust: 
    :type pace_adjust: str
    :param rank: 
    :type rank: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def teamdashlineups_get(request: web.Request, group_quantity, game_id, season_type, team_id, measure_type, per_mode, plus_minus, pace_adjust, rank, season, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games) -> web.Response:
    """teamdashlineups_get

    

    :param group_quantity: 
    :type group_quantity: str
    :param game_id: 
    :type game_id: str
    :param season_type: 
    :type season_type: str
    :param team_id: 
    :type team_id: str
    :param measure_type: 
    :type measure_type: str
    :param per_mode: 
    :type per_mode: str
    :param plus_minus: 
    :type plus_minus: str
    :param pace_adjust: 
    :type pace_adjust: str
    :param rank: 
    :type rank: str
    :param season: 
    :type season: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def teamdashptpass_get(request: web.Request, per_mode, season, season_type, team_id, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, last_n_games) -> web.Response:
    """teamdashptpass_get

    

    :param per_mode: 
    :type per_mode: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param team_id: 
    :type team_id: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def teamdashptreb_get(request: web.Request, per_mode, season, season_type, team_id, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games) -> web.Response:
    """teamdashptreb_get

    

    :param per_mode: 
    :type per_mode: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param team_id: 
    :type team_id: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def teamdashptshots_get(request: web.Request, per_mode, season, season_type, team_id, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games) -> web.Response:
    """teamdashptshots_get

    

    :param per_mode: 
    :type per_mode: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param team_id: 
    :type team_id: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def teamgamelog_get(request: web.Request, team_id, season, season_type) -> web.Response:
    """teamgamelog_get

    

    :param team_id: 
    :type team_id: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str

    """
    return web.Response(status=200)


async def teaminfocommon_get(request: web.Request, season, team_id, league_id, season_type) -> web.Response:
    """teaminfocommon_get

    

    :param season: 
    :type season: str
    :param team_id: 
    :type team_id: str
    :param league_id: 
    :type league_id: str
    :param season_type: 
    :type season_type: str

    """
    return web.Response(status=200)


async def teamplayerdashboard_get(request: web.Request, season_type, team_id, measure_type, per_mode, plus_minus, pace_adjust, rank, season, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games) -> web.Response:
    """teamplayerdashboard_get

    

    :param season_type: 
    :type season_type: str
    :param team_id: 
    :type team_id: str
    :param measure_type: 
    :type measure_type: str
    :param per_mode: 
    :type per_mode: str
    :param plus_minus: 
    :type plus_minus: str
    :param pace_adjust: 
    :type pace_adjust: str
    :param rank: 
    :type rank: str
    :param season: 
    :type season: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def teamplayeronoffdetails_get(request: web.Request, team_id, measure_type, per_mode, plus_minus, pace_adjust, rank, season, season_type, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games) -> web.Response:
    """teamplayeronoffdetails_get

    

    :param team_id: 
    :type team_id: str
    :param measure_type: 
    :type measure_type: str
    :param per_mode: 
    :type per_mode: str
    :param plus_minus: 
    :type plus_minus: str
    :param pace_adjust: 
    :type pace_adjust: str
    :param rank: 
    :type rank: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def teamplayeronoffsummary_get(request: web.Request, team_id, measure_type, per_mode, plus_minus, pace_adjust, rank, season, season_type, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games) -> web.Response:
    """teamplayeronoffsummary_get

    

    :param team_id: 
    :type team_id: str
    :param measure_type: 
    :type measure_type: str
    :param per_mode: 
    :type per_mode: str
    :param plus_minus: 
    :type plus_minus: str
    :param pace_adjust: 
    :type pace_adjust: str
    :param rank: 
    :type rank: str
    :param season: 
    :type season: str
    :param season_type: 
    :type season_type: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def teamvsplayer_get(request: web.Request, team_id, vs_player_id, season_type, measure_type, per_mode, plus_minus, pace_adjust, rank, season, outcome, location, month, season_segment, date_from, date_to, opponent_team_id, vs_conference, vs_division, game_segment, period, last_n_games) -> web.Response:
    """teamvsplayer_get

    

    :param team_id: 
    :type team_id: str
    :param vs_player_id: 
    :type vs_player_id: str
    :param season_type: 
    :type season_type: str
    :param measure_type: 
    :type measure_type: str
    :param per_mode: 
    :type per_mode: str
    :param plus_minus: 
    :type plus_minus: str
    :param pace_adjust: 
    :type pace_adjust: str
    :param rank: 
    :type rank: str
    :param season: 
    :type season: str
    :param outcome: 
    :type outcome: str
    :param location: 
    :type location: str
    :param month: 
    :type month: str
    :param season_segment: 
    :type season_segment: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param opponent_team_id: 
    :type opponent_team_id: str
    :param vs_conference: 
    :type vs_conference: str
    :param vs_division: 
    :type vs_division: str
    :param game_segment: 
    :type game_segment: str
    :param period: 
    :type period: str
    :param last_n_games: 
    :type last_n_games: str

    """
    return web.Response(status=200)


async def teamyearbyyearstats_get(request: web.Request, league_id, season_type, per_mode, team_id) -> web.Response:
    """teamyearbyyearstats_get

    

    :param league_id: 
    :type league_id: str
    :param season_type: 
    :type season_type: str
    :param per_mode: 
    :type per_mode: str
    :param team_id: 
    :type team_id: str

    """
    return web.Response(status=200)


async def video_status_get(request: web.Request, league_id, game_date) -> web.Response:
    """video_status_get

    

    :param league_id: 
    :type league_id: str
    :param game_date: 
    :type game_date: str

    """
    return web.Response(status=200)
