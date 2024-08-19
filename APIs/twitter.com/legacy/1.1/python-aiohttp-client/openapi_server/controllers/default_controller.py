from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def account_settings_get(request: web.Request, trend_location_woeid=None, sleep_time_enabled=None, start_sleep_time=None, end_sleep_time=None, time_zone=None, lang=None) -> web.Response:
    """account_settings_get

    Returns settings (including current trend, geo and sleep time information) for the authenticating user.

    :param trend_location_woeid: The Yahoo! Where On Earth ID to use as the user&#39;s default trend location. Global information is available by using 1 as the WOEID. The woeid must be one of the locations returned by GET trends/available.  Example Values: 1
    :type trend_location_woeid: str
    :param sleep_time_enabled: When set to true, t or 1, will enable sleep time for the user. Sleep time is the time when push or SMS notifications should not be sent to the user.  Example Values: true
    :type sleep_time_enabled: str
    :param start_sleep_time: The hour that sleep time should begin if it is enabled. The value for this parameter should be provided in ISO8601 format (i.e. 00-23). The time is considered to be in the same timezone as the user&#39;s time_zone setting.  Example Values: 13
    :type start_sleep_time: str
    :param end_sleep_time: The hour that sleep time should end if it is enabled. The value for this parameter should be provided in ISO8601 format (i.e. 00-23). The time is considered to be in the same timezone as the user&#39;s time_zone setting.  Example Values: 13
    :type end_sleep_time: str
    :param time_zone: The timezone dates and times should be displayed in for the user. The timezone must be one of the Rails TimeZone names.  Example Values: Europe/Copenhagen, Pacific/Tongatapu
    :type time_zone: str
    :param lang: The language which Twitter should render in for this user. The language must be specified by the appropriate two letter ISO 639-1 representation. Currently supported languages are provided by GET help/languages.  Example Values: it, en, es
    :type lang: str

    """
    return web.Response(status=200)


async def account_settings_post(request: web.Request, trend_location_woeid=None, sleep_time_enabled=None, start_sleep_time=None, end_sleep_time=None, time_zone=None, lang=None) -> web.Response:
    """account_settings_post

    Updates the authenticating user&#39;s settings.

    :param trend_location_woeid: The Yahoo! Where On Earth ID to use as the user&#39;s default trend location. Global information is available by using 1 as the WOEID. The woeid must be one of the locations returned by GET trends/available.  Example Values: 1
    :type trend_location_woeid: str
    :param sleep_time_enabled: When set to true, t or 1, will enable sleep time for the user. Sleep time is the time when push or SMS notifications should not be sent to the user.  Example Values: true
    :type sleep_time_enabled: str
    :param start_sleep_time: The hour that sleep time should begin if it is enabled. The value for this parameter should be provided in ISO8601 format (i.e. 00-23). The time is considered to be in the same timezone as the user&#39;s time_zone setting.  Example Values: 13
    :type start_sleep_time: str
    :param end_sleep_time: The hour that sleep time should end if it is enabled. The value for this parameter should be provided in ISO8601 format (i.e. 00-23). The time is considered to be in the same timezone as the user&#39;s time_zone setting.  Example Values: 13
    :type end_sleep_time: str
    :param time_zone: The timezone dates and times should be displayed in for the user. The timezone must be one of the Rails TimeZone names.  Example Values: Europe/Copenhagen, Pacific/Tongatapu
    :type time_zone: str
    :param lang: The language which Twitter should render in for this user. The language must be specified by the appropriate two letter ISO 639-1 representation. Currently supported languages are provided by GET help/languages.  Example Values: it, en, es
    :type lang: str

    """
    return web.Response(status=200)


async def account_update_delivery_device(request: web.Request, device, include_entities=None) -> web.Response:
    """account_update_delivery_device

    Sets which device Twitter delivers updates to for the authenticating user. Sending none as the device parameter will disable SMS updates.

    :param device: Must be one of: sms, none.  Example Values: sms
    :type device: str
    :param include_entities: When set to either true, t or 1, each tweet will include a node called \&quot;entities,\&quot;. This node offers a variety of metadata about the tweet in a discreet structure, including: user_mentions, urls, and hashtags. While entities are opt-in on timelines at present, they will be made a default component of output in the future. See Tweet Entities for more detail on entities.  Example Values: true
    :type include_entities: str

    """
    return web.Response(status=200)


async def account_update_profile(request: web.Request, name=None, url=None, location=None, description=None, include_entities=None, skip_status=None) -> web.Response:
    """account_update_profile

    Sets values that users are able to set under the Account tab of their settings page. Only the parameters specified will be updated.

    :param name: Full name associated with the profile. Maximum of 20 characters.  Example Values: Marcel Molina
    :type name: str
    :param url: URL associated with the profile. Will be prepended with \&quot;http://\&quot; if not present. Maximum of 100 characters.  Example Values: http://project.ioni.st
    :type url: str
    :param location: The city or country describing where the user of the account is located. The contents are not normalized or geocoded in any way. Maximum of 30 characters.  Example Values: San Francisco, CA
    :type location: str
    :param description: A description of the user owning the account. Maximum of 160 characters.  Example Values: Flipped my wig at age 22 and it never grew back. Also: I work at Twitter.
    :type description: str
    :param include_entities: The entities node will not be included when set to false.  Example Values: false
    :type include_entities: str
    :param skip_status: When set to either true, t or 1 statuses will not be included in the returned user objects.
    :type skip_status: str

    """
    return web.Response(status=200)


async def accounts_update_profile_background_image(request: web.Request, content_type, tile=None, use=None, include_entities=None, skip_status=None) -> web.Response:
    """accounts_update_profile_background_image

    Updates the authenticating user&#39;s profile background image. This method can also be used to enable or disable the profile background image. Although each parameter is marked as optional, at least one of image, tile or use must be provided when making this request.

    :param content_type: Content type header
    :type content_type: str
    :param tile: Whether or not to tile the background image. If set to true, t or 1 the background image will be displayed tiled. The image will not be tiled otherwise.
    :type tile: str
    :param use: Determines whether to display the profile background image or not. When set to true, t or 1 the background image will be displayed if an image is being uploaded with the request, or has been uploaded previously. An error will be returned if you try to use a background image when one is not being uploaded or does not exist. If this parameter is defined but set to anything other than true, t or 1, the background image will stop being used.
    :type use: str
    :param include_entities: The entities node will not be included when set to false.  Example Values: false
    :type include_entities: str
    :param skip_status: When set to either true, t or 1 statuses will not be included in the returned user objects.
    :type skip_status: str

    """
    return web.Response(status=200)


async def accounts_update_profile_colors(request: web.Request, profile_background_color=None, profile_link_color=None, profile_sidebar_border_color=None, profile_sidebar_fill_color=None, profile_text_color=None, include_entities=None, skip_status=None) -> web.Response:
    """accounts_update_profile_colors

    Sets one or more hex values that control the color scheme of the authenticating user&#39;s profile page on twitter.com. Each parameter&#39;s value must be a valid hexidecimal value, and may be either three or six characters (ex: #fff or #ffffff).

    :param profile_background_color: Profile background color. Example Values: 3D3D3D
    :type profile_background_color: str
    :param profile_link_color: Profile link color.Example Values: 0000FF
    :type profile_link_color: str
    :param profile_sidebar_border_color: Profile sidebar&#39;s border color. Example Values: 0F0F0F
    :type profile_sidebar_border_color: str
    :param profile_sidebar_fill_color: Profile sidebar&#39;s background color. Example Values: 00FF00
    :type profile_sidebar_fill_color: str
    :param profile_text_color: Profile text color. Example Values: 000000
    :type profile_text_color: str
    :param include_entities: The entities node will not be included when set to false. Example Values: false
    :type include_entities: str
    :param skip_status: When set to either true, t or 1 statuses will not be included in the returned user objects.
    :type skip_status: str

    """
    return web.Response(status=200)


async def accounts_update_profile_image(request: web.Request, content_type, skip_status=None) -> web.Response:
    """accounts_update_profile_image

    Updates the authenticating user&#39;s profile image. Note that this method expects raw multipart data, not a URL to an image. This method asynchronously processes the uploaded file before updating the user&#39;s profile image URL. You can either update your local cache the next time you request the user&#39;s information, or, at least 5 seconds after uploading the image, ask for the updated URL using GET users/profile_image/:screen_name (https://dev.twitter.com/docs/api/1/get/users/profile_image/:screen_name).

    :param content_type: Content type header
    :type content_type: str
    :param skip_status: When set to either true, t or 1 statuses will not be included in the returned user objects.
    :type skip_status: str

    """
    return web.Response(status=200)


