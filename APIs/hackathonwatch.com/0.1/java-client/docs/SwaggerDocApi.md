# SwaggerDocApi

All URIs are relative to *http://www.hackathonwatch.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**gETSwaggerDocFormat**](SwaggerDocApi.md#gETSwaggerDocFormat) | **GET** /swagger_doc.json | Swagger compatible API description |
| [**gETSwaggerDocNameFormat**](SwaggerDocApi.md#gETSwaggerDocNameFormat) | **GET** /swagger_doc/{name}.json | Swagger compatible API description for specific API |


<a id="gETSwaggerDocFormat"></a>
# **gETSwaggerDocFormat**
> gETSwaggerDocFormat()

Swagger compatible API description

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwaggerDocApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://www.hackathonwatch.com/api");

    SwaggerDocApi apiInstance = new SwaggerDocApi(defaultClient);
    try {
      apiInstance.gETSwaggerDocFormat();
    } catch (ApiException e) {
      System.err.println("Exception when calling SwaggerDocApi#gETSwaggerDocFormat");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="gETSwaggerDocNameFormat"></a>
# **gETSwaggerDocNameFormat**
> gETSwaggerDocNameFormat(name)

Swagger compatible API description for specific API

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwaggerDocApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://www.hackathonwatch.com/api");

    SwaggerDocApi apiInstance = new SwaggerDocApi(defaultClient);
    String name = "name_example"; // String | Resource name of mounted API
    try {
      apiInstance.gETSwaggerDocNameFormat(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwaggerDocApi#gETSwaggerDocNameFormat");
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
| **name** | **String**| Resource name of mounted API | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

