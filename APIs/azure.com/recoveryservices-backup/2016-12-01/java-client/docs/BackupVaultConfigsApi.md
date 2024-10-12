# BackupVaultConfigsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**backupVaultConfigsGet**](BackupVaultConfigsApi.md#backupVaultConfigsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupconfig/vaultconfig |  |
| [**backupVaultConfigsUpdate**](BackupVaultConfigsApi.md#backupVaultConfigsUpdate) | **PATCH** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupconfig/vaultconfig |  |


<a id="backupVaultConfigsGet"></a>
# **backupVaultConfigsGet**
> BackupVaultConfig backupVaultConfigsGet(subscriptionId, apiVersion, resourceGroupName, vaultName)



Fetches vault config.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupVaultConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BackupVaultConfigsApi apiInstance = new BackupVaultConfigsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String vaultName = "vaultName_example"; // String | The name of the recovery services vault.
    try {
      BackupVaultConfig result = apiInstance.backupVaultConfigsGet(subscriptionId, apiVersion, resourceGroupName, vaultName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupVaultConfigsApi#backupVaultConfigsGet");
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

[**BackupVaultConfig**](BackupVaultConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="backupVaultConfigsUpdate"></a>
# **backupVaultConfigsUpdate**
> BackupVaultConfig backupVaultConfigsUpdate(subscriptionId, apiVersion, resourceGroupName, vaultName, backupVaultConfig)



Updates vault config model type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupVaultConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BackupVaultConfigsApi apiInstance = new BackupVaultConfigsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String vaultName = "vaultName_example"; // String | The name of the recovery services vault.
    BackupVaultConfig backupVaultConfig = new BackupVaultConfig(); // BackupVaultConfig | Backup vault config.
    try {
      BackupVaultConfig result = apiInstance.backupVaultConfigsUpdate(subscriptionId, apiVersion, resourceGroupName, vaultName, backupVaultConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupVaultConfigsApi#backupVaultConfigsUpdate");
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
| **backupVaultConfig** | [**BackupVaultConfig**](BackupVaultConfig.md)| Backup vault config. | |

### Return type

[**BackupVaultConfig**](BackupVaultConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

