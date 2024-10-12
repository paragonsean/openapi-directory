# ApiSpecificationApi

All URIs are relative to *https://dash.readme.io/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteAPISpecification**](ApiSpecificationApi.md#deleteAPISpecification) | **DELETE** /api-specification/{id} |  |
| [**getAPISpecification**](ApiSpecificationApi.md#getAPISpecification) | **GET** /api-specification |  |
| [**updateAPISpecification**](ApiSpecificationApi.md#updateAPISpecification) | **PUT** /api-specification/{id} |  |
| [**uploadAPISpecification**](ApiSpecificationApi.md#uploadAPISpecification) | **POST** /api-specification |  |


<a id="deleteAPISpecification"></a>
# **deleteAPISpecification**
> deleteAPISpecification(id)



Delete an API specification in ReadMe

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiSpecificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dash.readme.io/api/v1");
    
    // Configure HTTP basic authorization: apiKey
    HttpBasicAuth apiKey = (HttpBasicAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setUsername("YOUR USERNAME");
    apiKey.setPassword("YOUR PASSWORD");

    ApiSpecificationApi apiInstance = new ApiSpecificationApi(defaultClient);
    String id = "id_example"; // String | ID of the API specification. The unique ID for each API can be found by navigating to your **API Definitions** page.
    try {
      apiInstance.deleteAPISpecification(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiSpecificationApi#deleteAPISpecification");
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
| **id** | **String**| ID of the API specification. The unique ID for each API can be found by navigating to your **API Definitions** page. | |

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
| **204** | The API specification was deleted |  -  |
| **404** | There is no API specification with that ID |  -  |

<a id="getAPISpecification"></a>
# **getAPISpecification**
> getAPISpecification(xReadmeVersion, perPage, page)



Get API specification metadata

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiSpecificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dash.readme.io/api/v1");
    
    // Configure HTTP basic authorization: apiKey
    HttpBasicAuth apiKey = (HttpBasicAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setUsername("YOUR USERNAME");
    apiKey.setPassword("YOUR PASSWORD");

    ApiSpecificationApi apiInstance = new ApiSpecificationApi(defaultClient);
    String xReadmeVersion = "v3.0"; // String | Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions.
    Integer perPage = 10; // Integer | Number of items to include in pagination (up to 100, defaults to 10)
    Integer page = 1; // Integer | Used to specify further pages (starts at 1)
    try {
      apiInstance.getAPISpecification(xReadmeVersion, perPage, page);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiSpecificationApi#getAPISpecification");
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
| **xReadmeVersion** | **String**| Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions. | |
| **perPage** | **Integer**| Number of items to include in pagination (up to 100, defaults to 10) | [optional] [default to 10] |
| **page** | **Integer**| Used to specify further pages (starts at 1) | [optional] [default to 1] |

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
| **200** | Successfully retrieved API specification metadata. |  * Link -  <br>  |

<a id="updateAPISpecification"></a>
# **updateAPISpecification**
> updateAPISpecification(id, spec)



Update an API specification in ReadMe

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiSpecificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dash.readme.io/api/v1");
    
    // Configure HTTP basic authorization: apiKey
    HttpBasicAuth apiKey = (HttpBasicAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setUsername("YOUR USERNAME");
    apiKey.setPassword("YOUR PASSWORD");

    ApiSpecificationApi apiInstance = new ApiSpecificationApi(defaultClient);
    String id = "id_example"; // String | ID of the API specification. The unique ID for each API can be found by navigating to your **API Definitions** page.
    File spec = new File("/path/to/file"); // File | OpenAPI/Swagger file
    try {
      apiInstance.updateAPISpecification(id, spec);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiSpecificationApi#updateAPISpecification");
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
| **id** | **String**| ID of the API specification. The unique ID for each API can be found by navigating to your **API Definitions** page. | |
| **spec** | **File**| OpenAPI/Swagger file | [optional] |

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
| **200** | The API specification was updated |  -  |
| **400** | There was a validation error during import |  -  |
| **404** | There is no API specification with that ID |  -  |

<a id="uploadAPISpecification"></a>
# **uploadAPISpecification**
> uploadAPISpecification(xReadmeVersion, spec)



Upload an API specification to ReadMe. Or, to use a newer solution see https://docs.readme.com/guides/docs/automatically-sync-api-specification-with-github

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiSpecificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dash.readme.io/api/v1");
    
    // Configure HTTP basic authorization: apiKey
    HttpBasicAuth apiKey = (HttpBasicAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setUsername("YOUR USERNAME");
    apiKey.setPassword("YOUR PASSWORD");

    ApiSpecificationApi apiInstance = new ApiSpecificationApi(defaultClient);
    String xReadmeVersion = "v3.0"; // String | Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions.
    File spec = new File("/path/to/file"); // File | OpenAPI/Swagger file
    try {
      apiInstance.uploadAPISpecification(xReadmeVersion, spec);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiSpecificationApi#uploadAPISpecification");
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
| **xReadmeVersion** | **String**| Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions. | |
| **spec** | **File**| OpenAPI/Swagger file | [optional] |

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
| **201** | The API specification successfully imported |  -  |
| **400** | There was a validation error during import |  -  |

