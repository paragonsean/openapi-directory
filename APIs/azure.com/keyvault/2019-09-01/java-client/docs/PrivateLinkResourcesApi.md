# PrivateLinkResourcesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**privateLinkResourcesListByVault**](PrivateLinkResourcesApi.md#privateLinkResourcesListByVault) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/privateLinkResources |  |


<a id="privateLinkResourcesListByVault"></a>
# **privateLinkResourcesListByVault**
> PrivateLinkResourceListResult privateLinkResourcesListByVault(subscriptionId, resourceGroupName, vaultName, apiVersion)



Gets the private link resources supported for the key vault.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateLinkResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    PrivateLinkResourcesApi apiInstance = new PrivateLinkResourcesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group that contains the key vault.
    String vaultName = "vaultName_example"; // String | The name of the key vault.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      PrivateLinkResourceListResult result = apiInstance.privateLinkResourcesListByVault(subscriptionId, resourceGroupName, vaultName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateLinkResourcesApi#privateLinkResourcesListByVault");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the resource group that contains the key vault. | |
| **vaultName** | **String**| The name of the key vault. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**PrivateLinkResourceListResult**](PrivateLinkResourceListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved private link resources. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

