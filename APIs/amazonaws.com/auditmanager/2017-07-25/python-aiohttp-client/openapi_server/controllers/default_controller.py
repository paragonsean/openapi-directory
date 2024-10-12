from typing import List, Dict
from aiohttp import web

from openapi_server.models.associate_assessment_report_evidence_folder_request import AssociateAssessmentReportEvidenceFolderRequest
from openapi_server.models.batch_associate_assessment_report_evidence_request import BatchAssociateAssessmentReportEvidenceRequest
from openapi_server.models.batch_associate_assessment_report_evidence_response import BatchAssociateAssessmentReportEvidenceResponse
from openapi_server.models.batch_create_delegation_by_assessment_request import BatchCreateDelegationByAssessmentRequest
from openapi_server.models.batch_create_delegation_by_assessment_response import BatchCreateDelegationByAssessmentResponse
from openapi_server.models.batch_delete_delegation_by_assessment_request import BatchDeleteDelegationByAssessmentRequest
from openapi_server.models.batch_delete_delegation_by_assessment_response import BatchDeleteDelegationByAssessmentResponse
from openapi_server.models.batch_disassociate_assessment_report_evidence_response import BatchDisassociateAssessmentReportEvidenceResponse
from openapi_server.models.batch_import_evidence_to_assessment_control_request import BatchImportEvidenceToAssessmentControlRequest
from openapi_server.models.batch_import_evidence_to_assessment_control_response import BatchImportEvidenceToAssessmentControlResponse
from openapi_server.models.create_assessment_framework_request import CreateAssessmentFrameworkRequest
from openapi_server.models.create_assessment_framework_response import CreateAssessmentFrameworkResponse
from openapi_server.models.create_assessment_report_request import CreateAssessmentReportRequest
from openapi_server.models.create_assessment_report_response import CreateAssessmentReportResponse
from openapi_server.models.create_assessment_request import CreateAssessmentRequest
from openapi_server.models.create_assessment_response import CreateAssessmentResponse
from openapi_server.models.create_control_request import CreateControlRequest
from openapi_server.models.create_control_response import CreateControlResponse
from openapi_server.models.deregister_account_response import DeregisterAccountResponse
from openapi_server.models.deregister_organization_admin_account_request import DeregisterOrganizationAdminAccountRequest
from openapi_server.models.disassociate_assessment_report_evidence_folder_request import DisassociateAssessmentReportEvidenceFolderRequest
from openapi_server.models.get_account_status_response import GetAccountStatusResponse
from openapi_server.models.get_assessment_framework_response import GetAssessmentFrameworkResponse
from openapi_server.models.get_assessment_report_url_response import GetAssessmentReportUrlResponse
from openapi_server.models.get_assessment_response import GetAssessmentResponse
from openapi_server.models.get_change_logs_response import GetChangeLogsResponse
from openapi_server.models.get_control_response import GetControlResponse
from openapi_server.models.get_delegations_response import GetDelegationsResponse
from openapi_server.models.get_evidence_by_evidence_folder_response import GetEvidenceByEvidenceFolderResponse
from openapi_server.models.get_evidence_file_upload_url_response import GetEvidenceFileUploadUrlResponse
from openapi_server.models.get_evidence_folder_response import GetEvidenceFolderResponse
from openapi_server.models.get_evidence_folders_by_assessment_control_response import GetEvidenceFoldersByAssessmentControlResponse
from openapi_server.models.get_evidence_folders_by_assessment_response import GetEvidenceFoldersByAssessmentResponse
from openapi_server.models.get_evidence_response import GetEvidenceResponse
from openapi_server.models.get_insights_by_assessment_response import GetInsightsByAssessmentResponse
from openapi_server.models.get_insights_response import GetInsightsResponse
from openapi_server.models.get_organization_admin_account_response import GetOrganizationAdminAccountResponse
from openapi_server.models.get_services_in_scope_response import GetServicesInScopeResponse
from openapi_server.models.get_settings_response import GetSettingsResponse
from openapi_server.models.list_assessment_control_insights_by_control_domain_response import ListAssessmentControlInsightsByControlDomainResponse
from openapi_server.models.list_assessment_framework_share_requests_response import ListAssessmentFrameworkShareRequestsResponse
from openapi_server.models.list_assessment_frameworks_response import ListAssessmentFrameworksResponse
from openapi_server.models.list_assessment_reports_response import ListAssessmentReportsResponse
from openapi_server.models.list_assessments_response import ListAssessmentsResponse
from openapi_server.models.list_control_domain_insights_by_assessment_response import ListControlDomainInsightsByAssessmentResponse
from openapi_server.models.list_control_domain_insights_response import ListControlDomainInsightsResponse
from openapi_server.models.list_control_insights_by_control_domain_response import ListControlInsightsByControlDomainResponse
from openapi_server.models.list_controls_response import ListControlsResponse
from openapi_server.models.list_keywords_for_data_source_response import ListKeywordsForDataSourceResponse
from openapi_server.models.list_notifications_response import ListNotificationsResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.register_account_request import RegisterAccountRequest
from openapi_server.models.register_account_response import RegisterAccountResponse
from openapi_server.models.register_organization_admin_account_request import RegisterOrganizationAdminAccountRequest
from openapi_server.models.register_organization_admin_account_response import RegisterOrganizationAdminAccountResponse
from openapi_server.models.start_assessment_framework_share_request import StartAssessmentFrameworkShareRequest
from openapi_server.models.start_assessment_framework_share_response import StartAssessmentFrameworkShareResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_assessment_control_request import UpdateAssessmentControlRequest
from openapi_server.models.update_assessment_control_response import UpdateAssessmentControlResponse
from openapi_server.models.update_assessment_control_set_status_request import UpdateAssessmentControlSetStatusRequest
from openapi_server.models.update_assessment_control_set_status_response import UpdateAssessmentControlSetStatusResponse
from openapi_server.models.update_assessment_framework_request import UpdateAssessmentFrameworkRequest
from openapi_server.models.update_assessment_framework_response import UpdateAssessmentFrameworkResponse
from openapi_server.models.update_assessment_framework_share_request import UpdateAssessmentFrameworkShareRequest
from openapi_server.models.update_assessment_framework_share_response import UpdateAssessmentFrameworkShareResponse
from openapi_server.models.update_assessment_request import UpdateAssessmentRequest
from openapi_server.models.update_assessment_response import UpdateAssessmentResponse
from openapi_server.models.update_assessment_status_request import UpdateAssessmentStatusRequest
from openapi_server.models.update_assessment_status_response import UpdateAssessmentStatusResponse
from openapi_server.models.update_control_request import UpdateControlRequest
from openapi_server.models.update_control_response import UpdateControlResponse
from openapi_server.models.update_settings_request import UpdateSettingsRequest
from openapi_server.models.update_settings_response import UpdateSettingsResponse
from openapi_server.models.validate_assessment_report_integrity_request import ValidateAssessmentReportIntegrityRequest
from openapi_server.models.validate_assessment_report_integrity_response import ValidateAssessmentReportIntegrityResponse
from openapi_server import util