async def application_rate_limit_status(request: web.Request, resources=None) -> web.Response:
    """application_rate_limit_status

    Returns the current rate limits for methods belonging to the specified resource families.  Each 1.1 API resource belongs to a \&quot;resource family\&quot; which is indicated in its method documentation. You can typically determine a method&#39;s resource family from the first component of the path after the resource version.  This method responds with a map of methods belonging to the families specified by the resources parameter, the current remaining uses for each of those resources within the current rate limiting window, and its expiration time in epoch time. It also includes a rate_limit_context field that indicates the current access token context.  You may also issue requests to this method without any parameters to receive a map of all rate limited GET methods. If your application only uses a few of methods, please explicitly provide a resources parameter with the specified resource families you work with.

    :param resources: A comma-separated list of resource families you want to know the current rate limit disposition for. For best performance, only specify the resource families pertinent to your application.Example Values: statuses,friends,trends,help
    :type resources: str

    """
    return web.Response(status=200)


async def blocks_create(request: web.Request, include_entities=None, skip_status=None) -> web.Response:
    """blocks_create

    Blocks the specified user from following the authenticating user. In addition the blocked user will not show in the authenticating users mentions or timeline (unless retweeted by another user). If a follow or friend relationship exists it is destroyed.

    :param include_entities: The entities node will not be included when set to false.  Example Values: false
    :type include_entities: str
    :param skip_status: When set to either true, t or 1 statuses will not be included in the returned user objects.
    :type skip_status: str

    """
    return web.Response(status=200)


async def blocks_destroy(request: web.Request, include_entities=None, skip_status=None) -> web.Response:
    """blocks_destroy

    Un-blocks the user specified in the ID parameter for the authenticating user. Returns the un-blocked user in the requested format when successful. If relationships existed before the block was instated, they will not be restored.

    :param include_entities: The entities node will not be included when set to false.  Example Values: false
    :type include_entities: str
    :param skip_status: When set to either true, t or 1 statuses will not be included in the returned user objects.
    :type skip_status: str

    """
    return web.Response(status=200)


async def blocks_ids(request: web.Request, stringify_ids=None, cursor=None) -> web.Response:
    """blocks_ids

    Returns an array of numeric user ids the authenticating user is blocking.

    :param stringify_ids: Many programming environments will not consume our ids due to their size. Provide this option to have ids returned as strings instead. Read more about Twitter IDs, JSON and Snowflake.  Example Values: true
    :type stringify_ids: str
    :param cursor: Causes the list of blocked users to be broken into pages of no more than 5000 IDs at a time. The number of IDs returned is not guaranteed to be 5000 as suspended users are filtered out after connections are queried. If no cursor is provided, a value of -1 will be assumed, which is the first \&quot;page.\&quot;  The response from the API will include a previous_cursor and next_cursor to allow paging back and forth. See Using cursors to navigate collections for more information.  Example Values: 12893764510938
    :type cursor: str

    """
    return web.Response(status=200)


async def blocks_list(request: web.Request, include_entities=None, skip_status=None, cursor=None) -> web.Response:
    """blocks_list

    Allows one to enable or disable retweets and device notifications from the specified user.

    :param include_entities: The entities node will not be included when set to false. Example Values: false
    :type include_entities: str
    :param skip_status: When set to either true, t or 1 statuses will not be included in the returned user objects.
    :type skip_status: str
    :param cursor: Causes the list of blocked users to be broken into pages of no more than 5000 IDs at a time. The number of IDs returned is not guaranteed to be 5000 as suspended users are filtered out after connections are queried. If no cursor is provided, a value of -1 will be assumed, which is the first \&quot;page.\&quot;  The response from the API will include a previous_cursor and next_cursor to allow paging back and forth. See Using cursors to navigate collections for more information.  Example Values: 12893764510938
    :type cursor: str

    """
    return web.Response(status=200)


async def direct_messages(request: web.Request, count=None, since_id=None, max_id=None, include_entities=None, page=None, skip_status=None) -> web.Response:
    """direct_messages

    Returns the 20 most recent direct messages sent to the authenticating user. Includes detailed information about the sender and recipient user. You can request up to 200 direct messages per call, up to a maximum of 800 incoming DMs.  Important: This method requires an access token with RWD (read, write and direct message) permissions. Consult The Application Permission Model for more information.

    :param count: Specifies the number of direct messages to try and retrieve, up to a maximum of 200. The value of count is best thought of as a limit to the number of Tweets to return because suspended or deleted content is removed after the count has been applied.  Example Values: 5
    :type count: str
    :param since_id: Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occured since the since_id, the since_id will be forced to the oldest ID available. Example Values: 12345
    :type since_id: str
    :param max_id: Returns results with an ID less than (that is, older than) or equal to the specified ID.  Example Values: 54321
    :type max_id: str
    :param include_entities: The entities node will not be included when set to false.  Example Values: false
    :type include_entities: str
    :param page: Specifies the page of results to retrieve.  Example Values: 3
    :type page: str
    :param skip_status: When set to either true, t or 1 statuses will not be included in the returned user objects.
    :type skip_status: str

    """
    return web.Response(status=200)


async def direct_messages_destroy(request: web.Request, id, include_entities=None) -> web.Response:
    """direct_messages_destroy

    Destroys the direct message specified in the required ID parameter. The authenticating user must be the recipient of the specified direct message.  Important: This method requires an access token with RWD (read, write and direct message) permissions. Consult The Application Permission Model for more information.

    :param id: The ID of the direct message to delete.  Example Values: 1270516771
    :type id: str
    :param include_entities: The entities node will not be included when set to false.  Example Values: false
    :type include_entities: str

    """
    return web.Response(status=200)


async def direct_messages_new(request: web.Request, text) -> web.Response:
    """direct_messages_new

    Sends a new direct message to the specified user from the authenticating user. Requires both the user and text parameters and must be a POST. Returns the sent message in the requested format if successful.

    :param text: The text of your direct message. Be sure to URL encode as necessary, and keep the message under 140 characters.  Example Values: Meet me behind the cafeteria after school
    :type text: str

    """
    return web.Response(status=200)


async def direct_messages_sent(request: web.Request, count=None, since_id=None, max_id=None, include_entities=None, page=None) -> web.Response:
    """direct_messages_sent

    Returns the 20 most recent direct messages sent by the authenticating user. Includes detailed information about the sender and recipient user. You can request up to 200 direct messages per call, up to a maximum of 800 outgoing DMs.  Important: This method requires an access token with RWD (read, write and direct message) permissions. Consult The Application Permission Model for more information.

    :param count: Specifies the number of direct messages to try and retrieve, up to a maximum of 200. The value of count is best thought of as a limit to the number of Tweets to return because suspended or deleted content is removed after the count has been applied.  Example Values: 5
    :type count: str
    :param since_id: Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occured since the since_id, the since_id will be forced to the oldest ID available.  Example Values: 12345
    :type since_id: str
    :param max_id: Returns results with an ID less than (that is, older than) or equal to the specified ID.  Example Values: 54321
    :type max_id: str
    :param include_entities: The entities node will not be included when set to false.  Example Values: false
    :type include_entities: str
    :param page: Specifies the page of results to retrieve.  Example Values: 3
    :type page: str

    """
    return web.Response(status=200)


async def direct_messages_show(request: web.Request, id) -> web.Response:
    """direct_messages_show

    Returns a single direct message, specified by an id parameter. Like the /1.1/direct_messages.format request, this method will include the user objects of the sender and recipient.  Important: This method requires an access token with RWD (read, write and direct message) permissions. Consult The Application Permission Model for more information.

    :param id: The ID of the direct message.  Example Values: 587424932
    :type id: str

    """
    return web.Response(status=200)


async def favorites_create(request: web.Request, id, include_entities=None) -> web.Response:
    """favorites_create

    Favorites the status specified in the ID parameter as the authenticating user. Returns the favorite status when successful.  This process invoked by this method is asynchronous. The immediately returned status may not indicate the resultant favorited status of the tweet. A 200 OK response from this method will indicate whether the intended action was successful or not.

    :param id: The numerical ID of the desired status.  Example Values: 123
    :type id: str
    :param include_entities: The entities node will be omitted when set to false.  Example Values: false
    :type include_entities: str

    """
    return web.Response(status=200)


async def favorites_destroy(request: web.Request, id, include_entities=None) -> web.Response:
    """favorites_destroy

    Un-favorites the status specified in the ID parameter as the authenticating user. Returns the un-favorited status in the requested format when successful.  This process invoked by this method is asynchronous. The immediately returned status may not indicate the resultant favorited status of the tweet. A 200 OK response from this method will indicate whether the intended action was successful or not.

    :param id: The numerical ID of the desired status.  Example Values: 123
    :type id: str
    :param include_entities: The entities node will be omitted when set to false.  Example Values: false
    :type include_entities: str

    """
    return web.Response(status=200)


async def favorites_list(request: web.Request, count=None, since_id=None, max_id=None, include_entities=None) -> web.Response:
    """favorites_list

    Returns the 20 most recent Tweets favorited by the authenticating or specified user.

    :param count: Specifies the number of records to retrieve. Must be less than or equal to 200. Defaults to 20.  Example Values: 5
    :type count: str
    :param since_id: Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occured since the since_id, the since_id will be forced to the oldest ID available.  Example Values: 12345
    :type since_id: str
    :param max_id: Returns results with an ID less than (that is, older than) or equal to the specified ID.  Example Values: 54321
    :type max_id: str
    :param include_entities: The entities node will be omitted when set to false.  Example Values: false
    :type include_entities: str

    """
    return web.Response(status=200)


