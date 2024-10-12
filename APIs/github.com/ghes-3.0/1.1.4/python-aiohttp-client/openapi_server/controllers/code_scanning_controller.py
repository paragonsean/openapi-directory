from typing import List, Dict
from aiohttp import web

from openapi_server.models.activity_list_public_events503_response import ActivityListPublicEvents503Response
from openapi_server.models.basic_error import BasicError
from openapi_server.models.code_scanning_alert import CodeScanningAlert
from openapi_server.models.code_scanning_alert_items import CodeScanningAlertItems
from openapi_server.models.code_scanning_alert_state import CodeScanningAlertState
from openapi_server.models.code_scanning_analysis import CodeScanningAnalysis
from openapi_server.models.code_scanning_sarifs_receipt import CodeScanningSarifsReceipt
from openapi_server.models.code_scanning_update_alert_request import CodeScanningUpdateAlertRequest
from openapi_server.models.code_scanning_upload_sarif_request import CodeScanningUploadSarifRequest
from openapi_server import util


async def code_scanning_get_alert(request: web.Request, owner, repo, alert_number) -> web.Response:
    """Get a code scanning alert

    Gets a single code scanning alert. You must use an access token with the &#x60;security_events&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;security_events&#x60; read permission to use this endpoint.  **Deprecation notice**: The instances field is deprecated and will, in future, not be included in the response for this endpoint. The example response reflects this change. The same information can now be retrieved via a GET request to the URL specified by &#x60;instances_url&#x60;.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param alert_number: The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the &#x60;number&#x60; field in the response from the &#x60;GET /repos/{owner}/{repo}/code-scanning/alerts&#x60; operation.
    :type alert_number: int

    """
    return web.Response(status=200)


async def code_scanning_list_alerts_for_repo(request: web.Request, owner, repo, tool_name=None, tool_guid=None, page=None, per_page=None, ref=None, state=None) -> web.Response:
    """List code scanning alerts for a repository

    Lists all open code scanning alerts for the default branch (usually &#x60;main&#x60; or &#x60;master&#x60;). You must use an access token with the &#x60;security_events&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;security_events&#x60; read permission to use this endpoint.  The response includes a &#x60;most_recent_instance&#x60; object. This provides details of the most recent instance of this alert for the default branch or for the specified Git reference (if you used &#x60;ref&#x60; in the request).

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param tool_name: The name of a code scanning tool. Only results by this tool will be listed. You can specify the tool by using either &#x60;tool_name&#x60; or &#x60;tool_guid&#x60;, but not both.
    :type tool_name: str
    :param tool_guid: The GUID of a code scanning tool. Only results by this tool will be listed. Note that some code scanning tools may not include a GUID in their analysis data. You can specify the tool by using either &#x60;tool_guid&#x60; or &#x60;tool_name&#x60;, but not both.
    :type tool_guid: str
    :param page: Page number of the results to fetch.
    :type page: int
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param ref: The Git reference for the results you want to list. The &#x60;ref&#x60; for a branch can be formatted either as &#x60;refs/heads/&lt;branch name&gt;&#x60; or simply &#x60;&lt;branch name&gt;&#x60;. To reference a pull request use &#x60;refs/pull/&lt;number&gt;/merge&#x60;.
    :type ref: str
    :param state: Set to &#x60;open&#x60;, &#x60;fixed&#x60;, or &#x60;dismissed&#x60; to list code scanning alerts in a specific state.
    :type state: dict | bytes

    """
    state = .from_dict(state)
    return web.Response(status=200)


