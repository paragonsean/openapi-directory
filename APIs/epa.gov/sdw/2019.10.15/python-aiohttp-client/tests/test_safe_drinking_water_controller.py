# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.sdw_rest_services_get_qid_get200_response import SdwRestServicesGetQidGet200Response
from openapi_server.models.sdw_rest_services_get_systems_get200_response import SdwRestServicesGetSystemsGet200Response


pytestmark = pytest.mark.asyncio

async def test_sdw_rest_services_get_download_get(client):
    """Test case for sdw_rest_services_get_download_get

    Safe Drinking Water Act (SDWA) Download Data Service
    """
    params = [('output', 'output_example'),
                    ('qid', 'qid_example'),
                    ('qcolumns', 'qcolumns_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/sdw_rest_services.get_download',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_sdw_rest_services_get_download_post(client):
    """Test case for sdw_rest_services_get_download_post

    Safe Drinking Water Act (SDWA) Download Data Service
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
        path='/echo/sdw_rest_services.get_download',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sdw_rest_services_get_qid_get(client):
    """Test case for sdw_rest_services_get_qid_get

    Safe Drinking Water Act (SDWA) Paginated Results Service
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
        path='/echo/sdw_rest_services.get_qid',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_sdw_rest_services_get_qid_post(client):
    """Test case for sdw_rest_services_get_qid_post

    Safe Drinking Water Act (SDWA) Paginated Results Service
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
        path='/echo/sdw_rest_services.get_qid',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sdw_rest_services_get_systems_get(client):
    """Test case for sdw_rest_services_get_systems_get

    Safe Drinking Water Act (SDWA) Systems Search Service
    """
    params = [('output', 'output_example'),
                    ('p_fn', 'p_fn_example'),
                    ('p_ct', 'p_ct_example'),
                    ('p_co', 'p_co_example'),
                    ('p_fips', 'p_fips_example'),
                    ('p_st', 'p_st_example'),
                    ('p_zip', 'p_zip_example'),
                    ('p_reg', 'p_reg_example'),
                    ('p_trb', 'p_trb_example'),
                    ('p_act', 'p_act_example'),
                    ('p_qiv', 'p_qiv_example'),
                    ('p_ico', 'p_ico_example'),
                    ('p_pid', 'p_pid_example'),
                    ('p_owop', 'p_owop_example'),
                    ('p_systyp', 'p_systyp_example'),
                    ('p_swtyp', 'p_swtyp_example'),
                    ('p_popsv', 'p_popsv_example'),
                    ('p_cntysv', 'p_cntysv_example'),
                    ('p_cs', 'p_cs_example'),
                    ('p_mr', 'p_mr_example'),
                    ('p_health', 'p_health_example'),
                    ('p_other', 'p_other_example'),
                    ('p_pn', 'p_pn_example'),
                    ('p_sv', 'p_sv_example'),
                    ('p_qs', 'p_qs_example'),
                    ('p_sfs', 'p_sfs_example'),
                    ('p_pswpol', 'p_pswpol_example'),
                    ('p_pswvio', 'p_pswvio_example'),
                    ('p_pbale', 'p_pbale_example'),
                    ('p_cuale', 'p_cuale_example'),
                    ('p_rc350v', 'p_rc350v_example'),
                    ('p_pbv', 'p_pbv_example'),
                    ('p_cuv', 'p_cuv_example'),
                    ('p_lcrv', 'p_lcrv_example'),
                    ('p_fea', 'p_fea_example'),
                    ('p_feay', 3.4),
                    ('p_feaa', 'p_feaa_example'),
                    ('p_iea', 'p_iea_example'),
                    ('p_ieay', 3.4),
                    ('p_ieaa', 'p_ieaa_example'),
                    ('p_qis', 'p_qis_example'),
                    ('p_pfead1', 'p_pfead1_example'),
                    ('p_pfead2', 'p_pfead2_example'),
                    ('p_pfeat', 'p_pfeat_example'),
                    ('p_ss5yr', 'p_ss5yr_example'),
                    ('p_sdc', 'p_sdc_example'),
                    ('p_sdc_ils', 'p_sdc_ils_example'),
                    ('p_ysl', 'p_ysl_example'),
                    ('p_ysly', 'p_ysly_example'),
                    ('p_ysla', 'p_ysla_example'),
                    ('p_idt1', 'p_idt1_example'),
                    ('p_idt2', 'p_idt2_example'),
                    ('p_cms_flag', 'p_cms_flag_example'),
                    ('queryset', 3.4),
                    ('responseset', 3.4),
                    ('callback', 'param_callback_example'),
                    ('qcolumns', 'qcolumns_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/sdw_rest_services.get_systems',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_sdw_rest_services_get_systems_post(client):
    """Test case for sdw_rest_services_get_systems_post

    Safe Drinking Water Act (SDWA) Systems Search Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'p_fn': 'p_fn_example',
        'p_ct': 'p_ct_example',
        'p_co': 'p_co_example',
        'p_fips': 'p_fips_example',
        'p_st': 'p_st_example',
        'p_zip': 'p_zip_example',
        'p_reg': 'p_reg_example',
        'p_trb': 'p_trb_example',
        'p_act': 'p_act_example',
        'p_qiv': 'p_qiv_example',
        'p_ico': 'p_ico_example',
        'p_pid': 'p_pid_example',
        'p_owop': 'p_owop_example',
        'p_systyp': 'p_systyp_example',
        'p_swtyp': 'p_swtyp_example',
        'p_popsv': 'p_popsv_example',
        'p_cntysv': 'p_cntysv_example',
        'p_cs': 'p_cs_example',
        'p_mr': 'p_mr_example',
        'p_health': 'p_health_example',
        'p_other': 'p_other_example',
        'p_pn': 'p_pn_example',
        'p_sv': 'p_sv_example',
        'p_qs': 'p_qs_example',
        'p_sfs': 'p_sfs_example',
        'p_pswpol': 'p_pswpol_example',
        'p_pswvio': 'p_pswvio_example',
        'p_pbale': 'p_pbale_example',
        'p_cuale': 'p_cuale_example',
        'p_rc350v': 'p_rc350v_example',
        'p_pbv': 'p_pbv_example',
        'p_cuv': 'p_cuv_example',
        'p_lcrv': 'p_lcrv_example',
        'p_fea': 'p_fea_example',
        'p_feay': 3.4,
        'p_feaa': 'p_feaa_example',
        'p_iea': 'p_iea_example',
        'p_ieay': 3.4,
        'p_ieaa': 'p_ieaa_example',
        'p_qis': 'p_qis_example',
        'p_pfead1': 'p_pfead1_example',
        'p_pfead2': 'p_pfead2_example',
        'p_pfeat': 'p_pfeat_example',
        'p_ss5yr': 'p_ss5yr_example',
        'p_sdc': 'p_sdc_example',
        'p_sdc_ils': 'p_sdc_ils_example',
        'p_ysl': 'p_ysl_example',
        'p_ysly': 'p_ysly_example',
        'p_ysla': 'p_ysla_example',
        'p_idt1': 'p_idt1_example',
        'p_idt2': 'p_idt2_example',
        'p_cms_flag': 'p_cms_flag_example',
        'queryset': 3.4,
        'responseset': 3.4,
        'param_callback': 'param_callback_example',
        'qcolumns': 'qcolumns_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/sdw_rest_services.get_systems',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

