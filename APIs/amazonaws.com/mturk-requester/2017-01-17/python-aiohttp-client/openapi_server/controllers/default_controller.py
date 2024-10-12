from typing import List, Dict
from aiohttp import web

from openapi_server.models.accept_qualification_request_request import AcceptQualificationRequestRequest
from openapi_server.models.approve_assignment_request import ApproveAssignmentRequest
from openapi_server.models.associate_qualification_with_worker_request import AssociateQualificationWithWorkerRequest
from openapi_server.models.create_additional_assignments_for_hit_request import CreateAdditionalAssignmentsForHITRequest
from openapi_server.models.create_hit_request import CreateHITRequest
from openapi_server.models.create_hit_response import CreateHITResponse
from openapi_server.models.create_hit_type_request import CreateHITTypeRequest
from openapi_server.models.create_hit_type_response import CreateHITTypeResponse
from openapi_server.models.create_hit_with_hit_type_request import CreateHITWithHITTypeRequest
from openapi_server.models.create_hit_with_hit_type_response import CreateHITWithHITTypeResponse
from openapi_server.models.create_qualification_type_request import CreateQualificationTypeRequest
from openapi_server.models.create_qualification_type_response import CreateQualificationTypeResponse
from openapi_server.models.create_worker_block_request import CreateWorkerBlockRequest
from openapi_server.models.delete_hit_request import DeleteHITRequest
from openapi_server.models.delete_qualification_type_request import DeleteQualificationTypeRequest
from openapi_server.models.delete_worker_block_request import DeleteWorkerBlockRequest
from openapi_server.models.disassociate_qualification_from_worker_request import DisassociateQualificationFromWorkerRequest
from openapi_server.models.get_account_balance_response import GetAccountBalanceResponse
from openapi_server.models.get_assignment_request import GetAssignmentRequest
from openapi_server.models.get_assignment_response import GetAssignmentResponse
from openapi_server.models.get_file_upload_url_request import GetFileUploadURLRequest
from openapi_server.models.get_file_upload_url_response import GetFileUploadURLResponse
from openapi_server.models.get_hit_request import GetHITRequest
from openapi_server.models.get_hit_response import GetHITResponse
from openapi_server.models.get_qualification_score_request import GetQualificationScoreRequest
from openapi_server.models.get_qualification_score_response import GetQualificationScoreResponse
from openapi_server.models.get_qualification_type_request import GetQualificationTypeRequest
from openapi_server.models.get_qualification_type_response import GetQualificationTypeResponse
from openapi_server.models.list_assignments_for_hit_request import ListAssignmentsForHITRequest
from openapi_server.models.list_assignments_for_hit_response import ListAssignmentsForHITResponse
from openapi_server.models.list_bonus_payments_request import ListBonusPaymentsRequest
from openapi_server.models.list_bonus_payments_response import ListBonusPaymentsResponse
from openapi_server.models.list_hits_for_qualification_type_request import ListHITsForQualificationTypeRequest
from openapi_server.models.list_hits_for_qualification_type_response import ListHITsForQualificationTypeResponse
from openapi_server.models.list_hits_request import ListHITsRequest
from openapi_server.models.list_hits_response import ListHITsResponse
from openapi_server.models.list_qualification_requests_request import ListQualificationRequestsRequest
from openapi_server.models.list_qualification_requests_response import ListQualificationRequestsResponse
from openapi_server.models.list_qualification_types_request import ListQualificationTypesRequest
from openapi_server.models.list_qualification_types_response import ListQualificationTypesResponse
from openapi_server.models.list_review_policy_results_for_hit_request import ListReviewPolicyResultsForHITRequest
from openapi_server.models.list_review_policy_results_for_hit_response import ListReviewPolicyResultsForHITResponse
from openapi_server.models.list_reviewable_hits_request import ListReviewableHITsRequest
from openapi_server.models.list_reviewable_hits_response import ListReviewableHITsResponse
from openapi_server.models.list_worker_blocks_request import ListWorkerBlocksRequest
from openapi_server.models.list_worker_blocks_response import ListWorkerBlocksResponse
from openapi_server.models.list_workers_with_qualification_type_request import ListWorkersWithQualificationTypeRequest
from openapi_server.models.list_workers_with_qualification_type_response import ListWorkersWithQualificationTypeResponse
from openapi_server.models.notify_workers_request import NotifyWorkersRequest
from openapi_server.models.notify_workers_response import NotifyWorkersResponse
from openapi_server.models.reject_assignment_request import RejectAssignmentRequest
from openapi_server.models.reject_qualification_request_request import RejectQualificationRequestRequest
from openapi_server.models.send_bonus_request import SendBonusRequest
from openapi_server.models.send_test_event_notification_request import SendTestEventNotificationRequest
from openapi_server.models.update_expiration_for_hit_request import UpdateExpirationForHITRequest
from openapi_server.models.update_hit_review_status_request import UpdateHITReviewStatusRequest
from openapi_server.models.update_hit_type_of_hit_request import UpdateHITTypeOfHITRequest
from openapi_server.models.update_notification_settings_request import UpdateNotificationSettingsRequest
from openapi_server.models.update_qualification_type_request import UpdateQualificationTypeRequest
from openapi_server.models.update_qualification_type_response import UpdateQualificationTypeResponse
from openapi_server import util


