# GcApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**farmsGetGarbageCollectionState**](GcApi.md#farmsGetGarbageCollectionState) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/operationresults/{operationId} |  |


<a id="farmsGetGarbageCollectionState"></a>
# **farmsGetGarbageCollectionState**
> String farmsGetGarbageCollectionState(subscriptionId, resourceGroupName, farmId, apiVersion, operationId)



Returns the state of the garbage collection job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GcApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GcApi apiInstance = new GcApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String farmId = "farmId_example"; // String | Farm Id.
    String apiVersion = "apiVersion_example"; // String | REST Api Version.
    String operationId = "operationId_example"; // String | Operation Id.
    try {
      String result = apiInstance.farmsGetGarbageCollectionState(subscriptionId, resourceGroupName, farmId, apiVersion, operationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GcApi#farmsGetGarbageCollectionState");
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
| **subscriptionId** | **String**| Subscription Id. | |
| **resourceGroupName** | **String**| Resource group name. | |
| **farmId** | **String**| Farm Id. | |
| **apiVersion** | **String**| REST Api Version. | |
| **operationId** | **String**| Operation Id. | |

### Return type

**String**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- The state of garbage collection has been returned. |  -  |
| **404** | NOT FOUND -- The specified farm or garbage collection job can not be found. |  -  |

