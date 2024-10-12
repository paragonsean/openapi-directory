# DefaultApi

All URIs are relative to *https://tinyuid.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1ShortenPost**](DefaultApi.md#v1ShortenPost) | **POST** /v1/shorten | Create short link |


<a id="v1ShortenPost"></a>
# **v1ShortenPost**
> V1ShortenPost200Response v1ShortenPost(url)

Create short link

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
    defaultClient.setBasePath("https://tinyuid.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String url = "url_example"; // String | Link
    try {
      V1ShortenPost200Response result = apiInstance.v1ShortenPost(url);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#v1ShortenPost");
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
| **url** | **String**| Link | |

### Return type

[**V1ShortenPost200Response**](V1ShortenPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

