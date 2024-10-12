from typing import List, Dict
from aiohttp import web

from openapi_server.models.pause_watching_in_a_media_center_request import PauseWatchingInAMediaCenterRequest
from openapi_server.models.start_watching_in_a_media_center_request import StartWatchingInAMediaCenterRequest
from openapi_server.models.stop_or_finish_watching_in_a_media_center_request import StopOrFinishWatchingInAMediaCenterRequest
from openapi_server import util


async def pause_watching_in_a_media_center(request: web.Request, trakt_api_version=None, trakt_api_key=None, body=None) -> web.Response:
    """Pause watching in a media center

    #### &amp;#128274; OAuth Required  Use this method when the video is paused. The playback progress will be saved and [**/sync/playback**](/reference/sync/playback/) can be used to resume the video from this exact position. Unpause a video by calling the [**/scrobble/start**](/reference/scrobble/start/) method again.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | item &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | object | &#x60;movie&#x60; or &#x60;episode&#x60; object. (see examples &amp;#8594;) | | &#x60;progress&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | float | Progress percentage between 0 and 100. | | &#x60;app_version&#x60; | string | Version number of the app. | | &#x60;app_date&#x60; | string | Build date of the app. |

    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = PauseWatchingInAMediaCenterRequest.from_dict(body)
    return web.Response(status=200)


async def start_watching_in_a_media_center(request: web.Request, trakt_api_version=None, trakt_api_key=None, body=None) -> web.Response:
    """Start watching in a media center

    #### &amp;#128274; OAuth Required  Use this method when the video initially starts playing or is unpaused. This will remove any playback progress if it exists.  **Note:** A watching status will auto expire after the remaining runtime has elapsed. There is no need to call this method again while continuing to watch the same item.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | item &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | object | &#x60;movie&#x60; or &#x60;episode&#x60; object. (see examples &amp;#8594;) | | &#x60;progress&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | float | Progress percentage between 0 and 100. | | &#x60;app_version&#x60; | string | Version number of the app. | | &#x60;app_date&#x60; | string | Build date of the app. |

    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = StartWatchingInAMediaCenterRequest.from_dict(body)
    return web.Response(status=200)


async def stop_or_finish_watching_in_a_media_center(request: web.Request, trakt_api_version=None, trakt_api_key=None, body=None) -> web.Response:
    """Stop or finish watching in a media center

    #### &amp;#128274; OAuth Required  Use this method when the video is stopped or finishes playing on its own. If the progress is above 80%, the video will be scrobbled and the &#x60;action&#x60; will be set to **scrobble**. A unique history &#x60;id&#x60; (64-bit integer) will be returned and can be used to reference this &#x60;scrobble&#x60; directly.  If the progress is less than 80%, it will be treated as a *pause* and the &#x60;action&#x60; will be set to **pause**. The playback progress will be saved and [**/sync/playback**](/reference/sync/playback/) can be used to resume the video from this exact position.  **Note:** If you prefer to use a threshold higher than 80%, you should use [**/scrobble/pause**](/reference/scrobble/pause/) yourself so it doesn&#39;t create duplicate scrobbles.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | item &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | object | &#x60;movie&#x60; or &#x60;episode&#x60; object. (see examples &amp;#8594;) | | &#x60;progress&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | flloat | Progress percentage between 0 and 100. | | &#x60;app_version&#x60; | string | Version number of the app. | | &#x60;app_date&#x60; | string | Build date of the app. |  **Note:** If the same item was just scrobbled, a &#x60;409&#x60; HTTP status code will returned to avoid scrobbling a duplicate. The response will contain a &#x60;watched_at&#x60; timestamp when the item was last scrobbled and a &#x60;expires_at&#x60; timestamp when the item can be scrobbled again.

    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = StopOrFinishWatchingInAMediaCenterRequest.from_dict(body)
    return web.Response(status=200)
