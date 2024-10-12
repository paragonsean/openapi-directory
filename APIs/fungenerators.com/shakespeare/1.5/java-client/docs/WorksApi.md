# WorksApi

All URIs are relative to *http://api.fungenerators.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**shakespeareQuoteGet**](WorksApi.md#shakespeareQuoteGet) | **GET** /shakespeare/quote |  |


<a id="shakespeareQuoteGet"></a>
# **shakespeareQuoteGet**
> shakespeareQuoteGet()



Get a random Shakespeare quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.fungenerators.com");
    
    // Configure API key authorization: X-Fungenerators-Api-Secret
    ApiKeyAuth X-Fungenerators-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Fungenerators-Api-Secret");
    X-Fungenerators-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Fungenerators-Api-Secret.setApiKeyPrefix("Token");

    WorksApi apiInstance = new WorksApi(defaultClient);
    try {
      apiInstance.shakespeareQuoteGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling WorksApi#shakespeareQuoteGet");
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

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