async def followers_ids(request: web.Request, stringify_ids=None, cursor=None) -> web.Response:
    """followers_ids

    Returns a cursored collection of user IDs for every user following the specified user.  At this time, results are ordered with the most recent following first — however, this ordering is subject to unannounced change and eventual consistency issues. Results are given in groups of 5,000 user IDs and multiple \&quot;pages\&quot; of results can be navigated through using the next_cursor value in subsequent requests. See Using cursors to navigate collections for more information.  This method is especially powerful when used in conjunction with GET users/lookup, a method that allows you to convert user IDs into full user objects in bulk.

    :param stringify_ids: Many programming environments will not consume our Tweet ids due to their size. Provide this option to have ids returned as strings instead. Example Values: true
    :type stringify_ids: str
    :param cursor: Causes the list of connections to be broken into pages of no more than 5000 IDs at a time. The number of IDs returned is not guaranteed to be 5000 as suspended users are filtered out after connections are queried. If no cursor is provided, a value of -1 will be assumed, which is the first \&quot;page.\&quot;  The response from the API will include a previous_cursor and next_cursor to allow paging back and forth.Example Values: 12893764510938
    :type cursor: str

    """
    return web.Response(status=200)


async def friends_ids(request: web.Request, stringify_ids=None, cursor=None) -> web.Response:
    """friends_ids

    Returns a cursored collection of user IDs for every user the specified user is following (otherwise known as their \&quot;friends\&quot;).  At this time, results are ordered with the most recent following first — however, this ordering is subject to unannounced change and eventual consistency issues. Results are given in groups of 5,000 user IDs and multiple \&quot;pages\&quot; of results can be navigated through using the next_cursor value in subsequent requests. See Using cursors to navigate collections for more information.  This method is especially powerful when used in conjunction with GET users/lookup, a method that allows you to convert user IDs into full user objects in bulk.

    :param stringify_ids: Many programming environments will not consume our Tweet ids due to their size. Provide this option to have ids returned as strings instead. Example Values: true
    :type stringify_ids: str
    :param cursor: Causes the list of connections to be broken into pages of no more than 5000 IDs at a time. The number of IDs returned is not guaranteed to be 5000 as suspended users are filtered out after connections are queried. If no cursor is provided, a value of -1 will be assumed, which is the first \&quot;page.\&quot;  The response from the API will include a previous_cursor and next_cursor to allow paging back and forth.Example Values: 12893764510938
    :type cursor: str

    """
    return web.Response(status=200)


async def friendships_create(request: web.Request, follow=None) -> web.Response:
    """friendships_create

    Allows the authenticating users to follow the user specified in the ID parameter.  Returns the befriended user in the requested format when successful. Returns a string describing the failure condition when unsuccessful. If you are already friends with the user a HTTP 403 may be returned, though for performance reasons you may get a 200 OK message even if the friendship already exists.  Actions taken in this method are asynchronous and changes will be eventually consistent.

    :param follow: Enable notifications for the target user. Example Values: true
    :type follow: str

    """
    return web.Response(status=200)


async def friendships_destroy(request: web.Request, ) -> web.Response:
    """friendships_destroy

    Allows the authenticating user to unfollow the user specified in the ID parameter.  Returns the unfollowed user in the requested format when successful. Returns a string describing the failure condition when unsuccessful.  Actions taken in this method are asynchronous and changes will be eventually consistent.


    """
    return web.Response(status=200)


async def friendships_incoming(request: web.Request, stringify_ids=None, cursor=None) -> web.Response:
    """friendships_incoming

    Returns the relationships of the authenticating user to the comma-separated list of up to 100 screen_names or user_ids provided. Values for connections can be: following, following_requested, followed_by, none.

    :param stringify_ids: Many programming environments will not consume our Tweet ids due to their size. Provide this option to have ids returned as strings instead. Example Values: true
    :type stringify_ids: str
    :param cursor: Causes the list of connections to be broken into pages of no more than 5000 IDs at a time. The number of IDs returned is not guaranteed to be 5000 as suspended users are filtered out after connections are queried. If no cursor is provided, a value of -1 will be assumed, which is the first \&quot;page.\&quot;  The response from the API will include a previous_cursor and next_cursor to allow paging back and forth.Example Values: 12893764510938
    :type cursor: str

    """
    return web.Response(status=200)


async def friendships_lookup(request: web.Request, ) -> web.Response:
    """friendships_lookup

    Returns the relationships of the authenticating user to the comma-separated list of up to 100 screen_names or user_ids provided. Values for connections can be: following, following_requested, followed_by, none.


    """
    return web.Response(status=200)


async def friendships_outgoing(request: web.Request, stringify_ids=None, cursor=None) -> web.Response:
    """friendships_outgoing

    Returns a collection of numeric IDs for every protected user for whom the authenticating user has a pending follow request.

    :param stringify_ids: Many programming environments will not consume our Tweet ids due to their size. Provide this option to have ids returned as strings instead. Example Values: true
    :type stringify_ids: str
    :param cursor: Causes the list of connections to be broken into pages of no more than 5000 IDs at a time. The number of IDs returned is not guaranteed to be 5000 as suspended users are filtered out after connections are queried. If no cursor is provided, a value of -1 will be assumed, which is the first \&quot;page.\&quot;  The response from the API will include a previous_cursor and next_cursor to allow paging back and forth.Example Values: 12893764510938
    :type cursor: str

    """
    return web.Response(status=200)


async def friendships_show(request: web.Request, target_id, target_screen_name, source_id=None, source_screen_name=None) -> web.Response:
    """friendships_show

    Returns detailed information about the relationship between two arbitrary users.

    :param target_id: The user_id of the target user.  Example Values: 20
    :type target_id: str
    :param target_screen_name: The screen_name of the target user.  Example Values: noradio
    :type target_screen_name: str
    :param source_id: The user_id of the subject user.  Example Values: 3191321
    :type source_id: str
    :param source_screen_name: The screen_name of the subject user.  Example Values: raffi
    :type source_screen_name: str

    """
    return web.Response(status=200)


async def friendships_update(request: web.Request, device, retweets) -> web.Response:
    """friendships_update

    Allows one to enable or disable retweets and device notifications from the specified user.

    :param device: Enable/disable device notifications from the target user. Example Values: true, false
    :type device: str
    :param retweets: Enable/disable retweets from the target user. Example Values: true, false
    :type retweets: str

    """
    return web.Response(status=200)


async def geo_place_id(request: web.Request, place_id) -> web.Response:
    """geo_place_id

    Returns all the information about a known place.Example Values: df51dec6f4ee2b2c

    :param place_id: A place in the world. These IDs can be retrieved from geo/reverse_geocode.  Example Values: df51dec6f4ee2b2c
    :type place_id: str

    """
    return web.Response(status=200)


async def geo_places(request: web.Request, attributestreet_address=None, param_callback=None) -> web.Response:
    """geo_places

    Creates a new place object at the given latitude and longitude.  Before creating a place you need to query GET geo/similar_places with the latitude, longitude and name of the place you wish to create. The query will return an array of places which are similar to the one you wish to create, and a token. If the place you wish to create isn&#39;t in the returned array you can use the token with this method to create a new one.

    :param attributestreet_address: This parameter searches for places which have this given street address. There are other well-known, and application specific attributes available. Custom attributes are also permitted. Learn more about Place Attributes.  Example Values: 795%20Folsom%20St
    :type attributestreet_address: str
    :param param_callback: If supplied, the response will use the JSONP format with a callback of the given name.
    :type param_callback: str

    """
    return web.Response(status=200)


async def geo_reverse_geocode(request: web.Request, lat, long, accuracy=None, granularity=None, max_results=None, param_callback=None) -> web.Response:
    """geo_reverse_geocode

    Given a latitude and a longitude, searches for up to 20 places that can be used as a place_id when updating a status.  This request is an informative call and will deliver generalized results about geography

    :param lat: The latitude to search around. This parameter will be ignored unless it is inside the range -90.0 to +90.0 (North is positive) inclusive. It will also be ignored if there isn&#39;t a corresponding long parameter.  Example Values: 37.7821120598956
    :type lat: str
    :param long: The longitude to search around. The valid ranges for longitude is -180.0 to +180.0 (East is positive) inclusive. This parameter will be ignored if outside that range, if it is not a number, if geo_enabled is disabled, or if there not a corresponding lat parameter.  Example Values: -122.400612831116
    :type long: str
    :param accuracy: A hint on the \&quot;region\&quot; in which to search. If a number, then this is a radius in meters, but it can also take a string that is suffixed with ft to specify feet. If this is not passed in, then it is assumed to be 0m. If coming from a device, in practice, this value is whatever accuracy the device has measuring its location (whether it be coming from a GPS, WiFi triangulation, etc.).  Example Values: 5ft
    :type accuracy: str
    :param granularity: This is the minimal granularity of place types to return and must be one of: poi, neighborhood, city, admin or country. If no granularity is provided for the request neighborhood is assumed. Setting this to city, for example, will find places which have a type of city, admin or country.  Example Values: city
    :type granularity: str
    :param max_results: A hint as to the number of results to return. This does not guarantee that the number of results returned will equal max_results, but instead informs how many \&quot;nearby\&quot; results to return. Ideally, only pass in the number of places you intend to display to the user here.  Example Values: 3
    :type max_results: str
    :param param_callback: If supplied, the response will use the JSONP format with a callback of the given name.
    :type param_callback: str

    """
    return web.Response(status=200)


