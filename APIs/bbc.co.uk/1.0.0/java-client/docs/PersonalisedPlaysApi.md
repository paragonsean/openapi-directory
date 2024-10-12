# PersonalisedPlaysApi

All URIs are relative to *https://rms.api.bbc.co.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**myPlaysPost**](PersonalisedPlaysApi.md#myPlaysPost) | **POST** /my/plays | Write Play Event |


<a id="myPlaysPost"></a>
# **myPlaysPost**
> myPlaysPost(authorization, xAPIKey, body)

Write Play Event

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PersonalisedPlaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    PersonalisedPlaysApi apiInstance = new PersonalisedPlaysApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    Body4 body = new Body4(); // Body4 | 
    try {
      apiInstance.myPlaysPost(authorization, xAPIKey, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling PersonalisedPlaysApi#myPlaysPost");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAPIKey** | **String**| API_KEY | |
| **body** | [**Body4**](Body4.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Request successfully sent to UAS. |  -  |
| **400** | The request was malformed. |  -  |
| **401** | There was an error with the supplied &#x60;Authorization&#x60; header. |  -  |

