from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_certificate_authority_audit_report_request import CreateCertificateAuthorityAuditReportRequest
from openapi_server.models.create_certificate_authority_audit_report_response import CreateCertificateAuthorityAuditReportResponse
from openapi_server.models.create_certificate_authority_request import CreateCertificateAuthorityRequest
from openapi_server.models.create_certificate_authority_response import CreateCertificateAuthorityResponse
from openapi_server.models.create_permission_request import CreatePermissionRequest
from openapi_server.models.delete_certificate_authority_request import DeleteCertificateAuthorityRequest
from openapi_server.models.delete_permission_request import DeletePermissionRequest
from openapi_server.models.delete_policy_request import DeletePolicyRequest
from openapi_server.models.describe_certificate_authority_audit_report_request import DescribeCertificateAuthorityAuditReportRequest
from openapi_server.models.describe_certificate_authority_audit_report_response import DescribeCertificateAuthorityAuditReportResponse
from openapi_server.models.describe_certificate_authority_request import DescribeCertificateAuthorityRequest
from openapi_server.models.describe_certificate_authority_response import DescribeCertificateAuthorityResponse
from openapi_server.models.get_certificate_authority_certificate_request import GetCertificateAuthorityCertificateRequest
from openapi_server.models.get_certificate_authority_certificate_response import GetCertificateAuthorityCertificateResponse
from openapi_server.models.get_certificate_authority_csr_request import GetCertificateAuthorityCsrRequest
from openapi_server.models.get_certificate_authority_csr_response import GetCertificateAuthorityCsrResponse
from openapi_server.models.get_certificate_request import GetCertificateRequest
from openapi_server.models.get_certificate_response import GetCertificateResponse
from openapi_server.models.get_policy_request import GetPolicyRequest
from openapi_server.models.get_policy_response import GetPolicyResponse
from openapi_server.models.import_certificate_authority_certificate_request import ImportCertificateAuthorityCertificateRequest
from openapi_server.models.issue_certificate_request import IssueCertificateRequest
from openapi_server.models.issue_certificate_response import IssueCertificateResponse
from openapi_server.models.list_certificate_authorities_request import ListCertificateAuthoritiesRequest
from openapi_server.models.list_certificate_authorities_response import ListCertificateAuthoritiesResponse
from openapi_server.models.list_permissions_request import ListPermissionsRequest
from openapi_server.models.list_permissions_response import ListPermissionsResponse
from openapi_server.models.list_tags_request import ListTagsRequest
from openapi_server.models.list_tags_response import ListTagsResponse
from openapi_server.models.put_policy_request import PutPolicyRequest
from openapi_server.models.restore_certificate_authority_request import RestoreCertificateAuthorityRequest
from openapi_server.models.revoke_certificate_request import RevokeCertificateRequest
from openapi_server.models.tag_certificate_authority_request import TagCertificateAuthorityRequest
from openapi_server.models.untag_certificate_authority_request import UntagCertificateAuthorityRequest
from openapi_server.models.update_certificate_authority_request import UpdateCertificateAuthorityRequest
from openapi_server import util


