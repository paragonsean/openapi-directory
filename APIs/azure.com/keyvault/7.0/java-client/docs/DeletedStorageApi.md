# DeletedStorageApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDeletedSasDefinition**](DeletedStorageApi.md#getDeletedSasDefinition) | **GET** /deletedstorage/{storage-account-name}/sas/{sas-definition-name} | Gets the specified deleted sas definition. |
| [**getDeletedSasDefinitions**](DeletedStorageApi.md#getDeletedSasDefinitions) | **GET** /deletedstorage/{storage-account-name}/sas | Lists deleted SAS definitions for the specified vault and storage account. |
| [**getDeletedStorageAccount**](DeletedStorageApi.md#getDeletedStorageAccount) | **GET** /deletedstorage/{storage-account-name} | Gets the specified deleted storage account. |
| [**getDeletedStorageAccounts**](DeletedStorageApi.md#getDeletedStorageAccounts) | **GET** /deletedstorage | Lists deleted storage accounts for the specified vault. |
| [**purgeDeletedStorageAccount**](DeletedStorageApi.md#purgeDeletedStorageAccount) | **DELETE** /deletedstorage/{storage-account-name} | Permanently deletes the specified storage account. |
| [**recoverDeletedSasDefinition**](DeletedStorageApi.md#recoverDeletedSasDefinition) | **POST** /deletedstorage/{storage-account-name}/sas/{sas-definition-name}/recover | Recovers the deleted SAS definition. |
| [**recoverDeletedStorageAccount**](DeletedStorageApi.md#recoverDeletedStorageAccount) | **POST** /deletedstorage/{storage-account-name}/recover | Recovers the deleted storage account. |


<a id="getDeletedSasDefinition"></a>
# **getDeletedSasDefinition**
> DeletedSasDefinitionBundle getDeletedSasDefinition(storageAccountName, sasDefinitionName, apiVersion)

Gets the specified deleted sas definition.

The Get Deleted SAS Definition operation returns the specified deleted SAS definition along with its attributes. This operation requires the storage/getsas permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeletedStorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    DeletedStorageApi apiInstance = new DeletedStorageApi(defaultClient);
    String storageAccountName = "storageAccountName_example"; // String | The name of the storage account.
    String sasDefinitionName = "sasDefinitionName_example"; // String | The name of the SAS definition.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      DeletedSasDefinitionBundle result = apiInstance.getDeletedSasDefinition(storageAccountName, sasDefinitionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeletedStorageApi#getDeletedSasDefinition");
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
| **200** | The deleted SAS definition and information on when the it will be purged, and how to recover the deleted SAS definition. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="getDeletedSasDefinitions"></a>
# **getDeletedSasDefinitions**
> DeletedSasDefinitionListResult getDeletedSasDefinitions(storageAccountName, apiVersion, maxresults)

Lists deleted SAS definitions for the specified vault and storage account.

The Get Deleted Sas Definitions operation returns the SAS definitions that have been deleted for a vault enabled for soft-delete. This operation requires the storage/listsas permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeletedStorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    DeletedStorageApi apiInstance = new DeletedStorageApi(defaultClient);
    String storageAccountName = "storageAccountName_example"; // String | The name of the storage account.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    Integer maxresults = 56; // Integer | Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    try {
      DeletedSasDefinitionListResult result = apiInstance.getDeletedSasDefinitions(storageAccountName, apiVersion, maxresults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeletedStorageApi#getDeletedSasDefinitions");
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

[**DeletedSasDefinitionListResult**](DeletedSasDefinitionListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A response message containing a list of deleted SAS definitions for the storage account, along with a link to the next page of deleted SAS definitions. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="getDeletedStorageAccount"></a>
# **getDeletedStorageAccount**
> DeletedStorageBundle getDeletedStorageAccount(storageAccountName, apiVersion)

Gets the specified deleted storage account.

The Get Deleted Storage Account operation returns the specified deleted storage account along with its attributes. This operation requires the storage/get permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeletedStorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    DeletedStorageApi apiInstance = new DeletedStorageApi(defaultClient);
    String storageAccountName = "storageAccountName_example"; // String | The name of the storage account.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      DeletedStorageBundle result = apiInstance.getDeletedStorageAccount(storageAccountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeletedStorageApi#getDeletedStorageAccount");
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
| **200** | The deleted storage account and information on when it will be purged, and how to recover the deleted storage account. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="getDeletedStorageAccounts"></a>
# **getDeletedStorageAccounts**
> DeletedStorageListResult getDeletedStorageAccounts(apiVersion, maxresults)

Lists deleted storage accounts for the specified vault.

The Get Deleted Storage Accounts operation returns the storage accounts that have been deleted for a vault enabled for soft-delete. This operation requires the storage/list permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeletedStorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    DeletedStorageApi apiInstance = new DeletedStorageApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    Integer maxresults = 56; // Integer | Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    try {
      DeletedStorageListResult result = apiInstance.getDeletedStorageAccounts(apiVersion, maxresults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeletedStorageApi#getDeletedStorageAccounts");
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

[**DeletedStorageListResult**](DeletedStorageListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A response message containing a list of deleted storage accounts in the vault, along with a link to the next page of deleted storage accounts. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="purgeDeletedStorageAccount"></a>
# **purgeDeletedStorageAccount**
> purgeDeletedStorageAccount(storageAccountName, apiVersion)

Permanently deletes the specified storage account.

The purge deleted storage account operation removes the secret permanently, without the possibility of recovery. This operation can only be performed on a soft-delete enabled vault. This operation requires the storage/purge permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeletedStorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    DeletedStorageApi apiInstance = new DeletedStorageApi(defaultClient);
    String storageAccountName = "storageAccountName_example"; // String | The name of the storage account.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      apiInstance.purgeDeletedStorageAccount(storageAccountName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeletedStorageApi#purgeDeletedStorageAccount");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content signaling that the storage account was purged forever. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="recoverDeletedSasDefinition"></a>
# **recoverDeletedSasDefinition**
> SasDefinitionBundle recoverDeletedSasDefinition(storageAccountName, sasDefinitionName, apiVersion)

Recovers the deleted SAS definition.

Recovers the deleted SAS definition for the specified storage account. This operation can only be performed on a soft-delete enabled vault. This operation requires the storage/recover permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeletedStorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    DeletedStorageApi apiInstance = new DeletedStorageApi(defaultClient);
    String storageAccountName = "storageAccountName_example"; // String | The name of the storage account.
    String sasDefinitionName = "sasDefinitionName_example"; // String | The name of the SAS definition.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      SasDefinitionBundle result = apiInstance.recoverDeletedSasDefinition(storageAccountName, sasDefinitionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeletedStorageApi#recoverDeletedSasDefinition");
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
| **200** | A SAS definition bundle of the original SAS definition and its attributes. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="recoverDeletedStorageAccount"></a>
# **recoverDeletedStorageAccount**
> StorageBundle recoverDeletedStorageAccount(storageAccountName, apiVersion)

Recovers the deleted storage account.

Recovers the deleted storage account in the specified vault. This operation can only be performed on a soft-delete enabled vault. This operation requires the storage/recover permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeletedStorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    DeletedStorageApi apiInstance = new DeletedStorageApi(defaultClient);
    String storageAccountName = "storageAccountName_example"; // String | The name of the storage account.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      StorageBundle result = apiInstance.recoverDeletedStorageAccount(storageAccountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeletedStorageApi#recoverDeletedStorageAccount");
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
| **200** | A storage bundle of the original storage account and its attributes. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