async def geo_search(request: web.Request, accuracy=None, granularity=None, contained_within=None, attributestreet_address=None, param_callback=None) -> web.Response:
    """geo_search

    Search for places that can be attached to a statuses/update. Given a latitude and a longitude pair, an IP address, or a name, this request will return a list of all the valid places that can be used as the place_id when updating a status.  Conceptually, a query can be made from the user&#39;s location, retrieve a list of places, have the user validate the location he or she is at, and then send the ID of this location with a call to POST statuses/update.  This is the recommended method to use find places that can be attached to statuses/update. Unlike GET geo/reverse_geocode which provides raw data access, this endpoint can potentially re-order places with regards to the user who is authenticated. This approach is also preferred for interactive place matching with the user.

    :param accuracy: A hint on the \&quot;region\&quot; in which to search. If a number, then this is a radius in meters, but it can also take a string that is suffixed with ft to specify feet. If this is not passed in, then it is assumed to be 0m. If coming from a device, in practice, this value is whatever accuracy the device has measuring its location (whether it be coming from a GPS, WiFi triangulation, etc.).  Example Values: 5ft
    :type accuracy: str
    :param granularity: This is the minimal granularity of place types to return and must be one of: poi, neighborhood, city, admin or country. If no granularity is provided for the request neighborhood is assumed. Setting this to city, for example, will find places which have a type of city, admin or country.  Example Values: city
    :type granularity: str
    :param contained_within: This is the place_id which you would like to restrict the search results to. Setting this value means only places within the given place_id will be found.  Specify a place_id. For example, to scope all results to places within \&quot;San Francisco, CA USA\&quot;, you would specify a place_id of \&quot;5a110d312052166f\&quot;  Example Values: 247f43d441defc03
    :type contained_within: str
    :param attributestreet_address: This parameter searches for places which have this given street address. There are other well-known, and application specific attributes available. Custom attributes are also permitted. Learn more about Place Attributes.  Example Values: 795%20Folsom%20St
    :type attributestreet_address: str
    :param param_callback: If supplied, the response will use the JSONP format with a callback of the given name.
    :type param_callback: str

    """
    return web.Response(status=200)


async def geo_similar_places(request: web.Request, contained_within=None, attributestreet_address=None, param_callback=None) -> web.Response:
    """geo_similar_places

    Locates places near the given coordinates which are similar in name.  Conceptually you would use this method to get a list of known places to choose from first. Then, if the desired place doesn&#39;t exist, make a request to POST geo/place to create a new one.  The token contained in the response is the token needed to be able to create a new place.

    :param contained_within: This is the place_id which you would like to restrict the search results to. Setting this value means only places within the given place_id will be found.  Specify a place_id. For example, to scope all results to places within \&quot;San Francisco, CA USA\&quot;, you would specify a place_id of \&quot;5a110d312052166f\&quot;  Example Values: 247f43d441defc03
    :type contained_within: str
    :param attributestreet_address: This parameter searches for places which have this given street address. There are other well-known, and application specific attributes available. Custom attributes are also permitted. Learn more about Place Attributes.  Example Values: 795%20Folsom%20St
    :type attributestreet_address: str
    :param param_callback: If supplied, the response will use the JSONP format with a callback of the given name.
    :type param_callback: str

    """
    return web.Response(status=200)


async def help_configurations(request: web.Request, ) -> web.Response:
    """help_configurations

    Returns the current configuration used by Twitter including twitter.com slugs which are not usernames, maximum photo resolutions, and t.co URL lengths.  It is recommended applications request this endpoint when they are loaded, but no more than once a day.


    """
    return web.Response(status=200)


async def help_languages(request: web.Request, ) -> web.Response:
    """help_languages

    Returns the list of languages supported by Twitter along with their ISO 639-1 code. The ISO 639-1 code is the two letter value to use if you include lang with any of your requests.


    """
    return web.Response(status=200)


async def help_privacy(request: web.Request, ) -> web.Response:
    """help_privacy

    Returns Twitter&#39;s Privacy Policy


    """
    return web.Response(status=200)


async def help_tos(request: web.Request, ) -> web.Response:
    """help_tos

    Returns the Twitter Terms of Service in the requested format. These are not the same as the Developer Rules of the Road.


    """
    return web.Response(status=200)


async def lists_create(request: web.Request, name, mode=None, description=None) -> web.Response:
    """lists_create

    Creates a new list for the authenticated user. Note that you can&#39;t create more than 20 lists per account.

    :param name: The name for the list.A list&#39;s name must start with a letter and can consist only of 25 or fewer letters, numbers, \&quot;-\&quot;, or \&quot;_\&quot; characters.
    :type name: str
    :param mode: Whether your list is public or private. Values can be public or private. If no mode is specified the list will be public.
    :type mode: str
    :param description: The description to give the list.
    :type description: str

    """
    return web.Response(status=200)


async def lists_destroy(request: web.Request, owner_screen_name=None, owner_id=None) -> web.Response:
    """lists_destroy

    Deletes the specified list. The authenticated user must own the list to be able to destroy it.

    :param owner_screen_name: The screen name of the user who owns the list being requested by a slug.
    :type owner_screen_name: str
    :param owner_id: The user ID of the user who owns the list being requested by a slug.
    :type owner_id: str

    """
    return web.Response(status=200)


async def lists_list(request: web.Request, screen_name, user_id) -> web.Response:
    """lists_list

    Returns all lists the authenticating or specified user subscribes to, including their own. The user is specified using the user_id or screen_name parameters. If no user is given, the authenticating user is used.  This method used to be GET lists in version 1.0 of the API and has been renamed for consistency with other call.

    :param screen_name: The screen name of the user for whom to return results for. Helpful for disambiguating when a valid screen name is also a user ID.  Example Values: noradio
    :type screen_name: str
    :param user_id: The ID of the user for whom to return results for. Helpful for disambiguating when a valid user ID is also a valid screen name.  Example Values: 12345  Note:: Specifies the ID of the user to get lists from. Helpful for disambiguating when a valid user ID is also a valid screen name.
    :type user_id: str

    """
    return web.Response(status=200)


async def lists_members(request: web.Request, owner_screen_name=None, owner_id=None, include_entities=None, skip_status=None, cursor=None) -> web.Response:
    """lists_members

    Returns the members of the specified list. Private list members will only be shown if the authenticated user owns the specified list.

    :param owner_screen_name: The screen name of the user who owns the list being requested by a slug.
    :type owner_screen_name: str
    :param owner_id: The user ID of the user who owns the list being requested by a slug.
    :type owner_id: str
    :param include_entities: The entities node will be disincluded when set to false.  Example Values: false
    :type include_entities: str
    :param skip_status: When set to either true, t or 1 statuses will not be included in the returned user objects.
    :type skip_status: str
    :param cursor: Causes the collection of list members to be broken into \&quot;pages\&quot; of somewhat consistent size. If no cursor is provided, a value of -1 will be assumed, which is the first \&quot;page.\&quot;  The response from the API will include a previous_cursor and next_cursor to allow paging back and forth. See Using cursors to navigate collections for more information.  Example Values: 12893764510938
    :type cursor: str

    """
    return web.Response(status=200)


async def lists_members_create(request: web.Request, owner_screen_name=None, owner_id=None) -> web.Response:
    """lists_members_create

    Add a member to a list. The authenticated user must own the list to be able to add members to it. Note that lists can&#39;t have more than 500 members.

    :param owner_screen_name: The screen name of the user who owns the list being requested by a slug.
    :type owner_screen_name: str
    :param owner_id: The user ID of the user who owns the list being requested by a slug.
    :type owner_id: str

    """
    return web.Response(status=200)


async def lists_members_create_all(request: web.Request, owner_screen_name=None, owner_id=None, user_id=None, screen_name=None) -> web.Response:
    """lists_members_create_all

    Adds multiple members to a list, by specifying a comma-separated list of member ids or screen names. The authenticated user must own the list to be able to add members to it. Note that lists can&#39;t have more than 500 members, and you are limited to adding up to 100 members to a list at a time with this method.  Please note that there can be issues with lists that rapidly remove and add memberships. Take care when using these methods such that you are not too rapidly switching between removals and adds on the same list.

    :param owner_screen_name: The screen name of the user who owns the list being requested by a slug.
    :type owner_screen_name: str
    :param owner_id: The user ID of the user who owns the list being requested by a slug.
    :type owner_id: str
    :param user_id: A comma separated list of user IDs, up to 100 are allowed in a single request.
    :type user_id: str
    :param screen_name: A comma separated list of screen names, up to 100 are allowed in a single request.
    :type screen_name: str

    """
    return web.Response(status=200)


