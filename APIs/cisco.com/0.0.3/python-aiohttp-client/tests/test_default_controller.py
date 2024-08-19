# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_security_advisories_cvrf_advisory_advisory_id_get(client):
    """Test case for security_advisories_cvrf_advisory_advisory_id_get

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/security/advisories/cvrf/advisory/{advisory_id}'.format(advisory_id='advisory_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_advisories_cvrf_all_get(client):
    """Test case for security_advisories_cvrf_all_get

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/security/advisories/cvrf/all',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_advisories_cvrf_cve_cve_id_get(client):
    """Test case for security_advisories_cvrf_cve_cve_id_get

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/security/advisories/cvrf/cve/{cve_id}'.format(cve_id='cve_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_advisories_cvrf_latest_number_get(client):
    """Test case for security_advisories_cvrf_latest_number_get

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/security/advisories/cvrf/latest/{number}'.format(number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_advisories_cvrf_product_get(client):
    """Test case for security_advisories_cvrf_product_get

    
    """
    params = [('product', 'product_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/security/advisories/cvrf/product',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_advisories_cvrf_severity_severity_firstpublished_get(client):
    """Test case for security_advisories_cvrf_severity_severity_firstpublished_get

    
    """
    params = [('startDate', '2013-10-20'),
                    ('endDate', '2013-10-20')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/security/advisories/cvrf/severity/{severity}/firstpublished'.format(severity='severity_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_advisories_cvrf_severity_severity_get(client):
    """Test case for security_advisories_cvrf_severity_severity_get

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/security/advisories/cvrf/severity/{severity}'.format(severity='severity_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_advisories_cvrf_severity_severity_lastpublished_get(client):
    """Test case for security_advisories_cvrf_severity_severity_lastpublished_get

    
    """
    params = [('startDate', '2013-10-20'),
                    ('endDate', '2013-10-20')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/security/advisories/cvrf/severity/{severity}/lastpublished'.format(severity='severity_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_advisories_cvrf_year_year_get(client):
    """Test case for security_advisories_cvrf_year_year_get

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/security/advisories/cvrf/year/{year}'.format(year='year_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_advisories_ios_get(client):
    """Test case for security_advisories_ios_get

    
    """
    params = [('version', 'version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/security/advisories/ios',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_advisories_iosxe_get(client):
    """Test case for security_advisories_iosxe_get

    
    """
    params = [('version', 'version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/security/advisories/iosxe',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_advisories_oval_advisory_advisory_id_get(client):
    """Test case for security_advisories_oval_advisory_advisory_id_get

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/security/advisories/oval/advisory/{advisory_id}'.format(advisory_id='advisory_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_advisories_oval_all_get(client):
    """Test case for security_advisories_oval_all_get

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/security/advisories/oval/all',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_advisories_oval_cve_cve_id_get(client):
    """Test case for security_advisories_oval_cve_cve_id_get

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/security/advisories/oval/cve/{cve_id}'.format(cve_id='cve_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_advisories_oval_latest_number_get(client):
    """Test case for security_advisories_oval_latest_number_get

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/security/advisories/oval/latest/{number}'.format(number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_advisories_oval_product_get(client):
    """Test case for security_advisories_oval_product_get

    
    """
    params = [('product', 'product_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/security/advisories/oval/product',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_advisories_oval_severity_severity_firstpublished_get(client):
    """Test case for security_advisories_oval_severity_severity_firstpublished_get

    
    """
    params = [('startDate', '2013-10-20'),
                    ('endDate', '2013-10-20')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/security/advisories/oval/severity/{severity}/firstpublished'.format(severity='severity_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_advisories_oval_severity_severity_get(client):
    """Test case for security_advisories_oval_severity_severity_get

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/security/advisories/oval/severity/{severity}'.format(severity='severity_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_advisories_oval_severity_severity_lastpublished_get(client):
    """Test case for security_advisories_oval_severity_severity_lastpublished_get

    
    """
    params = [('startDate', '2013-10-20'),
                    ('endDate', '2013-10-20')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/security/advisories/oval/severity/{severity}/lastpublished'.format(severity='severity_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

