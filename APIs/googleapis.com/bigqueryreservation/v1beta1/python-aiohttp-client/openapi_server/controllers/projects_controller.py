from typing import List, Dict
from aiohttp import web

from openapi_server.models.assignment import Assignment
from openapi_server.models.capacity_commitment import CapacityCommitment
from openapi_server.models.list_assignments_response import ListAssignmentsResponse
from openapi_server.models.list_capacity_commitments_response import ListCapacityCommitmentsResponse
from openapi_server.models.list_reservations_response import ListReservationsResponse
from openapi_server.models.merge_capacity_commitments_request import MergeCapacityCommitmentsRequest
from openapi_server.models.move_assignment_request import MoveAssignmentRequest
from openapi_server.models.reservation import Reservation
from openapi_server.models.search_assignments_response import SearchAssignmentsResponse
from openapi_server.models.split_capacity_commitment_request import SplitCapacityCommitmentRequest
from openapi_server.models.split_capacity_commitment_response import SplitCapacityCommitmentResponse
from openapi_server import util


async def bigqueryreservation_projects_locations_capacity_commitments_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, capacity_commitment_id=None, enforce_single_admin_project_per_org=None, body=None) -> web.Response:
    """bigqueryreservation_projects_locations_capacity_commitments_create

    Creates a new capacity commitment resource.

    :param parent: Required. Resource name of the parent reservation. E.g., &#x60;projects/myproject/locations/US&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param capacity_commitment_id: The optional capacity commitment ID. Capacity commitment name will be generated automatically if this field is empty. This field must only contain lower case alphanumeric characters or dashes. The first and last character cannot be a dash. Max length is 64 characters. NOTE: this ID won&#39;t be kept if the capacity commitment is split or merged.
    :type capacity_commitment_id: str
    :param enforce_single_admin_project_per_org: If true, fail the request if another project in the organization has a capacity commitment.
    :type enforce_single_admin_project_per_org: bool
    :param body: 
    :type body: dict | bytes

    """
    body = CapacityCommitment.from_dict(body)
    return web.Response(status=200)


async def bigqueryreservation_projects_locations_capacity_commitments_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """bigqueryreservation_projects_locations_capacity_commitments_list

    Lists all the capacity commitments for the admin project.

    :param parent: Required. Resource name of the parent reservation. E.g., &#x60;projects/myproject/locations/US&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param page_size: The maximum number of items to return.
    :type page_size: int
    :param page_token: The next_page_token value returned from a previous List request, if any.
    :type page_token: str

    """
    return web.Response(status=200)


