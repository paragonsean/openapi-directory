# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dfr_rest_services_get_air_compliance_get200_response import DfrRestServicesGetAirComplianceGet200Response
from openapi_server.models.dfr_rest_services_get_air_quality_get200_response import DfrRestServicesGetAirQualityGet200Response
from openapi_server.models.dfr_rest_services_get_aws_docs_get200_response import DfrRestServicesGetAwsDocsGet200Response
from openapi_server.models.dfr_rest_services_get_case_formal_actions_get200_response import DfrRestServicesGetCaseFormalActionsGet200Response
from openapi_server.models.dfr_rest_services_get_compliance_history_get200_response import DfrRestServicesGetComplianceHistoryGet200Response
from openapi_server.models.dfr_rest_services_get_compliance_summary_get200_response import DfrRestServicesGetComplianceSummaryGet200Response
from openapi_server.models.dfr_rest_services_get_cwa3yr_compliance_get200_response import DfrRestServicesGetCwa3yrComplianceGet200Response
from openapi_server.models.dfr_rest_services_get_cwa3yr_d80d90_counts_get200_response import DfrRestServicesGetCwa3yrD80d90CountsGet200Response
from openapi_server.models.dfr_rest_services_get_cwa_cs_compliance_get200_response import DfrRestServicesGetCwaCsComplianceGet200Response
from openapi_server.models.dfr_rest_services_get_cwa_eff_alr_exp_get200_response import DfrRestServicesGetCwaEffAlrExpGet200Response
from openapi_server.models.dfr_rest_services_get_cwa_eff_alr_get200_response import DfrRestServicesGetCwaEffAlrGet200Response
from openapi_server.models.dfr_rest_services_get_cwa_eff_compliance_exp_get200_response import DfrRestServicesGetCwaEffComplianceExpGet200Response
from openapi_server.models.dfr_rest_services_get_cwa_eff_compliance_get200_response import DfrRestServicesGetCwaEffComplianceGet200Response
from openapi_server.models.dfr_rest_services_get_cwa_ps_compliance_get200_response import DfrRestServicesGetCwaPsComplianceGet200Response
from openapi_server.models.dfr_rest_services_get_cwa_rnc_compliance_get200_response import DfrRestServicesGetCwaRncComplianceGet200Response
from openapi_server.models.dfr_rest_services_get_cwa_se_compliance_get200_response import DfrRestServicesGetCwaSeComplianceGet200Response
from openapi_server.models.dfr_rest_services_get_d80d90s_details_get200_response import DfrRestServicesGetD80d90sDetailsGet200Response
from openapi_server.models.dfr_rest_services_get_demographics_by_id_get200_response import DfrRestServicesGetDemographicsByIdGet200Response
from openapi_server.models.dfr_rest_services_get_dfr_get200_response import DfrRestServicesGetDfrGet200Response
from openapi_server.models.dfr_rest_services_get_ejscreen_indexes_get200_response import DfrRestServicesGetEjscreenIndexesGet200Response
from openapi_server.models.dfr_rest_services_get_enforcement_summary_get200_response import DfrRestServicesGetEnforcementSummaryGet200Response
from openapi_server.models.dfr_rest_services_get_extract_dates_get200_response import DfrRestServicesGetExtractDatesGet200Response
from openapi_server.models.dfr_rest_services_get_formal_actions_get200_response import DfrRestServicesGetFormalActionsGet200Response
from openapi_server.models.dfr_rest_services_get_icis_formal_actions_get200_response import DfrRestServicesGetIcisFormalActionsGet200Response
from openapi_server.models.dfr_rest_services_get_inspections_get200_response import DfrRestServicesGetInspectionsGet200Response
from openapi_server.models.dfr_rest_services_get_map_get200_response import DfrRestServicesGetMapGet200Response
from openapi_server.models.dfr_rest_services_get_naics_get200_response import DfrRestServicesGetNaicsGet200Response
from openapi_server.models.dfr_rest_services_get_notices_get200_response import DfrRestServicesGetNoticesGet200Response
from openapi_server.models.dfr_rest_services_get_permits_get200_response import DfrRestServicesGetPermitsGet200Response
from openapi_server.models.dfr_rest_services_get_rcra_compliance_get200_response import DfrRestServicesGetRcraComplianceGet200Response
from openapi_server.models.dfr_rest_services_get_sdwa_lead_and_copper_get200_response import DfrRestServicesGetSdwaLeadAndCopperGet200Response
from openapi_server.models.dfr_rest_services_get_sdwa_sanitary_surveys_get200_response import DfrRestServicesGetSdwaSanitarySurveysGet200Response
from openapi_server.models.dfr_rest_services_get_sdwa_site_visits_get200_response import DfrRestServicesGetSdwaSiteVisitsGet200Response
from openapi_server.models.dfr_rest_services_get_sdwa_violations_get200_response import DfrRestServicesGetSdwaViolationsGet200Response
from openapi_server.models.dfr_rest_services_get_sdwis_compliance_get200_response import DfrRestServicesGetSdwisComplianceGet200Response
from openapi_server.models.dfr_rest_services_get_sic_codes_get200_response import DfrRestServicesGetSicCodesGet200Response
from openapi_server.models.dfr_rest_services_get_spatial_metadata_get200_response import DfrRestServicesGetSpatialMetadataGet200Response
from openapi_server.models.dfr_rest_services_get_tri_history_get200_response import DfrRestServicesGetTriHistoryGet200Response
from openapi_server.models.dfr_rest_services_get_tri_releases_get200_response import DfrRestServicesGetTriReleasesGet200Response
from openapi_server.models.dfr_rest_services_get_tribes_get200_response import DfrRestServicesGetTribesGet200Response
from openapi_server.models.dfr_rest_services_get_water_quality_details_get200_response import DfrRestServicesGetWaterQualityDetailsGet200Response
from openapi_server.models.dfr_rest_services_get_water_quality_get200_response import DfrRestServicesGetWaterQualityGet200Response


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_air3_yr_download_get(client):
    """Test case for dfr_rest_services_air3_yr_download_get

    Downloads the complete Air Compliance History Section of the DFR
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.air_3_yr_download',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_air3_yr_download_post(client):
    """Test case for dfr_rest_services_air3_yr_download_post

    Downloads the complete Air Compliance History Section of the DFR
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.air_3_yr_download',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_cwa3_yr_effluent_download_get(client):
    """Test case for dfr_rest_services_cwa3_yr_effluent_download_get

    Downloads NPDES Effluent Violation Information by month and quarter.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.cwa_3_yr_effluent_download',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_cwa3_yr_effluent_download_post(client):
    """Test case for dfr_rest_services_cwa3_yr_effluent_download_post

    Downloads NPDES Effluent Violation Information by month and quarter.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.cwa_3_yr_effluent_download',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_cwa3_yr_sepscs_download_get(client):
    """Test case for dfr_rest_services_cwa3_yr_sepscs_download_get

    Downloads NPDES Compliance Schedule, Permit Schedule and Single Event Violation Information by month and quarter.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.cwa_3_yr_sepscs_download',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_cwa3_yr_sepscs_download_post(client):
    """Test case for dfr_rest_services_cwa3_yr_sepscs_download_post

    Downloads NPDES Compliance Schedule, Permit Schedule and Single Event Violation Information by month and quarter.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.cwa_3_yr_sepscs_download',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_air_compliance_get(client):
    """Test case for dfr_rest_services_get_air_compliance_get

    Detailed Facility Report Air Compliance Report Service
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_air_compliance',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_air_compliance_post(client):
    """Test case for dfr_rest_services_get_air_compliance_post

    Detailed Facility Report Air Compliance Report Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_air_compliance',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_air_quality_get(client):
    """Test case for dfr_rest_services_get_air_quality_get

    Detailed Facility Report Air Quality Report Service
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_air_quality',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_air_quality_post(client):
    """Test case for dfr_rest_services_get_air_quality_post

    Detailed Facility Report Air Quality Report Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_air_quality',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_aws_docs_get(client):
    """Test case for dfr_rest_services_get_aws_docs_get

    Placeholder
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_aws_docs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_aws_docs_post(client):
    """Test case for dfr_rest_services_get_aws_docs_post

    Placeholder
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_aws_docs',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_case_formal_actions_get(client):
    """Test case for dfr_rest_services_get_case_formal_actions_get

    Displays Cases related to the Facility
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_case_formal_actions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_case_formal_actions_post(client):
    """Test case for dfr_rest_services_get_case_formal_actions_post

    Displays Cases related to the Facility
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_case_formal_actions',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_compliance_history_get(client):
    """Test case for dfr_rest_services_get_compliance_history_get

    Detailed Facility Report 5 Year Compliance Monitoring History Service
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_compliance_history',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_compliance_history_post(client):
    """Test case for dfr_rest_services_get_compliance_history_post

    Detailed Facility Report 5 Year Compliance Monitoring History Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_compliance_history',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_compliance_summary_get(client):
    """Test case for dfr_rest_services_get_compliance_summary_get

    Detailed Facility Report Compliance Summary Service
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_compliance_summary',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_compliance_summary_post(client):
    """Test case for dfr_rest_services_get_compliance_summary_post

    Detailed Facility Report Compliance Summary Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_compliance_summary',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_csv_get(client):
    """Test case for dfr_rest_services_get_csv_get

    Downloads a spectific section  of the DFR in CSV Format
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_csv',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_csv_post(client):
    """Test case for dfr_rest_services_get_csv_post

    Downloads a spectific section  of the DFR in CSV Format
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_csv',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_cwa3yr_compliance_get(client):
    """Test case for dfr_rest_services_get_cwa3yr_compliance_get

    Detailed Facility Report 3 Year CWA Facility-Level Status Service
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_cwa_3yr_compliance',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_cwa3yr_compliance_post(client):
    """Test case for dfr_rest_services_get_cwa3yr_compliance_post

    Detailed Facility Report 3 Year CWA Facility-Level Status Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_cwa_3yr_compliance',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_cwa3yr_d80d90_counts_get(client):
    """Test case for dfr_rest_services_get_cwa3yr_d80d90_counts_get

    Displays monlthly and quarterly counts of D80 and D90 Effluent Non Reporting Violations Related to the Facility
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_cwa_3yr_d80d90_counts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_cwa3yr_d80d90_counts_post(client):
    """Test case for dfr_rest_services_get_cwa3yr_d80d90_counts_post

    Displays monlthly and quarterly counts of D80 and D90 Effluent Non Reporting Violations Related to the Facility
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_cwa_3yr_d80d90_counts',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_cwa_cs_compliance_get(client):
    """Test case for dfr_rest_services_get_cwa_cs_compliance_get

    Detailed Facility Report CWA CSV Compliance Service
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_cwa_cs_compliance',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_cwa_cs_compliance_post(client):
    """Test case for dfr_rest_services_get_cwa_cs_compliance_post

    Detailed Facility Report CWA CSV Compliance Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_cwa_cs_compliance',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_cwa_eff_alr_exp_get(client):
    """Test case for dfr_rest_services_get_cwa_eff_alr_exp_get

    Placeholder
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_cwa_eff_alr_exp',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_cwa_eff_alr_exp_post(client):
    """Test case for dfr_rest_services_get_cwa_eff_alr_exp_post

    Placeholder
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_cwa_eff_alr_exp',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_cwa_eff_alr_get(client):
    """Test case for dfr_rest_services_get_cwa_eff_alr_get

    Detailed Facility Report CWA Effluent ALR Service
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_cwa_eff_alr',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_cwa_eff_alr_post(client):
    """Test case for dfr_rest_services_get_cwa_eff_alr_post

    Detailed Facility Report CWA Effluent ALR Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_cwa_eff_alr',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_cwa_eff_compliance_exp_get(client):
    """Test case for dfr_rest_services_get_cwa_eff_compliance_exp_get

    Placeholder
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_cwa_eff_compliance_exp',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_cwa_eff_compliance_exp_post(client):
    """Test case for dfr_rest_services_get_cwa_eff_compliance_exp_post

    Placeholder
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_cwa_eff_compliance_exp',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_cwa_eff_compliance_get(client):
    """Test case for dfr_rest_services_get_cwa_eff_compliance_get

    Detailed Facility Report CWA Effluent Compliance Service
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_cwa_eff_compliance',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_cwa_eff_compliance_post(client):
    """Test case for dfr_rest_services_get_cwa_eff_compliance_post

    Detailed Facility Report CWA Effluent Compliance Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_cwa_eff_compliance',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_cwa_ps_compliance_get(client):
    """Test case for dfr_rest_services_get_cwa_ps_compliance_get

    Detailed Facility Report CWA PSV Compliance Service
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_cwa_ps_compliance',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_cwa_ps_compliance_post(client):
    """Test case for dfr_rest_services_get_cwa_ps_compliance_post

    Detailed Facility Report CWA PSV Compliance Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_cwa_ps_compliance',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_cwa_rnc_compliance_get(client):
    """Test case for dfr_rest_services_get_cwa_rnc_compliance_get

    Detailed Facility Report CWA RNC Compliance Service
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_cwa_rnc_compliance',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_cwa_rnc_compliance_post(client):
    """Test case for dfr_rest_services_get_cwa_rnc_compliance_post

    Detailed Facility Report CWA RNC Compliance Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_cwa_rnc_compliance',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_cwa_se_compliance_get(client):
    """Test case for dfr_rest_services_get_cwa_se_compliance_get

    Detailed Facility Report CWA SEV Compliance Service
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_cwa_se_compliance',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_cwa_se_compliance_post(client):
    """Test case for dfr_rest_services_get_cwa_se_compliance_post

    Detailed Facility Report CWA SEV Compliance Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_cwa_se_compliance',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_d80d90s_details_get(client):
    """Test case for dfr_rest_services_get_d80d90s_details_get

    Display detailed D80/D90 information for the facility for a given quarter or month
    """
    params = [('output', 'output_example'),
                    ('p_npdes_id', 'p_npdes_id_example'),
                    ('p_missinglate', 'p_missinglate_example'),
                    ('p_qmtype', 'p_qmtype_example'),
                    ('p_qmvalue', 'p_qmvalue_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_d80d90s_details',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_d80d90s_details_post(client):
    """Test case for dfr_rest_services_get_d80d90s_details_post

    Display detailed D80/D90 information for the facility for a given quarter or month
    """
    params = [('output', 'output_example'),
                    ('p_npdes_id', 'p_npdes_id_example'),
                    ('p_missinglate', 'p_missinglate_example'),
                    ('p_qmtype', 'p_qmtype_example'),
                    ('p_qmvalue', 'p_qmvalue_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_d80d90s_details',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_demographics_by_id_get(client):
    """Test case for dfr_rest_services_get_demographics_by_id_get

    Displays 2010 Census and ACS demographics by Facility ID
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_demographics_by_id',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_demographics_by_id_post(client):
    """Test case for dfr_rest_services_get_demographics_by_id_post

    Displays 2010 Census and ACS demographics by Facility ID
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_demographics_by_id',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_dfr_get(client):
    """Test case for dfr_rest_services_get_dfr_get

    Detailed Facility Report Service
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('p_system', 'p_system_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_dfr',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_dfr_post(client):
    """Test case for dfr_rest_services_get_dfr_post

    Detailed Facility Report Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'p_system': 'p_system_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_dfr',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_ejscreen_indexes_get(client):
    """Test case for dfr_rest_services_get_ejscreen_indexes_get

    Detailed Facility Report EJScreen Indexes Service
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_ejscreen_indexes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_ejscreen_indexes_post(client):
    """Test case for dfr_rest_services_get_ejscreen_indexes_post

    Detailed Facility Report EJScreen Indexes Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_ejscreen_indexes',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_enforcement_summary_get(client):
    """Test case for dfr_rest_services_get_enforcement_summary_get

    Detailed Facility Report Enforcement Summary Service
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_enforcement_summary',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_enforcement_summary_post(client):
    """Test case for dfr_rest_services_get_enforcement_summary_post

    Detailed Facility Report Enforcement Summary Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_enforcement_summary',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_extract_dates_get(client):
    """Test case for dfr_rest_services_get_extract_dates_get

    Displays the dates that data was extracted from native EPA systems for the DFR.
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_extract_dates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_extract_dates_post(client):
    """Test case for dfr_rest_services_get_extract_dates_post

    Displays the dates that data was extracted from native EPA systems for the DFR.
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_extract_dates',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_formal_actions_get(client):
    """Test case for dfr_rest_services_get_formal_actions_get

    Detailed Facility Report Formal Actions Service
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_formal_actions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_formal_actions_post(client):
    """Test case for dfr_rest_services_get_formal_actions_post

    Detailed Facility Report Formal Actions Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_formal_actions',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_icis_formal_actions_get(client):
    """Test case for dfr_rest_services_get_icis_formal_actions_get

    Detailed Facility Report ICIS Formal Actions Service
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_icis_formal_actions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_icis_formal_actions_post(client):
    """Test case for dfr_rest_services_get_icis_formal_actions_post

    Detailed Facility Report ICIS Formal Actions Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_icis_formal_actions',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_inspections_get(client):
    """Test case for dfr_rest_services_get_inspections_get

    Detailed Facility Report Inspections Summary Service
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_inspections',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_inspections_post(client):
    """Test case for dfr_rest_services_get_inspections_post

    Detailed Facility Report Inspections Summary Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_inspections',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_map_get(client):
    """Test case for dfr_rest_services_get_map_get

    Detailed Facility Report Map Service
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_map',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_map_post(client):
    """Test case for dfr_rest_services_get_map_post

    Detailed Facility Report Map Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_map',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_naics_get(client):
    """Test case for dfr_rest_services_get_naics_get

    Detailed Facility Report NAICS Code Service
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_naics',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_naics_post(client):
    """Test case for dfr_rest_services_get_naics_post

    Detailed Facility Report NAICS Code Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_naics',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_notices_get(client):
    """Test case for dfr_rest_services_get_notices_get

    Detailed Facility Report Notices Service
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_notices',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_notices_post(client):
    """Test case for dfr_rest_services_get_notices_post

    Detailed Facility Report Notices Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_notices',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_permits_get(client):
    """Test case for dfr_rest_services_get_permits_get

    Detailed Facility Report Permits Service
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_permits',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_permits_post(client):
    """Test case for dfr_rest_services_get_permits_post

    Detailed Facility Report Permits Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_permits',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_rcra_compliance_get(client):
    """Test case for dfr_rest_services_get_rcra_compliance_get

    Detailed Facility Report RCRA Compliance Service
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_rcra_compliance',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_rcra_compliance_post(client):
    """Test case for dfr_rest_services_get_rcra_compliance_post

    Detailed Facility Report RCRA Compliance Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_rcra_compliance',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_sdwa_lead_and_copper_get(client):
    """Test case for dfr_rest_services_get_sdwa_lead_and_copper_get

    Detailed Facility Report SDWA Lead and Copper Service
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_sdwa_lead_and_copper',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_sdwa_lead_and_copper_post(client):
    """Test case for dfr_rest_services_get_sdwa_lead_and_copper_post

    Detailed Facility Report SDWA Lead and Copper Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_sdwa_lead_and_copper',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_sdwa_sanitary_surveys_get(client):
    """Test case for dfr_rest_services_get_sdwa_sanitary_surveys_get

    Detailed Facility Report SDWA Sanitary Surveys Service
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_sdwa_sanitary_surveys',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_sdwa_sanitary_surveys_post(client):
    """Test case for dfr_rest_services_get_sdwa_sanitary_surveys_post

    Detailed Facility Report SDWA Sanitary Surveys Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_sdwa_sanitary_surveys',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_sdwa_site_visits_get(client):
    """Test case for dfr_rest_services_get_sdwa_site_visits_get

    Detailed Facility Report SDWA Sanitary Site Visits Service
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_sdwa_site_visits',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_sdwa_site_visits_post(client):
    """Test case for dfr_rest_services_get_sdwa_site_visits_post

    Detailed Facility Report SDWA Sanitary Site Visits Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_sdwa_site_visits',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_sdwa_violations_get(client):
    """Test case for dfr_rest_services_get_sdwa_violations_get

    Detailed Facility Report SDWA Violations Service
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_sdwa_violations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_sdwa_violations_post(client):
    """Test case for dfr_rest_services_get_sdwa_violations_post

    Detailed Facility Report SDWA Violations Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_sdwa_violations',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_sdwis_compliance_get(client):
    """Test case for dfr_rest_services_get_sdwis_compliance_get

    Detailed Facility Report SDWIS Compliance Service
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_sdwis_compliance',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_sdwis_compliance_post(client):
    """Test case for dfr_rest_services_get_sdwis_compliance_post

    Detailed Facility Report SDWIS Compliance Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_sdwis_compliance',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_sic_codes_get(client):
    """Test case for dfr_rest_services_get_sic_codes_get

    Detailed Facility Report SIC Code Service
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_sic_codes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_sic_codes_post(client):
    """Test case for dfr_rest_services_get_sic_codes_post

    Detailed Facility Report SIC Code Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_sic_codes',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_spatial_metadata_get(client):
    """Test case for dfr_rest_services_get_spatial_metadata_get

    Detailed Facility Report Spatial Metadata Service
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_spatial_metadata',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_spatial_metadata_post(client):
    """Test case for dfr_rest_services_get_spatial_metadata_post

    Detailed Facility Report Spatial Metadata Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_spatial_metadata',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_tri_history_get(client):
    """Test case for dfr_rest_services_get_tri_history_get

    Detailed Facility Report TRI History Service
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_tri_history',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_tri_history_post(client):
    """Test case for dfr_rest_services_get_tri_history_post

    Detailed Facility Report TRI History Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_tri_history',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_tri_releases_get(client):
    """Test case for dfr_rest_services_get_tri_releases_get

    Detailed Facility Report TRI Releases Service
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_tri_releases',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_tri_releases_post(client):
    """Test case for dfr_rest_services_get_tri_releases_post

    Detailed Facility Report TRI Releases Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_tri_releases',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_tribes_get(client):
    """Test case for dfr_rest_services_get_tribes_get

    Detailed Facility Report Tribes Service
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_tribes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_tribes_post(client):
    """Test case for dfr_rest_services_get_tribes_post

    Detailed Facility Report Tribes Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_tribes',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_water_quality_details_get(client):
    """Test case for dfr_rest_services_get_water_quality_details_get

    Displays detailed Water Quality information from EPA's Office of Water Systems
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_water_quality_details',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_water_quality_details_post(client):
    """Test case for dfr_rest_services_get_water_quality_details_post

    Displays detailed Water Quality information from EPA's Office of Water Systems
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_water_quality_details',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_get_water_quality_get(client):
    """Test case for dfr_rest_services_get_water_quality_get

    Detailed Facility Report Water Quality Service
    """
    params = [('output', 'output_example'),
                    ('p_id', 'p_id_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.get_water_quality',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_dfr_rest_services_get_water_quality_post(client):
    """Test case for dfr_rest_services_get_water_quality_post

    Detailed Facility Report Water Quality Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_id': 'p_id_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.get_water_quality',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_rcra3_yr_download_get(client):
    """Test case for dfr_rest_services_rcra3_yr_download_get

    Downloads the complete RCRA Compliance History Section of the DFR
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/dfr_rest_services.rcra_3_yr_download',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfr_rest_services_rcra3_yr_download_post(client):
    """Test case for dfr_rest_services_rcra3_yr_download_post

    Downloads the complete RCRA Compliance History Section of the DFR
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/echo/dfr_rest_services.rcra_3_yr_download',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

