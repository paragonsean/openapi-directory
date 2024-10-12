from typing import List, Dict
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
from openapi_server import util


async def catalog_create_secret(request: web.Request, database_name, secret_name, api_version, parameters) -> web.Response:
    """catalog_create_secret

    Creates the specified secret for use with external data sources in the specified database.

    :param database_name: The name of the database in which to create the secret.
    :type database_name: str
    :param secret_name: The name of the secret.
    :type secret_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The parameters required to create the secret (name and password)
    :type parameters: dict | bytes

    """
    parameters = DataLakeAnalyticsCatalogSecretCreateOrUpdateParameters.from_dict(parameters)
    return web.Response(status=200)


async def catalog_delete_all_secrets(request: web.Request, database_name, api_version) -> web.Response:
    """catalog_delete_all_secrets

    Deletes all secrets in the specified database

    :param database_name: The name of the database containing the secret.
    :type database_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def catalog_delete_secret(request: web.Request, database_name, secret_name, api_version) -> web.Response:
    """catalog_delete_secret

    Deletes the specified secret in the specified database

    :param database_name: The name of the database containing the secret.
    :type database_name: str
    :param secret_name: The name of the secret to delete
    :type secret_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def catalog_get_assembly(request: web.Request, database_name, assembly_name, api_version) -> web.Response:
    """catalog_get_assembly

    Retrieves the specified assembly from the Data Lake Analytics catalog.

    :param database_name: The name of the database containing the assembly.
    :type database_name: str
    :param assembly_name: The name of the assembly.
    :type assembly_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def catalog_get_credential(request: web.Request, database_name, credential_name, api_version) -> web.Response:
    """catalog_get_credential

    Retrieves the specified credential from the Data Lake Analytics catalog.

    :param database_name: The name of the database containing the schema.
    :type database_name: str
    :param credential_name: The name of the credential.
    :type credential_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def catalog_get_database(request: web.Request, database_name, api_version) -> web.Response:
    """catalog_get_database

    Retrieves the specified database from the Data Lake Analytics catalog.

    :param database_name: The name of the database.
    :type database_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def catalog_get_external_data_source(request: web.Request, database_name, external_data_source_name, api_version) -> web.Response:
    """catalog_get_external_data_source

    Retrieves the specified external data source from the Data Lake Analytics catalog.

    :param database_name: The name of the database containing the external data source.
    :type database_name: str
    :param external_data_source_name: The name of the external data source.
    :type external_data_source_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def catalog_get_procedure(request: web.Request, database_name, schema_name, procedure_name, api_version) -> web.Response:
    """catalog_get_procedure

    Retrieves the specified procedure from the Data Lake Analytics catalog.

    :param database_name: The name of the database containing the procedure.
    :type database_name: str
    :param schema_name: The name of the schema containing the procedure.
    :type schema_name: str
    :param procedure_name: The name of the procedure.
    :type procedure_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def catalog_get_schema(request: web.Request, database_name, schema_name, api_version) -> web.Response:
    """catalog_get_schema

    Retrieves the specified schema from the Data Lake Analytics catalog.

    :param database_name: The name of the database containing the schema.
    :type database_name: str
    :param schema_name: The name of the schema.
    :type schema_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def catalog_get_secret(request: web.Request, database_name, secret_name, api_version) -> web.Response:
    """catalog_get_secret

    Gets the specified secret in the specified database

    :param database_name: The name of the database containing the secret.
    :type database_name: str
    :param secret_name: The name of the secret to get
    :type secret_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def catalog_get_table(request: web.Request, database_name, schema_name, table_name, api_version) -> web.Response:
    """catalog_get_table

    Retrieves the specified table from the Data Lake Analytics catalog.

    :param database_name: The name of the database containing the table.
    :type database_name: str
    :param schema_name: The name of the schema containing the table.
    :type schema_name: str
    :param table_name: The name of the table.
    :type table_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def catalog_get_table_partition(request: web.Request, database_name, schema_name, table_name, partition_name, api_version) -> web.Response:
    """catalog_get_table_partition

    Retrieves the specified table partition from the Data Lake Analytics catalog.

    :param database_name: The name of the database containing the partition.
    :type database_name: str
    :param schema_name: The name of the schema containing the partition.
    :type schema_name: str
    :param table_name: The name of the table containing the partition.
    :type table_name: str
    :param partition_name: The name of the table partition.
    :type partition_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def catalog_get_table_statistic(request: web.Request, database_name, schema_name, table_name, statistics_name, api_version) -> web.Response:
    """catalog_get_table_statistic

    Retrieves the specified table statistics from the Data Lake Analytics catalog.

    :param database_name: The name of the database containing the statistics.
    :type database_name: str
    :param schema_name: The name of the schema containing the statistics.
    :type schema_name: str
    :param table_name: The name of the table containing the statistics.
    :type table_name: str
    :param statistics_name: The name of the table statistics.
    :type statistics_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def catalog_get_table_type(request: web.Request, database_name, schema_name, table_type_name, api_version) -> web.Response:
    """catalog_get_table_type

    Retrieves the specified table type from the Data Lake Analytics catalog.

    :param database_name: The name of the database containing the table type.
    :type database_name: str
    :param schema_name: The name of the schema containing the table type.
    :type schema_name: str
    :param table_type_name: The name of the table type to retrieve.
    :type table_type_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def catalog_get_table_valued_function(request: web.Request, database_name, schema_name, table_valued_function_name, api_version) -> web.Response:
    """catalog_get_table_valued_function

    Retrieves the specified table valued function from the Data Lake Analytics catalog.

    :param database_name: The name of the database containing the table valued function.
    :type database_name: str
    :param schema_name: The name of the schema containing the table valued function.
    :type schema_name: str
    :param table_valued_function_name: The name of the tableValuedFunction.
    :type table_valued_function_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def catalog_get_view(request: web.Request, database_name, schema_name, view_name, api_version) -> web.Response:
    """catalog_get_view

    Retrieves the specified view from the Data Lake Analytics catalog.

    :param database_name: The name of the database containing the view.
    :type database_name: str
    :param schema_name: The name of the schema containing the view.
    :type schema_name: str
    :param view_name: The name of the view.
    :type view_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def catalog_list_assemblies(request: web.Request, database_name, api_version, filter=None, top=None, skip=None, expand=None, select=None, orderby=None, count=None) -> web.Response:
    """catalog_list_assemblies

    Retrieves the list of assemblies from the Data Lake Analytics catalog.

    :param database_name: The name of the database containing the assembly.
    :type database_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param filter: OData filter. Optional.
    :type filter: str
    :param top: The number of items to return. Optional.
    :type top: int
    :param skip: The number of items to skip over before returning elements. Optional.
    :type skip: int
    :param expand: OData expansion. Expand related resources in line with the retrieved resources, e.g. Categories?$expand&#x3D;Products would expand Product data in line with each Category entry. Optional.
    :type expand: str
    :param select: OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional.
    :type select: str
    :param orderby: OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional.
    :type orderby: str
    :param count: The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional.
    :type count: bool

    """
    return web.Response(status=200)


async def catalog_list_credentials(request: web.Request, database_name, api_version, filter=None, top=None, skip=None, expand=None, select=None, orderby=None, count=None) -> web.Response:
    """catalog_list_credentials

    Retrieves the list of credentials from the Data Lake Analytics catalog.

    :param database_name: The name of the database containing the schema.
    :type database_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param filter: OData filter. Optional.
    :type filter: str
    :param top: The number of items to return. Optional.
    :type top: int
    :param skip: The number of items to skip over before returning elements. Optional.
    :type skip: int
    :param expand: OData expansion. Expand related resources in line with the retrieved resources, e.g. Categories?$expand&#x3D;Products would expand Product data in line with each Category entry. Optional.
    :type expand: str
    :param select: OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional.
    :type select: str
    :param orderby: OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional.
    :type orderby: str
    :param count: The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional.
    :type count: bool

    """
    return web.Response(status=200)


async def catalog_list_databases(request: web.Request, api_version, filter=None, top=None, skip=None, expand=None, select=None, orderby=None, count=None) -> web.Response:
    """catalog_list_databases

    Retrieves the list of databases from the Data Lake Analytics catalog.

    :param api_version: Client Api Version.
    :type api_version: str
    :param filter: OData filter. Optional.
    :type filter: str
    :param top: The number of items to return. Optional.
    :type top: int
    :param skip: The number of items to skip over before returning elements. Optional.
    :type skip: int
    :param expand: OData expansion. Expand related resources in line with the retrieved resources, e.g. Categories?$expand&#x3D;Products would expand Product data in line with each Category entry. Optional.
    :type expand: str
    :param select: OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional.
    :type select: str
    :param orderby: OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional.
    :type orderby: str
    :param count: The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional.
    :type count: bool

    """
    return web.Response(status=200)


async def catalog_list_external_data_sources(request: web.Request, database_name, api_version, filter=None, top=None, skip=None, expand=None, select=None, orderby=None, count=None) -> web.Response:
    """catalog_list_external_data_sources

    Retrieves the list of external data sources from the Data Lake Analytics catalog.

    :param database_name: The name of the database containing the external data sources.
    :type database_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param filter: OData filter. Optional.
    :type filter: str
    :param top: The number of items to return. Optional.
    :type top: int
    :param skip: The number of items to skip over before returning elements. Optional.
    :type skip: int
    :param expand: OData expansion. Expand related resources in line with the retrieved resources, e.g. Categories?$expand&#x3D;Products would expand Product data in line with each Category entry. Optional.
    :type expand: str
    :param select: OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional.
    :type select: str
    :param orderby: OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional.
    :type orderby: str
    :param count: The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional.
    :type count: bool

    """
    return web.Response(status=200)


async def catalog_list_procedures(request: web.Request, database_name, schema_name, api_version, filter=None, top=None, skip=None, expand=None, select=None, orderby=None, count=None) -> web.Response:
    """catalog_list_procedures

    Retrieves the list of procedures from the Data Lake Analytics catalog.

    :param database_name: The name of the database containing the procedures.
    :type database_name: str
    :param schema_name: The name of the schema containing the procedures.
    :type schema_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param filter: OData filter. Optional.
    :type filter: str
    :param top: The number of items to return. Optional.
    :type top: int
    :param skip: The number of items to skip over before returning elements. Optional.
    :type skip: int
    :param expand: OData expansion. Expand related resources in line with the retrieved resources, e.g. Categories?$expand&#x3D;Products would expand Product data in line with each Category entry. Optional.
    :type expand: str
    :param select: OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional.
    :type select: str
    :param orderby: OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional.
    :type orderby: str
    :param count: The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional.
    :type count: bool

    """
    return web.Response(status=200)


async def catalog_list_schemas(request: web.Request, database_name, api_version, filter=None, top=None, skip=None, expand=None, select=None, orderby=None, count=None) -> web.Response:
    """catalog_list_schemas

    Retrieves the list of schemas from the Data Lake Analytics catalog.

    :param database_name: The name of the database containing the schema.
    :type database_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param filter: OData filter. Optional.
    :type filter: str
    :param top: The number of items to return. Optional.
    :type top: int
    :param skip: The number of items to skip over before returning elements. Optional.
    :type skip: int
    :param expand: OData expansion. Expand related resources in line with the retrieved resources, e.g. Categories?$expand&#x3D;Products would expand Product data in line with each Category entry. Optional.
    :type expand: str
    :param select: OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional.
    :type select: str
    :param orderby: OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional.
    :type orderby: str
    :param count: The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional.
    :type count: bool

    """
    return web.Response(status=200)


async def catalog_list_table_partitions(request: web.Request, database_name, schema_name, table_name, api_version, filter=None, top=None, skip=None, expand=None, select=None, orderby=None, count=None) -> web.Response:
    """catalog_list_table_partitions

    Retrieves the list of table partitions from the Data Lake Analytics catalog.

    :param database_name: The name of the database containing the partitions.
    :type database_name: str
    :param schema_name: The name of the schema containing the partitions.
    :type schema_name: str
    :param table_name: The name of the table containing the partitions.
    :type table_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param filter: OData filter. Optional.
    :type filter: str
    :param top: The number of items to return. Optional.
    :type top: int
    :param skip: The number of items to skip over before returning elements. Optional.
    :type skip: int
    :param expand: OData expansion. Expand related resources in line with the retrieved resources, e.g. Categories?$expand&#x3D;Products would expand Product data in line with each Category entry. Optional.
    :type expand: str
    :param select: OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional.
    :type select: str
    :param orderby: OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional.
    :type orderby: str
    :param count: The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional.
    :type count: bool

    """
    return web.Response(status=200)


async def catalog_list_table_statistics(request: web.Request, database_name, schema_name, table_name, api_version, filter=None, top=None, skip=None, expand=None, select=None, orderby=None, count=None) -> web.Response:
    """catalog_list_table_statistics

    Retrieves the list of table statistics from the Data Lake Analytics catalog.

    :param database_name: The name of the database containing the statistics.
    :type database_name: str
    :param schema_name: The name of the schema containing the statistics.
    :type schema_name: str
    :param table_name: The name of the table containing the statistics.
    :type table_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param filter: OData filter. Optional.
    :type filter: str
    :param top: The number of items to return. Optional.
    :type top: int
    :param skip: The number of items to skip over before returning elements. Optional.
    :type skip: int
    :param expand: OData expansion. Expand related resources in line with the retrieved resources, e.g. Categories?$expand&#x3D;Products would expand Product data in line with each Category entry. Optional.
    :type expand: str
    :param select: OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional.
    :type select: str
    :param orderby: OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional.
    :type orderby: str
    :param count: The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional.
    :type count: bool

    """
    return web.Response(status=200)


async def catalog_list_table_types(request: web.Request, database_name, schema_name, api_version, filter=None, top=None, skip=None, expand=None, select=None, orderby=None, count=None) -> web.Response:
    """catalog_list_table_types

    Retrieves the list of table types from the Data Lake Analytics catalog.

    :param database_name: The name of the database containing the table types.
    :type database_name: str
    :param schema_name: The name of the schema containing the table types.
    :type schema_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param filter: OData filter. Optional.
    :type filter: str
    :param top: The number of items to return. Optional.
    :type top: int
    :param skip: The number of items to skip over before returning elements. Optional.
    :type skip: int
    :param expand: OData expansion. Expand related resources in line with the retrieved resources, e.g. Categories?$expand&#x3D;Products would expand Product data in line with each Category entry. Optional.
    :type expand: str
    :param select: OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional.
    :type select: str
    :param orderby: OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional.
    :type orderby: str
    :param count: The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional.
    :type count: bool

    """
    return web.Response(status=200)


async def catalog_list_table_valued_functions(request: web.Request, database_name, schema_name, api_version, filter=None, top=None, skip=None, expand=None, select=None, orderby=None, count=None) -> web.Response:
    """catalog_list_table_valued_functions

    Retrieves the list of table valued functions from the Data Lake Analytics catalog.

    :param database_name: The name of the database containing the table valued functions.
    :type database_name: str
    :param schema_name: The name of the schema containing the table valued functions.
    :type schema_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param filter: OData filter. Optional.
    :type filter: str
    :param top: The number of items to return. Optional.
    :type top: int
    :param skip: The number of items to skip over before returning elements. Optional.
    :type skip: int
    :param expand: OData expansion. Expand related resources in line with the retrieved resources, e.g. Categories?$expand&#x3D;Products would expand Product data in line with each Category entry. Optional.
    :type expand: str
    :param select: OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional.
    :type select: str
    :param orderby: OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional.
    :type orderby: str
    :param count: The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional.
    :type count: bool

    """
    return web.Response(status=200)


async def catalog_list_tables(request: web.Request, database_name, schema_name, api_version, filter=None, top=None, skip=None, expand=None, select=None, orderby=None, count=None) -> web.Response:
    """catalog_list_tables

    Retrieves the list of tables from the Data Lake Analytics catalog.

    :param database_name: The name of the database containing the tables.
    :type database_name: str
    :param schema_name: The name of the schema containing the tables.
    :type schema_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param filter: OData filter. Optional.
    :type filter: str
    :param top: The number of items to return. Optional.
    :type top: int
    :param skip: The number of items to skip over before returning elements. Optional.
    :type skip: int
    :param expand: OData expansion. Expand related resources in line with the retrieved resources, e.g. Categories?$expand&#x3D;Products would expand Product data in line with each Category entry. Optional.
    :type expand: str
    :param select: OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional.
    :type select: str
    :param orderby: OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional.
    :type orderby: str
    :param count: The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional.
    :type count: bool

    """
    return web.Response(status=200)


async def catalog_list_types(request: web.Request, database_name, schema_name, api_version, filter=None, top=None, skip=None, expand=None, select=None, orderby=None, count=None) -> web.Response:
    """catalog_list_types

    Retrieves the list of types within the specified database and schema from the Data Lake Analytics catalog.

    :param database_name: The name of the database containing the types.
    :type database_name: str
    :param schema_name: The name of the schema containing the types.
    :type schema_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param filter: OData filter. Optional.
    :type filter: str
    :param top: The number of items to return. Optional.
    :type top: int
    :param skip: The number of items to skip over before returning elements. Optional.
    :type skip: int
    :param expand: OData expansion. Expand related resources in line with the retrieved resources, e.g. Categories?$expand&#x3D;Products would expand Product data in line with each Category entry. Optional.
    :type expand: str
    :param select: OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional.
    :type select: str
    :param orderby: OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional.
    :type orderby: str
    :param count: The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional.
    :type count: bool

    """
    return web.Response(status=200)


async def catalog_list_views(request: web.Request, database_name, schema_name, api_version, filter=None, top=None, skip=None, expand=None, select=None, orderby=None, count=None) -> web.Response:
    """catalog_list_views

    Retrieves the list of views from the Data Lake Analytics catalog.

    :param database_name: The name of the database containing the views.
    :type database_name: str
    :param schema_name: The name of the schema containing the views.
    :type schema_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param filter: OData filter. Optional.
    :type filter: str
    :param top: The number of items to return. Optional.
    :type top: int
    :param skip: The number of items to skip over before returning elements. Optional.
    :type skip: int
    :param expand: OData expansion. Expand related resources in line with the retrieved resources, e.g. Categories?$expand&#x3D;Products would expand Product data in line with each Category entry. Optional.
    :type expand: str
    :param select: OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional.
    :type select: str
    :param orderby: OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional.
    :type orderby: str
    :param count: The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional.
    :type count: bool

    """
    return web.Response(status=200)


async def catalog_update_secret(request: web.Request, database_name, secret_name, api_version, parameters) -> web.Response:
    """catalog_update_secret

    Modifies the specified secret for use with external data sources in the specified database

    :param database_name: The name of the database containing the secret.
    :type database_name: str
    :param secret_name: The name of the secret.
    :type secret_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The parameters required to modify the secret (name and password)
    :type parameters: dict | bytes

    """
    parameters = DataLakeAnalyticsCatalogSecretCreateOrUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
