from typing import List, Dict
from aiohttp import web

from openapi_server.models.leaderboard_scores import LeaderboardScores
from openapi_server.models.player_leaderboard_score_list_response import PlayerLeaderboardScoreListResponse
from openapi_server.models.player_score_list_response import PlayerScoreListResponse
from openapi_server.models.player_score_response import PlayerScoreResponse
from openapi_server.models.player_score_submission_list import PlayerScoreSubmissionList
from openapi_server import util


async def games_scores_get(request: web.Request, player_id, leaderboard_id, time_span, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, include_rank_type=None, language=None, max_results=None, page_token=None) -> web.Response:
    """games_scores_get

    Get high scores, and optionally ranks, in leaderboards for the currently authenticated player. For a specific time span, &#x60;leaderboardId&#x60; can be set to &#x60;ALL&#x60; to retrieve data for all leaderboards in a given time span. &#x60;NOTE: You cannot ask for &#39;ALL&#39; leaderboards and &#39;ALL&#39; timeSpans in the same request; only one parameter may be set to &#39;ALL&#39;.

    :param player_id: A player ID. A value of &#x60;me&#x60; may be used in place of the authenticated player&#39;s ID.
    :type player_id: str
    :param leaderboard_id: The ID of the leaderboard. Can be set to &#39;ALL&#39; to retrieve data for all leaderboards for this application.
    :type leaderboard_id: str
    :param time_span: The time span for the scores and ranks you&#39;re requesting.
    :type time_span: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param include_rank_type: The types of ranks to return. If the parameter is omitted, no ranks will be returned.
    :type include_rank_type: str
    :param language: The preferred language to use for strings returned by this method.
    :type language: str
    :param max_results: The maximum number of leaderboard scores to return in the response. For any response, the actual number of leaderboard scores returned may be less than the specified &#x60;maxResults&#x60;.
    :type max_results: int
    :param page_token: The token returned by the previous request.
    :type page_token: str

    """
    return web.Response(status=200)


async def games_scores_list(request: web.Request, leaderboard_id, collection, time_span, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, language=None, max_results=None, page_token=None) -> web.Response:
    """games_scores_list

    Lists the scores in a leaderboard, starting from the top.

    :param leaderboard_id: The ID of the leaderboard.
    :type leaderboard_id: str
    :param collection: The collection of scores you&#39;re requesting.
    :type collection: str
    :param time_span: Required. The time span for the scores and ranks you&#39;re requesting.
    :type time_span: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param language: The preferred language to use for strings returned by this method.
    :type language: str
    :param max_results: The maximum number of leaderboard scores to return in the response. For any response, the actual number of leaderboard scores returned may be less than the specified &#x60;maxResults&#x60;.
    :type max_results: int
    :param page_token: The token returned by the previous request.
    :type page_token: str

    """
    return web.Response(status=200)


async def games_scores_list_window(request: web.Request, leaderboard_id, collection, time_span, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, language=None, max_results=None, page_token=None, results_above=None, return_top_if_absent=None) -> web.Response:
    """games_scores_list_window

    Lists the scores in a leaderboard around (and including) a player&#39;s score.

    :param leaderboard_id: The ID of the leaderboard.
    :type leaderboard_id: str
    :param collection: The collection of scores you&#39;re requesting.
    :type collection: str
    :param time_span: Required. The time span for the scores and ranks you&#39;re requesting.
    :type time_span: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param language: The preferred language to use for strings returned by this method.
    :type language: str
    :param max_results: The maximum number of leaderboard scores to return in the response. For any response, the actual number of leaderboard scores returned may be less than the specified &#x60;maxResults&#x60;.
    :type max_results: int
    :param page_token: The token returned by the previous request.
    :type page_token: str
    :param results_above: The preferred number of scores to return above the player&#39;s score. More scores may be returned if the player is at the bottom of the leaderboard; fewer may be returned if the player is at the top. Must be less than or equal to maxResults.
    :type results_above: int
    :param return_top_if_absent: True if the top scores should be returned when the player is not in the leaderboard. Defaults to true.
    :type return_top_if_absent: bool

    """
    return web.Response(status=200)


async def games_scores_submit(request: web.Request, leaderboard_id, score, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, language=None, score_tag=None) -> web.Response:
    """games_scores_submit

    Submits a score to the specified leaderboard.

    :param leaderboard_id: The ID of the leaderboard.
    :type leaderboard_id: str
    :param score: Required. The score you&#39;re submitting. The submitted score is ignored if it is worse than a previously submitted score, where worse depends on the leaderboard sort order. The meaning of the score value depends on the leaderboard format type. For fixed-point, the score represents the raw value. For time, the score represents elapsed time in milliseconds. For currency, the score represents a value in micro units.
    :type score: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param language: The preferred language to use for strings returned by this method.
    :type language: str
    :param score_tag: Additional information about the score you&#39;re submitting. Values must contain no more than 64 URI-safe characters as defined by section 2.3 of RFC 3986.
    :type score_tag: str

    """
    return web.Response(status=200)


async def games_scores_submit_multiple(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, language=None, body=None) -> web.Response:
    """games_scores_submit_multiple

    Submits multiple scores to leaderboards.

    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param language: The preferred language to use for strings returned by this method.
    :type language: str
    :param body: 
    :type body: dict | bytes

    """
    body = PlayerScoreSubmissionList.from_dict(body)
    return web.Response(status=200)
