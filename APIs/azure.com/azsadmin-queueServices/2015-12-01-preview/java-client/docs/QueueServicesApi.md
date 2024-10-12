# QueueServicesApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**queueServicesGet**](QueueServicesApi.md#queueServicesGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/queueservices/{serviceType} |  |
| [**queueServicesListMetricDefinitions**](QueueServicesApi.md#queueServicesListMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/queueservices/{serviceType}/metricdefinitions |  |
| [**queueServicesListMetrics**](QueueServicesApi.md#queueServicesListMetrics) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/queueservices/{serviceType}/metrics |  |


<a id="queueServicesGet"></a>
# **queueServicesGet**
> QueueService queueServicesGet(subscriptionId, resourceGroupName, farmId, serviceType, apiVersion)



Returns the queue service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueueServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    QueueServicesApi apiInstance = new QueueServicesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String farmId = "farmId_example"; // String | Farm Id.
    String serviceType = "default"; // String | The service type.
    String apiVersion = "apiVersion_example"; // String | REST Api Version.
    try {
      QueueService result = apiInstance.queueServicesGet(subscriptionId, resourceGroupName, farmId, serviceType, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueueServicesApi#queueServicesGet");
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
| **serviceType** | **String**| The service type. | [enum: default] |
| **apiVersion** | **String**| REST Api Version. | |

### Return type

[**QueueService**](QueueService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Queue service has been returned. |  -  |
| **404** | NOT FOUND -- The specified farm was not found. |  -  |

<a id="queueServicesListMetricDefinitions"></a>
# **queueServicesListMetricDefinitions**
> QueueServicesListMetricDefinitions200Response queueServicesListMetricDefinitions(subscriptionId, resourceGroupName, farmId, serviceType, apiVersion)



Returns a list of metric definitions for queue service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueueServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    QueueServicesApi apiInstance = new QueueServicesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String farmId = "farmId_example"; // String | Farm Id.
    String serviceType = "default"; // String | The service type.
    String apiVersion = "apiVersion_example"; // String | REST Api Version.
    try {
      QueueServicesListMetricDefinitions200Response result = apiInstance.queueServicesListMetricDefinitions(subscriptionId, resourceGroupName, farmId, serviceType, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueueServicesApi#queueServicesListMetricDefinitions");
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
| **serviceType** | **String**| The service type. | [enum: default] |
| **apiVersion** | **String**| REST Api Version. | |

### Return type

[**QueueServicesListMetricDefinitions200Response**](QueueServicesListMetricDefinitions200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- The list of metric definitions has been returned. |  -  |
| **404** | NOT FOUND -- The specified farm was not found. |  -  |

<a id="queueServicesListMetrics"></a>
# **queueServicesListMetrics**
> QueueServicesListMetrics200Response queueServicesListMetrics(subscriptionId, resourceGroupName, farmId, serviceType, apiVersion)



Returns a list of metrics for the queue service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueueServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    QueueServicesApi apiInstance = new QueueServicesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String farmId = "farmId_example"; // String | Farm Id.
    String serviceType = "default"; // String | The service type.
    String apiVersion = "apiVersion_example"; // String | REST Api Version.
    try {
      QueueServicesListMetrics200Response result = apiInstance.queueServicesListMetrics(subscriptionId, resourceGroupName, farmId, serviceType, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueueServicesApi#queueServicesListMetrics");
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
| **serviceType** | **String**| The service type. | [enum: default] |
| **apiVersion** | **String**| REST Api Version. | |

### Return type

[**QueueServicesListMetrics200Response**](QueueServicesListMetrics200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- The list of metrics has been returned. |  -  |
| **404** | NOT FOUND -- The specified farm was not found. |  -  |

