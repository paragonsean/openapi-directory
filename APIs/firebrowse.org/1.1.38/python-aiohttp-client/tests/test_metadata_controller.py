# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_barcode(client):
    """Test case for barcode

    Given a TCGA barcode, return its short letter sample type code.
    """
    params = [('format', json)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Metadata/SampleType/Barcode/{tcga_barcode}'.format(tcga_barcode='tcga_barcode_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_centers(client):
    """Test case for centers

    Obtain identities of TCGA consortium member centers.
    """
    params = [('format', json),
                    ('center', ['center_example'])]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Metadata/Centers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clinical_names(client):
    """Test case for clinical_names

    Retrieve names of all TCGA clinical data elements (CDEs).
    """
    params = [('format', json)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Metadata/ClinicalNames',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clinical_names_fh(client):
    """Test case for clinical_names_fh

    Retrieve names of CDEs normalized by Firehose and selected for analyses.
    """
    params = [('format', json)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Metadata/ClinicalNames_FH',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_code(client):
    """Test case for code

    Translate from numeric to symbolic TCGA sample codes.
    """
    params = [('format', json)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Metadata/SampleType/Code/{code}'.format(code=['code_example']),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cohorts(client):
    """Test case for cohorts

    Translate TCGA cohort abbreviations to full disease names.
    """
    params = [('format', json),
                    ('cohort', ['cohort_example'])]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Metadata/Cohorts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_counts(client):
    """Test case for counts

    Retrieve sample counts.
    """
    params = [('format', json),
                    ('date', ['2013-10-20']),
                    ('cohort', ['cohort_example']),
                    ('sample_type', ['sample_type_example']),
                    ('data_type', ['data_type_example']),
                    ('totals', True),
                    ('sort_by', cohort)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Metadata/Counts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dates(client):
    """Test case for dates

    Retrieve dates of all GDAC Firehose stddata & analyses runs that have been ingested into FireBrowse.
    """
    params = [('format', json)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Metadata/Dates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_heart_beat(client):
    """Test case for heart_beat

    Simple way to discern whether API server is up and running
    """
    params = [('format', json)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Metadata/HeartBeat',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_m_af_col_names(client):
    """Test case for m_af_col_names

    Retrieve names of all columns in the mutation annotation files (MAFs) served by FireBrowse.
    """
    params = [('format', json)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Metadata/MAFColNames',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patients(client):
    """Test case for patients

    Retrieve list of all TCGA patients.
    """
    params = [('format', json),
                    ('cohort', ['cohort_example']),
                    ('page', [56]),
                    ('page_size', [56]),
                    ('sort_by', cohort)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Metadata/Patients',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_platforms(client):
    """Test case for platforms

    Translate TCGA platform codes to full platform names.
    """
    params = [('format', json),
                    ('platform', ['platform_example'])]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Metadata/Platforms',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sample_types(client):
    """Test case for sample_types

    Return all TCGA sample type codes, both numeric and symbolic.
    """
    params = [('format', json)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Metadata/SampleTypes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_short_letter_code(client):
    """Test case for short_letter_code

    Translate from symbolic to numeric TCGA sample codes.
    """
    params = [('format', json)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Metadata/SampleType/ShortLetterCode/{short_letter_code}'.format(short_letter_code=['short_letter_code_example']),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_t_s_sites(client):
    """Test case for t_s_sites

    Obtain identities of tissue source sites in TCGA.
    """
    params = [('format', json),
                    ('tss_code', ['tss_code_example'])]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Metadata/TSSites',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

