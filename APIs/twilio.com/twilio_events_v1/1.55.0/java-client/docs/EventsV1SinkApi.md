# EventsV1SinkApi

All URIs are relative to *https://events.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSink**](EventsV1SinkApi.md#createSink) | **POST** /v1/Sinks |  |
| [**deleteSink**](EventsV1SinkApi.md#deleteSink) | **DELETE** /v1/Sinks/{Sid} |  |
| [**fetchSink**](EventsV1SinkApi.md#fetchSink) | **GET** /v1/Sinks/{Sid} |  |
| [**listSink**](EventsV1SinkApi.md#listSink) | **GET** /v1/Sinks |  |
| [**updateSink**](EventsV1SinkApi.md#updateSink) | **POST** /v1/Sinks/{Sid} |  |


<a id="createSink"></a>
# **createSink**
> EventsV1Sink createSink(description, sinkConfiguration, sinkType)



Create a new Sink

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsV1SinkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://events.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    EventsV1SinkApi apiInstance = new EventsV1SinkApi(defaultClient);
    String description = "description_example"; // String | A human readable description for the Sink **This value should not contain PII.**
    Object sinkConfiguration = null; // Object | The information required for Twilio to connect to the provided Sink encoded as JSON.
    SinkEnumSinkType sinkType = SinkEnumSinkType.fromValue("kinesis"); // SinkEnumSinkType | 
    try {
      EventsV1Sink result = apiInstance.createSink(description, sinkConfiguration, sinkType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsV1SinkApi#createSink");
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
| **description** | **String**| A human readable description for the Sink **This value should not contain PII.** | |
| **sinkConfiguration** | [**Object**](Object.md)| The information required for Twilio to connect to the provided Sink encoded as JSON. | |
| **sinkType** | **SinkEnumSinkType**|  | [enum: kinesis, webhook, segment] |

### Return type

[**EventsV1Sink**](EventsV1Sink.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteSink"></a>
# **deleteSink**
> deleteSink(sid)



Delete a specific Sink.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsV1SinkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://events.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    EventsV1SinkApi apiInstance = new EventsV1SinkApi(defaultClient);
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this Sink.
    try {
      apiInstance.deleteSink(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsV1SinkApi#deleteSink");
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
| **sid** | **String**| A 34 character string that uniquely identifies this Sink. | |

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The resource was deleted successfully. |  -  |

<a id="fetchSink"></a>
# **fetchSink**
> EventsV1Sink fetchSink(sid)



Fetch a specific Sink.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsV1SinkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://events.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    EventsV1SinkApi apiInstance = new EventsV1SinkApi(defaultClient);
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this Sink.
    try {
      EventsV1Sink result = apiInstance.fetchSink(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsV1SinkApi#fetchSink");
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
| **sid** | **String**| A 34 character string that uniquely identifies this Sink. | |

### Return type

[**EventsV1Sink**](EventsV1Sink.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listSink"></a>
# **listSink**
> ListSinkResponse listSink(inUse, status, pageSize, page, pageToken)



Retrieve a paginated list of Sinks belonging to the account used to make the request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsV1SinkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://events.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    EventsV1SinkApi apiInstance = new EventsV1SinkApi(defaultClient);
    Boolean inUse = true; // Boolean | A boolean query parameter filtering the results to return sinks used/not used by a subscription.
    String status = "status_example"; // String | A String query parameter filtering the results by status `initialized`, `validating`, `active` or `failed`.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListSinkResponse result = apiInstance.listSink(inUse, status, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsV1SinkApi#listSink");
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
| **inUse** | **Boolean**| A boolean query parameter filtering the results to return sinks used/not used by a subscription. | [optional] |
| **status** | **String**| A String query parameter filtering the results by status &#x60;initialized&#x60;, &#x60;validating&#x60;, &#x60;active&#x60; or &#x60;failed&#x60;. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListSinkResponse**](ListSinkResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateSink"></a>
# **updateSink**
> EventsV1Sink updateSink(sid, description)



Update a specific Sink

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsV1SinkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://events.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    EventsV1SinkApi apiInstance = new EventsV1SinkApi(defaultClient);
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this Sink.
    String description = "description_example"; // String | A human readable description for the Sink **This value should not contain PII.**
    try {
      EventsV1Sink result = apiInstance.updateSink(sid, description);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsV1SinkApi#updateSink");
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
| **sid** | **String**| A 34 character string that uniquely identifies this Sink. | |
| **description** | **String**| A human readable description for the Sink **This value should not contain PII.** | |

### Return type

[**EventsV1Sink**](EventsV1Sink.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

