# ConversionApi

All URIs are relative to *https://mermade.org.uk/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**convert**](ConversionApi.md#convert) | **POST** /convert | Convert a Swagger 2.0 definition passed in the body to OpenAPI 3.0.x  |
| [**convertUrl**](ConversionApi.md#convertUrl) | **GET** /convert | Convert a Swagger 2.0 definition to OpenAPI 3.0.x from a URL |


<a id="convert"></a>
# **convert**
> Object convert(filename, source, validate)

Convert a Swagger 2.0 definition passed in the body to OpenAPI 3.0.x 



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mermade.org.uk/api/v1");

    ConversionApi apiInstance = new ConversionApi(defaultClient);
    String filename = "filename_example"; // String | The file to upload and convert
    String source = "source_example"; // String | The text of a Swagger 2.0 definition to convert
    String validate = "true"; // String | 
    try {
      Object result = apiInstance.convert(filename, source, validate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversionApi#convert");
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
| **filename** | **String**| The file to upload and convert | [optional] |
| **source** | **String**| The text of a Swagger 2.0 definition to convert | [optional] |
| **validate** | **String**|  | [optional] [enum: true] |

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
| **200** | default |  -  |
| **400** | Invalid request |  -  |

<a id="convertUrl"></a>
# **convertUrl**
> Object convertUrl(url)

Convert a Swagger 2.0 definition to OpenAPI 3.0.x from a URL



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mermade.org.uk/api/v1");

    ConversionApi apiInstance = new ConversionApi(defaultClient);
    URI url = new URI(); // URI | The URL to retrieve the OpenAPI 2.0 definition from
    try {
      Object result = apiInstance.convertUrl(url);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversionApi#convertUrl");
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
| **url** | **URI**| The URL to retrieve the OpenAPI 2.0 definition from | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | default |  -  |

