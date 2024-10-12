# DefaultApi

All URIs are relative to *https://apimatic.io/api/transform*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**convertAPI**](DefaultApi.md#convertAPI) | **POST** /transform | Transform API Descriptions from/to various formats |


<a id="convertAPI"></a>
# **convertAPI**
> Object convertAPI(format, url)

Transform API Descriptions from/to various formats

Transform API Descriptions from/to various formats e.g., Swagger, API Blueprint, RAML, WADL, Google Discovery, I/O Docs.  ### INPUTS * API Blueprint * Swagger 1.0 - 1.2 * Swagger 2.0 JSON * Swagger 2.0 YAML * WADL - W3C 2009 * Google Discovery * RAML 0.8 * I/O Docs - Mashery * HAR 1.2 * Postman Collection 1.0 - 2.0 * APIMATIC Format * Mashape  ### OUTPUTS * API Blueprint * Swagger 1.2 * Swagger 2.0 JSON * Swagger 2.0 YAML * WADL - W3C 2009 * RAML 0.8 - 1.0 * APIMATIC Format

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
    defaultClient.setBasePath("https://apimatic.io/api/transform");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String format = "swagger10"; // String | 
    String url = "url_example"; // String | 
    try {
      Object result = apiInstance.convertAPI(format, url);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#convertAPI");
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
| **format** | **String**|  | [enum: swagger10, swagger20, swaggeryaml, apiblueprint, wadl2009, raml, apimatic] |
| **url** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The converted API specification |  -  |
| **429** | Rate-limit exceeded |  -  |

