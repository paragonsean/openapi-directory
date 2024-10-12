# StorageApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**backupStorageAccount**](StorageApi.md#backupStorageAccount) | **POST** /storage/{storage-account-name}/backup | Backs up the specified storage account. |
| [**deleteSasDefinition**](StorageApi.md#deleteSasDefinition) | **DELETE** /storage/{storage-account-name}/sas/{sas-definition-name} |  |
| [**deleteStorageAccount**](StorageApi.md#deleteStorageAccount) | **DELETE** /storage/{storage-account-name} |  |
| [**getSasDefinition**](StorageApi.md#getSasDefinition) | **GET** /storage/{storage-account-name}/sas/{sas-definition-name} |  |
| [**getSasDefinitions**](StorageApi.md#getSasDefinitions) | **GET** /storage/{storage-account-name}/sas |  |
| [**getStorageAccount**](StorageApi.md#getStorageAccount) | **GET** /storage/{storage-account-name} |  |
| [**getStorageAccounts**](StorageApi.md#getStorageAccounts) | **GET** /storage |  |
| [**regenerateStorageAccountKey**](StorageApi.md#regenerateStorageAccountKey) | **POST** /storage/{storage-account-name}/regeneratekey |  |
| [**restoreStorageAccount**](StorageApi.md#restoreStorageAccount) | **POST** /storage/restore | Restores a backed up storage account to a vault. |
| [**setSasDefinition**](StorageApi.md#setSasDefinition) | **PUT** /storage/{storage-account-name}/sas/{sas-definition-name} |  |
| [**setStorageAccount**](StorageApi.md#setStorageAccount) | **PUT** /storage/{storage-account-name} |  |
| [**updateSasDefinition**](StorageApi.md#updateSasDefinition) | **PATCH** /storage/{storage-account-name}/sas/{sas-definition-name} |  |
| [**updateStorageAccount**](StorageApi.md#updateStorageAccount) | **PATCH** /storage/{storage-account-name} |  |


<a id="backupStorageAccount"></a>
# **backupStorageAccount**
> BackupStorageResult backupStorageAccount(storageAccountName, apiVersion)

Backs up the specified storage account.

Requests that a backup of the specified storage account be downloaded to the client. This operation requires the storage/backup permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String storageAccountName = "storageAccountName_example"; // String | The name of the storage account.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      BackupStorageResult result = apiInstance.backupStorageAccount(storageAccountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#backupStorageAccount");
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
| **storageAccountName** | **String**| The name of the storage account. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**BackupStorageResult**](BackupStorageResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The backup blob containing the backed up storage account. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="deleteSasDefinition"></a>
# **deleteSasDefinition**
> DeletedSasDefinitionBundle deleteSasDefinition(storageAccountName, sasDefinitionName, apiVersion)



Deletes a SAS definition from a specified storage account. This operation requires the storage/deletesas permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String storageAccountName = "storageAccountName_example"; // String | The name of the storage account.
    String sasDefinitionName = "sasDefinitionName_example"; // String | The name of the SAS definition.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      DeletedSasDefinitionBundle result = apiInstance.deleteSasDefinition(storageAccountName, sasDefinitionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#deleteSasDefinition");
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
| **storageAccountName** | **String**| The name of the storage account. | |
| **sasDefinitionName** | **String**| The name of the SAS definition. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**DeletedSasDefinitionBundle**](DeletedSasDefinitionBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The deleted SAS definition and information on when the SAS definition will be deleted, and how to recover the deleted SAS definition. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="deleteStorageAccount"></a>
# **deleteStorageAccount**
> DeletedStorageBundle deleteStorageAccount(storageAccountName, apiVersion)



Deletes a storage account. This operation requires the storage/delete permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String storageAccountName = "storageAccountName_example"; // String | The name of the storage account.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      DeletedStorageBundle result = apiInstance.deleteStorageAccount(storageAccountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#deleteStorageAccount");
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
| **storageAccountName** | **String**| The name of the storage account. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**DeletedStorageBundle**](DeletedStorageBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The deleted storage account and information on when the storage account will be deleted, and how to recover the deleted storage account. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="getSasDefinition"></a>
# **getSasDefinition**
> SasDefinitionBundle getSasDefinition(storageAccountName, sasDefinitionName, apiVersion)



Gets information about a SAS definition for the specified storage account. This operation requires the storage/getsas permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String storageAccountName = "storageAccountName_example"; // String | The name of the storage account.
    String sasDefinitionName = "sasDefinitionName_example"; // String | The name of the SAS definition.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      SasDefinitionBundle result = apiInstance.getSasDefinition(storageAccountName, sasDefinitionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#getSasDefinition");
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
| **storageAccountName** | **String**| The name of the storage account. | |
| **sasDefinitionName** | **String**| The name of the SAS definition. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**SasDefinitionBundle**](SasDefinitionBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The retrieved SAS definition. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="getSasDefinitions"></a>
# **getSasDefinitions**
> SasDefinitionListResult getSasDefinitions(storageAccountName, apiVersion, maxresults)



List storage SAS definitions for the given storage account. This operation requires the storage/listsas permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String storageAccountName = "storageAccountName_example"; // String | The name of the storage account.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    Integer maxresults = 56; // Integer | Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    try {
      SasDefinitionListResult result = apiInstance.getSasDefinitions(storageAccountName, apiVersion, maxresults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#getSasDefinitions");
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
| **storageAccountName** | **String**| The name of the storage account. | |
| **apiVersion** | **String**| Client API version. | |
| **maxresults** | **Integer**| Maximum number of results to return in a page. If not specified the service will return up to 25 results. | [optional] |

### Return type

[**SasDefinitionListResult**](SasDefinitionListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A response message containing a list of SAS definitions along with a link to the next page of SAS definitions. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="getStorageAccount"></a>
# **getStorageAccount**
> StorageBundle getStorageAccount(storageAccountName, apiVersion)



Gets information about a specified storage account. This operation requires the storage/get permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String storageAccountName = "storageAccountName_example"; // String | The name of the storage account.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      StorageBundle result = apiInstance.getStorageAccount(storageAccountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#getStorageAccount");
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
| **storageAccountName** | **String**| The name of the storage account. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**StorageBundle**](StorageBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The retrieved storage account. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="getStorageAccounts"></a>
# **getStorageAccounts**
> StorageListResult getStorageAccounts(apiVersion, maxresults)



List storage accounts managed by the specified key vault. This operation requires the storage/list permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    Integer maxresults = 56; // Integer | Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    try {
      StorageListResult result = apiInstance.getStorageAccounts(apiVersion, maxresults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#getStorageAccounts");
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
| **apiVersion** | **String**| Client API version. | |
| **maxresults** | **Integer**| Maximum number of results to return in a page. If not specified the service will return up to 25 results. | [optional] |

### Return type

[**StorageListResult**](StorageListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A response message containing a list of storage accounts along with a link to the next page of storage accounts. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="regenerateStorageAccountKey"></a>
# **regenerateStorageAccountKey**
> StorageBundle regenerateStorageAccountKey(storageAccountName, apiVersion, parameters)



Regenerates the specified key value for the given storage account. This operation requires the storage/regeneratekey permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String storageAccountName = "storageAccountName_example"; // String | The name of the storage account.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    StorageAccountRegenerteKeyParameters parameters = new StorageAccountRegenerteKeyParameters(); // StorageAccountRegenerteKeyParameters | The parameters to regenerate storage account key.
    try {
      StorageBundle result = apiInstance.regenerateStorageAccountKey(storageAccountName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#regenerateStorageAccountKey");
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
| **storageAccountName** | **String**| The name of the storage account. | |
| **apiVersion** | **String**| Client API version. | |
| **parameters** | [**StorageAccountRegenerteKeyParameters**](StorageAccountRegenerteKeyParameters.md)| The parameters to regenerate storage account key. | |

### Return type

[**StorageBundle**](StorageBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated storage account. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="restoreStorageAccount"></a>
# **restoreStorageAccount**
> StorageBundle restoreStorageAccount(apiVersion, parameters)

Restores a backed up storage account to a vault.

Restores a backed up storage account to a vault. This operation requires the storage/restore permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    StorageRestoreParameters parameters = new StorageRestoreParameters(); // StorageRestoreParameters | The parameters to restore the storage account.
    try {
      StorageBundle result = apiInstance.restoreStorageAccount(apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#restoreStorageAccount");
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
| **apiVersion** | **String**| Client API version. | |
| **parameters** | [**StorageRestoreParameters**](StorageRestoreParameters.md)| The parameters to restore the storage account. | |

### Return type

[**StorageBundle**](StorageBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Restored storage account bundle in the vault. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="setSasDefinition"></a>
# **setSasDefinition**
> SasDefinitionBundle setSasDefinition(storageAccountName, sasDefinitionName, apiVersion, parameters)



Creates or updates a new SAS definition for the specified storage account. This operation requires the storage/setsas permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String storageAccountName = "storageAccountName_example"; // String | The name of the storage account.
    String sasDefinitionName = "sasDefinitionName_example"; // String | The name of the SAS definition.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    SasDefinitionCreateParameters parameters = new SasDefinitionCreateParameters(); // SasDefinitionCreateParameters | The parameters to create a SAS definition.
    try {
      SasDefinitionBundle result = apiInstance.setSasDefinition(storageAccountName, sasDefinitionName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#setSasDefinition");
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
| **storageAccountName** | **String**| The name of the storage account. | |
| **sasDefinitionName** | **String**| The name of the SAS definition. | |
| **apiVersion** | **String**| Client API version. | |
| **parameters** | [**SasDefinitionCreateParameters**](SasDefinitionCreateParameters.md)| The parameters to create a SAS definition. | |

### Return type

[**SasDefinitionBundle**](SasDefinitionBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The created SAS definition. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="setStorageAccount"></a>
# **setStorageAccount**
> StorageBundle setStorageAccount(storageAccountName, apiVersion, parameters)



Creates or updates a new storage account. This operation requires the storage/set permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String storageAccountName = "storageAccountName_example"; // String | The name of the storage account.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    StorageAccountCreateParameters parameters = new StorageAccountCreateParameters(); // StorageAccountCreateParameters | The parameters to create a storage account.
    try {
      StorageBundle result = apiInstance.setStorageAccount(storageAccountName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#setStorageAccount");
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
| **storageAccountName** | **String**| The name of the storage account. | |
| **apiVersion** | **String**| Client API version. | |
| **parameters** | [**StorageAccountCreateParameters**](StorageAccountCreateParameters.md)| The parameters to create a storage account. | |

### Return type

[**StorageBundle**](StorageBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The created storage account. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="updateSasDefinition"></a>
# **updateSasDefinition**
> SasDefinitionBundle updateSasDefinition(storageAccountName, sasDefinitionName, apiVersion, parameters)



Updates the specified attributes associated with the given SAS definition. This operation requires the storage/setsas permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String storageAccountName = "storageAccountName_example"; // String | The name of the storage account.
    String sasDefinitionName = "sasDefinitionName_example"; // String | The name of the SAS definition.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    SasDefinitionUpdateParameters parameters = new SasDefinitionUpdateParameters(); // SasDefinitionUpdateParameters | The parameters to update a SAS definition.
    try {
      SasDefinitionBundle result = apiInstance.updateSasDefinition(storageAccountName, sasDefinitionName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#updateSasDefinition");
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
| **storageAccountName** | **String**| The name of the storage account. | |
| **sasDefinitionName** | **String**| The name of the SAS definition. | |
| **apiVersion** | **String**| Client API version. | |
| **parameters** | [**SasDefinitionUpdateParameters**](SasDefinitionUpdateParameters.md)| The parameters to update a SAS definition. | |

### Return type

[**SasDefinitionBundle**](SasDefinitionBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated SAS definition. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="updateStorageAccount"></a>
# **updateStorageAccount**
> StorageBundle updateStorageAccount(storageAccountName, apiVersion, parameters)



Updates the specified attributes associated with the given storage account. This operation requires the storage/set/update permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String storageAccountName = "storageAccountName_example"; // String | The name of the storage account.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    StorageAccountUpdateParameters parameters = new StorageAccountUpdateParameters(); // StorageAccountUpdateParameters | The parameters to update a storage account.
    try {
      StorageBundle result = apiInstance.updateStorageAccount(storageAccountName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#updateStorageAccount");
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
| **storageAccountName** | **String**| The name of the storage account. | |
| **apiVersion** | **String**| Client API version. | |
| **parameters** | [**StorageAccountUpdateParameters**](StorageAccountUpdateParameters.md)| The parameters to update a storage account. | |

### Return type

[**StorageBundle**](StorageBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated storage account. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

