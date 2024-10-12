from typing import List, Dict
from aiohttp import web

from openapi_server.models.activity_list_public_events503_response import ActivityListPublicEvents503Response
from openapi_server.models.secret_scanning_alert import SecretScanningAlert
from openapi_server.models.secret_scanning_update_alert_request import SecretScanningUpdateAlertRequest
from openapi_server import util


async def secret_scanning_get_alert(request: web.Request, owner, repo, alert_number) -> web.Response:
    """Get a secret scanning alert

    Gets a single secret scanning alert detected in a private repository. To use this endpoint, you must be an administrator for the repository or organization, and you must use an access token with the &#x60;repo&#x60; scope or &#x60;security_events&#x60; scope.  GitHub Apps must have the &#x60;secret_scanning_alerts&#x60; read permission to use this endpoint.

    :param owner: The account owner of the repository. The name is not case sensitive.
    :type owner: str
    :param repo: The name of the repository. The name is not case sensitive.
    :type repo: str
    :param alert_number: The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the &#x60;number&#x60; field in the response from the &#x60;GET /repos/{owner}/{repo}/code-scanning/alerts&#x60; operation.
    :type alert_number: int

    """
    return web.Response(status=200)


async def secret_scanning_list_alerts_for_repo(request: web.Request, owner, repo, state=None, secret_type=None, resolution=None, page=None, per_page=None) -> web.Response:
    """List secret scanning alerts for a repository

    Lists secret scanning alerts for a private repository, from newest to oldest. To use this endpoint, you must be an administrator for the repository or organization, and you must use an access token with the &#x60;repo&#x60; scope or &#x60;security_events&#x60; scope.  GitHub Apps must have the &#x60;secret_scanning_alerts&#x60; read permission to use this endpoint.

    :param owner: The account owner of the repository. The name is not case sensitive.
    :type owner: str
    :param repo: The name of the repository. The name is not case sensitive.
    :type repo: str
    :param state: Set to &#x60;open&#x60; or &#x60;resolved&#x60; to only list secret scanning alerts in a specific state.
    :type state: str
    :param secret_type: A comma-separated list of secret types to return. By default all secret types are returned. See \&quot;[Secret scanning patterns](https://docs.github.com/enterprise-server@3.2/code-security/secret-scanning/secret-scanning-patterns#supported-secrets-for-advanced-security)\&quot; for a complete list of secret types.
    :type secret_type: str
    :param resolution: A comma-separated list of resolutions. Only secret scanning alerts with one of these resolutions are listed. Valid resolutions are &#x60;false_positive&#x60;, &#x60;wont_fix&#x60;, &#x60;revoked&#x60;, &#x60;pattern_edited&#x60;, &#x60;pattern_deleted&#x60; or &#x60;used_in_tests&#x60;.
    :type resolution: str
    :param page: Page number of the results to fetch.
    :type page: int
    :param per_page: The number of results per page (max 100).
    :type per_page: int

    """
    return web.Response(status=200)


async def secret_scanning_update_alert(request: web.Request, owner, repo, alert_number, body) -> web.Response:
    """Update a secret scanning alert

    Updates the status of a secret scanning alert in a private repository. To use this endpoint, you must be an administrator for the repository or organization, and you must use an access token with the &#x60;repo&#x60; scope or &#x60;security_events&#x60; scope.  GitHub Apps must have the &#x60;secret_scanning_alerts&#x60; write permission to use this endpoint.

    :param owner: The account owner of the repository. The name is not case sensitive.
    :type owner: str
    :param repo: The name of the repository. The name is not case sensitive.
    :type repo: str
    :param alert_number: The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the &#x60;number&#x60; field in the response from the &#x60;GET /repos/{owner}/{repo}/code-scanning/alerts&#x60; operation.
    :type alert_number: int
    :param body: 
    :type body: dict | bytes

    """
    body = SecretScanningUpdateAlertRequest.from_dict(body)
    return web.Response(status=200)
