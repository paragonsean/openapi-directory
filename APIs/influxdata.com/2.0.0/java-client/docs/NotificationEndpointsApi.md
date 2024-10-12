# NotificationEndpointsApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNotificationEndpoint**](NotificationEndpointsApi.md#createNotificationEndpoint) | **POST** /notificationEndpoints | Add a notification endpoint |
| [**deleteNotificationEndpointsID**](NotificationEndpointsApi.md#deleteNotificationEndpointsID) | **DELETE** /notificationEndpoints/{endpointID} | Delete a notification endpoint |
| [**deleteNotificationEndpointsIDLabelsID**](NotificationEndpointsApi.md#deleteNotificationEndpointsIDLabelsID) | **DELETE** /notificationEndpoints/{endpointID}/labels/{labelID} | Delete a label from a notification endpoint |
| [**getNotificationEndpoints**](NotificationEndpointsApi.md#getNotificationEndpoints) | **GET** /notificationEndpoints | List all notification endpoints |
| [**getNotificationEndpointsID**](NotificationEndpointsApi.md#getNotificationEndpointsID) | **GET** /notificationEndpoints/{endpointID} | Retrieve a notification endpoint |
| [**getNotificationEndpointsIDLabels**](NotificationEndpointsApi.md#getNotificationEndpointsIDLabels) | **GET** /notificationEndpoints/{endpointID}/labels | List all labels for a notification endpoint |
| [**patchNotificationEndpointsID**](NotificationEndpointsApi.md#patchNotificationEndpointsID) | **PATCH** /notificationEndpoints/{endpointID} | Update a notification endpoint |
| [**postNotificationEndpointIDLabels**](NotificationEndpointsApi.md#postNotificationEndpointIDLabels) | **POST** /notificationEndpoints/{endpointID}/labels | Add a label to a notification endpoint |
| [**putNotificationEndpointsID**](NotificationEndpointsApi.md#putNotificationEndpointsID) | **PUT** /notificationEndpoints/{endpointID} | Update a notification endpoint |


<a id="createNotificationEndpoint"></a>
# **createNotificationEndpoint**
> NotificationEndpoint createNotificationEndpoint(postNotificationEndpoint)

Add a notification endpoint

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationEndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    NotificationEndpointsApi apiInstance = new NotificationEndpointsApi(defaultClient);
    PostNotificationEndpoint postNotificationEndpoint = new PostNotificationEndpoint(); // PostNotificationEndpoint | Notification endpoint to create
    try {
      NotificationEndpoint result = apiInstance.createNotificationEndpoint(postNotificationEndpoint);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationEndpointsApi#createNotificationEndpoint");
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
| **postNotificationEndpoint** | [**PostNotificationEndpoint**](PostNotificationEndpoint.md)| Notification endpoint to create | |

### Return type

[**NotificationEndpoint**](NotificationEndpoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Notification endpoint created |  -  |
| **0** | Unexpected error |  -  |

<a id="deleteNotificationEndpointsID"></a>
# **deleteNotificationEndpointsID**
> deleteNotificationEndpointsID(endpointID, zapTraceSpan)

Delete a notification endpoint

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationEndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    NotificationEndpointsApi apiInstance = new NotificationEndpointsApi(defaultClient);
    String endpointID = "endpointID_example"; // String | The notification endpoint ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteNotificationEndpointsID(endpointID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationEndpointsApi#deleteNotificationEndpointsID");
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
| **endpointID** | **String**| The notification endpoint ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Delete has been accepted |  -  |
| **404** | The endpoint was not found |  -  |
| **0** | Unexpected error |  -  |

<a id="deleteNotificationEndpointsIDLabelsID"></a>
# **deleteNotificationEndpointsIDLabelsID**
> deleteNotificationEndpointsIDLabelsID(endpointID, labelID, zapTraceSpan)

Delete a label from a notification endpoint

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationEndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    NotificationEndpointsApi apiInstance = new NotificationEndpointsApi(defaultClient);
    String endpointID = "endpointID_example"; // String | The notification endpoint ID.
    String labelID = "labelID_example"; // String | The ID of the label to delete.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteNotificationEndpointsIDLabelsID(endpointID, labelID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationEndpointsApi#deleteNotificationEndpointsIDLabelsID");
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
| **endpointID** | **String**| The notification endpoint ID. | |
| **labelID** | **String**| The ID of the label to delete. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Delete has been accepted |  -  |
| **404** | Endpoint or label not found |  -  |
| **0** | Unexpected error |  -  |

<a id="getNotificationEndpoints"></a>
# **getNotificationEndpoints**
> NotificationEndpoints getNotificationEndpoints(orgID, zapTraceSpan, offset, limit)

List all notification endpoints

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationEndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    NotificationEndpointsApi apiInstance = new NotificationEndpointsApi(defaultClient);
    String orgID = "orgID_example"; // String | Only show notification endpoints that belong to specific organization ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    Integer offset = 56; // Integer | 
    Integer limit = 20; // Integer | 
    try {
      NotificationEndpoints result = apiInstance.getNotificationEndpoints(orgID, zapTraceSpan, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationEndpointsApi#getNotificationEndpoints");
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
| **orgID** | **String**| Only show notification endpoints that belong to specific organization ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |
| **offset** | **Integer**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 20] |

### Return type

[**NotificationEndpoints**](NotificationEndpoints.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of notification endpoints |  -  |
| **0** | Unexpected error |  -  |

<a id="getNotificationEndpointsID"></a>
# **getNotificationEndpointsID**
> NotificationEndpoint getNotificationEndpointsID(endpointID, zapTraceSpan)

Retrieve a notification endpoint

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationEndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    NotificationEndpointsApi apiInstance = new NotificationEndpointsApi(defaultClient);
    String endpointID = "endpointID_example"; // String | The notification endpoint ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      NotificationEndpoint result = apiInstance.getNotificationEndpointsID(endpointID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationEndpointsApi#getNotificationEndpointsID");
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
| **endpointID** | **String**| The notification endpoint ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**NotificationEndpoint**](NotificationEndpoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The notification endpoint requested |  -  |
| **0** | Unexpected error |  -  |

<a id="getNotificationEndpointsIDLabels"></a>
# **getNotificationEndpointsIDLabels**
> LabelsResponse getNotificationEndpointsIDLabels(endpointID, zapTraceSpan)

List all labels for a notification endpoint

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationEndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    NotificationEndpointsApi apiInstance = new NotificationEndpointsApi(defaultClient);
    String endpointID = "endpointID_example"; // String | The notification endpoint ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      LabelsResponse result = apiInstance.getNotificationEndpointsIDLabels(endpointID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationEndpointsApi#getNotificationEndpointsIDLabels");
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
| **endpointID** | **String**| The notification endpoint ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**LabelsResponse**](LabelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of all labels for a notification endpoint |  -  |
| **0** | Unexpected error |  -  |

<a id="patchNotificationEndpointsID"></a>
# **patchNotificationEndpointsID**
> NotificationEndpoint patchNotificationEndpointsID(endpointID, notificationEndpointUpdate, zapTraceSpan)

Update a notification endpoint

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationEndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    NotificationEndpointsApi apiInstance = new NotificationEndpointsApi(defaultClient);
    String endpointID = "endpointID_example"; // String | The notification endpoint ID.
    NotificationEndpointUpdate notificationEndpointUpdate = new NotificationEndpointUpdate(); // NotificationEndpointUpdate | Check update to apply
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      NotificationEndpoint result = apiInstance.patchNotificationEndpointsID(endpointID, notificationEndpointUpdate, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationEndpointsApi#patchNotificationEndpointsID");
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
| **endpointID** | **String**| The notification endpoint ID. | |
| **notificationEndpointUpdate** | [**NotificationEndpointUpdate**](NotificationEndpointUpdate.md)| Check update to apply | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**NotificationEndpoint**](NotificationEndpoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An updated notification endpoint |  -  |
| **404** | The notification endpoint was not found |  -  |
| **0** | Unexpected error |  -  |

<a id="postNotificationEndpointIDLabels"></a>
# **postNotificationEndpointIDLabels**
> LabelResponse postNotificationEndpointIDLabels(endpointID, labelMapping, zapTraceSpan)

Add a label to a notification endpoint

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationEndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    NotificationEndpointsApi apiInstance = new NotificationEndpointsApi(defaultClient);
    String endpointID = "endpointID_example"; // String | The notification endpoint ID.
    LabelMapping labelMapping = new LabelMapping(); // LabelMapping | Label to add
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      LabelResponse result = apiInstance.postNotificationEndpointIDLabels(endpointID, labelMapping, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationEndpointsApi#postNotificationEndpointIDLabels");
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
| **endpointID** | **String**| The notification endpoint ID. | |
| **labelMapping** | [**LabelMapping**](LabelMapping.md)| Label to add | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**LabelResponse**](LabelResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The label was added to the notification endpoint |  -  |
| **0** | Unexpected error |  -  |

<a id="putNotificationEndpointsID"></a>
# **putNotificationEndpointsID**
> NotificationEndpoint putNotificationEndpointsID(endpointID, notificationEndpoint, zapTraceSpan)

Update a notification endpoint

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationEndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    NotificationEndpointsApi apiInstance = new NotificationEndpointsApi(defaultClient);
    String endpointID = "endpointID_example"; // String | The notification endpoint ID.
    NotificationEndpoint notificationEndpoint = new NotificationEndpoint(); // NotificationEndpoint | A new notification endpoint to replace the existing endpoint with
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      NotificationEndpoint result = apiInstance.putNotificationEndpointsID(endpointID, notificationEndpoint, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationEndpointsApi#putNotificationEndpointsID");
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
| **endpointID** | **String**| The notification endpoint ID. | |
| **notificationEndpoint** | [**NotificationEndpoint**](NotificationEndpoint.md)| A new notification endpoint to replace the existing endpoint with | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**NotificationEndpoint**](NotificationEndpoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An updated notification endpoint |  -  |
| **404** | The notification endpoint was not found |  -  |
| **0** | Unexpected error |  -  |

