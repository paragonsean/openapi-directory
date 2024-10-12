from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_hidden_items_request import AddHiddenItemsRequest
from openapi_server.models.add_items_to_personal_list_request import AddItemsToPersonalListRequest
from openapi_server.models.create_personal_list_request import CreatePersonalListRequest
from openapi_server.models.remove_items_from_personal_list_request import RemoveItemsFromPersonalListRequest
from openapi_server.models.reorder_a_user_s_lists_request import ReorderAUserSListsRequest
from openapi_server.models.reorder_personally_recommended_items_request import ReorderPersonallyRecommendedItemsRequest
from openapi_server.models.update_personal_list_request import UpdatePersonalListRequest
from openapi_server import util


async def add_hidden_items(request: web.Request, section, trakt_api_version=None, trakt_api_key=None, body=None) -> web.Response:
    """Add hidden items

    #### &amp;#128274; OAuth Required  Hide items for a specific section. Here&#39;s what type of items can hidden for each section.  #### Hideable Media Objects  | Section | Objects | |---|---|---| | &#x60;calendar&#x60; | &#x60;movie&#x60;, &#x60;show&#x60; | | &#x60;progress_watched&#x60; | &#x60;show&#x60;, &#x60;season&#x60; | | &#x60;progress_collected&#x60; | &#x60;show&#x60;, &#x60;season&#x60; | | &#x60;recommendations&#x60; | &#x60;movie&#x60;, &#x60;show&#x60; | | &#x60;comments&#x60; | &#x60;user&#x60; |  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;movies&#x60; | array | Array of &#x60;movie&#x60; objects. (see examples &amp;#8594;) | | &#x60;shows&#x60; | array | Array of &#x60;show&#x60; objects. | | &#x60;seasons&#x60; | array | Array of &#x60;season&#x60; objects. | | &#x60;users&#x60; | array | Array of &#x60;user&#x60; objects. |

    :param section: 
    :type section: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddHiddenItemsRequest.from_dict(body)
    return web.Response(status=200)


async def add_items_to_personal_list(request: web.Request, id, list_id, trakt_api_version=None, trakt_api_key=None, body=None) -> web.Response:
    """Add items to personal list

    #### &amp;#128274; OAuth Required &amp;#128513; Emojis 🔥 VIP Enhanced  Add one or more items to a personal list. Items can be movies, shows, seasons, episodes, or people.  #### Notes  Each list item can optionally accept a &#x60;notes&#x60; *(255 maximum characters)* field with custom text. The user must be a [**Trakt VIP**](https://trakt.tv/vip) to send &#x60;notes&#x60;.  #### Limits  If the user&#39;s list item limit is exceeded, a &#x60;420&#x60; HTTP error code is returned. Use the [**/users/settings**](/reference/users/settings) method to get all limits for a user account. In most cases, upgrading to [**Trakt VIP**](https://trakt.tv/vip) will increase the limits.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;movies&#x60; | array | Array of &#x60;movie&#x60; objects. (see examples &amp;#8594;) | | &#x60;shows&#x60; | array | Array of &#x60;show&#x60; objects. | | &#x60;seasons&#x60; | array | Array of &#x60;season&#x60; objects. | | &#x60;episodes&#x60; | array | Array of &#x60;episode&#x60; objects. | | &#x60;people&#x60; | array | Array of &#x60;person&#x60; objects. |

    :param id: User slug
    :type id: str
    :param list_id: Trakt ID or Trakt slug
    :type list_id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddItemsToPersonalListRequest.from_dict(body)
    return web.Response(status=200)


