# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.air_rest_services_get_facilities_get200_response import AirRestServicesGetFacilitiesGet200Response
from openapi_server.models.air_rest_services_get_facility_info_get200_response import AirRestServicesGetFacilityInfoGet200Response
from openapi_server.models.air_rest_services_get_geojson_get200_response import AirRestServicesGetGeojsonGet200Response
from openapi_server.models.air_rest_services_get_map_get200_response import AirRestServicesGetMapGet200Response
from openapi_server.models.air_rest_services_get_qid_get200_response import AirRestServicesGetQidGet200Response


pytestmark = pytest.mark.asyncio

async def test_air_rest_services_get_download_get(client):
    """Test case for air_rest_services_get_download_get

    Clean Air Act Download Data Service
    """
    params = [('output', 'output_example'),
                    ('qid', 'qid_example'),
                    ('qcolumns', 'qcolumns_example'),
                    ('p_pretty_print', 3.4)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/air_rest_services.get_download',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_air_rest_services_get_download_post(client):
    """Test case for air_rest_services_get_download_post

    Clean Air Act Download Data Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'qid': 'qid_example',
        'qcolumns': 'qcolumns_example',
        'p_pretty_print': 3.4
        }
    response = await client.request(
        method='POST',
        path='/echo/air_rest_services.get_download',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_air_rest_services_get_facilities_get(client):
    """Test case for air_rest_services_get_facilities_get

    Clean Air Act Facility Search
    """
    params = [('output', 'output_example'),
                    ('p_fn', 'p_fn_example'),
                    ('p_sa', 'p_sa_example'),
                    ('p_sa1', 'p_sa1_example'),
                    ('p_ct', 'p_ct_example'),
                    ('p_co', 'p_co_example'),
                    ('p_fips', 'p_fips_example'),
                    ('p_st', 'p_st_example'),
                    ('p_zip', 'p_zip_example'),
                    ('p_lcon', 'p_lcon_example'),
                    ('p_frs', 'p_frs_example'),
                    ('p_reg', 'p_reg_example'),
                    ('p_sic', 'p_sic_example'),
                    ('p_ncs', 'p_ncs_example'),
                    ('p_qnc', 3.4),
                    ('p_pen', 'p_pen_example'),
                    ('p_opst', 'p_opst_example'),
                    ('p_c1lat', 3.4),
                    ('p_c1lon', 3.4),
                    ('p_c2lat', 3.4),
                    ('p_c2lon', 3.4),
                    ('p_usmex', 'p_usmex_example'),
                    ('p_sic2', 'p_sic2_example'),
                    ('p_sic4', 'p_sic4_example'),
                    ('p_fa', 'p_fa_example'),
                    ('p_act', 'p_act_example'),
                    ('p_maj', 'p_maj_example'),
                    ('p_mact', 'p_mact_example'),
                    ('p_nsps', 'p_nsps_example'),
                    ('p_nspsm', 'p_nspsm_example'),
                    ('p_prog', 'p_prog_example'),
                    ('p_fea', 'p_fea_example'),
                    ('p_feay', 3.4),
                    ('p_feaa', 'p_feaa_example'),
                    ('p_iea', 'p_iea_example'),
                    ('p_ieay', 3.4),
                    ('p_ieaa', 'p_ieaa_example'),
                    ('p_qiv', 'p_qiv_example'),
                    ('p_naa', 'p_naa_example'),
                    ('p_impw', 'p_impw_example'),
                    ('p_trep', 'p_trep_example'),
                    ('p_tri_cat', 'p_tri_cat_example'),
                    ('p_tri_amt', 'p_tri_amt_example'),
                    ('p_tri_any_amt', 3.4),
                    ('p_tri_pol', 'p_tri_pol_example'),
                    ('p_ghg_cat', 'p_ghg_cat_example'),
                    ('p_ghg_amt', 'p_ghg_amt_example'),
                    ('p_ghg_any_amt', 3.4),
                    ('p_ghg_yr', 'p_ghg_yr_example'),
                    ('p_nei_pol', 'p_nei_pol_example'),
                    ('p_nei_amt', 'p_nei_amt_example'),
                    ('p_nei_any_amt', 3.4),
                    ('p_nei_yr', 'p_nei_yr_example'),
                    ('p_nei_cat', 'p_nei_cat_example'),
                    ('p_pm', 'p_pm_example'),
                    ('p_pd', 'p_pd_example'),
                    ('p_ico', 'p_ico_example'),
                    ('p_huc', 'p_huc_example'),
                    ('p_wbd', 'p_wbd_example'),
                    ('p_pid', 'p_pid_example'),
                    ('p_med', 'p_med_example'),
                    ('p_ysl', 'p_ysl_example'),
                    ('p_ysly', 3.4),
                    ('p_ysla', 'p_ysla_example'),
                    ('p_stsl', 'p_stsl_example'),
                    ('p_stsly', 3.4),
                    ('p_stsla', 'p_stsla_example'),
                    ('p_stres', 'p_stres_example'),
                    ('p_sttyp', 'p_sttyp_example'),
                    ('p_qs', 'p_qs_example'),
                    ('p_sfs', 'p_sfs_example'),
                    ('p_tribeid', 3.4),
                    ('p_tribename', 'p_tribename_example'),
                    ('p_tribedist', 3.4),
                    ('p_owop', 'p_owop_example'),
                    ('p_agoo', 'p_agoo_example'),
                    ('p_idt1', 'p_idt1_example'),
                    ('p_idt2', 'p_idt2_example'),
                    ('p_stdt1', 'p_stdt1_example'),
                    ('p_stdt2', 'p_stdt2_example'),
                    ('p_pityp', 'p_pityp_example'),
                    ('p_cifdi', 'p_cifdi_example'),
                    ('p_pfead1', 'p_pfead1_example'),
                    ('p_pfead2', 'p_pfead2_example'),
                    ('p_pfeat', 'p_pfeat_example'),
                    ('p_psncq', 'p_psncq_example'),
                    ('p_pctrack', 'p_pctrack_example'),
                    ('p_swpa', 'p_swpa_example'),
                    ('p_des', 'p_des_example'),
                    ('p_fntype', 'p_fntype_example'),
                    ('p_hpvmth', 'p_hpvmth_example'),
                    ('p_recvio', 'p_recvio_example'),
                    ('p_pollvio', 'p_pollvio_example'),
                    ('p_ar', 'p_ar_example'),
                    ('p_tri_yr', 'p_tri_yr_example'),
                    ('p_pidall', 'p_pidall_example'),
                    ('p_fac_ico', 'p_fac_ico_example'),
                    ('p_icoo', 'p_icoo_example'),
                    ('p_fac_icos', 'p_fac_icos_example'),
                    ('p_ejscreen', 'p_ejscreen_example'),
                    ('p_limit_addr', 'p_limit_addr_example'),
                    ('p_lat', 3.4),
                    ('p_long', 3.4),
                    ('p_radius', 3.4),
                    ('p_decouple', 'p_decouple_example'),
                    ('p_ejscreen_over80cnt', 'p_ejscreen_over80cnt_example'),
                    ('queryset', 3.4),
                    ('responseset', 3.4),
                    ('tablelist', 'tablelist_example'),
                    ('maplist', 'maplist_example'),
                    ('summarylist', 'summarylist_example'),
                    ('callback', 'param_callback_example'),
                    ('qcolumns', 'qcolumns_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/air_rest_services.get_facilities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_air_rest_services_get_facilities_post(client):
    """Test case for air_rest_services_get_facilities_post

    Clean Air Act Facility Search
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_fn': 'p_fn_example',
        'p_sa': 'p_sa_example',
        'p_sa1': 'p_sa1_example',
        'p_ct': 'p_ct_example',
        'p_co': 'p_co_example',
        'p_fips': 'p_fips_example',
        'p_st': 'p_st_example',
        'p_zip': 'p_zip_example',
        'p_lcon': 'p_lcon_example',
        'p_frs': 'p_frs_example',
        'p_reg': 'p_reg_example',
        'p_sic': 'p_sic_example',
        'p_ncs': 'p_ncs_example',
        'p_qnc': 3.4,
        'p_pen': 'p_pen_example',
        'p_opst': 'p_opst_example',
        'p_c1lat': 3.4,
        'p_c1lon': 3.4,
        'p_c2lat': 3.4,
        'p_c2lon': 3.4,
        'p_usmex': 'p_usmex_example',
        'p_sic2': 'p_sic2_example',
        'p_sic4': 'p_sic4_example',
        'p_fa': 'p_fa_example',
        'p_act': 'p_act_example',
        'p_maj': 'p_maj_example',
        'p_mact': 'p_mact_example',
        'p_nsps': 'p_nsps_example',
        'p_nspsm': 'p_nspsm_example',
        'p_prog': 'p_prog_example',
        'p_fea': 'p_fea_example',
        'p_feay': 3.4,
        'p_feaa': 'p_feaa_example',
        'p_iea': 'p_iea_example',
        'p_ieay': 3.4,
        'p_ieaa': 'p_ieaa_example',
        'p_qiv': 'p_qiv_example',
        'p_naa': 'p_naa_example',
        'p_impw': 'p_impw_example',
        'p_trep': 'p_trep_example',
        'p_tri_cat': 'p_tri_cat_example',
        'p_tri_amt': 'p_tri_amt_example',
        'p_tri_any_amt': 3.4,
        'p_tri_pol': 'p_tri_pol_example',
        'p_ghg_cat': 'p_ghg_cat_example',
        'p_ghg_amt': 'p_ghg_amt_example',
        'p_ghg_any_amt': 3.4,
        'p_ghg_yr': 'p_ghg_yr_example',
        'p_nei_pol': 'p_nei_pol_example',
        'p_nei_amt': 'p_nei_amt_example',
        'p_nei_any_amt': 3.4,
        'p_nei_yr': 'p_nei_yr_example',
        'p_nei_cat': 'p_nei_cat_example',
        'p_pm': 'p_pm_example',
        'p_pd': 'p_pd_example',
        'p_ico': 'p_ico_example',
        'p_huc': 'p_huc_example',
        'p_wbd': 'p_wbd_example',
        'p_pid': 'p_pid_example',
        'p_med': 'p_med_example',
        'p_ysl': 'p_ysl_example',
        'p_ysly': 3.4,
        'p_ysla': 'p_ysla_example',
        'p_stsl': 'p_stsl_example',
        'p_stsly': 3.4,
        'p_stsla': 'p_stsla_example',
        'p_stres': 'p_stres_example',
        'p_sttyp': 'p_sttyp_example',
        'p_qs': 'p_qs_example',
        'p_sfs': 'p_sfs_example',
        'p_tribeid': 3.4,
        'p_tribename': 'p_tribename_example',
        'p_tribedist': 3.4,
        'p_owop': 'p_owop_example',
        'p_agoo': 'p_agoo_example',
        'p_idt1': 'p_idt1_example',
        'p_idt2': 'p_idt2_example',
        'p_stdt1': 'p_stdt1_example',
        'p_stdt2': 'p_stdt2_example',
        'p_pityp': 'p_pityp_example',
        'p_cifdi': 'p_cifdi_example',
        'p_pfead1': 'p_pfead1_example',
        'p_pfead2': 'p_pfead2_example',
        'p_pfeat': 'p_pfeat_example',
        'p_psncq': 'p_psncq_example',
        'p_pctrack': 'p_pctrack_example',
        'p_swpa': 'p_swpa_example',
        'p_des': 'p_des_example',
        'p_fntype': 'p_fntype_example',
        'p_hpvmth': 'p_hpvmth_example',
        'p_recvio': 'p_recvio_example',
        'p_pollvio': 'p_pollvio_example',
        'p_ar': 'p_ar_example',
        'p_tri_yr': 'p_tri_yr_example',
        'p_pidall': 'p_pidall_example',
        'p_fac_ico': 'p_fac_ico_example',
        'p_icoo': 'p_icoo_example',
        'p_fac_icos': 'p_fac_icos_example',
        'p_ejscreen': 'p_ejscreen_example',
        'p_limit_addr': 'p_limit_addr_example',
        'p_lat': 3.4,
        'p_long': 3.4,
        'p_radius': 3.4,
        'p_decouple': 'p_decouple_example',
        'p_ejscreen_over80cnt': 'p_ejscreen_over80cnt_example',
        'queryset': 3.4,
        'responseset': 3.4,
        'tablelist': 'tablelist_example',
        'maplist': 'maplist_example',
        'summarylist': 'summarylist_example',
        'param_callback': 'param_callback_example',
        'qcolumns': 'qcolumns_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/air_rest_services.get_facilities',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_air_rest_services_get_facility_info_get(client):
    """Test case for air_rest_services_get_facility_info_get

    Clean Air Act Facility Enhanced Search
    """
    params = [('output', 'output_example'),
                    ('p_fn', 'p_fn_example'),
                    ('p_sa', 'p_sa_example'),
                    ('p_sa1', 'p_sa1_example'),
                    ('p_ct', 'p_ct_example'),
                    ('p_co', 'p_co_example'),
                    ('p_fips', 'p_fips_example'),
                    ('p_st', 'p_st_example'),
                    ('p_zip', 'p_zip_example'),
                    ('p_lcon', 'p_lcon_example'),
                    ('p_frs', 'p_frs_example'),
                    ('p_reg', 'p_reg_example'),
                    ('p_sic', 'p_sic_example'),
                    ('p_ncs', 'p_ncs_example'),
                    ('p_qnc', 3.4),
                    ('p_pen', 'p_pen_example'),
                    ('p_opst', 'p_opst_example'),
                    ('xmin', 3.4),
                    ('ymin', 3.4),
                    ('xmax', 3.4),
                    ('ymax', 3.4),
                    ('p_usmex', 'p_usmex_example'),
                    ('p_sic2', 'p_sic2_example'),
                    ('p_sic4', 'p_sic4_example'),
                    ('p_fa', 'p_fa_example'),
                    ('p_act', 'p_act_example'),
                    ('p_maj', 'p_maj_example'),
                    ('p_mact', 'p_mact_example'),
                    ('p_nsps', 'p_nsps_example'),
                    ('p_nspsm', 'p_nspsm_example'),
                    ('p_prog', 'p_prog_example'),
                    ('p_fea', 'p_fea_example'),
                    ('p_feay', 3.4),
                    ('p_feaa', 'p_feaa_example'),
                    ('p_iea', 'p_iea_example'),
                    ('p_ieay', 3.4),
                    ('p_ieaa', 'p_ieaa_example'),
                    ('p_qiv', 'p_qiv_example'),
                    ('p_naa', 'p_naa_example'),
                    ('p_impw', 'p_impw_example'),
                    ('p_trep', 'p_trep_example'),
                    ('p_tri_cat', 'p_tri_cat_example'),
                    ('p_tri_amt', 'p_tri_amt_example'),
                    ('p_tri_any_amt', 3.4),
                    ('p_tri_pol', 'p_tri_pol_example'),
                    ('p_ghg_cat', 'p_ghg_cat_example'),
                    ('p_ghg_amt', 'p_ghg_amt_example'),
                    ('p_ghg_any_amt', 3.4),
                    ('p_ghg_yr', 'p_ghg_yr_example'),
                    ('p_nei_pol', 'p_nei_pol_example'),
                    ('p_nei_amt', 'p_nei_amt_example'),
                    ('p_nei_any_amt', 3.4),
                    ('p_nei_yr', 'p_nei_yr_example'),
                    ('p_nei_cat', 'p_nei_cat_example'),
                    ('p_pm', 'p_pm_example'),
                    ('p_pd', 'p_pd_example'),
                    ('p_ico', 'p_ico_example'),
                    ('p_huc', 'p_huc_example'),
                    ('p_wbd', 'p_wbd_example'),
                    ('p_pid', 'p_pid_example'),
                    ('p_med', 'p_med_example'),
                    ('p_ysl', 'p_ysl_example'),
                    ('p_ysly', 3.4),
                    ('p_ysla', 'p_ysla_example'),
                    ('p_stsl', 'p_stsl_example'),
                    ('p_stsly', 3.4),
                    ('p_stsla', 'p_stsla_example'),
                    ('p_stres', 'p_stres_example'),
                    ('p_sttyp', 'p_sttyp_example'),
                    ('p_qs', 'p_qs_example'),
                    ('p_sfs', 'p_sfs_example'),
                    ('p_tribeid', 3.4),
                    ('p_tribename', 'p_tribename_example'),
                    ('p_tribedist', 3.4),
                    ('p_owop', 'p_owop_example'),
                    ('p_agoo', 'p_agoo_example'),
                    ('p_idt1', 'p_idt1_example'),
                    ('p_idt2', 'p_idt2_example'),
                    ('p_stdt1', 'p_stdt1_example'),
                    ('p_stdt2', 'p_stdt2_example'),
                    ('p_pityp', 'p_pityp_example'),
                    ('p_cifdi', 'p_cifdi_example'),
                    ('p_pfead1', 'p_pfead1_example'),
                    ('p_pfead2', 'p_pfead2_example'),
                    ('p_pfeat', 'p_pfeat_example'),
                    ('p_psncq', 'p_psncq_example'),
                    ('p_pctrack', 'p_pctrack_example'),
                    ('p_swpa', 'p_swpa_example'),
                    ('p_des', 'p_des_example'),
                    ('p_fntype', 'p_fntype_example'),
                    ('p_hpvmth', 'p_hpvmth_example'),
                    ('p_recvio', 'p_recvio_example'),
                    ('p_pollvio', 'p_pollvio_example'),
                    ('p_ar', 'p_ar_example'),
                    ('p_tri_yr', 'p_tri_yr_example'),
                    ('p_pidall', 'p_pidall_example'),
                    ('p_fac_ico', 'p_fac_ico_example'),
                    ('p_icoo', 'p_icoo_example'),
                    ('p_fac_icos', 'p_fac_icos_example'),
                    ('p_ejscreen', 'p_ejscreen_example'),
                    ('p_limit_addr', 'p_limit_addr_example'),
                    ('p_lat', 3.4),
                    ('p_long', 3.4),
                    ('p_radius', 3.4),
                    ('p_decouple', 'p_decouple_example'),
                    ('p_ejscreen_over80cnt', 'p_ejscreen_over80cnt_example'),
                    ('queryset', 3.4),
                    ('responseset', 3.4),
                    ('summarylist', 'summarylist_example'),
                    ('callback', 'param_callback_example'),
                    ('qcolumns', 'qcolumns_example'),
                    ('p_pretty_print', 3.4)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/air_rest_services.get_facility_info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_air_rest_services_get_facility_info_post(client):
    """Test case for air_rest_services_get_facility_info_post

    Clean Air Act Facility Enhanced Search
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_fn': 'p_fn_example',
        'p_sa': 'p_sa_example',
        'p_sa1': 'p_sa1_example',
        'p_ct': 'p_ct_example',
        'p_co': 'p_co_example',
        'p_fips': 'p_fips_example',
        'p_st': 'p_st_example',
        'p_zip': 'p_zip_example',
        'p_lcon': 'p_lcon_example',
        'p_frs': 'p_frs_example',
        'p_reg': 'p_reg_example',
        'p_sic': 'p_sic_example',
        'p_ncs': 'p_ncs_example',
        'p_qnc': 3.4,
        'p_pen': 'p_pen_example',
        'p_opst': 'p_opst_example',
        'xmin': 3.4,
        'ymin': 3.4,
        'xmax': 3.4,
        'ymax': 3.4,
        'p_usmex': 'p_usmex_example',
        'p_sic2': 'p_sic2_example',
        'p_sic4': 'p_sic4_example',
        'p_fa': 'p_fa_example',
        'p_act': 'p_act_example',
        'p_maj': 'p_maj_example',
        'p_mact': 'p_mact_example',
        'p_nsps': 'p_nsps_example',
        'p_nspsm': 'p_nspsm_example',
        'p_prog': 'p_prog_example',
        'p_fea': 'p_fea_example',
        'p_feay': 3.4,
        'p_feaa': 'p_feaa_example',
        'p_iea': 'p_iea_example',
        'p_ieay': 3.4,
        'p_ieaa': 'p_ieaa_example',
        'p_qiv': 'p_qiv_example',
        'p_naa': 'p_naa_example',
        'p_impw': 'p_impw_example',
        'p_trep': 'p_trep_example',
        'p_tri_cat': 'p_tri_cat_example',
        'p_tri_amt': 'p_tri_amt_example',
        'p_tri_any_amt': 3.4,
        'p_tri_pol': 'p_tri_pol_example',
        'p_ghg_cat': 'p_ghg_cat_example',
        'p_ghg_amt': 'p_ghg_amt_example',
        'p_ghg_any_amt': 3.4,
        'p_ghg_yr': 'p_ghg_yr_example',
        'p_nei_pol': 'p_nei_pol_example',
        'p_nei_amt': 'p_nei_amt_example',
        'p_nei_any_amt': 3.4,
        'p_nei_yr': 'p_nei_yr_example',
        'p_nei_cat': 'p_nei_cat_example',
        'p_pm': 'p_pm_example',
        'p_pd': 'p_pd_example',
        'p_ico': 'p_ico_example',
        'p_huc': 'p_huc_example',
        'p_wbd': 'p_wbd_example',
        'p_pid': 'p_pid_example',
        'p_med': 'p_med_example',
        'p_ysl': 'p_ysl_example',
        'p_ysly': 3.4,
        'p_ysla': 'p_ysla_example',
        'p_stsl': 'p_stsl_example',
        'p_stsly': 3.4,
        'p_stsla': 'p_stsla_example',
        'p_stres': 'p_stres_example',
        'p_sttyp': 'p_sttyp_example',
        'p_qs': 'p_qs_example',
        'p_sfs': 'p_sfs_example',
        'p_tribeid': 3.4,
        'p_tribename': 'p_tribename_example',
        'p_tribedist': 3.4,
        'p_owop': 'p_owop_example',
        'p_agoo': 'p_agoo_example',
        'p_idt1': 'p_idt1_example',
        'p_idt2': 'p_idt2_example',
        'p_stdt1': 'p_stdt1_example',
        'p_stdt2': 'p_stdt2_example',
        'p_pityp': 'p_pityp_example',
        'p_cifdi': 'p_cifdi_example',
        'p_pfead1': 'p_pfead1_example',
        'p_pfead2': 'p_pfead2_example',
        'p_pfeat': 'p_pfeat_example',
        'p_psncq': 'p_psncq_example',
        'p_pctrack': 'p_pctrack_example',
        'p_swpa': 'p_swpa_example',
        'p_des': 'p_des_example',
        'p_fntype': 'p_fntype_example',
        'p_hpvmth': 'p_hpvmth_example',
        'p_recvio': 'p_recvio_example',
        'p_pollvio': 'p_pollvio_example',
        'p_ar': 'p_ar_example',
        'p_tri_yr': 'p_tri_yr_example',
        'p_pidall': 'p_pidall_example',
        'p_fac_ico': 'p_fac_ico_example',
        'p_icoo': 'p_icoo_example',
        'p_fac_icos': 'p_fac_icos_example',
        'p_ejscreen': 'p_ejscreen_example',
        'p_limit_addr': 'p_limit_addr_example',
        'p_lat': 3.4,
        'p_long': 3.4,
        'p_radius': 3.4,
        'p_decouple': 'p_decouple_example',
        'p_ejscreen_over80cnt': 'p_ejscreen_over80cnt_example',
        'queryset': 3.4,
        'responseset': 3.4,
        'summarylist': 'summarylist_example',
        'param_callback': 'param_callback_example',
        'qcolumns': 'qcolumns_example',
        'p_pretty_print': 3.4
        }
    response = await client.request(
        method='POST',
        path='/echo/air_rest_services.get_facility_info',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_air_rest_services_get_geojson_get(client):
    """Test case for air_rest_services_get_geojson_get

    Clean Air Act GeoJSON Service
    """
    params = [('output', 'output_example'),
                    ('qid', 'qid_example'),
                    ('callback', 'param_callback_example'),
                    ('newsort', 3.4),
                    ('descending', 'descending_example'),
                    ('qcolumns', 'qcolumns_example'),
                    ('p_pretty_print', 3.4)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/air_rest_services.get_geojson',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_air_rest_services_get_geojson_post(client):
    """Test case for air_rest_services_get_geojson_post

    Clean Air Act GeoJSON Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'qid': 'qid_example',
        'param_callback': 'param_callback_example',
        'newsort': 3.4,
        'descending': 'descending_example',
        'qcolumns': 'qcolumns_example',
        'p_pretty_print': 3.4
        }
    response = await client.request(
        method='POST',
        path='/echo/air_rest_services.get_geojson',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_air_rest_services_get_info_clusters_get(client):
    """Test case for air_rest_services_get_info_clusters_get

    Clean Air Act Info Clusters Service
    """
    params = [('output', 'output_example'),
                    ('p_qid', 'p_qid_example'),
                    ('p_pretty_print', 3.4)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/air_rest_services.get_info_clusters',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_air_rest_services_get_info_clusters_post(client):
    """Test case for air_rest_services_get_info_clusters_post

    Clean Air Act Info Clusters Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_qid': 'p_qid_example',
        'p_pretty_print': 3.4
        }
    response = await client.request(
        method='POST',
        path='/echo/air_rest_services.get_info_clusters',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_air_rest_services_get_map_get(client):
    """Test case for air_rest_services_get_map_get

    Clean Air Act Map Service
    """
    params = [('output', 'output_example'),
                    ('qid', 'qid_example'),
                    ('callback', 'param_callback_example'),
                    ('tablelist', 'tablelist_example'),
                    ('c1_lat', 3.4),
                    ('c1_long', 3.4),
                    ('c2_lat', 3.4),
                    ('c2_long', 3.4),
                    ('p_id', 'p_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/air_rest_services.get_map',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_air_rest_services_get_map_post(client):
    """Test case for air_rest_services_get_map_post

    Clean Air Act Map Service
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
        'p_id': 'p_id_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/air_rest_services.get_map',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_air_rest_services_get_qid_get(client):
    """Test case for air_rest_services_get_qid_get

    Clean Air Act Search by Query ID
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
        path='/echo/air_rest_services.get_qid',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_air_rest_services_get_qid_post(client):
    """Test case for air_rest_services_get_qid_post

    Clean Air Act Search by Query ID
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
        path='/echo/air_rest_services.get_qid',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

