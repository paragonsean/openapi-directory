from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_chrome_management_v1_count_chrome_app_requests_response import GoogleChromeManagementV1CountChromeAppRequestsResponse
from openapi_server.models.google_chrome_management_v1_count_chrome_browsers_needing_attention_response import GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponse
from openapi_server.models.google_chrome_management_v1_count_chrome_devices_reaching_auto_expiration_date_response import GoogleChromeManagementV1CountChromeDevicesReachingAutoExpirationDateResponse
from openapi_server.models.google_chrome_management_v1_count_chrome_devices_that_need_attention_response import GoogleChromeManagementV1CountChromeDevicesThatNeedAttentionResponse
from openapi_server.models.google_chrome_management_v1_count_chrome_hardware_fleet_devices_response import GoogleChromeManagementV1CountChromeHardwareFleetDevicesResponse
from openapi_server.models.google_chrome_management_v1_count_chrome_versions_response import GoogleChromeManagementV1CountChromeVersionsResponse
from openapi_server.models.google_chrome_management_v1_count_installed_apps_response import GoogleChromeManagementV1CountInstalledAppsResponse
from openapi_server.models.google_chrome_management_v1_count_print_jobs_by_printer_response import GoogleChromeManagementV1CountPrintJobsByPrinterResponse
from openapi_server.models.google_chrome_management_v1_count_print_jobs_by_user_response import GoogleChromeManagementV1CountPrintJobsByUserResponse
from openapi_server.models.google_chrome_management_v1_enumerate_print_jobs_response import GoogleChromeManagementV1EnumeratePrintJobsResponse
from openapi_server.models.google_chrome_management_v1_find_installed_app_devices_response import GoogleChromeManagementV1FindInstalledAppDevicesResponse
from openapi_server.models.google_chrome_management_v1_list_telemetry_devices_response import GoogleChromeManagementV1ListTelemetryDevicesResponse
from openapi_server.models.google_chrome_management_v1_list_telemetry_events_response import GoogleChromeManagementV1ListTelemetryEventsResponse
from openapi_server.models.google_chrome_management_v1_list_telemetry_notification_configs_response import GoogleChromeManagementV1ListTelemetryNotificationConfigsResponse
from openapi_server.models.google_chrome_management_v1_list_telemetry_users_response import GoogleChromeManagementV1ListTelemetryUsersResponse
from openapi_server.models.google_chrome_management_v1_telemetry_notification_config import GoogleChromeManagementV1TelemetryNotificationConfig
from openapi_server.models.google_chrome_management_v1_telemetry_user import GoogleChromeManagementV1TelemetryUser
from openapi_server import util


async def chromemanagement_customers_apps_count_chrome_app_requests(request: web.Request, customer, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, order_by=None, org_unit_id=None, page_size=None, page_token=None) -> web.Response:
    """chromemanagement_customers_apps_count_chrome_app_requests

    Generate summary of app installation requests.

    :param customer: Required. Customer id or \&quot;my_customer\&quot; to use the customer associated to the account making the request.
    :type customer: str
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
    :param order_by: Field used to order results. Supported fields: * request_count * latest_request_time
    :type order_by: str
    :param org_unit_id: The ID of the organizational unit.
    :type org_unit_id: str
    :param page_size: Maximum number of results to return. Maximum and default are 50, anything above will be coerced to 50.
    :type page_size: int
    :param page_token: Token to specify the page of the request to be returned.
    :type page_token: str

    """
    return web.Response(status=200)


async def chromemanagement_customers_reports_count_chrome_browsers_needing_attention(request: web.Request, customer, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, org_unit_id=None) -> web.Response:
    """chromemanagement_customers_reports_count_chrome_browsers_needing_attention

    Count of Chrome Browsers that have been recently enrolled, have new policy to be synced, or have no recent activity.

    :param customer: Required. The customer ID or \&quot;my_customer\&quot; prefixed with \&quot;customers/\&quot;.
    :type customer: str
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
    :param org_unit_id: Optional. The ID of the organizational unit. If omitted, all data will be returned.
    :type org_unit_id: str

    """
    return web.Response(status=200)


