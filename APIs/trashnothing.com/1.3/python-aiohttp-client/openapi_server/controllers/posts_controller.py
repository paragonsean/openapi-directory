from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_all_posts200_response import GetAllPosts200Response
from openapi_server.models.get_all_posts_changes200_response import GetAllPostsChanges200Response
from openapi_server.models.get_post_and_related_data200_response import GetPostAndRelatedData200Response
from openapi_server.models.get_posts200_response import GetPosts200Response
from openapi_server.models.get_posts_by_ids200_response import GetPostsByIds200Response
from openapi_server.models.post import Post
from openapi_server.models.search_posts200_response import SearchPosts200Response
from openapi_server import util


async def get_all_posts(request: web.Request, types, date_min, date_max, per_page=None, page=None, device_pixel_ratio=None) -> web.Response:
    """List all posts

    This endpoint provides an easy way to get a feed of all the publicly published posts on trash nothing. It provides access to all publicly published offer and wanted posts from the last 30 days. The posts are sorted by date (newest first). &lt;br /&gt;&lt;br /&gt; There are fewer options for filtering, sorting and searching posts with this endpoint but there is no 1,000 post limit and posts that are crossposted to multiple groups are not merged together in the response.  In most cases, crossposted posts are easy to detect because they have the same user_id, title and content. 

    :param types: A comma separated list of the post types to return.  The available post types are: offer, wanted 
    :type types: str
    :param date_min: Only posts newer than or equal to this UTC date and time will be returned. The UTC date and time used must be within a day or less of date_max. And the date and time must be within the last 30 days. And the date and time must be rounded to the nearest second. 
    :type date_min: str
    :param date_max: Only posts older than this UTC date and time will be returned. The UTC date and time used must be within a day or less of date_min. And the date and time must be rounded to the nearest second. 
    :type date_max: str
    :param per_page: The number of posts to return per page (must be &gt;&#x3D; 1 and &lt;&#x3D; 50).
    :type per_page: int
    :param page: The page of posts to return.
    :type page: int
    :param device_pixel_ratio: Client device pixel ratio used to determine thumbnail size (default 1.0).
    :type device_pixel_ratio: 

    """
    date_min = util.deserialize_datetime(date_min)
    date_max = util.deserialize_datetime(date_max)
    return web.Response(status=200)


async def get_all_posts_changes(request: web.Request, date_min, date_max, per_page=None, page=None) -> web.Response:
    """List all post changes

    This endpoint provides an easy way to get a feed of all the changes that have been made to publicly published posts on trash nothing.  Similar to the /posts/all endpoint, only data from the last 30 days is available and the changes are sorted by date (newest first).  Every change includes the date of the change, the post_id of the post that was changed and the type of change. &lt;br /&gt;&lt;br /&gt; The different types of changes that are returned are listed below. &lt;br /&gt;&lt;br /&gt; - deleted&lt;br /&gt; - undeleted&lt;br /&gt; - satisfied&lt;br /&gt; - promised&lt;br /&gt; - unpromised&lt;br /&gt; - withdrawn&lt;br /&gt; - edited&lt;br /&gt; &lt;br /&gt; For edited changes, clients can use the retrieve post API endpoint to get the edits that have been made to the post. 

    :param date_min: Only changes newer than or equal to this UTC date and time will be returned. The UTC date and time used must be within a day or less of date_max. And the date and time must be within the last 30 days. And the date and time must be rounded to the nearest second. 
    :type date_min: str
    :param date_max: Only changes older than this UTC date and time will be returned. The UTC date and time used must be within a day or less of date_min. And the date and time must be rounded to the nearest second. 
    :type date_max: str
    :param per_page: The number of changes to return per page (must be &gt;&#x3D; 1 and &lt;&#x3D; 50).
    :type per_page: int
    :param page: The page of changes to return.
    :type page: int

    """
    date_min = util.deserialize_datetime(date_min)
    date_max = util.deserialize_datetime(date_max)
    return web.Response(status=200)


async def get_post(request: web.Request, post_id) -> web.Response:
    """Retrieve a post

    

    :param post_id: The ID of the post to retrieve.
    :type post_id: str

    """
    return web.Response(status=200)


async def get_post_and_related_data(request: web.Request, post_id) -> web.Response:
    """Retrieve post display data

    Retrieve a post and other data related to the post that is useful for displaying the post such as data about the user who posted the post and the groups the post was posted on. 

    :param post_id: The ID of the post to retrieve.
    :type post_id: str

    """
    return web.Response(status=200)


