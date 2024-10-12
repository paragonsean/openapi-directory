from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_posts200_response import GetPosts200Response
from openapi_server.models.search_posts200_response import SearchPosts200Response
from openapi_server import util


async def get_user_posts(request: web.Request, user_id, types, sources, sort_by=None, group_ids=None, per_page=None, page=None, device_pixel_ratio=None, latitude=None, longitude=None, radius=None, date_min=None, date_max=None, outcomes=None, include_reposts=None) -> web.Response:
    """List posts by a user

    

    :param user_id: The user ID of the user whose posts will be retrieved. Using &#39;me&#39; as the user_id will return the posts for the current user. 
    :type user_id: str
    :param types: A comma separated list of the post types to return.  The available post types are: offer, taken, wanted, received, admin 
    :type types: str
    :param sources: A comma separated list of the post sources to retrieve posts from. The available sources are: groups, trashnothing, open_archive_groups. The trashnothing source is for public posts that are posted on trash nothing but are not associated with any group. The open_archive_groups source provides a way to easily request posts from groups that have open_archives set to true without having to pass a group_ids parameter.  When passed, it will automatically return posts from open archive groups that are within the area specified by the latitude, longitude and radius parameters (or all the open archive groups the requested user has posted to if latitude, longitude and radius aren&#39;t passed). &lt;br /&gt;&lt;br /&gt; NOTE: For requests using an api key instead of oauth, passing the trashnothing source or the open_archive_groups source makes the latitude, longitude and radius parameters required. 
    :type sources: str
    :param sort_by: How to sort the posts that are returned.  One of: date, active, distance &lt;br /&gt;&lt;br /&gt; Date sorting will sort posts from newest to oldest. Active sorting will sort active posts before satisfied, withdrawn and expired posts and then sort by date. Distance sorting will sort the closest posts first. 
    :type sort_by: str
    :param group_ids: A comma separated list of the group IDs to retrieve posts from. This parameter is only used if the &#39;groups&#39; source is passed in the sources parameter and only groups that the current user is a member of or that are open archives groups will be used (the group IDs of other groups will be silently discarded*). &lt;br /&gt;&lt;br /&gt; NOTE: For requests using an api key instead of oauth, this field is required if the &#39;groups&#39; source is passed. In addition, only posts from groups that have open_archives set to true will be used (the group IDS of other groups will be silently discarded*). &lt;br /&gt;&lt;br/&gt; *To determine which group IDs were used and which were discarded, use the group_ids field in the response. 
    :type group_ids: str
    :param per_page: The number of posts to return per page (must be &gt;&#x3D; 1 and &lt;&#x3D; 100).
    :type per_page: int
    :param page: The page of posts to return.
    :type page: int
    :param device_pixel_ratio: Client device pixel ratio used to determine thumbnail size (default 1.0).
    :type device_pixel_ratio: 
    :param latitude: The latitude of a point around which to return posts. 
    :type latitude: 
    :param longitude: The longitude of a point around which to return posts. 
    :type longitude: 
    :param radius: The radius in meters of a circle centered at the point defined by the latitude and longitude parameters. When latitude, longitude and radius are passed, only posts within the circle defined by these parameters will be returned. 
    :type radius: 
    :param date_min: Only posts newer than or equal to this UTC date and time will be returned. 
    :type date_min: str
    :param date_max: Only posts older than this UTC date and time will be returned.
    :type date_max: str
    :param outcomes: A comma separated list of the post outcomes to return.  The available post outcomes are: satisfied, withdrawn &lt;br /&gt;&lt;br /&gt; There are also a couple special values that can be passed.  If set to an empty string (the default), only posts that are not satisfied and not withdrawn and not expired are returned. If set to &#39;all&#39;, all posts will be returned no matter what outcome the posts have. If set to &#39;not-promised&#39;, only posts that are not satisfied ant not withdrawn and not expired and not promised are returned. 
    :type outcomes: str
    :param include_reposts: If set to 1 (the default), posts that are reposts will be included. If set to 0, reposts will be excluded. See the repost_count field of post objects for details about how reposts are identified. 
    :type include_reposts: int

    """
    date_min = util.deserialize_datetime(date_min)
    date_max = util.deserialize_datetime(date_max)
    return web.Response(status=200)


