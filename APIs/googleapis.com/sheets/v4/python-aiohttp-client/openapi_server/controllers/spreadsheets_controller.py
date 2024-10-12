from typing import List, Dict
from aiohttp import web

from openapi_server.models.append_values_response import AppendValuesResponse
from openapi_server.models.batch_clear_values_by_data_filter_request import BatchClearValuesByDataFilterRequest
from openapi_server.models.batch_clear_values_by_data_filter_response import BatchClearValuesByDataFilterResponse
from openapi_server.models.batch_clear_values_request import BatchClearValuesRequest
from openapi_server.models.batch_clear_values_response import BatchClearValuesResponse
from openapi_server.models.batch_get_values_by_data_filter_request import BatchGetValuesByDataFilterRequest
from openapi_server.models.batch_get_values_by_data_filter_response import BatchGetValuesByDataFilterResponse
from openapi_server.models.batch_get_values_response import BatchGetValuesResponse
from openapi_server.models.batch_update_spreadsheet_request import BatchUpdateSpreadsheetRequest
from openapi_server.models.batch_update_spreadsheet_response import BatchUpdateSpreadsheetResponse
from openapi_server.models.batch_update_values_by_data_filter_request import BatchUpdateValuesByDataFilterRequest
from openapi_server.models.batch_update_values_by_data_filter_response import BatchUpdateValuesByDataFilterResponse
from openapi_server.models.batch_update_values_request import BatchUpdateValuesRequest
from openapi_server.models.batch_update_values_response import BatchUpdateValuesResponse
from openapi_server.models.clear_values_response import ClearValuesResponse
from openapi_server.models.copy_sheet_to_another_spreadsheet_request import CopySheetToAnotherSpreadsheetRequest
from openapi_server.models.developer_metadata import DeveloperMetadata
from openapi_server.models.get_spreadsheet_by_data_filter_request import GetSpreadsheetByDataFilterRequest
from openapi_server.models.search_developer_metadata_request import SearchDeveloperMetadataRequest
from openapi_server.models.search_developer_metadata_response import SearchDeveloperMetadataResponse
from openapi_server.models.sheet_properties import SheetProperties
from openapi_server.models.spreadsheet import Spreadsheet
from openapi_server.models.update_values_response import UpdateValuesResponse
from openapi_server.models.value_range import ValueRange
from openapi_server import util


