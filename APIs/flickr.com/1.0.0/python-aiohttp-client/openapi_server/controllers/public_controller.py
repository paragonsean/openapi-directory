from typing import List, Dict
from aiohttp import web

from openapi_server.models.echo200_response import Echo200Response
from openapi_server.models.get_album_by_id200_response import GetAlbumByID200Response
from openapi_server.models.get_albums_by_person_id200_response import GetAlbumsByPersonID200Response
from openapi_server.models.get_favorites_by_person_id200_response import GetFavoritesByPersonID200Response
from openapi_server.models.get_favorites_context_by_id200_response import GetFavoritesContextByID200Response
from openapi_server.models.get_gallery_photos_by_id200_response import GetGalleryPhotosByID200Response
from openapi_server.models.get_group_by_id200_response import GetGroupByID200Response
from openapi_server.models.get_group_discussions_by_id200_response import GetGroupDiscussionsByID200Response
from openapi_server.models.get_group_topic_by_id200_response import GetGroupTopicByID200Response
from openapi_server.models.get_group_topic_replies_by_id200_response import GetGroupTopicRepliesByID200Response
from openapi_server.models.get_license_by_id200_response import GetLicenseByID200Response
from openapi_server.models.get_person_by_id200_response import GetPersonByID200Response
from openapi_server.models.get_photo_by_id200_response import GetPhotoByID200Response
from openapi_server.models.get_photo_exif_by_id200_response import GetPhotoExifByID200Response
from openapi_server.models.get_photo_sizes_by_id200_response import GetPhotoSizesByID200Response
from openapi_server import util


async def echo(request: web.Request, api_key, echo=None) -> web.Response:
    """echo

    Echos the input parameters back in the response

    :param api_key: 
    :type api_key: str
    :param echo: 
    :type echo: str

    """
    return web.Response(status=200)


async def get_access_token(request: web.Request, oauth_consumer_key, oauth_nonce, oauth_timestamp, oauth_signature_method, oauth_version, oauth_signature, oauth_verifier, oauth_token) -> web.Response:
    """get_access_token

    Returns an access token

    :param oauth_consumer_key: 
    :type oauth_consumer_key: str
    :param oauth_nonce: 
    :type oauth_nonce: str
    :param oauth_timestamp: 
    :type oauth_timestamp: str
    :param oauth_signature_method: 
    :type oauth_signature_method: str
    :param oauth_version: 
    :type oauth_version: str
    :param oauth_signature: 
    :type oauth_signature: str
    :param oauth_verifier: 
    :type oauth_verifier: str
    :param oauth_token: 
    :type oauth_token: str

    """
    return web.Response(status=200)


async def get_album_by_id(request: web.Request, api_key, photoset_id) -> web.Response:
    """get_album_by_id

    Returns a list of photos in an album.

    :param api_key: 
    :type api_key: str
    :param photoset_id: 
    :type photoset_id: str

    """
    return web.Response(status=200)


async def get_album_context_by_id(request: web.Request, api_key, photo_id, photoset_id=None) -> web.Response:
    """get_album_context_by_id

    Returns next and previous photos for a photo in a set

    :param api_key: 
    :type api_key: str
    :param photo_id: 
    :type photo_id: str
    :param photoset_id: 
    :type photoset_id: str

    """
    return web.Response(status=200)


async def get_albums_by_person_id(request: web.Request, api_key, user_id, page=None, per_page=None) -> web.Response:
    """get_albums_by_person_id

    Returns the albums belonging to the specified user

    :param api_key: 
    :type api_key: str
    :param user_id: 
    :type user_id: str
    :param page: 
    :type page: 
    :param per_page: 
    :type per_page: 

    """
    return web.Response(status=200)


async def get_favorites_by_person_id(request: web.Request, api_key, user_id, min_fave_date=None, max_fave_date=None, page=None, per_page=None) -> web.Response:
    """get_favorites_by_person_id

    Returns a list of the user&#39;s favorite photos. Only photos which the calling user has permission to see are returned.

    :param api_key: 
    :type api_key: str
    :param user_id: 
    :type user_id: str
    :param min_fave_date: 
    :type min_fave_date: 
    :param max_fave_date: 
    :type max_fave_date: 
    :param page: 
    :type page: 
    :param per_page: 
    :type per_page: 

    """
    return web.Response(status=200)


