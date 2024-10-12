from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def halo5_player_appearance(request: web.Request, player) -> web.Response:
    """Halo 5 - Player Appearance

    &lt;p&gt;This Endpoint retrieves appearance information for a player.&lt;/p&gt; &lt;p&gt;If the player is a member of a Company, the Company&#39;s ID and Name will be provided. Additional Company information is available via the Stats API.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;July 14, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added Endpoint.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

    :param player: The Player&#39;s Gamertag
    :type player: str

    """
    return web.Response(status=200)


async def halo5_player_emblem_image(request: web.Request, player, size=None) -> web.Response:
    """Halo 5 - Player Emblem Image

    &lt;p&gt;This Endpoint returns an HTTP Redirect (302 Found) response to the caller with the URL of an image of the Player&#39;s Emblem. The initial request to this API that returns the HTTP Redirect is throttled and requires a Subscription Key. However, the image itself (at hostname \&quot;image.halocdn.com\&quot;) is not throttled and does not require a Subscription Key. Note that if the Player later changes their Emblem, the image itself is not refreshed and will need to be refreshed via a new request to this API.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;August 12, 2019:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Expanded documentation for the HTTP 400 response code to cover unsupported emblem component(s).&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;July 14, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Renamed Endpoint from \&quot;Halo 5 - Emblem Image\&quot; to \&quot;Halo 5 - Player Emblem Image\&quot;.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 21, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Renamed Endpoint from \&quot;Emblem Image\&quot; to \&quot;Halo 5 - Emblem Image\&quot;.&lt;/li&gt;         &lt;li&gt;Removed \&quot;{title}\&quot; Request Parameter.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

    :param player: The Player&#39;s Gamertag.
    :type player: str
    :param size: An optional size (specified in pixels) of the image requested. When specified, this value must be one of the following values: 95, 128, 190, 256, 512. If a value is specified that is not in this list, the API returns HTTP 400 (\&quot;Bad Request\&quot;). If the size is empty or missing, the API will use 256.
    :type size: 

    """
    return web.Response(status=200)


async def halo5_player_spartan_image(request: web.Request, player, size=None, crop=None) -> web.Response:
    """Halo 5 - Player Spartan Image

    &lt;p&gt;This Endpoint returns an HTTP Redirect (302 Found) response to the caller with the URL of an image of the Player&#39;s Spartan&#39;s appearance. The initial request to this API that returns the HTTP Redirect is throttled and requires a Subscription Key. However, the image itself (at hostname \&quot;image.halocdn.com\&quot;) is not throttled and does not require a Subscription Key. Note that if the Player later changes their Spartan&#39;s appearance, the image itself is not refreshed and will need to be refreshed via a new request to this API.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;August 12, 2019:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Expanded documentation for the HTTP 400 response code to cover unsupported armor component(s).&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;July 14, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Renamed Endpoint from \&quot;Halo 5 - Spartan Image\&quot; to \&quot;Halo 5 - Player Spartan Image\&quot;.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 21, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Renamed Endpoint from \&quot;Spartan Image\&quot; to \&quot;Halo 5 - Spartan Image\&quot;.&lt;/li&gt;         &lt;li&gt;Removed \&quot;{title}\&quot; Request Parameter.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

    :param player: The Player&#39;s Gamertag.
    :type player: str
    :param size: An optional size (specified in pixels) of the image requested. When specified, this value must be one of the following values: 95, 128, 190, 256, 512. If a value is specified that is not in this list, the API returns HTTP 400 (\&quot;Bad Request\&quot;). If the size is empty or missing, the API will use 256.
    :type size: 
    :param crop: An optional crop that will be used to determine what portion of the Spartan is returned in the image. The value must be either \&quot;full\&quot; or \&quot;portrait\&quot;. If no value is specified \&quot;full\&quot; is used. If an unsupported value is provided, the API returns HTTP 400 (\&quot;Bad Request\&quot;).
    :type crop: str

    """
    return web.Response(status=200)
