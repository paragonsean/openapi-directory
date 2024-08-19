# GeneralApi

All URIs are relative to *https://api.twitter.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getOpenApiSpec**](GeneralApi.md#getOpenApiSpec) | **GET** /2/openapi.json | Returns the OpenAPI Specification document. |


<a id="getOpenApiSpec"></a>
# **getOpenApiSpec**
> Object getOpenApiSpec()

Returns the OpenAPI Specification document.

Full OpenAPI Specification in JSON format. (See https://github.com/OAI/OpenAPI-Specification/blob/master/README.md)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twitter.com");

    GeneralApi apiInstance = new GeneralApi(defaultClient);
    try {
      Object result = apiInstance.getOpenApiSpec();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneralApi#getOpenApiSpec");
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
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful |  -  |

