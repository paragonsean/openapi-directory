# PiApi

All URIs are relative to *https://api.math.tools*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**numbersPiGet**](PiApi.md#numbersPiGet) | **GET** /numbers/pi |  |


<a id="numbersPiGet"></a>
# **numbersPiGet**
> numbersPiGet(from, to)



Get digits of pi (Ï€)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.math.tools");
    
    // Configure API key authorization: X-Mathtools-Api-Secret
    ApiKeyAuth X-Mathtools-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Mathtools-Api-Secret");
    X-Mathtools-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Mathtools-Api-Secret.setApiKeyPrefix("Token");

    PiApi apiInstance = new PiApi(defaultClient);
    Integer from = 56; // Integer | Optional start position
    Integer to = 56; // Integer | Optional start position
    try {
      apiInstance.numbersPiGet(from, to);
    } catch (ApiException e) {
      System.err.println("Exception when calling PiApi#numbersPiGet");
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
| **from** | **Integer**| Optional start position | [optional] |
| **to** | **Integer**| Optional start position | [optional] |

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

