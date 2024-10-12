from typing import List, Dict
from aiohttp import web

from openapi_server.models.associate_lenses_request import AssociateLensesRequest
from openapi_server.models.associate_profiles_request import AssociateProfilesRequest
from openapi_server.models.create_lens_share_output import CreateLensShareOutput
from openapi_server.models.create_lens_share_request import CreateLensShareRequest
from openapi_server.models.create_lens_version_output import CreateLensVersionOutput
from openapi_server.models.create_lens_version_request import CreateLensVersionRequest
from openapi_server.models.create_milestone_output import CreateMilestoneOutput
from openapi_server.models.create_milestone_request import CreateMilestoneRequest
from openapi_server.models.create_profile_output import CreateProfileOutput
from openapi_server.models.create_profile_request import CreateProfileRequest
from openapi_server.models.create_profile_share_output import CreateProfileShareOutput
from openapi_server.models.create_workload_output import CreateWorkloadOutput
from openapi_server.models.create_workload_request import CreateWorkloadRequest
from openapi_server.models.create_workload_share_output import CreateWorkloadShareOutput
from openapi_server.models.create_workload_share_request import CreateWorkloadShareRequest
from openapi_server.models.disassociate_profiles_request import DisassociateProfilesRequest
from openapi_server.models.export_lens_output import ExportLensOutput
from openapi_server.models.get_answer_output import GetAnswerOutput
from openapi_server.models.get_consolidated_report_output import GetConsolidatedReportOutput
from openapi_server.models.get_lens_output import GetLensOutput
from openapi_server.models.get_lens_review_output import GetLensReviewOutput
from openapi_server.models.get_lens_review_report_output import GetLensReviewReportOutput
from openapi_server.models.get_lens_version_difference_output import GetLensVersionDifferenceOutput
from openapi_server.models.get_milestone_output import GetMilestoneOutput
from openapi_server.models.get_profile_output import GetProfileOutput
from openapi_server.models.get_profile_template_output import GetProfileTemplateOutput
from openapi_server.models.get_workload_output import GetWorkloadOutput
from openapi_server.models.import_lens_output import ImportLensOutput
from openapi_server.models.import_lens_request import ImportLensRequest
from openapi_server.models.list_answers_output import ListAnswersOutput
from openapi_server.models.list_check_details_output import ListCheckDetailsOutput
from openapi_server.models.list_check_details_request import ListCheckDetailsRequest
from openapi_server.models.list_check_summaries_output import ListCheckSummariesOutput
from openapi_server.models.list_lens_review_improvements_output import ListLensReviewImprovementsOutput
from openapi_server.models.list_lens_reviews_output import ListLensReviewsOutput
from openapi_server.models.list_lens_shares_output import ListLensSharesOutput
from openapi_server.models.list_lenses_output import ListLensesOutput
from openapi_server.models.list_milestones_output import ListMilestonesOutput
from openapi_server.models.list_milestones_request import ListMilestonesRequest
from openapi_server.models.list_notifications_output import ListNotificationsOutput
from openapi_server.models.list_notifications_request import ListNotificationsRequest
from openapi_server.models.list_profile_notifications_output import ListProfileNotificationsOutput
from openapi_server.models.list_profile_shares_output import ListProfileSharesOutput
from openapi_server.models.list_profiles_output import ListProfilesOutput
from openapi_server.models.list_share_invitations_output import ListShareInvitationsOutput
from openapi_server.models.list_tags_for_resource_output import ListTagsForResourceOutput
from openapi_server.models.list_workload_shares_output import ListWorkloadSharesOutput
from openapi_server.models.list_workloads_output import ListWorkloadsOutput
from openapi_server.models.list_workloads_request import ListWorkloadsRequest
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_answer_output import UpdateAnswerOutput
from openapi_server.models.update_answer_request import UpdateAnswerRequest
from openapi_server.models.update_global_settings_request import UpdateGlobalSettingsRequest
from openapi_server.models.update_lens_review_output import UpdateLensReviewOutput
from openapi_server.models.update_lens_review_request import UpdateLensReviewRequest
from openapi_server.models.update_profile_output import UpdateProfileOutput
from openapi_server.models.update_profile_request import UpdateProfileRequest
from openapi_server.models.update_share_invitation_output import UpdateShareInvitationOutput
from openapi_server.models.update_share_invitation_request import UpdateShareInvitationRequest
from openapi_server.models.update_workload_output import UpdateWorkloadOutput
from openapi_server.models.update_workload_request import UpdateWorkloadRequest
from openapi_server.models.update_workload_share_output import UpdateWorkloadShareOutput
from openapi_server.models.update_workload_share_request import UpdateWorkloadShareRequest
from openapi_server.models.upgrade_lens_review_request import UpgradeLensReviewRequest
from openapi_server.models.upgrade_profile_version_request import UpgradeProfileVersionRequest
from openapi_server import util


