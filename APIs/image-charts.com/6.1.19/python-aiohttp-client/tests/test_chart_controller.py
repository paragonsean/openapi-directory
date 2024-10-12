# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_chart(client):
    """Test case for get_chart

    Image-Charts API
    """
    params = [('cht', 'cht_example'),
                    ('chd', 'chd_example'),
                    ('chds', 'chds_example'),
                    ('choe', 'choe_example'),
                    ('chld', 'L|4'),
                    ('chxr', 'chxr_example'),
                    ('chxp', 'chxp_example'),
                    ('chof', '.png'),
                    ('chs', 'chs_example'),
                    ('chdl', 'chdl_example'),
                    ('chdls', '000000'),
                    ('chg', 'chg_example'),
                    ('chco', 'F56991,FF9F80,FFC48C,D1F2A5,EFFAB4'),
                    ('chtt', 'chtt_example'),
                    ('chts', 'chts_example'),
                    ('chxt', 'chxt_example'),
                    ('chxl', 'chxl_example'),
                    ('chxs', 'chxs_example'),
                    ('chm', 'chm_example'),
                    ('chls', 'chls_example'),
                    ('chl', 'chl_example'),
                    ('chlps', 'chlps_example'),
                    ('chma', 'chma_example'),
                    ('chdlp', 'r'),
                    ('chf', 'bg,s,FFFFFF'),
                    ('chbh', '10'),
                    ('chbr', '0'),
                    ('chan', 'chan_example'),
                    ('chli', 'chli_example'),
                    ('icac', 'icac_example'),
                    ('ichm', 'ichm_example'),
                    ('icff', 'icff_example'),
                    ('icfs', 'icfs_example'),
                    ('iclocale', 'iclocale_example'),
                    ('icwt', False),
                    ('icretina', 'icretina_example'),
                    ('icqrb', 'FFFFFF'),
                    ('icqrf', '000000')]
    headers = { 
        'Accept': 'image/svg+xml',
    }
    response = await client.request(
        method='GET',
        path='/chart',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