async def chromemanagement_customers_reports_count_chrome_devices_reaching_auto_expiration_date(request: web.Request, customer, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, max_aue_date=None, min_aue_date=None, org_unit_id=None) -> web.Response:
    """chromemanagement_customers_reports_count_chrome_devices_reaching_auto_expiration_date

    Generate report of the number of devices expiring in each month of the selected time frame. Devices are grouped by auto update expiration date and model. Further information can be found [here](https://support.google.com/chrome/a/answer/10564947).

    :param customer: Required. The customer ID or \&quot;my_customer\&quot; prefixed with \&quot;customers/\&quot;.
    :type customer: str
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
    :param max_aue_date: Optional. Maximum expiration date in format yyyy-mm-dd in UTC timezone. If included returns all devices that have already expired and devices with auto expiration date equal to or earlier than the maximum date.
    :type max_aue_date: str
    :param min_aue_date: Optional. Maximum expiration date in format yyyy-mm-dd in UTC timezone. If included returns all devices that have already expired and devices with auto expiration date equal to or later than the minimum date.
    :type min_aue_date: str
    :param org_unit_id: Optional. The organizational unit ID, if omitted, will return data for all organizational units.
    :type org_unit_id: str

    """
    return web.Response(status=200)


async def chromemanagement_customers_reports_count_chrome_devices_that_need_attention(request: web.Request, customer, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, org_unit_id=None, read_mask=None) -> web.Response:
    """chromemanagement_customers_reports_count_chrome_devices_that_need_attention

    Counts of ChromeOS devices that have not synced policies or have lacked user activity in the past 28 days, are out of date, or are not complaint. Further information can be found here https://support.google.com/chrome/a/answer/10564947

    :param customer: Required. The customer ID or \&quot;my_customer\&quot; prefixed with \&quot;customers/\&quot;.
    :type customer: str
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
    :param org_unit_id: Optional. The ID of the organizational unit. If omitted, all data will be returned.
    :type org_unit_id: str
    :param read_mask: Required. Mask of the fields that should be populated in the returned report.
    :type read_mask: str

    """
    return web.Response(status=200)


async def chromemanagement_customers_reports_count_chrome_hardware_fleet_devices(request: web.Request, customer, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, org_unit_id=None, read_mask=None) -> web.Response:
    """chromemanagement_customers_reports_count_chrome_hardware_fleet_devices

    Counts of devices with a specific hardware specification from the requested hardware type (for example model name, processor type). Further information can be found here https://support.google.com/chrome/a/answer/10564947

    :param customer: Required. The customer ID or \&quot;my_customer\&quot;.
    :type customer: str
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
    :param org_unit_id: Optional. The ID of the organizational unit. If omitted, all data will be returned.
    :type org_unit_id: str
    :param read_mask: Required. Mask of the fields that should be populated in the returned report.
    :type read_mask: str

    """
    return web.Response(status=200)


async def chromemanagement_customers_reports_count_chrome_versions(request: web.Request, customer, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, org_unit_id=None, page_size=None, page_token=None) -> web.Response:
    """chromemanagement_customers_reports_count_chrome_versions

    Generate report of installed Chrome versions.

    :param customer: Required. Customer id or \&quot;my_customer\&quot; to use the customer associated to the account making the request.
    :type customer: str
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
    :param filter: Query string to filter results, AND-separated fields in EBNF syntax. Note: OR operations are not supported in this filter. Supported filter fields: * last_active_date
    :type filter: str
    :param org_unit_id: The ID of the organizational unit.
    :type org_unit_id: str
    :param page_size: Maximum number of results to return. Maximum and default are 100.
    :type page_size: int
    :param page_token: Token to specify the page of the request to be returned.
    :type page_token: str

    """
    return web.Response(status=200)


