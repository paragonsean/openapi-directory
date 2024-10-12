# VolumesRevertApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**volumesRevert**](VolumesRevertApi.md#volumesRevert) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/revert | Revert a volume to one of its snapshots |


<a id="volumesRevert"></a>
# **volumesRevert**
> volumesRevert(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion, body)

Revert a volume to one of its snapshots

Revert a volume to the snapshot specified in the body

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesRevertApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VolumesRevertApi apiInstance = new VolumesRevertApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String accountName = "accountName_example"; // String | The name of the NetApp account
    String poolName = "poolName_example"; // String | The name of the capacity pool
    String volumeName = "volumeName_example"; // String | The name of the volume
    String apiVersion = "2019-11-01"; // String | Version of the API to be used with the client request.
    VolumeRevert body = new VolumeRevert(); // VolumeRevert | Object for snapshot to revert supplied in the body of the operation.
    try {
      apiInstance.volumesRevert(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesRevertApi#volumesRevert");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **accountName** | **String**| The name of the NetApp account | |
| **poolName** | **String**| The name of the capacity pool | |
| **volumeName** | **String**| The name of the volume | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | [default to 2019-11-01] |
| **body** | [**VolumeRevert**](VolumeRevert.md)| Object for snapshot to revert supplied in the body of the operation. | |

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
| **200** | OK - terminal state |  -  |
| **202** | Accepted |  -  |
| **0** | Error response describing why the operation failed. |  -  |

