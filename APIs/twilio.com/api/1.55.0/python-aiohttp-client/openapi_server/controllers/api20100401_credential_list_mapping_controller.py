from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_sip_sip_domain_sip_credential_list_mapping import ApiV2010AccountSipSipDomainSipCredentialListMapping
from openapi_server.models.list_sip_credential_list_mapping_response import ListSipCredentialListMappingResponse
from openapi_server import util


async def create_sip_credential_list_mapping(request: web.Request, account_sid, domain_sid, credential_list_sid) -> web.Response:
    """create_sip_credential_list_mapping

    Create a CredentialListMapping resource for an account.

    :param account_sid: The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    :type account_sid: str
    :param domain_sid: A 34 character string that uniquely identifies the SIP Domain for which the CredentialList resource will be mapped.
    :type domain_sid: str
    :param credential_list_sid: A 34 character string that uniquely identifies the CredentialList resource to map to the SIP domain.
    :type credential_list_sid: str

    """
    return web.Response(status=200)


async def delete_sip_credential_list_mapping(request: web.Request, account_sid, domain_sid, sid) -> web.Response:
    """delete_sip_credential_list_mapping

    Delete a CredentialListMapping resource from an account.

    :param account_sid: The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    :type account_sid: str
    :param domain_sid: A 34 character string that uniquely identifies the SIP Domain that includes the resource to delete.
    :type domain_sid: str
    :param sid: A 34 character string that uniquely identifies the resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_sip_credential_list_mapping(request: web.Request, account_sid, domain_sid, sid) -> web.Response:
    """fetch_sip_credential_list_mapping

    Fetch a single CredentialListMapping resource from an account.

    :param account_sid: The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    :type account_sid: str
    :param domain_sid: A 34 character string that uniquely identifies the SIP Domain that includes the resource to fetch.
    :type domain_sid: str
    :param sid: A 34 character string that uniquely identifies the resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_sip_credential_list_mapping(request: web.Request, account_sid, domain_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_sip_credential_list_mapping

    Read multiple CredentialListMapping resources from an account.

    :param account_sid: The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    :type account_sid: str
    :param domain_sid: A 34 character string that uniquely identifies the SIP Domain that includes the resource to read.
    :type domain_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
