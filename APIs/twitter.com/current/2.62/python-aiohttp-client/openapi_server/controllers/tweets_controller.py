from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_or_delete_rules_request import AddOrDeleteRulesRequest
from openapi_server.models.add_or_delete_rules_response import AddOrDeleteRulesResponse
from openapi_server.models.error import Error
from openapi_server.models.filtered_streaming_tweet_response import FilteredStreamingTweetResponse
from openapi_server.models.get2_lists_id_tweets_response import Get2ListsIdTweetsResponse
from openapi_server.models.get2_spaces_id_buyers_response import Get2SpacesIdBuyersResponse
from openapi_server.models.get2_spaces_id_tweets_response import Get2SpacesIdTweetsResponse
from openapi_server.models.get2_tweets_counts_all_response import Get2TweetsCountsAllResponse
from openapi_server.models.get2_tweets_counts_recent_response import Get2TweetsCountsRecentResponse
from openapi_server.models.get2_tweets_id_quote_tweets_response import Get2TweetsIdQuoteTweetsResponse
from openapi_server.models.get2_tweets_id_response import Get2TweetsIdResponse
from openapi_server.models.get2_tweets_response import Get2TweetsResponse
from openapi_server.models.get2_tweets_sample10_stream_response import Get2TweetsSample10StreamResponse
from openapi_server.models.get2_tweets_search_all_response import Get2TweetsSearchAllResponse
from openapi_server.models.get2_tweets_search_recent_response import Get2TweetsSearchRecentResponse
from openapi_server.models.get2_users_id_liked_tweets_response import Get2UsersIdLikedTweetsResponse
from openapi_server.models.get2_users_id_mentions_response import Get2UsersIdMentionsResponse
from openapi_server.models.get2_users_id_timelines_reverse_chronological_response import Get2UsersIdTimelinesReverseChronologicalResponse
from openapi_server.models.get2_users_id_tweets_response import Get2UsersIdTweetsResponse
from openapi_server.models.problem import Problem
from openapi_server.models.rules_lookup_response import RulesLookupResponse
from openapi_server.models.streaming_tweet_response import StreamingTweetResponse
from openapi_server.models.tweet_create_request import TweetCreateRequest
from openapi_server.models.tweet_create_response import TweetCreateResponse
from openapi_server.models.tweet_delete_response import TweetDeleteResponse
from openapi_server.models.tweet_hide_request import TweetHideRequest
from openapi_server.models.tweet_hide_response import TweetHideResponse
from openapi_server.models.users_likes_create_request import UsersLikesCreateRequest
from openapi_server.models.users_likes_create_response import UsersLikesCreateResponse
from openapi_server.models.users_likes_delete_response import UsersLikesDeleteResponse
from openapi_server.models.users_retweets_create_request import UsersRetweetsCreateRequest
from openapi_server.models.users_retweets_create_response import UsersRetweetsCreateResponse
from openapi_server.models.users_retweets_delete_response import UsersRetweetsDeleteResponse
from openapi_server import util


async def add_or_delete_rules(request: web.Request, body, dry_run=None) -> web.Response:
    """Add/Delete rules

    Add or delete rules from a User&#39;s active rule set. Users can provide unique, optionally tagged rules to add. Users can delete their entire rule set or a subset specified by rule ids or values.

    :param body: 
    :type body: dict | bytes
    :param dry_run: Dry Run can be used with both the add and delete action, with the expected result given, but without actually taking any action in the system (meaning the end state will always be as it was when the request was submitted). This is particularly useful to validate rule changes.
    :type dry_run: bool

    """
    body = AddOrDeleteRulesRequest.from_dict(body)
    return web.Response(status=200)


async def create_tweet(request: web.Request, body) -> web.Response:
    """Creation of a Tweet

    Causes the User to create a Tweet under the authorized account.

    :param body: 
    :type body: dict | bytes

    """
    body = TweetCreateRequest.from_dict(body)
    return web.Response(status=200)


async def delete_tweet_by_id(request: web.Request, id) -> web.Response:
    """Tweet delete by Tweet ID

    Delete specified Tweet (in the path) by ID.

    :param id: The ID of the Tweet to be deleted.
    :type id: str

    """
    return web.Response(status=200)


