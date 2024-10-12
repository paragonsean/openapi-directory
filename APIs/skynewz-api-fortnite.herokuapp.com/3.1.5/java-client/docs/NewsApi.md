# NewsApi

All URIs are relative to *https://skynewz-api-fortnite.herokuapp.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**newsGet**](NewsApi.md#newsGet) | **GET** /news | Get Fortnite News |


<a id="newsGet"></a>
# **newsGet**
> NewsGet200Response newsGet()

Get Fortnite News

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://skynewz-api-fortnite.herokuapp.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    NewsApi apiInstance = new NewsApi(defaultClient);
    try {
      NewsGet200Response result = apiInstance.newsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NewsApi#newsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NewsGet200Response**](NewsGet200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A JSON objects of current news |  -  |
| **0** | Unexpected error |  -  |

