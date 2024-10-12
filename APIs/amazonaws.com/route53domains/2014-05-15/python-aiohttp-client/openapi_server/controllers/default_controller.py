from typing import List, Dict
from aiohttp import web

from openapi_server.models.accept_domain_transfer_from_another_aws_account_request import AcceptDomainTransferFromAnotherAwsAccountRequest
from openapi_server.models.accept_domain_transfer_from_another_aws_account_response import AcceptDomainTransferFromAnotherAwsAccountResponse
from openapi_server.models.associate_delegation_signer_to_domain_request import AssociateDelegationSignerToDomainRequest
from openapi_server.models.associate_delegation_signer_to_domain_response import AssociateDelegationSignerToDomainResponse
from openapi_server.models.cancel_domain_transfer_to_another_aws_account_request import CancelDomainTransferToAnotherAwsAccountRequest
from openapi_server.models.cancel_domain_transfer_to_another_aws_account_response import CancelDomainTransferToAnotherAwsAccountResponse
from openapi_server.models.check_domain_availability_request import CheckDomainAvailabilityRequest
from openapi_server.models.check_domain_availability_response import CheckDomainAvailabilityResponse
from openapi_server.models.check_domain_transferability_request import CheckDomainTransferabilityRequest
from openapi_server.models.check_domain_transferability_response import CheckDomainTransferabilityResponse
from openapi_server.models.delete_domain_request import DeleteDomainRequest
from openapi_server.models.delete_domain_response import DeleteDomainResponse
from openapi_server.models.delete_tags_for_domain_request import DeleteTagsForDomainRequest
from openapi_server.models.disable_domain_auto_renew_request import DisableDomainAutoRenewRequest
from openapi_server.models.disable_domain_transfer_lock_request import DisableDomainTransferLockRequest
from openapi_server.models.disable_domain_transfer_lock_response import DisableDomainTransferLockResponse
from openapi_server.models.disassociate_delegation_signer_from_domain_request import DisassociateDelegationSignerFromDomainRequest
from openapi_server.models.disassociate_delegation_signer_from_domain_response import DisassociateDelegationSignerFromDomainResponse
from openapi_server.models.enable_domain_auto_renew_request import EnableDomainAutoRenewRequest
from openapi_server.models.enable_domain_transfer_lock_request import EnableDomainTransferLockRequest
from openapi_server.models.enable_domain_transfer_lock_response import EnableDomainTransferLockResponse
from openapi_server.models.get_contact_reachability_status_request import GetContactReachabilityStatusRequest
from openapi_server.models.get_contact_reachability_status_response import GetContactReachabilityStatusResponse
from openapi_server.models.get_domain_detail_request import GetDomainDetailRequest
from openapi_server.models.get_domain_detail_response import GetDomainDetailResponse
from openapi_server.models.get_domain_suggestions_request import GetDomainSuggestionsRequest
from openapi_server.models.get_domain_suggestions_response import GetDomainSuggestionsResponse
from openapi_server.models.get_operation_detail_request import GetOperationDetailRequest
from openapi_server.models.get_operation_detail_response import GetOperationDetailResponse
from openapi_server.models.list_domains_request import ListDomainsRequest
from openapi_server.models.list_domains_response import ListDomainsResponse
from openapi_server.models.list_operations_request import ListOperationsRequest
from openapi_server.models.list_operations_response import ListOperationsResponse
from openapi_server.models.list_prices_request import ListPricesRequest
from openapi_server.models.list_prices_response import ListPricesResponse
from openapi_server.models.list_tags_for_domain_request import ListTagsForDomainRequest
from openapi_server.models.list_tags_for_domain_response import ListTagsForDomainResponse
from openapi_server.models.push_domain_request import PushDomainRequest
from openapi_server.models.register_domain_request import RegisterDomainRequest
from openapi_server.models.register_domain_response import RegisterDomainResponse
from openapi_server.models.reject_domain_transfer_from_another_aws_account_request import RejectDomainTransferFromAnotherAwsAccountRequest
from openapi_server.models.reject_domain_transfer_from_another_aws_account_response import RejectDomainTransferFromAnotherAwsAccountResponse
from openapi_server.models.renew_domain_request import RenewDomainRequest
from openapi_server.models.renew_domain_response import RenewDomainResponse
from openapi_server.models.resend_contact_reachability_email_request import ResendContactReachabilityEmailRequest
from openapi_server.models.resend_contact_reachability_email_response import ResendContactReachabilityEmailResponse
from openapi_server.models.resend_operation_authorization_request import ResendOperationAuthorizationRequest
from openapi_server.models.retrieve_domain_auth_code_request import RetrieveDomainAuthCodeRequest
from openapi_server.models.retrieve_domain_auth_code_response import RetrieveDomainAuthCodeResponse
from openapi_server.models.transfer_domain_request import TransferDomainRequest
from openapi_server.models.transfer_domain_response import TransferDomainResponse
from openapi_server.models.transfer_domain_to_another_aws_account_request import TransferDomainToAnotherAwsAccountRequest
from openapi_server.models.transfer_domain_to_another_aws_account_response import TransferDomainToAnotherAwsAccountResponse
from openapi_server.models.update_domain_contact_privacy_request import UpdateDomainContactPrivacyRequest
from openapi_server.models.update_domain_contact_privacy_response import UpdateDomainContactPrivacyResponse
from openapi_server.models.update_domain_contact_request import UpdateDomainContactRequest
from openapi_server.models.update_domain_contact_response import UpdateDomainContactResponse
from openapi_server.models.update_domain_nameservers_request import UpdateDomainNameserversRequest
from openapi_server.models.update_domain_nameservers_response import UpdateDomainNameserversResponse
from openapi_server.models.update_tags_for_domain_request import UpdateTagsForDomainRequest
from openapi_server.models.view_billing_request import ViewBillingRequest
from openapi_server.models.view_billing_response import ViewBillingResponse
from openapi_server import util


