# SubscriptionUsagesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**subscriptionUsagesGet**](SubscriptionUsagesApi.md#subscriptionUsagesGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationName}/usages/{usageName} |  |
| [**subscriptionUsagesListByLocation**](SubscriptionUsagesApi.md#subscriptionUsagesListByLocation) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationName}/usages |  |


<a id="subscriptionUsagesGet"></a>
# **subscriptionUsagesGet**
> SubscriptionUsage subscriptionUsagesGet(locationName, usageName, subscriptionId, apiVersion)



Gets a subscription usage metric.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionUsagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    SubscriptionUsagesApi apiInstance = new SubscriptionUsagesApi(defaultClient);
    String locationName = "locationName_example"; // String | The name of the region where the resource is located.
    String usageName = "usageName_example"; // String | Name of usage metric to return.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      SubscriptionUsage result = apiInstance.subscriptionUsagesGet(locationName, usageName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionUsagesApi#subscriptionUsagesGet");
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
| **locationName** | **String**| The name of the region where the resource is located. | |
| **usageName** | **String**| Name of usage metric to return. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**SubscriptionUsage**](SubscriptionUsage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved particular subscription location usage. |  -  |
| **0** | *** Error Responses: ***   * 400 SubscriptionNotFound - The requested subscription was not found.   * 400 InvalidLocation - An invalid location was specified. |  -  |

<a id="subscriptionUsagesListByLocation"></a>
# **subscriptionUsagesListByLocation**
> SubscriptionUsageListResult subscriptionUsagesListByLocation(locationName, subscriptionId, apiVersion)



Gets all subscription usage metrics in a given location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionUsagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    SubscriptionUsagesApi apiInstance = new SubscriptionUsagesApi(defaultClient);
    String locationName = "locationName_example"; // String | The name of the region where the resource is located.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      SubscriptionUsageListResult result = apiInstance.subscriptionUsagesListByLocation(locationName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionUsagesApi#subscriptionUsagesListByLocation");
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
| **locationName** | **String**| The name of the region where the resource is located. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**SubscriptionUsageListResult**](SubscriptionUsageListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the subscription location usages. |  -  |
| **0** | *** Error Responses: ***   * 400 SubscriptionNotFound - The requested subscription was not found.   * 400 InvalidLocation - An invalid location was specified. |  -  |

