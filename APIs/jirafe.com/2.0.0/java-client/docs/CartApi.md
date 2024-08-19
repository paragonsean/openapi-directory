# CartApi

All URIs are relative to *https://event.jirafe.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postCart**](CartApi.md#postCart) | **POST** /{siteId}/cart | Send a cart for the given site |


<a id="postCart"></a>
# **postCart**
> postCart(siteId, body)

Send a cart for the given site

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://event.jirafe.com/v2");
    
    // Configure OAuth2 access token for authorization: oauth2_accessCode
    OAuth oauth2_accessCode = (OAuth) defaultClient.getAuthentication("oauth2_accessCode");
    oauth2_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2_implicit
    OAuth oauth2_implicit = (OAuth) defaultClient.getAuthentication("oauth2_implicit");
    oauth2_implicit.setAccessToken("YOUR ACCESS TOKEN");

    CartApi apiInstance = new CartApi(defaultClient);
    String siteId = "siteId_example"; // String | ID site to send the event
    Cart body = new Cart(); // Cart | cart json for the event
    try {
      apiInstance.postCart(siteId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartApi#postCart");
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
| **siteId** | **String**| ID site to send the event | |
| **body** | [**Cart**](Cart.md)| cart json for the event | |

### Return type

null (empty response body)

### Authorization

[oauth2_accessCode](../README.md#oauth2_accessCode), [oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **400** | validation |  -  |
| **403** | authorization |  -  |
| **503** | unknown |  -  |