async def chromemanagement_customers_reports_count_installed_apps(request: web.Request, customer, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, org_unit_id=None, page_size=None, page_token=None) -> web.Response:
    """chromemanagement_customers_reports_count_installed_apps

    Generate report of app installations.

    :param customer: Required. Customer id or \&quot;my_customer\&quot; to use the customer associated to the account making the request.
    :type customer: str
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
    :param filter: Query string to filter results, AND-separated fields in EBNF syntax. Note: OR operations are not supported in this filter. Supported filter fields: * app_name * app_type * install_type * number_of_permissions * total_install_count * latest_profile_active_date * permission_name * app_id
    :type filter: str
    :param order_by: Field used to order results. Supported order by fields: * app_name * app_type * install_type * number_of_permissions * total_install_count * app_id
    :type order_by: str
    :param org_unit_id: The ID of the organizational unit.
    :type org_unit_id: str
    :param page_size: Maximum number of results to return. Maximum and default are 100.
    :type page_size: int
    :param page_token: Token to specify the page of the request to be returned.
    :type page_token: str

    """
    return web.Response(status=200)


async def chromemanagement_customers_reports_count_print_jobs_by_printer(request: web.Request, customer, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None, printer_org_unit_id=None) -> web.Response:
    """chromemanagement_customers_reports_count_print_jobs_by_printer

    Get a summary of printing done by each printer.

    :param customer: Required. Customer ID prefixed with \&quot;customers/\&quot; or \&quot;customers/my_customer\&quot; to use the customer associated to the account making the request.
    :type customer: str
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
    :param filter: Query string to filter results, AND-separated fields in EBNF syntax. Note: OR operations are not supported in this filter. Note: Only &gt;&#x3D; and &lt;&#x3D; comparators are supported in this filter. Supported filter fields: * complete_time
    :type filter: str
    :param order_by: Field used to order results. If omitted, results will be ordered in ascending order of the &#39;printer&#39; field. Supported order_by fields: * printer * job_count * device_count * user_count
    :type order_by: str
    :param page_size: Maximum number of results to return. Maximum and default are 100.
    :type page_size: int
    :param page_token: Token to specify the page of the response to be returned.
    :type page_token: str
    :param printer_org_unit_id: The ID of the organizational unit for printers. If specified, only data for printers from the specified organizational unit will be returned. If omitted, data for printers from all organizational units will be returned.
    :type printer_org_unit_id: str

    """
    return web.Response(status=200)


async def chromemanagement_customers_reports_count_print_jobs_by_user(request: web.Request, customer, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None, printer_org_unit_id=None) -> web.Response:
    """chromemanagement_customers_reports_count_print_jobs_by_user

    Get a summary of printing done by each user.

    :param customer: Required. Customer ID prefixed with \&quot;customers/\&quot; or \&quot;customers/my_customer\&quot; to use the customer associated to the account making the request.
    :type customer: str
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
    :param filter: Query string to filter results, AND-separated fields in EBNF syntax. Note: OR operations are not supported in this filter. Note: Only &gt;&#x3D; and &lt;&#x3D; comparators are supported in this filter. Supported filter fields: * complete_time
    :type filter: str
    :param order_by: Field used to order results. If omitted, results will be ordered in ascending order of the &#39;user_email&#39; field. Supported order_by fields: * user_email * job_count * printer_count * device_count
    :type order_by: str
    :param page_size: Maximum number of results to return. Maximum and default are 100.
    :type page_size: int
    :param page_token: Token to specify the page of the response to be returned.
    :type page_token: str
    :param printer_org_unit_id: The ID of the organizational unit for printers. If specified, only print jobs initiated with printers from the specified organizational unit will be counted. If omitted, all print jobs will be counted.
    :type printer_org_unit_id: str

    """
    return web.Response(status=200)


