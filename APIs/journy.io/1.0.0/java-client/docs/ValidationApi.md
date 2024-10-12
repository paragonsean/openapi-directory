# ValidationApi

All URIs are relative to *https://api.journy.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getValidity**](ValidationApi.md#getValidity) | **GET** /validate | Validate API key |


<a id="getValidity"></a>
# **getValidity**
> GetValidity200Response getValidity()

Validate API key

Endpoint used to test the validity and some basic information about a specific API Key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ValidationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.journy.io");

    ValidationApi apiInstance = new ValidationApi(defaultClient);
    try {
      GetValidity200Response result = apiInstance.getValidity();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ValidationApi#getValidity");
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

[**GetValidity200Response**](GetValidity200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Key validation |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
| **401** | No API Key was provided or the key is not authorised to perform the action |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
| **403** | The API Key provided is currently not enabled |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
| **429** | Too many API requests were send |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
| **500** | An unexpected error occurred |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |

