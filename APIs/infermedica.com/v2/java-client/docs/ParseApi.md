# ParseApi

All URIs are relative to *https://api.infermedica.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getMentions**](ParseApi.md#getMentions) | **POST** /parse | Find mentions of observations in given text |


<a id="getMentions"></a>
# **getMentions**
> ParseResponse getMentions(body)

Find mentions of observations in given text

Returns list of mentions of observation found in given text.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ParseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.infermedica.com/v2");

    ParseApi apiInstance = new ParseApi(defaultClient);
    ParseRequest body = new ParseRequest(); // ParseRequest | 
    try {
      ParseResponse result = apiInstance.getMentions(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ParseApi#getMentions");
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
| **body** | [**ParseRequest**](ParseRequest.md)|  | |

### Return type

[**ParseResponse**](ParseResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Text too long |  -  |

