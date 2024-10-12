# DefaultApi

All URIs are relative to *https://services.scideas.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**perfectpdfApiPost**](DefaultApi.md#perfectpdfApiPost) | **POST** /perfectpdf/api | Returns PDF document. |


<a id="perfectpdfApiPost"></a>
# **perfectpdfApiPost**
> InlineResponse200 perfectpdfApiPost(perfectpdfApiBody)

Returns PDF document.

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
    defaultClient.setBasePath("https://services.scideas.net");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    PerfectpdfApiBody perfectpdfApiBody = new PerfectpdfApiBody(); // PerfectpdfApiBody | 
    try {
      InlineResponse200 result = apiInstance.perfectpdfApiPost(perfectpdfApiBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#perfectpdfApiPost");
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
| **perfectpdfApiBody** | [**PerfectpdfApiBody**](PerfectpdfApiBody.md)|  | |

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Either a PDF document or an error message |  -  |

