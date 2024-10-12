# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.data_lake_analytics_catalog_secret_create_or_update_parameters import DataLakeAnalyticsCatalogSecretCreateOrUpdateParameters
from openapi_server.models.u_sql_assembly import USqlAssembly
from openapi_server.models.u_sql_assembly_list import USqlAssemblyList
from openapi_server.models.u_sql_credential import USqlCredential
from openapi_server.models.u_sql_credential_list import USqlCredentialList
from openapi_server.models.u_sql_database import USqlDatabase
from openapi_server.models.u_sql_database_list import USqlDatabaseList
from openapi_server.models.u_sql_external_data_source import USqlExternalDataSource
from openapi_server.models.u_sql_external_data_source_list import USqlExternalDataSourceList
from openapi_server.models.u_sql_procedure import USqlProcedure
from openapi_server.models.u_sql_procedure_list import USqlProcedureList
from openapi_server.models.u_sql_schema import USqlSchema
from openapi_server.models.u_sql_schema_list import USqlSchemaList
from openapi_server.models.u_sql_secret import USqlSecret
from openapi_server.models.u_sql_table import USqlTable
from openapi_server.models.u_sql_table_list import USqlTableList
from openapi_server.models.u_sql_table_partition import USqlTablePartition
from openapi_server.models.u_sql_table_partition_list import USqlTablePartitionList
from openapi_server.models.u_sql_table_statistics import USqlTableStatistics
from openapi_server.models.u_sql_table_statistics_list import USqlTableStatisticsList
from openapi_server.models.u_sql_table_type import USqlTableType
from openapi_server.models.u_sql_table_type_list import USqlTableTypeList
from openapi_server.models.u_sql_table_valued_function import USqlTableValuedFunction
from openapi_server.models.u_sql_table_valued_function_list import USqlTableValuedFunctionList
from openapi_server.models.u_sql_type_list import USqlTypeList
from openapi_server.models.u_sql_view import USqlView
from openapi_server.models.u_sql_view_list import USqlViewList


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_catalog_create_secret(client):
    """Test case for catalog_create_secret

    
    """
    parameters = {"password":"password","uri":"uri"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/catalog/usql/databases/{database_name}/secrets/{secret_name}'.format(database_name='database_name_example', secret_name='secret_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_delete_all_secrets(client):
    """Test case for catalog_delete_all_secrets

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/catalog/usql/databases/{database_name}/secrets'.format(database_name='database_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_delete_secret(client):
    """Test case for catalog_delete_secret

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/catalog/usql/databases/{database_name}/secrets/{secret_name}'.format(database_name='database_name_example', secret_name='secret_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_get_assembly(client):
    """Test case for catalog_get_assembly

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/catalog/usql/databases/{database_name}/assemblies/{assembly_name}'.format(database_name='database_name_example', assembly_name='assembly_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_get_credential(client):
    """Test case for catalog_get_credential

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/catalog/usql/databases/{database_name}/credentials/{credential_name}'.format(database_name='database_name_example', credential_name='credential_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_get_database(client):
    """Test case for catalog_get_database

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/catalog/usql/databases/{database_name}'.format(database_name='database_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_get_external_data_source(client):
    """Test case for catalog_get_external_data_source

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/catalog/usql/databases/{database_name}/externaldatasources/{external_data_source_name}'.format(database_name='database_name_example', external_data_source_name='external_data_source_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_get_procedure(client):
    """Test case for catalog_get_procedure

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/catalog/usql/databases/{database_name}/schemas/{schema_name}/procedures/{procedure_name}'.format(database_name='database_name_example', schema_name='schema_name_example', procedure_name='procedure_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_get_schema(client):
    """Test case for catalog_get_schema

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/catalog/usql/databases/{database_name}/schemas/{schema_name}'.format(database_name='database_name_example', schema_name='schema_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_get_secret(client):
    """Test case for catalog_get_secret

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/catalog/usql/databases/{database_name}/secrets/{secret_name}'.format(database_name='database_name_example', secret_name='secret_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_get_table(client):
    """Test case for catalog_get_table

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/catalog/usql/databases/{database_name}/schemas/{schema_name}/tables/{table_name}'.format(database_name='database_name_example', schema_name='schema_name_example', table_name='table_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_get_table_partition(client):
    """Test case for catalog_get_table_partition

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/catalog/usql/databases/{database_name}/schemas/{schema_name}/tables/{table_name}/partitions/{partition_name}'.format(database_name='database_name_example', schema_name='schema_name_example', table_name='table_name_example', partition_name='partition_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_get_table_statistic(client):
    """Test case for catalog_get_table_statistic

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/catalog/usql/databases/{database_name}/schemas/{schema_name}/tables/{table_name}/statistics/{statistics_name}'.format(database_name='database_name_example', schema_name='schema_name_example', table_name='table_name_example', statistics_name='statistics_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_get_table_type(client):
    """Test case for catalog_get_table_type

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/catalog/usql/databases/{database_name}/schemas/{schema_name}/tabletypes/{table_type_name}'.format(database_name='database_name_example', schema_name='schema_name_example', table_type_name='table_type_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_get_table_valued_function(client):
    """Test case for catalog_get_table_valued_function

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/catalog/usql/databases/{database_name}/schemas/{schema_name}/tablevaluedfunctions/{table_valued_function_name}'.format(database_name='database_name_example', schema_name='schema_name_example', table_valued_function_name='table_valued_function_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_get_view(client):
    """Test case for catalog_get_view

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/catalog/usql/databases/{database_name}/schemas/{schema_name}/views/{view_name}'.format(database_name='database_name_example', schema_name='schema_name_example', view_name='view_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_list_assemblies(client):
    """Test case for catalog_list_assemblies

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('$expand', 'expand_example'),
                    ('$select', 'select_example'),
                    ('$orderby', 'orderby_example'),
                    ('$count', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/catalog/usql/databases/{database_name}/assemblies'.format(database_name='database_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_list_credentials(client):
    """Test case for catalog_list_credentials

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('$expand', 'expand_example'),
                    ('$select', 'select_example'),
                    ('$orderby', 'orderby_example'),
                    ('$count', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/catalog/usql/databases/{database_name}/credentials'.format(database_name='database_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_list_databases(client):
    """Test case for catalog_list_databases

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('$expand', 'expand_example'),
                    ('$select', 'select_example'),
                    ('$orderby', 'orderby_example'),
                    ('$count', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/catalog/usql/databases',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_list_external_data_sources(client):
    """Test case for catalog_list_external_data_sources

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('$expand', 'expand_example'),
                    ('$select', 'select_example'),
                    ('$orderby', 'orderby_example'),
                    ('$count', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/catalog/usql/databases/{database_name}/externaldatasources'.format(database_name='database_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_list_procedures(client):
    """Test case for catalog_list_procedures

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('$expand', 'expand_example'),
                    ('$select', 'select_example'),
                    ('$orderby', 'orderby_example'),
                    ('$count', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/catalog/usql/databases/{database_name}/schemas/{schema_name}/procedures'.format(database_name='database_name_example', schema_name='schema_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_list_schemas(client):
    """Test case for catalog_list_schemas

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('$expand', 'expand_example'),
                    ('$select', 'select_example'),
                    ('$orderby', 'orderby_example'),
                    ('$count', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/catalog/usql/databases/{database_name}/schemas'.format(database_name='database_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_list_table_partitions(client):
    """Test case for catalog_list_table_partitions

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('$expand', 'expand_example'),
                    ('$select', 'select_example'),
                    ('$orderby', 'orderby_example'),
                    ('$count', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/catalog/usql/databases/{database_name}/schemas/{schema_name}/tables/{table_name}/partitions'.format(database_name='database_name_example', schema_name='schema_name_example', table_name='table_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_list_table_statistics(client):
    """Test case for catalog_list_table_statistics

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('$expand', 'expand_example'),
                    ('$select', 'select_example'),
                    ('$orderby', 'orderby_example'),
                    ('$count', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/catalog/usql/databases/{database_name}/schemas/{schema_name}/tables/{table_name}/statistics'.format(database_name='database_name_example', schema_name='schema_name_example', table_name='table_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_list_table_types(client):
    """Test case for catalog_list_table_types

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('$expand', 'expand_example'),
                    ('$select', 'select_example'),
                    ('$orderby', 'orderby_example'),
                    ('$count', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/catalog/usql/databases/{database_name}/schemas/{schema_name}/tabletypes'.format(database_name='database_name_example', schema_name='schema_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_list_table_valued_functions(client):
    """Test case for catalog_list_table_valued_functions

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('$expand', 'expand_example'),
                    ('$select', 'select_example'),
                    ('$orderby', 'orderby_example'),
                    ('$count', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/catalog/usql/databases/{database_name}/schemas/{schema_name}/tablevaluedfunctions'.format(database_name='database_name_example', schema_name='schema_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_list_tables(client):
    """Test case for catalog_list_tables

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('$expand', 'expand_example'),
                    ('$select', 'select_example'),
                    ('$orderby', 'orderby_example'),
                    ('$count', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/catalog/usql/databases/{database_name}/schemas/{schema_name}/tables'.format(database_name='database_name_example', schema_name='schema_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_list_types(client):
    """Test case for catalog_list_types

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('$expand', 'expand_example'),
                    ('$select', 'select_example'),
                    ('$orderby', 'orderby_example'),
                    ('$count', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/catalog/usql/databases/{database_name}/schemas/{schema_name}/types'.format(database_name='database_name_example', schema_name='schema_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_list_views(client):
    """Test case for catalog_list_views

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('$expand', 'expand_example'),
                    ('$select', 'select_example'),
                    ('$orderby', 'orderby_example'),
                    ('$count', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/catalog/usql/databases/{database_name}/schemas/{schema_name}/views'.format(database_name='database_name_example', schema_name='schema_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_catalog_update_secret(client):
    """Test case for catalog_update_secret

    
    """
    parameters = {"password":"password","uri":"uri"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/catalog/usql/databases/{database_name}/secrets/{secret_name}'.format(database_name='database_name_example', secret_name='secret_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

