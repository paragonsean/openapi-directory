# LookupApi

All URIs are relative to *https://api.bintable.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**binLookup**](LookupApi.md#binLookup) | **GET** /{bin} | Lookup for bin |


<a id="binLookup"></a>
# **binLookup**
> List&lt;ResponseItem&gt; binLookup(bin, apiKey)

Lookup for bin

By passing in the appropriate BIN, you can lookup for card meta data in bintable.com API 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bintable.com/v1");

    LookupApi apiInstance = new LookupApi(defaultClient);
    String bin = "bin_example"; // String | pass the required BIN code
    String apiKey = "apiKey_example"; // String | The API key, which you can get from bintable.com website.
    try {
      List<ResponseItem> result = apiInstance.binLookup(bin, apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupApi#binLookup");
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
| **bin** | **String**| pass the required BIN code | |
| **apiKey** | **String**| The API key, which you can get from bintable.com website. | |

### Return type

[**List&lt;ResponseItem&gt;**](ResponseItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | BIN data response |  -  |
| **401** | Your balance is exhausted,or package expired |  -  |
| **403** | Invalid API Key |  -  |
| **422** | API key is missing |  -  |

