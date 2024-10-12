# BackupStorageConfigsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**backupStorageConfigsGet**](BackupStorageConfigsApi.md#backupStorageConfigsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupstorageconfig/vaultstorageconfig |  |
| [**backupStorageConfigsUpdate**](BackupStorageConfigsApi.md#backupStorageConfigsUpdate) | **PATCH** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupstorageconfig/vaultstorageconfig |  |


<a id="backupStorageConfigsGet"></a>
# **backupStorageConfigsGet**
> BackupStorageConfig backupStorageConfigsGet(subscriptionId, apiVersion, resourceGroupName, vaultName)



Fetches resource storage config.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupStorageConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BackupStorageConfigsApi apiInstance = new BackupStorageConfigsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String vaultName = "vaultName_example"; // String | The name of the recovery services vault.
    try {
      BackupStorageConfig result = apiInstance.backupStorageConfigsGet(subscriptionId, apiVersion, resourceGroupName, vaultName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupStorageConfigsApi#backupStorageConfigsGet");
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
| **subscriptionId** | **String**| The subscription Id. | |
| **apiVersion** | **String**| Client Api Version. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **vaultName** | **String**| The name of the recovery services vault. | |

### Return type

[**BackupStorageConfig**](BackupStorageConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="backupStorageConfigsUpdate"></a>
# **backupStorageConfigsUpdate**
> backupStorageConfigsUpdate(subscriptionId, apiVersion, resourceGroupName, vaultName, backupStorageConfig)



Updates vault storage model type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupStorageConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BackupStorageConfigsApi apiInstance = new BackupStorageConfigsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String vaultName = "vaultName_example"; // String | The name of the recovery services vault.
    BackupStorageConfig backupStorageConfig = new BackupStorageConfig(); // BackupStorageConfig | Backup storage config.
    try {
      apiInstance.backupStorageConfigsUpdate(subscriptionId, apiVersion, resourceGroupName, vaultName, backupStorageConfig);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupStorageConfigsApi#backupStorageConfigsUpdate");
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
| **subscriptionId** | **String**| The subscription Id. | |
| **apiVersion** | **String**| Client Api Version. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **vaultName** | **String**| The name of the recovery services vault. | |
| **backupStorageConfig** | [**BackupStorageConfig**](BackupStorageConfig.md)| Backup storage config. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | NoContent |  -  |