async def sheets_spreadsheets_batch_update(request: web.Request, spreadsheet_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """sheets_spreadsheets_batch_update

    Applies one or more updates to the spreadsheet. Each request is validated before being applied. If any request is not valid then the entire request will fail and nothing will be applied. Some requests have replies to give you some information about how they are applied. The replies will mirror the requests. For example, if you applied 4 updates and the 3rd one had a reply, then the response will have 2 empty replies, the actual reply, and another empty reply, in that order. Due to the collaborative nature of spreadsheets, it is not guaranteed that the spreadsheet will reflect exactly your changes after this completes, however it is guaranteed that the updates in the request will be applied together atomically. Your changes may be altered with respect to collaborator changes. If there are no collaborators, the spreadsheet should reflect your changes.

    :param spreadsheet_id: The spreadsheet to apply the updates to.
    :type spreadsheet_id: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = BatchUpdateSpreadsheetRequest.from_dict(body)
    return web.Response(status=200)


async def sheets_spreadsheets_create(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """sheets_spreadsheets_create

    Creates a spreadsheet, returning the newly created spreadsheet.

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
    :param body: 
    :type body: dict | bytes

    """
    body = Spreadsheet.from_dict(body)
    return web.Response(status=200)


async def sheets_spreadsheets_developer_metadata_get(request: web.Request, spreadsheet_id, metadata_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """sheets_spreadsheets_developer_metadata_get

    Returns the developer metadata with the specified ID. The caller must specify the spreadsheet ID and the developer metadata&#39;s unique metadataId.

    :param spreadsheet_id: The ID of the spreadsheet to retrieve metadata from.
    :type spreadsheet_id: str
    :param metadata_id: The ID of the developer metadata to retrieve.
    :type metadata_id: int
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

    """
    return web.Response(status=200)


async def sheets_spreadsheets_developer_metadata_search(request: web.Request, spreadsheet_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """sheets_spreadsheets_developer_metadata_search

    Returns all developer metadata matching the specified DataFilter. If the provided DataFilter represents a DeveloperMetadataLookup object, this will return all DeveloperMetadata entries selected by it. If the DataFilter represents a location in a spreadsheet, this will return all developer metadata associated with locations intersecting that region.

    :param spreadsheet_id: The ID of the spreadsheet to retrieve metadata from.
    :type spreadsheet_id: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = SearchDeveloperMetadataRequest.from_dict(body)
    return web.Response(status=200)


async def sheets_spreadsheets_get(request: web.Request, spreadsheet_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, include_grid_data=None, ranges=None) -> web.Response:
    """sheets_spreadsheets_get

    Returns the spreadsheet at the given ID. The caller must specify the spreadsheet ID. By default, data within grids is not returned. You can include grid data in one of 2 ways: * Specify a [field mask](https://developers.google.com/sheets/api/guides/field-masks) listing your desired fields using the &#x60;fields&#x60; URL parameter in HTTP * Set the includeGridData URL parameter to true. If a field mask is set, the &#x60;includeGridData&#x60; parameter is ignored For large spreadsheets, as a best practice, retrieve only the specific spreadsheet fields that you want. To retrieve only subsets of spreadsheet data, use the ranges URL parameter. Ranges are specified using [A1 notation](/sheets/api/guides/concepts#cell). You can define a single cell (for example, &#x60;A1&#x60;) or multiple cells (for example, &#x60;A1:D5&#x60;). You can also get cells from other sheets within the same spreadsheet (for example, &#x60;Sheet2!A1:C4&#x60;) or retrieve multiple ranges at once (for example, &#x60;?ranges&#x3D;A1:D5&amp;ranges&#x3D;Sheet2!A1:C4&#x60;). Limiting the range returns only the portions of the spreadsheet that intersect the requested ranges.

    :param spreadsheet_id: The spreadsheet to request.
    :type spreadsheet_id: str
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
    :param include_grid_data: True if grid data should be returned. This parameter is ignored if a field mask was set in the request.
    :type include_grid_data: bool
    :param ranges: The ranges to retrieve from the spreadsheet.
    :type ranges: List[str]

    """
    return web.Response(status=200)


async def sheets_spreadsheets_get_by_data_filter(request: web.Request, spreadsheet_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """sheets_spreadsheets_get_by_data_filter

    Returns the spreadsheet at the given ID. The caller must specify the spreadsheet ID. This method differs from GetSpreadsheet in that it allows selecting which subsets of spreadsheet data to return by specifying a dataFilters parameter. Multiple DataFilters can be specified. Specifying one or more data filters returns the portions of the spreadsheet that intersect ranges matched by any of the filters. By default, data within grids is not returned. You can include grid data one of 2 ways: * Specify a [field mask](https://developers.google.com/sheets/api/guides/field-masks) listing your desired fields using the &#x60;fields&#x60; URL parameter in HTTP * Set the includeGridData parameter to true. If a field mask is set, the &#x60;includeGridData&#x60; parameter is ignored For large spreadsheets, as a best practice, retrieve only the specific spreadsheet fields that you want.

    :param spreadsheet_id: The spreadsheet to request.
    :type spreadsheet_id: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = GetSpreadsheetByDataFilterRequest.from_dict(body)
    return web.Response(status=200)


async def sheets_spreadsheets_sheets_copy_to(request: web.Request, spreadsheet_id, sheet_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """sheets_spreadsheets_sheets_copy_to

    Copies a single sheet from a spreadsheet to another spreadsheet. Returns the properties of the newly created sheet.

    :param spreadsheet_id: The ID of the spreadsheet containing the sheet to copy.
    :type spreadsheet_id: str
    :param sheet_id: The ID of the sheet to copy.
    :type sheet_id: int
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
    :param body: 
    :type body: dict | bytes

    """
    body = CopySheetToAnotherSpreadsheetRequest.from_dict(body)
    return web.Response(status=200)


async def sheets_spreadsheets_values_append(request: web.Request, spreadsheet_id, range, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, include_values_in_response=None, insert_data_option=None, response_date_time_render_option=None, response_value_render_option=None, value_input_option=None, body=None) -> web.Response:
    """sheets_spreadsheets_values_append

    Appends values to a spreadsheet. The input range is used to search for existing data and find a \&quot;table\&quot; within that range. Values will be appended to the next row of the table, starting with the first column of the table. See the [guide](/sheets/api/guides/values#appending_values) and [sample code](/sheets/api/samples/writing#append_values) for specific details of how tables are detected and data is appended. The caller must specify the spreadsheet ID, range, and a valueInputOption. The &#x60;valueInputOption&#x60; only controls how the input data will be added to the sheet (column-wise or row-wise), it does not influence what cell the data starts being written to.

    :param spreadsheet_id: The ID of the spreadsheet to update.
    :type spreadsheet_id: str
    :param range: The [A1 notation](/sheets/api/guides/concepts#cell) of a range to search for a logical table of data. Values are appended after the last row of the table.
    :type range: str
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
    :param include_values_in_response: Determines if the update response should include the values of the cells that were appended. By default, responses do not include the updated values.
    :type include_values_in_response: bool
    :param insert_data_option: How the input data should be inserted.
    :type insert_data_option: str
    :param response_date_time_render_option: Determines how dates, times, and durations in the response should be rendered. This is ignored if response_value_render_option is FORMATTED_VALUE. The default dateTime render option is SERIAL_NUMBER.
    :type response_date_time_render_option: str
    :param response_value_render_option: Determines how values in the response should be rendered. The default render option is FORMATTED_VALUE.
    :type response_value_render_option: str
    :param value_input_option: How the input data should be interpreted.
    :type value_input_option: str
    :param body: 
    :type body: dict | bytes

    """
    body = ValueRange.from_dict(body)
    return web.Response(status=200)


async def sheets_spreadsheets_values_batch_clear(request: web.Request, spreadsheet_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """sheets_spreadsheets_values_batch_clear

    Clears one or more ranges of values from a spreadsheet. The caller must specify the spreadsheet ID and one or more ranges. Only values are cleared -- all other properties of the cell (such as formatting and data validation) are kept.

    :param spreadsheet_id: The ID of the spreadsheet to update.
    :type spreadsheet_id: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = BatchClearValuesRequest.from_dict(body)
    return web.Response(status=200)


async def sheets_spreadsheets_values_batch_clear_by_data_filter(request: web.Request, spreadsheet_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """sheets_spreadsheets_values_batch_clear_by_data_filter

    Clears one or more ranges of values from a spreadsheet. The caller must specify the spreadsheet ID and one or more DataFilters. Ranges matching any of the specified data filters will be cleared. Only values are cleared -- all other properties of the cell (such as formatting, data validation, etc..) are kept.

    :param spreadsheet_id: The ID of the spreadsheet to update.
    :type spreadsheet_id: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = BatchClearValuesByDataFilterRequest.from_dict(body)
    return web.Response(status=200)


async def sheets_spreadsheets_values_batch_get(request: web.Request, spreadsheet_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, date_time_render_option=None, major_dimension=None, ranges=None, value_render_option=None) -> web.Response:
    """sheets_spreadsheets_values_batch_get

    Returns one or more ranges of values from a spreadsheet. The caller must specify the spreadsheet ID and one or more ranges.

    :param spreadsheet_id: The ID of the spreadsheet to retrieve data from.
    :type spreadsheet_id: str
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
    :param date_time_render_option: How dates, times, and durations should be represented in the output. This is ignored if value_render_option is FORMATTED_VALUE. The default dateTime render option is SERIAL_NUMBER.
    :type date_time_render_option: str
    :param major_dimension: The major dimension that results should use. For example, if the spreadsheet data is: &#x60;A1&#x3D;1,B1&#x3D;2,A2&#x3D;3,B2&#x3D;4&#x60;, then requesting &#x60;ranges&#x3D;[\&quot;A1:B2\&quot;],majorDimension&#x3D;ROWS&#x60; returns &#x60;[[1,2],[3,4]]&#x60;, whereas requesting &#x60;ranges&#x3D;[\&quot;A1:B2\&quot;],majorDimension&#x3D;COLUMNS&#x60; returns &#x60;[[1,3],[2,4]]&#x60;.
    :type major_dimension: str
    :param ranges: The [A1 notation or R1C1 notation](/sheets/api/guides/concepts#cell) of the range to retrieve values from.
    :type ranges: List[str]
    :param value_render_option: How values should be represented in the output. The default render option is ValueRenderOption.FORMATTED_VALUE.
    :type value_render_option: str

    """
    return web.Response(status=200)


async def sheets_spreadsheets_values_batch_get_by_data_filter(request: web.Request, spreadsheet_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """sheets_spreadsheets_values_batch_get_by_data_filter

    Returns one or more ranges of values that match the specified data filters. The caller must specify the spreadsheet ID and one or more DataFilters. Ranges that match any of the data filters in the request will be returned.

    :param spreadsheet_id: The ID of the spreadsheet to retrieve data from.
    :type spreadsheet_id: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = BatchGetValuesByDataFilterRequest.from_dict(body)
    return web.Response(status=200)


async def sheets_spreadsheets_values_batch_update(request: web.Request, spreadsheet_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """sheets_spreadsheets_values_batch_update

    Sets values in one or more ranges of a spreadsheet. The caller must specify the spreadsheet ID, a valueInputOption, and one or more ValueRanges.

    :param spreadsheet_id: The ID of the spreadsheet to update.
    :type spreadsheet_id: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = BatchUpdateValuesRequest.from_dict(body)
    return web.Response(status=200)


async def sheets_spreadsheets_values_batch_update_by_data_filter(request: web.Request, spreadsheet_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """sheets_spreadsheets_values_batch_update_by_data_filter

    Sets values in one or more ranges of a spreadsheet. The caller must specify the spreadsheet ID, a valueInputOption, and one or more DataFilterValueRanges.

    :param spreadsheet_id: The ID of the spreadsheet to update.
    :type spreadsheet_id: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = BatchUpdateValuesByDataFilterRequest.from_dict(body)
    return web.Response(status=200)


async def sheets_spreadsheets_values_clear(request: web.Request, spreadsheet_id, range, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """sheets_spreadsheets_values_clear

    Clears values from a spreadsheet. The caller must specify the spreadsheet ID and range. Only values are cleared -- all other properties of the cell (such as formatting, data validation, etc..) are kept.

    :param spreadsheet_id: The ID of the spreadsheet to update.
    :type spreadsheet_id: str
    :param range: The [A1 notation or R1C1 notation](/sheets/api/guides/concepts#cell) of the values to clear.
    :type range: str
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
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def sheets_spreadsheets_values_get(request: web.Request, spreadsheet_id, range, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, date_time_render_option=None, major_dimension=None, value_render_option=None) -> web.Response:
    """sheets_spreadsheets_values_get

    Returns a range of values from a spreadsheet. The caller must specify the spreadsheet ID and a range.

    :param spreadsheet_id: The ID of the spreadsheet to retrieve data from.
    :type spreadsheet_id: str
    :param range: The [A1 notation or R1C1 notation](/sheets/api/guides/concepts#cell) of the range to retrieve values from.
    :type range: str
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
    :param date_time_render_option: How dates, times, and durations should be represented in the output. This is ignored if value_render_option is FORMATTED_VALUE. The default dateTime render option is SERIAL_NUMBER.
    :type date_time_render_option: str
    :param major_dimension: The major dimension that results should use. For example, if the spreadsheet data in Sheet1 is: &#x60;A1&#x3D;1,B1&#x3D;2,A2&#x3D;3,B2&#x3D;4&#x60;, then requesting &#x60;range&#x3D;Sheet1!A1:B2?majorDimension&#x3D;ROWS&#x60; returns &#x60;[[1,2],[3,4]]&#x60;, whereas requesting &#x60;range&#x3D;Sheet1!A1:B2?majorDimension&#x3D;COLUMNS&#x60; returns &#x60;[[1,3],[2,4]]&#x60;.
    :type major_dimension: str
    :param value_render_option: How values should be represented in the output. The default render option is FORMATTED_VALUE.
    :type value_render_option: str

    """
    return web.Response(status=200)


async def sheets_spreadsheets_values_update(request: web.Request, spreadsheet_id, range, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, include_values_in_response=None, response_date_time_render_option=None, response_value_render_option=None, value_input_option=None, body=None) -> web.Response:
    """sheets_spreadsheets_values_update

    Sets values in a range of a spreadsheet. The caller must specify the spreadsheet ID, range, and a valueInputOption.

    :param spreadsheet_id: The ID of the spreadsheet to update.
    :type spreadsheet_id: str
    :param range: The [A1 notation](/sheets/api/guides/concepts#cell) of the values to update.
    :type range: str
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
    :param include_values_in_response: Determines if the update response should include the values of the cells that were updated. By default, responses do not include the updated values. If the range to write was larger than the range actually written, the response includes all values in the requested range (excluding trailing empty rows and columns).
    :type include_values_in_response: bool
    :param response_date_time_render_option: Determines how dates, times, and durations in the response should be rendered. This is ignored if response_value_render_option is FORMATTED_VALUE. The default dateTime render option is SERIAL_NUMBER.
    :type response_date_time_render_option: str
    :param response_value_render_option: Determines how values in the response should be rendered. The default render option is FORMATTED_VALUE.
    :type response_value_render_option: str
    :param value_input_option: How the input data should be interpreted.
    :type value_input_option: str
    :param body: 
    :type body: dict | bytes

    """
    body = ValueRange.from_dict(body)
    return web.Response(status=200)
