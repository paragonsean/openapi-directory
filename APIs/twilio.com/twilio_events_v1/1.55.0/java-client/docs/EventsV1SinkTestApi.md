# EventsV1SinkTestApi

All URIs are relative to *https://events.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSinkTest**](EventsV1SinkTestApi.md#createSinkTest) | **POST** /v1/Sinks/{Sid}/Test |  |


<a id="createSinkTest"></a>
# **createSinkTest**
> EventsV1SinkSinkTest createSinkTest(sid)



Create a new Sink Test Event for the given Sink.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsV1SinkTestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://events.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    EventsV1SinkTestApi apiInstance = new EventsV1SinkTestApi(defaultClient);
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies the Sink to be Tested.
    try {
      EventsV1SinkSinkTest result = apiInstance.createSinkTest(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsV1SinkTestApi#createSinkTest");
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
| **sid** | **String**| A 34 character string that uniquely identifies the Sink to be Tested. | |

### Return type

[**EventsV1SinkSinkTest**](EventsV1SinkSinkTest.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

