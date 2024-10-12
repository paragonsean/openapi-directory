# SwaggerApi

All URIs are relative to *https://dash.readme.io/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteSwagger**](SwaggerApi.md#deleteSwagger) | **DELETE** /swagger/{id} |  |
| [**updateSwagger**](SwaggerApi.md#updateSwagger) | **PUT** /swagger/{id} |  |
| [**uploadSwagger**](SwaggerApi.md#uploadSwagger) | **POST** /swagger |  |


<a id="deleteSwagger"></a>
# **deleteSwagger**
> deleteSwagger(id)



DEPRECATED. Instead, use https://docs.readme.com/developers/reference/api-specification#deleteapispecification to delete a Swagger file in ReadMe

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwaggerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dash.readme.io/api/v1");
    
    // Configure HTTP basic authorization: apiKey
    HttpBasicAuth apiKey = (HttpBasicAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setUsername("YOUR USERNAME");
    apiKey.setPassword("YOUR PASSWORD");

    SwaggerApi apiInstance = new SwaggerApi(defaultClient);
    String id = "id_example"; // String | ID of swagger the file
    try {
      apiInstance.deleteSwagger(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwaggerApi#deleteSwagger");
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
| **id** | **String**| ID of swagger the file | |

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The Swagger file was successfully deleted |  -  |
| **404** | There is no Swagger file with that ID |  -  |

<a id="updateSwagger"></a>
# **updateSwagger**
> updateSwagger(id, swagger)



DEPRECATED. Instead, use https://docs.readme.com/developers/reference/api-specification#updateapispecification to update a Swagger file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwaggerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dash.readme.io/api/v1");
    
    // Configure HTTP basic authorization: apiKey
    HttpBasicAuth apiKey = (HttpBasicAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setUsername("YOUR USERNAME");
    apiKey.setPassword("YOUR PASSWORD");

    SwaggerApi apiInstance = new SwaggerApi(defaultClient);
    String id = "id_example"; // String | ID of the Swagger file
    File swagger = new File("/path/to/file"); // File | Swagger file
    try {
      apiInstance.updateSwagger(id, swagger);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwaggerApi#updateSwagger");
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
| **id** | **String**| ID of the Swagger file | |
| **swagger** | **File**| Swagger file | [optional] |

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Swagger file was successfully updated |  -  |
| **400** | There was a validation error during import |  -  |
| **404** | There is no Swagger file with that ID |  -  |

<a id="uploadSwagger"></a>
# **uploadSwagger**
> uploadSwagger(swagger)



DEPRECATED. Instead use https://docs.readme.com/developers/reference/api-specification#uploadapispecification to upload a Swagger file to ReadMe

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwaggerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dash.readme.io/api/v1");
    
    // Configure HTTP basic authorization: apiKey
    HttpBasicAuth apiKey = (HttpBasicAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setUsername("YOUR USERNAME");
    apiKey.setPassword("YOUR PASSWORD");

    SwaggerApi apiInstance = new SwaggerApi(defaultClient);
    File swagger = new File("/path/to/file"); // File | Swagger file
    try {
      apiInstance.uploadSwagger(swagger);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwaggerApi#uploadSwagger");
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
| **swagger** | **File**| Swagger file | [optional] |

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The Swagger file was successfully imported |  -  |
| **400** | There was a validation error during import |  -  |