async def lists_members_destroy(request: web.Request, list_id, slug, owner_screen_name=None, owner_id=None, user_id=None, screen_name=None) -> web.Response:
    """lists_members_destroy

    Removes the specified member from the list. The authenticated user must be the list&#39;s owner to remove members from the list.

    :param list_id: The numerical id of the list.
    :type list_id: str
    :param slug: You can identify a list by its slug instead of its numerical id. If you decide to do so, note that you&#39;ll also have to specify the list owner using the owner_id or owner_screen_name parameters.
    :type slug: str
    :param owner_screen_name: The screen name of the user who owns the list being requested by a slug.
    :type owner_screen_name: str
    :param owner_id: The user ID of the user who owns the list being requested by a slug.
    :type owner_id: str
    :param user_id: The ID of the user to remove from the list. Helpful for disambiguating when a valid user ID is also a valid screen name.
    :type user_id: str
    :param screen_name: The screen name of the user for whom to remove from the list. Helpful for disambiguating when a valid screen name is also a user ID.
    :type screen_name: str

    """
    return web.Response(status=200)


async def lists_members_destroy_all(request: web.Request, owner_screen_name=None, owner_id=None, screen_name=None, user_id=None) -> web.Response:
    """lists_members_destroy_all

    Removes multiple members from a list, by specifying a comma-separated list of member ids or screen names. The authenticated user must own the list to be able to remove members from it. Note that lists can&#39;t have more than 500 members, and you are limited to removing up to 100 members to a list at a time with this method.  Please note that there can be issues with lists that rapidly remove and add memberships. Take care when using these methods such that you are not too rapidly switching between removals and adds on the same list.

    :param owner_screen_name: The screen name of the user who owns the list being requested by a slug.
    :type owner_screen_name: str
    :param owner_id: The user ID of the user who owns the list being requested by a slug.
    :type owner_id: str
    :param screen_name: A comma separated list of screen names, up to 100 are allowed in a single request.
    :type screen_name: str
    :param user_id: A comma separated list of user IDs, up to 100 are allowed in a single request.
    :type user_id: str

    """
    return web.Response(status=200)


async def lists_members_show(request: web.Request, owner_screen_name=None, owner_id=None, include_entities=None, skip_status=None) -> web.Response:
    """lists_members_show

    Check if the specified user is a member of the specified list.

    :param owner_screen_name: The screen name of the user who owns the list being requested by a slug.
    :type owner_screen_name: str
    :param owner_id: The user ID of the user who owns the list being requested by a slug.
    :type owner_id: str
    :param include_entities: When set to either true, t or 1, each tweet will include a node called \&quot;entities\&quot;. This node offers a variety of metadata about the tweet in a discreet structure, including: user_mentions, urls, and hashtags. While entities are opt-in on timelines at present, they will be made a default component of output in the future.
    :type include_entities: str
    :param skip_status: When set to either true, t or 1 statuses will not be included in the returned user objects.
    :type skip_status: str

    """
    return web.Response(status=200)


async def lists_memberships(request: web.Request, user_id=None, screen_name=None, cursor=None, filter_to_owned_lists=None) -> web.Response:
    """lists_memberships

    Returns the lists the specified user has been added to. If user_id or screen_name are not provided the memberships for the authenticating user are returned.

    :param user_id: The ID of the user for whom to return results for. Helpful for disambiguating when a valid user ID is also a valid screen name.
    :type user_id: str
    :param screen_name: The screen name of the user for whom to return results for. Helpful for disambiguating when a valid screen name is also a user ID.
    :type screen_name: str
    :param cursor: Breaks the results into pages. A single page contains 20 lists. Provide a value of -1 to begin paging. Provide values as returned in the response body&#39;s next_cursor and previous_cursor attributes to page back and forth in the list.
    :type cursor: str
    :param filter_to_owned_lists: When set to true, t or 1, will return just lists the authenticating user owns, and the user represented by user_id or screen_name is a member of.
    :type filter_to_owned_lists: str

    """
    return web.Response(status=200)


async def lists_show(request: web.Request, owner_screen_name=None, owner_id=None) -> web.Response:
    """lists_show

    Returns the specified list. Private lists will only be shown if the authenticated user owns the specified list.

    :param owner_screen_name: The screen name of the user who owns the list being requested by a slug.
    :type owner_screen_name: str
    :param owner_id: The user ID of the user who owns the list being requested by a slug.
    :type owner_id: str

    """
    return web.Response(status=200)


async def lists_statuses(request: web.Request, include_rts, owner_screen_name=None, owner_id=None, since_id=None, max_id=None, count=None, include_entities=None) -> web.Response:
    """lists_statuses

    Returns tweet timeline for members of the specified list. Retweets are included by default. You can use the include_rts&#x3D;false parameter to omit retweet objects.

    :param include_rts: When set to either true, t or 1, the list timeline will contain native retweets (if they exist) in addition to the standard stream of tweets. The output format of retweeted tweets is identical to the representation you see in home_timeline.
    :type include_rts: str
    :param owner_screen_name: The screen name of the user who owns the list being requested by a slug.
    :type owner_screen_name: str
    :param owner_id: The user ID of the user who owns the list being requested by a slug.
    :type owner_id: str
    :param since_id: Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occured since the since_id, the since_id will be forced to the oldest ID available.
    :type since_id: str
    :param max_id: Returns results with an ID less than (that is, older than) or equal to the specified ID.
    :type max_id: str
    :param count: Specifies the number of results to retrieve per \&quot;page.
    :type count: str
    :param include_entities: Entities are ON by default in API 1.1, each tweet includes a node called \&quot;entities\&quot;. This node offers a variety of metadata about the tweet in a discreet structure, including: user_mentions, urls, and hashtags. You can omit entities from the result by using include_entities&#x3D;false
    :type include_entities: str

    """
    return web.Response(status=200)


async def lists_subscribers(request: web.Request, owner_screen_name=None, owner_id=None, cursor=None, include_entities=None, skip_status=None) -> web.Response:
    """lists_subscribers

    Returns the subscribers of the specified list. Private list subscribers will only be shown if the authenticated user owns the specified list.

    :param owner_screen_name: The screen name of the user who owns the list being requested by a slug.
    :type owner_screen_name: str
    :param owner_id: The user ID of the user who owns the list being requested by a slug.
    :type owner_id: str
    :param cursor: Breaks the results into pages. A single page contains 20 lists. Provide a value of -1 to begin paging. Provide values as returned in the response body&#39;s next_cursor and previous_cursor attributes to page back and forth in the list.
    :type cursor: str
    :param include_entities: When set to either true, t or 1, each tweet will include a node called \&quot;entities\&quot;. This node offers a variety of metadata about the tweet in a discreet structure, including: user_mentions, urls, and hashtags. While entities are opt-in on timelines at present, they will be made a default component of output in the future. See Tweet Entities for more details.
    :type include_entities: str
    :param skip_status: When set to either true, t or 1 statuses will not be included in the returned user objects.
    :type skip_status: str

    """
    return web.Response(status=200)


async def lists_subscribers_create(request: web.Request, owner_screen_name=None, owner_id=None) -> web.Response:
    """lists_subscribers_create

    Subscribes the authenticated user to the specified list.

    :param owner_screen_name: The screen name of the user who owns the list being requested by a slug.
    :type owner_screen_name: str
    :param owner_id: The user ID of the user who owns the list being requested by a slug.
    :type owner_id: str

    """
    return web.Response(status=200)


async def lists_subscribers_destroy(request: web.Request, owner_screen_name=None, owner_id=None) -> web.Response:
    """lists_subscribers_destroy

    Unsubscribes the authenticated user from the specified list.

    :param owner_screen_name: The screen name of the user who owns the list being requested by a slug.
    :type owner_screen_name: str
    :param owner_id: The user ID of the user who owns the list being requested by a slug.
    :type owner_id: str

    """
    return web.Response(status=200)


async def lists_subscribers_show(request: web.Request, owner_screen_name=None, owner_id=None, include_entities=None, skip_status=None) -> web.Response:
    """lists_subscribers_show

    Check if the specified user is a subscriber of the specified list. Returns the user if they are subscriber.

    :param owner_screen_name: The screen name of the user who owns the list being requested by a slug.
    :type owner_screen_name: str
    :param owner_id: The user ID of the user who owns the list being requested by a slug.
    :type owner_id: str
    :param include_entities: When set to either true, t or 1, each tweet will include a node called \&quot;entities\&quot;. This node offers a variety of metadata about the tweet in a discreet structure, including: user_mentions, urls, and hashtags. While entities are opt-in on timelines at present, they will be made a default component of output in the future. See Tweet Entities for more details.
    :type include_entities: str
    :param skip_status: When set to either true, t or 1 statuses will not be included in the returned user objects.
    :type skip_status: str

    """
    return web.Response(status=200)


