# SwaggerApi

All URIs are relative to *https://api.exhibitday.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**swaggerGet**](SwaggerApi.md#swaggerGet) | **GET** /api/docs/Swagger |  |


<a id="swaggerGet"></a>
# **swaggerGet**
> Object swaggerGet()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwaggerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.exhibitday.com");

    SwaggerApi apiInstance = new SwaggerApi(defaultClient);
    try {
      Object result = apiInstance.swaggerGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwaggerApi#swaggerGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

