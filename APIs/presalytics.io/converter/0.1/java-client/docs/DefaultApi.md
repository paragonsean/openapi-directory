# DefaultApi

All URIs are relative to *https://api.presalytics.io/doc-converter*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**svgconvert**](DefaultApi.md#svgconvert) | **POST** /svgconvert | converts pptx file to svg image |


<a id="svgconvert"></a>
# **svgconvert**
> FileUrl svgconvert(_file)

converts pptx file to svg image

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
    defaultClient.setBasePath("https://api.presalytics.io/doc-converter");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    File _file = new File("/path/to/file"); // File | 
    try {
      FileUrl result = apiInstance.svgconvert(_file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#svgconvert");
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
| **_file** | **File**|  | [optional] |

### Return type

[**FileUrl**](FileUrl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Url of svg file |  -  |
| **400** | Bad Request. |  -  |
| **415** | Invalid file type |  -  |

