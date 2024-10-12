# SyncV1StreamMessageApi

All URIs are relative to *https://sync.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createStreamMessage**](SyncV1StreamMessageApi.md#createStreamMessage) | **POST** /v1/Services/{ServiceSid}/Streams/{StreamSid}/Messages |  |


<a id="createStreamMessage"></a>
# **createStreamMessage**
> SyncV1ServiceSyncStreamStreamMessage createStreamMessage(serviceSid, streamSid, data)



Create a new Stream Message.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncV1StreamMessageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sync.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SyncV1StreamMessageApi apiInstance = new SyncV1StreamMessageApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) to create the new Stream Message in.
    String streamSid = "streamSid_example"; // String | The SID of the Sync Stream to create the new Stream Message resource for.
    Object data = null; // Object | A JSON string that represents an arbitrary, schema-less object that makes up the Stream Message body. Can be up to 4 KiB in length.
    try {
      SyncV1ServiceSyncStreamStreamMessage result = apiInstance.createStreamMessage(serviceSid, streamSid, data);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncV1StreamMessageApi#createStreamMessage");
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
| **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) to create the new Stream Message in. | |
| **streamSid** | **String**| The SID of the Sync Stream to create the new Stream Message resource for. | |
| **data** | [**Object**](Object.md)| A JSON string that represents an arbitrary, schema-less object that makes up the Stream Message body. Can be up to 4 KiB in length. | |

### Return type

[**SyncV1ServiceSyncStreamStreamMessage**](SyncV1ServiceSyncStreamStreamMessage.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

