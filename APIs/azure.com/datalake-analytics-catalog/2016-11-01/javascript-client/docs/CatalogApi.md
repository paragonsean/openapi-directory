# DataLakeAnalyticsCatalogManagementClient.CatalogApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogCreateCredential**](CatalogApi.md#catalogCreateCredential) | **PUT** /catalog/usql/databases/{databaseName}/credentials/{credentialName} | 
[**catalogCreateSecret**](CatalogApi.md#catalogCreateSecret) | **PUT** /catalog/usql/databases/{databaseName}/secrets/{secretName} | 
[**catalogDeleteAllSecrets**](CatalogApi.md#catalogDeleteAllSecrets) | **DELETE** /catalog/usql/databases/{databaseName}/secrets | 
[**catalogDeleteCredential**](CatalogApi.md#catalogDeleteCredential) | **POST** /catalog/usql/databases/{databaseName}/credentials/{credentialName} | 
[**catalogDeleteSecret**](CatalogApi.md#catalogDeleteSecret) | **DELETE** /catalog/usql/databases/{databaseName}/secrets/{secretName} | 
[**catalogGetAssembly**](CatalogApi.md#catalogGetAssembly) | **GET** /catalog/usql/databases/{databaseName}/assemblies/{assemblyName} | 
[**catalogGetCredential**](CatalogApi.md#catalogGetCredential) | **GET** /catalog/usql/databases/{databaseName}/credentials/{credentialName} | 
[**catalogGetDatabase**](CatalogApi.md#catalogGetDatabase) | **GET** /catalog/usql/databases/{databaseName} | 
[**catalogGetExternalDataSource**](CatalogApi.md#catalogGetExternalDataSource) | **GET** /catalog/usql/databases/{databaseName}/externaldatasources/{externalDataSourceName} | 
[**catalogGetPackage**](CatalogApi.md#catalogGetPackage) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/packages/{packageName} | 
[**catalogGetProcedure**](CatalogApi.md#catalogGetProcedure) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/procedures/{procedureName} | 
[**catalogGetSchema**](CatalogApi.md#catalogGetSchema) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName} | 
[**catalogGetSecret**](CatalogApi.md#catalogGetSecret) | **GET** /catalog/usql/databases/{databaseName}/secrets/{secretName} | 
[**catalogGetTable**](CatalogApi.md#catalogGetTable) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/tables/{tableName} | 
[**catalogGetTablePartition**](CatalogApi.md#catalogGetTablePartition) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/tables/{tableName}/partitions/{partitionName} | 
[**catalogGetTableStatistic**](CatalogApi.md#catalogGetTableStatistic) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/tables/{tableName}/statistics/{statisticsName} | 
[**catalogGetTableType**](CatalogApi.md#catalogGetTableType) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/tabletypes/{tableTypeName} | 
[**catalogGetTableValuedFunction**](CatalogApi.md#catalogGetTableValuedFunction) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/tablevaluedfunctions/{tableValuedFunctionName} | 
[**catalogGetView**](CatalogApi.md#catalogGetView) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/views/{viewName} | 
[**catalogListAcls**](CatalogApi.md#catalogListAcls) | **GET** /catalog/usql/acl | 
[**catalogListAclsByDatabase**](CatalogApi.md#catalogListAclsByDatabase) | **GET** /catalog/usql/databases/{databaseName}/acl | 
[**catalogListAssemblies**](CatalogApi.md#catalogListAssemblies) | **GET** /catalog/usql/databases/{databaseName}/assemblies | 
[**catalogListCredentials**](CatalogApi.md#catalogListCredentials) | **GET** /catalog/usql/databases/{databaseName}/credentials | 
[**catalogListDatabases**](CatalogApi.md#catalogListDatabases) | **GET** /catalog/usql/databases | 
[**catalogListExternalDataSources**](CatalogApi.md#catalogListExternalDataSources) | **GET** /catalog/usql/databases/{databaseName}/externaldatasources | 
[**catalogListPackages**](CatalogApi.md#catalogListPackages) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/packages | 
[**catalogListProcedures**](CatalogApi.md#catalogListProcedures) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/procedures | 
[**catalogListSchemas**](CatalogApi.md#catalogListSchemas) | **GET** /catalog/usql/databases/{databaseName}/schemas | 
[**catalogListTableFragments**](CatalogApi.md#catalogListTableFragments) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/tables/{tableName}/tablefragments | 
[**catalogListTablePartitions**](CatalogApi.md#catalogListTablePartitions) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/tables/{tableName}/partitions | 
[**catalogListTableStatistics**](CatalogApi.md#catalogListTableStatistics) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/tables/{tableName}/statistics | 
[**catalogListTableStatisticsByDatabase**](CatalogApi.md#catalogListTableStatisticsByDatabase) | **GET** /catalog/usql/databases/{databaseName}/statistics | 
[**catalogListTableStatisticsByDatabaseAndSchema**](CatalogApi.md#catalogListTableStatisticsByDatabaseAndSchema) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/statistics | 
[**catalogListTableTypes**](CatalogApi.md#catalogListTableTypes) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/tabletypes | 
[**catalogListTableValuedFunctions**](CatalogApi.md#catalogListTableValuedFunctions) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/tablevaluedfunctions | 
[**catalogListTableValuedFunctionsByDatabase**](CatalogApi.md#catalogListTableValuedFunctionsByDatabase) | **GET** /catalog/usql/databases/{databaseName}/tablevaluedfunctions | 
[**catalogListTables**](CatalogApi.md#catalogListTables) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/tables | 
[**catalogListTablesByDatabase**](CatalogApi.md#catalogListTablesByDatabase) | **GET** /catalog/usql/databases/{databaseName}/tables | 
[**catalogListTypes**](CatalogApi.md#catalogListTypes) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/types | 
[**catalogListViews**](CatalogApi.md#catalogListViews) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/views | 
[**catalogListViewsByDatabase**](CatalogApi.md#catalogListViewsByDatabase) | **GET** /catalog/usql/databases/{databaseName}/views | 
[**catalogPreviewTable**](CatalogApi.md#catalogPreviewTable) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/tables/{tableName}/previewrows | 
[**catalogPreviewTablePartition**](CatalogApi.md#catalogPreviewTablePartition) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/tables/{tableName}/partitions/{partitionName}/previewrows | 
[**catalogUpdateCredential**](CatalogApi.md#catalogUpdateCredential) | **PATCH** /catalog/usql/databases/{databaseName}/credentials/{credentialName} | 
[**catalogUpdateSecret**](CatalogApi.md#catalogUpdateSecret) | **PATCH** /catalog/usql/databases/{databaseName}/secrets/{secretName} | 



## catalogCreateCredential

> catalogCreateCredential(databaseName, credentialName, apiVersion, parameters)



Creates the specified credential for use with external data sources in the specified database.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database in which to create the credential. Note: This is NOT an external database name, but the name of an existing U-SQL database that should contain the new credential object.
let credentialName = "credentialName_example"; // String | The name of the credential.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let parameters = new DataLakeAnalyticsCatalogManagementClient.DataLakeAnalyticsCatalogCredentialCreateParameters(); // DataLakeAnalyticsCatalogCredentialCreateParameters | The parameters required to create the credential (name and password)
apiInstance.catalogCreateCredential(databaseName, credentialName, apiVersion, parameters, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database in which to create the credential. Note: This is NOT an external database name, but the name of an existing U-SQL database that should contain the new credential object. | 
 **credentialName** | **String**| The name of the credential. | 
 **apiVersion** | **String**| Client Api Version. | 
 **parameters** | [**DataLakeAnalyticsCatalogCredentialCreateParameters**](DataLakeAnalyticsCatalogCredentialCreateParameters.md)| The parameters required to create the credential (name and password) | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## catalogCreateSecret

> catalogCreateSecret(databaseName, secretName, apiVersion, parameters)



Creates the specified secret for use with external data sources in the specified database. This is deprecated and will be removed in the next release. Please use CreateCredential instead.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database in which to create the secret.
let secretName = "secretName_example"; // String | The name of the secret.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let parameters = new DataLakeAnalyticsCatalogManagementClient.DataLakeAnalyticsCatalogSecretCreateOrUpdateParameters(); // DataLakeAnalyticsCatalogSecretCreateOrUpdateParameters | The parameters required to create the secret (name and password)
apiInstance.catalogCreateSecret(databaseName, secretName, apiVersion, parameters, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database in which to create the secret. | 
 **secretName** | **String**| The name of the secret. | 
 **apiVersion** | **String**| Client Api Version. | 
 **parameters** | [**DataLakeAnalyticsCatalogSecretCreateOrUpdateParameters**](DataLakeAnalyticsCatalogSecretCreateOrUpdateParameters.md)| The parameters required to create the secret (name and password) | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## catalogDeleteAllSecrets

> catalogDeleteAllSecrets(databaseName, apiVersion)



Deletes all secrets in the specified database. This is deprecated and will be removed in the next release. In the future, please only drop individual credentials using DeleteCredential

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the secret.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.catalogDeleteAllSecrets(databaseName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the secret. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## catalogDeleteCredential

> catalogDeleteCredential(databaseName, credentialName, apiVersion, opts)



Deletes the specified credential in the specified database

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the credential.
let credentialName = "credentialName_example"; // String | The name of the credential to delete
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'cascade': false, // Boolean | Indicates if the delete should be a cascading delete (which deletes all resources dependent on the credential as well as the credential) or not. If false will fail if there are any resources relying on the credential.
  'parameters': new DataLakeAnalyticsCatalogManagementClient.DataLakeAnalyticsCatalogCredentialDeleteParameters() // DataLakeAnalyticsCatalogCredentialDeleteParameters | The parameters to delete a credential if the current user is not the account owner.
};
apiInstance.catalogDeleteCredential(databaseName, credentialName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the credential. | 
 **credentialName** | **String**| The name of the credential to delete | 
 **apiVersion** | **String**| Client Api Version. | 
 **cascade** | **Boolean**| Indicates if the delete should be a cascading delete (which deletes all resources dependent on the credential as well as the credential) or not. If false will fail if there are any resources relying on the credential. | [optional] [default to false]
 **parameters** | [**DataLakeAnalyticsCatalogCredentialDeleteParameters**](DataLakeAnalyticsCatalogCredentialDeleteParameters.md)| The parameters to delete a credential if the current user is not the account owner. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## catalogDeleteSecret

> catalogDeleteSecret(databaseName, secretName, apiVersion)



Deletes the specified secret in the specified database. This is deprecated and will be removed in the next release. Please use DeleteCredential instead.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the secret.
let secretName = "secretName_example"; // String | The name of the secret to delete
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.catalogDeleteSecret(databaseName, secretName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the secret. | 
 **secretName** | **String**| The name of the secret to delete | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## catalogGetAssembly

> USqlAssembly catalogGetAssembly(databaseName, assemblyName, apiVersion)



Retrieves the specified assembly from the Data Lake Analytics catalog.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the assembly.
let assemblyName = "assemblyName_example"; // String | The name of the assembly.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.catalogGetAssembly(databaseName, assemblyName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the assembly. | 
 **assemblyName** | **String**| The name of the assembly. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**USqlAssembly**](USqlAssembly.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogGetCredential

> USqlCredential catalogGetCredential(databaseName, credentialName, apiVersion)



Retrieves the specified credential from the Data Lake Analytics catalog.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the schema.
let credentialName = "credentialName_example"; // String | The name of the credential.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.catalogGetCredential(databaseName, credentialName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the schema. | 
 **credentialName** | **String**| The name of the credential. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**USqlCredential**](USqlCredential.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogGetDatabase

> USqlDatabase catalogGetDatabase(databaseName, apiVersion)



Retrieves the specified database from the Data Lake Analytics catalog.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.catalogGetDatabase(databaseName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**USqlDatabase**](USqlDatabase.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogGetExternalDataSource

> USqlExternalDataSource catalogGetExternalDataSource(databaseName, externalDataSourceName, apiVersion)



Retrieves the specified external data source from the Data Lake Analytics catalog.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the external data source.
let externalDataSourceName = "externalDataSourceName_example"; // String | The name of the external data source.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.catalogGetExternalDataSource(databaseName, externalDataSourceName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the external data source. | 
 **externalDataSourceName** | **String**| The name of the external data source. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**USqlExternalDataSource**](USqlExternalDataSource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogGetPackage

> USqlPackage catalogGetPackage(databaseName, schemaName, packageName, apiVersion)



Retrieves the specified package from the Data Lake Analytics catalog.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the package.
let schemaName = "schemaName_example"; // String | The name of the schema containing the package.
let packageName = "packageName_example"; // String | The name of the package.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.catalogGetPackage(databaseName, schemaName, packageName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the package. | 
 **schemaName** | **String**| The name of the schema containing the package. | 
 **packageName** | **String**| The name of the package. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**USqlPackage**](USqlPackage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogGetProcedure

> USqlProcedure catalogGetProcedure(databaseName, schemaName, procedureName, apiVersion)



Retrieves the specified procedure from the Data Lake Analytics catalog.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the procedure.
let schemaName = "schemaName_example"; // String | The name of the schema containing the procedure.
let procedureName = "procedureName_example"; // String | The name of the procedure.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.catalogGetProcedure(databaseName, schemaName, procedureName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the procedure. | 
 **schemaName** | **String**| The name of the schema containing the procedure. | 
 **procedureName** | **String**| The name of the procedure. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**USqlProcedure**](USqlProcedure.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogGetSchema

> USqlSchema catalogGetSchema(databaseName, schemaName, apiVersion)



Retrieves the specified schema from the Data Lake Analytics catalog.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the schema.
let schemaName = "schemaName_example"; // String | The name of the schema.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.catalogGetSchema(databaseName, schemaName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the schema. | 
 **schemaName** | **String**| The name of the schema. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**USqlSchema**](USqlSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogGetSecret

> USqlSecret catalogGetSecret(databaseName, secretName, apiVersion)



Gets the specified secret in the specified database. This is deprecated and will be removed in the next release. Please use GetCredential instead.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the secret.
let secretName = "secretName_example"; // String | The name of the secret to get
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.catalogGetSecret(databaseName, secretName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the secret. | 
 **secretName** | **String**| The name of the secret to get | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**USqlSecret**](USqlSecret.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogGetTable

> USqlTable catalogGetTable(databaseName, schemaName, tableName, apiVersion)



Retrieves the specified table from the Data Lake Analytics catalog.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the table.
let schemaName = "schemaName_example"; // String | The name of the schema containing the table.
let tableName = "tableName_example"; // String | The name of the table.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.catalogGetTable(databaseName, schemaName, tableName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the table. | 
 **schemaName** | **String**| The name of the schema containing the table. | 
 **tableName** | **String**| The name of the table. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**USqlTable**](USqlTable.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogGetTablePartition

> USqlTablePartition catalogGetTablePartition(databaseName, schemaName, tableName, partitionName, apiVersion)



Retrieves the specified table partition from the Data Lake Analytics catalog.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the partition.
let schemaName = "schemaName_example"; // String | The name of the schema containing the partition.
let tableName = "tableName_example"; // String | The name of the table containing the partition.
let partitionName = "partitionName_example"; // String | The name of the table partition.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.catalogGetTablePartition(databaseName, schemaName, tableName, partitionName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the partition. | 
 **schemaName** | **String**| The name of the schema containing the partition. | 
 **tableName** | **String**| The name of the table containing the partition. | 
 **partitionName** | **String**| The name of the table partition. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**USqlTablePartition**](USqlTablePartition.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogGetTableStatistic

> USqlTableStatistics catalogGetTableStatistic(databaseName, schemaName, tableName, statisticsName, apiVersion)



Retrieves the specified table statistics from the Data Lake Analytics catalog.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the statistics.
let schemaName = "schemaName_example"; // String | The name of the schema containing the statistics.
let tableName = "tableName_example"; // String | The name of the table containing the statistics.
let statisticsName = "statisticsName_example"; // String | The name of the table statistics.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.catalogGetTableStatistic(databaseName, schemaName, tableName, statisticsName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the statistics. | 
 **schemaName** | **String**| The name of the schema containing the statistics. | 
 **tableName** | **String**| The name of the table containing the statistics. | 
 **statisticsName** | **String**| The name of the table statistics. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**USqlTableStatistics**](USqlTableStatistics.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogGetTableType

> USqlTableType catalogGetTableType(databaseName, schemaName, tableTypeName, apiVersion)



Retrieves the specified table type from the Data Lake Analytics catalog.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the table type.
let schemaName = "schemaName_example"; // String | The name of the schema containing the table type.
let tableTypeName = "tableTypeName_example"; // String | The name of the table type to retrieve.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.catalogGetTableType(databaseName, schemaName, tableTypeName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the table type. | 
 **schemaName** | **String**| The name of the schema containing the table type. | 
 **tableTypeName** | **String**| The name of the table type to retrieve. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**USqlTableType**](USqlTableType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogGetTableValuedFunction

> USqlTableValuedFunction catalogGetTableValuedFunction(databaseName, schemaName, tableValuedFunctionName, apiVersion)



Retrieves the specified table valued function from the Data Lake Analytics catalog.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the table valued function.
let schemaName = "schemaName_example"; // String | The name of the schema containing the table valued function.
let tableValuedFunctionName = "tableValuedFunctionName_example"; // String | The name of the tableValuedFunction.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.catalogGetTableValuedFunction(databaseName, schemaName, tableValuedFunctionName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the table valued function. | 
 **schemaName** | **String**| The name of the schema containing the table valued function. | 
 **tableValuedFunctionName** | **String**| The name of the tableValuedFunction. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**USqlTableValuedFunction**](USqlTableValuedFunction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogGetView

> USqlView catalogGetView(databaseName, schemaName, viewName, apiVersion)



Retrieves the specified view from the Data Lake Analytics catalog.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the view.
let schemaName = "schemaName_example"; // String | The name of the schema containing the view.
let viewName = "viewName_example"; // String | The name of the view.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.catalogGetView(databaseName, schemaName, viewName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the view. | 
 **schemaName** | **String**| The name of the schema containing the view. | 
 **viewName** | **String**| The name of the view. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**USqlView**](USqlView.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogListAcls

> AclList catalogListAcls(apiVersion, opts)



Retrieves the list of access control list (ACL) entries for the Data Lake Analytics catalog.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example", // String | OData filter. Optional.
  'top': 56, // Number | The number of items to return. Optional.
  'skip': 56, // Number | The number of items to skip over before returning elements. Optional.
  'select': "select_example", // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
  'orderby': "orderby_example", // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
  'count': true // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
};
apiInstance.catalogListAcls(apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiVersion** | **String**| Client Api Version. | 
 **filter** | **String**| OData filter. Optional. | [optional] 
 **top** | **Number**| The number of items to return. Optional. | [optional] 
 **skip** | **Number**| The number of items to skip over before returning elements. Optional. | [optional] 
 **select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] 
 **orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] 
 **count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] 

### Return type

[**AclList**](AclList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogListAclsByDatabase

> AclList catalogListAclsByDatabase(databaseName, apiVersion, opts)



Retrieves the list of access control list (ACL) entries for the database from the Data Lake Analytics catalog.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example", // String | OData filter. Optional.
  'top': 56, // Number | The number of items to return. Optional.
  'skip': 56, // Number | The number of items to skip over before returning elements. Optional.
  'select': "select_example", // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
  'orderby': "orderby_example", // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
  'count': true // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
};
apiInstance.catalogListAclsByDatabase(databaseName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database. | 
 **apiVersion** | **String**| Client Api Version. | 
 **filter** | **String**| OData filter. Optional. | [optional] 
 **top** | **Number**| The number of items to return. Optional. | [optional] 
 **skip** | **Number**| The number of items to skip over before returning elements. Optional. | [optional] 
 **select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] 
 **orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] 
 **count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] 

### Return type

[**AclList**](AclList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogListAssemblies

> USqlAssemblyList catalogListAssemblies(databaseName, apiVersion, opts)



Retrieves the list of assemblies from the Data Lake Analytics catalog.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the assembly.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example", // String | OData filter. Optional.
  'top': 56, // Number | The number of items to return. Optional.
  'skip': 56, // Number | The number of items to skip over before returning elements. Optional.
  'select': "select_example", // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
  'orderby': "orderby_example", // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
  'count': true // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
};
apiInstance.catalogListAssemblies(databaseName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the assembly. | 
 **apiVersion** | **String**| Client Api Version. | 
 **filter** | **String**| OData filter. Optional. | [optional] 
 **top** | **Number**| The number of items to return. Optional. | [optional] 
 **skip** | **Number**| The number of items to skip over before returning elements. Optional. | [optional] 
 **select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] 
 **orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] 
 **count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] 

### Return type

[**USqlAssemblyList**](USqlAssemblyList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogListCredentials

> USqlCredentialList catalogListCredentials(databaseName, apiVersion, opts)



Retrieves the list of credentials from the Data Lake Analytics catalog.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the schema.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example", // String | OData filter. Optional.
  'top': 56, // Number | The number of items to return. Optional.
  'skip': 56, // Number | The number of items to skip over before returning elements. Optional.
  'select': "select_example", // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
  'orderby': "orderby_example", // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
  'count': true // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
};
apiInstance.catalogListCredentials(databaseName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the schema. | 
 **apiVersion** | **String**| Client Api Version. | 
 **filter** | **String**| OData filter. Optional. | [optional] 
 **top** | **Number**| The number of items to return. Optional. | [optional] 
 **skip** | **Number**| The number of items to skip over before returning elements. Optional. | [optional] 
 **select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] 
 **orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] 
 **count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] 

### Return type

[**USqlCredentialList**](USqlCredentialList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogListDatabases

> USqlDatabaseList catalogListDatabases(apiVersion, opts)



Retrieves the list of databases from the Data Lake Analytics catalog.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example", // String | OData filter. Optional.
  'top': 56, // Number | The number of items to return. Optional.
  'skip': 56, // Number | The number of items to skip over before returning elements. Optional.
  'select': "select_example", // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
  'orderby': "orderby_example", // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
  'count': true // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
};
apiInstance.catalogListDatabases(apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiVersion** | **String**| Client Api Version. | 
 **filter** | **String**| OData filter. Optional. | [optional] 
 **top** | **Number**| The number of items to return. Optional. | [optional] 
 **skip** | **Number**| The number of items to skip over before returning elements. Optional. | [optional] 
 **select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] 
 **orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] 
 **count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] 

### Return type

[**USqlDatabaseList**](USqlDatabaseList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogListExternalDataSources

> USqlExternalDataSourceList catalogListExternalDataSources(databaseName, apiVersion, opts)



Retrieves the list of external data sources from the Data Lake Analytics catalog.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the external data sources.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example", // String | OData filter. Optional.
  'top': 56, // Number | The number of items to return. Optional.
  'skip': 56, // Number | The number of items to skip over before returning elements. Optional.
  'select': "select_example", // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
  'orderby': "orderby_example", // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
  'count': true // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
};
apiInstance.catalogListExternalDataSources(databaseName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the external data sources. | 
 **apiVersion** | **String**| Client Api Version. | 
 **filter** | **String**| OData filter. Optional. | [optional] 
 **top** | **Number**| The number of items to return. Optional. | [optional] 
 **skip** | **Number**| The number of items to skip over before returning elements. Optional. | [optional] 
 **select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] 
 **orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] 
 **count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] 

### Return type

[**USqlExternalDataSourceList**](USqlExternalDataSourceList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogListPackages

> USqlPackageList catalogListPackages(databaseName, schemaName, apiVersion, opts)



Retrieves the list of packages from the Data Lake Analytics catalog.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the packages.
let schemaName = "schemaName_example"; // String | The name of the schema containing the packages.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example", // String | OData filter. Optional.
  'top': 56, // Number | The number of items to return. Optional.
  'skip': 56, // Number | The number of items to skip over before returning elements. Optional.
  'select': "select_example", // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
  'orderby': "orderby_example", // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
  'count': true // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
};
apiInstance.catalogListPackages(databaseName, schemaName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the packages. | 
 **schemaName** | **String**| The name of the schema containing the packages. | 
 **apiVersion** | **String**| Client Api Version. | 
 **filter** | **String**| OData filter. Optional. | [optional] 
 **top** | **Number**| The number of items to return. Optional. | [optional] 
 **skip** | **Number**| The number of items to skip over before returning elements. Optional. | [optional] 
 **select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] 
 **orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] 
 **count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] 

### Return type

[**USqlPackageList**](USqlPackageList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogListProcedures

> USqlProcedureList catalogListProcedures(databaseName, schemaName, apiVersion, opts)



Retrieves the list of procedures from the Data Lake Analytics catalog.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the procedures.
let schemaName = "schemaName_example"; // String | The name of the schema containing the procedures.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example", // String | OData filter. Optional.
  'top': 56, // Number | The number of items to return. Optional.
  'skip': 56, // Number | The number of items to skip over before returning elements. Optional.
  'select': "select_example", // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
  'orderby': "orderby_example", // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
  'count': true // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
};
apiInstance.catalogListProcedures(databaseName, schemaName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the procedures. | 
 **schemaName** | **String**| The name of the schema containing the procedures. | 
 **apiVersion** | **String**| Client Api Version. | 
 **filter** | **String**| OData filter. Optional. | [optional] 
 **top** | **Number**| The number of items to return. Optional. | [optional] 
 **skip** | **Number**| The number of items to skip over before returning elements. Optional. | [optional] 
 **select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] 
 **orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] 
 **count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] 

### Return type

[**USqlProcedureList**](USqlProcedureList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogListSchemas

> USqlSchemaList catalogListSchemas(databaseName, apiVersion, opts)



Retrieves the list of schemas from the Data Lake Analytics catalog.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the schema.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example", // String | OData filter. Optional.
  'top': 56, // Number | The number of items to return. Optional.
  'skip': 56, // Number | The number of items to skip over before returning elements. Optional.
  'select': "select_example", // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
  'orderby': "orderby_example", // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
  'count': true // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
};
apiInstance.catalogListSchemas(databaseName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the schema. | 
 **apiVersion** | **String**| Client Api Version. | 
 **filter** | **String**| OData filter. Optional. | [optional] 
 **top** | **Number**| The number of items to return. Optional. | [optional] 
 **skip** | **Number**| The number of items to skip over before returning elements. Optional. | [optional] 
 **select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] 
 **orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] 
 **count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] 

### Return type

[**USqlSchemaList**](USqlSchemaList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogListTableFragments

> USqlTableFragmentList catalogListTableFragments(databaseName, schemaName, tableName, apiVersion, opts)



Retrieves the list of table fragments from the Data Lake Analytics catalog.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the table fragments.
let schemaName = "schemaName_example"; // String | The name of the schema containing the table fragments.
let tableName = "tableName_example"; // String | The name of the table containing the table fragments.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example", // String | OData filter. Optional.
  'top': 56, // Number | The number of items to return. Optional.
  'skip': 56, // Number | The number of items to skip over before returning elements. Optional.
  'select': "select_example", // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
  'orderby': "orderby_example", // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
  'count': true // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
};
apiInstance.catalogListTableFragments(databaseName, schemaName, tableName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the table fragments. | 
 **schemaName** | **String**| The name of the schema containing the table fragments. | 
 **tableName** | **String**| The name of the table containing the table fragments. | 
 **apiVersion** | **String**| Client Api Version. | 
 **filter** | **String**| OData filter. Optional. | [optional] 
 **top** | **Number**| The number of items to return. Optional. | [optional] 
 **skip** | **Number**| The number of items to skip over before returning elements. Optional. | [optional] 
 **select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] 
 **orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] 
 **count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] 

### Return type

[**USqlTableFragmentList**](USqlTableFragmentList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogListTablePartitions

> USqlTablePartitionList catalogListTablePartitions(databaseName, schemaName, tableName, apiVersion, opts)



Retrieves the list of table partitions from the Data Lake Analytics catalog.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the partitions.
let schemaName = "schemaName_example"; // String | The name of the schema containing the partitions.
let tableName = "tableName_example"; // String | The name of the table containing the partitions.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example", // String | OData filter. Optional.
  'top': 56, // Number | The number of items to return. Optional.
  'skip': 56, // Number | The number of items to skip over before returning elements. Optional.
  'select': "select_example", // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
  'orderby': "orderby_example", // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
  'count': true // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
};
apiInstance.catalogListTablePartitions(databaseName, schemaName, tableName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the partitions. | 
 **schemaName** | **String**| The name of the schema containing the partitions. | 
 **tableName** | **String**| The name of the table containing the partitions. | 
 **apiVersion** | **String**| Client Api Version. | 
 **filter** | **String**| OData filter. Optional. | [optional] 
 **top** | **Number**| The number of items to return. Optional. | [optional] 
 **skip** | **Number**| The number of items to skip over before returning elements. Optional. | [optional] 
 **select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] 
 **orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] 
 **count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] 

### Return type

[**USqlTablePartitionList**](USqlTablePartitionList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogListTableStatistics

> USqlTableStatisticsList catalogListTableStatistics(databaseName, schemaName, tableName, apiVersion, opts)



Retrieves the list of table statistics from the Data Lake Analytics catalog.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the statistics.
let schemaName = "schemaName_example"; // String | The name of the schema containing the statistics.
let tableName = "tableName_example"; // String | The name of the table containing the statistics.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example", // String | OData filter. Optional.
  'top': 56, // Number | The number of items to return. Optional.
  'skip': 56, // Number | The number of items to skip over before returning elements. Optional.
  'select': "select_example", // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
  'orderby': "orderby_example", // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
  'count': true // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
};
apiInstance.catalogListTableStatistics(databaseName, schemaName, tableName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the statistics. | 
 **schemaName** | **String**| The name of the schema containing the statistics. | 
 **tableName** | **String**| The name of the table containing the statistics. | 
 **apiVersion** | **String**| Client Api Version. | 
 **filter** | **String**| OData filter. Optional. | [optional] 
 **top** | **Number**| The number of items to return. Optional. | [optional] 
 **skip** | **Number**| The number of items to skip over before returning elements. Optional. | [optional] 
 **select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] 
 **orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] 
 **count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] 

### Return type

[**USqlTableStatisticsList**](USqlTableStatisticsList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogListTableStatisticsByDatabase

> USqlTableStatisticsList catalogListTableStatisticsByDatabase(databaseName, apiVersion, opts)



Retrieves the list of all statistics in a database from the Data Lake Analytics catalog.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the table statistics.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example", // String | OData filter. Optional.
  'top': 56, // Number | The number of items to return. Optional.
  'skip': 56, // Number | The number of items to skip over before returning elements. Optional.
  'select': "select_example", // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
  'orderby': "orderby_example", // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
  'count': true // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
};
apiInstance.catalogListTableStatisticsByDatabase(databaseName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the table statistics. | 
 **apiVersion** | **String**| Client Api Version. | 
 **filter** | **String**| OData filter. Optional. | [optional] 
 **top** | **Number**| The number of items to return. Optional. | [optional] 
 **skip** | **Number**| The number of items to skip over before returning elements. Optional. | [optional] 
 **select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] 
 **orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] 
 **count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] 

### Return type

[**USqlTableStatisticsList**](USqlTableStatisticsList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogListTableStatisticsByDatabaseAndSchema

> USqlTableStatisticsList catalogListTableStatisticsByDatabaseAndSchema(databaseName, schemaName, apiVersion, opts)



Retrieves the list of all table statistics within the specified schema from the Data Lake Analytics catalog.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the statistics.
let schemaName = "schemaName_example"; // String | The name of the schema containing the statistics.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example", // String | OData filter. Optional.
  'top': 56, // Number | The number of items to return. Optional.
  'skip': 56, // Number | The number of items to skip over before returning elements. Optional.
  'select': "select_example", // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
  'orderby': "orderby_example", // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
  'count': true // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
};
apiInstance.catalogListTableStatisticsByDatabaseAndSchema(databaseName, schemaName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the statistics. | 
 **schemaName** | **String**| The name of the schema containing the statistics. | 
 **apiVersion** | **String**| Client Api Version. | 
 **filter** | **String**| OData filter. Optional. | [optional] 
 **top** | **Number**| The number of items to return. Optional. | [optional] 
 **skip** | **Number**| The number of items to skip over before returning elements. Optional. | [optional] 
 **select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] 
 **orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] 
 **count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] 

### Return type

[**USqlTableStatisticsList**](USqlTableStatisticsList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogListTableTypes

> USqlTableTypeList catalogListTableTypes(databaseName, schemaName, apiVersion, opts)



Retrieves the list of table types from the Data Lake Analytics catalog.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the table types.
let schemaName = "schemaName_example"; // String | The name of the schema containing the table types.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example", // String | OData filter. Optional.
  'top': 56, // Number | The number of items to return. Optional.
  'skip': 56, // Number | The number of items to skip over before returning elements. Optional.
  'select': "select_example", // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
  'orderby': "orderby_example", // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
  'count': true // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
};
apiInstance.catalogListTableTypes(databaseName, schemaName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the table types. | 
 **schemaName** | **String**| The name of the schema containing the table types. | 
 **apiVersion** | **String**| Client Api Version. | 
 **filter** | **String**| OData filter. Optional. | [optional] 
 **top** | **Number**| The number of items to return. Optional. | [optional] 
 **skip** | **Number**| The number of items to skip over before returning elements. Optional. | [optional] 
 **select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] 
 **orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] 
 **count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] 

### Return type

[**USqlTableTypeList**](USqlTableTypeList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogListTableValuedFunctions

> USqlTableValuedFunctionList catalogListTableValuedFunctions(databaseName, schemaName, apiVersion, opts)



Retrieves the list of table valued functions from the Data Lake Analytics catalog.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the table valued functions.
let schemaName = "schemaName_example"; // String | The name of the schema containing the table valued functions.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example", // String | OData filter. Optional.
  'top': 56, // Number | The number of items to return. Optional.
  'skip': 56, // Number | The number of items to skip over before returning elements. Optional.
  'select': "select_example", // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
  'orderby': "orderby_example", // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
  'count': true // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
};
apiInstance.catalogListTableValuedFunctions(databaseName, schemaName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the table valued functions. | 
 **schemaName** | **String**| The name of the schema containing the table valued functions. | 
 **apiVersion** | **String**| Client Api Version. | 
 **filter** | **String**| OData filter. Optional. | [optional] 
 **top** | **Number**| The number of items to return. Optional. | [optional] 
 **skip** | **Number**| The number of items to skip over before returning elements. Optional. | [optional] 
 **select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] 
 **orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] 
 **count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] 

### Return type

[**USqlTableValuedFunctionList**](USqlTableValuedFunctionList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogListTableValuedFunctionsByDatabase

> USqlTableValuedFunctionList catalogListTableValuedFunctionsByDatabase(databaseName, apiVersion, opts)



Retrieves the list of all table valued functions in a database from the Data Lake Analytics catalog.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the table valued functions.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example", // String | OData filter. Optional.
  'top': 56, // Number | The number of items to return. Optional.
  'skip': 56, // Number | The number of items to skip over before returning elements. Optional.
  'select': "select_example", // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
  'orderby': "orderby_example", // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
  'count': true // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
};
apiInstance.catalogListTableValuedFunctionsByDatabase(databaseName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the table valued functions. | 
 **apiVersion** | **String**| Client Api Version. | 
 **filter** | **String**| OData filter. Optional. | [optional] 
 **top** | **Number**| The number of items to return. Optional. | [optional] 
 **skip** | **Number**| The number of items to skip over before returning elements. Optional. | [optional] 
 **select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] 
 **orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] 
 **count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] 

### Return type

[**USqlTableValuedFunctionList**](USqlTableValuedFunctionList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogListTables

> USqlTableList catalogListTables(databaseName, schemaName, apiVersion, opts)



Retrieves the list of tables from the Data Lake Analytics catalog.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the tables.
let schemaName = "schemaName_example"; // String | The name of the schema containing the tables.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example", // String | OData filter. Optional.
  'top': 56, // Number | The number of items to return. Optional.
  'skip': 56, // Number | The number of items to skip over before returning elements. Optional.
  'select': "select_example", // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
  'orderby': "orderby_example", // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
  'count': true, // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
  'basic': false // Boolean | The basic switch indicates what level of information to return when listing tables. When basic is true, only database_name, schema_name, table_name and version are returned for each table, otherwise all table metadata is returned. By default, it is false. Optional.
};
apiInstance.catalogListTables(databaseName, schemaName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the tables. | 
 **schemaName** | **String**| The name of the schema containing the tables. | 
 **apiVersion** | **String**| Client Api Version. | 
 **filter** | **String**| OData filter. Optional. | [optional] 
 **top** | **Number**| The number of items to return. Optional. | [optional] 
 **skip** | **Number**| The number of items to skip over before returning elements. Optional. | [optional] 
 **select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] 
 **orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] 
 **count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] 
 **basic** | **Boolean**| The basic switch indicates what level of information to return when listing tables. When basic is true, only database_name, schema_name, table_name and version are returned for each table, otherwise all table metadata is returned. By default, it is false. Optional. | [optional] [default to false]

### Return type

[**USqlTableList**](USqlTableList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogListTablesByDatabase

> USqlTableList catalogListTablesByDatabase(databaseName, apiVersion, opts)



Retrieves the list of all tables in a database from the Data Lake Analytics catalog.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the tables.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example", // String | OData filter. Optional.
  'top': 56, // Number | The number of items to return. Optional.
  'skip': 56, // Number | The number of items to skip over before returning elements. Optional.
  'select': "select_example", // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
  'orderby': "orderby_example", // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
  'count': true, // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
  'basic': false // Boolean | The basic switch indicates what level of information to return when listing tables. When basic is true, only database_name, schema_name, table_name and version are returned for each table, otherwise all table metadata is returned. By default, it is false
};
apiInstance.catalogListTablesByDatabase(databaseName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the tables. | 
 **apiVersion** | **String**| Client Api Version. | 
 **filter** | **String**| OData filter. Optional. | [optional] 
 **top** | **Number**| The number of items to return. Optional. | [optional] 
 **skip** | **Number**| The number of items to skip over before returning elements. Optional. | [optional] 
 **select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] 
 **orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] 
 **count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] 
 **basic** | **Boolean**| The basic switch indicates what level of information to return when listing tables. When basic is true, only database_name, schema_name, table_name and version are returned for each table, otherwise all table metadata is returned. By default, it is false | [optional] [default to false]

### Return type

[**USqlTableList**](USqlTableList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogListTypes

> USqlTypeList catalogListTypes(databaseName, schemaName, apiVersion, opts)



Retrieves the list of types within the specified database and schema from the Data Lake Analytics catalog.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the types.
let schemaName = "schemaName_example"; // String | The name of the schema containing the types.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example", // String | OData filter. Optional.
  'top': 56, // Number | The number of items to return. Optional.
  'skip': 56, // Number | The number of items to skip over before returning elements. Optional.
  'select': "select_example", // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
  'orderby': "orderby_example", // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
  'count': true // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
};
apiInstance.catalogListTypes(databaseName, schemaName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the types. | 
 **schemaName** | **String**| The name of the schema containing the types. | 
 **apiVersion** | **String**| Client Api Version. | 
 **filter** | **String**| OData filter. Optional. | [optional] 
 **top** | **Number**| The number of items to return. Optional. | [optional] 
 **skip** | **Number**| The number of items to skip over before returning elements. Optional. | [optional] 
 **select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] 
 **orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] 
 **count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] 

### Return type

[**USqlTypeList**](USqlTypeList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogListViews

> USqlViewList catalogListViews(databaseName, schemaName, apiVersion, opts)



Retrieves the list of views from the Data Lake Analytics catalog.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the views.
let schemaName = "schemaName_example"; // String | The name of the schema containing the views.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example", // String | OData filter. Optional.
  'top': 56, // Number | The number of items to return. Optional.
  'skip': 56, // Number | The number of items to skip over before returning elements. Optional.
  'select': "select_example", // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
  'orderby': "orderby_example", // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
  'count': true // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
};
apiInstance.catalogListViews(databaseName, schemaName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the views. | 
 **schemaName** | **String**| The name of the schema containing the views. | 
 **apiVersion** | **String**| Client Api Version. | 
 **filter** | **String**| OData filter. Optional. | [optional] 
 **top** | **Number**| The number of items to return. Optional. | [optional] 
 **skip** | **Number**| The number of items to skip over before returning elements. Optional. | [optional] 
 **select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] 
 **orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] 
 **count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] 

### Return type

[**USqlViewList**](USqlViewList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogListViewsByDatabase

> USqlViewList catalogListViewsByDatabase(databaseName, apiVersion, opts)



Retrieves the list of all views in a database from the Data Lake Analytics catalog.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the views.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example", // String | OData filter. Optional.
  'top': 56, // Number | The number of items to return. Optional.
  'skip': 56, // Number | The number of items to skip over before returning elements. Optional.
  'select': "select_example", // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
  'orderby': "orderby_example", // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
  'count': true // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
};
apiInstance.catalogListViewsByDatabase(databaseName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the views. | 
 **apiVersion** | **String**| Client Api Version. | 
 **filter** | **String**| OData filter. Optional. | [optional] 
 **top** | **Number**| The number of items to return. Optional. | [optional] 
 **skip** | **Number**| The number of items to skip over before returning elements. Optional. | [optional] 
 **select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] 
 **orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] 
 **count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] 

### Return type

[**USqlViewList**](USqlViewList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogPreviewTable

> USqlTablePreview catalogPreviewTable(databaseName, schemaName, tableName, apiVersion, opts)



Retrieves a preview set of rows in given table.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the table.
let schemaName = "schemaName_example"; // String | The name of the schema containing the table.
let tableName = "tableName_example"; // String | The name of the table.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'maxRows': 789, // Number | The maximum number of preview rows to be retrieved. Rows returned may be less than or equal to this number depending on row sizes and number of rows in the table.
  'maxColumns': 789 // Number | The maximum number of columns to be retrieved.
};
apiInstance.catalogPreviewTable(databaseName, schemaName, tableName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the table. | 
 **schemaName** | **String**| The name of the schema containing the table. | 
 **tableName** | **String**| The name of the table. | 
 **apiVersion** | **String**| Client Api Version. | 
 **maxRows** | **Number**| The maximum number of preview rows to be retrieved. Rows returned may be less than or equal to this number depending on row sizes and number of rows in the table. | [optional] 
 **maxColumns** | **Number**| The maximum number of columns to be retrieved. | [optional] 

### Return type

[**USqlTablePreview**](USqlTablePreview.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogPreviewTablePartition

> USqlTablePreview catalogPreviewTablePartition(databaseName, schemaName, tableName, partitionName, apiVersion, opts)



Retrieves a preview set of rows in given partition.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the partition.
let schemaName = "schemaName_example"; // String | The name of the schema containing the partition.
let tableName = "tableName_example"; // String | The name of the table containing the partition.
let partitionName = "partitionName_example"; // String | The name of the table partition.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'maxRows': 789, // Number | The maximum number of preview rows to be retrieved.Rows returned may be less than or equal to this number depending on row sizes and number of rows in the partition.
  'maxColumns': 789 // Number | The maximum number of columns to be retrieved.
};
apiInstance.catalogPreviewTablePartition(databaseName, schemaName, tableName, partitionName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the partition. | 
 **schemaName** | **String**| The name of the schema containing the partition. | 
 **tableName** | **String**| The name of the table containing the partition. | 
 **partitionName** | **String**| The name of the table partition. | 
 **apiVersion** | **String**| Client Api Version. | 
 **maxRows** | **Number**| The maximum number of preview rows to be retrieved.Rows returned may be less than or equal to this number depending on row sizes and number of rows in the partition. | [optional] 
 **maxColumns** | **Number**| The maximum number of columns to be retrieved. | [optional] 

### Return type

[**USqlTablePreview**](USqlTablePreview.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogUpdateCredential

> catalogUpdateCredential(databaseName, credentialName, apiVersion, parameters)



Modifies the specified credential for use with external data sources in the specified database

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the credential.
let credentialName = "credentialName_example"; // String | The name of the credential.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let parameters = new DataLakeAnalyticsCatalogManagementClient.DataLakeAnalyticsCatalogCredentialUpdateParameters(); // DataLakeAnalyticsCatalogCredentialUpdateParameters | The parameters required to modify the credential (name and password)
apiInstance.catalogUpdateCredential(databaseName, credentialName, apiVersion, parameters, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the credential. | 
 **credentialName** | **String**| The name of the credential. | 
 **apiVersion** | **String**| Client Api Version. | 
 **parameters** | [**DataLakeAnalyticsCatalogCredentialUpdateParameters**](DataLakeAnalyticsCatalogCredentialUpdateParameters.md)| The parameters required to modify the credential (name and password) | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## catalogUpdateSecret

> catalogUpdateSecret(databaseName, secretName, apiVersion, parameters)



Modifies the specified secret for use with external data sources in the specified database. This is deprecated and will be removed in the next release. Please use UpdateCredential instead.

### Example

```javascript
import DataLakeAnalyticsCatalogManagementClient from 'data_lake_analytics_catalog_management_client';

let apiInstance = new DataLakeAnalyticsCatalogManagementClient.CatalogApi();
let databaseName = "databaseName_example"; // String | The name of the database containing the secret.
let secretName = "secretName_example"; // String | The name of the secret.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let parameters = new DataLakeAnalyticsCatalogManagementClient.DataLakeAnalyticsCatalogSecretCreateOrUpdateParameters(); // DataLakeAnalyticsCatalogSecretCreateOrUpdateParameters | The parameters required to modify the secret (name and password)
apiInstance.catalogUpdateSecret(databaseName, secretName, apiVersion, parameters, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databaseName** | **String**| The name of the database containing the secret. | 
 **secretName** | **String**| The name of the secret. | 
 **apiVersion** | **String**| Client Api Version. | 
 **parameters** | [**DataLakeAnalyticsCatalogSecretCreateOrUpdateParameters**](DataLakeAnalyticsCatalogSecretCreateOrUpdateParameters.md)| The parameters required to modify the secret (name and password) | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