async def get_posts(request: web.Request, types, sources, sort_by=None, group_ids=None, per_page=None, page=None, device_pixel_ratio=None, latitude=None, longitude=None, radius=None, date_min=None, date_max=None, outcomes=None, user_state=None, include_reposts=None) -> web.Response:
    """List posts

    NOTE: When paging through the posts returned by this endpoint, there will be at most 1,000 posts that can be returned (eg. 50 pages worth of posts with the default per_page value of 20).  In areas where there are more than 1,000 posts, clients can use more specific query parameters to adjust which posts are returned. NOTE: Passing the latitude, longitude and radius parameters filters all posts by their location and so these parameters will temporarily override the current users&#39; location preferences. When latitude, longitude and radius are not specified, public posts will be filtered by the current users&#39; location preferences. 

    :param types: A comma separated list of the post types to return.  The available post types are: offer, taken, wanted, received, admin 
    :type types: str
    :param sources: A comma separated list of the post sources to retrieve posts from. The available sources are: groups, trashnothing, open_archive_groups. The trashnothing source is for public posts that are posted on trash nothing but are not associated with any group. The open_archive_groups source provides a way to easily request posts from groups that have open_archives set to true without having to pass a group_ids parameter.  When passed, it will automatically return posts from open archive groups that are within the area specified by the latitude, longitude and radius parameters (or the current users&#39; location if latitude, longitude and radius aren&#39;t passed). &lt;br /&gt;&lt;br /&gt; NOTE: For requests using an api key instead of oauth, passing the trashnothing source or the open_archive_groups source makes the latitude, longitude and radius parameters required. 
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
    :param date_min: Only posts newer than or equal to this UTC date and time will be returned.  If unset, defaults to the current date and time minus 90 days. 
    :type date_min: str
    :param date_max: Only posts older than this UTC date and time will be returned.  If unset, defaults to the current date and time.
    :type date_max: str
    :param outcomes: A comma separated list of the post outcomes to return.  The available post outcomes are: satisfied, withdrawn &lt;br /&gt;&lt;br /&gt; There are also a couple special values that can be passed.  If set to an empty string (the default), only posts that are not satisfied and not withdrawn and not expired are returned. If set to &#39;all&#39;, all posts will be returned no matter what outcome the posts have. If set to &#39;not-promised&#39;, only posts that are not satisfied ant not withdrawn and not expired and not promised are returned. 
    :type outcomes: str
    :param user_state: If user_state is set, only posts matching the state specified will be returned.  Only one state may be passed and it must be one of the following: viewed, replied, bookmarked &lt;br&gt;&lt;br&gt; NOTE: This option will only work with oauth requests. 
    :type user_state: str
    :param include_reposts: If set to 1 (the default), posts that are reposts will be included. If set to 0, reposts will be excluded. See the repost_count field of post objects for details about how reposts are identified. 
    :type include_reposts: int

    """
    date_min = util.deserialize_datetime(date_min)
    date_max = util.deserialize_datetime(date_max)
    return web.Response(status=200)


async def get_posts_by_ids(request: web.Request, post_ids) -> web.Response:
    """Retrieve multiple posts

    

    :param post_ids: A comma separated list of the post IDs. If more than 10 post IDs are passed, only the first 10 posts will be returned. 
    :type post_ids: str

    """
    return web.Response(status=200)


async def search_posts(request: web.Request, search, types, sources, sort_by=None, group_ids=None, per_page=None, page=None, device_pixel_ratio=None, latitude=None, longitude=None, radius=None, date_min=None, date_max=None, outcomes=None, user_state=None, include_reposts=None) -> web.Response:
    """Search posts

    Searching posts takes the same arguments as listing posts except for the addition of the search and sort_by parameters. NOTE: When paging through the posts returned by this endpoint, there will be at most 1,000 posts that can be returned (eg. 50 pages worth of posts with the default per_page value of 20).  In areas where there are more than 1,000 posts, clients can use more specific query parameters to adjust which posts are returned. 

    :param search: The search query used to find posts.
    :type search: str
    :param types: A comma separated list of the post types to return.  The available post types are: offer, taken, wanted, received, admin 
    :type types: str
    :param sources: A comma separated list of the post sources to retrieve posts from. The available sources are: groups, trashnothing, open_archive_groups. The trashnothing source is for public posts that are posted on trash nothing but are not associated with any group. The open_archive_groups source provides a way to easily request posts from groups that have open_archives set to true without having to pass a group_ids parameter.  When passed, it will automatically return posts from open archive groups that are within the area specified by the latitude, longitude and radius parameters (or the current users&#39; location if latitude, longitude and radius aren&#39;t passed). &lt;br /&gt;&lt;br /&gt; NOTE: For requests using an api key instead of oauth, passing the trashnothing source or the open_archive_groups source makes the latitude, longitude and radius parameters required. 
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
    :param date_min: Only posts newer than or equal to this UTC date and time will be returned.  If unset, defaults to the current date and time minus 90 days. 
    :type date_min: str
    :param date_max: Only posts older than this UTC date and time will be returned.  If unset, defaults to the current date and time.
    :type date_max: str
    :param outcomes: A comma separated list of the post outcomes to return.  The available post outcomes are: satisfied, withdrawn &lt;br /&gt;&lt;br /&gt; There are also a couple special values that can be passed.  If set to an empty string (the default), only posts that are not satisfied and not withdrawn and not expired are returned. If set to &#39;all&#39;, all posts will be returned no matter what outcome the posts have. If set to &#39;not-promised&#39;, only posts that are not satisfied ant not withdrawn and not expired and not promised are returned. 
    :type outcomes: str
    :param user_state: If user_state is set, only posts matching the state specified will be returned.  Only one state may be passed and it must be one of the following: viewed, replied, bookmarked &lt;br&gt;&lt;br&gt; NOTE: This option will only work with oauth requests. 
    :type user_state: str
    :param include_reposts: If set to 1 (the default), posts that are reposts will be included. If set to 0, reposts will be excluded. See the repost_count field of post objects for details about how reposts are identified. 
    :type include_reposts: int

    """
    date_min = util.deserialize_datetime(date_min)
    date_max = util.deserialize_datetime(date_max)
    return web.Response(status=200)
