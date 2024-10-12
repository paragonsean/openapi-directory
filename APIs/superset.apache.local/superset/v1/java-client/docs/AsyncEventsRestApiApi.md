# AsyncEventsRestApiApi

All URIs are relative to *http://superset.apache.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**asyncEventGet**](AsyncEventsRestApiApi.md#asyncEventGet) | **GET** /async_event/ |  |


<a id="asyncEventGet"></a>
# **asyncEventGet**
> AsyncEventGet200Response asyncEventGet(lastId)



Reads off of the Redis events stream, using the user&#39;s JWT token and optional query params for last event received.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AsyncEventsRestApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    AsyncEventsRestApiApi apiInstance = new AsyncEventsRestApiApi(defaultClient);
    String lastId = "lastId_example"; // String | Last ID received by the client
    try {
      AsyncEventGet200Response result = apiInstance.asyncEventGet(lastId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AsyncEventsRestApiApi#asyncEventGet");
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
| **lastId** | **String**| Last ID received by the client | [optional] |

### Return type

[**AsyncEventGet200Response**](AsyncEventGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Async event results |  -  |
| **401** | Unauthorized |  -  |
| **500** | Fatal error |  -  |