async def accept_domain_transfer_from_another_aws_account(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """accept_domain_transfer_from_another_aws_account

    &lt;p&gt;Accepts the transfer of a domain from another Amazon Web Services account to the currentAmazon Web Services account. You initiate a transfer between Amazon Web Services accounts using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_TransferDomainToAnotherAwsAccount.html\&quot;&gt;TransferDomainToAnotherAwsAccount&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you use the CLI command at &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cli/latest/reference/route53domains/accept-domain-transfer-from-another-aws-account.html\&quot;&gt;accept-domain-transfer-from-another-aws-account&lt;/a&gt;, use JSON format as input instead of text because otherwise CLI will throw an error from domain transfer input that includes single quotes.&lt;/p&gt; &lt;p&gt;Use either &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ListOperations.html\&quot;&gt;ListOperations&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetOperationDetail.html\&quot;&gt;GetOperationDetail&lt;/a&gt; to determine whether the operation succeeded. &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetOperationDetail.html\&quot;&gt;GetOperationDetail&lt;/a&gt; provides additional information, for example, &lt;code&gt;Domain Transfer from Aws Account 111122223333 has been cancelled&lt;/code&gt;. &lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AcceptDomainTransferFromAnotherAwsAccountRequest.from_dict(body)
    return web.Response(status=200)


async def associate_delegation_signer_to_domain(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_delegation_signer_to_domain

    &lt;p&gt; Creates a delegation signer (DS) record in the registry zone for this domain name.&lt;/p&gt; &lt;p&gt;Note that creating DS record at the registry impacts DNSSEC validation of your DNS records. This action may render your domain name unavailable on the internet if the steps are completed in the wrong order, or with incorrect timing. For more information about DNSSEC signing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring-dnssec.html\&quot;&gt;Configuring DNSSEC signing&lt;/a&gt; in the &lt;i&gt;Route 53 developer guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AssociateDelegationSignerToDomainRequest.from_dict(body)
    return web.Response(status=200)


async def cancel_domain_transfer_to_another_aws_account(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """cancel_domain_transfer_to_another_aws_account

    &lt;p&gt;Cancels the transfer of a domain from the current Amazon Web Services account to another Amazon Web Services account. You initiate a transfer betweenAmazon Web Services accounts using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_TransferDomainToAnotherAwsAccount.html\&quot;&gt;TransferDomainToAnotherAwsAccount&lt;/a&gt;. &lt;/p&gt; &lt;important&gt; &lt;p&gt;You must cancel the transfer before the other Amazon Web Services account accepts the transfer using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_AcceptDomainTransferFromAnotherAwsAccount.html\&quot;&gt;AcceptDomainTransferFromAnotherAwsAccount&lt;/a&gt;.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;Use either &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ListOperations.html\&quot;&gt;ListOperations&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetOperationDetail.html\&quot;&gt;GetOperationDetail&lt;/a&gt; to determine whether the operation succeeded. &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetOperationDetail.html\&quot;&gt;GetOperationDetail&lt;/a&gt; provides additional information, for example, &lt;code&gt;Domain Transfer from Aws Account 111122223333 has been cancelled&lt;/code&gt;. &lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CancelDomainTransferToAnotherAwsAccountRequest.from_dict(body)
    return web.Response(status=200)


async def check_domain_availability(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """check_domain_availability

    This operation checks the availability of one domain name. Note that if the availability status of a domain is pending, you must submit another request to determine the availability of the domain name.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CheckDomainAvailabilityRequest.from_dict(body)
    return web.Response(status=200)


async def check_domain_transferability(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """check_domain_transferability

    Checks whether a domain name can be transferred to Amazon Route 53. 

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CheckDomainTransferabilityRequest.from_dict(body)
    return web.Response(status=200)


async def delete_domain(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_domain

    &lt;p&gt;This operation deletes the specified domain. This action is permanent. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-delete.html\&quot;&gt;Deleting a domain name registration&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To transfer the domain registration to another registrar, use the transfer process that’s provided by the registrar to which you want to transfer the registration. Otherwise, the following apply:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;You can’t get a refund for the cost of a deleted domain registration.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The registry for the top-level domain might hold the domain name for a brief time before releasing it for other users to register (varies by registry). &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;When the registration has been deleted, we&#39;ll send you a confirmation to the registrant contact. The email will come from &lt;code&gt;noreply@domainnameverification.net&lt;/code&gt; or &lt;code&gt;noreply@registrar.amazon.com&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteDomainRequest.from_dict(body)
    return web.Response(status=200)


async def delete_tags_for_domain(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_tags_for_domain

    &lt;p&gt;This operation deletes the specified tags for a domain.&lt;/p&gt; &lt;p&gt;All tag operations are eventually consistent; subsequent operations might not immediately represent all issued operations.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteTagsForDomainRequest.from_dict(body)
    return web.Response(status=200)


async def disable_domain_auto_renew(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disable_domain_auto_renew

    This operation disables automatic renewal of domain registration for the specified domain.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DisableDomainAutoRenewRequest.from_dict(body)
    return web.Response(status=200)


async def disable_domain_transfer_lock(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disable_domain_transfer_lock

    This operation removes the transfer lock on the domain (specifically the &lt;code&gt;clientTransferProhibited&lt;/code&gt; status) to allow domain transfers. We recommend you refrain from performing this action unless you intend to transfer the domain to a different registrar. Successful submission returns an operation ID that you can use to track the progress and completion of the action. If the request is not completed successfully, the domain registrant will be notified by email.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DisableDomainTransferLockRequest.from_dict(body)
    return web.Response(status=200)


async def disassociate_delegation_signer_from_domain(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_delegation_signer_from_domain

    Deletes a delegation signer (DS) record in the registry zone for this domain name.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DisassociateDelegationSignerFromDomainRequest.from_dict(body)
    return web.Response(status=200)


async def enable_domain_auto_renew(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """enable_domain_auto_renew

    &lt;p&gt;This operation configures Amazon Route 53 to automatically renew the specified domain before the domain registration expires. The cost of renewing your domain registration is billed to your Amazon Web Services account.&lt;/p&gt; &lt;p&gt;The period during which you can renew a domain name varies by TLD. For a list of TLDs and their renewal policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html\&quot;&gt;Domains That You Can Register with Amazon Route 53&lt;/a&gt; in the &lt;i&gt;Amazon Route 53 Developer Guide&lt;/i&gt;. Route 53 requires that you renew before the end of the renewal period so we can complete processing before the deadline.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = EnableDomainAutoRenewRequest.from_dict(body)
    return web.Response(status=200)


async def enable_domain_transfer_lock(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """enable_domain_transfer_lock

    This operation sets the transfer lock on the domain (specifically the &lt;code&gt;clientTransferProhibited&lt;/code&gt; status) to prevent domain transfers. Successful submission returns an operation ID that you can use to track the progress and completion of the action. If the request is not completed successfully, the domain registrant will be notified by email.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = EnableDomainTransferLockRequest.from_dict(body)
    return web.Response(status=200)


async def get_contact_reachability_status(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_contact_reachability_status

    &lt;p&gt;For operations that require confirmation that the email address for the registrant contact is valid, such as registering a new domain, this operation returns information about whether the registrant contact has responded.&lt;/p&gt; &lt;p&gt;If you want us to resend the email, use the &lt;code&gt;ResendContactReachabilityEmail&lt;/code&gt; operation.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetContactReachabilityStatusRequest.from_dict(body)
    return web.Response(status=200)


async def get_domain_detail(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_domain_detail

    This operation returns detailed information about a specified domain that is associated with the current Amazon Web Services account. Contact information for the domain is also returned as part of the output.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetDomainDetailRequest.from_dict(body)
    return web.Response(status=200)


async def get_domain_suggestions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_domain_suggestions

    The GetDomainSuggestions operation returns a list of suggested domain names.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetDomainSuggestionsRequest.from_dict(body)
    return web.Response(status=200)


async def get_operation_detail(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_operation_detail

    This operation returns the current status of an operation that is not completed.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetOperationDetailRequest.from_dict(body)
    return web.Response(status=200)


async def list_domains(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_items=None, marker=None) -> web.Response:
    """list_domains

    This operation returns all the domain names registered with Amazon Route 53 for the current Amazon Web Services account if no filtering conditions are used.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_items: Pagination limit
    :type max_items: str
    :param marker: Pagination token
    :type marker: str

    """
    body = ListDomainsRequest.from_dict(body)
    return web.Response(status=200)


async def list_operations(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_items=None, marker=None) -> web.Response:
    """list_operations

    &lt;p&gt;Returns information about all of the operations that return an operation ID and that have ever been performed on domains that were registered by the current account. &lt;/p&gt; &lt;p&gt;This command runs only in the us-east-1 Region.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_items: Pagination limit
    :type max_items: str
    :param marker: Pagination token
    :type marker: str

    """
    body = ListOperationsRequest.from_dict(body)
    return web.Response(status=200)


async def list_prices(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_items=None, marker=None) -> web.Response:
    """list_prices

    &lt;p&gt;Lists the following prices for either all the TLDs supported by Route 53, or the specified TLD:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Registration&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Transfer&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Owner change&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Domain renewal&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Domain restoration&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_items: Pagination limit
    :type max_items: str
    :param marker: Pagination token
    :type marker: str

    """
    body = ListPricesRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_domain(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_domain

    &lt;p&gt;This operation returns all of the tags that are associated with the specified domain.&lt;/p&gt; &lt;p&gt;All tag operations are eventually consistent; subsequent operations might not immediately represent all issued operations.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ListTagsForDomainRequest.from_dict(body)
    return web.Response(status=200)


async def push_domain(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """push_domain

    &lt;p&gt; Moves a domain from Amazon Web Services to another registrar. &lt;/p&gt; &lt;p&gt;Supported actions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Changes the IPS tags of a .uk domain, and pushes it to transit. Transit means that the domain is ready to be transferred to another registrar.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PushDomainRequest.from_dict(body)
    return web.Response(status=200)


async def register_domain(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """register_domain

    &lt;p&gt;This operation registers a domain. For some top-level domains (TLDs), this operation requires extra parameters.&lt;/p&gt; &lt;p&gt;When you register a domain, Amazon Route 53 does the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Creates a Route 53 hosted zone that has the same name as the domain. Route 53 assigns four name servers to your hosted zone and automatically updates your domain registration with the names of these name servers.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Enables auto renew, so your domain registration will renew automatically each year. We&#39;ll notify you in advance of the renewal date so you can choose whether to renew the registration.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Optionally enables privacy protection, so WHOIS queries return contact for the registrar or the phrase \&quot;REDACTED FOR PRIVACY\&quot;, or \&quot;On behalf of &amp;lt;domain name&amp;gt; owner.\&quot; If you don&#39;t enable privacy protection, WHOIS queries return the information that you entered for the administrative, registrant, and technical contacts.&lt;/p&gt; &lt;note&gt; &lt;p&gt;While some domains may allow different privacy settings per contact, we recommend specifying the same privacy setting for all contacts.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If registration is successful, returns an operation ID that you can use to track the progress and completion of the action. If the request is not completed successfully, the domain registrant is notified by email.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Charges your Amazon Web Services account an amount based on the top-level domain. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/route53/pricing/\&quot;&gt;Amazon Route 53 Pricing&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = RegisterDomainRequest.from_dict(body)
    return web.Response(status=200)


async def reject_domain_transfer_from_another_aws_account(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """reject_domain_transfer_from_another_aws_account

    &lt;p&gt;Rejects the transfer of a domain from another Amazon Web Services account to the current Amazon Web Services account. You initiate a transfer betweenAmazon Web Services accounts using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_TransferDomainToAnotherAwsAccount.html\&quot;&gt;TransferDomainToAnotherAwsAccount&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;Use either &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ListOperations.html\&quot;&gt;ListOperations&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetOperationDetail.html\&quot;&gt;GetOperationDetail&lt;/a&gt; to determine whether the operation succeeded. &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetOperationDetail.html\&quot;&gt;GetOperationDetail&lt;/a&gt; provides additional information, for example, &lt;code&gt;Domain Transfer from Aws Account 111122223333 has been cancelled&lt;/code&gt;. &lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = RejectDomainTransferFromAnotherAwsAccountRequest.from_dict(body)
    return web.Response(status=200)


async def renew_domain(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """renew_domain

    &lt;p&gt;This operation renews a domain for the specified number of years. The cost of renewing your domain is billed to your Amazon Web Services account.&lt;/p&gt; &lt;p&gt;We recommend that you renew your domain several weeks before the expiration date. Some TLD registries delete domains before the expiration date if you haven&#39;t renewed far enough in advance. For more information about renewing domain registration, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-renew.html\&quot;&gt;Renewing Registration for a Domain&lt;/a&gt; in the &lt;i&gt;Amazon Route 53 Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = RenewDomainRequest.from_dict(body)
    return web.Response(status=200)


async def resend_contact_reachability_email(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """resend_contact_reachability_email

    For operations that require confirmation that the email address for the registrant contact is valid, such as registering a new domain, this operation resends the confirmation email to the current email address for the registrant contact.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ResendContactReachabilityEmailRequest.from_dict(body)
    return web.Response(status=200)


async def resend_operation_authorization(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """resend_operation_authorization

     Resend the form of authorization email for this operation. 

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ResendOperationAuthorizationRequest.from_dict(body)
    return web.Response(status=200)


async def retrieve_domain_auth_code(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """retrieve_domain_auth_code

    This operation returns the authorization code for the domain. To transfer a domain to another registrar, you provide this value to the new registrar.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = RetrieveDomainAuthCodeRequest.from_dict(body)
    return web.Response(status=200)


async def transfer_domain(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """transfer_domain

    &lt;p&gt;Transfers a domain from another registrar to Amazon Route 53. &lt;/p&gt; &lt;p&gt;For more information about transferring domains, see the following topics:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;For transfer requirements, a detailed procedure, and information about viewing the status of a domain that you&#39;re transferring to Route 53, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-transfer-to-route-53.html\&quot;&gt;Transferring Registration for a Domain to Amazon Route 53&lt;/a&gt; in the &lt;i&gt;Amazon Route 53 Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For information about how to transfer a domain from one Amazon Web Services account to another, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_TransferDomainToAnotherAwsAccount.html\&quot;&gt;TransferDomainToAnotherAwsAccount&lt;/a&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For information about how to transfer a domain to another domain registrar, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-transfer-from-route-53.html\&quot;&gt;Transferring a Domain from Amazon Route 53 to Another Registrar&lt;/a&gt; in the &lt;i&gt;Amazon Route 53 Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the registrar for your domain is also the DNS service provider for the domain, we highly recommend that you transfer your DNS service to Route 53 or to another DNS service provider before you transfer your registration. Some registrars provide free DNS service when you purchase a domain registration. When you transfer the registration, the previous registrar will not renew your domain registration and could end your DNS service at any time.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If the registrar for your domain is also the DNS service provider for the domain and you don&#39;t transfer DNS service to another provider, your website, email, and the web applications associated with the domain might become unavailable.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;If the transfer is successful, this method returns an operation ID that you can use to track the progress and completion of the action. If the transfer doesn&#39;t complete successfully, the domain registrant will be notified by email.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = TransferDomainRequest.from_dict(body)
    return web.Response(status=200)


async def transfer_domain_to_another_aws_account(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """transfer_domain_to_another_aws_account

    &lt;p&gt;Transfers a domain from the current Amazon Web Services account to another Amazon Web Services account. Note the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The Amazon Web Services account that you&#39;re transferring the domain to must accept the transfer. If the other account doesn&#39;t accept the transfer within 3 days, we cancel the transfer. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_AcceptDomainTransferFromAnotherAwsAccount.html\&quot;&gt;AcceptDomainTransferFromAnotherAwsAccount&lt;/a&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You can cancel the transfer before the other account accepts it. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_CancelDomainTransferToAnotherAwsAccount.html\&quot;&gt;CancelDomainTransferToAnotherAwsAccount&lt;/a&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The other account can reject the transfer. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_RejectDomainTransferFromAnotherAwsAccount.html\&quot;&gt;RejectDomainTransferFromAnotherAwsAccount&lt;/a&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;important&gt; &lt;p&gt;When you transfer a domain from one Amazon Web Services account to another, Route 53 doesn&#39;t transfer the hosted zone that is associated with the domain. DNS resolution isn&#39;t affected if the domain and the hosted zone are owned by separate accounts, so transferring the hosted zone is optional. For information about transferring the hosted zone to another Amazon Web Services account, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-migrating.html\&quot;&gt;Migrating a Hosted Zone to a Different Amazon Web Services Account&lt;/a&gt; in the &lt;i&gt;Amazon Route 53 Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;Use either &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ListOperations.html\&quot;&gt;ListOperations&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetOperationDetail.html\&quot;&gt;GetOperationDetail&lt;/a&gt; to determine whether the operation succeeded. &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetOperationDetail.html\&quot;&gt;GetOperationDetail&lt;/a&gt; provides additional information, for example, &lt;code&gt;Domain Transfer from Aws Account 111122223333 has been cancelled&lt;/code&gt;. &lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = TransferDomainToAnotherAwsAccountRequest.from_dict(body)
    return web.Response(status=200)


async def update_domain_contact(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_domain_contact

    &lt;p&gt;This operation updates the contact information for a particular domain. You must specify information for at least one contact: registrant, administrator, or technical.&lt;/p&gt; &lt;p&gt;If the update is successful, this method returns an operation ID that you can use to track the progress and completion of the operation. If the request is not completed successfully, the domain registrant will be notified by email.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateDomainContactRequest.from_dict(body)
    return web.Response(status=200)


async def update_domain_contact_privacy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_domain_contact_privacy

    &lt;p&gt;This operation updates the specified domain contact&#39;s privacy setting. When privacy protection is enabled, your contact information is replaced with contact information for the registrar or with the phrase \&quot;REDACTED FOR PRIVACY\&quot;, or \&quot;On behalf of &amp;lt;domain name&amp;gt; owner.\&quot;&lt;/p&gt; &lt;note&gt; &lt;p&gt;While some domains may allow different privacy settings per contact, we recommend specifying the same privacy setting for all contacts.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This operation affects only the contact information for the specified contact type (administrative, registrant, or technical). If the request succeeds, Amazon Route 53 returns an operation ID that you can use with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetOperationDetail.html\&quot;&gt;GetOperationDetail&lt;/a&gt; to track the progress and completion of the action. If the request doesn&#39;t complete successfully, the domain registrant will be notified by email.&lt;/p&gt; &lt;important&gt; &lt;p&gt;By disabling the privacy service via API, you consent to the publication of the contact information provided for this domain via the public WHOIS database. You certify that you are the registrant of this domain name and have the authority to make this decision. You may withdraw your consent at any time by enabling privacy protection using either &lt;code&gt;UpdateDomainContactPrivacy&lt;/code&gt; or the Route 53 console. Enabling privacy protection removes the contact information provided for this domain from the WHOIS database. For more information on our privacy practices, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/privacy/\&quot;&gt;https://aws.amazon.com/privacy/&lt;/a&gt;.&lt;/p&gt; &lt;/important&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateDomainContactPrivacyRequest.from_dict(body)
    return web.Response(status=200)


async def update_domain_nameservers(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_domain_nameservers

    &lt;p&gt;This operation replaces the current set of name servers for the domain with the specified set of name servers. If you use Amazon Route 53 as your DNS service, specify the four name servers in the delegation set for the hosted zone for the domain.&lt;/p&gt; &lt;p&gt;If successful, this operation returns an operation ID that you can use to track the progress and completion of the action. If the request is not completed successfully, the domain registrant will be notified by email.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateDomainNameserversRequest.from_dict(body)
    return web.Response(status=200)


async def update_tags_for_domain(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_tags_for_domain

    &lt;p&gt;This operation adds or updates tags for a specified domain.&lt;/p&gt; &lt;p&gt;All tag operations are eventually consistent; subsequent operations might not immediately represent all issued operations.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateTagsForDomainRequest.from_dict(body)
    return web.Response(status=200)


async def view_billing(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_items=None, marker=None) -> web.Response:
    """view_billing

    Returns all the domain-related billing records for the current Amazon Web Services account for a specified period

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_items: Pagination limit
    :type max_items: str
    :param marker: Pagination token
    :type marker: str

    """
    body = ViewBillingRequest.from_dict(body)
    return web.Response(status=200)
