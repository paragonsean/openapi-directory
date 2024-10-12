# DeleteApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**iotHubResourceDelete**](DeleteApi.md#iotHubResourceDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName} | Delete an IoT hub. |
| [**iotHubResourceDeleteEventHubConsumerGroup**](DeleteApi.md#iotHubResourceDeleteEventHubConsumerGroup) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/eventHubEndpoints/{eventHubEndpointName}/ConsumerGroups/{name} | Delete a consumer group from an Event Hub-compatible endpoint in an IoT hub. |


<a id="iotHubResourceDelete"></a>
# **iotHubResourceDelete**
> IotHubDescription iotHubResourceDelete(apiVersion, subscriptionId, resourceGroupName, resourceName)

Delete an IoT hub.

Delete an IoT hub.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeleteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeleteApi apiInstance = new DeleteApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
    String resourceName = "resourceName_example"; // String | The name of the IoT hub.
    try {
      IotHubDescription result = apiInstance.iotHubResourceDelete(apiVersion, subscriptionId, resourceGroupName, resourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeleteApi#iotHubResourceDelete");
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
| **apiVersion** | **String**| The version of the API. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the IoT hub. | |
| **resourceName** | **String**| The name of the IoT hub. | |

### Return type

[**IotHubDescription**](IotHubDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is returned as a response to the status polling request for the delete operation. The body contains the resource representation that indicates a transitional provisioning state. |  -  |
| **202** | The Iot Hub resource provider always returns a 202 Accepted status code with valid Location and Retry-After headers. The resource provider also sets the Azure-AsyncOperation header with a URL that points to the operation resource for this operation. Subsequent GET attempts on the resource after a DELETE operation return a resource representation that indicates a transitional provisioning state (such as Terminating). To retrieve the status of the operation, a client can either poll the URL returned in the Location header after the Retry-After interval, get the IoT Hub service status directly, or query the operation resource. |  -  |
| **204** | Once the long running delete operation completes successfully, a 204 No Content status code is returned when the status polling request finds the Iot hub metadata in the service and the status of the delete operation is set to a completed state. |  -  |
| **404** | After the long running delete operation completes successfully, a 404 Not Found is returned when the status polling request no longer finds the Iot hub metadata in the service. |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="iotHubResourceDeleteEventHubConsumerGroup"></a>
# **iotHubResourceDeleteEventHubConsumerGroup**
> iotHubResourceDeleteEventHubConsumerGroup(apiVersion, subscriptionId, resourceGroupName, resourceName, eventHubEndpointName, name)

Delete a consumer group from an Event Hub-compatible endpoint in an IoT hub.

Delete a consumer group from an Event Hub-compatible endpoint in an IoT hub.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeleteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeleteApi apiInstance = new DeleteApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
    String resourceName = "resourceName_example"; // String | The name of the IoT hub.
    String eventHubEndpointName = "eventHubEndpointName_example"; // String | The name of the Event Hub-compatible endpoint in the IoT hub.
    String name = "name_example"; // String | The name of the consumer group to delete.
    try {
      apiInstance.iotHubResourceDeleteEventHubConsumerGroup(apiVersion, subscriptionId, resourceGroupName, resourceName, eventHubEndpointName, name);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeleteApi#iotHubResourceDeleteEventHubConsumerGroup");
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
| **apiVersion** | **String**| The version of the API. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the IoT hub. | |
| **resourceName** | **String**| The name of the IoT hub. | |
| **eventHubEndpointName** | **String**| The name of the Event Hub-compatible endpoint in the IoT hub. | |
| **name** | **String**| The name of the consumer group to delete. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is a synchronous operation. |  -  |
| **0** | DefaultErrorResponse |  -  |

