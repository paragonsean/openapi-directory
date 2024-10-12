from typing import List, Dict
from aiohttp import web

from openapi_server.models.representative_info_data import RepresentativeInfoData
from openapi_server.models.representative_info_response import RepresentativeInfoResponse
from openapi_server import util


async def civicinfo_representatives_representative_info_by_address(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, address=None, include_offices=None, levels=None, roles=None) -> web.Response:
    """civicinfo_representatives_representative_info_by_address

    Looks up political geography and representative information for a single address.

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
    :param address: The address to look up. May only be specified if the field ocdId is not given in the URL
    :type address: str
    :param include_offices: Whether to return information about offices and officials. If false, only the top-level district information will be returned.
    :type include_offices: bool
    :param levels: A list of office levels to filter by. Only offices that serve at least one of these levels will be returned. Divisions that don&#39;t contain a matching office will not be returned.
    :type levels: List[str]
    :param roles: A list of office roles to filter by. Only offices fulfilling one of these roles will be returned. Divisions that don&#39;t contain a matching office will not be returned.
    :type roles: List[str]

    """
    return web.Response(status=200)


async def civicinfo_representatives_representative_info_by_division(request: web.Request, ocd_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, levels=None, recursive=None, roles=None) -> web.Response:
    """civicinfo_representatives_representative_info_by_division

    Looks up representative information for a single geographic division.

    :param ocd_id: The Open Civic Data division identifier of the division to look up.
    :type ocd_id: str
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
    :param levels: A list of office levels to filter by. Only offices that serve at least one of these levels will be returned. Divisions that don&#39;t contain a matching office will not be returned.
    :type levels: List[str]
    :param recursive: If true, information about all divisions contained in the division requested will be included as well. For example, if querying ocd-division/country:us/district:dc, this would also return all DC&#39;s wards and ANCs.
    :type recursive: bool
    :param roles: A list of office roles to filter by. Only offices fulfilling one of these roles will be returned. Divisions that don&#39;t contain a matching office will not be returned.
    :type roles: List[str]

    """
    return web.Response(status=200)