async def bigqueryreservation_projects_locations_capacity_commitments_merge(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """bigqueryreservation_projects_locations_capacity_commitments_merge

    Merges capacity commitments of the same plan into a single commitment. The resulting capacity commitment has the greater commitment_end_time out of the to-be-merged capacity commitments. Attempting to merge capacity commitments of different plan will fail with the error code &#x60;google.rpc.Code.FAILED_PRECONDITION&#x60;.

    :param parent: Parent resource that identifies admin project and location e.g., &#x60;projects/myproject/locations/us&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = MergeCapacityCommitmentsRequest.from_dict(body)
    return web.Response(status=200)


async def bigqueryreservation_projects_locations_capacity_commitments_split(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """bigqueryreservation_projects_locations_capacity_commitments_split

    Splits capacity commitment to two commitments of the same plan and &#x60;commitment_end_time&#x60;. A common use case is to enable downgrading commitments. For example, in order to downgrade from 10000 slots to 8000, you might split a 10000 capacity commitment into commitments of 2000 and 8000. Then, you delete the first one after the commitment end time passes.

    :param name: Required. The resource name e.g.,: &#x60;projects/myproject/locations/US/capacityCommitments/123&#x60;
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = SplitCapacityCommitmentRequest.from_dict(body)
    return web.Response(status=200)


async def bigqueryreservation_projects_locations_reservations_assignments_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, assignment_id=None, body=None) -> web.Response:
    """bigqueryreservation_projects_locations_reservations_assignments_create

    Creates an assignment object which allows the given project to submit jobs of a certain type using slots from the specified reservation. Currently a resource (project, folder, organization) can only have one assignment per each (job_type, location) combination, and that reservation will be used for all jobs of the matching type. Different assignments can be created on different levels of the projects, folders or organization hierarchy. During query execution, the assignment is looked up at the project, folder and organization levels in that order. The first assignment found is applied to the query. When creating assignments, it does not matter if other assignments exist at higher levels. Example: * The organization &#x60;organizationA&#x60; contains two projects, &#x60;project1&#x60; and &#x60;project2&#x60;. * Assignments for all three entities (&#x60;organizationA&#x60;, &#x60;project1&#x60;, and &#x60;project2&#x60;) could all be created and mapped to the same or different reservations. \&quot;None\&quot; assignments represent an absence of the assignment. Projects assigned to None use on-demand pricing. To create a \&quot;None\&quot; assignment, use \&quot;none\&quot; as a reservation_id in the parent. Example parent: &#x60;projects/myproject/locations/US/reservations/none&#x60;. Returns &#x60;google.rpc.Code.PERMISSION_DENIED&#x60; if user does not have &#39;bigquery.admin&#39; permissions on the project using the reservation and the project that owns this reservation. Returns &#x60;google.rpc.Code.INVALID_ARGUMENT&#x60; when location of the assignment does not match location of the reservation.

    :param parent: Required. The parent resource name of the assignment E.g. &#x60;projects/myproject/locations/US/reservations/team1-prod&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param assignment_id: The optional assignment ID. Assignment name will be generated automatically if this field is empty. This field must only contain lower case alphanumeric characters or dashes. Max length is 64 characters.
    :type assignment_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Assignment.from_dict(body)
    return web.Response(status=200)


async def bigqueryreservation_projects_locations_reservations_assignments_delete(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, force=None) -> web.Response:
    """bigqueryreservation_projects_locations_reservations_assignments_delete

    Deletes a assignment. No expansion will happen. Example: * Organization &#x60;organizationA&#x60; contains two projects, &#x60;project1&#x60; and &#x60;project2&#x60;. * Reservation &#x60;res1&#x60; exists and was created previously. * CreateAssignment was used previously to define the following associations between entities and reservations: &#x60;&#x60; and &#x60;&#x60; In this example, deletion of the &#x60;&#x60; assignment won&#39;t affect the other assignment &#x60;&#x60;. After said deletion, queries from &#x60;project1&#x60; will still use &#x60;res1&#x60; while queries from &#x60;project2&#x60; will switch to use on-demand mode.

    :param name: Required. Name of the resource, e.g. &#x60;projects/myproject/locations/US/reservations/team1-prod/assignments/123&#x60;
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param force: Can be used to force delete commitments even if assignments exist. Deleting commitments with assignments may cause queries to fail if they no longer have access to slots.
    :type force: bool

    """
    return web.Response(status=200)


async def bigqueryreservation_projects_locations_reservations_assignments_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """bigqueryreservation_projects_locations_reservations_assignments_list

    Lists assignments. Only explicitly created assignments will be returned. Example: * Organization &#x60;organizationA&#x60; contains two projects, &#x60;project1&#x60; and &#x60;project2&#x60;. * Reservation &#x60;res1&#x60; exists and was created previously. * CreateAssignment was used previously to define the following associations between entities and reservations: &#x60;&#x60; and &#x60;&#x60; In this example, ListAssignments will just return the above two assignments for reservation &#x60;res1&#x60;, and no expansion/merge will happen. The wildcard \&quot;-\&quot; can be used for reservations in the request. In that case all assignments belongs to the specified project and location will be listed. **Note** \&quot;-\&quot; cannot be used for projects nor locations.

    :param parent: Required. The parent resource name e.g.: &#x60;projects/myproject/locations/US/reservations/team1-prod&#x60; Or: &#x60;projects/myproject/locations/US/reservations/-&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param page_size: The maximum number of items to return.
    :type page_size: int
    :param page_token: The next_page_token value returned from a previous List request, if any.
    :type page_token: str

    """
    return web.Response(status=200)


async def bigqueryreservation_projects_locations_reservations_assignments_move(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """bigqueryreservation_projects_locations_reservations_assignments_move

    Moves an assignment under a new reservation. This differs from removing an existing assignment and recreating a new one by providing a transactional change that ensures an assignee always has an associated reservation.

    :param name: Required. The resource name of the assignment, e.g. &#x60;projects/myproject/locations/US/reservations/team1-prod/assignments/123&#x60;
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = MoveAssignmentRequest.from_dict(body)
    return web.Response(status=200)


