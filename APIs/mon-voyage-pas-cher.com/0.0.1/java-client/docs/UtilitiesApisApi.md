# UtilitiesApisApi

All URIs are relative to *https://api.mon-voyage-pas-cher.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPing**](UtilitiesApisApi.md#getPing) | **GET** /pong |  |


<a id="getPing"></a>
# **getPing**
> PongResponse getPing()



Returns a ping. In case you need a health check in your system. Cannot be called /ping as AWS is using this route for their health check. This webservice doesn&#39;t have CORS enable, as it&#39;s supposed to be call server to server and not from a webpage ( it won&#39;t work over the tester)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UtilitiesApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mon-voyage-pas-cher.com");
    
    // Configure API key authorization: x-api-key
    ApiKeyAuth x-api-key = (ApiKeyAuth) defaultClient.getAuthentication("x-api-key");
    x-api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //x-api-key.setApiKeyPrefix("Token");

    UtilitiesApisApi apiInstance = new UtilitiesApisApi(defaultClient);
    try {
      PongResponse result = apiInstance.getPing();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UtilitiesApisApi#getPing");
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

[**PongResponse**](PongResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