async def create_certificate_authority(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_certificate_authority

    &lt;p&gt;Creates a root or subordinate private certificate authority (CA). You must specify the CA configuration, an optional configuration for Online Certificate Status Protocol (OCSP) and/or a certificate revocation list (CRL), the CA type, and an optional idempotency token to avoid accidental creation of multiple CAs. The CA configuration specifies the name of the algorithm and key size to be used to create the CA private key, the type of signing algorithm that the CA uses, and X.500 subject information. The OCSP configuration can optionally specify a custom URL for the OCSP responder. The CRL configuration specifies the CRL expiration period in days (the validity period of the CRL), the Amazon S3 bucket that will contain the CRL, and a CNAME alias for the S3 bucket that is included in certificates issued by the CA. If successful, this action returns the Amazon Resource Name (ARN) of the CA.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Both Amazon Web Services Private CA and the IAM principal must have permission to write to the S3 bucket that you specify. If the IAM principal making the call does not have permission to write to the bucket, then an exception is thrown. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/userguide/crl-planning.html#s3-policies\&quot;&gt;Access policies for CRLs in Amazon S3&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Amazon Web Services Private CA assets that are stored in Amazon S3 can be protected with encryption. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/userguide/PcaCreateCa.html#crl-encryption\&quot;&gt;Encrypting Your CRLs&lt;/a&gt;.&lt;/p&gt;

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
    body = CreateCertificateAuthorityRequest.from_dict(body)
    return web.Response(status=200)


async def create_certificate_authority_audit_report(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_certificate_authority_audit_report

    &lt;p&gt;Creates an audit report that lists every time that your CA private key is used. The report is saved in the Amazon S3 bucket that you specify on input. The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_IssueCertificate.html\&quot;&gt;IssueCertificate&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_RevokeCertificate.html\&quot;&gt;RevokeCertificate&lt;/a&gt; actions use the private key. &lt;/p&gt; &lt;note&gt; &lt;p&gt;Both Amazon Web Services Private CA and the IAM principal must have permission to write to the S3 bucket that you specify. If the IAM principal making the call does not have permission to write to the bucket, then an exception is thrown. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/userguide/crl-planning.html#s3-policies\&quot;&gt;Access policies for CRLs in Amazon S3&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Amazon Web Services Private CA assets that are stored in Amazon S3 can be protected with encryption. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/userguide/PcaAuditReport.html#audit-report-encryption\&quot;&gt;Encrypting Your Audit Reports&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can generate a maximum of one report every 30 minutes.&lt;/p&gt; &lt;/note&gt;

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
    body = CreateCertificateAuthorityAuditReportRequest.from_dict(body)
    return web.Response(status=200)


async def create_permission(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_permission

    &lt;p&gt;Grants one or more permissions on a private CA to the Certificate Manager (ACM) service principal (&lt;code&gt;acm.amazonaws.com&lt;/code&gt;). These permissions allow ACM to issue and renew ACM certificates that reside in the same Amazon Web Services account as the CA.&lt;/p&gt; &lt;p&gt;You can list current permissions with the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListPermissions.html\&quot;&gt;ListPermissions&lt;/a&gt; action and revoke them with the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeletePermission.html\&quot;&gt;DeletePermission&lt;/a&gt; action.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;About Permissions&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the private CA and the certificates it issues reside in the same account, you can use &lt;code&gt;CreatePermission&lt;/code&gt; to grant permissions for ACM to carry out automatic certificate renewals.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For automatic certificate renewal to succeed, the ACM service principal needs permissions to create, retrieve, and list certificates.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the private CA and the ACM certificates reside in different accounts, then permissions cannot be used to enable automatic renewals. Instead, the ACM certificate owner must set up a resource-based policy to enable cross-account issuance and renewals. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/userguide/pca-rbp.html\&quot;&gt;Using a Resource Based Policy with Amazon Web Services Private CA&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = CreatePermissionRequest.from_dict(body)
    return web.Response(status=200)


async def delete_certificate_authority(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_certificate_authority

    &lt;p&gt;Deletes a private certificate authority (CA). You must provide the Amazon Resource Name (ARN) of the private CA that you want to delete. You can find the ARN by calling the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListCertificateAuthorities.html\&quot;&gt;ListCertificateAuthorities&lt;/a&gt; action. &lt;/p&gt; &lt;note&gt; &lt;p&gt;Deleting a CA will invalidate other CAs and certificates below it in your CA hierarchy.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Before you can delete a CA that you have created and activated, you must disable it. To do this, call the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_UpdateCertificateAuthority.html\&quot;&gt;UpdateCertificateAuthority&lt;/a&gt; action and set the &lt;b&gt;CertificateAuthorityStatus&lt;/b&gt; parameter to &lt;code&gt;DISABLED&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;Additionally, you can delete a CA if you are waiting for it to be created (that is, the status of the CA is &lt;code&gt;CREATING&lt;/code&gt;). You can also delete it if the CA has been created but you haven&#39;t yet imported the signed certificate into Amazon Web Services Private CA (that is, the status of the CA is &lt;code&gt;PENDING_CERTIFICATE&lt;/code&gt;). &lt;/p&gt; &lt;p&gt;When you successfully call &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeleteCertificateAuthority.html\&quot;&gt;DeleteCertificateAuthority&lt;/a&gt;, the CA&#39;s status changes to &lt;code&gt;DELETED&lt;/code&gt;. However, the CA won&#39;t be permanently deleted until the restoration period has passed. By default, if you do not set the &lt;code&gt;PermanentDeletionTimeInDays&lt;/code&gt; parameter, the CA remains restorable for 30 days. You can set the parameter from 7 to 30 days. The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_DescribeCertificateAuthority.html\&quot;&gt;DescribeCertificateAuthority&lt;/a&gt; action returns the time remaining in the restoration window of a private CA in the &lt;code&gt;DELETED&lt;/code&gt; state. To restore an eligible CA, call the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_RestoreCertificateAuthority.html\&quot;&gt;RestoreCertificateAuthority&lt;/a&gt; action.&lt;/p&gt;

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
    body = DeleteCertificateAuthorityRequest.from_dict(body)
    return web.Response(status=200)


async def delete_permission(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_permission

    &lt;p&gt;Revokes permissions on a private CA granted to the Certificate Manager (ACM) service principal (acm.amazonaws.com). &lt;/p&gt; &lt;p&gt;These permissions allow ACM to issue and renew ACM certificates that reside in the same Amazon Web Services account as the CA. If you revoke these permissions, ACM will no longer renew the affected certificates automatically.&lt;/p&gt; &lt;p&gt;Permissions can be granted with the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreatePermission.html\&quot;&gt;CreatePermission&lt;/a&gt; action and listed with the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListPermissions.html\&quot;&gt;ListPermissions&lt;/a&gt; action. &lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;About Permissions&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the private CA and the certificates it issues reside in the same account, you can use &lt;code&gt;CreatePermission&lt;/code&gt; to grant permissions for ACM to carry out automatic certificate renewals.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For automatic certificate renewal to succeed, the ACM service principal needs permissions to create, retrieve, and list certificates.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the private CA and the ACM certificates reside in different accounts, then permissions cannot be used to enable automatic renewals. Instead, the ACM certificate owner must set up a resource-based policy to enable cross-account issuance and renewals. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/userguide/pca-rbp.html\&quot;&gt;Using a Resource Based Policy with Amazon Web Services Private CA&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = DeletePermissionRequest.from_dict(body)
    return web.Response(status=200)


async def delete_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_policy

    &lt;p&gt;Deletes the resource-based policy attached to a private CA. Deletion will remove any access that the policy has granted. If there is no policy attached to the private CA, this action will return successful.&lt;/p&gt; &lt;p&gt;If you delete a policy that was applied through Amazon Web Services Resource Access Manager (RAM), the CA will be removed from all shares in which it was included. &lt;/p&gt; &lt;p&gt;The Certificate Manager Service Linked Role that the policy supports is not affected when you delete the policy. &lt;/p&gt; &lt;p&gt;The current policy can be shown with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetPolicy.html\&quot;&gt;GetPolicy&lt;/a&gt; and updated with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_PutPolicy.html\&quot;&gt;PutPolicy&lt;/a&gt;.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;About Policies&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;A policy grants access on a private CA to an Amazon Web Services customer account, to Amazon Web Services Organizations, or to an Amazon Web Services Organizations unit. Policies are under the control of a CA administrator. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/userguide/pca-rbp.html\&quot;&gt;Using a Resource Based Policy with Amazon Web Services Private CA&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A policy permits a user of Certificate Manager (ACM) to issue ACM certificates signed by a CA in another account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For ACM to manage automatic renewal of these certificates, the ACM user must configure a Service Linked Role (SLR). The SLR allows the ACM service to assume the identity of the user, subject to confirmation against the Amazon Web Services Private CA policy. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/acm/latest/userguide/acm-slr.html\&quot;&gt;Using a Service Linked Role with ACM&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Updates made in Amazon Web Services Resource Manager (RAM) are reflected in policies. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/userguide/pca-ram.html\&quot;&gt;Attach a Policy for Cross-Account Access&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = DeletePolicyRequest.from_dict(body)
    return web.Response(status=200)


async def describe_certificate_authority(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_certificate_authority

    &lt;p&gt;Lists information about your private certificate authority (CA) or one that has been shared with you. You specify the private CA on input by its ARN (Amazon Resource Name). The output contains the status of your CA. This can be any of the following: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CREATING&lt;/code&gt; - Amazon Web Services Private CA is creating your private certificate authority.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PENDING_CERTIFICATE&lt;/code&gt; - The certificate is pending. You must use your Amazon Web Services Private CA-hosted or on-premises root or subordinate CA to sign your private CA CSR and then import it into Amazon Web Services Private CA. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ACTIVE&lt;/code&gt; - Your private CA is active.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DISABLED&lt;/code&gt; - Your private CA has been disabled.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;EXPIRED&lt;/code&gt; - Your private CA certificate has expired.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;FAILED&lt;/code&gt; - Your private CA has failed. Your CA can fail because of problems such a network outage or back-end Amazon Web Services failure or other errors. A failed CA can never return to the pending state. You must create a new CA. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DELETED&lt;/code&gt; - Your private CA is within the restoration period, after which it is permanently deleted. The length of time remaining in the CA&#39;s restoration period is also included in this action&#39;s output.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = DescribeCertificateAuthorityRequest.from_dict(body)
    return web.Response(status=200)


async def describe_certificate_authority_audit_report(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_certificate_authority_audit_report

    Lists information about a specific audit report created by calling the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthorityAuditReport.html\&quot;&gt;CreateCertificateAuthorityAuditReport&lt;/a&gt; action. Audit information is created every time the certificate authority (CA) private key is used. The private key is used when you call the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_IssueCertificate.html\&quot;&gt;IssueCertificate&lt;/a&gt; action or the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_RevokeCertificate.html\&quot;&gt;RevokeCertificate&lt;/a&gt; action. 

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
    body = DescribeCertificateAuthorityAuditReportRequest.from_dict(body)
    return web.Response(status=200)


async def get_certificate(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_certificate

    Retrieves a certificate from your private CA or one that has been shared with you. The ARN of the certificate is returned when you call the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_IssueCertificate.html\&quot;&gt;IssueCertificate&lt;/a&gt; action. You must specify both the ARN of your private CA and the ARN of the issued certificate when calling the &lt;b&gt;GetCertificate&lt;/b&gt; action. You can retrieve the certificate if it is in the &lt;b&gt;ISSUED&lt;/b&gt; state. You can call the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthorityAuditReport.html\&quot;&gt;CreateCertificateAuthorityAuditReport&lt;/a&gt; action to create a report that contains information about all of the certificates issued and revoked by your private CA. 

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
    body = GetCertificateRequest.from_dict(body)
    return web.Response(status=200)


async def get_certificate_authority_certificate(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_certificate_authority_certificate

    Retrieves the certificate and certificate chain for your private certificate authority (CA) or one that has been shared with you. Both the certificate and the chain are base64 PEM-encoded. The chain does not include the CA certificate. Each certificate in the chain signs the one before it. 

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
    body = GetCertificateAuthorityCertificateRequest.from_dict(body)
    return web.Response(status=200)


async def get_certificate_authority_csr(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_certificate_authority_csr

    Retrieves the certificate signing request (CSR) for your private certificate authority (CA). The CSR is created when you call the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html\&quot;&gt;CreateCertificateAuthority&lt;/a&gt; action. Sign the CSR with your Amazon Web Services Private CA-hosted or on-premises root or subordinate CA. Then import the signed certificate back into Amazon Web Services Private CA by calling the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_ImportCertificateAuthorityCertificate.html\&quot;&gt;ImportCertificateAuthorityCertificate&lt;/a&gt; action. The CSR is returned as a base64 PEM-encoded string. 

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
    body = GetCertificateAuthorityCsrRequest.from_dict(body)
    return web.Response(status=200)


async def get_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_policy

    &lt;p&gt;Retrieves the resource-based policy attached to a private CA. If either the private CA resource or the policy cannot be found, this action returns a &lt;code&gt;ResourceNotFoundException&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;The policy can be attached or updated with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_PutPolicy.html\&quot;&gt;PutPolicy&lt;/a&gt; and removed with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeletePolicy.html\&quot;&gt;DeletePolicy&lt;/a&gt;.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;About Policies&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;A policy grants access on a private CA to an Amazon Web Services customer account, to Amazon Web Services Organizations, or to an Amazon Web Services Organizations unit. Policies are under the control of a CA administrator. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/userguide/pca-rbp.html\&quot;&gt;Using a Resource Based Policy with Amazon Web Services Private CA&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A policy permits a user of Certificate Manager (ACM) to issue ACM certificates signed by a CA in another account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For ACM to manage automatic renewal of these certificates, the ACM user must configure a Service Linked Role (SLR). The SLR allows the ACM service to assume the identity of the user, subject to confirmation against the Amazon Web Services Private CA policy. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/acm/latest/userguide/acm-slr.html\&quot;&gt;Using a Service Linked Role with ACM&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Updates made in Amazon Web Services Resource Manager (RAM) are reflected in policies. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/userguide/pca-ram.html\&quot;&gt;Attach a Policy for Cross-Account Access&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = GetPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def import_certificate_authority_certificate(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """import_certificate_authority_certificate

    &lt;p&gt;Imports a signed private CA certificate into Amazon Web Services Private CA. This action is used when you are using a chain of trust whose root is located outside Amazon Web Services Private CA. Before you can call this action, the following preparations must in place:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;In Amazon Web Services Private CA, call the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html\&quot;&gt;CreateCertificateAuthority&lt;/a&gt; action to create the private CA that you plan to back with the imported certificate.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Call the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificateAuthorityCsr.html\&quot;&gt;GetCertificateAuthorityCsr&lt;/a&gt; action to generate a certificate signing request (CSR).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Sign the CSR using a root or intermediate CA hosted by either an on-premises PKI hierarchy or by a commercial CA.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Create a certificate chain and copy the signed certificate and the certificate chain to your working directory.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;Amazon Web Services Private CA supports three scenarios for installing a CA certificate:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Installing a certificate for a root CA hosted by Amazon Web Services Private CA.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Installing a subordinate CA certificate whose parent authority is hosted by Amazon Web Services Private CA.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Installing a subordinate CA certificate whose parent authority is externally hosted.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The following additional requirements apply when you import a CA certificate.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Only a self-signed certificate can be imported as a root CA.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A self-signed certificate cannot be imported as a subordinate CA.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Your certificate chain must not include the private CA certificate that you are importing.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Your root CA must be the last certificate in your chain. The subordinate certificate, if any, that your root CA signed must be next to last. The subordinate certificate signed by the preceding subordinate CA must come next, and so on until your chain is built. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The chain must be PEM-encoded.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The maximum allowed size of a certificate is 32 KB.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The maximum allowed size of a certificate chain is 2 MB.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;i&gt;Enforcement of Critical Constraints&lt;/i&gt; &lt;/p&gt; &lt;p&gt;Amazon Web Services Private CA allows the following extensions to be marked critical in the imported CA certificate or chain.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Basic constraints (&lt;i&gt;must&lt;/i&gt; be marked critical)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Subject alternative names&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Key usage&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Extended key usage&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Authority key identifier&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Subject key identifier&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Issuer alternative name&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Subject directory attributes&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Subject information access&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Certificate policies&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Policy mappings&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Inhibit anyPolicy&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Amazon Web Services Private CA rejects the following extensions when they are marked critical in an imported CA certificate or chain.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Name constraints&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Policy constraints&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;CRL distribution points&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Authority information access&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Freshest CRL&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Any other extension&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = ImportCertificateAuthorityCertificateRequest.from_dict(body)
    return web.Response(status=200)


async def issue_certificate(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """issue_certificate

    &lt;p&gt;Uses your private certificate authority (CA), or one that has been shared with you, to issue a client certificate. This action returns the Amazon Resource Name (ARN) of the certificate. You can retrieve the certificate by calling the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificate.html\&quot;&gt;GetCertificate&lt;/a&gt; action and specifying the ARN. &lt;/p&gt; &lt;note&gt; &lt;p&gt;You cannot use the ACM &lt;b&gt;ListCertificateAuthorities&lt;/b&gt; action to retrieve the ARNs of the certificates that you issue by using Amazon Web Services Private CA.&lt;/p&gt; &lt;/note&gt;

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
    body = IssueCertificateRequest.from_dict(body)
    return web.Response(status=200)


async def list_certificate_authorities(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_certificate_authorities

    Lists the private certificate authorities that you created by using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html\&quot;&gt;CreateCertificateAuthority&lt;/a&gt; action.

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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListCertificateAuthoritiesRequest.from_dict(body)
    return web.Response(status=200)


async def list_permissions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_permissions

    &lt;p&gt;List all permissions on a private CA, if any, granted to the Certificate Manager (ACM) service principal (acm.amazonaws.com). &lt;/p&gt; &lt;p&gt;These permissions allow ACM to issue and renew ACM certificates that reside in the same Amazon Web Services account as the CA. &lt;/p&gt; &lt;p&gt;Permissions can be granted with the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreatePermission.html\&quot;&gt;CreatePermission&lt;/a&gt; action and revoked with the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeletePermission.html\&quot;&gt;DeletePermission&lt;/a&gt; action.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;About Permissions&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the private CA and the certificates it issues reside in the same account, you can use &lt;code&gt;CreatePermission&lt;/code&gt; to grant permissions for ACM to carry out automatic certificate renewals.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For automatic certificate renewal to succeed, the ACM service principal needs permissions to create, retrieve, and list certificates.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the private CA and the ACM certificates reside in different accounts, then permissions cannot be used to enable automatic renewals. Instead, the ACM certificate owner must set up a resource-based policy to enable cross-account issuance and renewals. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/userguide/pca-rbp.html\&quot;&gt;Using a Resource Based Policy with Amazon Web Services Private CA&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListPermissionsRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_tags

    Lists the tags, if any, that are associated with your private CA or one that has been shared with you. Tags are labels that you can use to identify and organize your CAs. Each tag consists of a key and an optional value. Call the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_TagCertificateAuthority.html\&quot;&gt;TagCertificateAuthority&lt;/a&gt; action to add one or more tags to your CA. Call the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_UntagCertificateAuthority.html\&quot;&gt;UntagCertificateAuthority&lt;/a&gt; action to remove tags. 

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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListTagsRequest.from_dict(body)
    return web.Response(status=200)


async def put_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_policy

    &lt;p&gt;Attaches a resource-based policy to a private CA. &lt;/p&gt; &lt;p&gt;A policy can also be applied by sharing a private CA through Amazon Web Services Resource Access Manager (RAM). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/userguide/pca-ram.html\&quot;&gt;Attach a Policy for Cross-Account Access&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The policy can be displayed with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetPolicy.html\&quot;&gt;GetPolicy&lt;/a&gt; and removed with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeletePolicy.html\&quot;&gt;DeletePolicy&lt;/a&gt;.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;About Policies&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;A policy grants access on a private CA to an Amazon Web Services customer account, to Amazon Web Services Organizations, or to an Amazon Web Services Organizations unit. Policies are under the control of a CA administrator. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/userguide/pca-rbp.html\&quot;&gt;Using a Resource Based Policy with Amazon Web Services Private CA&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A policy permits a user of Certificate Manager (ACM) to issue ACM certificates signed by a CA in another account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For ACM to manage automatic renewal of these certificates, the ACM user must configure a Service Linked Role (SLR). The SLR allows the ACM service to assume the identity of the user, subject to confirmation against the Amazon Web Services Private CA policy. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/acm/latest/userguide/acm-slr.html\&quot;&gt;Using a Service Linked Role with ACM&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Updates made in Amazon Web Services Resource Manager (RAM) are reflected in policies. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/userguide/pca-ram.html\&quot;&gt;Attach a Policy for Cross-Account Access&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = PutPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def restore_certificate_authority(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """restore_certificate_authority

    Restores a certificate authority (CA) that is in the &lt;code&gt;DELETED&lt;/code&gt; state. You can restore a CA during the period that you defined in the &lt;b&gt;PermanentDeletionTimeInDays&lt;/b&gt; parameter of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeleteCertificateAuthority.html\&quot;&gt;DeleteCertificateAuthority&lt;/a&gt; action. Currently, you can specify 7 to 30 days. If you did not specify a &lt;b&gt;PermanentDeletionTimeInDays&lt;/b&gt; value, by default you can restore the CA at any time in a 30 day period. You can check the time remaining in the restoration period of a private CA in the &lt;code&gt;DELETED&lt;/code&gt; state by calling the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_DescribeCertificateAuthority.html\&quot;&gt;DescribeCertificateAuthority&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListCertificateAuthorities.html\&quot;&gt;ListCertificateAuthorities&lt;/a&gt; actions. The status of a restored CA is set to its pre-deletion status when the &lt;b&gt;RestoreCertificateAuthority&lt;/b&gt; action returns. To change its status to &lt;code&gt;ACTIVE&lt;/code&gt;, call the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_UpdateCertificateAuthority.html\&quot;&gt;UpdateCertificateAuthority&lt;/a&gt; action. If the private CA was in the &lt;code&gt;PENDING_CERTIFICATE&lt;/code&gt; state at deletion, you must use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_ImportCertificateAuthorityCertificate.html\&quot;&gt;ImportCertificateAuthorityCertificate&lt;/a&gt; action to import a certificate authority into the private CA before it can be activated. You cannot restore a CA after the restoration period has ended.

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
    body = RestoreCertificateAuthorityRequest.from_dict(body)
    return web.Response(status=200)


async def revoke_certificate(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """revoke_certificate

    &lt;p&gt;Revokes a certificate that was issued inside Amazon Web Services Private CA. If you enable a certificate revocation list (CRL) when you create or update your private CA, information about the revoked certificates will be included in the CRL. Amazon Web Services Private CA writes the CRL to an S3 bucket that you specify. A CRL is typically updated approximately 30 minutes after a certificate is revoked. If for any reason the CRL update fails, Amazon Web Services Private CA attempts makes further attempts every 15 minutes. With Amazon CloudWatch, you can create alarms for the metrics &lt;code&gt;CRLGenerated&lt;/code&gt; and &lt;code&gt;MisconfiguredCRLBucket&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/userguide/PcaCloudWatch.html\&quot;&gt;Supported CloudWatch Metrics&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Both Amazon Web Services Private CA and the IAM principal must have permission to write to the S3 bucket that you specify. If the IAM principal making the call does not have permission to write to the bucket, then an exception is thrown. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/userguide/crl-planning.html#s3-policies\&quot;&gt;Access policies for CRLs in Amazon S3&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Amazon Web Services Private CA also writes revocation information to the audit report. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthorityAuditReport.html\&quot;&gt;CreateCertificateAuthorityAuditReport&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You cannot revoke a root CA self-signed certificate.&lt;/p&gt; &lt;/note&gt;

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
    body = RevokeCertificateRequest.from_dict(body)
    return web.Response(status=200)


async def tag_certificate_authority(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_certificate_authority

    &lt;p&gt;Adds one or more tags to your private CA. Tags are labels that you can use to identify and organize your Amazon Web Services resources. Each tag consists of a key and an optional value. You specify the private CA on input by its Amazon Resource Name (ARN). You specify the tag by using a key-value pair. You can apply a tag to just one private CA if you want to identify a specific characteristic of that CA, or you can apply the same tag to multiple private CAs if you want to filter for a common relationship among those CAs. To remove one or more tags, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_UntagCertificateAuthority.html\&quot;&gt;UntagCertificateAuthority&lt;/a&gt; action. Call the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListTags.html\&quot;&gt;ListTags&lt;/a&gt; action to see what tags are associated with your CA. &lt;/p&gt; &lt;note&gt; &lt;p&gt;To attach tags to a private CA during the creation procedure, a CA administrator must first associate an inline IAM policy with the &lt;code&gt;CreateCertificateAuthority&lt;/code&gt; action and explicitly allow tagging. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/userguide/auth-InlinePolicies.html#policy-tag-ca\&quot;&gt;Attaching tags to a CA at the time of creation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = TagCertificateAuthorityRequest.from_dict(body)
    return web.Response(status=200)


async def untag_certificate_authority(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_certificate_authority

    Remove one or more tags from your private CA. A tag consists of a key-value pair. If you do not specify the value portion of the tag when calling this action, the tag will be removed regardless of value. If you specify a value, the tag is removed only if it is associated with the specified value. To add tags to a private CA, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_TagCertificateAuthority.html\&quot;&gt;TagCertificateAuthority&lt;/a&gt;. Call the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListTags.html\&quot;&gt;ListTags&lt;/a&gt; action to see what tags are associated with your CA. 

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
    body = UntagCertificateAuthorityRequest.from_dict(body)
    return web.Response(status=200)


async def update_certificate_authority(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_certificate_authority

    &lt;p&gt;Updates the status or configuration of a private certificate authority (CA). Your private CA must be in the &lt;code&gt;ACTIVE&lt;/code&gt; or &lt;code&gt;DISABLED&lt;/code&gt; state before you can update it. You can disable a private CA that is in the &lt;code&gt;ACTIVE&lt;/code&gt; state or make a CA that is in the &lt;code&gt;DISABLED&lt;/code&gt; state active again.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Both Amazon Web Services Private CA and the IAM principal must have permission to write to the S3 bucket that you specify. If the IAM principal making the call does not have permission to write to the bucket, then an exception is thrown. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/userguide/crl-planning.html#s3-policies\&quot;&gt;Access policies for CRLs in Amazon S3&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = UpdateCertificateAuthorityRequest.from_dict(body)
    return web.Response(status=200)
