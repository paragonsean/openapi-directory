# DefaultApi

All URIs are relative to *https://api.easypdfserver.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**makePdfPost**](DefaultApi.md#makePdfPost) | **POST** /make-pdf | Generate a PDF from HTML or URL. |


<a id="makePdfPost"></a>
# **makePdfPost**
> File makePdfPost(makePdfPostRequest)

Generate a PDF from HTML or URL.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.easypdfserver.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    MakePdfPostRequest makePdfPostRequest = new MakePdfPostRequest(); // MakePdfPostRequest | Pass the API key from easypdfserver.com and either HTML or URL to generate your PDF.
    try {
      File result = apiInstance.makePdfPost(makePdfPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#makePdfPost");
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
| **makePdfPostRequest** | [**MakePdfPostRequest**](MakePdfPostRequest.md)| Pass the API key from easypdfserver.com and either HTML or URL to generate your PDF. | |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/pdf

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Your PDF file |  -  |