async def get_favorites_context_by_id(request: web.Request, api_key, photo_id, user_id=None) -> web.Response:
    """get_favorites_context_by_id

    Returns next and previous favorites for a photo in a user&#39;s favorites

    :param api_key: 
    :type api_key: str
    :param photo_id: 
    :type photo_id: str
    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)


async def get_gallery_photos_by_id(request: web.Request, api_key, gallery_id) -> web.Response:
    """get_gallery_photos_by_id

    Returns a list of photos in a gallery.

    :param api_key: 
    :type api_key: str
    :param gallery_id: 
    :type gallery_id: str

    """
    return web.Response(status=200)


async def get_group_by_id(request: web.Request, api_key, group_id=None, group_path_alias=None, lang=None) -> web.Response:
    """get_group_by_id

    Get information about a group

    :param api_key: 
    :type api_key: str
    :param group_id: 
    :type group_id: str
    :param group_path_alias: 
    :type group_path_alias: str
    :param lang: 
    :type lang: str

    """
    return web.Response(status=200)


async def get_group_discussions_by_id(request: web.Request, api_key, group_id=None, page=None, per_page=None) -> web.Response:
    """get_group_discussions_by_id

    Get a list of discussion topics in a group.

    :param api_key: 
    :type api_key: str
    :param group_id: 
    :type group_id: str
    :param page: 
    :type page: 
    :param per_page: 
    :type per_page: 

    """
    return web.Response(status=200)


async def get_group_photos_by_id(request: web.Request, api_key, group_id=None) -> web.Response:
    """get_group_photos_by_id

    Returns a list of pool photos for a given group

    :param api_key: 
    :type api_key: str
    :param group_id: 
    :type group_id: str

    """
    return web.Response(status=200)


async def get_group_topic_by_id(request: web.Request, api_key, topic_id, group_id=None) -> web.Response:
    """get_group_topic_by_id

    Get information about a group discussion topic

    :param api_key: 
    :type api_key: str
    :param topic_id: 
    :type topic_id: str
    :param group_id: 
    :type group_id: str

    """
    return web.Response(status=200)


async def get_group_topic_replies_by_id(request: web.Request, api_key, topic_id, reply_id, group_id=None) -> web.Response:
    """get_group_topic_replies_by_id

    Get information on a group topic reply

    :param api_key: 
    :type api_key: str
    :param topic_id: 
    :type topic_id: str
    :param reply_id: 
    :type reply_id: str
    :param group_id: 
    :type group_id: str

    """
    return web.Response(status=200)


async def get_license_by_id(request: web.Request, api_key) -> web.Response:
    """get_license_by_id

    Fetches a list of available photo licenses for Flickr

    :param api_key: 
    :type api_key: str

    """
    return web.Response(status=200)


async def get_media_by_person_id(request: web.Request, api_key, user_id, safe_search=None, min_upload_date=None, max_upload_date=None, min_taken_date=None, max_taken_date=None, content_type=None, privacy_filter=None, page=None, per_page=None) -> web.Response:
    """get_media_by_person_id

    Return photos from the given user&#39;s photostream

    :param api_key: 
    :type api_key: str
    :param user_id: 
    :type user_id: str
    :param safe_search: 
    :type safe_search: 
    :param min_upload_date: 
    :type min_upload_date: 
    :param max_upload_date: 
    :type max_upload_date: 
    :param min_taken_date: 
    :type min_taken_date: 
    :param max_taken_date: 
    :type max_taken_date: 
    :param content_type: 
    :type content_type: 
    :param privacy_filter: 
    :type privacy_filter: 
    :param page: 
    :type page: 
    :param per_page: 
    :type per_page: 

    """
    return web.Response(status=200)


async def get_media_by_search(request: web.Request, api_key, text=None, tags=None, user_id=None, min_upload_date=None, max_upload_date=None, min_taken_date=None, max_taken_date=None, license=None, sort=None, privacy_filter=None, bbox=None, accuracy=None, safe_search=None, content_type=None, machine_tags=None, machine_tag_mode=None, group_id=None, contacts=None, woe_id=None, place_id=None, media=None, has_geo=None, geo_context=None, lat=None, lon=None, radius=None, radius_units=None, is_commons=None, in_gallery=None, is_getty=None, per_page=None, page=None) -> web.Response:
    """get_media_by_search

    Return a list of photos matching some criteria.

    :param api_key: 
    :type api_key: str
    :param text: A free text search. Photos who&#39;s title, description or tags contain the text will be returned. You can exclude results that match a term by prepending it with a - character.
    :type text: str
    :param tags: A comma-delimited list of tags. Photos with one or more of the tags listed will be returned. You can exclude results that match a term by prepending it with a - character.
    :type tags: str
    :param user_id: The NSID of the user who&#39;s photo to search. If this parameter isn&#39;t passed then everybody&#39;s public photos will be searched. A value of \&quot;me\&quot; will search against the calling user&#39;s photos for authenticated calls.
    :type user_id: str
    :param min_upload_date: Minimum upload date. Photos with an upload date greater than or equal to this value will be returned. The date can be in the form of a unix timestamp or mysql datetime.
    :type min_upload_date: str
    :param max_upload_date: Maximum upload date. Photos with an upload date less than or equal to this value will be returned. The date can be in the form of a unix timestamp or mysql datetime.
    :type max_upload_date: str
    :param min_taken_date: Minimum taken date. Photos with an taken date greater than or equal to this value will be returned. The date can be in the form of a mysql datetime or unix timestamp.
    :type min_taken_date: str
    :param max_taken_date: Maximum taken date. Photos with an taken date less than or equal to this value will be returned. The date can be in the form of a mysql datetime or unix timestamp.
    :type max_taken_date: str
    :param license: The license id for photos (for possible values see the flickr.photos.licenses.getInfo method). Multiple licenses may be comma-separated.
    :type license: str
    :param sort: The order in which to sort returned photos. Deafults to date-posted-desc (unless you are doing a radial geo query, in which case the default sorting is by ascending distance from the point specified). The possible values are:   date-posted-asc,   date-posted-desc,   date-taken-asc,   date-taken-desc,   interestingness-desc,   interestingness-asc, and   relevance. 
    :type sort: str
    :param privacy_filter: Return photos only matching a certain privacy level. This only applies when making an authenticated call to view photos you own. Valid values are:,   1: public photos,   2: private photos visible to friends,   3: private photos visible to family,   4: private photos visible to friends &amp; family,   5: completely private photos 
    :type privacy_filter: 
    :param bbox: A comma-delimited list of 4 values defining the Bounding Box of the area that will be searched.
    :type bbox: str
    :param accuracy: Recorded accuracy level of the location information. Current range is 1-16:   World level is 1   Country is ~3   Region is ~6   City is ~11   Street is ~16 
    :type accuracy: str
    :param safe_search: Safe search setting:   1: for safe,   2: for moderate,   3: for restricted 
    :type safe_search: 
    :param content_type: Content Type setting:   1: photos only.   2: screenshots only.   3: &#39;other&#39; only.   4: photos and screenshots.   5: screenshots and &#39;other&#39;.   6: photos and &#39;other&#39;.   7: photos, screenshots, and &#39;other&#39; (all). 
    :type content_type: 
    :param machine_tags: Aside from passing in a fully formed machine tag, there is a special syntax for searching on specific properties : Find photos using the &#39;dc&#39; namespace : \&quot;machine_tags\&quot; &#x3D;&gt; \&quot;dc:\&quot; Find photos with a title in the &#39;dc&#39; namespace : \&quot;machine_tags\&quot; &#x3D;&gt; \&quot;dc:title&#x3D;\&quot; Find photos titled \&quot;mr. camera\&quot; in the &#39;dc&#39; namespace : \&quot;machine_tags\&quot; &#x3D;&gt; \&quot;dc:title&#x3D;\\\&quot;mr. camera\\\&quot; Find photos whose value is \&quot;mr. camera\&quot; : \&quot;machine_tags\&quot; &#x3D;&gt; \&quot;*:*&#x3D;\\\&quot;mr. camera\\\&quot;\&quot; Find photos that have a title, in any namespace : \&quot;machine_tags\&quot; &#x3D;&gt; \&quot;*:title&#x3D;\&quot; Find photos that have a title, in any namespace, whose value is \&quot;mr. camera\&quot; : \&quot;machine_tags\&quot; &#x3D;&gt; \&quot;*:title&#x3D;\\\&quot;mr. camera\\\&quot;\&quot; Find photos, in the &#39;dc&#39; namespace whose value is \&quot;mr. camera\&quot; : \&quot;machine_tags\&quot; &#x3D;&gt; \&quot;dc:*&#x3D;\\\&quot;mr. camera\\\&quot;\&quot; Multiple machine tags may be queried by passing a comma-separated list. The number of machine tags you can pass in a single query depends on the tag mode (AND or OR) that you are querying with. \&quot;AND\&quot; queries are limited to (16) machine tags. \&quot;OR\&quot; queries are limited to (8). 
    :type machine_tags: str
    :param machine_tag_mode: Either &#39;any&#39; for an OR combination of tags, or &#39;all&#39; for an AND combination. Defaults to &#39;any&#39; if not specified.
    :type machine_tag_mode: str
    :param group_id: The id of a group who&#39;s pool to search. If specified, only matching photos posted to the group&#39;s pool will be returned.
    :type group_id: str
    :param contacts: Search your contacts. Either &#39;all&#39; or &#39;ff&#39; for just friends and family. (Experimental)
    :type contacts: str
    :param woe_id: A 32-bit identifier that uniquely represents spatial entities. (not used if bbox argument is present).
    :type woe_id: str
    :param place_id: A Flickr place id. (not used if bbox argument is present). Geo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against \&quot;parameterless searches\&quot; for queries without a geo component. A tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters — If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future). 
    :type place_id: str
    :param media: Filter results by media type. Possible values are all (default), photos or videos
    :type media: str
    :param has_geo: Any photo that has been geotagged, or if the value is \&quot;0\&quot; any photo that has not been geotagged. Geo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against \&quot;parameterless searches\&quot; for queries without a geo component. A tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters — If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future). 
    :type has_geo: str
    :param geo_context: Geo context is a numeric value representing the photo&#39;s geotagginess beyond latitude and longitude. For example, you may wish to search for photos that were taken \&quot;indoors\&quot; or \&quot;outdoors\&quot;. The current list of context IDs is: 0, not defined. 1, indoors. 2, outdoors. Geo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against \&quot;parameterless searches\&quot; for queries without a geo component. A tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters — If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future). 
    :type geo_context: str
    :param lat: A valid latitude, in decimal format, for doing radial geo queries. Geo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against \&quot;parameterless searches\&quot; for queries without a geo component. A tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters — If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future). 
    :type lat: str
    :param lon: A valid longitude, in decimal format, for doing radial geo queries. Geo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against \&quot;parameterless searches\&quot; for queries without a geo component. A tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters — If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future). 
    :type lon: str
    :param radius: A valid radius used for geo queries, greater than zero and less than 20 miles (or 32 kilometers), for use with point-based geo queries. The default value is 5 (km).
    :type radius: 
    :param radius_units: The unit of measure when doing radial geo queries. Valid options are \&quot;mi\&quot; (miles) and \&quot;km\&quot; (kilometers). The default is \&quot;km\&quot;.
    :type radius_units: str
    :param is_commons: Limit the scope of the search to only photos that are part of the Flickr Commons project. Default is false.
    :type is_commons: bool
    :param in_gallery: Limit the scope of the search to only photos that are in a gallery? Default is false, search all photos.
    :type in_gallery: bool
    :param is_getty: Limit the scope of the search to only photos that are for sale on Getty. Default is false.
    :type is_getty: bool
    :param per_page: Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.
    :type per_page: 
    :param page: The page of results to return. If this argument is omitted, it defaults to 1.
    :type page: 

    """
    return web.Response(status=200)


async def get_person_by_id(request: web.Request, api_key, user_id=None) -> web.Response:
    """get_person_by_id

    Returns a person

    :param api_key: 
    :type api_key: str
    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)


