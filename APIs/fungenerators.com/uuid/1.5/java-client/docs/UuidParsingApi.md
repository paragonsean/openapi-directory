# UuidParsingApi

All URIs are relative to *https://api.fungenerators.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**uuidPost**](UuidParsingApi.md#uuidPost) | **POST** /uuid |  |


<a id="uuidPost"></a>
# **uuidPost**
> uuidPost(uuidstr)



Parse a UUID string and return its version and check whether it is valid.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UuidParsingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fungenerators.com");
    
    // Configure API key authorization: X-Fungenerators-Api-Secret
    ApiKeyAuth X-Fungenerators-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Fungenerators-Api-Secret");
    X-Fungenerators-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Fungenerators-Api-Secret.setApiKeyPrefix("Token");

    UuidParsingApi apiInstance = new UuidParsingApi(defaultClient);
    String uuidstr = "uuidstr_example"; // String | UUID String to parse
    try {
      apiInstance.uuidPost(uuidstr);
    } catch (ApiException e) {
      System.err.println("Exception when calling UuidParsingApi#uuidPost");
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
| **uuidstr** | **String**| UUID String to parse | |

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

