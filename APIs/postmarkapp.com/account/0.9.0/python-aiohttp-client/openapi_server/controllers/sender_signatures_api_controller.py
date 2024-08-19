from typing import List, Dict
from aiohttp import web

from openapi_server.models.sender_listing_results import SenderListingResults
from openapi_server.models.sender_signature_creation_model import SenderSignatureCreationModel
from openapi_server.models.sender_signature_editing_model import SenderSignatureEditingModel
from openapi_server.models.sender_signature_extended_information import SenderSignatureExtendedInformation
from openapi_server.models.standard_postmark_response import StandardPostmarkResponse
from openapi_server import util


async def create_sender_signature(request: web.Request, x_postmark_account_token, body=None) -> web.Response:
    """Create a Sender Signature

    

    :param x_postmark_account_token: The token associated with the Account on which this request will operate.
    :type x_postmark_account_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = SenderSignatureCreationModel.from_dict(body)
    return web.Response(status=200)


async def delete_sender_signature(request: web.Request, x_postmark_account_token, signatureid) -> web.Response:
    """Delete a Sender Signature

    

    :param x_postmark_account_token: The token associated with the Account on which this request will operate.
    :type x_postmark_account_token: str
    :param signatureid: The ID for the Sender Signature that should be deleted by the request.
    :type signatureid: int

    """
    return web.Response(status=200)


async def edit_sender_signature(request: web.Request, x_postmark_account_token, signatureid, body=None) -> web.Response:
    """Update a Sender Signature

    

    :param x_postmark_account_token: The token associated with the Account on which this request will operate.
    :type x_postmark_account_token: str
    :param signatureid: The ID for the Sender Signature that should be modified by the request.
    :type signatureid: int
    :param body: 
    :type body: dict | bytes

    """
    body = SenderSignatureEditingModel.from_dict(body)
    return web.Response(status=200)


async def get_sender_signature(request: web.Request, x_postmark_account_token, signatureid) -> web.Response:
    """Get a Sender Signature

    

    :param x_postmark_account_token: The token associated with the Account on which this request will operate.
    :type x_postmark_account_token: str
    :param signatureid: The ID for the Sender Signature that should be retrieved.
    :type signatureid: int

    """
    return web.Response(status=200)


async def list_sender_signatures(request: web.Request, x_postmark_account_token, count, offset) -> web.Response:
    """List Sender Signatures

    

    :param x_postmark_account_token: The token associated with the Account on which this request will operate.
    :type x_postmark_account_token: str
    :param count: Number of records to return per request. Max 500.
    :type count: int
    :param offset: Number of records to skip
    :type offset: int

    """
    return web.Response(status=200)


async def request_new_dkim_key_for_sender_signature(request: web.Request, x_postmark_account_token, signatureid) -> web.Response:
    """Request a new DKIM Key

    Requests a new DKIM key to be created. Until the DNS entries are confirmed, the new values will be in the &#x60;DKIMPendingHost&#x60; and &#x60;DKIMPendingTextValue&#x60; fields. After the new DKIM value is verified in DNS, the pending values will migrate to &#x60;DKIMTextValue&#x60; and &#x60;DKIMPendingTextValue&#x60; and Postmark will begin to sign emails with the new DKIM key. 

    :param x_postmark_account_token: The token associated with the Account on which this request will operate.
    :type x_postmark_account_token: str
    :param signatureid: The ID for the Sender Signature for which a new DKIM Key should be generated.
    :type signatureid: int

    """
    return web.Response(status=200)


async def request_spf_verification_for_sender_signature(request: web.Request, x_postmark_account_token, signatureid) -> web.Response:
    """Request DNS Verification for SPF

    

    :param x_postmark_account_token: The token associated with the Account on which this request will operate.
    :type x_postmark_account_token: str
    :param signatureid: The ID for the Sender Signature for which SPF DNS records should be verified.
    :type signatureid: int

    """
    return web.Response(status=200)


async def resend_sender_signature_confirmation_email(request: web.Request, x_postmark_account_token, signatureid) -> web.Response:
    """Resend Signature Confirmation Email

    

    :param x_postmark_account_token: The token associated with the Account on which this request will operate.
    :type x_postmark_account_token: str
    :param signatureid: The ID for the Sender Signature that should have its confirmation email resent.
    :type signatureid: int

    """
    return web.Response(status=200)