async def get_photo_by_id(request: web.Request, api_key, photo_id) -> web.Response:
    """get_photo_by_id

    Returns a photo

    :param api_key: 
    :type api_key: str
    :param photo_id: 
    :type photo_id: str

    """
    return web.Response(status=200)


async def get_photo_exif_by_id(request: web.Request, api_key, photo_id, secret=None) -> web.Response:
    """get_photo_exif_by_id

    Retrieves a list of EXIF/TIFF/GPS tags for a given photo. The calling user must have permission to view the photo.

    :param api_key: 
    :type api_key: str
    :param photo_id: 
    :type photo_id: str
    :param secret: 
    :type secret: str

    """
    return web.Response(status=200)


async def get_photo_sizes_by_id(request: web.Request, api_key, photo_id) -> web.Response:
    """get_photo_sizes_by_id

    Returns photo sizes

    :param api_key: 
    :type api_key: str
    :param photo_id: 
    :type photo_id: str

    """
    return web.Response(status=200)


async def get_photolist_context_by_id(request: web.Request, api_key, photo_id, photolist_id) -> web.Response:
    """get_photolist_context_by_id

    Returns next and previous photos in a photo list

    :param api_key: 
    :type api_key: str
    :param photo_id: 
    :type photo_id: str
    :param photolist_id: 
    :type photolist_id: str

    """
    return web.Response(status=200)


