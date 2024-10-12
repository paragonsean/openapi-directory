# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_export_csv_registrierkassen_registrierkasse_uuid_belege_get(client):
    """Test case for export_csv_registrierkassen_registrierkasse_uuid_belege_get

    
    """
    params = [('before', 'before_example'),
                    ('after', 'after_example'),
                    ('posten', True)]
    headers = { 
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/export/csv/registrierkassen/{registrierkasse_uuid}/belege'.format(registrierkasse_uuid='registrierkasse_uuid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_dep131_registrierkassen_registrierkasse_uuid_belege_get(client):
    """Test case for export_dep131_registrierkassen_registrierkasse_uuid_belege_get

    
    """
    params = [('before', 'before_example'),
                    ('after', 'after_example')]
    headers = { 
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/export/dep131/registrierkassen/{registrierkasse_uuid}/belege'.format(registrierkasse_uuid='registrierkasse_uuid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_dep7_registrierkassen_registrierkasse_uuid_belege_get(client):
    """Test case for export_dep7_registrierkassen_registrierkasse_uuid_belege_get

    
    """
    params = [('before', 'before_example'),
                    ('after', 'after_example')]
    headers = { 
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/export/dep7/registrierkassen/{registrierkasse_uuid}/belege'.format(registrierkasse_uuid='registrierkasse_uuid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_gobd_registrierkassen_registrierkasse_uuid_get(client):
    """Test case for export_gobd_registrierkassen_registrierkasse_uuid_get

    
    """
    params = [('before', 'before_example'),
                    ('after', 'after_example')]
    headers = { 
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/export/gobd/registrierkassen/{registrierkasse_uuid}'.format(registrierkasse_uuid='registrierkasse_uuid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_html_belege_beleg_uuid_get(client):
    """Test case for export_html_belege_beleg_uuid_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/export/html/belege/{beleg_uuid}'.format(beleg_uuid='beleg_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_pdf_belege_beleg_uuid_get(client):
    """Test case for export_pdf_belege_beleg_uuid_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/export/pdf/belege/{beleg_uuid}'.format(beleg_uuid='beleg_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_qr_belege_beleg_uuid_get(client):
    """Test case for export_qr_belege_beleg_uuid_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/export/qr/belege/{beleg_uuid}'.format(beleg_uuid='beleg_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_thermal_print_belege_beleg_uuid_get(client):
    """Test case for export_thermal_print_belege_beleg_uuid_get

    
    """
    params = [('qr', True),
                    ('width', 42),
                    ('dialect', escpos),
                    ('encoding', raw)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/export/thermal-print/belege/{beleg_uuid}'.format(beleg_uuid='beleg_uuid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_xls_registrierkassen_registrierkasse_uuid_belege_get(client):
    """Test case for export_xls_registrierkassen_registrierkasse_uuid_belege_get

    
    """
    params = [('before', 'before_example'),
                    ('after', 'after_example')]
    headers = { 
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/export/xls/registrierkassen/{registrierkasse_uuid}/belege'.format(registrierkasse_uuid='registrierkasse_uuid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

