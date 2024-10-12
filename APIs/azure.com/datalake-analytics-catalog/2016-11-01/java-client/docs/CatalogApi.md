# CatalogApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogCreateCredential**](CatalogApi.md#catalogCreateCredential) | **PUT** /catalog/usql/databases/{databaseName}/credentials/{credentialName} |  |
| [**catalogCreateSecret**](CatalogApi.md#catalogCreateSecret) | **PUT** /catalog/usql/databases/{databaseName}/secrets/{secretName} |  |
| [**catalogDeleteAllSecrets**](CatalogApi.md#catalogDeleteAllSecrets) | **DELETE** /catalog/usql/databases/{databaseName}/secrets |  |
| [**catalogDeleteCredential**](CatalogApi.md#catalogDeleteCredential) | **POST** /catalog/usql/databases/{databaseName}/credentials/{credentialName} |  |
| [**catalogDeleteSecret**](CatalogApi.md#catalogDeleteSecret) | **DELETE** /catalog/usql/databases/{databaseName}/secrets/{secretName} |  |
| [**catalogGetAssembly**](CatalogApi.md#catalogGetAssembly) | **GET** /catalog/usql/databases/{databaseName}/assemblies/{assemblyName} |  |
| [**catalogGetCredential**](CatalogApi.md#catalogGetCredential) | **GET** /catalog/usql/databases/{databaseName}/credentials/{credentialName} |  |
| [**catalogGetDatabase**](CatalogApi.md#catalogGetDatabase) | **GET** /catalog/usql/databases/{databaseName} |  |
| [**catalogGetExternalDataSource**](CatalogApi.md#catalogGetExternalDataSource) | **GET** /catalog/usql/databases/{databaseName}/externaldatasources/{externalDataSourceName} |  |
| [**catalogGetPackage**](CatalogApi.md#catalogGetPackage) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/packages/{packageName} |  |
| [**catalogGetProcedure**](CatalogApi.md#catalogGetProcedure) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/procedures/{procedureName} |  |
| [**catalogGetSchema**](CatalogApi.md#catalogGetSchema) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName} |  |
| [**catalogGetSecret**](CatalogApi.md#catalogGetSecret) | **GET** /catalog/usql/databases/{databaseName}/secrets/{secretName} |  |
| [**catalogGetTable**](CatalogApi.md#catalogGetTable) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/tables/{tableName} |  |
| [**catalogGetTablePartition**](CatalogApi.md#catalogGetTablePartition) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/tables/{tableName}/partitions/{partitionName} |  |
| [**catalogGetTableStatistic**](CatalogApi.md#catalogGetTableStatistic) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/tables/{tableName}/statistics/{statisticsName} |  |
| [**catalogGetTableType**](CatalogApi.md#catalogGetTableType) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/tabletypes/{tableTypeName} |  |
| [**catalogGetTableValuedFunction**](CatalogApi.md#catalogGetTableValuedFunction) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/tablevaluedfunctions/{tableValuedFunctionName} |  |
| [**catalogGetView**](CatalogApi.md#catalogGetView) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/views/{viewName} |  |
| [**catalogListAcls**](CatalogApi.md#catalogListAcls) | **GET** /catalog/usql/acl |  |
| [**catalogListAclsByDatabase**](CatalogApi.md#catalogListAclsByDatabase) | **GET** /catalog/usql/databases/{databaseName}/acl |  |
| [**catalogListAssemblies**](CatalogApi.md#catalogListAssemblies) | **GET** /catalog/usql/databases/{databaseName}/assemblies |  |
| [**catalogListCredentials**](CatalogApi.md#catalogListCredentials) | **GET** /catalog/usql/databases/{databaseName}/credentials |  |
| [**catalogListDatabases**](CatalogApi.md#catalogListDatabases) | **GET** /catalog/usql/databases |  |
| [**catalogListExternalDataSources**](CatalogApi.md#catalogListExternalDataSources) | **GET** /catalog/usql/databases/{databaseName}/externaldatasources |  |
| [**catalogListPackages**](CatalogApi.md#catalogListPackages) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/packages |  |
| [**catalogListProcedures**](CatalogApi.md#catalogListProcedures) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/procedures |  |
| [**catalogListSchemas**](CatalogApi.md#catalogListSchemas) | **GET** /catalog/usql/databases/{databaseName}/schemas |  |
| [**catalogListTableFragments**](CatalogApi.md#catalogListTableFragments) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/tables/{tableName}/tablefragments |  |
| [**catalogListTablePartitions**](CatalogApi.md#catalogListTablePartitions) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/tables/{tableName}/partitions |  |
| [**catalogListTableStatistics**](CatalogApi.md#catalogListTableStatistics) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/tables/{tableName}/statistics |  |
| [**catalogListTableStatisticsByDatabase**](CatalogApi.md#catalogListTableStatisticsByDatabase) | **GET** /catalog/usql/databases/{databaseName}/statistics |  |
| [**catalogListTableStatisticsByDatabaseAndSchema**](CatalogApi.md#catalogListTableStatisticsByDatabaseAndSchema) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/statistics |  |
| [**catalogListTableTypes**](CatalogApi.md#catalogListTableTypes) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/tabletypes |  |
| [**catalogListTableValuedFunctions**](CatalogApi.md#catalogListTableValuedFunctions) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/tablevaluedfunctions |  |
| [**catalogListTableValuedFunctionsByDatabase**](CatalogApi.md#catalogListTableValuedFunctionsByDatabase) | **GET** /catalog/usql/databases/{databaseName}/tablevaluedfunctions |  |
| [**catalogListTables**](CatalogApi.md#catalogListTables) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/tables |  |
| [**catalogListTablesByDatabase**](CatalogApi.md#catalogListTablesByDatabase) | **GET** /catalog/usql/databases/{databaseName}/tables |  |
| [**catalogListTypes**](CatalogApi.md#catalogListTypes) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/types |  |
| [**catalogListViews**](CatalogApi.md#catalogListViews) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/views |  |
| [**catalogListViewsByDatabase**](CatalogApi.md#catalogListViewsByDatabase) | **GET** /catalog/usql/databases/{databaseName}/views |  |
| [**catalogPreviewTable**](CatalogApi.md#catalogPreviewTable) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/tables/{tableName}/previewrows |  |
| [**catalogPreviewTablePartition**](CatalogApi.md#catalogPreviewTablePartition) | **GET** /catalog/usql/databases/{databaseName}/schemas/{schemaName}/tables/{tableName}/partitions/{partitionName}/previewrows |  |
| [**catalogUpdateCredential**](CatalogApi.md#catalogUpdateCredential) | **PATCH** /catalog/usql/databases/{databaseName}/credentials/{credentialName} |  |
| [**catalogUpdateSecret**](CatalogApi.md#catalogUpdateSecret) | **PATCH** /catalog/usql/databases/{databaseName}/secrets/{secretName} |  |


<a id="catalogCreateCredential"></a>
# **catalogCreateCredential**
> catalogCreateCredential(databaseName, credentialName, apiVersion, parameters)



Creates the specified credential for use with external data sources in the specified database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database in which to create the credential. Note: This is NOT an external database name, but the name of an existing U-SQL database that should contain the new credential object.
    String credentialName = "credentialName_example"; // String | The name of the credential.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    DataLakeAnalyticsCatalogCredentialCreateParameters parameters = new DataLakeAnalyticsCatalogCredentialCreateParameters(); // DataLakeAnalyticsCatalogCredentialCreateParameters | The parameters required to create the credential (name and password)
    try {
      apiInstance.catalogCreateCredential(databaseName, credentialName, apiVersion, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogCreateCredential");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database in which to create the credential. Note: This is NOT an external database name, but the name of an existing U-SQL database that should contain the new credential object. | |
| **credentialName** | **String**| The name of the credential. | |
| **apiVersion** | **String**| Client Api Version. | |
| **parameters** | [**DataLakeAnalyticsCatalogCredentialCreateParameters**](DataLakeAnalyticsCatalogCredentialCreateParameters.md)| The parameters required to create the credential (name and password) | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully created the credential within the specified database. |  -  |

<a id="catalogCreateSecret"></a>
# **catalogCreateSecret**
> catalogCreateSecret(databaseName, secretName, apiVersion, parameters)



Creates the specified secret for use with external data sources in the specified database. This is deprecated and will be removed in the next release. Please use CreateCredential instead.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database in which to create the secret.
    String secretName = "secretName_example"; // String | The name of the secret.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    DataLakeAnalyticsCatalogSecretCreateOrUpdateParameters parameters = new DataLakeAnalyticsCatalogSecretCreateOrUpdateParameters(); // DataLakeAnalyticsCatalogSecretCreateOrUpdateParameters | The parameters required to create the secret (name and password)
    try {
      apiInstance.catalogCreateSecret(databaseName, secretName, apiVersion, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogCreateSecret");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database in which to create the secret. | |
| **secretName** | **String**| The name of the secret. | |
| **apiVersion** | **String**| Client Api Version. | |
| **parameters** | [**DataLakeAnalyticsCatalogSecretCreateOrUpdateParameters**](DataLakeAnalyticsCatalogSecretCreateOrUpdateParameters.md)| The parameters required to create the secret (name and password) | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully created the specified secret in the specified database. |  -  |

<a id="catalogDeleteAllSecrets"></a>
# **catalogDeleteAllSecrets**
> catalogDeleteAllSecrets(databaseName, apiVersion)



Deletes all secrets in the specified database. This is deprecated and will be removed in the next release. In the future, please only drop individual credentials using DeleteCredential

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the secret.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      apiInstance.catalogDeleteAllSecrets(databaseName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogDeleteAllSecrets");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the secret. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully deleted all secrets from the specified database. |  -  |

<a id="catalogDeleteCredential"></a>
# **catalogDeleteCredential**
> catalogDeleteCredential(databaseName, credentialName, apiVersion, cascade, parameters)



Deletes the specified credential in the specified database

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the credential.
    String credentialName = "credentialName_example"; // String | The name of the credential to delete
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    Boolean cascade = false; // Boolean | Indicates if the delete should be a cascading delete (which deletes all resources dependent on the credential as well as the credential) or not. If false will fail if there are any resources relying on the credential.
    DataLakeAnalyticsCatalogCredentialDeleteParameters parameters = new DataLakeAnalyticsCatalogCredentialDeleteParameters(); // DataLakeAnalyticsCatalogCredentialDeleteParameters | The parameters to delete a credential if the current user is not the account owner.
    try {
      apiInstance.catalogDeleteCredential(databaseName, credentialName, apiVersion, cascade, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogDeleteCredential");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the credential. | |
| **credentialName** | **String**| The name of the credential to delete | |
| **apiVersion** | **String**| Client Api Version. | |
| **cascade** | **Boolean**| Indicates if the delete should be a cascading delete (which deletes all resources dependent on the credential as well as the credential) or not. If false will fail if there are any resources relying on the credential. | [optional] [default to false] |
| **parameters** | [**DataLakeAnalyticsCatalogCredentialDeleteParameters**](DataLakeAnalyticsCatalogCredentialDeleteParameters.md)| The parameters to delete a credential if the current user is not the account owner. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully deleted the specified credential from the specified database. |  -  |

<a id="catalogDeleteSecret"></a>
# **catalogDeleteSecret**
> catalogDeleteSecret(databaseName, secretName, apiVersion)



Deletes the specified secret in the specified database. This is deprecated and will be removed in the next release. Please use DeleteCredential instead.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the secret.
    String secretName = "secretName_example"; // String | The name of the secret to delete
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      apiInstance.catalogDeleteSecret(databaseName, secretName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogDeleteSecret");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the secret. | |
| **secretName** | **String**| The name of the secret to delete | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully deleted the specified secret from the specified database. |  -  |

<a id="catalogGetAssembly"></a>
# **catalogGetAssembly**
> USqlAssembly catalogGetAssembly(databaseName, assemblyName, apiVersion)



Retrieves the specified assembly from the Data Lake Analytics catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the assembly.
    String assemblyName = "assemblyName_example"; // String | The name of the assembly.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      USqlAssembly result = apiInstance.catalogGetAssembly(databaseName, assemblyName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogGetAssembly");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the assembly. | |
| **assemblyName** | **String**| The name of the assembly. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**USqlAssembly**](USqlAssembly.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the details of the specified assembly in the specified database. |  -  |

<a id="catalogGetCredential"></a>
# **catalogGetCredential**
> USqlCredential catalogGetCredential(databaseName, credentialName, apiVersion)



Retrieves the specified credential from the Data Lake Analytics catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the schema.
    String credentialName = "credentialName_example"; // String | The name of the credential.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      USqlCredential result = apiInstance.catalogGetCredential(databaseName, credentialName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogGetCredential");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the schema. | |
| **credentialName** | **String**| The name of the credential. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**USqlCredential**](USqlCredential.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the specified credential (name only) from the specified database. |  -  |

<a id="catalogGetDatabase"></a>
# **catalogGetDatabase**
> USqlDatabase catalogGetDatabase(databaseName, apiVersion)



Retrieves the specified database from the Data Lake Analytics catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      USqlDatabase result = apiInstance.catalogGetDatabase(databaseName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogGetDatabase");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**USqlDatabase**](USqlDatabase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the details of the specified database. |  -  |

<a id="catalogGetExternalDataSource"></a>
# **catalogGetExternalDataSource**
> USqlExternalDataSource catalogGetExternalDataSource(databaseName, externalDataSourceName, apiVersion)



Retrieves the specified external data source from the Data Lake Analytics catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the external data source.
    String externalDataSourceName = "externalDataSourceName_example"; // String | The name of the external data source.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      USqlExternalDataSource result = apiInstance.catalogGetExternalDataSource(databaseName, externalDataSourceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogGetExternalDataSource");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the external data source. | |
| **externalDataSourceName** | **String**| The name of the external data source. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**USqlExternalDataSource**](USqlExternalDataSource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved details of the specified external data source in the specified database. |  -  |

<a id="catalogGetPackage"></a>
# **catalogGetPackage**
> USqlPackage catalogGetPackage(databaseName, schemaName, packageName, apiVersion)



Retrieves the specified package from the Data Lake Analytics catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the package.
    String schemaName = "schemaName_example"; // String | The name of the schema containing the package.
    String packageName = "packageName_example"; // String | The name of the package.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      USqlPackage result = apiInstance.catalogGetPackage(databaseName, schemaName, packageName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogGetPackage");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the package. | |
| **schemaName** | **String**| The name of the schema containing the package. | |
| **packageName** | **String**| The name of the package. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**USqlPackage**](USqlPackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the specified package from the underlying database and schema combination |  -  |

<a id="catalogGetProcedure"></a>
# **catalogGetProcedure**
> USqlProcedure catalogGetProcedure(databaseName, schemaName, procedureName, apiVersion)



Retrieves the specified procedure from the Data Lake Analytics catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the procedure.
    String schemaName = "schemaName_example"; // String | The name of the schema containing the procedure.
    String procedureName = "procedureName_example"; // String | The name of the procedure.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      USqlProcedure result = apiInstance.catalogGetProcedure(databaseName, schemaName, procedureName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogGetProcedure");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the procedure. | |
| **schemaName** | **String**| The name of the schema containing the procedure. | |
| **procedureName** | **String**| The name of the procedure. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**USqlProcedure**](USqlProcedure.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the specified procedure from the underlying database and schema combination. |  -  |

<a id="catalogGetSchema"></a>
# **catalogGetSchema**
> USqlSchema catalogGetSchema(databaseName, schemaName, apiVersion)



Retrieves the specified schema from the Data Lake Analytics catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the schema.
    String schemaName = "schemaName_example"; // String | The name of the schema.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      USqlSchema result = apiInstance.catalogGetSchema(databaseName, schemaName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogGetSchema");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the schema. | |
| **schemaName** | **String**| The name of the schema. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**USqlSchema**](USqlSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the details of the specified schema in the specified database. |  -  |

<a id="catalogGetSecret"></a>
# **catalogGetSecret**
> USqlSecret catalogGetSecret(databaseName, secretName, apiVersion)



Gets the specified secret in the specified database. This is deprecated and will be removed in the next release. Please use GetCredential instead.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the secret.
    String secretName = "secretName_example"; // String | The name of the secret to get
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      USqlSecret result = apiInstance.catalogGetSecret(databaseName, secretName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogGetSecret");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the secret. | |
| **secretName** | **String**| The name of the secret to get | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**USqlSecret**](USqlSecret.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved details of the specified secret in the specified database. |  -  |

<a id="catalogGetTable"></a>
# **catalogGetTable**
> USqlTable catalogGetTable(databaseName, schemaName, tableName, apiVersion)



Retrieves the specified table from the Data Lake Analytics catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the table.
    String schemaName = "schemaName_example"; // String | The name of the schema containing the table.
    String tableName = "tableName_example"; // String | The name of the table.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      USqlTable result = apiInstance.catalogGetTable(databaseName, schemaName, tableName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogGetTable");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the table. | |
| **schemaName** | **String**| The name of the schema containing the table. | |
| **tableName** | **String**| The name of the table. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**USqlTable**](USqlTable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the specified table from the underlying database and schema combination |  -  |

<a id="catalogGetTablePartition"></a>
# **catalogGetTablePartition**
> USqlTablePartition catalogGetTablePartition(databaseName, schemaName, tableName, partitionName, apiVersion)



Retrieves the specified table partition from the Data Lake Analytics catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the partition.
    String schemaName = "schemaName_example"; // String | The name of the schema containing the partition.
    String tableName = "tableName_example"; // String | The name of the table containing the partition.
    String partitionName = "partitionName_example"; // String | The name of the table partition.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      USqlTablePartition result = apiInstance.catalogGetTablePartition(databaseName, schemaName, tableName, partitionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogGetTablePartition");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the partition. | |
| **schemaName** | **String**| The name of the schema containing the partition. | |
| **tableName** | **String**| The name of the table containing the partition. | |
| **partitionName** | **String**| The name of the table partition. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**USqlTablePartition**](USqlTablePartition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the details of the specified table partition in the specified database, schema, and table. |  -  |

<a id="catalogGetTableStatistic"></a>
# **catalogGetTableStatistic**
> USqlTableStatistics catalogGetTableStatistic(databaseName, schemaName, tableName, statisticsName, apiVersion)



Retrieves the specified table statistics from the Data Lake Analytics catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the statistics.
    String schemaName = "schemaName_example"; // String | The name of the schema containing the statistics.
    String tableName = "tableName_example"; // String | The name of the table containing the statistics.
    String statisticsName = "statisticsName_example"; // String | The name of the table statistics.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      USqlTableStatistics result = apiInstance.catalogGetTableStatistic(databaseName, schemaName, tableName, statisticsName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogGetTableStatistic");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the statistics. | |
| **schemaName** | **String**| The name of the schema containing the statistics. | |
| **tableName** | **String**| The name of the table containing the statistics. | |
| **statisticsName** | **String**| The name of the table statistics. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**USqlTableStatistics**](USqlTableStatistics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the details of the specified table statistics in the specified database and schema. |  -  |

<a id="catalogGetTableType"></a>
# **catalogGetTableType**
> USqlTableType catalogGetTableType(databaseName, schemaName, tableTypeName, apiVersion)



Retrieves the specified table type from the Data Lake Analytics catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the table type.
    String schemaName = "schemaName_example"; // String | The name of the schema containing the table type.
    String tableTypeName = "tableTypeName_example"; // String | The name of the table type to retrieve.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      USqlTableType result = apiInstance.catalogGetTableType(databaseName, schemaName, tableTypeName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogGetTableType");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the table type. | |
| **schemaName** | **String**| The name of the schema containing the table type. | |
| **tableTypeName** | **String**| The name of the table type to retrieve. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**USqlTableType**](USqlTableType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the specified table type from the underlying database and schema combination |  -  |

<a id="catalogGetTableValuedFunction"></a>
# **catalogGetTableValuedFunction**
> USqlTableValuedFunction catalogGetTableValuedFunction(databaseName, schemaName, tableValuedFunctionName, apiVersion)



Retrieves the specified table valued function from the Data Lake Analytics catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the table valued function.
    String schemaName = "schemaName_example"; // String | The name of the schema containing the table valued function.
    String tableValuedFunctionName = "tableValuedFunctionName_example"; // String | The name of the tableValuedFunction.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      USqlTableValuedFunction result = apiInstance.catalogGetTableValuedFunction(databaseName, schemaName, tableValuedFunctionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogGetTableValuedFunction");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the table valued function. | |
| **schemaName** | **String**| The name of the schema containing the table valued function. | |
| **tableValuedFunctionName** | **String**| The name of the tableValuedFunction. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**USqlTableValuedFunction**](USqlTableValuedFunction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the details of the specified table valued function in the specified database and schema. |  -  |

<a id="catalogGetView"></a>
# **catalogGetView**
> USqlView catalogGetView(databaseName, schemaName, viewName, apiVersion)



Retrieves the specified view from the Data Lake Analytics catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the view.
    String schemaName = "schemaName_example"; // String | The name of the schema containing the view.
    String viewName = "viewName_example"; // String | The name of the view.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      USqlView result = apiInstance.catalogGetView(databaseName, schemaName, viewName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogGetView");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the view. | |
| **schemaName** | **String**| The name of the schema containing the view. | |
| **viewName** | **String**| The name of the view. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**USqlView**](USqlView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the specified view from the underlying database and schema combination |  -  |

<a id="catalogListAcls"></a>
# **catalogListAcls**
> AclList catalogListAcls(apiVersion, $filter, $top, $skip, $select, $orderby, $count)



Retrieves the list of access control list (ACL) entries for the Data Lake Analytics catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | OData filter. Optional.
    Integer $top = 56; // Integer | The number of items to return. Optional.
    Integer $skip = 56; // Integer | The number of items to skip over before returning elements. Optional.
    String $select = "$select_example"; // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
    String $orderby = "$orderby_example"; // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
    Boolean $count = true; // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
    try {
      AclList result = apiInstance.catalogListAcls(apiVersion, $filter, $top, $skip, $select, $orderby, $count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogListAcls");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **apiVersion** | **String**| Client Api Version. | |
| **$filter** | **String**| OData filter. Optional. | [optional] |
| **$top** | **Integer**| The number of items to return. Optional. | [optional] |
| **$skip** | **Integer**| The number of items to skip over before returning elements. Optional. | [optional] |
| **$select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] |
| **$orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] |
| **$count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] |

### Return type

[**AclList**](AclList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of access control list (ACL) entries for the Data Lake Analytics catalog. |  -  |

<a id="catalogListAclsByDatabase"></a>
# **catalogListAclsByDatabase**
> AclList catalogListAclsByDatabase(databaseName, apiVersion, $filter, $top, $skip, $select, $orderby, $count)



Retrieves the list of access control list (ACL) entries for the database from the Data Lake Analytics catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | OData filter. Optional.
    Integer $top = 56; // Integer | The number of items to return. Optional.
    Integer $skip = 56; // Integer | The number of items to skip over before returning elements. Optional.
    String $select = "$select_example"; // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
    String $orderby = "$orderby_example"; // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
    Boolean $count = true; // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
    try {
      AclList result = apiInstance.catalogListAclsByDatabase(databaseName, apiVersion, $filter, $top, $skip, $select, $orderby, $count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogListAclsByDatabase");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$filter** | **String**| OData filter. Optional. | [optional] |
| **$top** | **Integer**| The number of items to return. Optional. | [optional] |
| **$skip** | **Integer**| The number of items to skip over before returning elements. Optional. | [optional] |
| **$select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] |
| **$orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] |
| **$count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] |

### Return type

[**AclList**](AclList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of access control list (ACL) entries for the specified database. |  -  |

<a id="catalogListAssemblies"></a>
# **catalogListAssemblies**
> USqlAssemblyList catalogListAssemblies(databaseName, apiVersion, $filter, $top, $skip, $select, $orderby, $count)



Retrieves the list of assemblies from the Data Lake Analytics catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the assembly.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | OData filter. Optional.
    Integer $top = 56; // Integer | The number of items to return. Optional.
    Integer $skip = 56; // Integer | The number of items to skip over before returning elements. Optional.
    String $select = "$select_example"; // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
    String $orderby = "$orderby_example"; // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
    Boolean $count = true; // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
    try {
      USqlAssemblyList result = apiInstance.catalogListAssemblies(databaseName, apiVersion, $filter, $top, $skip, $select, $orderby, $count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogListAssemblies");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the assembly. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$filter** | **String**| OData filter. Optional. | [optional] |
| **$top** | **Integer**| The number of items to return. Optional. | [optional] |
| **$skip** | **Integer**| The number of items to skip over before returning elements. Optional. | [optional] |
| **$select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] |
| **$orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] |
| **$count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] |

### Return type

[**USqlAssemblyList**](USqlAssemblyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of assemblies in the specified database. |  -  |

<a id="catalogListCredentials"></a>
# **catalogListCredentials**
> USqlCredentialList catalogListCredentials(databaseName, apiVersion, $filter, $top, $skip, $select, $orderby, $count)



Retrieves the list of credentials from the Data Lake Analytics catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the schema.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | OData filter. Optional.
    Integer $top = 56; // Integer | The number of items to return. Optional.
    Integer $skip = 56; // Integer | The number of items to skip over before returning elements. Optional.
    String $select = "$select_example"; // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
    String $orderby = "$orderby_example"; // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
    Boolean $count = true; // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
    try {
      USqlCredentialList result = apiInstance.catalogListCredentials(databaseName, apiVersion, $filter, $top, $skip, $select, $orderby, $count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogListCredentials");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the schema. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$filter** | **String**| OData filter. Optional. | [optional] |
| **$top** | **Integer**| The number of items to return. Optional. | [optional] |
| **$skip** | **Integer**| The number of items to skip over before returning elements. Optional. | [optional] |
| **$select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] |
| **$orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] |
| **$count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] |

### Return type

[**USqlCredentialList**](USqlCredentialList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of credentials in the specified database. |  -  |

<a id="catalogListDatabases"></a>
# **catalogListDatabases**
> USqlDatabaseList catalogListDatabases(apiVersion, $filter, $top, $skip, $select, $orderby, $count)



Retrieves the list of databases from the Data Lake Analytics catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | OData filter. Optional.
    Integer $top = 56; // Integer | The number of items to return. Optional.
    Integer $skip = 56; // Integer | The number of items to skip over before returning elements. Optional.
    String $select = "$select_example"; // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
    String $orderby = "$orderby_example"; // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
    Boolean $count = true; // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
    try {
      USqlDatabaseList result = apiInstance.catalogListDatabases(apiVersion, $filter, $top, $skip, $select, $orderby, $count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogListDatabases");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **apiVersion** | **String**| Client Api Version. | |
| **$filter** | **String**| OData filter. Optional. | [optional] |
| **$top** | **Integer**| The number of items to return. Optional. | [optional] |
| **$skip** | **Integer**| The number of items to skip over before returning elements. Optional. | [optional] |
| **$select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] |
| **$orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] |
| **$count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] |

### Return type

[**USqlDatabaseList**](USqlDatabaseList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of databases. |  -  |

<a id="catalogListExternalDataSources"></a>
# **catalogListExternalDataSources**
> USqlExternalDataSourceList catalogListExternalDataSources(databaseName, apiVersion, $filter, $top, $skip, $select, $orderby, $count)



Retrieves the list of external data sources from the Data Lake Analytics catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the external data sources.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | OData filter. Optional.
    Integer $top = 56; // Integer | The number of items to return. Optional.
    Integer $skip = 56; // Integer | The number of items to skip over before returning elements. Optional.
    String $select = "$select_example"; // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
    String $orderby = "$orderby_example"; // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
    Boolean $count = true; // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
    try {
      USqlExternalDataSourceList result = apiInstance.catalogListExternalDataSources(databaseName, apiVersion, $filter, $top, $skip, $select, $orderby, $count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogListExternalDataSources");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the external data sources. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$filter** | **String**| OData filter. Optional. | [optional] |
| **$top** | **Integer**| The number of items to return. Optional. | [optional] |
| **$skip** | **Integer**| The number of items to skip over before returning elements. Optional. | [optional] |
| **$select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] |
| **$orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] |
| **$count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] |

### Return type

[**USqlExternalDataSourceList**](USqlExternalDataSourceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of external data sources in the specified database. |  -  |

<a id="catalogListPackages"></a>
# **catalogListPackages**
> USqlPackageList catalogListPackages(databaseName, schemaName, apiVersion, $filter, $top, $skip, $select, $orderby, $count)



Retrieves the list of packages from the Data Lake Analytics catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the packages.
    String schemaName = "schemaName_example"; // String | The name of the schema containing the packages.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | OData filter. Optional.
    Integer $top = 56; // Integer | The number of items to return. Optional.
    Integer $skip = 56; // Integer | The number of items to skip over before returning elements. Optional.
    String $select = "$select_example"; // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
    String $orderby = "$orderby_example"; // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
    Boolean $count = true; // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
    try {
      USqlPackageList result = apiInstance.catalogListPackages(databaseName, schemaName, apiVersion, $filter, $top, $skip, $select, $orderby, $count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogListPackages");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the packages. | |
| **schemaName** | **String**| The name of the schema containing the packages. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$filter** | **String**| OData filter. Optional. | [optional] |
| **$top** | **Integer**| The number of items to return. Optional. | [optional] |
| **$skip** | **Integer**| The number of items to skip over before returning elements. Optional. | [optional] |
| **$select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] |
| **$orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] |
| **$count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] |

### Return type

[**USqlPackageList**](USqlPackageList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of packages in the specified database and schema. |  -  |

<a id="catalogListProcedures"></a>
# **catalogListProcedures**
> USqlProcedureList catalogListProcedures(databaseName, schemaName, apiVersion, $filter, $top, $skip, $select, $orderby, $count)



Retrieves the list of procedures from the Data Lake Analytics catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the procedures.
    String schemaName = "schemaName_example"; // String | The name of the schema containing the procedures.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | OData filter. Optional.
    Integer $top = 56; // Integer | The number of items to return. Optional.
    Integer $skip = 56; // Integer | The number of items to skip over before returning elements. Optional.
    String $select = "$select_example"; // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
    String $orderby = "$orderby_example"; // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
    Boolean $count = true; // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
    try {
      USqlProcedureList result = apiInstance.catalogListProcedures(databaseName, schemaName, apiVersion, $filter, $top, $skip, $select, $orderby, $count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogListProcedures");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the procedures. | |
| **schemaName** | **String**| The name of the schema containing the procedures. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$filter** | **String**| OData filter. Optional. | [optional] |
| **$top** | **Integer**| The number of items to return. Optional. | [optional] |
| **$skip** | **Integer**| The number of items to skip over before returning elements. Optional. | [optional] |
| **$select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] |
| **$orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] |
| **$count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] |

### Return type

[**USqlProcedureList**](USqlProcedureList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of procedures in the specified database and schema. |  -  |

<a id="catalogListSchemas"></a>
# **catalogListSchemas**
> USqlSchemaList catalogListSchemas(databaseName, apiVersion, $filter, $top, $skip, $select, $orderby, $count)



Retrieves the list of schemas from the Data Lake Analytics catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the schema.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | OData filter. Optional.
    Integer $top = 56; // Integer | The number of items to return. Optional.
    Integer $skip = 56; // Integer | The number of items to skip over before returning elements. Optional.
    String $select = "$select_example"; // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
    String $orderby = "$orderby_example"; // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
    Boolean $count = true; // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
    try {
      USqlSchemaList result = apiInstance.catalogListSchemas(databaseName, apiVersion, $filter, $top, $skip, $select, $orderby, $count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogListSchemas");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the schema. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$filter** | **String**| OData filter. Optional. | [optional] |
| **$top** | **Integer**| The number of items to return. Optional. | [optional] |
| **$skip** | **Integer**| The number of items to skip over before returning elements. Optional. | [optional] |
| **$select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] |
| **$orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] |
| **$count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] |

### Return type

[**USqlSchemaList**](USqlSchemaList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of schemas in the specified database. |  -  |

<a id="catalogListTableFragments"></a>
# **catalogListTableFragments**
> USqlTableFragmentList catalogListTableFragments(databaseName, schemaName, tableName, apiVersion, $filter, $top, $skip, $select, $orderby, $count)



Retrieves the list of table fragments from the Data Lake Analytics catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the table fragments.
    String schemaName = "schemaName_example"; // String | The name of the schema containing the table fragments.
    String tableName = "tableName_example"; // String | The name of the table containing the table fragments.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | OData filter. Optional.
    Integer $top = 56; // Integer | The number of items to return. Optional.
    Integer $skip = 56; // Integer | The number of items to skip over before returning elements. Optional.
    String $select = "$select_example"; // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
    String $orderby = "$orderby_example"; // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
    Boolean $count = true; // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
    try {
      USqlTableFragmentList result = apiInstance.catalogListTableFragments(databaseName, schemaName, tableName, apiVersion, $filter, $top, $skip, $select, $orderby, $count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogListTableFragments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the table fragments. | |
| **schemaName** | **String**| The name of the schema containing the table fragments. | |
| **tableName** | **String**| The name of the table containing the table fragments. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$filter** | **String**| OData filter. Optional. | [optional] |
| **$top** | **Integer**| The number of items to return. Optional. | [optional] |
| **$skip** | **Integer**| The number of items to skip over before returning elements. Optional. | [optional] |
| **$select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] |
| **$orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] |
| **$count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] |

### Return type

[**USqlTableFragmentList**](USqlTableFragmentList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of table fragments in the specified database and schema. |  -  |

<a id="catalogListTablePartitions"></a>
# **catalogListTablePartitions**
> USqlTablePartitionList catalogListTablePartitions(databaseName, schemaName, tableName, apiVersion, $filter, $top, $skip, $select, $orderby, $count)



Retrieves the list of table partitions from the Data Lake Analytics catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the partitions.
    String schemaName = "schemaName_example"; // String | The name of the schema containing the partitions.
    String tableName = "tableName_example"; // String | The name of the table containing the partitions.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | OData filter. Optional.
    Integer $top = 56; // Integer | The number of items to return. Optional.
    Integer $skip = 56; // Integer | The number of items to skip over before returning elements. Optional.
    String $select = "$select_example"; // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
    String $orderby = "$orderby_example"; // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
    Boolean $count = true; // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
    try {
      USqlTablePartitionList result = apiInstance.catalogListTablePartitions(databaseName, schemaName, tableName, apiVersion, $filter, $top, $skip, $select, $orderby, $count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogListTablePartitions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the partitions. | |
| **schemaName** | **String**| The name of the schema containing the partitions. | |
| **tableName** | **String**| The name of the table containing the partitions. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$filter** | **String**| OData filter. Optional. | [optional] |
| **$top** | **Integer**| The number of items to return. Optional. | [optional] |
| **$skip** | **Integer**| The number of items to skip over before returning elements. Optional. | [optional] |
| **$select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] |
| **$orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] |
| **$count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] |

### Return type

[**USqlTablePartitionList**](USqlTablePartitionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of table partitions in the specified database, schema, and table. |  -  |

<a id="catalogListTableStatistics"></a>
# **catalogListTableStatistics**
> USqlTableStatisticsList catalogListTableStatistics(databaseName, schemaName, tableName, apiVersion, $filter, $top, $skip, $select, $orderby, $count)



Retrieves the list of table statistics from the Data Lake Analytics catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the statistics.
    String schemaName = "schemaName_example"; // String | The name of the schema containing the statistics.
    String tableName = "tableName_example"; // String | The name of the table containing the statistics.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | OData filter. Optional.
    Integer $top = 56; // Integer | The number of items to return. Optional.
    Integer $skip = 56; // Integer | The number of items to skip over before returning elements. Optional.
    String $select = "$select_example"; // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
    String $orderby = "$orderby_example"; // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
    Boolean $count = true; // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
    try {
      USqlTableStatisticsList result = apiInstance.catalogListTableStatistics(databaseName, schemaName, tableName, apiVersion, $filter, $top, $skip, $select, $orderby, $count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogListTableStatistics");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the statistics. | |
| **schemaName** | **String**| The name of the schema containing the statistics. | |
| **tableName** | **String**| The name of the table containing the statistics. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$filter** | **String**| OData filter. Optional. | [optional] |
| **$top** | **Integer**| The number of items to return. Optional. | [optional] |
| **$skip** | **Integer**| The number of items to skip over before returning elements. Optional. | [optional] |
| **$select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] |
| **$orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] |
| **$count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] |

### Return type

[**USqlTableStatisticsList**](USqlTableStatisticsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of table statistics in the specified database and schema. |  -  |

<a id="catalogListTableStatisticsByDatabase"></a>
# **catalogListTableStatisticsByDatabase**
> USqlTableStatisticsList catalogListTableStatisticsByDatabase(databaseName, apiVersion, $filter, $top, $skip, $select, $orderby, $count)



Retrieves the list of all statistics in a database from the Data Lake Analytics catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the table statistics.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | OData filter. Optional.
    Integer $top = 56; // Integer | The number of items to return. Optional.
    Integer $skip = 56; // Integer | The number of items to skip over before returning elements. Optional.
    String $select = "$select_example"; // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
    String $orderby = "$orderby_example"; // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
    Boolean $count = true; // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
    try {
      USqlTableStatisticsList result = apiInstance.catalogListTableStatisticsByDatabase(databaseName, apiVersion, $filter, $top, $skip, $select, $orderby, $count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogListTableStatisticsByDatabase");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the table statistics. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$filter** | **String**| OData filter. Optional. | [optional] |
| **$top** | **Integer**| The number of items to return. Optional. | [optional] |
| **$skip** | **Integer**| The number of items to skip over before returning elements. Optional. | [optional] |
| **$select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] |
| **$orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] |
| **$count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] |

### Return type

[**USqlTableStatisticsList**](USqlTableStatisticsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of all table statistics in the specified database. |  -  |

<a id="catalogListTableStatisticsByDatabaseAndSchema"></a>
# **catalogListTableStatisticsByDatabaseAndSchema**
> USqlTableStatisticsList catalogListTableStatisticsByDatabaseAndSchema(databaseName, schemaName, apiVersion, $filter, $top, $skip, $select, $orderby, $count)



Retrieves the list of all table statistics within the specified schema from the Data Lake Analytics catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the statistics.
    String schemaName = "schemaName_example"; // String | The name of the schema containing the statistics.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | OData filter. Optional.
    Integer $top = 56; // Integer | The number of items to return. Optional.
    Integer $skip = 56; // Integer | The number of items to skip over before returning elements. Optional.
    String $select = "$select_example"; // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
    String $orderby = "$orderby_example"; // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
    Boolean $count = true; // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
    try {
      USqlTableStatisticsList result = apiInstance.catalogListTableStatisticsByDatabaseAndSchema(databaseName, schemaName, apiVersion, $filter, $top, $skip, $select, $orderby, $count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogListTableStatisticsByDatabaseAndSchema");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the statistics. | |
| **schemaName** | **String**| The name of the schema containing the statistics. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$filter** | **String**| OData filter. Optional. | [optional] |
| **$top** | **Integer**| The number of items to return. Optional. | [optional] |
| **$skip** | **Integer**| The number of items to skip over before returning elements. Optional. | [optional] |
| **$select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] |
| **$orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] |
| **$count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] |

### Return type

[**USqlTableStatisticsList**](USqlTableStatisticsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of all table statistics in the specified database and schema. |  -  |

<a id="catalogListTableTypes"></a>
# **catalogListTableTypes**
> USqlTableTypeList catalogListTableTypes(databaseName, schemaName, apiVersion, $filter, $top, $skip, $select, $orderby, $count)



Retrieves the list of table types from the Data Lake Analytics catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the table types.
    String schemaName = "schemaName_example"; // String | The name of the schema containing the table types.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | OData filter. Optional.
    Integer $top = 56; // Integer | The number of items to return. Optional.
    Integer $skip = 56; // Integer | The number of items to skip over before returning elements. Optional.
    String $select = "$select_example"; // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
    String $orderby = "$orderby_example"; // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
    Boolean $count = true; // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
    try {
      USqlTableTypeList result = apiInstance.catalogListTableTypes(databaseName, schemaName, apiVersion, $filter, $top, $skip, $select, $orderby, $count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogListTableTypes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the table types. | |
| **schemaName** | **String**| The name of the schema containing the table types. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$filter** | **String**| OData filter. Optional. | [optional] |
| **$top** | **Integer**| The number of items to return. Optional. | [optional] |
| **$skip** | **Integer**| The number of items to skip over before returning elements. Optional. | [optional] |
| **$select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] |
| **$orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] |
| **$count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] |

### Return type

[**USqlTableTypeList**](USqlTableTypeList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of table types in the specified database and schema. |  -  |

<a id="catalogListTableValuedFunctions"></a>
# **catalogListTableValuedFunctions**
> USqlTableValuedFunctionList catalogListTableValuedFunctions(databaseName, schemaName, apiVersion, $filter, $top, $skip, $select, $orderby, $count)



Retrieves the list of table valued functions from the Data Lake Analytics catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the table valued functions.
    String schemaName = "schemaName_example"; // String | The name of the schema containing the table valued functions.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | OData filter. Optional.
    Integer $top = 56; // Integer | The number of items to return. Optional.
    Integer $skip = 56; // Integer | The number of items to skip over before returning elements. Optional.
    String $select = "$select_example"; // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
    String $orderby = "$orderby_example"; // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
    Boolean $count = true; // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
    try {
      USqlTableValuedFunctionList result = apiInstance.catalogListTableValuedFunctions(databaseName, schemaName, apiVersion, $filter, $top, $skip, $select, $orderby, $count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogListTableValuedFunctions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the table valued functions. | |
| **schemaName** | **String**| The name of the schema containing the table valued functions. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$filter** | **String**| OData filter. Optional. | [optional] |
| **$top** | **Integer**| The number of items to return. Optional. | [optional] |
| **$skip** | **Integer**| The number of items to skip over before returning elements. Optional. | [optional] |
| **$select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] |
| **$orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] |
| **$count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] |

### Return type

[**USqlTableValuedFunctionList**](USqlTableValuedFunctionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of table valued functions in the specified database and schema. |  -  |

<a id="catalogListTableValuedFunctionsByDatabase"></a>
# **catalogListTableValuedFunctionsByDatabase**
> USqlTableValuedFunctionList catalogListTableValuedFunctionsByDatabase(databaseName, apiVersion, $filter, $top, $skip, $select, $orderby, $count)



Retrieves the list of all table valued functions in a database from the Data Lake Analytics catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the table valued functions.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | OData filter. Optional.
    Integer $top = 56; // Integer | The number of items to return. Optional.
    Integer $skip = 56; // Integer | The number of items to skip over before returning elements. Optional.
    String $select = "$select_example"; // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
    String $orderby = "$orderby_example"; // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
    Boolean $count = true; // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
    try {
      USqlTableValuedFunctionList result = apiInstance.catalogListTableValuedFunctionsByDatabase(databaseName, apiVersion, $filter, $top, $skip, $select, $orderby, $count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogListTableValuedFunctionsByDatabase");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the table valued functions. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$filter** | **String**| OData filter. Optional. | [optional] |
| **$top** | **Integer**| The number of items to return. Optional. | [optional] |
| **$skip** | **Integer**| The number of items to skip over before returning elements. Optional. | [optional] |
| **$select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] |
| **$orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] |
| **$count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] |

### Return type

[**USqlTableValuedFunctionList**](USqlTableValuedFunctionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of all table valued functions in the specified database. |  -  |

<a id="catalogListTables"></a>
# **catalogListTables**
> USqlTableList catalogListTables(databaseName, schemaName, apiVersion, $filter, $top, $skip, $select, $orderby, $count, basic)



Retrieves the list of tables from the Data Lake Analytics catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the tables.
    String schemaName = "schemaName_example"; // String | The name of the schema containing the tables.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | OData filter. Optional.
    Integer $top = 56; // Integer | The number of items to return. Optional.
    Integer $skip = 56; // Integer | The number of items to skip over before returning elements. Optional.
    String $select = "$select_example"; // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
    String $orderby = "$orderby_example"; // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
    Boolean $count = true; // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
    Boolean basic = false; // Boolean | The basic switch indicates what level of information to return when listing tables. When basic is true, only database_name, schema_name, table_name and version are returned for each table, otherwise all table metadata is returned. By default, it is false. Optional.
    try {
      USqlTableList result = apiInstance.catalogListTables(databaseName, schemaName, apiVersion, $filter, $top, $skip, $select, $orderby, $count, basic);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogListTables");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the tables. | |
| **schemaName** | **String**| The name of the schema containing the tables. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$filter** | **String**| OData filter. Optional. | [optional] |
| **$top** | **Integer**| The number of items to return. Optional. | [optional] |
| **$skip** | **Integer**| The number of items to skip over before returning elements. Optional. | [optional] |
| **$select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] |
| **$orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] |
| **$count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] |
| **basic** | **Boolean**| The basic switch indicates what level of information to return when listing tables. When basic is true, only database_name, schema_name, table_name and version are returned for each table, otherwise all table metadata is returned. By default, it is false. Optional. | [optional] [default to false] |

### Return type

[**USqlTableList**](USqlTableList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of tables in the specified database and schema. |  -  |

<a id="catalogListTablesByDatabase"></a>
# **catalogListTablesByDatabase**
> USqlTableList catalogListTablesByDatabase(databaseName, apiVersion, $filter, $top, $skip, $select, $orderby, $count, basic)



Retrieves the list of all tables in a database from the Data Lake Analytics catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the tables.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | OData filter. Optional.
    Integer $top = 56; // Integer | The number of items to return. Optional.
    Integer $skip = 56; // Integer | The number of items to skip over before returning elements. Optional.
    String $select = "$select_example"; // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
    String $orderby = "$orderby_example"; // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
    Boolean $count = true; // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
    Boolean basic = false; // Boolean | The basic switch indicates what level of information to return when listing tables. When basic is true, only database_name, schema_name, table_name and version are returned for each table, otherwise all table metadata is returned. By default, it is false
    try {
      USqlTableList result = apiInstance.catalogListTablesByDatabase(databaseName, apiVersion, $filter, $top, $skip, $select, $orderby, $count, basic);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogListTablesByDatabase");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the tables. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$filter** | **String**| OData filter. Optional. | [optional] |
| **$top** | **Integer**| The number of items to return. Optional. | [optional] |
| **$skip** | **Integer**| The number of items to skip over before returning elements. Optional. | [optional] |
| **$select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] |
| **$orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] |
| **$count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] |
| **basic** | **Boolean**| The basic switch indicates what level of information to return when listing tables. When basic is true, only database_name, schema_name, table_name and version are returned for each table, otherwise all table metadata is returned. By default, it is false | [optional] [default to false] |

### Return type

[**USqlTableList**](USqlTableList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of all tables in the specified database. |  -  |

<a id="catalogListTypes"></a>
# **catalogListTypes**
> USqlTypeList catalogListTypes(databaseName, schemaName, apiVersion, $filter, $top, $skip, $select, $orderby, $count)



Retrieves the list of types within the specified database and schema from the Data Lake Analytics catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the types.
    String schemaName = "schemaName_example"; // String | The name of the schema containing the types.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | OData filter. Optional.
    Integer $top = 56; // Integer | The number of items to return. Optional.
    Integer $skip = 56; // Integer | The number of items to skip over before returning elements. Optional.
    String $select = "$select_example"; // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
    String $orderby = "$orderby_example"; // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
    Boolean $count = true; // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
    try {
      USqlTypeList result = apiInstance.catalogListTypes(databaseName, schemaName, apiVersion, $filter, $top, $skip, $select, $orderby, $count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogListTypes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the types. | |
| **schemaName** | **String**| The name of the schema containing the types. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$filter** | **String**| OData filter. Optional. | [optional] |
| **$top** | **Integer**| The number of items to return. Optional. | [optional] |
| **$skip** | **Integer**| The number of items to skip over before returning elements. Optional. | [optional] |
| **$select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] |
| **$orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] |
| **$count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] |

### Return type

[**USqlTypeList**](USqlTypeList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of types in the specified database and schema. |  -  |

<a id="catalogListViews"></a>
# **catalogListViews**
> USqlViewList catalogListViews(databaseName, schemaName, apiVersion, $filter, $top, $skip, $select, $orderby, $count)



Retrieves the list of views from the Data Lake Analytics catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the views.
    String schemaName = "schemaName_example"; // String | The name of the schema containing the views.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | OData filter. Optional.
    Integer $top = 56; // Integer | The number of items to return. Optional.
    Integer $skip = 56; // Integer | The number of items to skip over before returning elements. Optional.
    String $select = "$select_example"; // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
    String $orderby = "$orderby_example"; // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
    Boolean $count = true; // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
    try {
      USqlViewList result = apiInstance.catalogListViews(databaseName, schemaName, apiVersion, $filter, $top, $skip, $select, $orderby, $count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogListViews");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the views. | |
| **schemaName** | **String**| The name of the schema containing the views. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$filter** | **String**| OData filter. Optional. | [optional] |
| **$top** | **Integer**| The number of items to return. Optional. | [optional] |
| **$skip** | **Integer**| The number of items to skip over before returning elements. Optional. | [optional] |
| **$select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] |
| **$orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] |
| **$count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] |

### Return type

[**USqlViewList**](USqlViewList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of views in the specified database and schema. |  -  |

<a id="catalogListViewsByDatabase"></a>
# **catalogListViewsByDatabase**
> USqlViewList catalogListViewsByDatabase(databaseName, apiVersion, $filter, $top, $skip, $select, $orderby, $count)



Retrieves the list of all views in a database from the Data Lake Analytics catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the views.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | OData filter. Optional.
    Integer $top = 56; // Integer | The number of items to return. Optional.
    Integer $skip = 56; // Integer | The number of items to skip over before returning elements. Optional.
    String $select = "$select_example"; // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
    String $orderby = "$orderby_example"; // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
    Boolean $count = true; // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
    try {
      USqlViewList result = apiInstance.catalogListViewsByDatabase(databaseName, apiVersion, $filter, $top, $skip, $select, $orderby, $count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogListViewsByDatabase");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the views. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$filter** | **String**| OData filter. Optional. | [optional] |
| **$top** | **Integer**| The number of items to return. Optional. | [optional] |
| **$skip** | **Integer**| The number of items to skip over before returning elements. Optional. | [optional] |
| **$select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] |
| **$orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] |
| **$count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] |

### Return type

[**USqlViewList**](USqlViewList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of all views in the specified database. |  -  |

<a id="catalogPreviewTable"></a>
# **catalogPreviewTable**
> USqlTablePreview catalogPreviewTable(databaseName, schemaName, tableName, apiVersion, maxRows, maxColumns)



Retrieves a preview set of rows in given table.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the table.
    String schemaName = "schemaName_example"; // String | The name of the schema containing the table.
    String tableName = "tableName_example"; // String | The name of the table.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    Long maxRows = 56L; // Long | The maximum number of preview rows to be retrieved. Rows returned may be less than or equal to this number depending on row sizes and number of rows in the table.
    Long maxColumns = 56L; // Long | The maximum number of columns to be retrieved.
    try {
      USqlTablePreview result = apiInstance.catalogPreviewTable(databaseName, schemaName, tableName, apiVersion, maxRows, maxColumns);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogPreviewTable");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the table. | |
| **schemaName** | **String**| The name of the schema containing the table. | |
| **tableName** | **String**| The name of the table. | |
| **apiVersion** | **String**| Client Api Version. | |
| **maxRows** | **Long**| The maximum number of preview rows to be retrieved. Rows returned may be less than or equal to this number depending on row sizes and number of rows in the table. | [optional] |
| **maxColumns** | **Long**| The maximum number of columns to be retrieved. | [optional] |

### Return type

[**USqlTablePreview**](USqlTablePreview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved preview rows for the specified table. |  -  |

<a id="catalogPreviewTablePartition"></a>
# **catalogPreviewTablePartition**
> USqlTablePreview catalogPreviewTablePartition(databaseName, schemaName, tableName, partitionName, apiVersion, maxRows, maxColumns)



Retrieves a preview set of rows in given partition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the partition.
    String schemaName = "schemaName_example"; // String | The name of the schema containing the partition.
    String tableName = "tableName_example"; // String | The name of the table containing the partition.
    String partitionName = "partitionName_example"; // String | The name of the table partition.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    Long maxRows = 56L; // Long | The maximum number of preview rows to be retrieved.Rows returned may be less than or equal to this number depending on row sizes and number of rows in the partition.
    Long maxColumns = 56L; // Long | The maximum number of columns to be retrieved.
    try {
      USqlTablePreview result = apiInstance.catalogPreviewTablePartition(databaseName, schemaName, tableName, partitionName, apiVersion, maxRows, maxColumns);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogPreviewTablePartition");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the partition. | |
| **schemaName** | **String**| The name of the schema containing the partition. | |
| **tableName** | **String**| The name of the table containing the partition. | |
| **partitionName** | **String**| The name of the table partition. | |
| **apiVersion** | **String**| Client Api Version. | |
| **maxRows** | **Long**| The maximum number of preview rows to be retrieved.Rows returned may be less than or equal to this number depending on row sizes and number of rows in the partition. | [optional] |
| **maxColumns** | **Long**| The maximum number of columns to be retrieved. | [optional] |

### Return type

[**USqlTablePreview**](USqlTablePreview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved preview rows for the specified partition. |  -  |

<a id="catalogUpdateCredential"></a>
# **catalogUpdateCredential**
> catalogUpdateCredential(databaseName, credentialName, apiVersion, parameters)



Modifies the specified credential for use with external data sources in the specified database

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the credential.
    String credentialName = "credentialName_example"; // String | The name of the credential.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    DataLakeAnalyticsCatalogCredentialUpdateParameters parameters = new DataLakeAnalyticsCatalogCredentialUpdateParameters(); // DataLakeAnalyticsCatalogCredentialUpdateParameters | The parameters required to modify the credential (name and password)
    try {
      apiInstance.catalogUpdateCredential(databaseName, credentialName, apiVersion, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogUpdateCredential");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the credential. | |
| **credentialName** | **String**| The name of the credential. | |
| **apiVersion** | **String**| Client Api Version. | |
| **parameters** | [**DataLakeAnalyticsCatalogCredentialUpdateParameters**](DataLakeAnalyticsCatalogCredentialUpdateParameters.md)| The parameters required to modify the credential (name and password) | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the specified credential&#39;s password in the specified database |  -  |

<a id="catalogUpdateSecret"></a>
# **catalogUpdateSecret**
> catalogUpdateSecret(databaseName, secretName, apiVersion, parameters)



Modifies the specified secret for use with external data sources in the specified database. This is deprecated and will be removed in the next release. Please use UpdateCredential instead.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database containing the secret.
    String secretName = "secretName_example"; // String | The name of the secret.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    DataLakeAnalyticsCatalogSecretCreateOrUpdateParameters parameters = new DataLakeAnalyticsCatalogSecretCreateOrUpdateParameters(); // DataLakeAnalyticsCatalogSecretCreateOrUpdateParameters | The parameters required to modify the secret (name and password)
    try {
      apiInstance.catalogUpdateSecret(databaseName, secretName, apiVersion, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#catalogUpdateSecret");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseName** | **String**| The name of the database containing the secret. | |
| **secretName** | **String**| The name of the secret. | |
| **apiVersion** | **String**| Client Api Version. | |
| **parameters** | [**DataLakeAnalyticsCatalogSecretCreateOrUpdateParameters**](DataLakeAnalyticsCatalogSecretCreateOrUpdateParameters.md)| The parameters required to modify the secret (name and password) | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the details of the specified secret in the specified database. |  -  |

