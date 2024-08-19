# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_files_post_project_link(client):
    """Test case for files_post_project_link

    Add a link to a project.
    """
    body = {"lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"fileGuid":"fileGuid","createdDateTime":"2000-01-23T04:56:07.000+00:00","description":"description","isInternal":True,"isReadOnly":True,"size":0.8008281904610115,"createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"projectGuid":"projectGuid","name":"name","guid":"guid","lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00","usages":[{"isReadOnly":True,"name":"name","guid":"guid","type":"Invoice"},{"isReadOnly":True,"name":"name","guid":"guid","type":"Invoice"}],"category":"Misc","contentType":"contentType"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/projectlinks',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_keywords_link_keyword_to_project(client):
    """Test case for keywords_link_keyword_to_project

    Link existing keyword to project
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/projects/{project_guid}/keywords/{guid}'.format(project_guid='project_guid_example', guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_phase_members_post_phase_member(client):
    """Test case for phase_members_post_phase_member

    Adds a phase member.
    """
    body = {"lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"phaseGuid":"phaseGuid","workHoursIncludingChildPhases":6.027456183070403,"createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"workHours":0.8008281904610115,"createdDateTime":"2000-01-23T04:56:07.000+00:00","guid":"guid","lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00","isActive":True,"currentWorkcontractTitle":"currentWorkcontractTitle","user":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"}}
    params = [('addToAllSubPhases', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/phasemembers',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_phase_members_post_phase_members_from_business_unit_users(client):
    """Test case for phase_members_post_phase_members_from_business_unit_users

    Adds business unit users to phase members.
    """
    body = {"phaseGuid":"phaseGuid","businessUnitGuid":"businessUnitGuid"}
    params = [('addToAllSubPhases', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/phasemembersfrombusinessunitusers',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_phases_patch_phase(client):
    """Test case for phases_patch_phase

    Update (Patch) a phase or a part of it
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/phases/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_phases_post_phase(client):
    """Test case for phases_post_phase

    Insert a phase
    """
    body = {"defaultWorkType":{"name":"name","guid":"guid"},"code":"code","workHoursEstimate":1.4658129805029452,"project":{"name":"name","guid":"guid"},"phaseStatus":{"description":"description","phaseStatusTypeGuid":"phaseStatusTypeGuid"},"originalStartDate":"2000-01-23","isClosed":False,"isLocked":False,"sortOrder":6,"name":"name","parentPhase":{"name":"name","guid":"guid"},"originalWorkHoursEstimate":0.8008281904610115,"deadline":"2000-01-23","originalDeadline":"2000-01-23","startDate":"2000-01-23","isCompleted":False}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/phases',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_price_lists_post_custom_pricelist(client):
    """Test case for price_lists_post_custom_pricelist

    Create custom price list for a project. If project already has a custom price list returns existing price list. Creates a new price list if project doesn't have a custom price list. Project can only have one custom price list. Note that project's price list will be changed to the custom price list created here and also existing prices are copied to the new price list.
    """
    params = [('isVolumePricing', False)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/projects/{project_guid}/pricelists/custom'.format(project_guid='project_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_custom_values_patch_project_custom_value(client):
    """Test case for project_custom_values_patch_project_custom_value

    Update (Patch) a project custom value or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/projects/customvalues/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_custom_values_post_project_custom_value(client):
    """Test case for project_custom_values_post_project_custom_value

    Insert a project custom value.
    """
    body = {"lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"projectGuid":"projectGuid","createdDateTime":"2000-01-23T04:56:07.000+00:00","guid":"guid","lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00","value":"value","customProperty":{"name":"name","guid":"guid","type":"Numeric","parameters":"parameters"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/projects/customvalues',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_forecasts_patch_forecast(client):
    """Test case for project_forecasts_patch_forecast

    Update (Patch) an project forecast or a part of it
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/projectforecasts/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_forecasts_post_forecast(client):
    """Test case for project_forecasts_post_forecast

    Insert a project forecast
    """
    body = {"lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"revenueForecast":{"amount":6.027456183070403,"currencyCode":"currencyCode"},"year":2005,"billingForecast":{"amount":6.027456183070403,"currencyCode":"currencyCode"},"createdDateTime":"2000-01-23T04:56:07.000+00:00","project":{"guid":"guid"},"expenseForecast":{"amount":6.027456183070403,"currencyCode":"currencyCode"},"laborExpenseForecastNotes":"laborExpenseForecastNotes","expenseForecastNotes":"expenseForecastNotes","month":1,"createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"laborExpenseForecast":{"amount":6.027456183070403,"currencyCode":"currencyCode"},"guid":"guid","lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00","billingForecastNotes":"billingForecastNotes","revenueForecastNotes":"revenueForecastNotes"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/projectforecasts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_invoice_settings_patch_project_invoice_settings_0(client):
    """Test case for project_invoice_settings_patch_project_invoice_settings_0

    Update (Patch) project invoice settings.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/projectinvoicesettings/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_invoice_settings_post_project_invoice_settings_0(client):
    """Test case for project_invoice_settings_post_project_invoice_settings_0

    Create a new project invoice settings.
    """
    body = {"projectFeeDescriptionFormat":"projectFeeDescriptionFormat","showReferenceNumber":True,"showLogoAndTitle":True,"showAttachmentPriceExcludingValueAddedTax":True,"projectTravelExpensePrimaryGroupBy":"projectTravelExpensePrimaryGroupBy","showQuantity":True,"project":{"guid":"guid"},"htmlText2":{"tagContext":"tagContext","value":"value","allowTags":True},"htmlText1":{"tagContext":"tagContext","value":"value","allowTags":True},"showFooter":True,"freeText1":{"tagContext":"tagContext","value":"value","allowTags":True},"freeText2":{"tagContext":"tagContext","value":"value","allowTags":True},"projectFeeGrouping":"OneByOne","projectTravelExpenseSecondaryGroupBy":"projectTravelExpenseSecondaryGroupBy","showAttachmentUnitPrice":True,"workHourPrimaryGroupBy":"workHourPrimaryGroupBy","showAttachmentValueAddedTax":True,"showPriceExcludingValueAddedTax":True,"showAttachmentUnit":True,"showUnitPrice":True,"workHourDescriptionFormat":"workHourDescriptionFormat","projectFeeSecondaryGroupBy":"projectFeeSecondaryGroupBy","workHourSecondaryGroupBy":"workHourSecondaryGroupBy","showUnit":True,"showCategories":True,"projectTravelExpenseDescriptionFormat":"projectTravelExpenseDescriptionFormat","projectFeePrimaryGroupBy":"projectFeePrimaryGroupBy","showValueAddedTax":True,"style":"BlackAndWhite"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/projectinvoicesettings',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_products_post_project_product(client):
    """Test case for project_products_post_project_product

    Adds a product to a project.
    """
    body = {"product":{"guid":"guid"},"guid":"guid","project":{"guid":"guid"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/projectproducts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_work_hour_prices_patch_project_work_hour_price(client):
    """Test case for project_work_hour_prices_patch_project_work_hour_price

    Update (Patch) a work hour price or a part of it
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/projectworkhourprices/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_work_hour_prices_post_project_work_hour_price(client):
    """Test case for project_work_hour_prices_post_project_work_hour_price

    Insert a work hour price
    """
    body = {"phase":{"guid":"guid"},"unitPrice":{"amount":5.962133916683182,"currencyCode":"currencyCode"},"workType":{"guid":"guid"},"project":{"guid":"guid"},"user":{"guid":"guid"},"isBillable":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/projectworkhourprices',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_work_types_patch_project_worktype(client):
    """Test case for project_work_types_patch_project_worktype

    Update (patch) a project work type.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/projectworktypes/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_work_types_post_project_worktype(client):
    """Test case for project_work_types_post_project_worktype

    Adds a work type to a project.
    """
    body = {"isDefault":True,"projectGuid":"projectGuid","guid":"guid","worktype":{"code":"code","isProductive":True,"name":"name","guid":"guid","isActive":True}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/projectworktypes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_patch_project(client):
    """Test case for projects_patch_project

    Update (Patch) a project or a part of it
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/projects/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_post_project(client):
    """Test case for projects_post_project

    Insert a project
    """
    body = {"businessUnit":{"guid":"guid"},"orderNumber":"orderNumber","billingContact":{"guid":"guid"},"useOvertimeMultipliers":True,"expectedOrderDate":"2000-01-23","description":"description","internalName":"internalName","number":6,"ourReference":"ourReference","customerContact":{"guid":"guid"},"currency":{"guid":"guid"},"deadline":"2000-01-23","completionEstimatePercentage":0,"isJoiningAllowed":True,"useProductsFromSetting":True,"yourReference":"yourReference","costCenter":{"guid":"guid"},"leadSource":{"guid":"guid"},"probability":5,"useWorktypesFromSetting":True,"isInternal":True,"invoiceNotes":"invoiceNotes","projectStatus":{"projectStatusTypeGuid":"projectStatusTypeGuid","description":"description"},"isClosed":True,"expectedValue":{"amount":6.027456183070403,"currencyCode":"currencyCode"},"invoiceTemplate":{"templateInvoiceGuid":"templateInvoiceGuid","guid":"guid"},"name":"name","projectOwner":{"guid":"guid"},"salesPerson":{"guid":"guid"},"salesStatus":{"salesStatusTypeGuid":"salesStatusTypeGuid"},"paymentTerm":1,"startDate":"2000-01-23","customer":{"guid":"guid"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/projects',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proposal_fees_patch_proposal_fee(client):
    """Test case for proposal_fees_patch_proposal_fee

    Update (Patch) a proposal fee row or a part of it
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/proposalfeerows/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proposal_fees_post_proposal_fee(client):
    """Test case for proposal_fees_post_proposal_fee

    Insert a proposal fee row.
    """
    body = {"proposal":{"guid":"guid"},"unitPrice":{"amount":5.962133916683182,"currencyCode":"currencyCode"},"product":{"guid":"guid"},"quantity":0.8008281904610115,"vatRate":1.4658129805029452,"description":"description","isShownOnProposal":True,"measurementUnit":"measurementUnit","subtotal":{"guid":"guid"},"sortOrder":6,"unitCost":{"amount":5.962133916683182,"currencyCode":"currencyCode"},"name":"name","projectFee":{"guid":"guid"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/proposalfeerows',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proposal_settings_patch_proposal_settings(client):
    """Test case for proposal_settings_patch_proposal_settings

    Update (Patch) proposal settings
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/proposals/{guid}/proposalsettings'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proposal_subtotals_patch_proposal_subtotal(client):
    """Test case for proposal_subtotals_patch_proposal_subtotal

    Update (Patch) a Proposal subtotal or a part of it
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/proposalsubtotals/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proposal_subtotals_post_proposal_subtotal(client):
    """Test case for proposal_subtotals_post_proposal_subtotal

    Insert a proposal subtotal
    """
    body = {"phase":{"guid":"guid"},"proposal":{"guid":"guid"},"sortOrder":0,"name":"name","description":"description","isShownOnProposal":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/proposalsubtotals',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proposal_workhours_patch_proposal_workhour(client):
    """Test case for proposal_workhours_patch_proposal_workhour

    Update (Patch) a proposal work row or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/proposalworkrows/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proposal_workhours_post_proposal_workhour(client):
    """Test case for proposal_workhours_post_proposal_workhour

    Insert a proposal work row.
    """
    body = {"phase":{"guid":"guid"},"proposal":{"guid":"guid"},"quantity":0.8008281904610115,"subtotal":{"guid":"guid"},"sortOrder":6,"name":"name","workType":{"guid":"guid"},"description":"description","isShownOnProposal":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/proposalworkrows',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proposals_patch_proposal(client):
    """Test case for proposals_patch_proposal

    Update (Patch) a Proposal or a part of it
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/proposals/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proposals_post_proposal(client):
    """Test case for proposals_post_proposal

    Insert a proposal.
    """
    body = {"freeText1":{"value":"value"},"proposalDate":"2000-01-23","freeText2":{"value":"value"},"customerContactPerson":{"guid":"guid"},"proposalStatus":{"guid":"guid"},"culture":{"guid":"guid"},"name":"name","project":{"guid":"guid"},"language":{"guid":"guid"},"billingAddress":{"guid":"guid"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/proposals',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_notes_patch_project_sales_note(client):
    """Test case for sales_notes_patch_project_sales_note

    Update (Patch) a project sales note or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/projectsalesnotes/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_notes_post_project_sales_notes(client):
    """Test case for sales_notes_post_project_sales_notes

    Insert a project sales note.
    """
    body = {"note":"note","project":{"guid":"guid"},"user":{"guid":"guid"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/projectsalesnotes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

