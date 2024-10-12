# TopicTypesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**topicTypesGet**](TopicTypesApi.md#topicTypesGet) | **GET** /providers/Microsoft.EventGrid/topicTypes/{topicTypeName} | Get a topic type |
| [**topicTypesList**](TopicTypesApi.md#topicTypesList) | **GET** /providers/Microsoft.EventGrid/topicTypes | List topic types |
| [**topicTypesListEventTypes**](TopicTypesApi.md#topicTypesListEventTypes) | **GET** /providers/Microsoft.EventGrid/topicTypes/{topicTypeName}/eventTypes | List event types |


<a id="topicTypesGet"></a>
# **topicTypesGet**
> TopicTypeInfo topicTypesGet(topicTypeName, apiVersion)

Get a topic type

Get information about a topic type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    TopicTypesApi apiInstance = new TopicTypesApi(defaultClient);
    String topicTypeName = "topicTypeName_example"; // String | Name of the topic type
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      TopicTypeInfo result = apiInstance.topicTypesGet(topicTypeName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopicTypesApi#topicTypesGet");
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
| **topicTypeName** | **String**| Name of the topic type | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

[**TopicTypeInfo**](TopicTypeInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | *** Error Responses: ***   * 400 Bad Request.   * 404 Not Found.   * 500 Internal Server Error. |  -  |

<a id="topicTypesList"></a>
# **topicTypesList**
> TopicTypesListResult topicTypesList(apiVersion)

List topic types

List all registered topic types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    TopicTypesApi apiInstance = new TopicTypesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      TopicTypesListResult result = apiInstance.topicTypesList(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopicTypesApi#topicTypesList");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

[**TopicTypesListResult**](TopicTypesListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | *** Error Responses: ***   * 400 Bad Request.   * 404 Not Found.   * 500 Internal Server Error. |  -  |

<a id="topicTypesListEventTypes"></a>
# **topicTypesListEventTypes**
> EventTypesListResult topicTypesListEventTypes(topicTypeName, apiVersion)

List event types

List event types for a topic type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    TopicTypesApi apiInstance = new TopicTypesApi(defaultClient);
    String topicTypeName = "topicTypeName_example"; // String | Name of the topic type
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      EventTypesListResult result = apiInstance.topicTypesListEventTypes(topicTypeName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopicTypesApi#topicTypesListEventTypes");
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
| **topicTypeName** | **String**| Name of the topic type | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

[**EventTypesListResult**](EventTypesListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | *** Error Responses: ***   * 400 Bad Request.   * 404 Not Found.   * 500 Internal Server Error. |  -  |

