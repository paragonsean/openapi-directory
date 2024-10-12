from typing import List, Dict
from aiohttp import web

from openapi_server.models.custom_price_list_output_model import CustomPriceListOutputModel
from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.patch_operation import PatchOperation
from openapi_server.models.phase_input_model import PhaseInputModel
from openapi_server.models.phase_member_model import PhaseMemberModel
from openapi_server.models.phase_members_from_business_unit_users_model import PhaseMembersFromBusinessUnitUsersModel
from openapi_server.models.phase_output_model import PhaseOutputModel
from openapi_server.models.project_custom_value_model import ProjectCustomValueModel
from openapi_server.models.project_file_model import ProjectFileModel
from openapi_server.models.project_forecast_input_model import ProjectForecastInputModel
from openapi_server.models.project_forecast_output_model import ProjectForecastOutputModel
from openapi_server.models.project_input_model_base import ProjectInputModelBase
from openapi_server.models.project_invoice_settings_input_model import ProjectInvoiceSettingsInputModel
from openapi_server.models.project_invoice_settings_output_model import ProjectInvoiceSettingsOutputModel
from openapi_server.models.project_keyword_model import ProjectKeywordModel
from openapi_server.models.project_output_model import ProjectOutputModel
from openapi_server.models.project_product_input_model import ProjectProductInputModel
from openapi_server.models.project_product_output_model import ProjectProductOutputModel
from openapi_server.models.project_sales_note_input_model import ProjectSalesNoteInputModel
from openapi_server.models.project_sales_note_output_model import ProjectSalesNoteOutputModel
from openapi_server.models.project_work_hour_price_input_model import ProjectWorkHourPriceInputModel
from openapi_server.models.project_work_hour_price_output_model import ProjectWorkHourPriceOutputModel
from openapi_server.models.project_work_type_model import ProjectWorkTypeModel
from openapi_server.models.proposal_fee_row_input_model import ProposalFeeRowInputModel
from openapi_server.models.proposal_fee_row_output_model import ProposalFeeRowOutputModel
from openapi_server.models.proposal_input_model import ProposalInputModel
from openapi_server.models.proposal_output_model import ProposalOutputModel
from openapi_server.models.proposal_settings_output_model import ProposalSettingsOutputModel
from openapi_server.models.proposal_subtotal_input_model import ProposalSubtotalInputModel
from openapi_server.models.proposal_subtotal_output_model import ProposalSubtotalOutputModel
from openapi_server.models.proposal_workhour_row_input_model import ProposalWorkhourRowInputModel
from openapi_server.models.proposal_workhour_row_output_model import ProposalWorkhourRowOutputModel
from openapi_server import util


async def files_post_project_link(request: web.Request, body=None) -> web.Response:
    """Add a link to a project.

    

    :param body: ProjectFileModel.
    :type body: dict | bytes

    """
    body = ProjectFileModel.from_dict(body)
    return web.Response(status=200)


async def keywords_link_keyword_to_project(request: web.Request, project_guid, guid) -> web.Response:
    """Link existing keyword to project

    

    :param project_guid: 
    :type project_guid: str
    :param guid: 
    :type guid: str

    """
    return web.Response(status=200)


async def phase_members_post_phase_member(request: web.Request, add_to_all_sub_phases=None, body=None) -> web.Response:
    """Adds a phase member.

    User is always added as a root phase (project) member also.

    :param add_to_all_sub_phases: Optional: Add member to all sub phases. Default true.
    :type add_to_all_sub_phases: bool
    :param body: PhaseMemberModel.
    :type body: dict | bytes

    """
    body = PhaseMemberModel.from_dict(body)
    return web.Response(status=200)


async def phase_members_post_phase_members_from_business_unit_users(request: web.Request, add_to_all_sub_phases=None, body=None) -> web.Response:
    """Adds business unit users to phase members.

    Users are always added as a root phase (project) member also.

    :param add_to_all_sub_phases: Optional: Add member to all sub phases. Default true.
    :type add_to_all_sub_phases: bool
    :param body: PhaseMemberModel.
    :type body: dict | bytes

    """
    body = PhaseMembersFromBusinessUnitUsersModel.from_dict(body)
    return web.Response(status=200)


