# OrderApi

All URIs are relative to *https://event.jirafe.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postOrderCancelled**](OrderApi.md#postOrderCancelled) | **POST** /{siteId}/order | Send a order for the given site |


<a id="postOrderCancelled"></a>
# **postOrderCancelled**
> postOrderCancelled(siteId, body)

Send a order for the given site

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

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

    OrderApi apiInstance = new OrderApi(defaultClient);
    String siteId = "siteId_example"; // String | ID site to send the event
    OrderCancelled body = new OrderCancelled(); // OrderCancelled | order json for the event
    try {
      apiInstance.postOrderCancelled(siteId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#postOrderCancelled");
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
| **body** | [**OrderCancelled**](OrderCancelled.md)| order json for the event | |

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