async def find_tweet_by_id(request: web.Request, id, tweet_fields=None, expansions=None, media_fields=None, poll_fields=None, user_fields=None, place_fields=None) -> web.Response:
    """Tweet lookup by Tweet ID

    Returns a variety of information about the Tweet specified by the requested ID.

    :param id: A single Tweet ID.
    :type id: str
    :param tweet_fields: A comma separated list of Tweet fields to display.
    :type tweet_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param media_fields: A comma separated list of Media fields to display.
    :type media_fields: List[str]
    :param poll_fields: A comma separated list of Poll fields to display.
    :type poll_fields: List[str]
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param place_fields: A comma separated list of Place fields to display.
    :type place_fields: List[str]

    """
    return web.Response(status=200)


async def find_tweets_by_id(request: web.Request, ids, tweet_fields=None, expansions=None, media_fields=None, poll_fields=None, user_fields=None, place_fields=None) -> web.Response:
    """Tweet lookup by Tweet IDs

    Returns a variety of information about the Tweet specified by the requested ID.

    :param ids: A comma separated list of Tweet IDs. Up to 100 are allowed in a single request.
    :type ids: List[str]
    :param tweet_fields: A comma separated list of Tweet fields to display.
    :type tweet_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param media_fields: A comma separated list of Media fields to display.
    :type media_fields: List[str]
    :param poll_fields: A comma separated list of Poll fields to display.
    :type poll_fields: List[str]
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param place_fields: A comma separated list of Place fields to display.
    :type place_fields: List[str]

    """
    return web.Response(status=200)


async def find_tweets_that_quote_a_tweet(request: web.Request, id, max_results=None, pagination_token=None, exclude=None, tweet_fields=None, expansions=None, media_fields=None, poll_fields=None, user_fields=None, place_fields=None) -> web.Response:
    """Retrieve Tweets that quote a Tweet.

    Returns a variety of information about each Tweet that quotes the Tweet specified by the requested ID.

    :param id: A single Tweet ID.
    :type id: str
    :param max_results: The maximum number of results to be returned.
    :type max_results: int
    :param pagination_token: This parameter is used to get a specified &#39;page&#39; of results.
    :type pagination_token: str
    :param exclude: The set of entities to exclude (e.g. &#39;replies&#39; or &#39;retweets&#39;).
    :type exclude: List[str]
    :param tweet_fields: A comma separated list of Tweet fields to display.
    :type tweet_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param media_fields: A comma separated list of Media fields to display.
    :type media_fields: List[str]
    :param poll_fields: A comma separated list of Poll fields to display.
    :type poll_fields: List[str]
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param place_fields: A comma separated list of Place fields to display.
    :type place_fields: List[str]

    """
    return web.Response(status=200)


async def get_rules(request: web.Request, ids=None, max_results=None, pagination_token=None) -> web.Response:
    """Rules lookup

    Returns rules from a User&#39;s active rule set. Users can fetch all of their rules or a subset, specified by the provided rule ids.

    :param ids: A comma-separated list of Rule IDs.
    :type ids: List[str]
    :param max_results: The maximum number of results.
    :type max_results: int
    :param pagination_token: This value is populated by passing the &#39;next_token&#39; returned in a request to paginate through results.
    :type pagination_token: str

    """
    return web.Response(status=200)


