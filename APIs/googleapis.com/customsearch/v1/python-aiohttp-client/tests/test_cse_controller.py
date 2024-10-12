# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.search import Search


pytestmark = pytest.mark.asyncio

async def test_search_cse_list(client):
    """Test case for search_cse_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('c2coff', 'c2coff_example'),
                    ('cr', 'cr_example'),
                    ('cx', 'cx_example'),
                    ('dateRestrict', 'date_restrict_example'),
                    ('exactTerms', 'exact_terms_example'),
                    ('excludeTerms', 'exclude_terms_example'),
                    ('fileType', 'file_type_example'),
                    ('filter', 'filter_example'),
                    ('gl', 'gl_example'),
                    ('googlehost', 'googlehost_example'),
                    ('highRange', 'high_range_example'),
                    ('hl', 'hl_example'),
                    ('hq', 'hq_example'),
                    ('imgColorType', 'img_color_type_example'),
                    ('imgDominantColor', 'img_dominant_color_example'),
                    ('imgSize', 'img_size_example'),
                    ('imgType', 'img_type_example'),
                    ('linkSite', 'link_site_example'),
                    ('lowRange', 'low_range_example'),
                    ('lr', 'lr_example'),
                    ('num', 56),
                    ('orTerms', 'or_terms_example'),
                    ('q', 'q_example'),
                    ('relatedSite', 'related_site_example'),
                    ('rights', 'rights_example'),
                    ('safe', 'safe_example'),
                    ('searchType', 'search_type_example'),
                    ('siteSearch', 'site_search_example'),
                    ('siteSearchFilter', 'site_search_filter_example'),
                    ('sort', 'sort_example'),
                    ('start', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/customsearch/v1',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_cse_siterestrict_list(client):
    """Test case for search_cse_siterestrict_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('c2coff', 'c2coff_example'),
                    ('cr', 'cr_example'),
                    ('cx', 'cx_example'),
                    ('dateRestrict', 'date_restrict_example'),
                    ('exactTerms', 'exact_terms_example'),
                    ('excludeTerms', 'exclude_terms_example'),
                    ('fileType', 'file_type_example'),
                    ('filter', 'filter_example'),
                    ('gl', 'gl_example'),
                    ('googlehost', 'googlehost_example'),
                    ('highRange', 'high_range_example'),
                    ('hl', 'hl_example'),
                    ('hq', 'hq_example'),
                    ('imgColorType', 'img_color_type_example'),
                    ('imgDominantColor', 'img_dominant_color_example'),
                    ('imgSize', 'img_size_example'),
                    ('imgType', 'img_type_example'),
                    ('linkSite', 'link_site_example'),
                    ('lowRange', 'low_range_example'),
                    ('lr', 'lr_example'),
                    ('num', 56),
                    ('orTerms', 'or_terms_example'),
                    ('q', 'q_example'),
                    ('relatedSite', 'related_site_example'),
                    ('rights', 'rights_example'),
                    ('safe', 'safe_example'),
                    ('searchType', 'search_type_example'),
                    ('siteSearch', 'site_search_example'),
                    ('siteSearchFilter', 'site_search_filter_example'),
                    ('sort', 'sort_example'),
                    ('start', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/customsearch/v1/siterestrict',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

