from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_verification_request import UpdateVerificationRequest
from openapi_server.models.verification_request import VerificationRequest
from openapi_server.models.verification_response import VerificationResponse
from openapi_server.models.verification_status_response import VerificationStatusResponse
from openapi_server.models.yodlee_error import YodleeError
from openapi_server import util


async def get_verification_status(request: web.Request, account_id=None, provider_account_id=None, verification_type=None) -> web.Response:
    """Get Verification Status

    The get verification status service is used to retrieve the verification status of all accounts for which the MS or CDV process has been initiated.&lt;br&gt;For the MS process, the account details object returns the aggregated information of the verified accounts. For the CDV process, the account details object returns the user provided account information.&lt;br&gt;

    :param account_id: Comma separated accountId
    :type account_id: str
    :param provider_account_id: Comma separated providerAccountId
    :type provider_account_id: str
    :param verification_type: verificationType
    :type verification_type: str

    """
    return web.Response(status=200)


async def initiate_matching_or_challenge_deposite_verification(request: web.Request, body) -> web.Response:
    """Initiaite Matching Service and Challenge Deposit

    The post verification service is used to initiate the matching service (MS) and the challenge deposit account verification (CDV) process to verify account ownership.&lt;br&gt;The MS and CDV process can verify ownership of only bank accounts (i.e., checking and savings).&lt;br&gt;The MS verification can be initiated only for an already aggregated account or a providerAccount.&lt;br&gt;The prerequisite for the MS verification process is to request the ACCT_PROFILE dataset with the HOLDER_NAME attribute.&lt;br&gt;In the MS verification process, a string-match of the account holder name with the registered user name is performed instantaneously. You can contact the Yodlee CustomerCare to configure the full name or only the last name match.&lt;br&gt;Once the CDV process is initiated Yodlee will post the microtransaction (i.e., credit and debit) in the user&#39;s account. The CDV process takes 2 to 3 days to complete as it requires the user to provide the microtransaction details.&lt;br&gt;The CDV process is currently supported only in the United States.&lt;br&gt;The verificationId in the response can be used to track the verification request.&lt;br&gt;&lt;br&gt;&lt;b&gt;Notes:&lt;/b&gt;&lt;li&gt;This endpoint cannot be used to test the CDV functionality in the developer sandbox or test environment. You will need a money transmitter license to implement the CDV functionality and also require the Yodlee Professional Services team&#39;s assistance to set up a dedicated environment.

    :param body: verification information
    :type body: dict | bytes

    """
    body = VerificationRequest.from_dict(body)
    return web.Response(status=200)


async def verify_challenge_deposit(request: web.Request, body) -> web.Response:
    """Verify Challenge Deposit

    The put verification service is used to complete the challenge deposit verification (CDV) process.&lt;br&gt;This service is used only by the customer of CDV flow.&lt;br&gt;In the CDV process, the user-provided microtransaction details (i.e., credit and debit) is matched against the microtransactions posted by Yodlee. For a successful verification of the account&#39;s ownership both the microtransaction details should match.&lt;br&gt;The CDV process is currently supported only in the United States.&lt;br&gt;&lt;br&gt;&lt;b&gt;Notes:&lt;/b&gt;&lt;ul&gt;&lt;li&gt;This endpoint cannot be used to test the CDV functionality in the developer sandbox or test environment. You will need a money transmitter license to implement the CDV functionality and also require the Yodlee Professional Services team&#39;s assistance to set up a dedicated environment.&lt;/li&gt;&lt;/ul&gt;

    :param body: verification information
    :type body: dict | bytes

    """
    body = UpdateVerificationRequest.from_dict(body)
    return web.Response(status=200)
