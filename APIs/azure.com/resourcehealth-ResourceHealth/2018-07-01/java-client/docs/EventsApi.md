# EventsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**eventsListBySingleResource**](EventsApi.md#eventsListBySingleResource) | **GET** /{resourceUri}/providers/Microsoft.ResourceHealth/events |  |
| [**eventsListBySubscriptionId**](EventsApi.md#eventsListBySubscriptionId) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ResourceHealth/events |  |


<a id="eventsListBySingleResource"></a>
# **eventsListBySingleResource**
> Events eventsListBySingleResource(resourceUri, apiVersion, $filter, view)



Lists current service health events for given resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String resourceUri = "resourceUri_example"; // String | The fully qualified ID of the resource, including the resource name and resource type. Currently the API support not nested and one nesting level resource types : /subscriptions/{subscriptionId}/resourceGroups/{resource-group-name}/providers/{resource-provider-name}/{resource-type}/{resource-name} and /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resource-provider-name}/{parentResourceType}/{parentResourceName}/{resourceType}/{resourceName}
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom=MSDN
    String view = "view_example"; // String | setting view=full expands the article parameters
    try {
      Events result = apiInstance.eventsListBySingleResource(resourceUri, apiVersion, $filter, view);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#eventsListBySingleResource");
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
| **resourceUri** | **String**| The fully qualified ID of the resource, including the resource name and resource type. Currently the API support not nested and one nesting level resource types : /subscriptions/{subscriptionId}/resourceGroups/{resource-group-name}/providers/{resource-provider-name}/{resource-type}/{resource-name} and /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resource-provider-name}/{parentResourceType}/{parentResourceName}/{resourceType}/{resourceName} | |
| **apiVersion** | **String**| Client Api Version. | |
| **$filter** | **String**| The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom&#x3D;MSDN | [optional] |
| **view** | **String**| setting view&#x3D;full expands the article parameters | [optional] |

### Return type

[**Events**](Events.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of current service health events for given resource |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="eventsListBySubscriptionId"></a>
# **eventsListBySubscriptionId**
> Events eventsListBySubscriptionId(apiVersion, subscriptionId, $filter, view)



Lists current service health events in the subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom=MSDN
    String view = "view_example"; // String | setting view=full expands the article parameters
    try {
      Events result = apiInstance.eventsListBySubscriptionId(apiVersion, subscriptionId, $filter, view);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#eventsListBySubscriptionId");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$filter** | **String**| The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom&#x3D;MSDN | [optional] |
| **view** | **String**| setting view&#x3D;full expands the article parameters | [optional] |

### Return type

[**Events**](Events.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of current service health events in the subscription |  -  |
| **0** | DefaultErrorResponse |  -  |