async def phases_patch_phase(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a phase or a part of it

    

    :param guid: ID of the phase
    :type guid: str
    :param body: JSON Patch document of PhaseInputModel
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def phases_post_phase(request: web.Request, body=None) -> web.Response:
    """Insert a phase

    

    :param body: PhaseOutputModel
    :type body: dict | bytes

    """
    body = PhaseInputModel.from_dict(body)
    return web.Response(status=200)


async def price_lists_post_custom_pricelist(request: web.Request, project_guid, is_volume_pricing=None) -> web.Response:
    """Create custom price list for a project. If project already has a custom price list returns existing price list. Creates a new price list if project doesn&#39;t have a custom price list. Project can only have one custom price list. Note that project&#39;s price list will be changed to the custom price list created here and also existing prices are copied to the new price list.

    

    :param project_guid: ID of the project.
    :type project_guid: str
    :param is_volume_pricing: Get the custom volume pricing price list or regular custom price list. Default is false.
    :type is_volume_pricing: bool

    """
    return web.Response(status=200)


async def project_custom_values_patch_project_custom_value(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a project custom value or a part of it.

    

    :param guid: ID of the project custom value Can also be comma separate list of IDs to patch multiple project custom values with one call. When multiple IDs are given, returns model which has list of succeeded project custom values and list of errors.
    :type guid: str
    :param body: JSON Patch document of ProjectCustomValueModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def project_custom_values_post_project_custom_value(request: web.Request, body=None) -> web.Response:
    """Insert a project custom value.

    

    :param body: ProjectCustomValueModel.
    :type body: dict | bytes

    """
    body = ProjectCustomValueModel.from_dict(body)
    return web.Response(status=200)


async def project_forecasts_patch_forecast(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) an project forecast or a part of it

    

    :param guid: ID of the project forecast
    :type guid: str
    :param body: JSON patch document of ProjectForecastInputModel
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def project_forecasts_post_forecast(request: web.Request, body=None) -> web.Response:
    """Insert a project forecast

    

    :param body: ProjectForecastOutputInputModel
    :type body: dict | bytes

    """
    body = ProjectForecastInputModel.from_dict(body)
    return web.Response(status=200)


async def project_invoice_settings_patch_project_invoice_settings_0(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) project invoice settings.

    

    :param guid: ID of the project invoice settings.
    :type guid: str
    :param body: JSON patch document of ProjectInvoiceSettingsInputModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def project_invoice_settings_post_project_invoice_settings_0(request: web.Request, body=None) -> web.Response:
    """Create a new project invoice settings.

    

    :param body: Project invoice settings.
    :type body: dict | bytes

    """
    body = ProjectInvoiceSettingsInputModel.from_dict(body)
    return web.Response(status=200)


async def project_products_post_project_product(request: web.Request, body=None) -> web.Response:
    """Adds a product to a project.

    

    :param body: projectProductModel
    :type body: dict | bytes

    """
    body = ProjectProductInputModel.from_dict(body)
    return web.Response(status=200)


async def project_work_hour_prices_patch_project_work_hour_price(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a work hour price or a part of it

    

    :param guid: ID of the work hour price
    :type guid: str
    :param body: JSON patch document of ProjectWorkHourPriceInputModel
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def project_work_hour_prices_post_project_work_hour_price(request: web.Request, body=None) -> web.Response:
    """Insert a work hour price

    

    :param body: ProjectWorkHourPriceInputModel
    :type body: dict | bytes

    """
    body = ProjectWorkHourPriceInputModel.from_dict(body)
    return web.Response(status=200)


async def project_work_types_patch_project_worktype(request: web.Request, guid, body=None) -> web.Response:
    """Update (patch) a project work type.

    This currently can be used only to change the default work type in a project. The \&quot;UseWorktypesFromSetting\&quot; flag for the Project should be false (the project should not use the organization list of work types).

    :param guid: ID of the project work type.
    :type guid: str
    :param body: JSON patch document of ProjectWorkTypeModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def project_work_types_post_project_worktype(request: web.Request, body=None) -> web.Response:
    """Adds a work type to a project.

    The \&quot;UseWorktypesFromSetting\&quot; flag for the Project should be false (the project should not use the organization list of work types).

    :param body: ProjectWorkTypeModel.
    :type body: dict | bytes

    """
    body = ProjectWorkTypeModel.from_dict(body)
    return web.Response(status=200)


async def projects_patch_project(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a project or a part of it

    To update current project status, give ProjectStatusTypeGuid and possibly Description. To update current sales status, give SalesStatusTypeGuid (

    :param guid: ID of the project
    :type guid: str
    :param body: JSON Patch document of ProjectInputModel
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def projects_post_project(request: web.Request, body=None) -> web.Response:
    """Insert a project

    When creating a new project, the price list property will be ignored, as it is chosen by default.

    :param body: ProjectInputModelBase
    :type body: dict | bytes

    """
    body = ProjectInputModelBase.from_dict(body)
    return web.Response(status=200)


async def proposal_fees_patch_proposal_fee(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a proposal fee row or a part of it

    

    :param guid: ID of the proposal fee row
    :type guid: str
    :param body: JSON patch document of ProposalFeeModel
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def proposal_fees_post_proposal_fee(request: web.Request, body=None) -> web.Response:
    """Insert a proposal fee row.

    

    :param body: ProposalFeeModel
    :type body: dict | bytes

    """
    body = ProposalFeeRowInputModel.from_dict(body)
    return web.Response(status=200)


async def proposal_settings_patch_proposal_settings(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) proposal settings

    

    :param guid: Guid of the Proposal
    :type guid: str
    :param body: JSON patch document of ProposalSettingsInputModel
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def proposal_subtotals_patch_proposal_subtotal(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a Proposal subtotal or a part of it

    It is not possible to changed the proposalGuid for an existing proposal subtotal. Also, when a proposal subtotal is connected to a phase, the connection can only be broken if the phase is deleted.

    :param guid: ID of the Proposal subtotal
    :type guid: str
    :param body: JSON patch document of ProposalSubtotalModel
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def proposal_subtotals_post_proposal_subtotal(request: web.Request, body=None) -> web.Response:
    """Insert a proposal subtotal

    

    :param body: ProposalSubtotalModel
    :type body: dict | bytes

    """
    body = ProposalSubtotalInputModel.from_dict(body)
    return web.Response(status=200)


async def proposal_workhours_patch_proposal_workhour(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a proposal work row or a part of it.

    

    :param guid: ID of the proposal work row.
    :type guid: str
    :param body: JSON patch document of ProposalWorkhourModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def proposal_workhours_post_proposal_workhour(request: web.Request, body=None) -> web.Response:
    """Insert a proposal work row.

    

    :param body: ProposalWorkhourModel
    :type body: dict | bytes

    """
    body = ProposalWorkhourRowInputModel.from_dict(body)
    return web.Response(status=200)


async def proposals_patch_proposal(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a Proposal or a part of it

    

    :param guid: Guid of the Proposal
    :type guid: str
    :param body: JSON patch document of ProposalInputModel
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def proposals_post_proposal(request: web.Request, body=None) -> web.Response:
    """Insert a proposal.

    

    :param body: ProposalInputModel
    :type body: dict | bytes

    """
    body = ProposalInputModel.from_dict(body)
    return web.Response(status=200)


async def sales_notes_patch_project_sales_note(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a project sales note or a part of it.

    

    :param guid: ID of the project sales note.
    :type guid: str
    :param body: JSON patch document of project sales note model.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def sales_notes_post_project_sales_notes(request: web.Request, body=None) -> web.Response:
    """Insert a project sales note.

    

    :param body: SalesNoteOutputModel
    :type body: dict | bytes

    """
    body = ProjectSalesNoteInputModel.from_dict(body)
    return web.Response(status=200)