async def associate_lenses(request: web.Request, workload_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_lenses

    &lt;p&gt;Associate a lens to a workload.&lt;/p&gt; &lt;p&gt;Up to 10 lenses can be associated with a workload in a single API operation. A maximum of 20 lenses can be associated with a workload.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;b&gt;Disclaimer&lt;/b&gt; &lt;/p&gt; &lt;p&gt;By accessing and/or applying custom lenses created by another Amazon Web Services user or account, you acknowledge that custom lenses created by other users and shared with you are Third Party Content as defined in the Amazon Web Services Customer Agreement. &lt;/p&gt; &lt;/note&gt;

    :param workload_id: 
    :type workload_id: str
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
    body = AssociateLensesRequest.from_dict(body)
    return web.Response(status=200)


async def associate_profiles(request: web.Request, workload_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_profiles

    Associate a profile with a workload.

    :param workload_id: 
    :type workload_id: str
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
    body = AssociateProfilesRequest.from_dict(body)
    return web.Response(status=200)


async def create_lens_share(request: web.Request, lens_alias, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_lens_share

    &lt;p&gt;Create a lens share.&lt;/p&gt; &lt;p&gt;The owner of a lens can share it with other Amazon Web Services accounts, users, an organization, and organizational units (OUs) in the same Amazon Web Services Region. Lenses provided by Amazon Web Services (Amazon Web Services Official Content) cannot be shared.&lt;/p&gt; &lt;p&gt; Shared access to a lens is not removed until the lens invitation is deleted.&lt;/p&gt; &lt;p&gt;If you share a lens with an organization or OU, all accounts in the organization or OU are granted access to the lens.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-sharing.html\&quot;&gt;Sharing a custom lens&lt;/a&gt; in the &lt;i&gt;Well-Architected Tool User Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;b&gt;Disclaimer&lt;/b&gt; &lt;/p&gt; &lt;p&gt;By sharing your custom lenses with other Amazon Web Services accounts, you acknowledge that Amazon Web Services will make your custom lenses available to those other accounts. Those other accounts may continue to access and use your shared custom lenses even if you delete the custom lenses from your own Amazon Web Services account or terminate your Amazon Web Services account.&lt;/p&gt; &lt;/note&gt;

    :param lens_alias: 
    :type lens_alias: str
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
    body = CreateLensShareRequest.from_dict(body)
    return web.Response(status=200)


async def create_lens_version(request: web.Request, lens_alias, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_lens_version

    &lt;p&gt;Create a new lens version.&lt;/p&gt; &lt;p&gt;A lens can have up to 100 versions.&lt;/p&gt; &lt;p&gt;Use this operation to publish a new lens version after you have imported a lens. The &lt;code&gt;LensAlias&lt;/code&gt; is used to identify the lens to be published. The owner of a lens can share the lens with other Amazon Web Services accounts and users in the same Amazon Web Services Region. Only the owner of a lens can delete it. &lt;/p&gt;

    :param lens_alias: 
    :type lens_alias: str
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
    body = CreateLensVersionRequest.from_dict(body)
    return web.Response(status=200)


async def create_milestone(request: web.Request, workload_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_milestone

    Create a milestone for an existing workload.

    :param workload_id: 
    :type workload_id: str
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
    body = CreateMilestoneRequest.from_dict(body)
    return web.Response(status=200)


async def create_profile(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_profile

    Create a profile.

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
    body = CreateProfileRequest.from_dict(body)
    return web.Response(status=200)


async def create_profile_share(request: web.Request, profile_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_profile_share

    Create a profile share.

    :param profile_arn: The profile ARN.
    :type profile_arn: str
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
    body = CreateLensShareRequest.from_dict(body)
    return web.Response(status=200)


async def create_workload(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_workload

    &lt;p&gt;Create a new workload.&lt;/p&gt; &lt;p&gt;The owner of a workload can share the workload with other Amazon Web Services accounts, users, an organization, and organizational units (OUs) in the same Amazon Web Services Region. Only the owner of a workload can delete it.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/wellarchitected/latest/userguide/define-workload.html\&quot;&gt;Defining a Workload&lt;/a&gt; in the &lt;i&gt;Well-Architected Tool User Guide&lt;/i&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Either &lt;code&gt;AwsRegions&lt;/code&gt;, &lt;code&gt;NonAwsRegions&lt;/code&gt;, or both must be specified when creating a workload.&lt;/p&gt; &lt;p&gt;You also must specify &lt;code&gt;ReviewOwner&lt;/code&gt;, even though the parameter is listed as not being required in the following section. &lt;/p&gt; &lt;/important&gt;

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
    body = CreateWorkloadRequest.from_dict(body)
    return web.Response(status=200)


async def create_workload_share(request: web.Request, workload_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_workload_share

    &lt;p&gt;Create a workload share.&lt;/p&gt; &lt;p&gt;The owner of a workload can share it with other Amazon Web Services accounts and users in the same Amazon Web Services Region. Shared access to a workload is not removed until the workload invitation is deleted.&lt;/p&gt; &lt;p&gt;If you share a workload with an organization or OU, all accounts in the organization or OU are granted access to the workload.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/wellarchitected/latest/userguide/workloads-sharing.html\&quot;&gt;Sharing a workload&lt;/a&gt; in the &lt;i&gt;Well-Architected Tool User Guide&lt;/i&gt;.&lt;/p&gt;

    :param workload_id: 
    :type workload_id: str
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
    body = CreateWorkloadShareRequest.from_dict(body)
    return web.Response(status=200)


async def delete_lens(request: web.Request, lens_alias, client_request_token, lens_status, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_lens

    &lt;p&gt;Delete an existing lens.&lt;/p&gt; &lt;p&gt;Only the owner of a lens can delete it. After the lens is deleted, Amazon Web Services accounts and users that you shared the lens with can continue to use it, but they will no longer be able to apply it to new workloads. &lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;b&gt;Disclaimer&lt;/b&gt; &lt;/p&gt; &lt;p&gt;By sharing your custom lenses with other Amazon Web Services accounts, you acknowledge that Amazon Web Services will make your custom lenses available to those other accounts. Those other accounts may continue to access and use your shared custom lenses even if you delete the custom lenses from your own Amazon Web Services account or terminate your Amazon Web Services account.&lt;/p&gt; &lt;/note&gt;

    :param lens_alias: 
    :type lens_alias: str
    :param client_request_token: 
    :type client_request_token: str
    :param lens_status: The status of the lens to be deleted.
    :type lens_status: str
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


async def delete_lens_share(request: web.Request, share_id, lens_alias, client_request_token, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_lens_share

    &lt;p&gt;Delete a lens share.&lt;/p&gt; &lt;p&gt;After the lens share is deleted, Amazon Web Services accounts, users, organizations, and organizational units (OUs) that you shared the lens with can continue to use it, but they will no longer be able to apply it to new workloads.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;b&gt;Disclaimer&lt;/b&gt; &lt;/p&gt; &lt;p&gt;By sharing your custom lenses with other Amazon Web Services accounts, you acknowledge that Amazon Web Services will make your custom lenses available to those other accounts. Those other accounts may continue to access and use your shared custom lenses even if you delete the custom lenses from your own Amazon Web Services account or terminate your Amazon Web Services account.&lt;/p&gt; &lt;/note&gt;

    :param share_id: 
    :type share_id: str
    :param lens_alias: 
    :type lens_alias: str
    :param client_request_token: 
    :type client_request_token: str
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


async def delete_profile(request: web.Request, profile_arn, client_request_token, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_profile

    &lt;p&gt;Delete a profile.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;b&gt;Disclaimer&lt;/b&gt; &lt;/p&gt; &lt;p&gt;By sharing your profile with other Amazon Web Services accounts, you acknowledge that Amazon Web Services will make your profile available to those other accounts. Those other accounts may continue to access and use your shared profile even if you delete the profile from your own Amazon Web Services account or terminate your Amazon Web Services account.&lt;/p&gt; &lt;/note&gt;

    :param profile_arn: The profile ARN.
    :type profile_arn: str
    :param client_request_token: 
    :type client_request_token: str
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


async def delete_profile_share(request: web.Request, share_id, profile_arn, client_request_token, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_profile_share

    Delete a profile share.

    :param share_id: 
    :type share_id: str
    :param profile_arn: The profile ARN.
    :type profile_arn: str
    :param client_request_token: 
    :type client_request_token: str
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


async def delete_workload(request: web.Request, workload_id, client_request_token, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_workload

    Delete an existing workload.

    :param workload_id: 
    :type workload_id: str
    :param client_request_token: 
    :type client_request_token: str
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


async def delete_workload_share(request: web.Request, share_id, workload_id, client_request_token, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_workload_share

    Delete a workload share.

    :param share_id: 
    :type share_id: str
    :param workload_id: 
    :type workload_id: str
    :param client_request_token: 
    :type client_request_token: str
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


async def disassociate_lenses(request: web.Request, workload_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_lenses

    &lt;p&gt;Disassociate a lens from a workload.&lt;/p&gt; &lt;p&gt;Up to 10 lenses can be disassociated from a workload in a single API operation.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The Amazon Web Services Well-Architected Framework lens (&lt;code&gt;wellarchitected&lt;/code&gt;) cannot be removed from a workload.&lt;/p&gt; &lt;/note&gt;

    :param workload_id: 
    :type workload_id: str
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
    body = AssociateLensesRequest.from_dict(body)
    return web.Response(status=200)


async def disassociate_profiles(request: web.Request, workload_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_profiles

    Disassociate a profile from a workload.

    :param workload_id: 
    :type workload_id: str
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
    body = DisassociateProfilesRequest.from_dict(body)
    return web.Response(status=200)


async def export_lens(request: web.Request, lens_alias, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, lens_version=None) -> web.Response:
    """export_lens

    &lt;p&gt;Export an existing lens.&lt;/p&gt; &lt;p&gt;Only the owner of a lens can export it. Lenses provided by Amazon Web Services (Amazon Web Services Official Content) cannot be exported.&lt;/p&gt; &lt;p&gt;Lenses are defined in JSON. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-format-specification.html\&quot;&gt;JSON format specification&lt;/a&gt; in the &lt;i&gt;Well-Architected Tool User Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;b&gt;Disclaimer&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Do not include or gather personal identifiable information (PII) of end users or other identifiable individuals in or via your custom lenses. If your custom lens or those shared with you and used in your account do include or collect PII you are responsible for: ensuring that the included PII is processed in accordance with applicable law, providing adequate privacy notices, and obtaining necessary consents for processing such data.&lt;/p&gt; &lt;/note&gt;

    :param lens_alias: 
    :type lens_alias: str
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
    :param lens_version: The lens version to be exported.
    :type lens_version: str

    """
    return web.Response(status=200)


async def get_answer(request: web.Request, workload_id, lens_alias, question_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, milestone_number=None) -> web.Response:
    """get_answer

    Get the answer to a specific question in a workload review.

    :param workload_id: 
    :type workload_id: str
    :param lens_alias: 
    :type lens_alias: str
    :param question_id: 
    :type question_id: str
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
    :param milestone_number: 
    :type milestone_number: int

    """
    return web.Response(status=200)


async def get_consolidated_report(request: web.Request, format, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, include_shared_resources=None, next_token=None, max_results=None) -> web.Response:
    """get_consolidated_report

    &lt;p&gt;Get a consolidated report of your workloads.&lt;/p&gt; &lt;p&gt;You can optionally choose to include workloads that have been shared with you.&lt;/p&gt;

    :param format: &lt;p&gt;The format of the consolidated report.&lt;/p&gt; &lt;p&gt;For &lt;code&gt;PDF&lt;/code&gt;, &lt;code&gt;Base64String&lt;/code&gt; is returned. For &lt;code&gt;JSON&lt;/code&gt;, &lt;code&gt;Metrics&lt;/code&gt; is returned.&lt;/p&gt;
    :type format: str
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
    :param include_shared_resources: Set to &lt;code&gt;true&lt;/code&gt; to have shared resources included in the report.
    :type include_shared_resources: bool
    :param next_token: 
    :type next_token: str
    :param max_results: The maximum number of results to return for this request.
    :type max_results: int

    """
    return web.Response(status=200)


async def get_lens(request: web.Request, lens_alias, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, lens_version=None) -> web.Response:
    """get_lens

    Get an existing lens.

    :param lens_alias: 
    :type lens_alias: str
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
    :param lens_version: The lens version to be retrieved.
    :type lens_version: str

    """
    return web.Response(status=200)


async def get_lens_review(request: web.Request, workload_id, lens_alias, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, milestone_number=None) -> web.Response:
    """get_lens_review

    Get lens review.

    :param workload_id: 
    :type workload_id: str
    :param lens_alias: 
    :type lens_alias: str
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
    :param milestone_number: 
    :type milestone_number: int

    """
    return web.Response(status=200)


async def get_lens_review_report(request: web.Request, workload_id, lens_alias, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, milestone_number=None) -> web.Response:
    """get_lens_review_report

    Get lens review report.

    :param workload_id: 
    :type workload_id: str
    :param lens_alias: 
    :type lens_alias: str
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
    :param milestone_number: 
    :type milestone_number: int

    """
    return web.Response(status=200)


async def get_lens_version_difference(request: web.Request, lens_alias, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, base_lens_version=None, target_lens_version=None) -> web.Response:
    """get_lens_version_difference

    Get lens version differences.

    :param lens_alias: 
    :type lens_alias: str
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
    :param base_lens_version: The base version of the lens.
    :type base_lens_version: str
    :param target_lens_version: The lens version to target a difference for.
    :type target_lens_version: str

    """
    return web.Response(status=200)


async def get_milestone(request: web.Request, workload_id, milestone_number, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_milestone

    Get a milestone for an existing workload.

    :param workload_id: 
    :type workload_id: str
    :param milestone_number: 
    :type milestone_number: int
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


async def get_profile(request: web.Request, profile_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, profile_version=None) -> web.Response:
    """get_profile

    Get profile information.

    :param profile_arn: The profile ARN.
    :type profile_arn: str
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
    :param profile_version: The profile version.
    :type profile_version: str

    """
    return web.Response(status=200)


async def get_profile_template(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_profile_template

    Get profile template.

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


async def get_workload(request: web.Request, workload_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_workload

    Get an existing workload.

    :param workload_id: 
    :type workload_id: str
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


async def import_lens(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """import_lens

    &lt;p&gt;Import a new custom lens or update an existing custom lens.&lt;/p&gt; &lt;p&gt;To update an existing custom lens, specify its ARN as the &lt;code&gt;LensAlias&lt;/code&gt;. If no ARN is specified, a new custom lens is created.&lt;/p&gt; &lt;p&gt;The new or updated lens will have a status of &lt;code&gt;DRAFT&lt;/code&gt;. The lens cannot be applied to workloads or shared with other Amazon Web Services accounts until it&#39;s published with &lt;a&gt;CreateLensVersion&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Lenses are defined in JSON. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-format-specification.html\&quot;&gt;JSON format specification&lt;/a&gt; in the &lt;i&gt;Well-Architected Tool User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;A custom lens cannot exceed 500 KB in size.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;b&gt;Disclaimer&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Do not include or gather personal identifiable information (PII) of end users or other identifiable individuals in or via your custom lenses. If your custom lens or those shared with you and used in your account do include or collect PII you are responsible for: ensuring that the included PII is processed in accordance with applicable law, providing adequate privacy notices, and obtaining necessary consents for processing such data.&lt;/p&gt; &lt;/note&gt;

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
    body = ImportLensRequest.from_dict(body)
    return web.Response(status=200)


async def list_answers(request: web.Request, workload_id, lens_alias, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, pillar_id=None, milestone_number=None, next_token=None, max_results=None, question_priority=None) -> web.Response:
    """list_answers

    List of answers for a particular workload and lens.

    :param workload_id: 
    :type workload_id: str
    :param lens_alias: 
    :type lens_alias: str
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
    :param pillar_id: 
    :type pillar_id: str
    :param milestone_number: 
    :type milestone_number: int
    :param next_token: 
    :type next_token: str
    :param max_results: The maximum number of results to return for this request.
    :type max_results: int
    :param question_priority: The priority of the question.
    :type question_priority: str

    """
    return web.Response(status=200)


async def list_check_details(request: web.Request, workload_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_check_details

    List of Trusted Advisor check details by account related to the workload.

    :param workload_id: 
    :type workload_id: str
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
    body = ListCheckDetailsRequest.from_dict(body)
    return web.Response(status=200)


async def list_check_summaries(request: web.Request, workload_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_check_summaries

    List of Trusted Advisor checks summarized for all accounts related to the workload.

    :param workload_id: 
    :type workload_id: str
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
    body = ListCheckDetailsRequest.from_dict(body)
    return web.Response(status=200)


async def list_lens_review_improvements(request: web.Request, workload_id, lens_alias, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, pillar_id=None, milestone_number=None, next_token=None, max_results=None, question_priority=None) -> web.Response:
    """list_lens_review_improvements

    List lens review improvements.

    :param workload_id: 
    :type workload_id: str
    :param lens_alias: 
    :type lens_alias: str
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
    :param pillar_id: 
    :type pillar_id: str
    :param milestone_number: 
    :type milestone_number: int
    :param next_token: 
    :type next_token: str
    :param max_results: The maximum number of results to return for this request.
    :type max_results: int
    :param question_priority: The priority of the question.
    :type question_priority: str

    """
    return web.Response(status=200)


async def list_lens_reviews(request: web.Request, workload_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, milestone_number=None, next_token=None, max_results=None) -> web.Response:
    """list_lens_reviews

    List lens reviews for a particular workload.

    :param workload_id: 
    :type workload_id: str
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
    :param milestone_number: 
    :type milestone_number: int
    :param next_token: 
    :type next_token: str
    :param max_results: 
    :type max_results: int

    """
    return web.Response(status=200)


async def list_lens_shares(request: web.Request, lens_alias, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, shared_with_prefix=None, next_token=None, max_results=None, status=None) -> web.Response:
    """list_lens_shares

    List the lens shares associated with the lens.

    :param lens_alias: 
    :type lens_alias: str
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
    :param shared_with_prefix: The Amazon Web Services account ID, IAM role, organization ID, or organizational unit (OU) ID with which the lens is shared.
    :type shared_with_prefix: str
    :param next_token: 
    :type next_token: str
    :param max_results: The maximum number of results to return for this request.
    :type max_results: int
    :param status: 
    :type status: str

    """
    return web.Response(status=200)


async def list_lenses(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, lens_type=None, lens_status=None, lens_name=None) -> web.Response:
    """list_lenses

    List the available lenses.

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
    :param next_token: 
    :type next_token: str
    :param max_results: 
    :type max_results: int
    :param lens_type: The type of lenses to be returned.
    :type lens_type: str
    :param lens_status: The status of lenses to be returned.
    :type lens_status: str
    :param lens_name: 
    :type lens_name: str

    """
    return web.Response(status=200)


async def list_milestones(request: web.Request, workload_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_milestones

    List all milestones for an existing workload.

    :param workload_id: 
    :type workload_id: str
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
    body = ListMilestonesRequest.from_dict(body)
    return web.Response(status=200)


async def list_notifications(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_notifications

    List lens notifications.

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
    body = ListNotificationsRequest.from_dict(body)
    return web.Response(status=200)


async def list_profile_notifications(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, workload_id=None, next_token=None, max_results=None) -> web.Response:
    """list_profile_notifications

    List profile notifications.

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
    :param workload_id: 
    :type workload_id: str
    :param next_token: 
    :type next_token: str
    :param max_results: 
    :type max_results: int

    """
    return web.Response(status=200)


async def list_profile_shares(request: web.Request, profile_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, shared_with_prefix=None, next_token=None, max_results=None, status=None) -> web.Response:
    """list_profile_shares

    List profile shares.

    :param profile_arn: The profile ARN.
    :type profile_arn: str
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
    :param shared_with_prefix: The Amazon Web Services account ID, IAM role, organization ID, or organizational unit (OU) ID with which the profile is shared.
    :type shared_with_prefix: str
    :param next_token: 
    :type next_token: str
    :param max_results: The maximum number of results to return for this request.
    :type max_results: int
    :param status: 
    :type status: str

    """
    return web.Response(status=200)


async def list_profiles(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, profile_name_prefix=None, profile_owner_type=None, next_token=None, max_results=None) -> web.Response:
    """list_profiles

    List profiles.

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
    :param profile_name_prefix: Prefix for profile name.
    :type profile_name_prefix: str
    :param profile_owner_type: Profile owner type.
    :type profile_owner_type: str
    :param next_token: 
    :type next_token: str
    :param max_results: 
    :type max_results: int

    """
    return web.Response(status=200)


async def list_share_invitations(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, workload_name_prefix=None, lens_name_prefix=None, share_resource_type=None, next_token=None, max_results=None, profile_name_prefix=None) -> web.Response:
    """list_share_invitations

    List the workload invitations.

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
    :param workload_name_prefix: 
    :type workload_name_prefix: str
    :param lens_name_prefix: An optional string added to the beginning of each lens name returned in the results.
    :type lens_name_prefix: str
    :param share_resource_type: The type of share invitations to be returned.
    :type share_resource_type: str
    :param next_token: 
    :type next_token: str
    :param max_results: The maximum number of results to return for this request.
    :type max_results: int
    :param profile_name_prefix: Profile name prefix.
    :type profile_name_prefix: str

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, workload_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    &lt;p&gt;List the tags for a resource.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The WorkloadArn parameter can be a workload ARN, a custom lens ARN, or a profile ARN.&lt;/p&gt; &lt;/note&gt;

    :param workload_arn: 
    :type workload_arn: str
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


async def list_workload_shares(request: web.Request, workload_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, shared_with_prefix=None, next_token=None, max_results=None, status=None) -> web.Response:
    """list_workload_shares

    List the workload shares associated with the workload.

    :param workload_id: 
    :type workload_id: str
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
    :param shared_with_prefix: The Amazon Web Services account ID, IAM role, organization ID, or organizational unit (OU) ID with which the workload is shared.
    :type shared_with_prefix: str
    :param next_token: 
    :type next_token: str
    :param max_results: The maximum number of results to return for this request.
    :type max_results: int
    :param status: 
    :type status: str

    """
    return web.Response(status=200)


async def list_workloads(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_workloads

    Paginated list of workloads.

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
    body = ListWorkloadsRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, workload_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;p&gt;Adds one or more tags to the specified resource.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The WorkloadArn parameter can be a workload ARN, a custom lens ARN, or a profile ARN.&lt;/p&gt; &lt;/note&gt;

    :param workload_arn: 
    :type workload_arn: str
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


async def untag_resource(request: web.Request, workload_arn, tag_keys, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    &lt;p&gt;Deletes specified tags from a resource.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The WorkloadArn parameter can be a workload ARN, a custom lens ARN, or a profile ARN.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;To specify multiple tags, use separate &lt;b&gt;tagKeys&lt;/b&gt; parameters, for example:&lt;/p&gt; &lt;p&gt; &lt;code&gt;DELETE /tags/WorkloadArn?tagKeys&#x3D;key1&amp;amp;tagKeys&#x3D;key2&lt;/code&gt; &lt;/p&gt;

    :param workload_arn: 
    :type workload_arn: str
    :param tag_keys: A list of tag keys. Existing tags of the resource whose keys are members of this list are removed from the resource.
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


async def update_answer(request: web.Request, workload_id, lens_alias, question_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_answer

    Update the answer to a specific question in a workload review.

    :param workload_id: 
    :type workload_id: str
    :param lens_alias: 
    :type lens_alias: str
    :param question_id: 
    :type question_id: str
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
    body = UpdateAnswerRequest.from_dict(body)
    return web.Response(status=200)


async def update_global_settings(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_global_settings

    Updates whether the Amazon Web Services account is opted into organization sharing and discovery integration features.

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
    body = UpdateGlobalSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_lens_review(request: web.Request, workload_id, lens_alias, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_lens_review

    Update lens review for a particular workload.

    :param workload_id: 
    :type workload_id: str
    :param lens_alias: 
    :type lens_alias: str
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
    body = UpdateLensReviewRequest.from_dict(body)
    return web.Response(status=200)


async def update_profile(request: web.Request, profile_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_profile

    Update a profile.

    :param profile_arn: The profile ARN.
    :type profile_arn: str
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
    body = UpdateProfileRequest.from_dict(body)
    return web.Response(status=200)


async def update_share_invitation(request: web.Request, share_invitation_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_share_invitation

    &lt;p&gt;Update a workload or custom lens share invitation.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API operation can be called independently of any resource. Previous documentation implied that a workload ARN must be specified.&lt;/p&gt; &lt;/note&gt;

    :param share_invitation_id: The ID assigned to the share invitation.
    :type share_invitation_id: str
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
    body = UpdateShareInvitationRequest.from_dict(body)
    return web.Response(status=200)


async def update_workload(request: web.Request, workload_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_workload

    Update an existing workload.

    :param workload_id: 
    :type workload_id: str
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
    body = UpdateWorkloadRequest.from_dict(body)
    return web.Response(status=200)


async def update_workload_share(request: web.Request, share_id, workload_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_workload_share

    Update a workload share.

    :param share_id: 
    :type share_id: str
    :param workload_id: 
    :type workload_id: str
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
    body = UpdateWorkloadShareRequest.from_dict(body)
    return web.Response(status=200)


async def upgrade_lens_review(request: web.Request, workload_id, lens_alias, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """upgrade_lens_review

    Upgrade lens review for a particular workload.

    :param workload_id: 
    :type workload_id: str
    :param lens_alias: 
    :type lens_alias: str
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
    body = UpgradeLensReviewRequest.from_dict(body)
    return web.Response(status=200)


async def upgrade_profile_version(request: web.Request, workload_id, profile_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """upgrade_profile_version

    Upgrade a profile.

    :param workload_id: 
    :type workload_id: str
    :param profile_arn: The profile ARN.
    :type profile_arn: str
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
    body = UpgradeProfileVersionRequest.from_dict(body)
    return web.Response(status=200)