async def accept_qualification_request(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """accept_qualification_request

    &lt;p&gt; The &lt;code&gt;AcceptQualificationRequest&lt;/code&gt; operation approves a Worker&#39;s request for a Qualification. &lt;/p&gt; &lt;p&gt; Only the owner of the Qualification type can grant a Qualification request for that type. &lt;/p&gt; &lt;p&gt; A successful request for the &lt;code&gt;AcceptQualificationRequest&lt;/code&gt; operation returns with no errors and an empty body. &lt;/p&gt;

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
    body = AcceptQualificationRequestRequest.from_dict(body)
    return web.Response(status=200)


async def approve_assignment(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """approve_assignment

    &lt;p&gt; The &lt;code&gt;ApproveAssignment&lt;/code&gt; operation approves the results of a completed assignment. &lt;/p&gt; &lt;p&gt; Approving an assignment initiates two payments from the Requester&#39;s Amazon.com account &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The Worker who submitted the results is paid the reward specified in the HIT. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Amazon Mechanical Turk fees are debited. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; If the Requester&#39;s account does not have adequate funds for these payments, the call to ApproveAssignment returns an exception, and the approval is not processed. You can include an optional feedback message with the approval, which the Worker can see in the Status section of the web site. &lt;/p&gt; &lt;p&gt; You can also call this operation for assignments that were previous rejected and approve them by explicitly overriding the previous rejection. This only works on rejected assignments that were submitted within the previous 30 days and only if the assignment&#39;s related HIT has not been deleted. &lt;/p&gt;

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
    body = ApproveAssignmentRequest.from_dict(body)
    return web.Response(status=200)


async def associate_qualification_with_worker(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_qualification_with_worker

    &lt;p&gt; The &lt;code&gt;AssociateQualificationWithWorker&lt;/code&gt; operation gives a Worker a Qualification. &lt;code&gt;AssociateQualificationWithWorker&lt;/code&gt; does not require that the Worker submit a Qualification request. It gives the Qualification directly to the Worker. &lt;/p&gt; &lt;p&gt; You can only assign a Qualification of a Qualification type that you created (using the &lt;code&gt;CreateQualificationType&lt;/code&gt; operation). &lt;/p&gt; &lt;note&gt; &lt;p&gt; Note: &lt;code&gt;AssociateQualificationWithWorker&lt;/code&gt; does not affect any pending Qualification requests for the Qualification by the Worker. If you assign a Qualification to a Worker, then later grant a Qualification request made by the Worker, the granting of the request may modify the Qualification score. To resolve a pending Qualification request without affecting the Qualification the Worker already has, reject the request with the &lt;code&gt;RejectQualificationRequest&lt;/code&gt; operation. &lt;/p&gt; &lt;/note&gt;

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
    body = AssociateQualificationWithWorkerRequest.from_dict(body)
    return web.Response(status=200)


async def create_additional_assignments_for_hit(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_additional_assignments_for_hit

    &lt;p&gt; The &lt;code&gt;CreateAdditionalAssignmentsForHIT&lt;/code&gt; operation increases the maximum number of assignments of an existing HIT. &lt;/p&gt; &lt;p&gt; To extend the maximum number of assignments, specify the number of additional assignments.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;HITs created with fewer than 10 assignments cannot be extended to have 10 or more assignments. Attempting to add assignments in a way that brings the total number of assignments for a HIT from fewer than 10 assignments to 10 or more assignments will result in an &lt;code&gt;AWS.MechanicalTurk.InvalidMaximumAssignmentsIncrease&lt;/code&gt; exception.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;HITs that were created before July 22, 2015 cannot be extended. Attempting to extend HITs that were created before July 22, 2015 will result in an &lt;code&gt;AWS.MechanicalTurk.HITTooOldForExtension&lt;/code&gt; exception. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = CreateAdditionalAssignmentsForHITRequest.from_dict(body)
    return web.Response(status=200)


async def create_hit(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_hit

    &lt;p&gt;The &lt;code&gt;CreateHIT&lt;/code&gt; operation creates a new Human Intelligence Task (HIT). The new HIT is made available for Workers to find and accept on the Amazon Mechanical Turk website. &lt;/p&gt; &lt;p&gt; This operation allows you to specify a new HIT by passing in values for the properties of the HIT, such as its title, reward amount and number of assignments. When you pass these values to &lt;code&gt;CreateHIT&lt;/code&gt;, a new HIT is created for you, with a new &lt;code&gt;HITTypeID&lt;/code&gt;. The HITTypeID can be used to create additional HITs in the future without needing to specify common parameters such as the title, description and reward amount each time.&lt;/p&gt; &lt;p&gt; An alternative way to create HITs is to first generate a HITTypeID using the &lt;code&gt;CreateHITType&lt;/code&gt; operation and then call the &lt;code&gt;CreateHITWithHITType&lt;/code&gt; operation. This is the recommended best practice for Requesters who are creating large numbers of HITs. &lt;/p&gt; &lt;p&gt;CreateHIT also supports several ways to provide question data: by providing a value for the &lt;code&gt;Question&lt;/code&gt; parameter that fully specifies the contents of the HIT, or by providing a &lt;code&gt;HitLayoutId&lt;/code&gt; and associated &lt;code&gt;HitLayoutParameters&lt;/code&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt; If a HIT is created with 10 or more maximum assignments, there is an additional fee. For more information, see &lt;a href&#x3D;\&quot;https://requester.mturk.com/pricing\&quot;&gt;Amazon Mechanical Turk Pricing&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = CreateHITRequest.from_dict(body)
    return web.Response(status=200)


async def create_hit_type(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_hit_type

     The &lt;code&gt;CreateHITType&lt;/code&gt; operation creates a new HIT type. This operation allows you to define a standard set of HIT properties to use when creating HITs. If you register a HIT type with values that match an existing HIT type, the HIT type ID of the existing type will be returned. 

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
    body = CreateHITTypeRequest.from_dict(body)
    return web.Response(status=200)


async def create_hit_with_hit_type(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_hit_with_hit_type

    &lt;p&gt; The &lt;code&gt;CreateHITWithHITType&lt;/code&gt; operation creates a new Human Intelligence Task (HIT) using an existing HITTypeID generated by the &lt;code&gt;CreateHITType&lt;/code&gt; operation. &lt;/p&gt; &lt;p&gt; This is an alternative way to create HITs from the &lt;code&gt;CreateHIT&lt;/code&gt; operation. This is the recommended best practice for Requesters who are creating large numbers of HITs. &lt;/p&gt; &lt;p&gt;CreateHITWithHITType also supports several ways to provide question data: by providing a value for the &lt;code&gt;Question&lt;/code&gt; parameter that fully specifies the contents of the HIT, or by providing a &lt;code&gt;HitLayoutId&lt;/code&gt; and associated &lt;code&gt;HitLayoutParameters&lt;/code&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt; If a HIT is created with 10 or more maximum assignments, there is an additional fee. For more information, see &lt;a href&#x3D;\&quot;https://requester.mturk.com/pricing\&quot;&gt;Amazon Mechanical Turk Pricing&lt;/a&gt;. &lt;/p&gt; &lt;/note&gt;

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
    body = CreateHITWithHITTypeRequest.from_dict(body)
    return web.Response(status=200)


async def create_qualification_type(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_qualification_type

     The &lt;code&gt;CreateQualificationType&lt;/code&gt; operation creates a new Qualification type, which is represented by a &lt;code&gt;QualificationType&lt;/code&gt; data structure. 

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
    body = CreateQualificationTypeRequest.from_dict(body)
    return web.Response(status=200)


async def create_worker_block(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_worker_block

    The &lt;code&gt;CreateWorkerBlock&lt;/code&gt; operation allows you to prevent a Worker from working on your HITs. For example, you can block a Worker who is producing poor quality work. You can block up to 100,000 Workers.

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
    body = CreateWorkerBlockRequest.from_dict(body)
    return web.Response(status=200)


async def delete_hit(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_hit

    &lt;p&gt; The &lt;code&gt;DeleteHIT&lt;/code&gt; operation is used to delete HIT that is no longer needed. Only the Requester who created the HIT can delete it. &lt;/p&gt; &lt;p&gt; You can only dispose of HITs that are in the &lt;code&gt;Reviewable&lt;/code&gt; state, with all of their submitted assignments already either approved or rejected. If you call the DeleteHIT operation on a HIT that is not in the &lt;code&gt;Reviewable&lt;/code&gt; state (for example, that has not expired, or still has active assignments), or on a HIT that is Reviewable but without all of its submitted assignments already approved or rejected, the service will return an error. &lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; HITs are automatically disposed of after 120 days. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; After you dispose of a HIT, you can no longer approve the HIT&#39;s rejected assignments. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Disposed HITs are not returned in results for the ListHITs operation. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Disposing HITs can improve the performance of operations such as ListReviewableHITs and ListHITs. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = DeleteHITRequest.from_dict(body)
    return web.Response(status=200)


async def delete_qualification_type(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_qualification_type

    &lt;p&gt; The &lt;code&gt;DeleteQualificationType&lt;/code&gt; deletes a Qualification type and deletes any HIT types that are associated with the Qualification type. &lt;/p&gt; &lt;p&gt;This operation does not revoke Qualifications already assigned to Workers because the Qualifications might be needed for active HITs. If there are any pending requests for the Qualification type, Amazon Mechanical Turk rejects those requests. After you delete a Qualification type, you can no longer use it to create HITs or HIT types.&lt;/p&gt; &lt;note&gt; &lt;p&gt;DeleteQualificationType must wait for all the HITs that use the deleted Qualification type to be deleted before completing. It may take up to 48 hours before DeleteQualificationType completes and the unique name of the Qualification type is available for reuse with CreateQualificationType.&lt;/p&gt; &lt;/note&gt;

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
    body = DeleteQualificationTypeRequest.from_dict(body)
    return web.Response(status=200)


async def delete_worker_block(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_worker_block

    The &lt;code&gt;DeleteWorkerBlock&lt;/code&gt; operation allows you to reinstate a blocked Worker to work on your HITs. This operation reverses the effects of the CreateWorkerBlock operation. You need the Worker ID to use this operation. If the Worker ID is missing or invalid, this operation fails and returns the message “WorkerId is invalid.” If the specified Worker is not blocked, this operation returns successfully.

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
    body = DeleteWorkerBlockRequest.from_dict(body)
    return web.Response(status=200)


async def disassociate_qualification_from_worker(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_qualification_from_worker

    &lt;p&gt; The &lt;code&gt;DisassociateQualificationFromWorker&lt;/code&gt; revokes a previously granted Qualification from a user. &lt;/p&gt; &lt;p&gt; You can provide a text message explaining why the Qualification was revoked. The user who had the Qualification can see this message. &lt;/p&gt;

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
    body = DisassociateQualificationFromWorkerRequest.from_dict(body)
    return web.Response(status=200)


async def get_account_balance(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_account_balance

    The &lt;code&gt;GetAccountBalance&lt;/code&gt; operation retrieves the Prepaid HITs balance in your Amazon Mechanical Turk account if you are a Prepaid Requester. Alternatively, this operation will retrieve the remaining available AWS Billing usage if you have enabled AWS Billing. Note: If you have enabled AWS Billing and still have a remaining Prepaid HITs balance, this balance can be viewed on the My Account page in the Requester console.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: 
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


async def get_assignment(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_assignment

     The &lt;code&gt;GetAssignment&lt;/code&gt; operation retrieves the details of the specified Assignment. 

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
    body = GetAssignmentRequest.from_dict(body)
    return web.Response(status=200)


async def get_file_upload_url(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_file_upload_url

     The &lt;code&gt;GetFileUploadURL&lt;/code&gt; operation generates and returns a temporary URL. You use the temporary URL to retrieve a file uploaded by a Worker as an answer to a FileUploadAnswer question for a HIT. The temporary URL is generated the instant the GetFileUploadURL operation is called, and is valid for 60 seconds. You can get a temporary file upload URL any time until the HIT is disposed. After the HIT is disposed, any uploaded files are deleted, and cannot be retrieved. Pending Deprecation on December 12, 2017. The Answer Specification structure will no longer support the &lt;code&gt;FileUploadAnswer&lt;/code&gt; element to be used for the QuestionForm data structure. Instead, we recommend that Requesters who want to create HITs asking Workers to upload files to use Amazon S3. 

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
    body = GetFileUploadURLRequest.from_dict(body)
    return web.Response(status=200)


async def get_hit(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_hit

     The &lt;code&gt;GetHIT&lt;/code&gt; operation retrieves the details of the specified HIT. 

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
    body = GetHITRequest.from_dict(body)
    return web.Response(status=200)


async def get_qualification_score(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_qualification_score

    &lt;p&gt; The &lt;code&gt;GetQualificationScore&lt;/code&gt; operation returns the value of a Worker&#39;s Qualification for a given Qualification type. &lt;/p&gt; &lt;p&gt; To get a Worker&#39;s Qualification, you must know the Worker&#39;s ID. The Worker&#39;s ID is included in the assignment data returned by the &lt;code&gt;ListAssignmentsForHIT&lt;/code&gt; operation. &lt;/p&gt; &lt;p&gt;Only the owner of a Qualification type can query the value of a Worker&#39;s Qualification of that type.&lt;/p&gt;

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
    body = GetQualificationScoreRequest.from_dict(body)
    return web.Response(status=200)


async def get_qualification_type(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_qualification_type

     The &lt;code&gt;GetQualificationType&lt;/code&gt;operation retrieves information about a Qualification type using its ID. 

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
    body = GetQualificationTypeRequest.from_dict(body)
    return web.Response(status=200)


async def list_assignments_for_hit(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_assignments_for_hit

    &lt;p&gt; The &lt;code&gt;ListAssignmentsForHIT&lt;/code&gt; operation retrieves completed assignments for a HIT. You can use this operation to retrieve the results for a HIT. &lt;/p&gt; &lt;p&gt; You can get assignments for a HIT at any time, even if the HIT is not yet Reviewable. If a HIT requested multiple assignments, and has received some results but has not yet become Reviewable, you can still retrieve the partial results with this operation. &lt;/p&gt; &lt;p&gt; Use the AssignmentStatus parameter to control which set of assignments for a HIT are returned. The ListAssignmentsForHIT operation can return submitted assignments awaiting approval, or it can return assignments that have already been approved or rejected. You can set AssignmentStatus&#x3D;Approved,Rejected to get assignments that have already been approved and rejected together in one result set. &lt;/p&gt; &lt;p&gt; Only the Requester who created the HIT can retrieve the assignments for that HIT. &lt;/p&gt; &lt;p&gt; Results are sorted and divided into numbered pages and the operation returns a single page of results. You can use the parameters of the operation to control sorting and pagination. &lt;/p&gt;

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
    body = ListAssignmentsForHITRequest.from_dict(body)
    return web.Response(status=200)


async def list_bonus_payments(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_bonus_payments

     The &lt;code&gt;ListBonusPayments&lt;/code&gt; operation retrieves the amounts of bonuses you have paid to Workers for a given HIT or assignment. 

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
    body = ListBonusPaymentsRequest.from_dict(body)
    return web.Response(status=200)


async def list_hits(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_hits

     The &lt;code&gt;ListHITs&lt;/code&gt; operation returns all of a Requester&#39;s HITs. The operation returns HITs of any status, except for HITs that have been deleted of with the DeleteHIT operation or that have been auto-deleted. 

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
    body = ListHITsRequest.from_dict(body)
    return web.Response(status=200)


async def list_hits_for_qualification_type(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_hits_for_qualification_type

     The &lt;code&gt;ListHITsForQualificationType&lt;/code&gt; operation returns the HITs that use the given Qualification type for a Qualification requirement. The operation returns HITs of any status, except for HITs that have been deleted with the &lt;code&gt;DeleteHIT&lt;/code&gt; operation or that have been auto-deleted. 

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
    body = ListHITsForQualificationTypeRequest.from_dict(body)
    return web.Response(status=200)


async def list_qualification_requests(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_qualification_requests

     The &lt;code&gt;ListQualificationRequests&lt;/code&gt; operation retrieves requests for Qualifications of a particular Qualification type. The owner of the Qualification type calls this operation to poll for pending requests, and accepts them using the AcceptQualification operation. 

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
    body = ListQualificationRequestsRequest.from_dict(body)
    return web.Response(status=200)


async def list_qualification_types(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_qualification_types

     The &lt;code&gt;ListQualificationTypes&lt;/code&gt; operation returns a list of Qualification types, filtered by an optional search term. 

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
    body = ListQualificationTypesRequest.from_dict(body)
    return web.Response(status=200)


async def list_review_policy_results_for_hit(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_review_policy_results_for_hit

     The &lt;code&gt;ListReviewPolicyResultsForHIT&lt;/code&gt; operation retrieves the computed results and the actions taken in the course of executing your Review Policies for a given HIT. For information about how to specify Review Policies when you call CreateHIT, see Review Policies. The ListReviewPolicyResultsForHIT operation can return results for both Assignment-level and HIT-level review results. 

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
    body = ListReviewPolicyResultsForHITRequest.from_dict(body)
    return web.Response(status=200)


async def list_reviewable_hits(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_reviewable_hits

     The &lt;code&gt;ListReviewableHITs&lt;/code&gt; operation retrieves the HITs with Status equal to Reviewable or Status equal to Reviewing that belong to the Requester calling the operation. 

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
    body = ListReviewableHITsRequest.from_dict(body)
    return web.Response(status=200)


async def list_worker_blocks(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_worker_blocks

    The &lt;code&gt;ListWorkersBlocks&lt;/code&gt; operation retrieves a list of Workers who are blocked from working on your HITs.

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
    body = ListWorkerBlocksRequest.from_dict(body)
    return web.Response(status=200)


async def list_workers_with_qualification_type(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_workers_with_qualification_type

     The &lt;code&gt;ListWorkersWithQualificationType&lt;/code&gt; operation returns all of the Workers that have been associated with a given Qualification type. 

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
    body = ListWorkersWithQualificationTypeRequest.from_dict(body)
    return web.Response(status=200)


async def notify_workers(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """notify_workers

     The &lt;code&gt;NotifyWorkers&lt;/code&gt; operation sends an email to one or more Workers that you specify with the Worker ID. You can specify up to 100 Worker IDs to send the same message with a single call to the NotifyWorkers operation. The NotifyWorkers operation will send a notification email to a Worker only if you have previously approved or rejected work from the Worker. 

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
    body = NotifyWorkersRequest.from_dict(body)
    return web.Response(status=200)


async def reject_assignment(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """reject_assignment

    &lt;p&gt; The &lt;code&gt;RejectAssignment&lt;/code&gt; operation rejects the results of a completed assignment. &lt;/p&gt; &lt;p&gt; You can include an optional feedback message with the rejection, which the Worker can see in the Status section of the web site. When you include a feedback message with the rejection, it helps the Worker understand why the assignment was rejected, and can improve the quality of the results the Worker submits in the future. &lt;/p&gt; &lt;p&gt; Only the Requester who created the HIT can reject an assignment for the HIT. &lt;/p&gt;

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
    body = RejectAssignmentRequest.from_dict(body)
    return web.Response(status=200)


async def reject_qualification_request(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """reject_qualification_request

    &lt;p&gt; The &lt;code&gt;RejectQualificationRequest&lt;/code&gt; operation rejects a user&#39;s request for a Qualification. &lt;/p&gt; &lt;p&gt; You can provide a text message explaining why the request was rejected. The Worker who made the request can see this message.&lt;/p&gt;

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
    body = RejectQualificationRequestRequest.from_dict(body)
    return web.Response(status=200)


async def send_bonus(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """send_bonus

     The &lt;code&gt;SendBonus&lt;/code&gt; operation issues a payment of money from your account to a Worker. This payment happens separately from the reward you pay to the Worker when you approve the Worker&#39;s assignment. The SendBonus operation requires the Worker&#39;s ID and the assignment ID as parameters to initiate payment of the bonus. You must include a message that explains the reason for the bonus payment, as the Worker may not be expecting the payment. Amazon Mechanical Turk collects a fee for bonus payments, similar to the HIT listing fee. This operation fails if your account does not have enough funds to pay for both the bonus and the fees. 

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
    body = SendBonusRequest.from_dict(body)
    return web.Response(status=200)


async def send_test_event_notification(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """send_test_event_notification

     The &lt;code&gt;SendTestEventNotification&lt;/code&gt; operation causes Amazon Mechanical Turk to send a notification message as if a HIT event occurred, according to the provided notification specification. This allows you to test notifications without setting up notifications for a real HIT type and trying to trigger them using the website. When you call this operation, the service attempts to send the test notification immediately. 

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
    body = SendTestEventNotificationRequest.from_dict(body)
    return web.Response(status=200)


async def update_expiration_for_hit(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_expiration_for_hit

     The &lt;code&gt;UpdateExpirationForHIT&lt;/code&gt; operation allows you update the expiration time of a HIT. If you update it to a time in the past, the HIT will be immediately expired. 

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
    body = UpdateExpirationForHITRequest.from_dict(body)
    return web.Response(status=200)


async def update_hit_review_status(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_hit_review_status

     The &lt;code&gt;UpdateHITReviewStatus&lt;/code&gt; operation updates the status of a HIT. If the status is Reviewable, this operation can update the status to Reviewing, or it can revert a Reviewing HIT back to the Reviewable status. 

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
    body = UpdateHITReviewStatusRequest.from_dict(body)
    return web.Response(status=200)


async def update_hit_type_of_hit(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_hit_type_of_hit

     The &lt;code&gt;UpdateHITTypeOfHIT&lt;/code&gt; operation allows you to change the HITType properties of a HIT. This operation disassociates the HIT from its old HITType properties and associates it with the new HITType properties. The HIT takes on the properties of the new HITType in place of the old ones. 

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
    body = UpdateHITTypeOfHITRequest.from_dict(body)
    return web.Response(status=200)


async def update_notification_settings(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_notification_settings

     The &lt;code&gt;UpdateNotificationSettings&lt;/code&gt; operation creates, updates, disables or re-enables notifications for a HIT type. If you call the UpdateNotificationSettings operation for a HIT type that already has a notification specification, the operation replaces the old specification with a new one. You can call the UpdateNotificationSettings operation to enable or disable notifications for the HIT type, without having to modify the notification specification itself by providing updates to the Active status without specifying a new notification specification. To change the Active status of a HIT type&#39;s notifications, the HIT type must already have a notification specification, or one must be provided in the same call to &lt;code&gt;UpdateNotificationSettings&lt;/code&gt;. 

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
    body = UpdateNotificationSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_qualification_type(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_qualification_type

    &lt;p&gt; The &lt;code&gt;UpdateQualificationType&lt;/code&gt; operation modifies the attributes of an existing Qualification type, which is represented by a QualificationType data structure. Only the owner of a Qualification type can modify its attributes. &lt;/p&gt; &lt;p&gt; Most attributes of a Qualification type can be changed after the type has been created. However, the Name and Keywords fields cannot be modified. The RetryDelayInSeconds parameter can be modified or added to change the delay or to enable retries, but RetryDelayInSeconds cannot be used to disable retries. &lt;/p&gt; &lt;p&gt; You can use this operation to update the test for a Qualification type. The test is updated based on the values specified for the Test, TestDurationInSeconds and AnswerKey parameters. All three parameters specify the updated test. If you are updating the test for a type, you must specify the Test and TestDurationInSeconds parameters. The AnswerKey parameter is optional; omitting it specifies that the updated test does not have an answer key. &lt;/p&gt; &lt;p&gt; If you omit the Test parameter, the test for the Qualification type is unchanged. There is no way to remove a test from a Qualification type that has one. If the type already has a test, you cannot update it to be AutoGranted. If the Qualification type does not have a test and one is provided by an update, the type will henceforth have a test. &lt;/p&gt; &lt;p&gt; If you want to update the test duration or answer key for an existing test without changing the questions, you must specify a Test parameter with the original questions, along with the updated values. &lt;/p&gt; &lt;p&gt; If you provide an updated Test but no AnswerKey, the new test will not have an answer key. Requests for such Qualifications must be granted manually. &lt;/p&gt; &lt;p&gt; You can also update the AutoGranted and AutoGrantedValue attributes of the Qualification type.&lt;/p&gt;

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
    body = UpdateQualificationTypeRequest.from_dict(body)
    return web.Response(status=200)
