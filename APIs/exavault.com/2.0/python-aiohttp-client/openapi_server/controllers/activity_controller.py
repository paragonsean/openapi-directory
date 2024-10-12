from typing import List, Dict
from aiohttp import web

from openapi_server.models.session_activity_response import SessionActivityResponse
from openapi_server.models.webhook_activity_response import WebhookActivityResponse
from openapi_server import util


async def get_session_logs(request: web.Request, ev_api_key, ev_access_token, start_date=None, end_date=None, ip_address=None, username=None, path=None, type=None, offset=None, limit=None, sort=None) -> web.Response:
    """Get activity logs

    Returns the detailed activity logs for your account. Optional query paramaters will filter the returned results based on a number of options including usernames, activity types, or date ranges.   **NOTE:** Total Results will always return as 0 to avoid quering data you&#39;re not using and stay as performant as possible.     **Operation Types** Session activity is logged with an operation type that is different from what is visible through the [activity log interface in the web file manager](/docs/account/10-activity-logs/00-activity-logs). Consult the table below to compare the two:  | File Manager Value | API Value | Notes | |-----|----|---| | Connect | PASS | | | Disconnect | EXIT | | | Upload | STOR | | | Download | RETR | | | Delete | DELE | | | Create Folder | MKD | | | Rename | RNTO | | | Move | MOVE | | | Copy | COPY | | | Compress | COMPR | | | Extract | EXTRACT | | | Shared Folders | SHARE | | | Send Files | SEND | | | Receive Files | RECV | | | _N/A_ | EDIT\\_SEND | Update send. Not shown in file manager | | Update Share | EDIT\\_SHARE| |  | Update Receive | EDIT\\_RECV | | | Delete Send | DELE\\_SEND | | | Delete Receive | DELE\\_RECV | | | Delete Share | DELE\\_SHARE | | | Create Notification | NOTIFY | | | Update Notification | EDIT\\_NTFY| | | Delete Notification | DELE\\_NTFY | | | Create User | USER | | | Update User | EDIT\\_USER | | | Delete User | DELE\\_USER | | | _N/A_ | DFA | Create direct link. Not shown in file manager | | _N/A_ | EDIT\\_DFA | Update direct link options. Not shown in file manager | | _N/A_ | DELE\\_DFA | Deactivate direct link. Not shown in file manager| 

    :param ev_api_key: API Key
    :type ev_api_key: str
    :param ev_access_token: Access Token
    :type ev_access_token: str
    :param start_date: Start date of the filter data range
    :type start_date: str
    :param end_date: End date of the filter data range
    :type end_date: str
    :param ip_address: Used to filter session logs by ip address.
    :type ip_address: str
    :param username: Username used for filtering a list
    :type username: str
    :param path: Path used to filter records
    :type path: str
    :param type: Filter session logs for operation type (see table above for acceptable values)
    :type type: str
    :param offset: Offset of the records list
    :type offset: int
    :param limit: Limit of the records list
    :type limit: int
    :param sort: Comma separated list sort params
    :type sort: str

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)


async def get_webhook_logs(request: web.Request, ev_api_key, ev_access_token, start_date=None, end_date=None, endpoint_url=None, event=None, status_code=None, _resource_path=None, username=None, offset=None, limit=None, sort=None) -> web.Response:
    """Get webhook logs

    Returns the webhook logs for your account. Use the available query parameters to filter the listing of activity that is returned.  **NOTE:** Total Results will always return as 0 to avoid querying data you&#39;re not using and stay as performant as possible.   **Event Types**  Webhooks are triggered by enabled event types for your account, which are configured on the [developer settings page](/docs/account/09-settings/06-developer-settings). Not all event types may be allowed for your account type. These are the valid options for event types:  - resources.upload - resources.download - resources.delete - resources.createFolder - resources.rename - resources.move - resources.copy - resources.compress - resources.extract - shares.formSubmit 

    :param ev_api_key: API Key
    :type ev_api_key: str
    :param ev_access_token: Access Token
    :type ev_access_token: str
    :param start_date: Earliest date of entries to include in list
    :type start_date: str
    :param end_date: Latest date of entries to include in list
    :type end_date: str
    :param endpoint_url: Webhook listener endpoint
    :type endpoint_url: str
    :param event: Type of activity that triggered the webhook attempt
    :type event: str
    :param status_code: Response code from the webhook endpoint
    :type status_code: int
    :param _resource_path: Path of the resource that triggered the webhook attempt
    :type _resource_path: str
    :param username: Filter by triggering username.
    :type username: str
    :param offset: Records to skip before returning results.
    :type offset: int
    :param limit: Limit of the records list
    :type limit: int
    :param sort: Comma separated list sort params
    :type sort: str

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)