async def lists_subscriptions(request: web.Request, count=None, cursor=None) -> web.Response:
    """lists_subscriptions

    Obtain a collection of the lists the specified user is subscribed to, 20 lists per page by default. Does not include the user&#39;s own lists.

    :param count: The amount of results to return per page. Defaults to 20. Maximum of 1,000 when using cursors.
    :type count: str
    :param cursor: Breaks the results into pages. A single page contains 20 lists. Provide a value of -1 to begin paging. Provide values as returned in the response body&#39;s next_cursor and previous_cursor attributes to page back and forth in the list. It is recommended to always use cursors when the method supports them.
    :type cursor: str

    """
    return web.Response(status=200)


async def lists_update(request: web.Request, owner_screen_name=None, owner_id=None, name=None, mode=None, description=None) -> web.Response:
    """lists_update

    Updates the specified list. The authenticated user must own the list to be able to update it.

    :param owner_screen_name: The screen name of the user who owns the list being requested by a slug.
    :type owner_screen_name: str
    :param owner_id: The user ID of the user who owns the list being requested by a slug.
    :type owner_id: str
    :param name: The name for the list.
    :type name: str
    :param mode: Whether your list is public or private. Values can be public or private. If no mode is specified the list will be public.
    :type mode: str
    :param description: The description to give the list.
    :type description: str

    """
    return web.Response(status=200)


async def saved_searches_create(request: web.Request, query) -> web.Response:
    """saved_searches_create

    Create a new saved search for the authenticated user. A user may only have 25 saved searches.

    :param query: The query of the search the user would like to save.
    :type query: str

    """
    return web.Response(status=200)


async def saved_searches_destroy(request: web.Request, id) -> web.Response:
    """saved_searches_destroy

    Destroys a saved search for the authenticating user. The authenticating user must be the owner of saved search id being destroyed.

    :param id: The ID of the saved search.  Example Values: 313006
    :type id: str

    """
    return web.Response(status=200)


async def saved_searches_list(request: web.Request, ) -> web.Response:
    """saved_searches_list

    Returns the authenticated user&#39;s saved search queries.


    """
    return web.Response(status=200)


async def savedsearchesid(request: web.Request, id) -> web.Response:
    """savedsearchesid

    Returns the authenticated user&#39;s saved search queries.

    :param id: The ID of the saved search.  Example Values: 313006
    :type id: str

    """
    return web.Response(status=200)


async def search_tweets(request: web.Request, q, geocode=None, lang=None, locale=None, result_type=None, count=None, until=None, since_id=None, max_id=None, include_entities=None, param_callback=None) -> web.Response:
    """search_tweets

    Returns a collection of relevant Tweets matching a specified query.  Please note that Twitter&#39;s search service and, by extension, the Search API is not meant to be an exhaustive source of Tweets. Not all Tweets will be indexed or made available via the search interface.  In API v1.1, the response format of the Search API has been improved to return Tweet objects more similar to the objects you&#39;ll find across the REST API and platform. You may need to tolerate some inconsistencies and variance in perspectival values (fields that pertain to the perspective of the authenticating user) and embedded user objects.

    :param q: A UTF-8, URL-encoded search query of 1,000 characters maximum, including operators. Queries may additionally be limited by complexity.Example: @noradio.
    :type q: str
    :param geocode: Returns tweets by users located within a given radius of the given latitude/longitude. The location is preferentially taking from the Geotagging API, but will fall back to their Twitter profile. The parameter value is specified by \&quot;latitude,longitude,radius\&quot;, where radius units must be specified as either \&quot;mi\&quot; (miles) or \&quot;km\&quot; (kilometers). Note that you cannot use the near operator via the API to geocode arbitrary locations; however you can use this geocode parameter to search near geocodes directly. A maximum of 1,000 distinct \&quot;sub-regions\&quot; will be considered when using the radius modifier.
    :type geocode: str
    :param lang: Restricts tweets to the given language, given by an ISO 639-1 code. Language detection is best-effort.Example Values: eu
    :type lang: str
    :param locale: Specify the language of the query you are sending (only ja is currently effective). This is intended for language-specific consumers and the default should work in the majority of cases.Example Values: ja
    :type locale: str
    :param result_type: Optional. Specifies what type of search results you would prefer to receive. The current default is \&quot;mixed.\&quot; Valid values include: * mixed: Include both popular and real time results in the response. * recent: return only the most recent results in the response * popular: return only the most popular results in the response. Example Values: mixed, recent, popular
    :type result_type: str
    :param count: The number of tweets to return per page, up to a maximum of 100. Defaults to 15. This was formerly the \&quot;rpp\&quot; parameter in the old Search API. Example Values: 100
    :type count: str
    :param until: Returns tweets generated before the given date. Date should be formatted as YYYY-MM-DD. Keep in mind that the search index may not go back as far as the date you specify here. Example Values: 2012-09-01
    :type until: str
    :param since_id: Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occured since the since_id, the since_id will be forced to the oldest ID available. Example Values: 12345
    :type since_id: str
    :param max_id: Returns results with an ID less than (that is, older than) or equal to the specified ID. Example Values: 12345
    :type max_id: str
    :param include_entities: The entities node will be disincluded when set to false. Example Values: false
    :type include_entities: str
    :param param_callback: If supplied, the response will use the JSONP format with a callback of the given name. The usefulness of this parameter is somewhat diminished by the requirement of authentication for requests to this endpoint. Example Values: processTweets
    :type param_callback: str

    """
    return web.Response(status=200)


async def statuses_destroy(request: web.Request, id, trim_user=None) -> web.Response:
    """statuses_destroy

    Destroys the status specified by the required ID parameter. The authenticating user must be the author of the specified status. Returns the destroyed status if successful.

    :param id: The numerical ID of the desired status.
    :type id: str
    :param trim_user: When set to either true, t or 1, each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object.
    :type trim_user: str

    """
    return web.Response(status=200)


async def statuses_home_timeline(request: web.Request, count=None, max_id=None, since_id=None, trim_user=None, exclude_replies=None, contributor_details=None) -> web.Response:
    """statuses_home_timeline

    Returns a collection of the most recent Tweets and retweets posted by the authenticating user and the users they follow. The home timeline is central to how most users interact with the Twitter service.  Up to 800 Tweets are obtainable on the home timeline. It is more volatile for users that follow many users or follow users who tweet frequently.

    :param count: Specifies the number of records to retrieve. Must be less than or equal to 200.
    :type count: int
    :param max_id: Returns results with an ID less than (that is, older than) or equal to the specified ID.
    :type max_id: int
    :param since_id: Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occured since the since_id, the since_id will be forced to the oldest ID available.
    :type since_id: int
    :param trim_user: When set to either true, t or 1, each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object.
    :type trim_user: str
    :param exclude_replies: This parameter will prevent replies from appearing in the returned timeline. Using exclude_replies with the count parameter will mean you will receive up-to count tweets — this is because the count parameter retrieves that many tweets before filtering out retweets and replies.
    :type exclude_replies: str
    :param contributor_details: This parameter enhances the contributors element of the status response to include the screen_name of the contributor. By default only the user_id of the contributor is included.
    :type contributor_details: str

    """
    return web.Response(status=200)


async def statuses_mentions_timeline(request: web.Request, count=None, since_id=None, max_id=None, trim_user=None, contributor_details=None, include_entities=None) -> web.Response:
    """statuses_mentions_timeline

    Returns the 20 most recent mentions (tweets containing a users&#39;s @screen_name) for the authenticating user.The timeline returned is the equivalent of the one seen when you view your mentions on twitter.com.This method can only return up to 800 statuses.This method will include retweets in the JSON response regardless of whether the include_rts parameter is set.

    :param count: Specifies the number of tweets to try and retrieve, up to a maximum of 200. The value of count is best thought of as a limit to the number of tweets to return because suspended or deleted content is removed after the count has been applied. We include retweets in the count, even if include_rts is not supplied. It is recommended you always send include_rts&#x3D;1 when using this API method.
    :type count: int
    :param since_id: Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occured since the since_id, the since_id will be forced to the oldest ID available.
    :type since_id: int
    :param max_id: Returns results with an ID less than (that is, older than) or equal to the specified ID.
    :type max_id: int
    :param trim_user: When set to either true, t or 1, each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object.
    :type trim_user: str
    :param contributor_details: This parameter enhances the contributors element of the status response to include the screen_name of the contributor. By default only the user_id of the contributor is included.
    :type contributor_details: str
    :param include_entities: The entities node will be disincluded when set to false.
    :type include_entities: bool

    """
    return web.Response(status=200)


