from typing import List, Dict
from aiohttp import web

from openapi_server.models.download_file_type import DownloadFileType
from openapi_server.models.get_downloads_response import GetDownloadsResponse
from openapi_server.models.premium_access_download_data import PremiumAccessDownloadData
from openapi_server.models.product_type_for_downloads import ProductTypeForDownloads
from openapi_server import util


async def v3_downloads_get(request: web.Request, accept_language=None, date_from=None, date_to=None, use_time=None, page=None, page_size=None, product_type=None, company_downloads=None) -> web.Response:
    """Returns information about a customer&#39;s downloaded assets.

    Returns information about a customer&#39;s previously downloaded assets.  You&#39;ll need an API key and access token to use this resource.     This endpoint requires being a Getty Images customer to limit your results to only assets that you have a license to use,  you need to also include an authorization token in the header of your request.  Please consult our [Authorization FAQ](http://developers.gettyimages.com/en/authorization-faq.html) for more information on authorization tokens. 

    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str
    :param date_from: If specified, selects assets downloaded on or after this date. Dates should be submitted in ISO 8601 format (i.e., YYYY-MM-DD).   Any hour, minute, second values in the request are not used, unless useTimePart parameter is included.  Date/times in the response are UTC. Default is 30 days prior to date_to
    :type date_from: str
    :param date_to: If specified, selects assets downloaded on or before this date. Dates should be submitted in ISO 8601 format (i.e., YYYY-MM-DD)  Any hour, minute, second values in the request are not used, unless useTimePart parameter is included.  Date/times in the response are UTC. Default is current date or 30 days after specified start date, whichever one is earlier.
    :type date_to: str
    :param use_time: If specified, time values provided with date_to or date_from will be used. Time values should be appended to the date value in ISO 8601 format  i.e.: 2019-09-19T19:30:37 or 2019-09-19 19:30:37.  Time zone can be specified as optional.  Default value is false
    :type use_time: bool
    :param page: Identifies page to return. Default is 1.
    :type page: int
    :param page_size: Specifies page size. Default is 30, maximum page_size is 100.
    :type page_size: int
    :param product_type: Specifies product type to be included in the previous download results. Product types easyaccess, editorialsubscription, imagepack, and premiumaccess are for GettyImages API keys. Product types royaltyfreesubscription and creditpack are for iStock API keys. To get previous iStockPhoto credit downloads, creditpack must be selected.
    :type product_type: dict | bytes
    :param company_downloads: If specified, returns the list of previously downloaded images for all users in your company. Your account must be enabled for this functionality. Contact your Getty Images account rep for more information. Default is false.
    :type company_downloads: bool

    """
    date_from = util.deserialize_datetime(date_from)
    date_to = util.deserialize_datetime(date_to)
    product_type = .from_dict(product_type)
    return web.Response(status=200)


