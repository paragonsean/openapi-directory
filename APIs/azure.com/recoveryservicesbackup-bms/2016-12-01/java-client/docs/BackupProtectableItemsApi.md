# BackupProtectableItemsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**backupProtectableItemsList**](BackupProtectableItemsApi.md#backupProtectableItemsList) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupProtectableItems |  |


<a id="backupProtectableItemsList"></a>
# **backupProtectableItemsList**
> WorkloadProtectableItemResourceList backupProtectableItemsList(apiVersion, vaultName, resourceGroupName, subscriptionId, $filter, $skipToken)



Provides a pageable list of protectable objects within your subscription according to the query filter and the  pagination parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupProtectableItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BackupProtectableItemsApi apiInstance = new BackupProtectableItemsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String vaultName = "vaultName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String $filter = "$filter_example"; // String | OData filter options.
    String $skipToken = "$skipToken_example"; // String | skipToken Filter.
    try {
      WorkloadProtectableItemResourceList result = apiInstance.backupProtectableItemsList(apiVersion, vaultName, resourceGroupName, subscriptionId, $filter, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupProtectableItemsApi#backupProtectableItemsList");
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
| **vaultName** | **String**| The name of the recovery services vault. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **subscriptionId** | **String**| The subscription Id. | |
| **$filter** | **String**| OData filter options. | [optional] |
| **$skipToken** | **String**| skipToken Filter. | [optional] |

### Return type

[**WorkloadProtectableItemResourceList**](WorkloadProtectableItemResourceList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