async def statuses_oembed(request: web.Request, maxwidth=None, hide_media=None, hide_thread=None, omit_script=None, align=None, related=None, lang=None) -> web.Response:
    """statuses_oembed

    Returns information allowing the creation of an embedded representation of a Tweet on third party sites. See the oEmbed specification (http://oembed.com) for information about the response format. Either the id or url parameters must be specified in a request, it is not necessary to include both. While this endpoint allows a bit of customization for the final appearance of the embedded Tweet, be aware that the appearance of the rendered Tweet may change over time to be consistent with Twitter&#39;s Display Guidelines (https://dev.twitter.com/terms/display-guidelines). Do not rely on any class or id parameters to stay constant in the returned markup.

    :param maxwidth: The maximum width in pixels that the embed should be rendered at. This value is constrained to be between 250 and 550 pixels. Note that Twitter does not support the oEmbed maxheight parameter. Tweets are fundamentally text, and are therefore of unpredictable height that cannot be scaled like an image or video. Relatedly, the oEmbed response will not provide a value for height. Implementations that need consistent heights for Tweets should refer to the hide_thread and hide_media parameters below.
    :type maxwidth: int
    :param hide_media: Specifies whether the embedded Tweet should automatically expand images which were uploaded via POST statuses/update_with_media. When set to either true, t or 1 images will not be expanded. Defaults to false.
    :type hide_media: str
    :param hide_thread: Specifies whether the embedded Tweet should automatically show the original message in the case that the embedded Tweet is a reply. When set to either true, t or 1 the original Tweet will not be shown. Defaults to false.
    :type hide_thread: str
    :param omit_script: Specifies whether the embedded Tweet HTML should include a &#39;script&#39; element pointing to widgets.js. In cases where a page already includes widgets.js, setting this value to true will prevent a redundant script element from being included. When set to either true, t or 1 the &#39;script&#39;element will not be included in the embed HTML, meaning that pages must include a reference to widgets.js manually. Defaults to false.
    :type omit_script: str
    :param align: Specifies whether the embedded Tweet should be left aligned, right aligned, or centered in the page. Valid values are left, right, center, and none. Defaults to none, meaning no alignment styles are specified for the Tweet.
    :type align: str
    :param related: A value for the TWT related parameter, as described in Web Intents (https://dev.twitter.com/docs/intents). This value will be forwarded to all Web Intents calls. Example values: twitterapi, twittermedia, twitter.
    :type related: str
    :param lang: Language code for the rendered embed. This will affect the text and localization of the rendered HTML. Example value: fr
    :type lang: str

    """
    return web.Response(status=200)


async def statuses_retweets(request: web.Request, id, count=None, trim_user=None) -> web.Response:
    """statuses_retweets

    Returns up to 100 of the first retweets of a given tweet.

    :param id: The numerical ID of the desired status.
    :type id: str
    :param count: Specifies the number of records to retrieve. Must be less than or equal to 100.
    :type count: str
    :param trim_user: When set to either true, t or 1, each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object.
    :type trim_user: str

    """
    return web.Response(status=200)


async def statuses_show(request: web.Request, id, trim_user=None, include_my_retweet=None, include_entities=None) -> web.Response:
    """statuses_show

    Returns a single status, specified by the id parameter below. The status&#39;s author will be returned inline.

    :param id: The numerical ID of the desired status.
    :type id: str
    :param trim_user: When set to either true, t or 1, each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object.
    :type trim_user: str
    :param include_my_retweet: When set to either true, t or 1, any Tweets returned that have been retweeted by the authenticating user will include an additional current_user_retweet node, containing the ID of the source status for the retweet.
    :type include_my_retweet: str
    :param include_entities: The entities node will be disincluded when set to false.
    :type include_entities: str

    """
    return web.Response(status=200)


async def statuses_update(request: web.Request, status, in_reply_to_status_id=None, lat=None, long=None, place_id=None, display_coordinates=None, trim_user=None) -> web.Response:
    """statuses_update

    Updates the authenticating user&#39;s status, also known as tweeting. To upload an image to accompany the tweet, use POST statuses/update_with_media (https://dev.twitter.com/docs/api/1/post/statuses/update_with_media). For each update attempt, the update text is compared with the authenticating user&#39;s recent tweets. Any attempt that would result in duplication will be blocked, resulting in a 403 error. Therefore, a user cannot submit the same status twice in a row. While not rate limited by the API a user is limited in the number of tweets they can create at a time. If the number of updates posted by the user reaches the current allowed limit this method will return an HTTP 403 error.

    :param status: The text of your status update, typically up to 140 characters. URL encode as necessary. t.co link short-url wrapping (https://dev.twitter.com/docs/tco-link-wrapper/faq) may effect character counts.
    :type status: str
    :param in_reply_to_status_id: The ID of an existing status that the update is in reply to. Note: This parameter will be ignored unless the author of the tweet this parameter references is mentioned within the status text. Therefore, you must include @username, where username is the author of the referenced tweet, within the update.
    :type in_reply_to_status_id: str
    :param lat: The latitude of the location this tweet refers to. This parameter will be ignored unless it is inside the range -90.0 to +90.0 (North is positive) inclusive. It will also be ignored if there isn&#39;t a corresponding long parameter.
    :type lat: str
    :param long: The longitude of the location this tweet refers to. The valid ranges for longitude is -180.0 to +180.0 (East is positive) inclusive. This parameter will be ignored if outside that range, if it is not a number, if geo_enabled is disabled, or if there not a corresponding lat parameter.
    :type long: str
    :param place_id: A place in the world. These IDs can be retrieved from GET geo/reverse_geocode (https://dev.twitter.com/docs/api/1/get/geo/reverse_geocode).
    :type place_id: str
    :param display_coordinates: Whether or not to put a pin on the exact coordinates a tweet has been sent from.
    :type display_coordinates: str
    :param trim_user: When set to either true, t or 1, each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object.
    :type trim_user: str

    """
    return web.Response(status=200)


async def statuses_update_with_media(request: web.Request, status, media, content_type, possibly_sensitive=None, in_reply_to_status_id=None, lat=None, long=None, place_id=None, display_coordinates=None) -> web.Response:
    """statuses_update_with_media

    Updates the authenticating user&#39;s status and attaches media for upload. Unlike POST statuses/update (https://dev.twitter.com/docs/api/1.1/post/statuses/update), this method expects raw multipart data. Your POST request&#39;s Content-Type should be set to multipart/form-data with the media[] parameter. The Tweet text will be rewritten to include the media URL(s), which will reduce the number of characters allowed in the Tweet text. If the URL(s) cannot be appended without text truncation, the tweet will be rejected and this method will return an HTTP 403 error. Important: Make sure that you&#39;re using upload.twitter.com as your host while posting statuses with media. It is strongly recommended to use SSL with this method.

    :param status: The text of your status update. URL encode as necessary. t.co link wrapping (https://dev.twitter.com/docs/tco-link-wrapper/faq) may affect character counts if the post contains URLs. You must additionally account for the characters_reserved_per_media per uploaded media, additionally accounting for space characters in between finalized URLs. Note: Request the GET help/configuration (https://dev.twitter.com/docs/api/1.1/get/help/configuration) endpoint to get the current characters_reserved_per_media and max_media_per_upload values.
    :type status: str
    :param media: Up to max_media_per_upload files may be specified in the request, each named media[]. Supported image formats are PNG, JPG and GIF. Animated GIFs are not supported. Note: Request the GET help/configuration (https://dev.twitter.com/docs/api/1.1/get/help/configuration) endpoint to get the current max_media_per_upload and photo_size_limit values.
    :type media: str
    :param content_type: Content type.
    :type content_type: str
    :param possibly_sensitive: Set to true for content which may not be suitable for every audience.
    :type possibly_sensitive: str
    :param in_reply_to_status_id: The ID of an existing status that the update is in reply to. Note: This parameter will be ignored unless the author of the tweet this parameter references is mentioned within the status text. Therefore, you must include @username, where username is the author of the referenced tweet, within the update.
    :type in_reply_to_status_id: str
    :param lat: The latitude of the location this tweet refers to. This parameter will be ignored unless it is inside the range -90.0 to +90.0 (North is positive) inclusive. It will also be ignored if there isn&#39;t a corresponding long parameter. Example value: 37.7821120598956.
    :type lat: str
    :param long: The longitude of the location this tweet refers to. The valid ranges for longitude is -180.0 to +180.0 (East is positive) inclusive. This parameter will be ignored if outside that range, not a number, geo_enabled is disabled, or if there not a corresponding lat parameter. Example value: -122.400612831116.
    :type long: str
    :param place_id: A place in the world identified by a Twitter place ID. Place IDs can be retrieved from geo/reverse_geocode.
    :type place_id: str
    :param display_coordinates: Whether or not to put a pin on the exact coordinates a tweet has been sent from.
    :type display_coordinates: str

    """
    return web.Response(status=200)