async def bigqueryreservation_projects_locations_reservations_assignments_patch(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, update_mask=None, body=None) -> web.Response:
    """bigqueryreservation_projects_locations_reservations_assignments_patch

    Updates an existing assignment. Only the &#x60;priority&#x60; field can be updated.

    :param name: Output only. Name of the resource. E.g.: &#x60;projects/myproject/locations/US/reservations/team1-prod/assignments/123&#x60;. The assignment_id must only contain lower case alphanumeric characters or dashes and the max length is 64 characters.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param update_mask: Standard field mask for the set of fields to be updated.
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = Assignment.from_dict(body)
    return web.Response(status=200)


async def bigqueryreservation_projects_locations_reservations_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, reservation_id=None, body=None) -> web.Response:
    """bigqueryreservation_projects_locations_reservations_create

    Creates a new reservation resource.

    :param parent: Required. Project, location. E.g., &#x60;projects/myproject/locations/US&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param reservation_id: The reservation ID. It must only contain lower case alphanumeric characters or dashes. It must start with a letter and must not end with a dash. Its maximum length is 64 characters.
    :type reservation_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Reservation.from_dict(body)
    return web.Response(status=200)


async def bigqueryreservation_projects_locations_reservations_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """bigqueryreservation_projects_locations_reservations_get

    Returns information about the reservation.

    :param name: Required. Resource name of the reservation to retrieve. E.g., &#x60;projects/myproject/locations/US/reservations/team1-prod&#x60;
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def bigqueryreservation_projects_locations_reservations_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """bigqueryreservation_projects_locations_reservations_list

    Lists all the reservations for the project in the specified location.

    :param parent: Required. The parent resource name containing project and location, e.g.: &#x60;projects/myproject/locations/US&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Can be used to filter out reservations based on names, capacity, etc, e.g.: filter&#x3D;\&quot;reservation.slot_capacity &gt; 200\&quot; filter&#x3D;\&quot;reservation.name &#x3D; \\\&quot;*dev/*\\\&quot;\&quot; Advanced filtering syntax can be [here](https://cloud.google.com/logging/docs/view/advanced-filters).
    :type filter: str
    :param page_size: The maximum number of items to return.
    :type page_size: int
    :param page_token: The next_page_token value returned from a previous List request, if any.
    :type page_token: str

    """
    return web.Response(status=200)


async def bigqueryreservation_projects_locations_search_assignments(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None, query=None) -> web.Response:
    """bigqueryreservation_projects_locations_search_assignments

    Looks up assignments for a specified resource for a particular region. If the request is about a project: 1. Assignments created on the project will be returned if they exist. 2. Otherwise assignments created on the closest ancestor will be returned. 3. Assignments for different JobTypes will all be returned. The same logic applies if the request is about a folder. If the request is about an organization, then assignments created on the organization will be returned (organization doesn&#39;t have ancestors). Comparing to ListAssignments, there are some behavior differences: 1. permission on the assignee will be verified in this API. 2. Hierarchy lookup (project-&gt;folder-&gt;organization) happens in this API. 3. Parent here is &#x60;projects/*/locations/*&#x60;, instead of &#x60;projects/*/locations/*reservations/*&#x60;. **Note** \&quot;-\&quot; cannot be used for projects nor locations.

    :param parent: Required. The resource name of the admin project(containing project and location), e.g.: &#x60;projects/myproject/locations/US&#x60;.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param page_size: The maximum number of items to return.
    :type page_size: int
    :param page_token: The next_page_token value returned from a previous List request, if any.
    :type page_token: str
    :param query: Please specify resource name as assignee in the query. Examples: * &#x60;assignee&#x3D;projects/myproject&#x60; * &#x60;assignee&#x3D;folders/123&#x60; * &#x60;assignee&#x3D;organizations/456&#x60;
    :type query: str

    """
    return web.Response(status=200)