async def get_tweets_firehose_stream(request: web.Request, partition, backfill_minutes=None, start_time=None, end_time=None, tweet_fields=None, expansions=None, media_fields=None, poll_fields=None, user_fields=None, place_fields=None) -> web.Response:
    """Firehose stream

    Streams 100% of public Tweets.

    :param partition: The partition number.
    :type partition: int
    :param backfill_minutes: The number of minutes of backfill requested.
    :type backfill_minutes: int
    :param start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Tweets will be provided.
    :type start_time: str
    :param end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Tweets will be provided.
    :type end_time: str
    :param tweet_fields: A comma separated list of Tweet fields to display.
    :type tweet_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param media_fields: A comma separated list of Media fields to display.
    :type media_fields: List[str]
    :param poll_fields: A comma separated list of Poll fields to display.
    :type poll_fields: List[str]
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param place_fields: A comma separated list of Place fields to display.
    :type place_fields: List[str]

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def get_tweets_sample10_stream(request: web.Request, partition, backfill_minutes=None, start_time=None, end_time=None, tweet_fields=None, expansions=None, media_fields=None, poll_fields=None, user_fields=None, place_fields=None) -> web.Response:
    """Sample 10% stream

    Streams a deterministic 10% of public Tweets.

    :param partition: The partition number.
    :type partition: int
    :param backfill_minutes: The number of minutes of backfill requested.
    :type backfill_minutes: int
    :param start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Tweets will be provided.
    :type start_time: str
    :param end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Tweets will be provided.
    :type end_time: str
    :param tweet_fields: A comma separated list of Tweet fields to display.
    :type tweet_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param media_fields: A comma separated list of Media fields to display.
    :type media_fields: List[str]
    :param poll_fields: A comma separated list of Poll fields to display.
    :type poll_fields: List[str]
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param place_fields: A comma separated list of Place fields to display.
    :type place_fields: List[str]

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def hide_reply_by_id(request: web.Request, tweet_id, body=None) -> web.Response:
    """Hide replies

    Hides or unhides a reply to an owned conversation.

    :param tweet_id: The ID of the reply that you want to hide or unhide.
    :type tweet_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = TweetHideRequest.from_dict(body)
    return web.Response(status=200)


async def lists_id_tweets(request: web.Request, id, max_results=None, pagination_token=None, tweet_fields=None, expansions=None, media_fields=None, poll_fields=None, user_fields=None, place_fields=None) -> web.Response:
    """List Tweets timeline by List ID.

    Returns a list of Tweets associated with the provided List ID.

    :param id: The ID of the List.
    :type id: str
    :param max_results: The maximum number of results.
    :type max_results: int
    :param pagination_token: This parameter is used to get the next &#39;page&#39; of results.
    :type pagination_token: str
    :param tweet_fields: A comma separated list of Tweet fields to display.
    :type tweet_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param media_fields: A comma separated list of Media fields to display.
    :type media_fields: List[str]
    :param poll_fields: A comma separated list of Poll fields to display.
    :type poll_fields: List[str]
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param place_fields: A comma separated list of Place fields to display.
    :type place_fields: List[str]

    """
    return web.Response(status=200)


async def sample_stream(request: web.Request, backfill_minutes=None, tweet_fields=None, expansions=None, media_fields=None, poll_fields=None, user_fields=None, place_fields=None) -> web.Response:
    """Sample stream

    Streams a deterministic 1% of public Tweets.

    :param backfill_minutes: The number of minutes of backfill requested.
    :type backfill_minutes: int
    :param tweet_fields: A comma separated list of Tweet fields to display.
    :type tweet_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param media_fields: A comma separated list of Media fields to display.
    :type media_fields: List[str]
    :param poll_fields: A comma separated list of Poll fields to display.
    :type poll_fields: List[str]
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param place_fields: A comma separated list of Place fields to display.
    :type place_fields: List[str]

    """
    return web.Response(status=200)


async def search_stream(request: web.Request, backfill_minutes=None, start_time=None, end_time=None, tweet_fields=None, expansions=None, media_fields=None, poll_fields=None, user_fields=None, place_fields=None) -> web.Response:
    """Filtered stream

    Streams Tweets matching the stream&#39;s active rule set.

    :param backfill_minutes: The number of minutes of backfill requested.
    :type backfill_minutes: int
    :param start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Tweets will be provided.
    :type start_time: str
    :param end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Tweets will be provided.
    :type end_time: str
    :param tweet_fields: A comma separated list of Tweet fields to display.
    :type tweet_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param media_fields: A comma separated list of Media fields to display.
    :type media_fields: List[str]
    :param poll_fields: A comma separated list of Poll fields to display.
    :type poll_fields: List[str]
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param place_fields: A comma separated list of Place fields to display.
    :type place_fields: List[str]

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def space_buyers_0(request: web.Request, id, pagination_token=None, max_results=None, user_fields=None, expansions=None, tweet_fields=None) -> web.Response:
    """Retrieve the list of Users who purchased a ticket to the given space

    Retrieves the list of Users who purchased a ticket to the given space

    :param id: The ID of the Space to be retrieved.
    :type id: str
    :param pagination_token: This parameter is used to get a specified &#39;page&#39; of results.
    :type pagination_token: str
    :param max_results: The maximum number of results.
    :type max_results: int
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param tweet_fields: A comma separated list of Tweet fields to display.
    :type tweet_fields: List[str]

    """
    return web.Response(status=200)


async def space_tweets_0(request: web.Request, id, max_results=None, tweet_fields=None, expansions=None, media_fields=None, poll_fields=None, user_fields=None, place_fields=None) -> web.Response:
    """Retrieve Tweets from a Space.

    Retrieves Tweets shared in the specified Space.

    :param id: The ID of the Space to be retrieved.
    :type id: str
    :param max_results: The number of Tweets to fetch from the provided space. If not provided, the value will default to the maximum of 100.
    :type max_results: int
    :param tweet_fields: A comma separated list of Tweet fields to display.
    :type tweet_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param media_fields: A comma separated list of Media fields to display.
    :type media_fields: List[str]
    :param poll_fields: A comma separated list of Poll fields to display.
    :type poll_fields: List[str]
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param place_fields: A comma separated list of Place fields to display.
    :type place_fields: List[str]

    """
    return web.Response(status=200)


