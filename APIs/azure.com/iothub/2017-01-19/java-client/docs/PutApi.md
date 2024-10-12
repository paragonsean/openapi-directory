# PutApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**iotHubResourceCreateEventHubConsumerGroup**](PutApi.md#iotHubResourceCreateEventHubConsumerGroup) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/eventHubEndpoints/{eventHubEndpointName}/ConsumerGroups/{name} | Add a consumer group to an Event Hub-compatible endpoint in an IoT hub. |
| [**iotHubResourceCreateOrUpdate**](PutApi.md#iotHubResourceCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName} | Create or update the metadata of an IoT hub. |


<a id="iotHubResourceCreateEventHubConsumerGroup"></a>
# **iotHubResourceCreateEventHubConsumerGroup**
> EventHubConsumerGroupInfo iotHubResourceCreateEventHubConsumerGroup(apiVersion, subscriptionId, resourceGroupName, resourceName, eventHubEndpointName, name)

Add a consumer group to an Event Hub-compatible endpoint in an IoT hub.

Add a consumer group to an Event Hub-compatible endpoint in an IoT hub.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PutApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    PutApi apiInstance = new PutApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
    String resourceName = "resourceName_example"; // String | The name of the IoT hub.
    String eventHubEndpointName = "eventHubEndpointName_example"; // String | The name of the Event Hub-compatible endpoint in the IoT hub.
    String name = "name_example"; // String | The name of the consumer group to add.
    try {
      EventHubConsumerGroupInfo result = apiInstance.iotHubResourceCreateEventHubConsumerGroup(apiVersion, subscriptionId, resourceGroupName, resourceName, eventHubEndpointName, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PutApi#iotHubResourceCreateEventHubConsumerGroup");
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
| **name** | **String**| The name of the consumer group to add. | |

### Return type

[**EventHubConsumerGroupInfo**](EventHubConsumerGroupInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is a synchronous operation. |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="iotHubResourceCreateOrUpdate"></a>
# **iotHubResourceCreateOrUpdate**
> IotHubDescription iotHubResourceCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, iotHubDescription)

Create or update the metadata of an IoT hub.

Create or update the metadata of an Iot hub. The usual pattern to modify a property is to retrieve the IoT hub metadata and security metadata, and then combine them with the modified values in a new body to update the IoT hub.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PutApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    PutApi apiInstance = new PutApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
    String resourceName = "resourceName_example"; // String | The name of the IoT hub to create or update.
    IotHubDescription iotHubDescription = new IotHubDescription(); // IotHubDescription | The IoT hub metadata and security metadata.
    try {
      IotHubDescription result = apiInstance.iotHubResourceCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, iotHubDescription);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PutApi#iotHubResourceCreateOrUpdate");
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
| **resourceName** | **String**| The name of the IoT hub to create or update. | |
| **iotHubDescription** | [**IotHubDescription**](IotHubDescription.md)| The IoT hub metadata and security metadata. | |

### Return type

[**IotHubDescription**](IotHubDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is returned as a response to the status polling request for the create or update operation. The body contains the resource representation that indicates a transitional provisioning state. |  -  |
| **201** | This is a long running operation. The operation returns a 201 if the validation is complete. The response includes an Azure-AsyncOperation header that contains a status URL. Clients are expected to poll the status URL for the status of the operation. If successful, the operation returns HTTP status code of 201 (OK). |  -  |
| **0** | DefaultErrorResponse |  -  |

