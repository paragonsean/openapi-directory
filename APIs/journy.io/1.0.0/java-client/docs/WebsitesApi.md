# WebsitesApi

All URIs are relative to *https://api.journy.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getTrackingSnippet**](WebsitesApi.md#getTrackingSnippet) | **GET** /tracking/snippet | Get snippet for a website |


<a id="getTrackingSnippet"></a>
# **getTrackingSnippet**
> GetTrackingSnippet200Response getTrackingSnippet(domain)

Get snippet for a website

Endpoint used to get a snippet for a website.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebsitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.journy.io");

    WebsitesApi apiInstance = new WebsitesApi(defaultClient);
    String domain = "domain_example"; // String | The domain you want to receive a snippet for
    try {
      GetTrackingSnippet200Response result = apiInstance.getTrackingSnippet(domain);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebsitesApi#getTrackingSnippet");
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
| **domain** | **String**| The domain you want to receive a snippet for | |

### Return type

[**GetTrackingSnippet200Response**](GetTrackingSnippet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Snippet |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
| **400** | Bad request, some fields or parameters are incorrect |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
| **401** | No API Key was provided or the key is not authorised to perform the action |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
| **403** | The API Key provided is currently not enabled |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
| **404** | Not found |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
| **429** | Too many API requests were send |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
| **500** | An unexpected error occurred |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |

