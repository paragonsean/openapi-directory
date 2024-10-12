# RecoveryPointsCrrApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**recoveryPointsCrrList**](RecoveryPointsCrrApi.md#recoveryPointsCrrList) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName}/recoveryPoints/ |  |


<a id="recoveryPointsCrrList"></a>
# **recoveryPointsCrrList**
> RecoveryPointResourceList recoveryPointsCrrList(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, $filter)



Lists the backup copies for the backed up item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecoveryPointsCrrApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RecoveryPointsCrrApi apiInstance = new RecoveryPointsCrrApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String vaultName = "vaultName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name associated with the backed up item.
    String containerName = "containerName_example"; // String | Container name associated with the backed up item.
    String protectedItemName = "protectedItemName_example"; // String | Backed up item whose backup copies are to be fetched.
    String $filter = "$filter_example"; // String | OData filter options.
    try {
      RecoveryPointResourceList result = apiInstance.recoveryPointsCrrList(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecoveryPointsCrrApi#recoveryPointsCrrList");
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
| **fabricName** | **String**| Fabric name associated with the backed up item. | |
| **containerName** | **String**| Container name associated with the backed up item. | |
| **protectedItemName** | **String**| Backed up item whose backup copies are to be fetched. | |
| **$filter** | **String**| OData filter options. | [optional] |

### Return type

[**RecoveryPointResourceList**](RecoveryPointResourceList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

