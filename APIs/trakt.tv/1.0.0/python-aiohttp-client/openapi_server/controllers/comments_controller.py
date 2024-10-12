from typing import List, Dict
from aiohttp import web

from openapi_server.models.post_a_comment_request import PostACommentRequest
from openapi_server.models.post_a_reply_for_a_comment_request import PostAReplyForACommentRequest
from openapi_server.models.update_a_comment_or_reply_request import UpdateACommentOrReplyRequest
from openapi_server import util


async def delete_a_comment_or_reply(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Delete a comment or reply

    #### &amp;#128274; OAuth Required  Delete a single comment. The OAuth user must match the author of the comment in order to delete it. If not, a &#x60;401&#x60; HTTP status code is returned. The comment must also be less than 2 weeks old or have 0 replies. If not, a &#x60;409&#x60; HTTP status is returned.

    :param id: Automatically added
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_a_comment_or_reply(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get a comment or reply

    ####  &amp;#128513; Emojis  Returns a single comment and indicates how many replies it has. Use [**/comments/:id/replies**](/reference/comments/replies/) to get the actual replies.

    :param id: A specific comment ID.
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_all_users_who_liked_a_comment(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get all users who liked a comment

    #### &amp;#128196; Pagination  Returns all users who liked a comment. If you only need the &#x60;replies&#x60; count, the main &#x60;comment&#x60; object already has that, so no need to use this method.

    :param id: A specific comment ID.
    :type id: int
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_recently_created_comments(request: web.Request, comment_type, type, include_replies=None, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get recently created comments

    #### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#128513; Emojis  Returns the most recently written comments across all of Trakt. You can optionally filter by the &#x60;comment_type&#x60; and media &#x60;type&#x60; to limit what gets returned. If you want to &#x60;include_replies&#x60; that will return replies in place alongside top level comments.

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


async def get_recently_updated_comments(request: web.Request, comment_type, type, include_replies=None, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get recently updated comments

    #### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#128513; Emojis  Returns the most recently updated comments across all of Trakt. You can optionally filter by the &#x60;comment_type&#x60; and media &#x60;type&#x60; to limit what gets returned. If you want to &#x60;include_replies&#x60; that will return replies in place alongside top level comments.

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


async def get_replies_for_a_comment(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get replies for a comment

    #### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all replies for a comment. It is possible these replies could have replies themselves, so in that case you would just call [**/comments/:id/replies**](/reference/comments/replies/) again with the new comment &#x60;id&#x60;.

    :param id: A specific comment ID.
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_the_attached_media_item(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get the attached media item

    #### &amp;#10024; Extended Info  Returns the media item this comment is attached to. The media type can be &#x60;movie&#x60;, &#x60;show&#x60;, &#x60;season&#x60;, &#x60;episode&#x60;, or &#x60;list&#x60; and it also returns the standard media object for that media type.

    :param id: A specific comment ID.
    :type id: int
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_trending_comments(request: web.Request, comment_type, type, include_replies=None, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get trending comments

    #### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#128513; Emojis  Returns all comments with the most likes and replies over the last 7 days. You can optionally filter by the &#x60;comment_type&#x60; and media &#x60;type&#x60; to limit what gets returned. If you want to &#x60;include_replies&#x60; that will return replies in place alongside top level comments.

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


async def like_a_comment(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Like a comment

    #### &amp;#128274; OAuth Required  Votes help determine popular comments. Only one like is allowed per comment per user.

    :param id: A specific comment ID.
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def post_a_comment(request: web.Request, trakt_api_version=None, trakt_api_key=None, body=None) -> web.Response:
    """Post a comment

    #### &amp;#128274; OAuth Required &amp;#128513; Emojis  Add a new comment to a movie, show, season, episode, or list. Make sure to allow and encourage *spoilers* to be indicated in your app and follow the rules listed above.  #### JSON POST Data  | Key | Type | Default | Value | |---|---|---|---| | item &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | object | | &#x60;movie&#x60;, &#x60;show&#x60;, &#x60;season&#x60;, &#x60;episode&#x60;, or &#x60;list&#x60; object. (see examples &amp;#8594;) | | &#x60;comment&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string |  | Text for the comment. | | &#x60;spoiler&#x60; | boolean | &#x60;false&#x60; | Is this a spoiler? | | &#x60;sharing&#x60;  | object | | Control sharing to any connected social networks. (see below &amp;#8595;) |  #### Sharing  The &#x60;sharing&#x60; object is optional and will apply the user&#39;s settings if not sent. If &#x60;sharing&#x60; is sent, each key will override the user&#39;s setting for that social network. Send &#x60;true&#x60; to post or &#x60;false&#x60; to not post on the indicated social network. You can see which social networks a user has connected with the [**/users/settings**](/reference/users/settings) method.  | Key | Type | |---|---| | &#x60;twitter&#x60; | boolean | | &#x60;tumblr&#x60; | boolean | | &#x60;medium&#x60; | boolean |

    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostACommentRequest.from_dict(body)
    return web.Response(status=200)


async def post_a_reply_for_a_comment(request: web.Request, id, trakt_api_version=None, trakt_api_key=None, body=None) -> web.Response:
    """Post a reply for a comment

    #### &amp;#128274; OAuth Required &amp;#128513; Emojis  Add a new reply to an existing comment. Make sure to allow and encourage *spoilers* to be indicated in your app and follow the rules listed above.  #### JSON POST Data  | Key | Type | Default | Value | |---|---|---|---| | &#x60;comment&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string |  | Text for the reply. | | &#x60;spoiler&#x60; | boolean | &#x60;false&#x60; | Is this a spoiler? |

    :param id: Automatically added
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostAReplyForACommentRequest.from_dict(body)
    return web.Response(status=200)


async def remove_like_on_a_comment(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Remove like on a comment

    #### &amp;#128274; OAuth Required  Remove a like on a comment.

    :param id: Automatically added
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def update_a_comment_or_reply(request: web.Request, id, trakt_api_version=None, trakt_api_key=None, body=None) -> web.Response:
    """Update a comment or reply

    #### &amp;#128274; OAuth Required &amp;#128513; Emojis  Update a single comment. The OAuth user must match the author of the comment in order to update it. If not, a &#x60;401&#x60; HTTP status is returned.  #### JSON POST Data  | Key | Type | Default | Value | |---|---|---|---| | &#x60;comment&#x60; | string |  | Text for the comment. | | &#x60;spoiler&#x60; | boolean | &#x60;false&#x60; | Is this a spoiler? |

    :param id: Automatically added
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateACommentOrReplyRequest.from_dict(body)
    return web.Response(status=200)
