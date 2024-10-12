# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.echo_rest_services_get_facilities_get200_response import EchoRestServicesGetFacilitiesGet200Response
from openapi_server.models.echo_rest_services_get_facility_info_get200_response import EchoRestServicesGetFacilityInfoGet200Response
from openapi_server.models.echo_rest_services_get_geojson_get200_response import EchoRestServicesGetGeojsonGet200Response
from openapi_server.models.echo_rest_services_get_map_get200_response import EchoRestServicesGetMapGet200Response
from openapi_server.models.echo_rest_services_get_qid_get200_response import EchoRestServicesGetQidGet200Response


pytestmark = pytest.mark.asyncio

async def test_echo_rest_services_get_download_get(client):
    """Test case for echo_rest_services_get_download_get

    Combined ECHO Download Data Service
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
        path='/echo/echo_rest_services.get_download',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_echo_rest_services_get_download_post(client):
    """Test case for echo_rest_services_get_download_post

    Combined ECHO Download Data Service
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
        path='/echo/echo_rest_services.get_download',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_echo_rest_services_get_facilities_get(client):
    """Test case for echo_rest_services_get_facilities_get

    Combined ECHO Facility Search Service
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
                    ('p_frs', 'p_frs_example'),
                    ('p_reg', 'p_reg_example'),
                    ('p_sic', 'p_sic_example'),
                    ('p_ncs', 'p_ncs_example'),
                    ('p_pen', 'p_pen_example'),
                    ('p_c1lat', 3.4),
                    ('p_c1lon', 3.4),
                    ('p_c2lat', 3.4),
                    ('p_c2lon', 3.4),
                    ('p_usmex', 'p_usmex_example'),
                    ('p_sic2', 'p_sic2_example'),
                    ('p_sic4', 'p_sic4_example'),
                    ('p_fa', 'p_fa_example'),
                    ('p_ff', 'p_ff_example'),
                    ('p_act', 'p_act_example'),
                    ('p_maj', 'p_maj_example'),
                    ('p_mact', 'p_mact_example'),
                    ('p_fea', 'p_fea_example'),
                    ('p_feay', 3.4),
                    ('p_feaa', 'p_feaa_example'),
                    ('p_feac', 'p_feac_example'),
                    ('p_fea_5yr', 'p_fea_5yr_example'),
                    ('p_iea', 'p_iea_example'),
                    ('p_ieay', 3.4),
                    ('p_ieaa', 'p_ieaa_example'),
                    ('p_iea_5yr', 'p_iea_5yr_example'),
                    ('p_cs', 3.4),
                    ('p_qiv', 'p_qiv_example'),
                    ('p_naa', 'p_naa_example'),
                    ('p_impw', 'p_impw_example'),
                    ('p_trep', 'p_trep_example'),
                    ('p_ocr', 'p_ocr_example'),
                    ('p_oct', 'p_oct_example'),
                    ('p_pm', 'p_pm_example'),
                    ('p_pd', 'p_pd_example'),
                    ('p_ico', 'p_ico_example'),
                    ('p_huc', 'p_huc_example'),
                    ('p_pid', 'p_pid_example'),
                    ('p_med', 'p_med_example'),
                    ('p_istatute', 'p_istatute_example'),
                    ('p_ysl', 'p_ysl_example'),
                    ('p_ysly', 3.4),
                    ('p_ysla', 'p_ysla_example'),
                    ('p_qs', 'p_qs_example'),
                    ('p_sfs', 'p_sfs_example'),
                    ('p_tribeid', 3.4),
                    ('p_tribename', 'p_tribename_example'),
                    ('p_tribedist', 3.4),
                    ('p_wbd', 'p_wbd_example'),
                    ('p_fntype', 'p_fntype_example'),
                    ('p_icoo', 'p_icoo_example'),
                    ('p_fac_icos', 'p_fac_icos_example'),
                    ('p_ejscreen', 'p_ejscreen_example'),
                    ('p_limit_addr', 'p_limit_addr_example'),
                    ('p_lat', 3.4),
                    ('p_long', 3.4),
                    ('p_radius', 3.4),
                    ('p_ejscreen_over80cnt', 'p_ejscreen_over80cnt_example'),
                    ('p_agoo', 'p_agoo_example'),
                    ('p_neiu', 'p_neiu_example'),
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
        path='/echo/echo_rest_services.get_facilities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_echo_rest_services_get_facilities_post(client):
    """Test case for echo_rest_services_get_facilities_post

    Combined ECHO Facility Search Service
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
        'p_frs': 'p_frs_example',
        'p_reg': 'p_reg_example',
        'p_sic': 'p_sic_example',
        'p_ncs': 'p_ncs_example',
        'p_pen': 'p_pen_example',
        'p_c1lat': 3.4,
        'p_c1lon': 3.4,
        'p_c2lat': 3.4,
        'p_c2lon': 3.4,
        'p_usmex': 'p_usmex_example',
        'p_sic2': 'p_sic2_example',
        'p_sic4': 'p_sic4_example',
        'p_fa': 'p_fa_example',
        'p_ff': 'p_ff_example',
        'p_act': 'p_act_example',
        'p_maj': 'p_maj_example',
        'p_mact': 'p_mact_example',
        'p_fea': 'p_fea_example',
        'p_feay': 3.4,
        'p_feaa': 'p_feaa_example',
        'p_feac': 'p_feac_example',
        'p_fea_5yr': 'p_fea_5yr_example',
        'p_iea': 'p_iea_example',
        'p_ieay': 3.4,
        'p_ieaa': 'p_ieaa_example',
        'p_iea_5yr': 'p_iea_5yr_example',
        'p_cs': 3.4,
        'p_qiv': 'p_qiv_example',
        'p_naa': 'p_naa_example',
        'p_impw': 'p_impw_example',
        'p_trep': 'p_trep_example',
        'p_ocr': 'p_ocr_example',
        'p_oct': 'p_oct_example',
        'p_pm': 'p_pm_example',
        'p_pd': 'p_pd_example',
        'p_ico': 'p_ico_example',
        'p_huc': 'p_huc_example',
        'p_pid': 'p_pid_example',
        'p_med': 'p_med_example',
        'p_istatute': 'p_istatute_example',
        'p_ysl': 'p_ysl_example',
        'p_ysly': 3.4,
        'p_ysla': 'p_ysla_example',
        'p_qs': 'p_qs_example',
        'p_sfs': 'p_sfs_example',
        'p_tribeid': 3.4,
        'p_tribename': 'p_tribename_example',
        'p_tribedist': 3.4,
        'p_wbd': 'p_wbd_example',
        'p_fntype': 'p_fntype_example',
        'p_icoo': 'p_icoo_example',
        'p_fac_icos': 'p_fac_icos_example',
        'p_ejscreen': 'p_ejscreen_example',
        'p_limit_addr': 'p_limit_addr_example',
        'p_lat': 3.4,
        'p_long': 3.4,
        'p_radius': 3.4,
        'p_ejscreen_over80cnt': 'p_ejscreen_over80cnt_example',
        'p_agoo': 'p_agoo_example',
        'p_neiu': 'p_neiu_example',
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
        path='/echo/echo_rest_services.get_facilities',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_echo_rest_services_get_facility_info_get(client):
    """Test case for echo_rest_services_get_facility_info_get

    Combined ECHO Facility Enhanced Search Service
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
                    ('p_frs', 'p_frs_example'),
                    ('p_reg', 'p_reg_example'),
                    ('p_sic', 'p_sic_example'),
                    ('p_ncs', 'p_ncs_example'),
                    ('p_pen', 'p_pen_example'),
                    ('xmin', 3.4),
                    ('ymin', 3.4),
                    ('xmax', 3.4),
                    ('ymax', 3.4),
                    ('p_usmex', 'p_usmex_example'),
                    ('p_sic2', 'p_sic2_example'),
                    ('p_sic4', 'p_sic4_example'),
                    ('p_fa', 'p_fa_example'),
                    ('p_ff', 'p_ff_example'),
                    ('p_act', 'p_act_example'),
                    ('p_maj', 'p_maj_example'),
                    ('p_mact', 'p_mact_example'),
                    ('p_fea', 'p_fea_example'),
                    ('p_feay', 3.4),
                    ('p_feaa', 'p_feaa_example'),
                    ('p_feac', 'p_feac_example'),
                    ('p_feac_5yr', 'p_feac_5yr_example'),
                    ('p_iea', 'p_iea_example'),
                    ('p_ieay', 3.4),
                    ('p_ieaa', 'p_ieaa_example'),
                    ('p_iea_5yr', 'p_iea_5yr_example'),
                    ('p_cs', 3.4),
                    ('p_qiv', 'p_qiv_example'),
                    ('p_naa', 'p_naa_example'),
                    ('p_impw', 'p_impw_example'),
                    ('p_trep', 'p_trep_example'),
                    ('p_ocr', 'p_ocr_example'),
                    ('p_oct', 'p_oct_example'),
                    ('p_pm', 'p_pm_example'),
                    ('p_pd', 'p_pd_example'),
                    ('p_ico', 'p_ico_example'),
                    ('p_huc', 'p_huc_example'),
                    ('p_pid', 'p_pid_example'),
                    ('p_med', 'p_med_example'),
                    ('p_istatute', 'p_istatute_example'),
                    ('p_ysl', 'p_ysl_example'),
                    ('p_ysly', 3.4),
                    ('p_ysla', 'p_ysla_example'),
                    ('p_qs', 'p_qs_example'),
                    ('p_sfs', 'p_sfs_example'),
                    ('p_tribeid', 3.4),
                    ('p_tribename', 'p_tribename_example'),
                    ('p_tribedist', 3.4),
                    ('p_wbd', 'p_wbd_example'),
                    ('p_fntype', 'p_fntype_example'),
                    ('p_icoo', 'p_icoo_example'),
                    ('p_fac_icos', 'p_fac_icos_example'),
                    ('p_ejscreen', 'p_ejscreen_example'),
                    ('p_limit_addr', 'p_limit_addr_example'),
                    ('p_lat', 3.4),
                    ('p_long', 3.4),
                    ('p_radius', 3.4),
                    ('p_ejscreen_over80cnt', 'p_ejscreen_over80cnt_example'),
                    ('p_agoo', 'p_agoo_example'),
                    ('p_neiu', 'p_neiu_example'),
                    ('responseset', 3.4),
                    ('callback', 'param_callback_example'),
                    ('qcolumns', 'qcolumns_example'),
                    ('p_pretty_print', 3.4)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/echo_rest_services.get_facility_info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_echo_rest_services_get_facility_info_post(client):
    """Test case for echo_rest_services_get_facility_info_post

    Combined ECHO Facility Enhanced Search Service
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
        'p_frs': 'p_frs_example',
        'p_reg': 'p_reg_example',
        'p_sic': 'p_sic_example',
        'p_ncs': 'p_ncs_example',
        'p_pen': 'p_pen_example',
        'xmin': 3.4,
        'ymin': 3.4,
        'xmax': 3.4,
        'ymax': 3.4,
        'p_usmex': 'p_usmex_example',
        'p_sic2': 'p_sic2_example',
        'p_sic4': 'p_sic4_example',
        'p_fa': 'p_fa_example',
        'p_ff': 'p_ff_example',
        'p_act': 'p_act_example',
        'p_maj': 'p_maj_example',
        'p_mact': 'p_mact_example',
        'p_fea': 'p_fea_example',
        'p_feay': 3.4,
        'p_feaa': 'p_feaa_example',
        'p_feac': 'p_feac_example',
        'p_feac_5yr': 'p_feac_5yr_example',
        'p_iea': 'p_iea_example',
        'p_ieay': 3.4,
        'p_ieaa': 'p_ieaa_example',
        'p_iea_5yr': 'p_iea_5yr_example',
        'p_cs': 3.4,
        'p_qiv': 'p_qiv_example',
        'p_naa': 'p_naa_example',
        'p_impw': 'p_impw_example',
        'p_trep': 'p_trep_example',
        'p_ocr': 'p_ocr_example',
        'p_oct': 'p_oct_example',
        'p_pm': 'p_pm_example',
        'p_pd': 'p_pd_example',
        'p_ico': 'p_ico_example',
        'p_huc': 'p_huc_example',
        'p_pid': 'p_pid_example',
        'p_med': 'p_med_example',
        'p_istatute': 'p_istatute_example',
        'p_ysl': 'p_ysl_example',
        'p_ysly': 3.4,
        'p_ysla': 'p_ysla_example',
        'p_qs': 'p_qs_example',
        'p_sfs': 'p_sfs_example',
        'p_tribeid': 3.4,
        'p_tribename': 'p_tribename_example',
        'p_tribedist': 3.4,
        'p_wbd': 'p_wbd_example',
        'p_fntype': 'p_fntype_example',
        'p_icoo': 'p_icoo_example',
        'p_fac_icos': 'p_fac_icos_example',
        'p_ejscreen': 'p_ejscreen_example',
        'p_limit_addr': 'p_limit_addr_example',
        'p_lat': 3.4,
        'p_long': 3.4,
        'p_radius': 3.4,
        'p_ejscreen_over80cnt': 'p_ejscreen_over80cnt_example',
        'p_agoo': 'p_agoo_example',
        'p_neiu': 'p_neiu_example',
        'responseset': 3.4,
        'param_callback': 'param_callback_example',
        'qcolumns': 'qcolumns_example',
        'p_pretty_print': 3.4
        }
    response = await client.request(
        method='POST',
        path='/echo/echo_rest_services.get_facility_info',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_echo_rest_services_get_geojson_get(client):
    """Test case for echo_rest_services_get_geojson_get

    Combined ECHO GeoJSON Service
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
        path='/echo/echo_rest_services.get_geojson',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_echo_rest_services_get_geojson_post(client):
    """Test case for echo_rest_services_get_geojson_post

    Combined ECHO GeoJSON Service
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
        path='/echo/echo_rest_services.get_geojson',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_echo_rest_services_get_info_clusters_get(client):
    """Test case for echo_rest_services_get_info_clusters_get

    Combined ECHO Info Clusters Service
    """
    params = [('output', 'output_example'),
                    ('p_qid', 'p_qid_example'),
                    ('p_pretty_print', 3.4)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/echo_rest_services.get_info_clusters',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_echo_rest_services_get_info_clusters_post(client):
    """Test case for echo_rest_services_get_info_clusters_post

    Combined ECHO Info Clusters Service
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
        path='/echo/echo_rest_services.get_info_clusters',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_echo_rest_services_get_map_get(client):
    """Test case for echo_rest_services_get_map_get

    Combined ECHO Map Service
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
        path='/echo/echo_rest_services.get_map',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_echo_rest_services_get_map_post(client):
    """Test case for echo_rest_services_get_map_post

    Combined ECHO Map Service
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
        path='/echo/echo_rest_services.get_map',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_echo_rest_services_get_qid_get(client):
    """Test case for echo_rest_services_get_qid_get

    Combined ECHO Paginated Results Service
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
        path='/echo/echo_rest_services.get_qid',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_echo_rest_services_get_qid_post(client):
    """Test case for echo_rest_services_get_qid_post

    Combined ECHO Paginated Results Service
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
        path='/echo/echo_rest_services.get_qid',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