async def chromemanagement_customers_reports_enumerate_print_jobs(request: web.Request, customer, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None, printer_org_unit_id=None) -> web.Response:
    """chromemanagement_customers_reports_enumerate_print_jobs

    Get a list of print jobs.

    :param customer: Required. Customer ID prefixed with \&quot;customers/\&quot; or \&quot;customers/my_customer\&quot; to use the customer associated to the account making the request.
    :type customer: str
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
    :param filter: Query string to filter results, AND-separated fields in EBNF syntax. Note: OR operations are not supported in this filter. Note: Only &gt;&#x3D; and &lt;&#x3D; comparators are supported for &#x60;complete_time&#x60;. Note: Only &#x3D; comparator supported for &#x60;user_id&#x60; and &#x60;printer_id&#x60;. Supported filter fields: * complete_time * printer_id * user_id
    :type filter: str
    :param order_by: Field used to order results. If not specified, results will be ordered in descending order of the &#x60;complete_time&#x60; field. Supported order by fields: * title * state * create_time * complete_time * document_page_count * color_mode * duplex_mode * printer * user_email
    :type order_by: str
    :param page_size: The number of print jobs in the page from 0 to 100 inclusive, if page_size is not specified or zero, the size will be 50.
    :type page_size: int
    :param page_token: A page token received from a previous &#x60;EnumeratePrintJobs&#x60; call. Provide this to retrieve the subsequent page. If omitted, the first page of results will be returned. When paginating, all other parameters provided to &#x60;EnumeratePrintJobs&#x60; must match the call that provided the page token.
    :type page_token: str
    :param printer_org_unit_id: The ID of the organizational unit for printers. If specified, only print jobs submitted to printers from the specified organizational unit will be returned.
    :type printer_org_unit_id: str

    """
    return web.Response(status=200)


async def chromemanagement_customers_reports_find_installed_app_devices(request: web.Request, customer, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, app_id=None, app_type=None, filter=None, order_by=None, org_unit_id=None, page_size=None, page_token=None) -> web.Response:
    """chromemanagement_customers_reports_find_installed_app_devices

    Generate report of managed Chrome browser devices that have a specified app installed.

    :param customer: Required. Customer id or \&quot;my_customer\&quot; to use the customer associated to the account making the request.
    :type customer: str
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
    :param app_id: Unique identifier of the app. For Chrome apps and extensions, the 32-character id (e.g. ehoadneljpdggcbbknedodolkkjodefl). For Android apps, the package name (e.g. com.evernote).
    :type app_id: str
    :param app_type: Type of the app.
    :type app_type: str
    :param filter: Query string to filter results, AND-separated fields in EBNF syntax. Note: OR operations are not supported in this filter. Supported filter fields: * last_active_date
    :type filter: str
    :param order_by: Field used to order results. Supported order by fields: * machine * device_id
    :type order_by: str
    :param org_unit_id: The ID of the organizational unit.
    :type org_unit_id: str
    :param page_size: Maximum number of results to return. Maximum and default are 100.
    :type page_size: int
    :param page_token: Token to specify the page of the request to be returned.
    :type page_token: str

    """
    return web.Response(status=200)


async def chromemanagement_customers_telemetry_devices_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None, read_mask=None) -> web.Response:
    """chromemanagement_customers_telemetry_devices_list

    List all telemetry devices.

    :param parent: Required. Customer id or \&quot;my_customer\&quot; to use the customer associated to the account making the request.
    :type parent: str
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
    :param filter: Optional. Only include resources that match the filter. Supported filter fields: - org_unit_id - serial_number - device_id - reports_timestamp The \&quot;reports_timestamp\&quot; filter accepts either the Unix Epoch milliseconds format or the RFC3339 UTC \&quot;Zulu\&quot; format with nanosecond resolution and up to nine fractional digits. Both formats should be surrounded by simple double quotes. Examples: \&quot;2014-10-02T15:01:23Z\&quot;, \&quot;2014-10-02T15:01:23.045123456Z\&quot;, \&quot;1679283943823\&quot;.
    :type filter: str
    :param page_size: Maximum number of results to return. Default value is 100. Maximum value is 1000.
    :type page_size: int
    :param page_token: Token to specify next page in the list.
    :type page_token: str
    :param read_mask: Required. Read mask to specify which fields to return.
    :type read_mask: str

    """
    return web.Response(status=200)