async def v3_downloads_images_id_post(request: web.Request, id, accept_language=None, auto_download=None, file_type=None, height=None, product_id=None, product_type=None, use_team_credits=None, body=None) -> web.Response:
    """Download an image

    Use this endpoint to generate download URLs and related data for images you are authorized to download.  Most product offerings have enforced periodic download limits such as monthly, weekly, and daily. When this operation executes, the count of allowed downloads is decremented by one for the product offering. Once the download limit is reached for a given product offering, no further downloads may be requested for that product offering until the next download period.  The download limit for a given download period is covered in your product agreement established with Getty Images.  You&#39;ll need an API key and a [Resource Owner Grant or Implicit Grant](http://developers.gettyimages.com/en/authorization-faq.html) access token to use this resource.  ## Auto Downloads The &#x60;auto_download&#x60; request query parameter specifies whether to automatically download the image.  If the &#x60;auto_download&#x60; request query parameter is set to _true_, the API will return an HTTP status code 303 *See Other*. Your client code will need to process this response and redirect to the URI specified in the *Location* header to enable you to automatically download the file. The redirection workflow follows the [HTTP 1.1 protocol](https://tools.ietf.org/html/rfc7231#section-6.4.4).  Client Request:  &#x60;&#x60;&#x60; https://api.gettyimages.com/v3/downloads/images/[asset_id]?auto_download&#x3D;true &#x60;&#x60;&#x60;  Server Response:  Your client code should follow redirect (3xx) status codes returned from the URI in the response Location header. More information here: [HTTP 1.1 protocol](https://tools.ietf.org/html/rfc7231#section-6.4).  &#x60;&#x60;&#x60; HTTP/1.1 303 See Other Location: https://delivery.gettyimages.com/... &#x60;&#x60;&#x60;  If the &#x60;auto_download&#x60; request query parameter is set to false, the API will return a HTTP status code 200, along with the URI in the response body which can be used to download the image.   Client Request:  &#x60;&#x60;&#x60; https://api.gettyimages.com/v3/downloads/images/[asset_id]?auto_download&#x3D;false &#x60;&#x60;&#x60;  Server Response:  &#x60;&#x60;&#x60; HTTP/1.1 200 OK {  \&quot;uri\&quot;: \&quot;https://delivery.gettyimages.com/...\&quot; } &#x60;&#x60;&#x60; ## Downloading Via the Returned URI  Your client code should follow redirect (3xx) status codes returned from the URI in the response. More information here: [HTTP 1.1 protocol](https://tools.ietf.org/html/rfc7231#section-6.4).  The URI returned by this call should be considered opaque and the format could change at any time. In order to get the filename, length or file type, the response headers must be inspected. An example response follows:  &#x60;&#x60;&#x60; content-length: 33959979 content-type: image/jpeg content-disposition: attachment; filename&#x3D;GettyImages-1167612765.jpg &#x60;&#x60;&#x60;  The &#x60;content-disposition&#x60; header must be parsed to get a usable filename.  ## Download URI expiration  Download URIs are _**only valid for 24 hours**_, starting from the moment they are returned from this call. 

    :param id: &lt;remarks&gt;                      Id of image to download.                  &lt;/remarks&gt;
    :type id: str
    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str
    :param auto_download: &lt;remarks&gt;                      Specifies whether to auto-download the image. If true is specified, a 303 SeeOther status is returned with a                      Location header set to the location of the image.                      If false is specified, the download URI will be returned in the response message. Default is true.                  &lt;/remarks&gt;
    :type auto_download: bool
    :param file_type: &lt;remarks&gt;                      File Type expressed with three character file extension.                  &lt;/remarks&gt;
    :type file_type: dict | bytes
    :param height: &lt;remarks&gt;                      Specifies the pixel height of the particular image to download.                      Available heights can be found in the images/{ids} response for the specific image.                      If left blank, it will return the largest available size.                  &lt;/remarks&gt;
    :type height: str
    :param product_id: &lt;remarks&gt;                      Identifier of the instance for the selected product offering type.                  &lt;/remarks&gt;
    :type product_id: int
    :param product_type: &lt;remarks&gt;                      Product types easyaccess, editorialsubscription, imagepack, and premiumaccess are for GettyImages API keys. Product types royaltyfreesubscription and creditpack are for iStock API keys. Default product type for iStock API keys is creditpack.                  &lt;/remarks&gt;
    :type product_type: dict | bytes
    :param use_team_credits: Specifies whether to download the image with iStock Team Credits. Only applicable to iStock API keys authenticated with a user that has Team Credits. Blank is the same as False.
    :type use_team_credits: bool
    :param body: &lt;remarks&gt;                      Additional information required from specific customers when downloading.                       Only users who have been set up with a project code by Getty Images Sales need to use this field.                  &lt;/remarks&gt;
    :type body: dict | bytes

    """
    file_type = .from_dict(file_type)
    product_type = .from_dict(product_type)
    body = PremiumAccessDownloadData.from_dict(body)
    return web.Response(status=200)


