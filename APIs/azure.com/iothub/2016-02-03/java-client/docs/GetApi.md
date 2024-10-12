# GetApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**iotHubResourceGet**](GetApi.md#iotHubResourceGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName} | Get the non-security related metadata of an IoT hub. |
| [**iotHubResourceGetEventHubConsumerGroup**](GetApi.md#iotHubResourceGetEventHubConsumerGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/eventHubEndpoints/{eventHubEndpointName}/ConsumerGroups/{name} | Get a consumer group from the Event Hub-compatible device-to-cloud endpoint for an IoT hub. |
| [**iotHubResourceGetJob**](GetApi.md#iotHubResourceGetJob) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/jobs/{jobId} | Get the details of a job from an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry. |
| [**iotHubResourceGetQuotaMetrics**](GetApi.md#iotHubResourceGetQuotaMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/quotaMetrics | Get the quota metrics for an IoT hub. |
| [**iotHubResourceGetStats**](GetApi.md#iotHubResourceGetStats) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/IotHubStats | Get the statistics from an IoT hub. |
| [**iotHubResourceGetValidSkus**](GetApi.md#iotHubResourceGetValidSkus) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/skus | Get the list of valid SKUs for an IoT hub. |
| [**iotHubResourceListByResourceGroup**](GetApi.md#iotHubResourceListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs | Get all the IoT hubs in a resource group. |
| [**iotHubResourceListBySubscription**](GetApi.md#iotHubResourceListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Devices/IotHubs | Get all the IoT hubs in a subscription. |
| [**iotHubResourceListEventHubConsumerGroups**](GetApi.md#iotHubResourceListEventHubConsumerGroups) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/eventHubEndpoints/{eventHubEndpointName}/ConsumerGroups | Get a list of the consumer groups in the Event Hub-compatible device-to-cloud endpoint in an IoT hub. |
| [**iotHubResourceListJobs**](GetApi.md#iotHubResourceListJobs) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/jobs | Get a list of all the jobs in an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry. |


<a id="iotHubResourceGet"></a>
# **iotHubResourceGet**
> IotHubDescription iotHubResourceGet(apiVersion, subscriptionId, resourceGroupName, resourceName)

Get the non-security related metadata of an IoT hub.

Get the non-security related metadata of an IoT hub.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    GetApi apiInstance = new GetApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
    String resourceName = "resourceName_example"; // String | The name of the IoT hub.
    try {
      IotHubDescription result = apiInstance.iotHubResourceGet(apiVersion, subscriptionId, resourceGroupName, resourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetApi#iotHubResourceGet");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The body contains all the non-security properties of the IoT hub. Security-related properties are set to null. |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="iotHubResourceGetEventHubConsumerGroup"></a>
# **iotHubResourceGetEventHubConsumerGroup**
> EventHubConsumerGroupInfo iotHubResourceGetEventHubConsumerGroup(apiVersion, subscriptionId, resourceGroupName, resourceName, eventHubEndpointName, name)

Get a consumer group from the Event Hub-compatible device-to-cloud endpoint for an IoT hub.

Get a consumer group from the Event Hub-compatible device-to-cloud endpoint for an IoT hub.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    GetApi apiInstance = new GetApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
    String resourceName = "resourceName_example"; // String | The name of the IoT hub.
    String eventHubEndpointName = "eventHubEndpointName_example"; // String | The name of the Event Hub-compatible endpoint in the IoT hub.
    String name = "name_example"; // String | The name of the consumer group to retrieve.
    try {
      EventHubConsumerGroupInfo result = apiInstance.iotHubResourceGetEventHubConsumerGroup(apiVersion, subscriptionId, resourceGroupName, resourceName, eventHubEndpointName, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetApi#iotHubResourceGetEventHubConsumerGroup");
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
| **name** | **String**| The name of the consumer group to retrieve. | |

### Return type

[**EventHubConsumerGroupInfo**](EventHubConsumerGroupInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is a synchronous operation. The body contains a JSON-serialized consumer group. |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="iotHubResourceGetJob"></a>
# **iotHubResourceGetJob**
> JobResponse iotHubResourceGetJob(apiVersion, subscriptionId, resourceGroupName, resourceName, jobId)

Get the details of a job from an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry.

Get the details of a job from an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    GetApi apiInstance = new GetApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
    String resourceName = "resourceName_example"; // String | The name of the IoT hub.
    String jobId = "jobId_example"; // String | The job identifier.
    try {
      JobResponse result = apiInstance.iotHubResourceGetJob(apiVersion, subscriptionId, resourceGroupName, resourceName, jobId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetApi#iotHubResourceGetJob");
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
| **jobId** | **String**| The job identifier. | |

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is a synchronous operation. The response contains a JSON-serialized description of the job in the IoT hub. |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="iotHubResourceGetQuotaMetrics"></a>
# **iotHubResourceGetQuotaMetrics**
> IotHubQuotaMetricInfoListResult iotHubResourceGetQuotaMetrics(apiVersion, subscriptionId, resourceGroupName, resourceName)

Get the quota metrics for an IoT hub.

Get the quota metrics for an IoT hub.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    GetApi apiInstance = new GetApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
    String resourceName = "resourceName_example"; // String | The name of the IoT hub.
    try {
      IotHubQuotaMetricInfoListResult result = apiInstance.iotHubResourceGetQuotaMetrics(apiVersion, subscriptionId, resourceGroupName, resourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetApi#iotHubResourceGetQuotaMetrics");
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

[**IotHubQuotaMetricInfoListResult**](IotHubQuotaMetricInfoListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is a synchronous operation. The response contains a JSON-serialized array of the quota metrics for the IoT hub. |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="iotHubResourceGetStats"></a>
# **iotHubResourceGetStats**
> RegistryStatistics iotHubResourceGetStats(apiVersion, subscriptionId, resourceGroupName, resourceName)

Get the statistics from an IoT hub.

Get the statistics from an IoT hub.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    GetApi apiInstance = new GetApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
    String resourceName = "resourceName_example"; // String | The name of the IoT hub.
    try {
      RegistryStatistics result = apiInstance.iotHubResourceGetStats(apiVersion, subscriptionId, resourceGroupName, resourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetApi#iotHubResourceGetStats");
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

[**RegistryStatistics**](RegistryStatistics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is a synchronous operation. The body contains JSON-serialized statistics from the identity registry in the IoT hub. |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="iotHubResourceGetValidSkus"></a>
# **iotHubResourceGetValidSkus**
> IotHubSkuDescriptionListResult iotHubResourceGetValidSkus(apiVersion, subscriptionId, resourceGroupName, resourceName)

Get the list of valid SKUs for an IoT hub.

Get the list of valid SKUs for an IoT hub.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    GetApi apiInstance = new GetApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
    String resourceName = "resourceName_example"; // String | The name of the IoT hub.
    try {
      IotHubSkuDescriptionListResult result = apiInstance.iotHubResourceGetValidSkus(apiVersion, subscriptionId, resourceGroupName, resourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetApi#iotHubResourceGetValidSkus");
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

[**IotHubSkuDescriptionListResult**](IotHubSkuDescriptionListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is a synchronous operation. The body contains a JSON-serialized array of the valid SKUs for this IoT hub. |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="iotHubResourceListByResourceGroup"></a>
# **iotHubResourceListByResourceGroup**
> IotHubDescriptionListResult iotHubResourceListByResourceGroup(apiVersion, subscriptionId, resourceGroupName)

Get all the IoT hubs in a resource group.

Get all the IoT hubs in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    GetApi apiInstance = new GetApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hubs.
    try {
      IotHubDescriptionListResult result = apiInstance.iotHubResourceListByResourceGroup(apiVersion, subscriptionId, resourceGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetApi#iotHubResourceListByResourceGroup");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the IoT hubs. | |

### Return type

[**IotHubDescriptionListResult**](IotHubDescriptionListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is a synchronous operation. The body contains a JSON-serialized array of the metadata from all the IoT hubs in the resource group. |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="iotHubResourceListBySubscription"></a>
# **iotHubResourceListBySubscription**
> IotHubDescriptionListResult iotHubResourceListBySubscription(apiVersion, subscriptionId)

Get all the IoT hubs in a subscription.

Get all the IoT hubs in a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    GetApi apiInstance = new GetApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    try {
      IotHubDescriptionListResult result = apiInstance.iotHubResourceListBySubscription(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetApi#iotHubResourceListBySubscription");
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

### Return type

[**IotHubDescriptionListResult**](IotHubDescriptionListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is a synchronous operation. The body contains a JSON-serialized array of the metadata from all the IoT hubs in the subscription. |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="iotHubResourceListEventHubConsumerGroups"></a>
# **iotHubResourceListEventHubConsumerGroups**
> EventHubConsumerGroupsListResult iotHubResourceListEventHubConsumerGroups(apiVersion, subscriptionId, resourceGroupName, resourceName, eventHubEndpointName)

Get a list of the consumer groups in the Event Hub-compatible device-to-cloud endpoint in an IoT hub.

Get a list of the consumer groups in the Event Hub-compatible device-to-cloud endpoint in an IoT hub.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    GetApi apiInstance = new GetApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
    String resourceName = "resourceName_example"; // String | The name of the IoT hub.
    String eventHubEndpointName = "eventHubEndpointName_example"; // String | The name of the Event Hub-compatible endpoint.
    try {
      EventHubConsumerGroupsListResult result = apiInstance.iotHubResourceListEventHubConsumerGroups(apiVersion, subscriptionId, resourceGroupName, resourceName, eventHubEndpointName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetApi#iotHubResourceListEventHubConsumerGroups");
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
| **eventHubEndpointName** | **String**| The name of the Event Hub-compatible endpoint. | |

### Return type

[**EventHubConsumerGroupsListResult**](EventHubConsumerGroupsListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is a synchronous operation. The body contains a JSON-serialized list of the consumer groups in the Event Hub-compatible endpoint in this IoT hub |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="iotHubResourceListJobs"></a>
# **iotHubResourceListJobs**
> JobResponseListResult iotHubResourceListJobs(apiVersion, subscriptionId, resourceGroupName, resourceName)

Get a list of all the jobs in an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry.

Get a list of all the jobs in an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    GetApi apiInstance = new GetApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
    String resourceName = "resourceName_example"; // String | The name of the IoT hub.
    try {
      JobResponseListResult result = apiInstance.iotHubResourceListJobs(apiVersion, subscriptionId, resourceGroupName, resourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetApi#iotHubResourceListJobs");
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

[**JobResponseListResult**](JobResponseListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is a synchronous operation. The response contains a JSON-serialized array of all the jobs in the IoT hub. |  -  |
| **0** | DefaultErrorResponse |  -  |