async def code_scanning_list_recent_analyses(request: web.Request, owner, repo, tool_name=None, tool_guid=None, page=None, per_page=None, ref=None, sarif_id=None) -> web.Response:
    """List code scanning analyses for a repository

    Lists the details of all code scanning analyses for a repository, starting with the most recent. The response is paginated and you can use the &#x60;page&#x60; and &#x60;per_page&#x60; parameters to list the analyses you&#39;re interested in. By default 30 analyses are listed per page.  The &#x60;rules_count&#x60; field in the response give the number of rules that were run in the analysis. For very old analyses this data is not available, and &#x60;0&#x60; is returned in this field.  You must use an access token with the &#x60;security_events&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;security_events&#x60; read permission to use this endpoint.  **Deprecation notice**: The &#x60;tool_name&#x60; field is deprecated and will, in future, not be included in the response for this endpoint. The example response reflects this change. The tool name can now be found inside the &#x60;tool&#x60; field.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param tool_name: The name of a code scanning tool. Only results by this tool will be listed. You can specify the tool by using either &#x60;tool_name&#x60; or &#x60;tool_guid&#x60;, but not both.
    :type tool_name: str
    :param tool_guid: The GUID of a code scanning tool. Only results by this tool will be listed. Note that some code scanning tools may not include a GUID in their analysis data. You can specify the tool by using either &#x60;tool_guid&#x60; or &#x60;tool_name&#x60;, but not both.
    :type tool_guid: str
    :param page: Page number of the results to fetch.
    :type page: int
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param ref: The Git reference for the analyses you want to list. The &#x60;ref&#x60; for a branch can be formatted either as &#x60;refs/heads/&lt;branch name&gt;&#x60; or simply &#x60;&lt;branch name&gt;&#x60;. To reference a pull request use &#x60;refs/pull/&lt;number&gt;/merge&#x60;.
    :type ref: str
    :param sarif_id: Filter analyses belonging to the same SARIF upload.
    :type sarif_id: str

    """
    return web.Response(status=200)


async def code_scanning_update_alert(request: web.Request, owner, repo, alert_number, body) -> web.Response:
    """Update a code scanning alert

    Updates the status of a single code scanning alert. You must use an access token with the &#x60;security_events&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;security_events&#x60; write permission to use this endpoint.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param alert_number: The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the &#x60;number&#x60; field in the response from the &#x60;GET /repos/{owner}/{repo}/code-scanning/alerts&#x60; operation.
    :type alert_number: int
    :param body: 
    :type body: dict | bytes

    """
    body = CodeScanningUpdateAlertRequest.from_dict(body)
    return web.Response(status=200)


async def code_scanning_upload_sarif(request: web.Request, owner, repo, body) -> web.Response:
    """Upload an analysis as SARIF data

    Uploads SARIF data containing the results of a code scanning analysis to make the results available in a repository. You must use an access token with the &#x60;security_events&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;security_events&#x60; write permission to use this endpoint.  There are two places where you can upload code scanning results.  - If you upload to a pull request, for example &#x60;--ref refs/pull/42/merge&#x60; or &#x60;--ref refs/pull/42/head&#x60;, then the results appear as alerts in a pull request check. For more information, see \&quot;[Triaging code scanning alerts in pull requests](/code-security/secure-coding/triaging-code-scanning-alerts-in-pull-requests).\&quot;  - If you upload to a branch, for example &#x60;--ref refs/heads/my-branch&#x60;, then the results appear in the **Security** tab for your repository. For more information, see \&quot;[Managing code scanning alerts for your repository](/code-security/secure-coding/managing-code-scanning-alerts-for-your-repository#viewing-the-alerts-for-a-repository).\&quot;  You must compress the SARIF-formatted analysis data that you want to upload, using &#x60;gzip&#x60;, and then encode it as a Base64 format string. For example:  &#x60;&#x60;&#x60; gzip -c analysis-data.sarif | base64 -w0 &#x60;&#x60;&#x60;  SARIF upload supports a maximum of 1000 results per analysis run. Any results over this limit are ignored. Typically, but not necessarily, a SARIF file contains a single run of a single tool. If a code scanning tool generates too many results, you should update the analysis configuration to run only the most important rules or queries.  The &#x60;202 Accepted&#x60;, response includes an &#x60;id&#x60; value. You can use this ID to check the status of the upload by using this for the &#x60;/sarifs/{sarif_id}&#x60; endpoint. For more information, see \&quot;[Get information about a SARIF upload](/rest/reference/code-scanning#get-information-about-a-sarif-upload).\&quot;

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = CodeScanningUploadSarifRequest.from_dict(body)
    return web.Response(status=200)
