from typing import List, Dict
from aiohttp import web

from openapi_server.models.action_response import ActionResponse
from openapi_server.models.actions_response import ActionsResponse
from openapi_server import util


async def certificates_id_actions_action_id_get(request: web.Request, id, action_id) -> web.Response:
    """Get an Action for a Certificate

    Returns a specific Action for a Certificate. Only type &#x60;managed&#x60; Certificates have Actions.

    :param id: ID of the Certificate
    :type id: int
    :param action_id: ID of the Action
    :type action_id: int

    """
    return web.Response(status=200)


async def certificates_id_actions_get(request: web.Request, id, sort=None, status=None) -> web.Response:
    """Get all Actions for a Certificate

    Returns all Action objects for a Certificate. You can sort the results by using the &#x60;sort&#x60; URI parameter, and filter them with the &#x60;status&#x60; parameter.  Only type &#x60;managed&#x60; Certificates can have Actions. For type &#x60;uploaded&#x60; Certificates the &#x60;actions&#x60; key will always contain an empty array. 

    :param id: ID of the Resource
    :type id: int
    :param sort: Can be used multiple times.
    :type sort: str
    :param status: Can be used multiple times, the response will contain only Actions with specified statuses
    :type status: str

    """
    return web.Response(status=200)


async def certificates_id_actions_retry_post(request: web.Request, id) -> web.Response:
    """Retry Issuance or Renewal

    Retry a failed Certificate issuance or renewal.  Only applicable if the type of the Certificate is &#x60;managed&#x60; and the issuance or renewal status is &#x60;failed&#x60;.  #### Call specific error codes  | Code                                                    | Description                                                               | |---------------------------------------------------------|---------------------------------------------------------------------------| | &#x60;caa_record_does_not_allow_ca&#x60;                          | CAA record does not allow certificate authority                           | | &#x60;ca_dns_validation_failed&#x60;                              | Certificate Authority: DNS validation failed                              | | &#x60;ca_too_many_authorizations_failed_recently&#x60;            | Certificate Authority: Too many authorizations failed recently            | | &#x60;ca_too_many_certificates_issued_for_registered_domain&#x60; | Certificate Authority: Too many certificates issued for registered domain | | &#x60;ca_too_many_duplicate_certificates&#x60;                    | Certificate Authority: Too many duplicate certificates                    | | &#x60;could_not_verify_domain_delegated_to_zone&#x60;             | Could not verify domain delegated to zone                                 | | &#x60;dns_zone_not_found&#x60;                                    | DNS zone not found                                                        | | &#x60;dns_zone_is_secondary_zone&#x60;                            | DNS zone is a secondary zone                                              | 

    :param id: ID of the Certificate
    :type id: int

    """
    return web.Response(status=200)