async def associate_assessment_report_evidence_folder(request: web.Request, assessment_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_assessment_report_evidence_folder

     Associates an evidence folder to an assessment report in an Audit Manager assessment. 

    :param assessment_id:  The identifier for the assessment. 
    :type assessment_id: str
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
    body = AssociateAssessmentReportEvidenceFolderRequest.from_dict(body)
    return web.Response(status=200)


async def batch_associate_assessment_report_evidence(request: web.Request, assessment_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_associate_assessment_report_evidence

     Associates a list of evidence to an assessment report in an Audit Manager assessment. 

    :param assessment_id:  The identifier for the assessment. 
    :type assessment_id: str
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
    body = BatchAssociateAssessmentReportEvidenceRequest.from_dict(body)
    return web.Response(status=200)


async def batch_create_delegation_by_assessment(request: web.Request, assessment_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_create_delegation_by_assessment

     Creates a batch of delegations for an assessment in Audit Manager. 

    :param assessment_id:  The identifier for the assessment. 
    :type assessment_id: str
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
    body = BatchCreateDelegationByAssessmentRequest.from_dict(body)
    return web.Response(status=200)


async def batch_delete_delegation_by_assessment(request: web.Request, assessment_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_delete_delegation_by_assessment

     Deletes a batch of delegations for an assessment in Audit Manager. 

    :param assessment_id:  The identifier for the assessment. 
    :type assessment_id: str
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
    body = BatchDeleteDelegationByAssessmentRequest.from_dict(body)
    return web.Response(status=200)


async def batch_disassociate_assessment_report_evidence(request: web.Request, assessment_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_disassociate_assessment_report_evidence

     Disassociates a list of evidence from an assessment report in Audit Manager. 

    :param assessment_id:  The identifier for the assessment. 
    :type assessment_id: str
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
    body = BatchAssociateAssessmentReportEvidenceRequest.from_dict(body)
    return web.Response(status=200)


async def batch_import_evidence_to_assessment_control(request: web.Request, assessment_id, control_set_id, control_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_import_evidence_to_assessment_control

    &lt;p&gt;Adds one or more pieces of evidence to a control in an Audit Manager assessment. &lt;/p&gt; &lt;p&gt;You can import manual evidence from any S3 bucket by specifying the S3 URI of the object. You can also upload a file from your browser, or enter plain text in response to a risk assessment question. &lt;/p&gt; &lt;p&gt;The following restrictions apply to this action:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;manualEvidence&lt;/code&gt; can be only one of the following: &lt;code&gt;evidenceFileName&lt;/code&gt;, &lt;code&gt;s3ResourcePath&lt;/code&gt;, or &lt;code&gt;textResponse&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Maximum size of an individual evidence file: 100 MB&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Number of daily manual evidence uploads per control: 100&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Supported file formats: See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/userguide/upload-evidence.html#supported-manual-evidence-files\&quot;&gt;Supported file types for manual evidence&lt;/a&gt; in the &lt;i&gt;Audit Manager User Guide&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information about Audit Manager service restrictions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/userguide/service-quotas.html\&quot;&gt;Quotas and restrictions for Audit Manager&lt;/a&gt;.&lt;/p&gt;

    :param assessment_id:  The identifier for the assessment. 
    :type assessment_id: str
    :param control_set_id:  The identifier for the control set. 
    :type control_set_id: str
    :param control_id:  The identifier for the control. 
    :type control_id: str
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
    body = BatchImportEvidenceToAssessmentControlRequest.from_dict(body)
    return web.Response(status=200)


async def create_assessment(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_assessment

     Creates an assessment in Audit Manager. 

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
    body = CreateAssessmentRequest.from_dict(body)
    return web.Response(status=200)


async def create_assessment_framework(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_assessment_framework

     Creates a custom framework in Audit Manager. 

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
    body = CreateAssessmentFrameworkRequest.from_dict(body)
    return web.Response(status=200)


async def create_assessment_report(request: web.Request, assessment_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_assessment_report

     Creates an assessment report for the specified assessment. 

    :param assessment_id:  The identifier for the assessment. 
    :type assessment_id: str
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
    body = CreateAssessmentReportRequest.from_dict(body)
    return web.Response(status=200)


async def create_control(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_control

     Creates a new custom control in Audit Manager. 

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
    body = CreateControlRequest.from_dict(body)
    return web.Response(status=200)


async def delete_assessment(request: web.Request, assessment_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_assessment

     Deletes an assessment in Audit Manager. 

    :param assessment_id:  The identifier for the assessment. 
    :type assessment_id: str
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
    return web.Response(status=200)


async def delete_assessment_framework(request: web.Request, framework_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_assessment_framework

     Deletes a custom framework in Audit Manager. 

    :param framework_id:  The identifier for the custom framework. 
    :type framework_id: str
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
    return web.Response(status=200)


async def delete_assessment_framework_share(request: web.Request, request_id, request_type, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_assessment_framework_share

     Deletes a share request for a custom framework in Audit Manager. 

    :param request_id: The unique identifier for the share request to be deleted.
    :type request_id: str
    :param request_type: Specifies whether the share request is a sent request or a received request.
    :type request_type: str
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
    return web.Response(status=200)


async def delete_assessment_report(request: web.Request, assessment_id, assessment_report_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_assessment_report

    &lt;p&gt;Deletes an assessment report in Audit Manager. &lt;/p&gt; &lt;p&gt;When you run the &lt;code&gt;DeleteAssessmentReport&lt;/code&gt; operation, Audit Manager attempts to delete the following data:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;The specified assessment report that’s stored in your S3 bucket&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The associated metadata that’s stored in Audit Manager&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;If Audit Manager can’t access the assessment report in your S3 bucket, the report isn’t deleted. In this event, the &lt;code&gt;DeleteAssessmentReport&lt;/code&gt; operation doesn’t fail. Instead, it proceeds to delete the associated metadata only. You must then delete the assessment report from the S3 bucket yourself. &lt;/p&gt; &lt;p&gt;This scenario happens when Audit Manager receives a &lt;code&gt;403 (Forbidden)&lt;/code&gt; or &lt;code&gt;404 (Not Found)&lt;/code&gt; error from Amazon S3. To avoid this, make sure that your S3 bucket is available, and that you configured the correct permissions for Audit Manager to delete resources in your S3 bucket. For an example permissions policy that you can use, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/userguide/security_iam_id-based-policy-examples.html#full-administrator-access-assessment-report-destination\&quot;&gt;Assessment report destination permissions&lt;/a&gt; in the &lt;i&gt;Audit Manager User Guide&lt;/i&gt;. For information about the issues that could cause a &lt;code&gt;403 (Forbidden)&lt;/code&gt; or &lt;code&gt;404 (Not Found&lt;/code&gt;) error from Amazon S3, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#ErrorCodeList\&quot;&gt;List of Error Codes&lt;/a&gt; in the &lt;i&gt;Amazon Simple Storage Service API Reference&lt;/i&gt;. &lt;/p&gt;

    :param assessment_id:  The unique identifier for the assessment. 
    :type assessment_id: str
    :param assessment_report_id:  The unique identifier for the assessment report. 
    :type assessment_report_id: str
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
    return web.Response(status=200)


async def delete_control(request: web.Request, control_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_control

    &lt;p&gt; Deletes a custom control in Audit Manager. &lt;/p&gt; &lt;important&gt; &lt;p&gt;When you invoke this operation, the custom control is deleted from any frameworks or assessments that it’s currently part of. As a result, Audit Manager will stop collecting evidence for that custom control in all of your assessments. This includes assessments that you previously created before you deleted the custom control.&lt;/p&gt; &lt;/important&gt;

    :param control_id:  The unique identifier for the control. 
    :type control_id: str
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
    return web.Response(status=200)


async def deregister_account(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """deregister_account

    &lt;p&gt; Deregisters an account in Audit Manager. &lt;/p&gt; &lt;note&gt; &lt;p&gt;Before you deregister, you can use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateSettings.html\&quot;&gt;UpdateSettings&lt;/a&gt; API operation to set your preferred data retention policy. By default, Audit Manager retains your data. If you want to delete your data, you can use the &lt;code&gt;DeregistrationPolicy&lt;/code&gt; attribute to request the deletion of your data. &lt;/p&gt; &lt;p&gt;For more information about data retention, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/userguide/data-protection.html\&quot;&gt;Data Protection&lt;/a&gt; in the &lt;i&gt;Audit Manager User Guide&lt;/i&gt;. &lt;/p&gt; &lt;/note&gt;

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
    return web.Response(status=200)


async def deregister_organization_admin_account(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """deregister_organization_admin_account

    &lt;p&gt;Removes the specified Amazon Web Services account as a delegated administrator for Audit Manager. &lt;/p&gt; &lt;p&gt;When you remove a delegated administrator from your Audit Manager settings, you continue to have access to the evidence that you previously collected under that account. This is also the case when you deregister a delegated administrator from Organizations. However, Audit Manager stops collecting and attaching evidence to that delegated administrator account moving forward.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Keep in mind the following cleanup task if you use evidence finder:&lt;/p&gt; &lt;p&gt;Before you use your management account to remove a delegated administrator, make sure that the current delegated administrator account signs in to Audit Manager and disables evidence finder first. Disabling evidence finder automatically deletes the event data store that was created in their account when they enabled evidence finder. If this task isn’t completed, the event data store remains in their account. In this case, we recommend that the original delegated administrator goes to CloudTrail Lake and manually &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-eds-disable-termination.html\&quot;&gt;deletes the event data store&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This cleanup task is necessary to ensure that you don&#39;t end up with multiple event data stores. Audit Manager ignores an unused event data store after you remove or change a delegated administrator account. However, the unused event data store continues to incur storage costs from CloudTrail Lake if you don&#39;t delete it.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;When you deregister a delegated administrator account for Audit Manager, the data for that account isn’t deleted. If you want to delete resource data for a delegated administrator account, you must perform that task separately before you deregister the account. Either, you can do this in the Audit Manager console. Or, you can use one of the delete API operations that are provided by Audit Manager. &lt;/p&gt; &lt;p&gt;To delete your Audit Manager resource data, see the following instructions: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeleteAssessment.html\&quot;&gt;DeleteAssessment&lt;/a&gt; (see also: &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/userguide/delete-assessment.html\&quot;&gt;Deleting an assessment&lt;/a&gt; in the &lt;i&gt;Audit Manager User Guide&lt;/i&gt;)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeleteAssessmentFramework.html\&quot;&gt;DeleteAssessmentFramework&lt;/a&gt; (see also: &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/userguide/delete-custom-framework.html\&quot;&gt;Deleting a custom framework&lt;/a&gt; in the &lt;i&gt;Audit Manager User Guide&lt;/i&gt;)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeleteAssessmentFrameworkShare.html\&quot;&gt;DeleteAssessmentFrameworkShare&lt;/a&gt; (see also: &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/userguide/deleting-shared-framework-requests.html\&quot;&gt;Deleting a share request&lt;/a&gt; in the &lt;i&gt;Audit Manager User Guide&lt;/i&gt;)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeleteAssessmentReport.html\&quot;&gt;DeleteAssessmentReport&lt;/a&gt; (see also: &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/userguide/generate-assessment-report.html#delete-assessment-report-steps\&quot;&gt;Deleting an assessment report&lt;/a&gt; in the &lt;i&gt;Audit Manager User Guide&lt;/i&gt;)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeleteControl.html\&quot;&gt;DeleteControl&lt;/a&gt; (see also: &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/userguide/delete-controls.html\&quot;&gt;Deleting a custom control&lt;/a&gt; in the &lt;i&gt;Audit Manager User Guide&lt;/i&gt;)&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;At this time, Audit Manager doesn&#39;t provide an option to delete evidence for a specific delegated administrator. Instead, when your management account deregisters Audit Manager, we perform a cleanup for the current delegated administrator account at the time of deregistration.&lt;/p&gt;

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
    body = DeregisterOrganizationAdminAccountRequest.from_dict(body)
    return web.Response(status=200)


async def disassociate_assessment_report_evidence_folder(request: web.Request, assessment_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_assessment_report_evidence_folder

     Disassociates an evidence folder from the specified assessment report in Audit Manager. 

    :param assessment_id:  The unique identifier for the assessment. 
    :type assessment_id: str
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
    body = DisassociateAssessmentReportEvidenceFolderRequest.from_dict(body)
    return web.Response(status=200)


async def get_account_status(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_account_status

     Gets the registration status of an account in Audit Manager. 

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
    return web.Response(status=200)


async def get_assessment(request: web.Request, assessment_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_assessment

    Gets information about a specified assessment. 

    :param assessment_id: The unique identifier for the assessment. 
    :type assessment_id: str
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
    return web.Response(status=200)


async def get_assessment_framework(request: web.Request, framework_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_assessment_framework

    Gets information about a specified framework.

    :param framework_id:  The identifier for the framework. 
    :type framework_id: str
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
    return web.Response(status=200)


async def get_assessment_report_url(request: web.Request, assessment_report_id, assessment_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_assessment_report_url

     Gets the URL of an assessment report in Audit Manager. 

    :param assessment_report_id:  The unique identifier for the assessment report. 
    :type assessment_report_id: str
    :param assessment_id:  The unique identifier for the assessment. 
    :type assessment_id: str
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
    return web.Response(status=200)


async def get_change_logs(request: web.Request, assessment_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, control_set_id=None, control_id=None, next_token=None, max_results=None) -> web.Response:
    """get_change_logs

     Gets a list of changelogs from Audit Manager. 

    :param assessment_id: The unique identifier for the assessment. 
    :type assessment_id: str
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
    :param control_set_id:  The unique identifier for the control set. 
    :type control_set_id: str
    :param control_id:  The unique identifier for the control. 
    :type control_id: str
    :param next_token:  The pagination token that&#39;s used to fetch the next set of results. 
    :type next_token: str
    :param max_results: Represents the maximum number of results on a page or for an API request call. 
    :type max_results: int

    """
    return web.Response(status=200)


async def get_control(request: web.Request, control_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_control

     Gets information about a specified control.

    :param control_id:  The identifier for the control. 
    :type control_id: str
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
    return web.Response(status=200)


async def get_delegations(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """get_delegations

     Gets a list of delegations from an audit owner to a delegate. 

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
    :param next_token:  The pagination token that&#39;s used to fetch the next set of results. 
    :type next_token: str
    :param max_results:  Represents the maximum number of results on a page or for an API request call. 
    :type max_results: int

    """
    return web.Response(status=200)


async def get_evidence(request: web.Request, assessment_id, control_set_id, evidence_folder_id, evidence_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_evidence

     Gets information about a specified evidence item.

    :param assessment_id:  The unique identifier for the assessment. 
    :type assessment_id: str
    :param control_set_id:  The unique identifier for the control set. 
    :type control_set_id: str
    :param evidence_folder_id:  The unique identifier for the folder that the evidence is stored in. 
    :type evidence_folder_id: str
    :param evidence_id:  The unique identifier for the evidence. 
    :type evidence_id: str
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
    return web.Response(status=200)


async def get_evidence_by_evidence_folder(request: web.Request, assessment_id, control_set_id, evidence_folder_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """get_evidence_by_evidence_folder

     Gets all evidence from a specified evidence folder in Audit Manager. 

    :param assessment_id:  The identifier for the assessment. 
    :type assessment_id: str
    :param control_set_id:  The identifier for the control set. 
    :type control_set_id: str
    :param evidence_folder_id:  The unique identifier for the folder that the evidence is stored in. 
    :type evidence_folder_id: str
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
    :param next_token:  The pagination token that&#39;s used to fetch the next set of results. 
    :type next_token: str
    :param max_results:  Represents the maximum number of results on a page or for an API request call. 
    :type max_results: int

    """
    return web.Response(status=200)


async def get_evidence_file_upload_url(request: web.Request, file_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_evidence_file_upload_url

    &lt;p&gt;Creates a presigned Amazon S3 URL that can be used to upload a file as manual evidence. For instructions on how to use this operation, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/userguide/upload-evidence.html#how-to-upload-manual-evidence-files\&quot;&gt;Upload a file from your browser &lt;/a&gt; in the &lt;i&gt;Audit Manager User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;The following restrictions apply to this operation:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Maximum size of an individual evidence file: 100 MB&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Number of daily manual evidence uploads per control: 100&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Supported file formats: See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/userguide/upload-evidence.html#supported-manual-evidence-files\&quot;&gt;Supported file types for manual evidence&lt;/a&gt; in the &lt;i&gt;Audit Manager User Guide&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information about Audit Manager service restrictions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/userguide/service-quotas.html\&quot;&gt;Quotas and restrictions for Audit Manager&lt;/a&gt;.&lt;/p&gt;

    :param file_name: The file that you want to upload. For a list of supported file formats, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/userguide/upload-evidence.html#supported-manual-evidence-files\&quot;&gt;Supported file types for manual evidence&lt;/a&gt; in the &lt;i&gt;Audit Manager User Guide&lt;/i&gt;.
    :type file_name: str
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
    return web.Response(status=200)


async def get_evidence_folder(request: web.Request, assessment_id, control_set_id, evidence_folder_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_evidence_folder

     Gets an evidence folder from a specified assessment in Audit Manager. 

    :param assessment_id:  The unique identifier for the assessment. 
    :type assessment_id: str
    :param control_set_id:  The unique identifier for the control set. 
    :type control_set_id: str
    :param evidence_folder_id:  The unique identifier for the folder that the evidence is stored in. 
    :type evidence_folder_id: str
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
    return web.Response(status=200)


async def get_evidence_folders_by_assessment(request: web.Request, assessment_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """get_evidence_folders_by_assessment

     Gets the evidence folders from a specified assessment in Audit Manager. 

    :param assessment_id:  The unique identifier for the assessment. 
    :type assessment_id: str
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
    :param next_token:  The pagination token that&#39;s used to fetch the next set of results. 
    :type next_token: str
    :param max_results:  Represents the maximum number of results on a page or for an API request call. 
    :type max_results: int

    """
    return web.Response(status=200)


async def get_evidence_folders_by_assessment_control(request: web.Request, assessment_id, control_set_id, control_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """get_evidence_folders_by_assessment_control

     Gets a list of evidence folders that are associated with a specified control in an Audit Manager assessment. 

    :param assessment_id:  The identifier for the assessment. 
    :type assessment_id: str
    :param control_set_id:  The identifier for the control set. 
    :type control_set_id: str
    :param control_id:  The identifier for the control. 
    :type control_id: str
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
    :param next_token:  The pagination token that&#39;s used to fetch the next set of results. 
    :type next_token: str
    :param max_results:  Represents the maximum number of results on a page or for an API request call. 
    :type max_results: int

    """
    return web.Response(status=200)


async def get_insights(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_insights

    Gets the latest analytics data for all your current active assessments. 

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
    return web.Response(status=200)


async def get_insights_by_assessment(request: web.Request, assessment_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_insights_by_assessment

    Gets the latest analytics data for a specific active assessment. 

    :param assessment_id: The unique identifier for the assessment. 
    :type assessment_id: str
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
    return web.Response(status=200)


async def get_organization_admin_account(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_organization_admin_account

     Gets the name of the delegated Amazon Web Services administrator account for a specified organization. 

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
    return web.Response(status=200)


async def get_services_in_scope(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_services_in_scope

    Gets a list of all of the Amazon Web Services that you can choose to include in your assessment. When you &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_CreateAssessment.html\&quot;&gt;create an assessment&lt;/a&gt;, specify which of these services you want to include to narrow the assessment&#39;s &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_Scope.html\&quot;&gt;scope&lt;/a&gt;.

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
    return web.Response(status=200)


async def get_settings(request: web.Request, attribute, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_settings

     Gets the settings for a specified Amazon Web Services account. 

    :param attribute:  The list of setting attribute enum values. 
    :type attribute: str
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
    return web.Response(status=200)


async def list_assessment_control_insights_by_control_domain(request: web.Request, control_domain_id, assessment_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_assessment_control_insights_by_control_domain

    &lt;p&gt;Lists the latest analytics data for controls within a specific control domain and a specific active assessment.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Control insights are listed only if the control belongs to the control domain and assessment that was specified. Moreover, the control must have collected evidence on the &lt;code&gt;lastUpdated&lt;/code&gt; date of &lt;code&gt;controlInsightsByAssessment&lt;/code&gt;. If neither of these conditions are met, no data is listed for that control. &lt;/p&gt; &lt;/note&gt;

    :param control_domain_id: The unique identifier for the control domain. 
    :type control_domain_id: str
    :param assessment_id: The unique identifier for the active assessment. 
    :type assessment_id: str
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
    :param next_token: The pagination token that&#39;s used to fetch the next set of results. 
    :type next_token: str
    :param max_results: Represents the maximum number of results on a page or for an API request call. 
    :type max_results: int

    """
    return web.Response(status=200)


async def list_assessment_framework_share_requests(request: web.Request, request_type, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_assessment_framework_share_requests

     Returns a list of sent or received share requests for custom frameworks in Audit Manager. 

    :param request_type:  Specifies whether the share request is a sent request or a received request.
    :type request_type: str
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
    :param next_token:  The pagination token that&#39;s used to fetch the next set of results. 
    :type next_token: str
    :param max_results:  Represents the maximum number of results on a page or for an API request call. 
    :type max_results: int

    """
    return web.Response(status=200)


async def list_assessment_frameworks(request: web.Request, framework_type, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_assessment_frameworks

     Returns a list of the frameworks that are available in the Audit Manager framework library. 

    :param framework_type:  The type of framework, such as a standard framework or a custom framework. 
    :type framework_type: str
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
    :param next_token:  The pagination token that&#39;s used to fetch the next set of results. 
    :type next_token: str
    :param max_results:  Represents the maximum number of results on a page or for an API request call. 
    :type max_results: int

    """
    return web.Response(status=200)


async def list_assessment_reports(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_assessment_reports

     Returns a list of assessment reports created in Audit Manager. 

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
    :param next_token:  The pagination token that&#39;s used to fetch the next set of results. 
    :type next_token: str
    :param max_results:  Represents the maximum number of results on a page or for an API request call. 
    :type max_results: int

    """
    return web.Response(status=200)


async def list_assessments(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, status=None, next_token=None, max_results=None) -> web.Response:
    """list_assessments

     Returns a list of current and past assessments from Audit Manager. 

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
    :param status:  The current status of the assessment.
    :type status: str
    :param next_token:  The pagination token that&#39;s used to fetch the next set of results. 
    :type next_token: str
    :param max_results:  Represents the maximum number of results on a page or for an API request call. 
    :type max_results: int

    """
    return web.Response(status=200)


async def list_control_domain_insights(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_control_domain_insights

    &lt;p&gt;Lists the latest analytics data for control domains across all of your active assessments. &lt;/p&gt; &lt;note&gt; &lt;p&gt;A control domain is listed only if at least one of the controls within that domain collected evidence on the &lt;code&gt;lastUpdated&lt;/code&gt; date of &lt;code&gt;controlDomainInsights&lt;/code&gt;. If this condition isn’t met, no data is listed for that control domain.&lt;/p&gt; &lt;/note&gt;

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
    :param next_token: The pagination token that&#39;s used to fetch the next set of results. 
    :type next_token: str
    :param max_results: Represents the maximum number of results on a page or for an API request call. 
    :type max_results: int

    """
    return web.Response(status=200)


async def list_control_domain_insights_by_assessment(request: web.Request, assessment_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_control_domain_insights_by_assessment

    &lt;p&gt;Lists analytics data for control domains within a specified active assessment.&lt;/p&gt; &lt;note&gt; &lt;p&gt;A control domain is listed only if at least one of the controls within that domain collected evidence on the &lt;code&gt;lastUpdated&lt;/code&gt; date of &lt;code&gt;controlDomainInsights&lt;/code&gt;. If this condition isn’t met, no data is listed for that domain.&lt;/p&gt; &lt;/note&gt;

    :param assessment_id: The unique identifier for the active assessment. 
    :type assessment_id: str
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
    :param next_token: The pagination token that&#39;s used to fetch the next set of results. 
    :type next_token: str
    :param max_results: Represents the maximum number of results on a page or for an API request call. 
    :type max_results: int

    """
    return web.Response(status=200)


async def list_control_insights_by_control_domain(request: web.Request, control_domain_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_control_insights_by_control_domain

    &lt;p&gt;Lists the latest analytics data for controls within a specific control domain across all active assessments.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Control insights are listed only if the control belongs to the control domain that was specified and the control collected evidence on the &lt;code&gt;lastUpdated&lt;/code&gt; date of &lt;code&gt;controlInsightsMetadata&lt;/code&gt;. If neither of these conditions are met, no data is listed for that control. &lt;/p&gt; &lt;/note&gt;

    :param control_domain_id: The unique identifier for the control domain. 
    :type control_domain_id: str
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
    :param next_token: The pagination token that&#39;s used to fetch the next set of results. 
    :type next_token: str
    :param max_results: Represents the maximum number of results on a page or for an API request call. 
    :type max_results: int

    """
    return web.Response(status=200)


async def list_controls(request: web.Request, control_type, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_controls

     Returns a list of controls from Audit Manager. 

    :param control_type:  The type of control, such as a standard control or a custom control. 
    :type control_type: str
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
    :param next_token:  The pagination token that&#39;s used to fetch the next set of results. 
    :type next_token: str
    :param max_results:  Represents the maximum number of results on a page or for an API request call. 
    :type max_results: int

    """
    return web.Response(status=200)


async def list_keywords_for_data_source(request: web.Request, source, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_keywords_for_data_source

     Returns a list of keywords that are pre-mapped to the specified control data source. 

    :param source:  The control mapping data source that the keywords apply to. 
    :type source: str
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
    :param next_token:  The pagination token that&#39;s used to fetch the next set of results. 
    :type next_token: str
    :param max_results:  Represents the maximum number of results on a page or for an API request call. 
    :type max_results: int

    """
    return web.Response(status=200)


async def list_notifications(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_notifications

     Returns a list of all Audit Manager notifications. 

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
    :param next_token:  The pagination token that&#39;s used to fetch the next set of results. 
    :type next_token: str
    :param max_results:  Represents the maximum number of results on a page or for an API request call. 
    :type max_results: int

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

     Returns a list of tags for the specified resource in Audit Manager. 

    :param resource_arn:  The Amazon Resource Name (ARN) of the resource. 
    :type resource_arn: str
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
    return web.Response(status=200)


async def register_account(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """register_account

     Enables Audit Manager for the specified Amazon Web Services account. 

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
    body = RegisterAccountRequest.from_dict(body)
    return web.Response(status=200)


async def register_organization_admin_account(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """register_organization_admin_account

     Enables an Amazon Web Services account within the organization as the delegated administrator for Audit Manager. 

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
    body = RegisterOrganizationAdminAccountRequest.from_dict(body)
    return web.Response(status=200)


async def start_assessment_framework_share(request: web.Request, framework_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_assessment_framework_share

    &lt;p&gt; Creates a share request for a custom framework in Audit Manager. &lt;/p&gt; &lt;p&gt;The share request specifies a recipient and notifies them that a custom framework is available. Recipients have 120 days to accept or decline the request. If no action is taken, the share request expires.&lt;/p&gt; &lt;p&gt;When you create a share request, Audit Manager stores a snapshot of your custom framework in the US East (N. Virginia) Amazon Web Services Region. Audit Manager also stores a backup of the same snapshot in the US West (Oregon) Amazon Web Services Region.&lt;/p&gt; &lt;p&gt;Audit Manager deletes the snapshot and the backup snapshot when one of the following events occurs:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The sender revokes the share request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The recipient declines the share request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The recipient encounters an error and doesn&#39;t successfully accept the share request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The share request expires before the recipient responds to the request.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;When a sender &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/userguide/framework-sharing.html#framework-sharing-resend\&quot;&gt;resends a share request&lt;/a&gt;, the snapshot is replaced with an updated version that corresponds with the latest version of the custom framework. &lt;/p&gt; &lt;p&gt;When a recipient accepts a share request, the snapshot is replicated into their Amazon Web Services account under the Amazon Web Services Region that was specified in the share request. &lt;/p&gt; &lt;important&gt; &lt;p&gt;When you invoke the &lt;code&gt;StartAssessmentFrameworkShare&lt;/code&gt; API, you are about to share a custom framework with another Amazon Web Services account. You may not share a custom framework that is derived from a standard framework if the standard framework is designated as not eligible for sharing by Amazon Web Services, unless you have obtained permission to do so from the owner of the standard framework. To learn more about which standard frameworks are eligible for sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/userguide/share-custom-framework-concepts-and-terminology.html#eligibility\&quot;&gt;Framework sharing eligibility&lt;/a&gt; in the &lt;i&gt;Audit Manager User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param framework_id:  The unique identifier for the custom framework to be shared. 
    :type framework_id: str
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
    body = StartAssessmentFrameworkShareRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

     Tags the specified resource in Audit Manager. 

    :param resource_arn:  The Amazon Resource Name (ARN) of the resource. 
    :type resource_arn: str
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
    body = TagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, resource_arn, tag_keys, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

     Removes a tag from a resource in Audit Manager. 

    :param resource_arn:  The Amazon Resource Name (ARN) of the specified resource. 
    :type resource_arn: str
    :param tag_keys:  The name or key of the tag. 
    :type tag_keys: List[str]
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
    return web.Response(status=200)


async def update_assessment(request: web.Request, assessment_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_assessment

     Edits an Audit Manager assessment. 

    :param assessment_id:  The unique identifier for the assessment. 
    :type assessment_id: str
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
    body = UpdateAssessmentRequest.from_dict(body)
    return web.Response(status=200)


async def update_assessment_control(request: web.Request, assessment_id, control_set_id, control_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_assessment_control

     Updates a control within an assessment in Audit Manager. 

    :param assessment_id:  The unique identifier for the assessment. 
    :type assessment_id: str
    :param control_set_id:  The unique identifier for the control set. 
    :type control_set_id: str
    :param control_id:  The unique identifier for the control. 
    :type control_id: str
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
    body = UpdateAssessmentControlRequest.from_dict(body)
    return web.Response(status=200)


async def update_assessment_control_set_status(request: web.Request, assessment_id, control_set_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_assessment_control_set_status

     Updates the status of a control set in an Audit Manager assessment. 

    :param assessment_id:  The unique identifier for the assessment. 
    :type assessment_id: str
    :param control_set_id:  The unique identifier for the control set. 
    :type control_set_id: str
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
    body = UpdateAssessmentControlSetStatusRequest.from_dict(body)
    return web.Response(status=200)


async def update_assessment_framework(request: web.Request, framework_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_assessment_framework

     Updates a custom framework in Audit Manager. 

    :param framework_id:  The unique identifier for the framework. 
    :type framework_id: str
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
    body = UpdateAssessmentFrameworkRequest.from_dict(body)
    return web.Response(status=200)


async def update_assessment_framework_share(request: web.Request, request_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_assessment_framework_share

     Updates a share request for a custom framework in Audit Manager. 

    :param request_id:  The unique identifier for the share request. 
    :type request_id: str
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
    body = UpdateAssessmentFrameworkShareRequest.from_dict(body)
    return web.Response(status=200)


async def update_assessment_status(request: web.Request, assessment_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_assessment_status

     Updates the status of an assessment in Audit Manager. 

    :param assessment_id:  The unique identifier for the assessment. 
    :type assessment_id: str
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
    body = UpdateAssessmentStatusRequest.from_dict(body)
    return web.Response(status=200)


async def update_control(request: web.Request, control_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_control

     Updates a custom control in Audit Manager. 

    :param control_id:  The identifier for the control. 
    :type control_id: str
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
    body = UpdateControlRequest.from_dict(body)
    return web.Response(status=200)


async def update_settings(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_settings

     Updates Audit Manager settings for the current account. 

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
    body = UpdateSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def validate_assessment_report_integrity(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """validate_assessment_report_integrity

     Validates the integrity of an assessment report in Audit Manager. 

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
    body = ValidateAssessmentReportIntegrityRequest.from_dict(body)
    return web.Response(status=200)
