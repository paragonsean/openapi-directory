from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.trending_images import TrendingImages
from openapi_server import util


async def images_trending(request: web.Request, x_bing_apis_sdk, accept=None, accept_language=None, user_agent=None, x_ms_edge_client_id=None, x_ms_edge_client_ip=None, x_search_location=None, cc=None, mkt=None, safe_search=None, set_lang=None) -> web.Response:
    """The Image Trending Search API lets you search on Bing and get back a list of images that are trending based on search requests made by others. The images are broken out into different categories. For example, Popular People Searches. For a list of markets that support trending images, see [Trending Images](https://docs.microsoft.com/en-us/azure/cognitive-services/bing-image-search/trending-images).

    

    :param x_bing_apis_sdk: Activate swagger compliance
    :type x_bing_apis_sdk: str
    :param accept: The default media type is application/json. To specify that the response use [JSON-LD](http://json-ld.org/), set the Accept header to application/ld+json.
    :type accept: str
    :param accept_language: A comma-delimited list of one or more languages to use for user interface strings. The list is in decreasing order of preference. For additional information, including expected format, see [RFC2616](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html). This header and the [setLang](https://docs.microsoft.com/en-us/rest/api/cognitiveservices/bing-images-api-v7-reference#setlang) query parameter are mutually exclusive; do not specify both. If you set this header, you must also specify the [cc](https://docs.microsoft.com/en-us/rest/api/cognitiveservices/bing-images-api-v7-reference#cc) query parameter. To determine the market to return results for, Bing uses the first supported language it finds from the list and combines it with the cc parameter value. If the list does not include a supported language, Bing finds the closest language and market that supports the request or it uses an aggregated or default market for the results. To determine the market that Bing used, see the BingAPIs-Market header. Use this header and the cc query parameter only if you specify multiple languages. Otherwise, use the [mkt](https://docs.microsoft.com/en-us/rest/api/cognitiveservices/bing-images-api-v7-reference#mkt) and [setLang](https://docs.microsoft.com/en-us/rest/api/cognitiveservices/bing-images-api-v7-reference#setlang) query parameters. A user interface string is a string that&#39;s used as a label in a user interface. There are few user interface strings in the JSON response objects. Any links to Bing.com properties in the response objects apply the specified language.
    :type accept_language: str
    :param user_agent: The user agent originating the request. Bing uses the user agent to provide mobile users with an optimized experience. Although optional, you are encouraged to always specify this header. The user-agent should be the same string that any commonly used browser sends. For information about user agents, see [RFC 2616](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html). The following are examples of user-agent strings. Windows Phone: Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 822). Android: Mozilla / 5.0 (Linux; U; Android 2.3.5; en - us; SCH - I500 Build / GINGERBREAD) AppleWebKit / 533.1 (KHTML; like Gecko) Version / 4.0 Mobile Safari / 533.1. iPhone: Mozilla / 5.0 (iPhone; CPU iPhone OS 6_1 like Mac OS X) AppleWebKit / 536.26 (KHTML; like Gecko) Mobile / 10B142 iPhone4; 1 BingWeb / 3.03.1428.20120423. PC: Mozilla / 5.0 (Windows NT 6.3; WOW64; Trident / 7.0; Touch; rv:11.0) like Gecko. iPad: Mozilla / 5.0 (iPad; CPU OS 7_0 like Mac OS X) AppleWebKit / 537.51.1 (KHTML, like Gecko) Version / 7.0 Mobile / 11A465 Safari / 9537.53
    :type user_agent: str
    :param x_ms_edge_client_id: Bing uses this header to provide users with consistent behavior across Bing API calls. Bing often flights new features and improvements, and it uses the client ID as a key for assigning traffic on different flights. If you do not use the same client ID for a user across multiple requests, then Bing may assign the user to multiple conflicting flights. Being assigned to multiple conflicting flights can lead to an inconsistent user experience. For example, if the second request has a different flight assignment than the first, the experience may be unexpected. Also, Bing can use the client ID to tailor web results to that client ID’s search history, providing a richer experience for the user. Bing also uses this header to help improve result rankings by analyzing the activity generated by a client ID. The relevance improvements help with better quality of results delivered by Bing APIs and in turn enables higher click-through rates for the API consumer. IMPORTANT: Although optional, you should consider this header required. Persisting the client ID across multiple requests for the same end user and device combination enables 1) the API consumer to receive a consistent user experience, and 2) higher click-through rates via better quality of results from the Bing APIs. Each user that uses your application on the device must have a unique, Bing generated client ID. If you do not include this header in the request, Bing generates an ID and returns it in the X-MSEdge-ClientID response header. The only time that you should NOT include this header in a request is the first time the user uses your app on that device. Use the client ID for each Bing API request that your app makes for this user on the device. Persist the client ID. To persist the ID in a browser app, use a persistent HTTP cookie to ensure the ID is used across all sessions. Do not use a session cookie. For other apps such as mobile apps, use the device&#39;s persistent storage to persist the ID. The next time the user uses your app on that device, get the client ID that you persisted. Bing responses may or may not include this header. If the response includes this header, capture the client ID and use it for all subsequent Bing requests for the user on that device. If you include the X-MSEdge-ClientID, you must not include cookies in the request.
    :type x_ms_edge_client_id: str
    :param x_ms_edge_client_ip: The IPv4 or IPv6 address of the client device. The IP address is used to discover the user&#39;s location. Bing uses the location information to determine safe search behavior. Although optional, you are encouraged to always specify this header and the X-Search-Location header. Do not obfuscate the address (for example, by changing the last octet to 0). Obfuscating the address results in the location not being anywhere near the device&#39;s actual location, which may result in Bing serving erroneous results.
    :type x_ms_edge_client_ip: str
    :param x_search_location: A semicolon-delimited list of key/value pairs that describe the client&#39;s geographical location. Bing uses the location information to determine safe search behavior and to return relevant local content. Specify the key/value pair as &lt;key&gt;:&lt;value&gt;. The following are the keys that you use to specify the user&#39;s location. lat (required): The latitude of the client&#39;s location, in degrees. The latitude must be greater than or equal to -90.0 and less than or equal to +90.0. Negative values indicate southern latitudes and positive values indicate northern latitudes. long (required): The longitude of the client&#39;s location, in degrees. The longitude must be greater than or equal to -180.0 and less than or equal to +180.0. Negative values indicate western longitudes and positive values indicate eastern longitudes. re (required): The radius, in meters, which specifies the horizontal accuracy of the coordinates. Pass the value returned by the device&#39;s location service. Typical values might be 22m for GPS/Wi-Fi, 380m for cell tower triangulation, and 18,000m for reverse IP lookup. ts (optional): The UTC UNIX timestamp of when the client was at the location. (The UNIX timestamp is the number of seconds since January 1, 1970.) head (optional): The client&#39;s relative heading or direction of travel. Specify the direction of travel as degrees from 0 through 360, counting clockwise relative to true north. Specify this key only if the sp key is nonzero. sp (optional): The horizontal velocity (speed), in meters per second, that the client device is traveling. alt (optional): The altitude of the client device, in meters. are (optional): The radius, in meters, that specifies the vertical accuracy of the coordinates. Specify this key only if you specify the alt key. Although many of the keys are optional, the more information that you provide, the more accurate the location results are. Although optional, you are encouraged to always specify the user&#39;s geographical location. Providing the location is especially important if the client&#39;s IP address does not accurately reflect the user&#39;s physical location (for example, if the client uses VPN). For optimal results, you should include this header and the X-MSEdge-ClientIP header, but at a minimum, you should include this header.
    :type x_search_location: str
    :param cc: A 2-character country code of the country where the results come from. This API supports only the United States, Canada, Australia, and China markets. If you specify this query parameter, it must be set to us, ca, au, or cn. If you set this parameter, you must also specify the Accept-Language header. Bing uses the first supported language it finds from the languages list, and combine that language with the country code that you specify to determine the market to return results for. If the languages list does not include a supported language, Bing finds the closest language and market that supports the request, or it may use an aggregated or default market for the results instead of a specified one. You should use this query parameter and the Accept-Language query parameter only if you specify multiple languages; otherwise, you should use the mkt and setLang query parameters. This parameter and the mkt query parameter are mutually exclusive—do not specify both.
    :type cc: str
    :param mkt: The market where the results come from. Typically, mkt is the country where the user is making the request from. However, it could be a different country if the user is not located in a country where Bing delivers results. The market must be in the form &lt;language code&gt;-&lt;country code&gt;. For example, en-US. The string is case insensitive. For a list of possible market values, see [Market Codes](https://docs.microsoft.com/en-us/rest/api/cognitiveservices/bing-images-api-v7-reference#market-codes). NOTE: If known, you are encouraged to always specify the market. Specifying the market helps Bing route the request and return an appropriate and optimal response. If you specify a market that is not listed in [Market Codes](https://docs.microsoft.com/en-us/rest/api/cognitiveservices/bing-images-api-v7-reference#market-codes), Bing uses a best fit market code based on an internal mapping that is subject to change. This parameter and the [cc](https://docs.microsoft.com/en-us/rest/api/cognitiveservices/bing-images-api-v7-reference#cc) query parameter are mutually exclusive—do not specify both.
    :type mkt: str
    :param safe_search: Filter images for adult content. The following are the possible filter values. Off: May return images with adult content. If the request is through the Image Search API, the response includes thumbnail images that are clear (non-fuzzy). However, if the request is through the Web Search API, the response includes thumbnail images that are pixelated (fuzzy). Moderate: If the request is through the Image Search API, the response doesn&#39;t include images with adult content. If the request is through the Web Search API, the response may include images with adult content (the thumbnail images are pixelated (fuzzy)). Strict: Do not return images with adult content. The default is Moderate. If the request comes from a market that Bing&#39;s adult policy requires that safeSearch is set to Strict, Bing ignores the safeSearch value and uses Strict. If you use the site: query operator, there is the chance that the response may contain adult content regardless of what the safeSearch query parameter is set to. Use site: only if you are aware of the content on the site and your scenario supports the possibility of adult content.
    :type safe_search: str
    :param set_lang: The language to use for user interface strings. Specify the language using the ISO 639-1 2-letter language code. For example, the language code for English is EN. The default is EN (English). Although optional, you should always specify the language. Typically, you set setLang to the same language specified by mkt unless the user wants the user interface strings displayed in a different language. This parameter and the [Accept-Language](https://docs.microsoft.com/en-us/rest/api/cognitiveservices/bing-images-api-v7-reference#acceptlanguage) header are mutually exclusive; do not specify both. A user interface string is a string that&#39;s used as a label in a user interface. There are few user interface strings in the JSON response objects. Also, any links to Bing.com properties in the response objects apply the specified language.
    :type set_lang: str

    """
    return web.Response(status=200)