async def chromemanagement_customers_telemetry_events_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None, read_mask=None) -> web.Response:
    """chromemanagement_customers_telemetry_events_list

    List telemetry events.

    :param parent: Required. Customer id or \&quot;my_customer\&quot; to use the customer associated to the account making the request.
    :type parent: str
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
    :param filter: Optional. Only include resources that match the filter. Although this parameter is currently optional, this parameter will be required- please specify at least 1 event type. Supported filter fields: - device_id - user_id - device_org_unit_id - user_org_unit_id - timestamp - event_type The \&quot;timestamp\&quot; filter accepts either the Unix Epoch milliseconds format or the RFC3339 UTC \&quot;Zulu\&quot; format with nanosecond resolution and up to nine fractional digits. Both formats should be surrounded by simple double quotes. Examples: \&quot;2014-10-02T15:01:23Z\&quot;, \&quot;2014-10-02T15:01:23.045123456Z\&quot;, \&quot;1679283943823\&quot;.
    :type filter: str
    :param page_size: Optional. Maximum number of results to return. Default value is 100. Maximum value is 1000.
    :type page_size: int
    :param page_token: Optional. Token to specify next page in the list.
    :type page_token: str
    :param read_mask: Required. Read mask to specify which fields to return. Although currently required, this field will become optional, while the filter parameter with an event type will be come required.
    :type read_mask: str

    """
    return web.Response(status=200)


async def chromemanagement_customers_telemetry_notification_configs_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """chromemanagement_customers_telemetry_notification_configs_create

    Create a telemetry notification config.

    :param parent: Required. The parent resource where this notification config will be created. Format: &#x60;customers/{customer}&#x60;
    :type parent: str
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
    body = GoogleChromeManagementV1TelemetryNotificationConfig.from_dict(body)
    return web.Response(status=200)


async def chromemanagement_customers_telemetry_notification_configs_delete(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """chromemanagement_customers_telemetry_notification_configs_delete

    Delete a telemetry notification config.

    :param name: Required. The name of the notification config to delete. Format: &#x60;customers/{customer}/telemetry/notificationConfigs/{notification_config}&#x60;
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

    """
    return web.Response(status=200)


async def chromemanagement_customers_telemetry_notification_configs_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """chromemanagement_customers_telemetry_notification_configs_list

    List all telemetry notification configs.

    :param parent: Required. The parent which owns the notification configs.
    :type parent: str
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
    :param page_size: The maximum number of notification configs to return. The service may return fewer than this value. If unspecified, at most 100 notification configs will be returned. The maximum value is 100; values above 100 will be coerced to 100.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListTelemetryNotificationConfigs&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListTelemetryNotificationConfigs&#x60; must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def chromemanagement_customers_telemetry_users_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, read_mask=None) -> web.Response:
    """chromemanagement_customers_telemetry_users_get

    Get telemetry user.

    :param name: Required. Name of the &#x60;TelemetryUser&#x60; to return.
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
    :param read_mask: Read mask to specify which fields to return.
    :type read_mask: str

    """
    return web.Response(status=200)


async def chromemanagement_customers_telemetry_users_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None, read_mask=None) -> web.Response:
    """chromemanagement_customers_telemetry_users_list

    List all telemetry users.

    :param parent: Required. Customer id or \&quot;my_customer\&quot; to use the customer associated to the account making the request.
    :type parent: str
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
    :param filter: Only include resources that match the filter. Supported filter fields: - user_id - user_org_unit_id 
    :type filter: str
    :param page_size: Maximum number of results to return. Default value is 100. Maximum value is 1000.
    :type page_size: int
    :param page_token: Token to specify next page in the list.
    :type page_token: str
    :param read_mask: Read mask to specify which fields to return.
    :type read_mask: str

    """
    return web.Response(status=200)
