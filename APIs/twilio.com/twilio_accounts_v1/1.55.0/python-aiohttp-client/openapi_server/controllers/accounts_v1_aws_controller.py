from typing import List, Dict
from aiohttp import web

from openapi_server.models.accounts_v1_credential_credential_aws import AccountsV1CredentialCredentialAws
from openapi_server.models.list_credential_aws_response import ListCredentialAwsResponse
from openapi_server import util


async def create_credential_aws(request: web.Request, credentials, account_sid=None, friendly_name=None) -> web.Response:
    """create_credential_aws

    Create a new AWS Credential

    :param credentials: A string that contains the AWS access credentials in the format &#x60;&lt;AWS_ACCESS_KEY_ID&gt;:&lt;AWS_SECRET_ACCESS_KEY&gt;&#x60;. For example, &#x60;AKIAIOSFODNN7EXAMPLE:wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY&#x60;
    :type credentials: str
    :param account_sid: The SID of the Subaccount that this Credential should be associated with. Must be a valid Subaccount of the account issuing the request.
    :type account_sid: str
    :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    :type friendly_name: str

    """
    return web.Response(status=200)


async def delete_credential_aws(request: web.Request, sid) -> web.Response:
    """delete_credential_aws

    Delete a Credential from your account

    :param sid: The Twilio-provided string that uniquely identifies the AWS resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_credential_aws(request: web.Request, sid) -> web.Response:
    """fetch_credential_aws

    Fetch the AWS credentials specified by the provided Credential Sid

    :param sid: The Twilio-provided string that uniquely identifies the AWS resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_credential_aws(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_credential_aws

    Retrieves a collection of AWS Credentials belonging to the account used to make the request

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_credential_aws(request: web.Request, sid, friendly_name=None) -> web.Response:
    """update_credential_aws

    Modify the properties of a given Account

    :param sid: The Twilio-provided string that uniquely identifies the AWS resource to update.
    :type sid: str
    :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    :type friendly_name: str

    """
    return web.Response(status=200)
