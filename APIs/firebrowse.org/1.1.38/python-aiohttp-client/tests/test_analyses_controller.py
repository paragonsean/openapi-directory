# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_all(client):
    """Test case for all

    Retrieve all data by genes Gistic2 results.
    """
    params = [('format', json),
                    ('cohort', ['cohort_example']),
                    ('gene', ['gene_example']),
                    ('tcga_participant_barcode', ['tcga_participant_barcode_example']),
                    ('page', [56]),
                    ('page_size', [56]),
                    ('sort_by', cohort)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Analyses/CopyNumber/Genes/All',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_amplified(client):
    """Test case for amplified

    Retrieve Gistic2 significantly amplified genes results.
    """
    params = [('format', json),
                    ('cohort', ['cohort_example']),
                    ('gene', ['gene_example']),
                    ('q', 3.4),
                    ('page', [56]),
                    ('page_size', [56]),
                    ('sort_by', cohort)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Analyses/CopyNumber/Genes/Amplified',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deleted(client):
    """Test case for deleted

    Retrieve Gistic2 significantly deleted genes results.
    """
    params = [('format', json),
                    ('cohort', ['cohort_example']),
                    ('gene', ['gene_example']),
                    ('q', 3.4),
                    ('page', [56]),
                    ('page_size', [56]),
                    ('sort_by', cohort)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Analyses/CopyNumber/Genes/Deleted',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_feature_table(client):
    """Test case for feature_table

    Retrieve aggregated analysis features table.
    """
    params = [('format', tsv),
                    ('cohort', ['cohort_example']),
                    ('date', ['2013-10-20']),
                    ('column', ['column_example']),
                    ('page', [56]),
                    ('page_size', [56])]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Analyses/FeatureTable',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_focal(client):
    """Test case for focal

    Retrieve focal data by genes Gistic2 results.
    """
    params = [('format', json),
                    ('cohort', ['cohort_example']),
                    ('gene', ['gene_example']),
                    ('tcga_participant_barcode', ['tcga_participant_barcode_example']),
                    ('page', [56]),
                    ('page_size', [56]),
                    ('sort_by', cohort)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Analyses/CopyNumber/Genes/Focal',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_m_af(client):
    """Test case for m_af

    Retrieve MutSig final analysis MAF.
    """
    params = [('format', json),
                    ('cohort', ['cohort_example']),
                    ('tool', ['tool_example']),
                    ('gene', ['gene_example']),
                    ('tcga_participant_barcode', ['tcga_participant_barcode_example']),
                    ('column', ['column_example']),
                    ('page', [56]),
                    ('page_size', [56]),
                    ('sort_by', cohort)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Analyses/Mutation/MAF',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_m_rna_seq_quartiles(client):
    """Test case for m_rna_seq_quartiles

    Returns RNASeq expression quartiles, e.g. suitable for drawing a boxplot.
    """
    params = [('format', json),
                    ('gene', 'gene_example'),
                    ('cohort', ['cohort_example']),
                    ('protocol', ['protocol_example']),
                    ('sample_type', ['sample_type_example']),
                    ('Exclude', ['exclude_example'])]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Analyses/mRNASeq/Quartiles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reports(client):
    """Test case for reports

    Retrieve links to summary reports from Firehose analysis runs.
    """
    params = [('format', json),
                    ('date', ['2013-10-20']),
                    ('cohort', ['cohort_example']),
                    ('name', ['name_example']),
                    ('type', ['type_example']),
                    ('page', [56]),
                    ('page_size', [56]),
                    ('sort_by', date)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Analyses/Reports',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_s_mg(client):
    """Test case for s_mg

    Retrieve Significantly Mutated Genes (SMG).
    """
    params = [('format', json),
                    ('cohort', ['cohort_example']),
                    ('tool', ['tool_example']),
                    ('rank', 56),
                    ('gene', ['gene_example']),
                    ('q', 3.4),
                    ('page', [56]),
                    ('page_size', [56]),
                    ('sort_by', rank)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Analyses/Mutation/SMG',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_thresholded(client):
    """Test case for thresholded

    Retrieve all thresholded by genes Gistic2 results.
    """
    params = [('format', json),
                    ('cohort', ['cohort_example']),
                    ('gene', ['gene_example']),
                    ('tcga_participant_barcode', ['tcga_participant_barcode_example']),
                    ('page', [56]),
                    ('page_size', [56]),
                    ('sort_by', cohort)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Analyses/CopyNumber/Genes/Thresholded',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

