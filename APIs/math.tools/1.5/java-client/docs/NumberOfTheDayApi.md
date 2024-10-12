# NumberOfTheDayApi

All URIs are relative to *https://api.math.tools*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**numbersNodGet**](NumberOfTheDayApi.md#numbersNodGet) | **GET** /numbers/nod |  |


<a id="numbersNodGet"></a>
# **numbersNodGet**
> numbersNodGet()



Get the number of the day for current day

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumberOfTheDayApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.math.tools");
    
    // Configure API key authorization: X-Mathtools-Api-Secret
    ApiKeyAuth X-Mathtools-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Mathtools-Api-Secret");
    X-Mathtools-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Mathtools-Api-Secret.setApiKeyPrefix("Token");

    NumberOfTheDayApi apiInstance = new NumberOfTheDayApi(defaultClient);
    try {
      apiInstance.numbersNodGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling NumberOfTheDayApi#numbersNodGet");
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

[X-Mathtools-Api-Secret](../README.md#X-Mathtools-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success response |  -  |
| **401** | 401 Unauthorized response |  -  |

