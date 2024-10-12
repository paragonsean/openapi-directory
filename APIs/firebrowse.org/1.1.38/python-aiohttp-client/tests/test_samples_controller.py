# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_clinical(client):
    """Test case for clinical

    Retrieve TCGA CDEs verbatim, i.e. not normalized by Firehose.
    """
    params = [('format', json),
                    ('cohort', ['cohort_example']),
                    ('tcga_participant_barcode', ['tcga_participant_barcode_example']),
                    ('cde_name', ['cde_name_example']),
                    ('page', [56]),
                    ('page_size', [56]),
                    ('sort_by', cohort)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Samples/Clinical',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clinical_fh(client):
    """Test case for clinical_fh

    Retrieve CDEs normalized by Firehose and selected for analyses.
    """
    params = [('format', json),
                    ('cohort', ['cohort_example']),
                    ('tcga_participant_barcode', ['tcga_participant_barcode_example']),
                    ('fh_cde_name', ['fh_cde_name_example']),
                    ('page', [56]),
                    ('page_size', [56]),
                    ('sort_by', cohort)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Samples/Clinical_FH',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_m_rna_seq(client):
    """Test case for m_rna_seq

    Retrieve mRNASeq data.
    """
    params = [('format', json),
                    ('gene', ['gene_example']),
                    ('cohort', ['cohort_example']),
                    ('tcga_participant_barcode', ['tcga_participant_barcode_example']),
                    ('sample_type', ['sample_type_example']),
                    ('protocol', ['protocol_example']),
                    ('page', [56]),
                    ('page_size', [56]),
                    ('sort_by', cohort)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Samples/mRNASeq',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mi_r_seq(client):
    """Test case for mi_r_seq

    Retrieve miRSeq data.
    """
    params = [('format', json),
                    ('mir', ['mir_example']),
                    ('cohort', ['cohort_example']),
                    ('tcga_participant_barcode', ['tcga_participant_barcode_example']),
                    ('tool', ['tool_example']),
                    ('sample_type', ['sample_type_example']),
                    ('page', [56]),
                    ('page_size', [56]),
                    ('sort_by', cohort)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Samples/miRSeq',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

