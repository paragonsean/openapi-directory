# RateLimitApi

All URIs are relative to *http://HOSTNAME/api/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**rateLimitGet**](RateLimitApi.md#rateLimitGet) | **GET** /rate_limit | Get rate limit status for the authenticated user |


<a id="rateLimitGet"></a>
# **rateLimitGet**
> RateLimitOverview rateLimitGet()

Get rate limit status for the authenticated user

**Note:** Accessing this endpoint does not count against your REST API rate limit.  **Note:** The &#x60;rate&#x60; object is deprecated. If you&#39;re writing new API client code or updating existing code, you should use the &#x60;core&#x60; object instead of the &#x60;rate&#x60; object. The &#x60;core&#x60; object contains the same information that is present in the &#x60;rate&#x60; object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RateLimitApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    RateLimitApi apiInstance = new RateLimitApi(defaultClient);
    try {
      RateLimitOverview result = apiInstance.rateLimitGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RateLimitApi#rateLimitGet");
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

[**RateLimitOverview**](RateLimitOverview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
| **304** | Not modified |  -  |
| **404** | Resource not found |  -  |

