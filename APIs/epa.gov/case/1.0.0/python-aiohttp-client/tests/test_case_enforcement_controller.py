# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.case_rest_services_get_case_info_get200_response import CaseRestServicesGetCaseInfoGet200Response
from openapi_server.models.case_rest_services_get_case_report_get200_response import CaseRestServicesGetCaseReportGet200Response
from openapi_server.models.case_rest_services_get_cases_from_facility_get200_response import CaseRestServicesGetCasesFromFacilityGet200Response
from openapi_server.models.case_rest_services_get_cases_get200_response import CaseRestServicesGetCasesGet200Response
from openapi_server.models.case_rest_services_get_crcase_report_get200_response import CaseRestServicesGetCrcaseReportGet200Response
from openapi_server.models.case_rest_services_get_facilities_from_case_get200_response import CaseRestServicesGetFacilitiesFromCaseGet200Response
from openapi_server.models.case_rest_services_get_map_get200_response import CaseRestServicesGetMapGet200Response
from openapi_server.models.case_rest_services_get_qid_get200_response import CaseRestServicesGetQidGet200Response


pytestmark = pytest.mark.asyncio

async def test_case_rest_services_get_case_info_get(client):
    """Test case for case_rest_services_get_case_info_get

    Enforcement Case Search (new version)
    """
    params = [('output', 'output_example'),
                    ('p_case_category', 'p_case_category_example'),
                    ('p_case_status', 'p_case_status_example'),
                    ('p_milestone', 'p_milestone_example'),
                    ('p_from_date', 'p_from_date_example'),
                    ('p_to_date', 'p_to_date_example'),
                    ('p_milestone_fy', 'p_milestone_fy_example'),
                    ('p_name', 'p_name_example'),
                    ('p_name_type', 'p_name_type_example'),
                    ('p_case_number', 'p_case_number_example'),
                    ('p_docket_number', 'p_docket_number_example'),
                    ('p_court_docket_number', 'p_court_docket_number_example'),
                    ('p_activity_number', 'p_activity_number_example'),
                    ('p_case_lead', 'p_case_lead_example'),
                    ('p_case_sens_flg', 'p_case_sens_flg_example'),
                    ('p_region', 'p_region_example'),
                    ('p_state', 'p_state_example'),
                    ('p_district', 'p_district_example'),
                    ('p_sic', 'p_sic_example'),
                    ('p_sic_ao_naics', 'p_sic_ao_naics_example'),
                    ('p_sic_primary_flg', 'p_sic_primary_flg_example'),
                    ('p_sic_frs_flg', 'p_sic_frs_flg_example'),
                    ('p_naics', 'p_naics_example'),
                    ('p_naics_primary_flg', 'p_naics_primary_flg_example'),
                    ('p_naics_frs_flg', 'p_naics_frs_flg_example'),
                    ('p_enf_type', 'p_enf_type_example'),
                    ('p_law', 'p_law_example'),
                    ('p_section', 'p_section_example'),
                    ('p_cp_citation', 'p_cp_citation_example'),
                    ('p_rank_order', 'p_rank_order_example'),
                    ('p_enf_program', 'p_enf_program_example'),
                    ('p_violation', 'p_violation_example'),
                    ('p_priority_area', 'p_priority_area_example'),
                    ('p_priority_area_desc', 'p_priority_area_desc_example'),
                    ('p_tribal', 'p_tribal_example'),
                    ('p_oeca_core', 'p_oeca_core_example'),
                    ('p_multimedia', 'p_multimedia_example'),
                    ('p_fed_case', 'p_fed_case_example'),
                    ('p_activity_contact', 'p_activity_contact_example'),
                    ('p_role', 'p_role_example'),
                    ('p_fed_penalty', 'p_fed_penalty_example'),
                    ('p_total_fed_penalty', 'p_total_fed_penalty_example'),
                    ('p_cost_recovery', 'p_cost_recovery_example'),
                    ('p_total_cost_recovery', 'p_total_cost_recovery_example'),
                    ('p_complying_actions', 'p_complying_actions_example'),
                    ('p_comp_act_val', 'p_comp_act_val_example'),
                    ('p_total_comp_act_val', 'p_total_comp_act_val_example'),
                    ('p_sep_cats', 'p_sep_cats_example'),
                    ('p_sep_val', 'p_sep_val_example'),
                    ('p_total_sep_val', 'p_total_sep_val_example'),
                    ('p_lodged_date', 'p_lodged_date_example'),
                    ('p_entered_date', 'p_entered_date_example'),
                    ('p_facility_id', 'p_facility_id_example'),
                    ('p_fac_city', 'p_fac_city_example'),
                    ('p_fac_zip', 'p_fac_zip_example'),
                    ('p_fac_county', 'p_fac_county_example'),
                    ('p_case_summary', 'p_case_summary_example'),
                    ('p_case_summary_type', 'p_case_summary_type_example'),
                    ('p_usmex', 'p_usmex_example'),
                    ('p_c1lat', 3.4),
                    ('p_c1lon', 3.4),
                    ('p_c2lat', 3.4),
                    ('p_c2lon', 3.4),
                    ('p_voluntary', 'p_voluntary_example'),
                    ('p_fed_indicator', 'p_fed_indicator_example'),
                    ('p_fntype', 'p_fntype_example'),
                    ('p_civil_criminal_indicator', 'p_civil_criminal_indicator_example'),
                    ('queryset', 3.4),
                    ('responseset', 3.4),
                    ('mapset', '1400'),
                    ('callback', 'param_callback_example'),
                    ('qcolumns', 'qcolumns_example'),
                    ('p_pretty_print', 3.4),
                    ('p_ocmap_fy', 'p_ocmap_fy_example'),
                    ('p_qs', 'p_qs_example'),
                    ('p_has_map', 'p_has_map_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/case_rest_services.get_case_info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_case_rest_services_get_case_info_post(client):
    """Test case for case_rest_services_get_case_info_post

    Enforcement Case Search (new version)
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_case_category': 'p_case_category_example',
        'p_case_status': 'p_case_status_example',
        'p_milestone': 'p_milestone_example',
        'p_from_date': 'p_from_date_example',
        'p_to_date': 'p_to_date_example',
        'p_milestone_fy': 'p_milestone_fy_example',
        'p_name': 'p_name_example',
        'p_name_type': 'p_name_type_example',
        'p_case_number': 'p_case_number_example',
        'p_docket_number': 'p_docket_number_example',
        'p_court_docket_number': 'p_court_docket_number_example',
        'p_activity_number': 'p_activity_number_example',
        'p_case_lead': 'p_case_lead_example',
        'p_case_sens_flg': 'p_case_sens_flg_example',
        'p_region': 'p_region_example',
        'p_state': 'p_state_example',
        'p_district': 'p_district_example',
        'p_sic': 'p_sic_example',
        'p_sic_ao_naics': 'p_sic_ao_naics_example',
        'p_sic_primary_flg': 'p_sic_primary_flg_example',
        'p_sic_frs_flg': 'p_sic_frs_flg_example',
        'p_naics': 'p_naics_example',
        'p_naics_primary_flg': 'p_naics_primary_flg_example',
        'p_naics_frs_flg': 'p_naics_frs_flg_example',
        'p_enf_type': 'p_enf_type_example',
        'p_law': 'p_law_example',
        'p_section': 'p_section_example',
        'p_cp_citation': 'p_cp_citation_example',
        'p_rank_order': 'p_rank_order_example',
        'p_enf_program': 'p_enf_program_example',
        'p_violation': 'p_violation_example',
        'p_priority_area': 'p_priority_area_example',
        'p_priority_area_desc': 'p_priority_area_desc_example',
        'p_tribal': 'p_tribal_example',
        'p_oeca_core': 'p_oeca_core_example',
        'p_multimedia': 'p_multimedia_example',
        'p_fed_case': 'p_fed_case_example',
        'p_activity_contact': 'p_activity_contact_example',
        'p_role': 'p_role_example',
        'p_fed_penalty': 'p_fed_penalty_example',
        'p_total_fed_penalty': 'p_total_fed_penalty_example',
        'p_cost_recovery': 'p_cost_recovery_example',
        'p_total_cost_recovery': 'p_total_cost_recovery_example',
        'p_complying_actions': 'p_complying_actions_example',
        'p_comp_act_val': 'p_comp_act_val_example',
        'p_total_comp_act_val': 'p_total_comp_act_val_example',
        'p_sep_cats': 'p_sep_cats_example',
        'p_sep_val': 'p_sep_val_example',
        'p_total_sep_val': 'p_total_sep_val_example',
        'p_lodged_date': 'p_lodged_date_example',
        'p_entered_date': 'p_entered_date_example',
        'p_facility_id': 'p_facility_id_example',
        'p_fac_city': 'p_fac_city_example',
        'p_fac_zip': 'p_fac_zip_example',
        'p_fac_county': 'p_fac_county_example',
        'p_case_summary': 'p_case_summary_example',
        'p_case_summary_type': 'p_case_summary_type_example',
        'p_usmex': 'p_usmex_example',
        'p_c1lat': 3.4,
        'p_c1lon': 3.4,
        'p_c2lat': 3.4,
        'p_c2lon': 3.4,
        'p_voluntary': 'p_voluntary_example',
        'p_fed_indicator': 'p_fed_indicator_example',
        'p_fntype': 'p_fntype_example',
        'p_civil_criminal_indicator': 'p_civil_criminal_indicator_example',
        'queryset': 3.4,
        'responseset': 3.4,
        'mapset': '1400',
        'param_callback': 'param_callback_example',
        'qcolumns': 'qcolumns_example',
        'p_pretty_print': 3.4,
        'p_ocmap_fy': 'p_ocmap_fy_example',
        'p_qs': 'p_qs_example',
        'p_has_map': 'p_has_map_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/case_rest_services.get_case_info',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_case_rest_services_get_case_report_get(client):
    """Test case for case_rest_services_get_case_report_get

    Enforcement Case Summary Report Search
    """
    params = [('p_id', 'p_id_example'),
                    ('output', 'output_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/case_rest_services.get_case_report',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_case_rest_services_get_case_report_post(client):
    """Test case for case_rest_services_get_case_report_post

    Enforcement Case Summary Report Search
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'p_id': 'p_id_example',
        'output': 'output_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/case_rest_services.get_case_report',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_case_rest_services_get_cases_from_facility_get(client):
    """Test case for case_rest_services_get_cases_from_facility_get

    Placeholder
    """
    params = [('p_id', 'p_id_example'),
                    ('output', 'output_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/case_rest_services.get_cases_from_facility',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_case_rest_services_get_cases_from_facility_post(client):
    """Test case for case_rest_services_get_cases_from_facility_post

    Placeholder
    """
    params = [('p_id', 'p_id_example'),
                    ('output', 'output_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/echo/case_rest_services.get_cases_from_facility',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_case_rest_services_get_cases_get(client):
    """Test case for case_rest_services_get_cases_get

    Enforcement Case Search
    """
    params = [('output', 'output_example'),
                    ('p_case_category', 'p_case_category_example'),
                    ('p_case_status', 'p_case_status_example'),
                    ('p_violation', 'p_violation_example'),
                    ('p_milestone', 'p_milestone_example'),
                    ('p_from_date', 'p_from_date_example'),
                    ('p_to_date', 'p_to_date_example'),
                    ('p_milestone_fy', 'p_milestone_fy_example'),
                    ('p_name', 'p_name_example'),
                    ('p_name_type', 'p_name_type_example'),
                    ('p_case_number', 'p_case_number_example'),
                    ('p_docket_number', 'p_docket_number_example'),
                    ('p_court_docket_number', 'p_court_docket_number_example'),
                    ('p_activity_number', 'p_activity_number_example'),
                    ('p_case_lead', 'p_case_lead_example'),
                    ('p_case_sens_flg', 'p_case_sens_flg_example'),
                    ('p_region', 'p_region_example'),
                    ('p_state', 'p_state_example'),
                    ('p_district', 'p_district_example'),
                    ('p_sic', 'p_sic_example'),
                    ('p_sic_ao_naics', 'p_sic_ao_naics_example'),
                    ('p_sic_primary_flg', 'p_sic_primary_flg_example'),
                    ('p_sic_frs_flg', 'p_sic_frs_flg_example'),
                    ('p_naics', 'p_naics_example'),
                    ('p_naics_primary_flg', 'p_naics_primary_flg_example'),
                    ('p_naics_frs_flg', 'p_naics_frs_flg_example'),
                    ('p_enf_type', 'p_enf_type_example'),
                    ('p_law', 'p_law_example'),
                    ('p_section', 'p_section_example'),
                    ('p_cp_citation', 'p_cp_citation_example'),
                    ('p_rank_order', 'p_rank_order_example'),
                    ('p_enf_program', 'p_enf_program_example'),
                    ('p_priority_area', 'p_priority_area_example'),
                    ('p_priority_area_desc', 'p_priority_area_desc_example'),
                    ('p_tribal', 'p_tribal_example'),
                    ('p_oeca_core', 'p_oeca_core_example'),
                    ('p_multimedia', 'p_multimedia_example'),
                    ('p_fed_case', 'p_fed_case_example'),
                    ('p_activity_contact', 'p_activity_contact_example'),
                    ('p_role', 'p_role_example'),
                    ('p_fed_penalty', 'p_fed_penalty_example'),
                    ('p_total_fed_penalty', 'p_total_fed_penalty_example'),
                    ('p_cost_recovery', 'p_cost_recovery_example'),
                    ('p_total_cost_recovery', 'p_total_cost_recovery_example'),
                    ('p_complying_actions', 'p_complying_actions_example'),
                    ('p_comp_act_val', 'p_comp_act_val_example'),
                    ('p_total_comp_act_val', 'p_total_comp_act_val_example'),
                    ('p_sep_cats', 'p_sep_cats_example'),
                    ('p_sep_val', 'p_sep_val_example'),
                    ('p_total_sep_val', 'p_total_sep_val_example'),
                    ('p_lodged_date', 'p_lodged_date_example'),
                    ('p_entered_date', 'p_entered_date_example'),
                    ('p_facility_id', 'p_facility_id_example'),
                    ('p_fac_city', 'p_fac_city_example'),
                    ('p_fac_zip', 'p_fac_zip_example'),
                    ('p_fac_county', 'p_fac_county_example'),
                    ('p_case_summary', 'p_case_summary_example'),
                    ('p_case_summary_type', 'p_case_summary_type_example'),
                    ('p_usmex', 'p_usmex_example'),
                    ('p_c1lat', 3.4),
                    ('p_c1lon', 3.4),
                    ('p_c2lat', 3.4),
                    ('p_c2lon', 3.4),
                    ('p_voluntary', 'p_voluntary_example'),
                    ('p_fed_indicator', 'p_fed_indicator_example'),
                    ('p_fntype', 'p_fntype_example'),
                    ('p_civil_criminal_indicator', 'p_civil_criminal_indicator_example'),
                    ('queryset', 3.4),
                    ('responseset', 3.4),
                    ('maplist', 'maplist_example'),
                    ('tablelist', 'tablelist_example'),
                    ('callback', 'param_callback_example'),
                    ('qcolumns', 'qcolumns_example'),
                    ('p_ocmap_fy', 'p_ocmap_fy_example'),
                    ('p_qs', 'p_qs_example'),
                    ('p_has_map', 'p_has_map_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/case_rest_services.get_cases',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_case_rest_services_get_cases_post(client):
    """Test case for case_rest_services_get_cases_post

    Enforcement Case Search
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_case_category': 'p_case_category_example',
        'p_case_status': 'p_case_status_example',
        'p_milestone': 'p_milestone_example',
        'p_from_date': 'p_from_date_example',
        'p_to_date': 'p_to_date_example',
        'p_milestone_fy': 'p_milestone_fy_example',
        'p_name': 'p_name_example',
        'p_name_type': 'p_name_type_example',
        'p_case_number': 'p_case_number_example',
        'p_docket_number': 'p_docket_number_example',
        'p_court_docket_number': 'p_court_docket_number_example',
        'p_activity_number': 'p_activity_number_example',
        'p_case_lead': 'p_case_lead_example',
        'p_case_sens_flg': 'p_case_sens_flg_example',
        'p_region': 'p_region_example',
        'p_state': 'p_state_example',
        'p_district': 'p_district_example',
        'p_sic': 'p_sic_example',
        'p_sic_ao_naics': 'p_sic_ao_naics_example',
        'p_sic_primary_flg': 'p_sic_primary_flg_example',
        'p_sic_frs_flg': 'p_sic_frs_flg_example',
        'p_naics': 'p_naics_example',
        'p_naics_primary_flg': 'p_naics_primary_flg_example',
        'p_naics_frs_flg': 'p_naics_frs_flg_example',
        'p_enf_type': 'p_enf_type_example',
        'p_law': 'p_law_example',
        'p_section': 'p_section_example',
        'p_cp_citation': 'p_cp_citation_example',
        'p_rank_order': 'p_rank_order_example',
        'p_enf_program': 'p_enf_program_example',
        'p_violation': 'p_violation_example',
        'p_priority_area': 'p_priority_area_example',
        'p_priority_area_desc': 'p_priority_area_desc_example',
        'p_tribal': 'p_tribal_example',
        'p_oeca_core': 'p_oeca_core_example',
        'p_multimedia': 'p_multimedia_example',
        'p_fed_case': 'p_fed_case_example',
        'p_activity_contact': 'p_activity_contact_example',
        'p_role': 'p_role_example',
        'p_fed_penalty': 'p_fed_penalty_example',
        'p_total_fed_penalty': 'p_total_fed_penalty_example',
        'p_cost_recovery': 'p_cost_recovery_example',
        'p_total_cost_recovery': 'p_total_cost_recovery_example',
        'p_complying_actions': 'p_complying_actions_example',
        'p_comp_act_val': 'p_comp_act_val_example',
        'p_total_comp_act_val': 'p_total_comp_act_val_example',
        'p_sep_cats': 'p_sep_cats_example',
        'p_sep_val': 'p_sep_val_example',
        'p_total_sep_val': 'p_total_sep_val_example',
        'p_lodged_date': 'p_lodged_date_example',
        'p_entered_date': 'p_entered_date_example',
        'p_facility_id': 'p_facility_id_example',
        'p_fac_city': 'p_fac_city_example',
        'p_fac_zip': 'p_fac_zip_example',
        'p_fac_county': 'p_fac_county_example',
        'p_case_summary': 'p_case_summary_example',
        'p_case_summary_type': 'p_case_summary_type_example',
        'p_usmex': 'p_usmex_example',
        'p_c1lat': 3.4,
        'p_c1lon': 3.4,
        'p_c2lat': 3.4,
        'p_c2lon': 3.4,
        'p_voluntary': 'p_voluntary_example',
        'p_fed_indicator': 'p_fed_indicator_example',
        'p_fntype': 'p_fntype_example',
        'p_civil_criminal_indicator': 'p_civil_criminal_indicator_example',
        'queryset': 3.4,
        'responseset': 3.4,
        'maplist': 'maplist_example',
        'tablelist': 'tablelist_example',
        'param_callback': 'param_callback_example',
        'qcolumns': 'qcolumns_example',
        'p_ocmap_fy': 'p_ocmap_fy_example',
        'p_qs': 'p_qs_example',
        'p_has_map': 'p_has_map_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/case_rest_services.get_cases',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_case_rest_services_get_crcase_report_get(client):
    """Test case for case_rest_services_get_crcase_report_get

    Enforcement Criminal Case Summary Report Search
    """
    params = [('p_id', 'p_id_example'),
                    ('output', 'output_example'),
                    ('callback', 'param_callback_example'),
                    ('mapset', '1400')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/case_rest_services.get_crcase_report',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_case_rest_services_get_crcase_report_post(client):
    """Test case for case_rest_services_get_crcase_report_post

    Enforcement Criminal Case Summary Report Search
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'p_id': 'p_id_example',
        'output': 'output_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/case_rest_services.get_crcase_report',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_case_rest_services_get_download_get(client):
    """Test case for case_rest_services_get_download_get

    Enforcement Case Download Data Service
    """
    params = [('output', 'output_example'),
                    ('qid', 'qid_example'),
                    ('qcolumns', 'qcolumns_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/case_rest_services.get_download',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_case_rest_services_get_download_post(client):
    """Test case for case_rest_services_get_download_post

    Enforcement Case Download Data Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'qid': 'qid_example',
        'qcolumns': 'qcolumns_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/case_rest_services.get_download',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_case_rest_services_get_facilities_from_case_get(client):
    """Test case for case_rest_services_get_facilities_from_case_get

    Placeholder
    """
    params = [('p_id', 'p_id_example'),
                    ('output', 'output_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/case_rest_services.get_facilities_from_case',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_case_rest_services_get_facilities_from_case_post(client):
    """Test case for case_rest_services_get_facilities_from_case_post

    Placeholder
    """
    params = [('p_id', 'p_id_example'),
                    ('output', 'output_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/echo/case_rest_services.get_facilities_from_case',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_case_rest_services_get_map_get(client):
    """Test case for case_rest_services_get_map_get

    Enforcement Case Map Service
    """
    params = [('output', 'output_example'),
                    ('qid', 'qid_example'),
                    ('callback', 'param_callback_example'),
                    ('tablelist', 'tablelist_example'),
                    ('c1_lat', 3.4),
                    ('c1_long', 3.4),
                    ('c2_lat', 3.4),
                    ('c2_long', 3.4)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/case_rest_services.get_map',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_case_rest_services_get_map_post(client):
    """Test case for case_rest_services_get_map_post

    Enforcement Case Map Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'qid': 'qid_example',
        'param_callback': 'param_callback_example',
        'tablelist': 'tablelist_example',
        'c1_lat': 3.4,
        'c1_long': 3.4,
        'c2_lat': 3.4,
        'c2_long': 3.4,
        'mapset': '1400'
        }
    response = await client.request(
        method='POST',
        path='/echo/case_rest_services.get_map',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_case_rest_services_get_qid_get(client):
    """Test case for case_rest_services_get_qid_get

    Enforcement Case Paginated Results Service
    """
    params = [('output', 'output_example'),
                    ('qid', 'qid_example'),
                    ('pageno', 1.0),
                    ('callback', 'param_callback_example'),
                    ('newsort', 3.4),
                    ('descending', 'descending_example'),
                    ('qcolumns', 'qcolumns_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/case_rest_services.get_qid',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_case_rest_services_get_qid_post(client):
    """Test case for case_rest_services_get_qid_post

    Enforcement Case Paginated Results Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'qid': 'qid_example',
        'pageno': 1.0,
        'param_callback': 'param_callback_example',
        'newsort': 3.4,
        'descending': 'descending_example',
        'qcolumns': 'qcolumns_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/case_rest_services.get_qid',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