async def v3_downloads_videos_id_post(request: web.Request, id, accept_language=None, auto_download=None, size=None, product_id=None, product_type=None, use_team_credits=None, body=None) -> web.Response:
    """Download a video

    Use this endpoint to generate download URLs and related data for videos you are authorized to download.  Most product offerings have enforced periodic download limits such as monthly, weekly, and daily. When this operation executes, the count of allowed downloads is decremented by one for the product offering. Once the download limit is reached for a given product offering, no further downloads may be requested for that product offering until the next download period.  The download limit for a given download period is covered in your product agreement established with Getty Images.  You&#39;ll need an API key and a [Resource Owner Grant or Implicit Grant](http://developers.gettyimages.com/en/authorization-faq.html) access token to use this resource.  ## Auto Downloads The &#x60;auto_download&#x60; request query parameter specifies whether to automatically download the video.  If the &#x60;auto_download&#x60; request query parameter is set to _true_, the API will return an HTTP status code 303 *See Other*. Your client code will need to process this response and redirect to the URI specified in the *Location* header to enable you to automatically download the file. The redirection workflow follows the [HTTP 1.1 protocol](https://tools.ietf.org/html/rfc7231#section-6.4.4).  Client Request:  &#x60;&#x60;&#x60; https://api.gettyimages.com/v3/downloads/videos/[asset_id]?auto_download&#x3D;true &#x60;&#x60;&#x60;  Server Response:  Your client code should follow redirect (3xx) status codes returned from the URI in the response Location header. More information here: [HTTP 1.1 protocol](https://tools.ietf.org/html/rfc7231#section-6.4).  &#x60;&#x60;&#x60; HTTP/1.1 303 See Other Location: https://delivery.gettyimages.com/... &#x60;&#x60;&#x60;  If the &#x60;auto_download&#x60; request query parameter is set to false, the API will return a HTTP status code 200, along with the URI in the response body which can be used to download the video.   Client Request:  &#x60;&#x60;&#x60; https://api.gettyimages.com/v3/downloads/videos/[asset_id]?auto_download&#x3D;false &#x60;&#x60;&#x60;  Server Response:  &#x60;&#x60;&#x60; HTTP/1.1 200 OK {  \&quot;uri\&quot;: \&quot;https://delivery.gettyimages.com/...\&quot; } &#x60;&#x60;&#x60;  ## Downloading Via the Returned URI  Your client code should follow redirect (3xx) status codes returned from the URI in the response. More information here: [HTTP 1.1 protocol](https://tools.ietf.org/html/rfc7231#section-6.4).  The URI returned by this call should be considered opaque and the format could change at any time. In order to get the filename, length or file type, the response headers must be inspected. An example response follows:  &#x60;&#x60;&#x60; content-length: 283925783 content-type: video/quicktime content-disposition: attachment; filename&#x3D;GettyImages-690773579.mov &#x60;&#x60;&#x60;  The &#x60;content-disposition&#x60; header must be parsed to get a usable filename.  ## Download URI expiration  Download URIs are _**only valid for 24 hours**_, starting from the moment they are returned from this call. 

    :param id: &lt;remarks&gt;                      Id of video to download.                  &lt;/remarks&gt;
    :type id: str
    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str
    :param auto_download: &lt;remarks&gt;                      Specifies whether to auto-download the video. If true is specified, a 303 SeeOther status is returned with a                      Location header set to the location of the video.                      If false is specified, the download URI will be returned in the response message. Default is false.                  &lt;/remarks&gt;
    :type auto_download: bool
    :param size: Specifies the size to be downloaded.
    :type size: str
    :param product_id: &lt;remarks&gt;                      Identifier of the instance for the selected product offering type.                  &lt;/remarks&gt;
    :type product_id: int
    :param product_type: &lt;remarks&gt;                      Product types easyaccess, editorialsubscription, imagepack, and premiumaccess are for GettyImages API keys. Product types royaltyfreesubscription and creditpack are for iStock API keys. Default product type for iStock API keys is creditpack.                  &lt;/remarks&gt;
    :type product_type: dict | bytes
    :param use_team_credits: Specifies whether to download the image with iStock Team Credits. Only applicable to iStock API keys authenticated with a user that has Team Credits. Blank is the same as False.
    :type use_team_credits: bool
    :param body: &lt;remarks&gt;                      Additional information required from specific customers when downloading.                       Only users who have been set up with a project code by Getty Images Sales need to use this field.                  &lt;/remarks&gt;
    :type body: dict | bytes

    """
    product_type = .from_dict(product_type)
    body = PremiumAccessDownloadData.from_dict(body)
    return web.Response(status=200)