async def approve_follow_request(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Approve follow request

    #### &amp;#128274; OAuth Required  Approve a follower using the &#x60;id&#x60; of the request. If the &#x60;id&#x60; is not found, was already approved, or was already denied, a &#x60;404&#x60; error will be returned.

    :param id: ID of the follower request.
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def create_personal_list(request: web.Request, id, trakt_api_version=None, trakt_api_key=None, body=None) -> web.Response:
    """Create personal list

    #### &amp;#128274; OAuth Required 🔥 VIP Enhanced  Create a new personal list. The &#x60;name&#x60; is the only required field, but the other info is recommended to ask for.  #### Limits  If the user&#39;s list limit is exceeded, a &#x60;420&#x60; HTTP error code is returned. Use the [**/users/settings**](/reference/users/settings) method to get all limits for a user account. In most cases, upgrading to [**Trakt VIP**](https://trakt.tv/vip) will increase the limits.  #### Privacy  Lists will be &#x60;private&#x60; by default. Here is what each value means.  | Value | Privacy impact... | |---|---| | &#x60;private&#x60; | Only you can see the list. | | &#x60;link&#x60; | Anyone with the &#x60;share_link&#x60; can see the list. | | &#x60;friends&#x60; | Only your friends can see the list. | | &#x60;public&#x60; | Anyone can see the list. |  #### JSON POST Data  | Key | Type | Default | Value | |---|---|---|---| | &#x60;name&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string |  | Name of the list. | | &#x60;description&#x60; | string |  | Description for this list. | | &#x60;privacy&#x60; | string | &#x60;private&#x60; | &#x60;private&#x60;, &#x60;link&#x60;, &#x60;friends&#x60;, &#x60;public&#x60; | | &#x60;display_numbers&#x60; | boolean | &#x60;false&#x60; | Should each item be numbered? | | &#x60;allow_comments&#x60; | boolean | &#x60;true&#x60; | Are comments allowed? | | &#x60;sort_by&#x60; | string | &#x60;rank&#x60; | &#x60;rank&#x60;, &#x60;added&#x60;, &#x60;title&#x60;, &#x60;released&#x60;, &#x60;runtime&#x60;, &#x60;popularity&#x60;, &#x60;percentage&#x60;, &#x60;votes&#x60;, &#x60;my_rating&#x60;, &#x60;random&#x60;, &#x60;watched&#x60;, &#x60;collected&#x60; | | &#x60;sort_how&#x60; | string | &#x60;asc&#x60; | &#x60;asc&#x60;, &#x60;desc&#x60; |

    :param id: Automatically added
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreatePersonalListRequest.from_dict(body)
    return web.Response(status=200)


async def delete_a_users_personal_list(request: web.Request, id, list_id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Delete a user&#39;s personal list

    #### &amp;#128274; OAuth Required  Remove a personal list and all items it contains.

    :param id: Automatically added
    :type id: str
    :param list_id: Automatically added
    :type list_id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def deny_follow_request(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Deny follow request

    #### &amp;#128274; OAuth Required  Deny a follower using the &#x60;id&#x60; of the request. If the &#x60;id&#x60; is not found, was already approved, or was already denied, a &#x60;404&#x60; error will be returned.

    :param id: Automatically added
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def follow_this_user(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Follow this user

    #### &amp;#128274; OAuth Required  If the user has a private profile, the follow request will require approval (&#x60;approved_at&#x60; will be null). If a user is public, they will be followed immediately (&#x60;approved_at&#x60; will have a date).  **Note:** If this user is already being followed, a &#x60;409&#x60; HTTP status code will returned.

    :param id: User slug
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_a_users_personal_lists(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get a user&#39;s personal lists

    #### &amp;#128275; OAuth Optional &amp;#128513; Emojis  Returns all personal lists for a user. Use the [**/users/:id/lists/:list_id/items**](#reference/users/list-items) method to get the actual items a specific list contains.

    :param id: User slug
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_all_lists_a_user_can_collaborate_on(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get all lists a user can collaborate on

    #### &amp;#128275; OAuth Optional  Returns all lists a user can collaborate on. This gives full access to add, remove, and re-order list items. It essentially works just like a list owned by the user, just make sure to use the correct list owner &#x60;user&#x60; when building the API URLs.

    :param id: User slug
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_comments(request: web.Request, id, comment_type, type, include_replies=None, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get comments

    #### &amp;#128275; OAuth Optional &amp;#128196; Pagination &amp;#10024; Extended Info  Returns the most recently written comments for the user. You can optionally filter by the &#x60;comment_type&#x60; and media &#x60;type&#x60; to limit what gets returned.  By default, only top level comments are returned. Set &#x60;?include_replies&#x3D;true&#x60; to return replies in addition to top level comments. Set &#x60;?include_replies&#x3D;only&#x60; to return only replies and no top level comments.

    :param id: User slug
    :type id: str
    :param comment_type: 
    :type comment_type: str
    :param type: 
    :type type: str
    :param include_replies: include comment replies
    :type include_replies: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_follow_requests(request: web.Request, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get follow requests

    #### &amp;#128274; OAuth Required &amp;#10024; Extended Info  List a user&#39;s pending follow requests so they can either approve or deny them.

    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_followers(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get followers

    #### &amp;#128275; OAuth Optional &amp;#10024; Extended Info  Returns all followers including when the relationship began.

    :param id: User slug
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_following(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get following

    #### &amp;#128275; OAuth Optional &amp;#10024; Extended Info  Returns all user&#39;s they follow including when the relationship began.

    :param id: User slug
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_friends(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get friends

    #### &amp;#128275; OAuth Optional &amp;#10024; Extended Info  Returns all friends for a user including when the relationship began. Friendship is a 2 way relationship where each user follows the other.

    :param id: User slug
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_hidden_items(request: web.Request, section, type=None, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get hidden items

    #### &amp;#128274; OAuth Required &amp;#128196; Pagination &amp;#10024; Extended Info  Get hidden items for a section. This will return an array of standard media objects. You can optionally limit the &#x60;type&#x60; of results to return.

    :param section: 
    :type section: str
    :param type: Narrow down by element type.
    :type type: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_items_on_a_personal_list(request: web.Request, id, list_id, type, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get items on a personal list

    #### &amp;#128275; OAuth Optional &amp;#128196; Pagination Optional &amp;#10024; Extended Info &amp;#128513; Emojis  Get all items on a personal list. Items can be a &#x60;movie&#x60;, &#x60;show&#x60;, &#x60;season&#x60;, &#x60;episode&#x60;, or &#x60;person&#x60;. You can optionally specify the &#x60;type&#x60; parameter with a single value or comma delimited string for multiple item types.  #### Notes  Each list item contains a &#x60;notes&#x60; field with text entered by the user.  #### Sorting Headers  All list items are sorted by ascending &#x60;rank&#x60;. We also send &#x60;X-Sort-By&#x60; and &#x60;X-Sort-How&#x60; headers which can be used to custom sort the list _**in your app**_ based on the user&#39;s preference. Values for &#x60;X-Sort-By&#x60; include &#x60;rank&#x60;, &#x60;added&#x60;, &#x60;title&#x60;, &#x60;released&#x60;, &#x60;runtime&#x60;, &#x60;popularity&#x60;, &#x60;percentage&#x60;, &#x60;votes&#x60;, &#x60;my_rating&#x60;, &#x60;random&#x60;, &#x60;watched&#x60;, and &#x60;collected&#x60;. Values for &#x60;X-Sort-How&#x60; include &#x60;asc&#x60; and &#x60;desc&#x60;.

    :param id: User slug
    :type id: str
    :param list_id: Trakt ID or Trakt slug
    :type list_id: str
    :param type: Filter for a specific item type
    :type type: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_likes(request: web.Request, id, type, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get likes

    #### &amp;#128274; OAuth Optional &amp;#128196; Pagination  Get items a user likes. This will return an array of standard media objects. You can optionally limit the &#x60;type&#x60; of results to return.  #### Comment Media Objects  If you add &#x60;?extended&#x3D;comments&#x60; to the URL, it will return media objects for each comment like.  **Note:** This returns a lot of data, so please only use this extended parameter if you actually need it!

    :param id: User slug
    :type id: str
    :param type: 
    :type type: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_pending_following_requests(request: web.Request, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get pending following requests

    #### &amp;#128274; OAuth Required &amp;#10024; Extended Info  List a user&#39;s pending following requests that they&#39;re waiting for the other user&#39;s to approve.

    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_personal_list(request: web.Request, id, list_id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get personal list

    #### &amp;#128275; OAuth Optional &amp;#128513; Emojis  Returns a single personal list. Use the [**/users/:id/lists/:list_id/items**](#reference/users/list-items) method to get the actual items this list contains.

    :param id: User slug
    :type id: str
    :param list_id: Trakt ID or Trakt slug
    :type list_id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_saved_filters(request: web.Request, section, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get saved filters

    #### &amp;#128274; OAuth Required &amp;#128196; Pagination 🔥 VIP Only  Get all saved filters a user has created. The &#x60;path&#x60; and &#x60;query&#x60; can be used to construct an API path to retrieve the saved data. Think of this like a dynamically updated list.

    :param section: 
    :type section: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_stats(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get stats

    #### &amp;#128275; OAuth Optional  Returns stats about the movies, shows, and episodes a user has watched, collected, and rated.

    :param id: User slug
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_user_profile(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get user profile

    #### &amp;#128275; OAuth Optional &amp;#10024; Extended Info  Get a user&#39;s profile information. If the user is private, info will only be returned if you send OAuth and are either that user or an approved follower. Adding &#x60;?extended&#x3D;vip&#x60; will return some additional VIP related fields so you can display the user&#39;s Trakt VIP status and year count.

    :param id: User slug
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_watching(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get watching

    #### &amp;#128275; OAuth Optional &amp;#10024; Extended Info  Returns a movie or episode if the user is currently watching something.  If they are not, it returns no data and a &#x60;204&#x60; HTTP status code.

    :param id: User slug
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def like_a_list(request: web.Request, id, list_id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Like a list

    #### &amp;#128274; OAuth Required  Votes help determine popular lists. Only one like is allowed per list per user.

    :param id: User slug
    :type id: str
    :param list_id: Trakt ID or Trakt slug
    :type list_id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def remove_hidden_items(request: web.Request, section, trakt_api_version=None, trakt_api_key=None, body=None) -> web.Response:
    """Remove hidden items

    #### &amp;#128274; OAuth Required  Unhide items for a specific section. Here&#39;s what type of items can unhidden for each section.  #### Unhideable Media Objects  | Section | Objects | |---|---|---| | &#x60;calendar&#x60; | &#x60;movie&#x60;, &#x60;show&#x60; | | &#x60;progress_watched&#x60; | &#x60;show&#x60;, &#x60;season&#x60; | | &#x60;progress_collected&#x60; | &#x60;show&#x60;, &#x60;season&#x60; | | &#x60;recommendations&#x60; | &#x60;movie&#x60;, &#x60;show&#x60; | | &#x60;comments&#x60; | &#x60;user&#x60; |  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;movies&#x60; | array | Array of &#x60;movie&#x60; objects. (see examples &amp;#8594;) | | &#x60;shows&#x60; | array | Array of &#x60;show&#x60; objects. | | &#x60;seasons&#x60; | array | Array of &#x60;season&#x60; objects. | | &#x60;users&#x60; | array | Array of &#x60;user&#x60; objects. |

    :param section: 
    :type section: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddHiddenItemsRequest.from_dict(body)
    return web.Response(status=200)


async def remove_items_from_personal_list(request: web.Request, id, list_id, trakt_api_version=None, trakt_api_key=None, body=None) -> web.Response:
    """Remove items from personal list

    #### &amp;#128274; OAuth Required  Remove one or more items from a personal list.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;movies&#x60; | array | Array of &#x60;movie&#x60; objects. (see examples &amp;#8594;) | | &#x60;shows&#x60; | array | Array of &#x60;show&#x60; objects. | | &#x60;seasons&#x60; | array | Array of &#x60;season&#x60; objects. | | &#x60;episodes&#x60; | array | Array of &#x60;episode&#x60; objects. | | &#x60;people&#x60; | array | Array of &#x60;person&#x60; objects. |

    :param id: User slug
    :type id: str
    :param list_id: Trakt ID or Trakt slug
    :type list_id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = RemoveItemsFromPersonalListRequest.from_dict(body)
    return web.Response(status=200)


async def remove_like_on_a_list(request: web.Request, id, list_id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Remove like on a list

    #### &amp;#128274; OAuth Required  Remove a like on a list.

    :param id: Automatically added
    :type id: str
    :param list_id: Automatically added
    :type list_id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def reorder_a_users_lists(request: web.Request, id, trakt_api_version=None, trakt_api_key=None, body=None) -> web.Response:
    """Reorder a user&#39;s lists

    #### &amp;#128274; OAuth Required  Reorder all lists by sending the updated &#x60;rank&#x60; of list ids. Use the [**/users/:id/lists**](#reference/users/lists) method to get all list ids.

    :param id: User slug
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReorderAUserSListsRequest.from_dict(body)
    return web.Response(status=200)


async def reorder_items_on_a_list(request: web.Request, id, list_id, trakt_api_version=None, trakt_api_key=None, body=None) -> web.Response:
    """Reorder items on a list

    #### &amp;#128274; OAuth Required  Reorder all items on a list by sending the updated &#x60;rank&#x60; of list item ids. Use the [**/users/:id/lists/:list_id/items**](#reference/users/list-items) method to get all list item ids.

    :param id: User slug
    :type id: str
    :param list_id: Trakt ID or Trakt slug
    :type list_id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReorderPersonallyRecommendedItemsRequest.from_dict(body)
    return web.Response(status=200)


async def retrieve_settings(request: web.Request, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Retrieve settings

    #### &amp;#128274; OAuth Required  Get the user&#39;s settings so you can align your app&#39;s experience with what they&#39;re used to on the trakt website. A globally unique &#x60;uuid&#x60; is also returned, which can be used to identify the user locally in your app if needed. However, the &#x60;uuid&#x60; can&#39;t be used to retrieve data from the Trakt API.

    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def unfollow_this_user(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Unfollow this user

    #### &amp;#128274; OAuth Required  Unfollow someone you already follow.

    :param id: Automatically added
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def update_personal_list(request: web.Request, id, list_id, trakt_api_version=None, trakt_api_key=None, body=None) -> web.Response:
    """Update personal list

    #### &amp;#128274; OAuth Required  Update a personal list by sending 1 or more parameters. If you update the list name, the original slug will still be retained so existing references to this list won&#39;t break.  #### Privacy  Lists will be &#x60;private&#x60; by default. Here is what each value means.  | Value | Privacy impact... | |---|---| | &#x60;private&#x60; | Only you can see the list. | | &#x60;link&#x60; | Anyone with the &#x60;share_link&#x60; can see the list. | | &#x60;friends&#x60; | Only your friends can see the list. | | &#x60;public&#x60; | Anyone can see the list. |  #### JSON POST Data  | Key | Type | Value | |---|---|---|---| | &#x60;name&#x60; | string | Name of the list. | | &#x60;description&#x60; | string | Description for this list. | | &#x60;privacy&#x60; | string | &#x60;private&#x60;, &#x60;link&#x60;, &#x60;friends&#x60;, &#x60;public&#x60; | | &#x60;display_numbers&#x60; | boolean | Should each item be numbered? | | &#x60;allow_comments&#x60; | boolean | Are comments allowed? | | &#x60;sort_by&#x60; | string | &#x60;rank&#x60;, &#x60;added&#x60;, &#x60;title&#x60;, &#x60;released&#x60;, &#x60;runtime&#x60;, &#x60;popularity&#x60;, &#x60;percentage&#x60;, &#x60;votes&#x60;, &#x60;my_rating&#x60;, &#x60;random&#x60;, &#x60;watched&#x60;, &#x60;collected&#x60; | | &#x60;sort_how&#x60; | string | &#x60;asc&#x60;, &#x60;desc&#x60; |

    :param id: Automatically added
    :type id: str
    :param list_id: Automatically added
    :type list_id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdatePersonalListRequest.from_dict(body)
    return web.Response(status=200)


async def users_id_collection_type_get(request: web.Request, id, type, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get collection

    #### &amp;#128275; OAuth Optional &amp;#10024; Extended Info  Get all collected items in a user&#39;s collection. A collected item indicates availability to watch digitally or on physical media.  Each &#x60;movie&#x60; object contains &#x60;collected_at&#x60; and &#x60;updated_at&#x60; timestamps. Since users can set custom dates when they collected movies, it is possible for &#x60;collected_at&#x60; to be in the past. We also include &#x60;updated_at&#x60; to help sync Trakt data with your app. Cache this timestamp locally and only re-process the movie if you see a newer timestamp.  Each &#x60;show&#x60; object contains &#x60;last_collected_at&#x60; and &#x60;last_updated_at&#x60; timestamps. Since users can set custom dates when they collected episodes, it is possible for &#x60;last_collected_at&#x60; to be in the past. We also include &#x60;last_updated_at&#x60; to help sync Trakt data with your app. Cache this timestamp locally and only re-process the show if you see a newer timestamp.  If you add &#x60;?extended&#x3D;metadata&#x60; to the URL, it will return the additional &#x60;media_type&#x60;, &#x60;resolution&#x60;, &#x60;hdr&#x60;, &#x60;audio&#x60;, &#x60;audio_channels&#x60; and &#39;3d&#39; metadata. It will use &#x60;null&#x60; if the metadata isn&#39;t set for an item.

    :param id: User slug
    :type id: str
    :param type: 
    :type type: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def users_id_history_type_item_id_get(request: web.Request, id, type, item_id, start_at=None, end_at=None, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get watched history

    #### &amp;#128275; OAuth Optional &amp;#128196; Pagination &amp;#10024; Extended Info  Returns movies and episodes that a user has watched, sorted by most recent. You can optionally limit the &#x60;type&#x60; to &#x60;movies&#x60; or &#x60;episodes&#x60;. The &#x60;id&#x60; _(64-bit integer)_ in each history item uniquely identifies the event and can be used to remove individual events by using the [**/sync/history/remove**](#reference/sync/remove-from-history/get-watched-history) method. The &#x60;action&#x60; will be set to &#x60;scrobble&#x60;, &#x60;checkin&#x60;, or &#x60;watch&#x60;.  Specify a &#x60;type&#x60; and trakt &#x60;item_id&#x60; to limit the history for just that item. If the &#x60;item_id&#x60; is valid, but there is no history, an empty array will be returned.  | Example URL | Returns watches for... | |---|---| | &#x60;/history/movies/12601&#x60; | TRON: Legacy | | &#x60;/history/shows/1388&#x60; | All episodes of Breaking Bad | | &#x60;/history/seasons/3950&#x60; | All episodes of Breaking Bad: Season 1 | | &#x60;/history/episodes/73482&#x60; | Only episode 1 for Breaking Bad: Season 1 |

    :param id: User slug
    :type id: str
    :param type: 
    :type type: str
    :param item_id: Trakt ID for a specific item.
    :type item_id: int
    :param start_at: Starting date.
    :type start_at: str
    :param end_at: Ending date.
    :type end_at: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def users_id_lists_list_id_comments_sort_get(request: web.Request, id, list_id, sort, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get all list comments

    #### &amp;#128275; OAuth Optional &amp;#128196; Pagination &amp;#128513; Emojis  Returns all top level comments for a list. By default, the &#x60;newest&#x60; comments are returned first. Other sorting options include &#x60;oldest&#x60;, most &#x60;likes&#x60;, and most &#x60;replies&#x60;.

    :param id: User slug
    :type id: str
    :param list_id: Trakt ID or Trakt slug
    :type list_id: str
    :param sort: how to sort
    :type sort: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def users_id_lists_list_id_likes_get(request: web.Request, id, list_id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get all users who liked a list

    #### &amp;#128275; OAuth Optional &amp;#128196; Pagination  Returns all users who liked a list.

    :param id: User slug
    :type id: str
    :param list_id: Trakt ID or Trakt slug
    :type list_id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def users_id_ratings_type_rating_get(request: web.Request, id, type, rating, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get ratings

    #### &amp;#128275; OAuth Optional &amp;#128196; Pagination Optional &amp;#10024; Extended Info  Get a user&#39;s ratings filtered by &#x60;type&#x60;. You can optionally filter for a specific &#x60;rating&#x60; between 1 and 10. Send a comma separated string for &#x60;rating&#x60; if you need multiple ratings.

    :param id: User slug
    :type id: str
    :param type: 
    :type type: str
    :param rating: Filter for a specific rating.
    :type rating: int
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def users_id_recommendations_type_sort_get(request: web.Request, id, type, sort, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get personal recommendations

    #### &amp;#128274; OAuth Required &amp;#128196; Pagination Optional &amp;#10024; Extended Info &amp;#128513; Emojis  Returns the top 50 items a user personally recommendeds to others. These recommendations are used to enchance Trakt&#39;s social recommendation algorithm. Apps should encourage user&#39;s to build their personal recommendations so the algorithm keeps getting better.  #### Notes  Each recommendation contains a &#x60;notes&#x60; field explaining why the user recommended the item.

    :param id: User slug
    :type id: str
    :param type: Filter for a specific item type
    :type type: str
    :param sort: How to sort (only if type is also sent)
    :type sort: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def users_id_watched_type_get(request: web.Request, id, type, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get watched

    #### &amp;#128275; OAuth Optional &amp;#10024; Extended Info  Returns all movies or shows a user has watched sorted by most plays.  If &#x60;type&#x60; is set to _shows_ and you add &#x60;?extended&#x3D;noseasons&#x60; to the URL, it won&#39;t return season or episode info.  Each &#x60;movie&#x60; and &#x60;show&#x60; object contains &#x60;last_watched_at&#x60; and &#x60;last_updated_at&#x60; timestamps. Since users can set custom dates when they watched movies and episodes, it is possible for &#x60;last_watched_at&#x60; to be in the past. We also include &#x60;last_updated_at&#x60; to help sync Trakt data with your app. Cache this timestamp locally and only re-process the movies and shows if you see a newer timestamp.  Each &#x60;show&#x60; object contains a &#x60;reset_at&#x60; timestamp. If not &#x60;null&#x60;, this is when the user started re-watching the show. Your app can adjust the progress by ignoring episodes with a &#x60;last_watched_at&#x60; prior to the &#x60;reset_at&#x60;.

    :param id: User slug
    :type id: str
    :param type: 
    :type type: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def users_id_watchlist_type_sort_get(request: web.Request, id, type, sort, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get watchlist

    #### &amp;#128275; OAuth Optional &amp;#128196; Pagination Optional &amp;#10024; Extended Info &amp;#128513; Emojis  Returns all items in a user&#39;s watchlist filtered by type.  #### Notes  Each watchlist item contains a &#x60;notes&#x60; field with text entered by the user.  #### Sorting Headers  By default, all list items are sorted by &#x60;rank&#x60; &#x60;asc&#x60;. We send &#x60;X-Applied-Sort-By&#x60; and &#x60;X-Applied-Sort-How&#x60; headers to indicate how the results are actually being sorted.  We also send &#x60;X-Sort-By&#x60; and &#x60;X-Sort-How&#x60; headers which indicate the user&#39;s sort preference. Use these to to custom sort the watchlist _**in your app**_ for more advanced sort abilities we can&#39;t do in the API. Values for &#x60;X-Sort-By&#x60; include &#x60;rank&#x60;, &#x60;added&#x60;, &#x60;title&#x60;, &#x60;released&#x60;, &#x60;runtime&#x60;, &#x60;popularity&#x60;, &#x60;percentage&#x60;, and &#x60;votes&#x60;. Values for &#x60;X-Sort-How&#x60; include &#x60;asc&#x60; and &#x60;desc&#x60;.  #### Auto Removal  When an item is watched, it will be automatically removed from the watchlist. For shows and seasons, watching 1 episode will remove the entire show or season.  _**The watchlist should not be used as a list of what the user is actively watching.**_  Use a combination of the [**/sync/watched**](/reference/sync/get-watched) and [**/shows/:id/progress**](/reference/shows/watched-progress) methods to get what the user is actively watching.

    :param id: User slug
    :type id: str
    :param type: Filter for a specific item type
    :type type: str
    :param sort: How to sort (only if type is also sent)
    :type sort: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)
