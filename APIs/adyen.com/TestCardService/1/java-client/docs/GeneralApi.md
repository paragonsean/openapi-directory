# GeneralApi

All URIs are relative to *https://pal-test.adyen.com/pal/services/TestCard/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postCreateTestCardRanges**](GeneralApi.md#postCreateTestCardRanges) | **POST** /createTestCardRanges | Creates one or more test card ranges. |


<a id="postCreateTestCardRanges"></a>
# **postCreateTestCardRanges**
> CreateTestCardRangesResult postCreateTestCardRanges(createTestCardRangesRequest)

Creates one or more test card ranges.

Creates one or more test card ranges.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://pal-test.adyen.com/pal/services/TestCard/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    GeneralApi apiInstance = new GeneralApi(defaultClient);
    CreateTestCardRangesRequest createTestCardRangesRequest = new CreateTestCardRangesRequest(); // CreateTestCardRangesRequest | 
    try {
      CreateTestCardRangesResult result = apiInstance.postCreateTestCardRanges(createTestCardRangesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneralApi#postCreateTestCardRanges");
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
| **createTestCardRangesRequest** | [**CreateTestCardRangesRequest**](CreateTestCardRangesRequest.md)|  | [optional] |

### Return type

[**CreateTestCardRangesResult**](CreateTestCardRangesResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

