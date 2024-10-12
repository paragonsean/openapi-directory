# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_active_object_count_using_get(client):
    """Test case for get_active_object_count_using_get

    Count of active objects by type, for specified species and date
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/stats/count/activeObject/{species_type_key}/{date_yyyymmdd}'.format(species_type_key=56, date_yyyymmdd='date_yyyymmdd_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_active_object_diff_using_get(client):
    """Test case for get_active_object_diff_using_get

    Count difference of active objects, by type, for specified species and date range
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/stats/diff/activeObject/{species_type_key}/{date_from_yyyymmdd}/{date_to_yyyymmdd}'.format(species_type_key=56, date_from_yyyymmdd='date_from_yyyymmdd_example', date_to_yyyymmdd='date_to_yyyymmdd_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gene_type_count_using_get(client):
    """Test case for get_gene_type_count_using_get

    Count of gene types, for specified species and date
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/stats/count/geneType/{species_type_key}/{date_yyyymmdd}'.format(species_type_key=56, date_yyyymmdd='date_yyyymmdd_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gene_type_diff_using_get(client):
    """Test case for get_gene_type_diff_using_get

    Count difference of gene types, for specified species and date range
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/stats/diff/geneType/{species_type_key}/{date_from_yyyymmdd}/{date_to_yyyymmdd}'.format(species_type_key=56, date_from_yyyymmdd='date_from_yyyymmdd_example', date_to_yyyymmdd='date_to_yyyymmdd_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_object_status_count_using_get(client):
    """Test case for get_object_status_count_using_get

    Count of objects with given status, for specified species and date
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/stats/count/objectStatus/{species_type_key}/{date_yyyymmdd}'.format(species_type_key=56, date_yyyymmdd='date_yyyymmdd_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_object_status_diff_using_get(client):
    """Test case for get_object_status_diff_using_get

    Count difference of objects with given status, for specified species and date range
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/stats/diff/objectStatus/{species_type_key}/{date_from_yyyymmdd}/{date_to_yyyymmdd}'.format(species_type_key=56, date_from_yyyymmdd='date_from_yyyymmdd_example', date_to_yyyymmdd='date_to_yyyymmdd_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_objects_with_ref_seq_count_using_get(client):
    """Test case for get_objects_with_ref_seq_count_using_get

    Count of objects with reference sequence(s), by object type, for specified species and date
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/stats/count/objectWithRefSeq/{species_type_key}/{date_yyyymmdd}'.format(species_type_key=56, date_yyyymmdd='date_yyyymmdd_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_objects_with_ref_seq_diff_using_get(client):
    """Test case for get_objects_with_ref_seq_diff_using_get

    Count difference of objects with reference sequence(s), by object type, for specified species and date range
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/stats/diff/objectWithRefSeq/{species_type_key}/{date_from_yyyymmdd}/{date_to_yyyymmdd}'.format(species_type_key=56, date_from_yyyymmdd='date_from_yyyymmdd_example', date_to_yyyymmdd='date_to_yyyymmdd_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_objects_with_reference_count_using_get(client):
    """Test case for get_objects_with_reference_count_using_get

    Count of objects with reference, by object type, for specified species and date
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/stats/count/objectWithReference/{species_type_key}/{date_yyyymmdd}'.format(species_type_key=56, date_yyyymmdd='date_yyyymmdd_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_objects_with_reference_diff_using_get(client):
    """Test case for get_objects_with_reference_diff_using_get

    Count difference of objects with reference, by object type, for specified species and date range
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/stats/diff/objectWithReference/{species_type_key}/{date_from_yyyymmdd}/{date_to_yyyymmdd}'.format(species_type_key=56, date_from_yyyymmdd='date_from_yyyymmdd_example', date_to_yyyymmdd='date_to_yyyymmdd_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_objects_with_xdbs_count_using_get(client):
    """Test case for get_objects_with_xdbs_count_using_get

    Count of objects with external database ids, by database id, for specified species, object type and date
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/stats/count/objectWithXdb/{species_type_key}/{object_key}/{date_yyyymmdd}'.format(species_type_key=56, object_key=56, date_yyyymmdd='date_yyyymmdd_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_objects_with_xdbs_diff_using_get(client):
    """Test case for get_objects_with_xdbs_diff_using_get

    Count difference of objects with external database ids, by database id, for specified species, object type and date range
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/stats/diff/objectWithXdb/{species_type_key}/{object_key}/{date_from_yyyymmdd}/{date_to_yyyymmdd}'.format(species_type_key=56, object_key=56, date_from_yyyymmdd='date_from_yyyymmdd_example', date_to_yyyymmdd='date_to_yyyymmdd_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_protein_interaction_count_using_get(client):
    """Test case for get_protein_interaction_count_using_get

    Count of protein interactions, for specified species and date
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/stats/count/proteinInteraction/{species_type_key}/{date_yyyymmdd}'.format(species_type_key=56, date_yyyymmdd='date_yyyymmdd_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_protein_interaction_diff_using_get(client):
    """Test case for get_protein_interaction_diff_using_get

    Count difference of protein interactions, for specified species and date range
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/stats/diff/proteinInteraction/{species_type_key}/{date_from_yyyymmdd}/{date_to_yyyymmdd}'.format(species_type_key=56, date_from_yyyymmdd='date_from_yyyymmdd_example', date_to_yyyymmdd='date_to_yyyymmdd_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_qtl_inheritance_type_count_using_get(client):
    """Test case for get_qtl_inheritance_type_count_using_get

    Count of strains, by qtl inheritance type, for specified species and date
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/stats/count/qtlInheritanceType/{species_type_key}/{date_yyyymmdd}'.format(species_type_key=56, date_yyyymmdd='date_yyyymmdd_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_qtl_inheritance_type_diff_using_get(client):
    """Test case for get_qtl_inheritance_type_diff_using_get

    Count difference of strains, by qtl inheritance type, for specified species and date range
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/stats/diff/qtlInheritanceType/{species_type_key}/{date_from_yyyymmdd}/{date_to_yyyymmdd}'.format(species_type_key=56, date_from_yyyymmdd='date_from_yyyymmdd_example', date_to_yyyymmdd='date_to_yyyymmdd_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_retired_object_count_using_get(client):
    """Test case for get_retired_object_count_using_get

    Count of retired objects by type, for specified species and date
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/stats/count/retiredObject/{species_type_key}/{date_yyyymmdd}'.format(species_type_key=56, date_yyyymmdd='date_yyyymmdd_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_retired_object_diff_using_get(client):
    """Test case for get_retired_object_diff_using_get

    Count difference of retired objects, by type, for specified species and date range
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/stats/diff/retiredObject/{species_type_key}/{date_from_yyyymmdd}/{date_to_yyyymmdd}'.format(species_type_key=56, date_from_yyyymmdd='date_from_yyyymmdd_example', date_to_yyyymmdd='date_to_yyyymmdd_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_strain_type_count_using_get(client):
    """Test case for get_strain_type_count_using_get

    Count of strain types, for specified species and date
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/stats/count/strainType/{species_type_key}/{date_yyyymmdd}'.format(species_type_key=56, date_yyyymmdd='date_yyyymmdd_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_strain_type_diff_using_get(client):
    """Test case for get_strain_type_diff_using_get

    Count difference of strain types, for specified species and date range
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/stats/diff/strainType/{species_type_key}/{date_from_yyyymmdd}/{date_to_yyyymmdd}'.format(species_type_key=56, date_from_yyyymmdd='date_from_yyyymmdd_example', date_to_yyyymmdd='date_to_yyyymmdd_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_term_stats_using_get(client):
    """Test case for get_term_stats_using_get

    getTermStats
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/stats/term/{acc_id}/{filter_acc_id}'.format(acc_id='acc_id_example', filter_acc_id='filter_acc_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_withdrawn_object_count_using_get(client):
    """Test case for get_withdrawn_object_count_using_get

    Count of withdrawn objects by type, for specified species and date
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/stats/count/withdrawnObject/{species_type_key}/{date_yyyymmdd}'.format(species_type_key=56, date_yyyymmdd='date_yyyymmdd_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_withdrawn_object_diff_using_get(client):
    """Test case for get_withdrawn_object_diff_using_get

    Count difference of withdrawn objects, by type, for specified species and date range
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/stats/diff/withdrawnObject/{species_type_key}/{date_from_yyyymmdd}/{date_to_yyyymmdd}'.format(species_type_key=56, date_from_yyyymmdd='date_from_yyyymmdd_example', date_to_yyyymmdd='date_to_yyyymmdd_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_xdbs_count_using_get(client):
    """Test case for get_xdbs_count_using_get

    Count of external database ids, for specied species and date
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/stats/count/xdb/{species_type_key}/{date_yyyymmdd}'.format(species_type_key=56, date_yyyymmdd='date_yyyymmdd_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_xdbs_diff_using_get(client):
    """Test case for get_xdbs_diff_using_get

    Count difference of external database ids, for specified species and date range
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/stats/diff/xdb/{species_type_key}/{date_from_yyyymmdd}/{date_to_yyyymmdd}'.format(species_type_key=56, date_from_yyyymmdd='date_from_yyyymmdd_example', date_to_yyyymmdd='date_to_yyyymmdd_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

