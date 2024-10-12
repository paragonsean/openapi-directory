# DefaultApi

All URIs are relative to *http://stream-api.betfair.com:443/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**requestPost**](DefaultApi.md#requestPost) | **POST** /request |  |


<a id="requestPost"></a>
# **requestPost**
> AllResponseTypesExample requestPost(allRequestTypesExample)



This is a socket protocol delimited by CRLF (not http)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://stream-api.betfair.com:443/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    AllRequestTypesExample allRequestTypesExample = new AllRequestTypesExample(); // AllRequestTypesExample | Requests are sent to socket
    try {
      AllResponseTypesExample result = apiInstance.requestPost(allRequestTypesExample);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#requestPost");
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
| **allRequestTypesExample** | [**AllRequestTypesExample**](AllRequestTypesExample.md)| Requests are sent to socket | |

### Return type

[**AllResponseTypesExample**](AllResponseTypesExample.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Responses are received from socket |  -  |