async def get_photostream_context_by_id(request: web.Request, api_key, photo_id) -> web.Response:
    """get_photostream_context_by_id

    Returns next and previous photos for a photo in a photostream

    :param api_key: 
    :type api_key: str
    :param photo_id: 
    :type photo_id: str

    """
    return web.Response(status=200)


async def get_request_token(request: web.Request, oauth_consumer_key, oauth_nonce, oauth_timestamp, oauth_signature_method, oauth_version, oauth_signature, oauth_callback) -> web.Response:
    """get_request_token

    Returns an oauth token and oauth token secret

    :param oauth_consumer_key: 
    :type oauth_consumer_key: str
    :param oauth_nonce: 
    :type oauth_nonce: str
    :param oauth_timestamp: 
    :type oauth_timestamp: str
    :param oauth_signature_method: 
    :type oauth_signature_method: str
    :param oauth_version: 
    :type oauth_version: str
    :param oauth_signature: 
    :type oauth_signature: str
    :param oauth_callback: 
    :type oauth_callback: str

    """
    return web.Response(status=200)


async def restmethodflickr_groups_pools_get_context_get(request: web.Request, api_key, photo_id, group_id=None) -> web.Response:
    """restmethodflickr_groups_pools_get_context_get

    Returns next and previous photos for a photo in a group pool

    :param api_key: 
    :type api_key: str
    :param photo_id: 
    :type photo_id: str
    :param group_id: 
    :type group_id: str

    """
    return web.Response(status=200)


async def upload_photo(request: web.Request, api_key, photo, content_type=None, description=None, hidden=None, is_family=None, is_friend=None, is_public=None, safety_level=None, tags=None, title=None) -> web.Response:
    """upload_photo

    Uploads a new photo to Flickr

    :param api_key: 
    :type api_key: str
    :param photo: 
    :type photo: str
    :param content_type: 
    :type content_type: str
    :param description: 
    :type description: str
    :param hidden: 
    :type hidden: str
    :param is_family: 
    :type is_family: str
    :param is_friend: 
    :type is_friend: str
    :param is_public: 
    :type is_public: str
    :param safety_level: 
    :type safety_level: str
    :param tags: 
    :type tags: str
    :param title: 
    :type title: str

    """
    return web.Response(status=200)