async def search_user_posts(request: web.Request, user_id, search, types, sources, sort_by=None, group_ids=None, per_page=None, page=None, device_pixel_ratio=None, latitude=None, longitude=None, radius=None, date_min=None, date_max=None, outcomes=None, include_reposts=None) -> web.Response:
    """Search posts by a user

    Searching posts takes the same arguments as listing posts except for the addition of the search and sort_by parameters. 

    :param user_id: The user ID of the user whose posts will be retrieved. Using &#39;me&#39; as the user_id will return the posts for the current user. 
    :type user_id: str
    :param search: The search query used to find posts.
    :type search: str
    :param types: A comma separated list of the post types to return.  The available post types are: offer, taken, wanted, received, admin 
    :type types: str
    :param sources: A comma separated list of the post sources to retrieve posts from. The available sources are: groups, trashnothing, open_archive_groups. The trashnothing source is for public posts that are posted on trash nothing but are not associated with any group. The open_archive_groups source provides a way to easily request posts from groups that have open_archives set to true without having to pass a group_ids parameter.  When passed, it will automatically return posts from open archive groups that are within the area specified by the latitude, longitude and radius parameters (or all the open archive groups the requested user has posted to if latitude, longitude and radius aren&#39;t passed). &lt;br /&gt;&lt;br /&gt; NOTE: For requests using an api key instead of oauth, passing the trashnothing source or the open_archive_groups source makes the latitude, longitude and radius parameters required. 
    :type sources: str
    :param sort_by: How to sort the posts that are returned.  One of: relevance, date, active, distance &lt;br /&gt;&lt;br /&gt; Relevance sorting will sort the posts that best match the search query first. Date sorting will sort posts from newest to oldest. Active sorting will sort active posts before satisfied, withdrawn and expired posts and then sort by date. Distance sorting will sort the closest posts first. 
    :type sort_by: str
    :param group_ids: A comma separated list of the group IDs to retrieve posts from. This parameter is only used if the &#39;groups&#39; source is passed in the sources parameter and only groups that the current user is a member of or that are open archives groups will be used (the group IDs of other groups will be silently discarded*). &lt;br /&gt;&lt;br /&gt; NOTE: For requests using an api key instead of oauth, this field is required if the &#39;groups&#39; source is passed. In addition, only posts from groups that have open_archives set to true will be used (the group IDS of other groups will be silently discarded*). &lt;br /&gt;&lt;br/&gt; *To determine which group IDs were used and which were discarded, use the group_ids field in the response. 
    :type group_ids: str
    :param per_page: The number of posts to return per page (must be &gt;&#x3D; 1 and &lt;&#x3D; 100).
    :type per_page: int
    :param page: The page of posts to return.
    :type page: int
    :param device_pixel_ratio: Client device pixel ratio used to determine thumbnail size (default 1.0).
    :type device_pixel_ratio: 
    :param latitude: The latitude of a point around which to return posts. 
    :type latitude: 
    :param longitude: The longitude of a point around which to return posts. 
    :type longitude: 
    :param radius: The radius in meters of a circle centered at the point defined by the latitude and longitude parameters. When latitude, longitude and radius are passed, only posts within the circle defined by these parameters will be returned. 
    :type radius: 
    :param date_min: Only posts newer than or equal to this UTC date and time will be returned. 
    :type date_min: str
    :param date_max: Only posts older than this UTC date and time will be returned.
    :type date_max: str
    :param outcomes: A comma separated list of the post outcomes to return.  The available post outcomes are: satisfied, withdrawn &lt;br /&gt;&lt;br /&gt; There are also a couple special values that can be passed.  If set to an empty string (the default), only posts that are not satisfied and not withdrawn and not expired are returned. If set to &#39;all&#39;, all posts will be returned no matter what outcome the posts have. If set to &#39;not-promised&#39;, only posts that are not satisfied ant not withdrawn and not expired and not promised are returned. 
    :type outcomes: str
    :param include_reposts: If set to 1 (the default), posts that are reposts will be included. If set to 0, reposts will be excluded. See the repost_count field of post objects for details about how reposts are identified. 
    :type include_reposts: int

    """
    date_min = util.deserialize_datetime(date_min)
    date_max = util.deserialize_datetime(date_max)
    return web.Response(status=200)
