# StreamingEndpointApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**streamingEndpointsUpdate**](StreamingEndpointApi.md#streamingEndpointsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/streamingEndpoints/{streamingEndpointName} | Update StreamingEndpoint |


<a id="streamingEndpointsUpdate"></a>
# **streamingEndpointsUpdate**
> StreamingEndpoint streamingEndpointsUpdate(subscriptionId, resourceGroupName, accountName, streamingEndpointName, apiVersion, parameters)

Update StreamingEndpoint

Updates a existing StreamingEndpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamingEndpointApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    StreamingEndpointApi apiInstance = new StreamingEndpointApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String streamingEndpointName = "streamingEndpointName_example"; // String | The name of the StreamingEndpoint.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    StreamingEndpoint parameters = new StreamingEndpoint(); // StreamingEndpoint | StreamingEndpoint properties needed for creation.
    try {
      StreamingEndpoint result = apiInstance.streamingEndpointsUpdate(subscriptionId, resourceGroupName, accountName, streamingEndpointName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamingEndpointApi#streamingEndpointsUpdate");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **streamingEndpointName** | **String**| The name of the StreamingEndpoint. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |
| **parameters** | [**StreamingEndpoint**](StreamingEndpoint.md)| StreamingEndpoint properties needed for creation. | |

### Return type

[**StreamingEndpoint**](StreamingEndpoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **202** | Accepted. The request has been accepted for processing and the operation will complete asynchronously. See https://go.microsoft.com/fwlink/?linkid&#x3D;2087017 for details on the monitoring asynchronous Azure Operations. |  -  |
| **0** | The streaming error response describing why the operation failed. |  -  |

