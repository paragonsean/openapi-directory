# NumberGenerationApi

All URIs are relative to *https://api.math.tools*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**numbersRandomGet**](NumberGenerationApi.md#numbersRandomGet) | **GET** /numbers/random |  |


<a id="numbersRandomGet"></a>
# **numbersRandomGet**
> numbersRandomGet(min, max, total)



Generate random number(s)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumberGenerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.math.tools");
    
    // Configure API key authorization: X-Mathtools-Api-Secret
    ApiKeyAuth X-Mathtools-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Mathtools-Api-Secret");
    X-Mathtools-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Mathtools-Api-Secret.setApiKeyPrefix("Token");

    NumberGenerationApi apiInstance = new NumberGenerationApi(defaultClient);
    Integer min = 56; // Integer | Minimum Number value in the range
    Integer max = 56; // Integer | Maximum Number value
    Integer total = 56; // Integer | Total number of random numbers to generate. Defaults to 1
    try {
      apiInstance.numbersRandomGet(min, max, total);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumberGenerationApi#numbersRandomGet");
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
| **min** | **Integer**| Minimum Number value in the range | [optional] |
| **max** | **Integer**| Maximum Number value | [optional] |
| **total** | **Integer**| Total number of random numbers to generate. Defaults to 1 | [optional] |

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