async def tweet_counts_full_archive_search(request: web.Request, query, start_time=None, end_time=None, since_id=None, until_id=None, next_token=None, pagination_token=None, granularity=None, search_count_fields=None) -> web.Response:
    """Full archive search counts

    Returns Tweet Counts that match a search query.

    :param query: One query/rule/filter for matching Tweets. Refer to https://t.co/rulelength to identify the max query length.
    :type query: str
    :param start_time: YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp (from most recent 7 days) from which the Tweets will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).
    :type start_time: str
    :param end_time: YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Tweets will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).
    :type end_time: str
    :param since_id: Returns results with a Tweet ID greater than (that is, more recent than) the specified ID.
    :type since_id: str
    :param until_id: Returns results with a Tweet ID less than (that is, older than) the specified ID.
    :type until_id: str
    :param next_token: This parameter is used to get the next &#39;page&#39; of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
    :type next_token: str
    :param pagination_token: This parameter is used to get the next &#39;page&#39; of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
    :type pagination_token: str
    :param granularity: The granularity for the search counts results.
    :type granularity: str
    :param search_count_fields: A comma separated list of SearchCount fields to display.
    :type search_count_fields: List[str]

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def tweet_counts_recent_search(request: web.Request, query, start_time=None, end_time=None, since_id=None, until_id=None, next_token=None, pagination_token=None, granularity=None, search_count_fields=None) -> web.Response:
    """Recent search counts

    Returns Tweet Counts from the last 7 days that match a search query.

    :param query: One query/rule/filter for matching Tweets. Refer to https://t.co/rulelength to identify the max query length.
    :type query: str
    :param start_time: YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp (from most recent 7 days) from which the Tweets will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).
    :type start_time: str
    :param end_time: YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Tweets will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).
    :type end_time: str
    :param since_id: Returns results with a Tweet ID greater than (that is, more recent than) the specified ID.
    :type since_id: str
    :param until_id: Returns results with a Tweet ID less than (that is, older than) the specified ID.
    :type until_id: str
    :param next_token: This parameter is used to get the next &#39;page&#39; of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
    :type next_token: str
    :param pagination_token: This parameter is used to get the next &#39;page&#39; of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
    :type pagination_token: str
    :param granularity: The granularity for the search counts results.
    :type granularity: str
    :param search_count_fields: A comma separated list of SearchCount fields to display.
    :type search_count_fields: List[str]

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def tweets_fullarchive_search(request: web.Request, query, start_time=None, end_time=None, since_id=None, until_id=None, max_results=None, next_token=None, pagination_token=None, sort_order=None, tweet_fields=None, expansions=None, media_fields=None, poll_fields=None, user_fields=None, place_fields=None) -> web.Response:
    """Full-archive search

    Returns Tweets that match a search query.

    :param query: One query/rule/filter for matching Tweets. Refer to https://t.co/rulelength to identify the max query length.
    :type query: str
    :param start_time: YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp from which the Tweets will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).
    :type start_time: str
    :param end_time: YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Tweets will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).
    :type end_time: str
    :param since_id: Returns results with a Tweet ID greater than (that is, more recent than) the specified ID.
    :type since_id: str
    :param until_id: Returns results with a Tweet ID less than (that is, older than) the specified ID.
    :type until_id: str
    :param max_results: The maximum number of search results to be returned by a request.
    :type max_results: int
    :param next_token: This parameter is used to get the next &#39;page&#39; of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
    :type next_token: str
    :param pagination_token: This parameter is used to get the next &#39;page&#39; of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
    :type pagination_token: str
    :param sort_order: This order in which to return results.
    :type sort_order: str
    :param tweet_fields: A comma separated list of Tweet fields to display.
    :type tweet_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param media_fields: A comma separated list of Media fields to display.
    :type media_fields: List[str]
    :param poll_fields: A comma separated list of Poll fields to display.
    :type poll_fields: List[str]
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param place_fields: A comma separated list of Place fields to display.
    :type place_fields: List[str]

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def tweets_recent_search(request: web.Request, query, start_time=None, end_time=None, since_id=None, until_id=None, max_results=None, next_token=None, pagination_token=None, sort_order=None, tweet_fields=None, expansions=None, media_fields=None, poll_fields=None, user_fields=None, place_fields=None) -> web.Response:
    """Recent search

    Returns Tweets from the last 7 days that match a search query.

    :param query: One query/rule/filter for matching Tweets. Refer to https://t.co/rulelength to identify the max query length.
    :type query: str
    :param start_time: YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp from which the Tweets will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).
    :type start_time: str
    :param end_time: YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Tweets will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).
    :type end_time: str
    :param since_id: Returns results with a Tweet ID greater than (that is, more recent than) the specified ID.
    :type since_id: str
    :param until_id: Returns results with a Tweet ID less than (that is, older than) the specified ID.
    :type until_id: str
    :param max_results: The maximum number of search results to be returned by a request.
    :type max_results: int
    :param next_token: This parameter is used to get the next &#39;page&#39; of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
    :type next_token: str
    :param pagination_token: This parameter is used to get the next &#39;page&#39; of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
    :type pagination_token: str
    :param sort_order: This order in which to return results.
    :type sort_order: str
    :param tweet_fields: A comma separated list of Tweet fields to display.
    :type tweet_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param media_fields: A comma separated list of Media fields to display.
    :type media_fields: List[str]
    :param poll_fields: A comma separated list of Poll fields to display.
    :type poll_fields: List[str]
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param place_fields: A comma separated list of Place fields to display.
    :type place_fields: List[str]

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def users_id_like(request: web.Request, id, body=None) -> web.Response:
    """Causes the User (in the path) to like the specified Tweet

    Causes the User (in the path) to like the specified Tweet. The User in the path must match the User context authorizing the request.

    :param id: The ID of the authenticated source User that is requesting to like the Tweet.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UsersLikesCreateRequest.from_dict(body)
    return web.Response(status=200)


async def users_id_liked_tweets(request: web.Request, id, max_results=None, pagination_token=None, tweet_fields=None, expansions=None, media_fields=None, poll_fields=None, user_fields=None, place_fields=None) -> web.Response:
    """Returns Tweet objects liked by the provided User ID

    Returns a list of Tweets liked by the provided User ID

    :param id: The ID of the User to lookup.
    :type id: str
    :param max_results: The maximum number of results.
    :type max_results: int
    :param pagination_token: This parameter is used to get the next &#39;page&#39; of results.
    :type pagination_token: str
    :param tweet_fields: A comma separated list of Tweet fields to display.
    :type tweet_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param media_fields: A comma separated list of Media fields to display.
    :type media_fields: List[str]
    :param poll_fields: A comma separated list of Poll fields to display.
    :type poll_fields: List[str]
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param place_fields: A comma separated list of Place fields to display.
    :type place_fields: List[str]

    """
    return web.Response(status=200)


async def users_id_mentions(request: web.Request, id, since_id=None, until_id=None, max_results=None, pagination_token=None, start_time=None, end_time=None, tweet_fields=None, expansions=None, media_fields=None, poll_fields=None, user_fields=None, place_fields=None) -> web.Response:
    """User mention timeline by User ID

    Returns Tweet objects that mention username associated to the provided User ID

    :param id: The ID of the User to lookup.
    :type id: str
    :param since_id: The minimum Tweet ID to be included in the result set. This parameter takes precedence over start_time if both are specified.
    :type since_id: str
    :param until_id: The maximum Tweet ID to be included in the result set. This parameter takes precedence over end_time if both are specified.
    :type until_id: str
    :param max_results: The maximum number of results.
    :type max_results: int
    :param pagination_token: This parameter is used to get the next &#39;page&#39; of results.
    :type pagination_token: str
    :param start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Tweets will be provided. The since_id parameter takes precedence if it is also specified.
    :type start_time: str
    :param end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Tweets will be provided. The until_id parameter takes precedence if it is also specified.
    :type end_time: str
    :param tweet_fields: A comma separated list of Tweet fields to display.
    :type tweet_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param media_fields: A comma separated list of Media fields to display.
    :type media_fields: List[str]
    :param poll_fields: A comma separated list of Poll fields to display.
    :type poll_fields: List[str]
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param place_fields: A comma separated list of Place fields to display.
    :type place_fields: List[str]

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def users_id_retweets(request: web.Request, id, body=None) -> web.Response:
    """Causes the User (in the path) to retweet the specified Tweet.

    Causes the User (in the path) to retweet the specified Tweet. The User in the path must match the User context authorizing the request.

    :param id: The ID of the authenticated source User that is requesting to retweet the Tweet.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UsersRetweetsCreateRequest.from_dict(body)
    return web.Response(status=200)


async def users_id_timeline(request: web.Request, id, since_id=None, until_id=None, max_results=None, pagination_token=None, exclude=None, start_time=None, end_time=None, tweet_fields=None, expansions=None, media_fields=None, poll_fields=None, user_fields=None, place_fields=None) -> web.Response:
    """User home timeline by User ID

    Returns Tweet objects that appears in the provided User ID&#39;s home timeline

    :param id: The ID of the authenticated source User to list Reverse Chronological Timeline Tweets of.
    :type id: str
    :param since_id: The minimum Tweet ID to be included in the result set. This parameter takes precedence over start_time if both are specified.
    :type since_id: str
    :param until_id: The maximum Tweet ID to be included in the result set. This parameter takes precedence over end_time if both are specified.
    :type until_id: str
    :param max_results: The maximum number of results.
    :type max_results: int
    :param pagination_token: This parameter is used to get the next &#39;page&#39; of results.
    :type pagination_token: str
    :param exclude: The set of entities to exclude (e.g. &#39;replies&#39; or &#39;retweets&#39;).
    :type exclude: List[str]
    :param start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Tweets will be provided. The since_id parameter takes precedence if it is also specified.
    :type start_time: str
    :param end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Tweets will be provided. The until_id parameter takes precedence if it is also specified.
    :type end_time: str
    :param tweet_fields: A comma separated list of Tweet fields to display.
    :type tweet_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param media_fields: A comma separated list of Media fields to display.
    :type media_fields: List[str]
    :param poll_fields: A comma separated list of Poll fields to display.
    :type poll_fields: List[str]
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param place_fields: A comma separated list of Place fields to display.
    :type place_fields: List[str]

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def users_id_tweets(request: web.Request, id, since_id=None, until_id=None, max_results=None, pagination_token=None, exclude=None, start_time=None, end_time=None, tweet_fields=None, expansions=None, media_fields=None, poll_fields=None, user_fields=None, place_fields=None) -> web.Response:
    """User Tweets timeline by User ID

    Returns a list of Tweets authored by the provided User ID

    :param id: The ID of the User to lookup.
    :type id: str
    :param since_id: The minimum Tweet ID to be included in the result set. This parameter takes precedence over start_time if both are specified.
    :type since_id: str
    :param until_id: The maximum Tweet ID to be included in the result set. This parameter takes precedence over end_time if both are specified.
    :type until_id: str
    :param max_results: The maximum number of results.
    :type max_results: int
    :param pagination_token: This parameter is used to get the next &#39;page&#39; of results.
    :type pagination_token: str
    :param exclude: The set of entities to exclude (e.g. &#39;replies&#39; or &#39;retweets&#39;).
    :type exclude: List[str]
    :param start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Tweets will be provided. The since_id parameter takes precedence if it is also specified.
    :type start_time: str
    :param end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Tweets will be provided. The until_id parameter takes precedence if it is also specified.
    :type end_time: str
    :param tweet_fields: A comma separated list of Tweet fields to display.
    :type tweet_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param media_fields: A comma separated list of Media fields to display.
    :type media_fields: List[str]
    :param poll_fields: A comma separated list of Poll fields to display.
    :type poll_fields: List[str]
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param place_fields: A comma separated list of Place fields to display.
    :type place_fields: List[str]

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def users_id_unlike(request: web.Request, id, tweet_id) -> web.Response:
    """Causes the User (in the path) to unlike the specified Tweet

    Causes the User (in the path) to unlike the specified Tweet. The User must match the User context authorizing the request

    :param id: The ID of the authenticated source User that is requesting to unlike the Tweet.
    :type id: str
    :param tweet_id: The ID of the Tweet that the User is requesting to unlike.
    :type tweet_id: str

    """
    return web.Response(status=200)


async def users_id_unretweets(request: web.Request, id, source_tweet_id) -> web.Response:
    """Causes the User (in the path) to unretweet the specified Tweet

    Causes the User (in the path) to unretweet the specified Tweet. The User must match the User context authorizing the request

    :param id: The ID of the authenticated source User that is requesting to retweet the Tweet.
    :type id: str
    :param source_tweet_id: The ID of the Tweet that the User is requesting to unretweet.
    :type source_tweet_id: str

    """
    return web.Response(status=200)
