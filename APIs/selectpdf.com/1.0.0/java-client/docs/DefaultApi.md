# DefaultApi

All URIs are relative to *https://selectpdf.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**api2ConvertPost**](DefaultApi.md#api2ConvertPost) | **POST** /api2/convert | Performs a html to pdf conversion |


<a id="api2ConvertPost"></a>
# **api2ConvertPost**
> api2ConvertPost(parameters)

Performs a html to pdf conversion

Converts provided HTML string or url to PDF

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
    defaultClient.setBasePath("https://selectpdf.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ConversionParameters parameters = new ConversionParameters(); // ConversionParameters | Conversion parameters
    try {
      apiInstance.api2ConvertPost(parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2ConvertPost");
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
| **parameters** | [**ConversionParameters**](ConversionParameters.md)| Conversion parameters | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The API call succeeded. The pdf document is returned. |  -  |
| **400** | Bad Request. Url or html string not specified. The body of the response contains an explanation in plain text. |  -  |
| **401** | Authorization Required. License key not specified or invalid. The body of the response contains an explanation in plain text. |  -  |
| **499** | Conversion error. The body of the response contains an explanation in plain text. |  -  |

