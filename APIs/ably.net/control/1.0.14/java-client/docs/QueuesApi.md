# QueuesApi

All URIs are relative to *https://control.ably.net/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appsAppIdQueuesGet**](QueuesApi.md#appsAppIdQueuesGet) | **GET** /apps/{app_id}/queues | Lists queues |
| [**appsAppIdQueuesPost**](QueuesApi.md#appsAppIdQueuesPost) | **POST** /apps/{app_id}/queues | Creates a queue |
| [**appsAppIdQueuesQueueIdDelete**](QueuesApi.md#appsAppIdQueuesQueueIdDelete) | **DELETE** /apps/{app_id}/queues/{queue_id} | Deletes a queue |


<a id="appsAppIdQueuesGet"></a>
# **appsAppIdQueuesGet**
> List&lt;QueueResponse&gt; appsAppIdQueuesGet(appId)

Lists queues

Lists the queues associated with the specified application ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://control.ably.net/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    QueuesApi apiInstance = new QueuesApi(defaultClient);
    String appId = "appId_example"; // String | The application ID.
    try {
      List<QueueResponse> result = apiInstance.appsAppIdQueuesGet(appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueuesApi#appsAppIdQueuesGet");
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
| **appId** | **String**| The application ID. | |

### Return type

[**List&lt;QueueResponse&gt;**](QueueResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Queue list |  -  |
| **401** | Authentication failed |  -  |
| **404** | App not found |  -  |
| **500** | Internal server error |  -  |
| **503** | 503 Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

<a id="appsAppIdQueuesPost"></a>
# **appsAppIdQueuesPost**
> QueueResponse appsAppIdQueuesPost(appId, queue)

Creates a queue

Creates a queue for the application specified by application ID. The properties for the queue to be created are specified in the request body.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://control.ably.net/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    QueuesApi apiInstance = new QueuesApi(defaultClient);
    String appId = "appId_example"; // String | The application ID.
    Queue queue = new Queue(); // Queue | 
    try {
      QueueResponse result = apiInstance.appsAppIdQueuesPost(appId, queue);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueuesApi#appsAppIdQueuesPost");
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
| **appId** | **String**| The application ID. | |
| **queue** | [**Queue**](Queue.md)|  | [optional] |

### Return type

[**QueueResponse**](QueueResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Queue created |  -  |
| **400** | Bad request |  -  |
| **401** | Authentication failed |  -  |
| **404** | App not found |  -  |
| **422** | Invalid request |  -  |
| **500** | Internal server error |  -  |

<a id="appsAppIdQueuesQueueIdDelete"></a>
# **appsAppIdQueuesQueueIdDelete**
> appsAppIdQueuesQueueIdDelete(appId, queueId)

Deletes a queue

Delete the queue with the specified queue name, from the application with the specified application ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://control.ably.net/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    QueuesApi apiInstance = new QueuesApi(defaultClient);
    String appId = "appId_example"; // String | The application ID.
    String queueId = "queueId_example"; // String | The queue ID.
    try {
      apiInstance.appsAppIdQueuesQueueIdDelete(appId, queueId);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueuesApi#appsAppIdQueuesQueueIdDelete");
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
| **appId** | **String**| The application ID. | |
| **queueId** | **String**| The queue ID. | |

### Return type

null (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Queue deleted |  -  |
| **400** | Bad request |  -  |
| **401** | Authentication failed |  -  |
| **404** | App not found |  -  |
| **500** | Internal server error |  -  |
| **503** | 503 Service unavailable |  -  |