async def statuses_user_timeline(request: web.Request, count=None, since_id=None, max_id=None, trim_user=None, exclude_replies=None, contributor_details=None, include_rts=None) -> web.Response:
    """statuses_user_timeline

    Returns the 20 most recent statuses posted by the authenticating user. It is also possible to request another user&#39;s timeline by using the screen_name or user_id parameter. The other users timeline will only be visible if they are not protected, or if the authenticating user&#39;s follow request was accepted by the protected user. The timeline returned is the equivalent of the one seen when you view a user&#39;s profile on twitter.com. This method can only return up to 3,200 of a user&#39;s most recent statuses. Native retweets of other statuses by the user is included in this total, regardless of whether include_rts is specified when requesting this resource. This method will not include retweets in the XML and JSON responses unless the include_rts parameter is set. The RSS and Atom responses will always include retweets as statuses prefixed with RT, regardless of provided parameters. Always specify either an user_id or screen_name when requesting a user timeline.

    :param count: Specifies the number of tweets to try and retrieve, up to a maximum of 200. The value of count is best thought of as a limit to the number of tweets to return because suspended or deleted content is removed after the count has been applied. We include retweets in the count, even if include_rts is not supplied. It is recommended you always send include_rts&#x3D;1 when using this API method.
    :type count: int
    :param since_id: Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occured since the since_id, the since_id will be forced to the oldest ID available.
    :type since_id: int
    :param max_id: Returns results with an ID less than (that is, older than) or equal to the specified ID.
    :type max_id: int
    :param trim_user: When set to either true, t or 1, each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object.
    :type trim_user: str
    :param exclude_replies: This parameter will prevent replies from appearing in the returned timeline. Using exclude_replies with the count parameter will mean you will receive up-to count tweets — this is because the count parameter retrieves that many tweets before filtering out retweets and replies. This parameter is only supported for JSON and XML responses.
    :type exclude_replies: bool
    :param contributor_details: This parameter enhances the contributors element of the status response to include the screen_name of the contributor. By default only the user_id of the contributor is included.
    :type contributor_details: bool
    :param include_rts: When set to false, the timeline will strip any native retweets (though they will still count toward both the maximal length of the timeline and the slice selected by the count parameter). Note: If you&#39;re using the trim_user parameter in conjunction with include_rts, the retweets will still contain a full user object.
    :type include_rts: bool

    """
    return web.Response(status=200)


async def statusesretweetid(request: web.Request, id, trim_user=None) -> web.Response:
    """statusesretweetid

    Retweets a tweet. Returns the original tweet with retweet details embedded.

    :param id: The numerical ID of the desired status.
    :type id: str
    :param trim_user: When set to either true, t or 1, each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object.
    :type trim_user: str

    """
    return web.Response(status=200)


async def trends_available(request: web.Request, ) -> web.Response:
    """trends_available

    Returns the locations that Twitter has trending topic information for.  The response is an array of \&quot;locations\&quot; that encode the location&#39;s WOEID and some other human-readable information such as a canonical name and country the location belongs in.  A WOEID is a Yahoo! Where On Earth ID.


    """
    return web.Response(status=200)


async def trends_closest(request: web.Request, lat=None, long=None) -> web.Response:
    """trends_closest

    Returns the locations that Twitter has trending topic information for, closest to a specified location.  The response is an array of \&quot;locations\&quot; that encode the location&#39;s WOEID and some other human-readable information such as a canonical name and country the location belongs in.  A WOEID is a Yahoo! Where On Earth ID.

    :param lat: If provided with a long parameter the available trend locations will be sorted by distance, nearest to furthest, to the co-ordinate pair. The valid ranges for longitude is -180.0 to +180.0 (West is negative, East is positive) inclusive.  Example Values: 37.781157
    :type lat: str
    :param long: If provided with a lat parameter the available trend locations will be sorted by distance, nearest to furthest, to the co-ordinate pair. The valid ranges for longitude is -180.0 to +180.0 (West is negative, East is positive) inclusive.  Example Values: -122.400612831116
    :type long: str

    """
    return web.Response(status=200)


async def trends_place(request: web.Request, id, exclude=None) -> web.Response:
    """trends_place

    Returns the top 10 trending topics for a specific WOEID, if trending information is available for it.  The response is an array of \&quot;trend\&quot; objects that encode the name of the trending topic, the query parameter that can be used to search for the topic on Twitter Search, and the Twitter Search URL.  This information is cached for 5 minutes. Requesting more frequently than that will not return any more data, and will count against your rate limit usage.

    :param id: The Yahoo! Where On Earth ID of the location to return trending information for. Global information is available by using 1 as the WOEID.
    :type id: str
    :param exclude: Setting this equal to hashtags will remove all hashtags from the trends list.
    :type exclude: str

    """
    return web.Response(status=200)


async def users_contributees(request: web.Request, include_entities=None, skip_status=None) -> web.Response:
    """users_contributees

    Returns a collection of users that the specified user can contribute to.

    :param include_entities: The entities node will be disincluded when set to false. Example Values: false
    :type include_entities: str
    :param skip_status: When set to either true, t or 1 statuses will not be included in the returned user objects.
    :type skip_status: str

    """
    return web.Response(status=200)


async def users_contributors(request: web.Request, include_entities=None, skip_status=None) -> web.Response:
    """users_contributors

    Returns a collection of users who can contribute to the specified account.

    :param include_entities: The entities node will be disincluded when set to false. Example Values: false
    :type include_entities: str
    :param skip_status: When set to either true, t or 1 statuses will not be included in the returned user objects.
    :type skip_status: str

    """
    return web.Response(status=200)


async def users_lookup(request: web.Request, screen_name=None, user_id=None, include_entities=None) -> web.Response:
    """users_lookup

    Returns fully-hydrated user objects for up to 100 users per request, as specified by comma-separated values passed to the user_id and/or screen_name parameters.  This method is especially useful when used in conjunction with collections of user IDs returned from GET friends/ids and GET followers/ids.  GET users/show is used to retrieve a single user object.

    :param screen_name: A comma separated list of screen names, up to 100 are allowed in a single request. You are strongly encouraged to use a POST for larger (up to 100 screen names) requests.  Example Values: twitterapi,twitter
    :type screen_name: str
    :param user_id: A comma separated list of user IDs, up to 100 are allowed in a single request. You are strongly encouraged to use a POST for larger requests.  Example Values: 783214,6253282
    :type user_id: str
    :param include_entities: The entities node that may appear within embedded statuses will be disincluded when set to false.  Example Values: false
    :type include_entities: str

    """
    return web.Response(status=200)


async def users_report_spam(request: web.Request, ) -> web.Response:
    """users_report_spam

    The user specified in the id is blocked by the authenticated user and reported as a spammer.


    """
    return web.Response(status=200)


async def users_search(request: web.Request, q, page=None, count=None, include_entities=None) -> web.Response:
    """users_search

    Provides a simple, relevance-based search interface to public user accounts on Twitter. Try querying by topical interest, full name, company name, location, or other criteria. Exact match searches are not supported.  Only the first 1,000 matching results are available.

    :param q: The search query to run against people search.  Example Values: Twitter%20API
    :type q: str
    :param page: Specifies the page of results to retrieve.  Example Values: 3
    :type page: str
    :param count: The number of potential user results to retrieve per page. This value has a maximum of 20.  Example Values: 5
    :type count: str
    :param include_entities: The entities node will be disincluded when set to false.  Example Values: false
    :type include_entities: str

    """
    return web.Response(status=200)


async def users_show(request: web.Request, screen_name, user_id, include_entities=None) -> web.Response:
    """users_show

    Returns a variety of information about the user specified by the required user_id or screen_name parameter. The author&#39;s most recent Tweet will be returned inline when possible.  GET users/lookup is used to retrieve a bulk collection of user objects.

    :param screen_name: The screen name of the user for whom to return results for. Either a id or screen_name is required for this method.  Example Values: noradio
    :type screen_name: str
    :param user_id: The ID of the user for whom to return results for. Either an id or screen_name is required for this method.  Example Values: 12345
    :type user_id: str
    :param include_entities: The entities node will be disincluded when set to false.  Example Values: false
    :type include_entities: str

    """
    return web.Response(status=200)


async def users_suggestions(request: web.Request, lang=None) -> web.Response:
    """users_suggestions

    Access to Twitter&#39;s suggested user list. This returns the list of suggested user categories. The category can be used in GET users/suggestions/:slug to get the users in that category.

    :param lang: Restricts the suggested categories to the requested language. The language must be specified by the appropriate two letter ISO 639-1 representation. Currently supported languages are provided by the GET help/languages API request. Unsupported language codes will receive English (en) results. If you use lang in this request, ensure you also include it when requesting the GET users/suggestions/:slug list.
    :type lang: str

    """
    return web.Response(status=200)


async def users_suggestions_slug(request: web.Request, slug, lang=None) -> web.Response:
    """users_suggestions_slug

    Access the users in a given category of the Twitter suggested user list. It is recommended that applications cache this data for no more than one hour.

    :param slug: The short name of list or a category  Example Values: twitter
    :type slug: str
    :param lang: Restricts the suggested categories to the requested language. The language must be specified by the appropriate two letter ISO 639-1 representation. Currently supported languages are provided by the GET help/languages API request. Unsupported language codes will receive English (en) results. If you use lang in this request, ensure you also include it when requesting the GET users/suggestions/:slug list.
    :type lang: str

    """
    return web.Response(status=200)


async def users_suggestionsslugmembers(request: web.Request, slug) -> web.Response:
    """users_suggestionsslugmembers

    Access the users in a given category of the Twitter suggested user list and return their most recent status if they are not a protected user.

    :param slug: The short name of list or a category  Example Values: twitter
    :type slug: str

    """
    return web.Response(status=200)
