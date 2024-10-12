from typing import List, Dict
from aiohttp import web

from openapi_server.models.terrain_tile import TerrainTile
from openapi_server import util


async def vectortile_terraintiles_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, altitude_precision_centimeters=None, client_info_api_client=None, client_info_application_id=None, client_info_application_version=None, client_info_device_model=None, client_info_operating_system=None, client_info_platform=None, client_info_user_id=None, max_elevation_resolution_cells=None, min_elevation_resolution_cells=None, terrain_formats=None, enable_modeled_volumes=None, enable_political_features=None, enable_private_roads=None, enable_unclipped_buildings=None, language_code=None, region_code=None) -> web.Response:
    """vectortile_terraintiles_get

    Gets a terrain tile by its tile resource name.

    :param name: Required. Resource name of the tile. The tile resource name is prefixed by its collection ID &#x60;terraintiles/&#x60; followed by the resource ID, which encodes the tile&#39;s global x and y coordinates and zoom level as &#x60;@,,z&#x60;. For example, &#x60;terraintiles/@1,2,3z&#x60;.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param altitude_precision_centimeters: The precision of terrain altitudes in centimeters. Possible values: between 1 (cm level precision) and 1,000,000 (10-kilometer level precision).
    :type altitude_precision_centimeters: int
    :param client_info_api_client: API client name and version. For example, the SDK calling the API. The exact format is up to the client.
    :type client_info_api_client: str
    :param client_info_application_id: Application ID, such as the package name on Android and the bundle identifier on iOS platforms.
    :type client_info_application_id: str
    :param client_info_application_version: Application version number, such as \&quot;1.2.3\&quot;. The exact format is application-dependent.
    :type client_info_application_version: str
    :param client_info_device_model: Device model as reported by the device. The exact format is platform-dependent.
    :type client_info_device_model: str
    :param client_info_operating_system: Operating system name and version as reported by the OS. For example, \&quot;Mac OS X 10.10.4\&quot;. The exact format is platform-dependent.
    :type client_info_operating_system: str
    :param client_info_platform: Platform where the application is running.
    :type client_info_platform: str
    :param client_info_user_id: Required. A client-generated user ID. The ID should be generated and persisted during the first user session or whenever a pre-existing ID is not found. The exact format is up to the client. This must be non-empty in a GetFeatureTileRequest (whether via the header or GetFeatureTileRequest.client_info).
    :type client_info_user_id: str
    :param max_elevation_resolution_cells: The maximum allowed resolution for the returned elevation heightmap. Possible values: between 1 and 1024 (and not less than min_elevation_resolution_cells). Over-sized heightmaps will be non-uniformly down-sampled such that each edge is no longer than this value. Non-uniformity is chosen to maximise the amount of preserved data. For example: Original resolution: 100px (width) * 30px (height) max_elevation_resolution: 30 New resolution: 30px (width) * 30px (height)
    :type max_elevation_resolution_cells: int
    :param min_elevation_resolution_cells:  api-linter: core::0131::request-unknown-fields&#x3D;disabled aip.dev/not-precedent: Maintaining existing request parameter pattern. The minimum allowed resolution for the returned elevation heightmap. Possible values: between 0 and 1024 (and not more than max_elevation_resolution_cells). Zero is supported for backward compatibility. Under-sized heightmaps will be non-uniformly up-sampled such that each edge is no shorter than this value. Non-uniformity is chosen to maximise the amount of preserved data. For example: Original resolution: 30px (width) * 10px (height) min_elevation_resolution: 30 New resolution: 30px (width) * 30px (height)
    :type min_elevation_resolution_cells: int
    :param terrain_formats: Terrain formats that the client understands.
    :type terrain_formats: List[str]
    :param enable_modeled_volumes: Flag indicating whether 3D building models should be enabled. If this is set structures will be returned as 3D modeled volumes rather than 2.5D extruded areas where possible.
    :type enable_modeled_volumes: bool
    :param enable_political_features: Flag indicating whether political features should be returned.
    :type enable_political_features: bool
    :param enable_private_roads: Flag indicating whether the returned tile will contain road features that are marked private. Private roads are indicated by the Feature.segment_info.road_info.is_private field.
    :type enable_private_roads: bool
    :param enable_unclipped_buildings: Flag indicating whether unclipped buildings should be returned. If this is set, building render ops will extend beyond the tile boundary. Buildings will only be returned on the tile that contains their centroid.
    :type enable_unclipped_buildings: bool
    :param language_code: Required. The BCP-47 language code corresponding to the language in which the name was requested, such as \&quot;en-US\&quot; or \&quot;sr-Latn\&quot;. For more information, see http://www.unicode.org/reports/tr35/#Unicode_locale_identifier.
    :type language_code: str
    :param region_code: Required. The Unicode country/region code (CLDR) of the location from which the request is coming from, such as \&quot;US\&quot; and \&quot;419\&quot;. For more information, see http://www.unicode.org/reports/tr35/#unicode_region_subtag.
    :type region_code: str

    """
    return web.Response(status=200)
