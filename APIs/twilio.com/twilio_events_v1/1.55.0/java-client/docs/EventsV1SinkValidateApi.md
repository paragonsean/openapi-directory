# EventsV1SinkValidateApi

All URIs are relative to *https://events.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSinkValidate**](EventsV1SinkValidateApi.md#createSinkValidate) | **POST** /v1/Sinks/{Sid}/Validate |  |


<a id="createSinkValidate"></a>
# **createSinkValidate**
> EventsV1SinkSinkValidate createSinkValidate(sid, testId)



Validate that a test event for a Sink was received.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsV1SinkValidateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://events.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    EventsV1SinkValidateApi apiInstance = new EventsV1SinkValidateApi(defaultClient);
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies the Sink being validated.
    String testId = "testId_example"; // String | A 34 character string that uniquely identifies the test event for a Sink being validated.
    try {
      EventsV1SinkSinkValidate result = apiInstance.createSinkValidate(sid, testId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsV1SinkValidateApi#createSinkValidate");
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
| **sid** | **String**| A 34 character string that uniquely identifies the Sink being validated. | |
| **testId** | **String**| A 34 character string that uniquely identifies the test event for a Sink being validated. | |

### Return type

[**EventsV1SinkSinkValidate**](EventsV1SinkSinkValidate.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

