# CodeReferencesApi

All URIs are relative to *https://api.configcat.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1CodeReferencesDeleteReportsPost**](CodeReferencesApi.md#v1CodeReferencesDeleteReportsPost) | **POST** /v1/code-references/delete-reports |  |
| [**v1CodeReferencesPost**](CodeReferencesApi.md#v1CodeReferencesPost) | **POST** /v1/code-references |  |


<a id="v1CodeReferencesDeleteReportsPost"></a>
# **v1CodeReferencesDeleteReportsPost**
> v1CodeReferencesDeleteReportsPost(deleteRepositoryReportsRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodeReferencesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.configcat.com");
    
    // Configure HTTP basic authorization: Basic
    HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
    Basic.setUsername("YOUR USERNAME");
    Basic.setPassword("YOUR PASSWORD");

    CodeReferencesApi apiInstance = new CodeReferencesApi(defaultClient);
    DeleteRepositoryReportsRequest deleteRepositoryReportsRequest = new DeleteRepositoryReportsRequest(); // DeleteRepositoryReportsRequest | 
    try {
      apiInstance.v1CodeReferencesDeleteReportsPost(deleteRepositoryReportsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodeReferencesApi#v1CodeReferencesDeleteReportsPost");
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
| **deleteRepositoryReportsRequest** | [**DeleteRepositoryReportsRequest**](DeleteRepositoryReportsRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad request. |  -  |
| **401** | Unauthorized. In case of the Public Management API credentials are invalid. |  -  |
| **404** | Not found. |  -  |
| **429** | Too many requests. In case of the request rate exceeds the rate limits. |  -  |

<a id="v1CodeReferencesPost"></a>
# **v1CodeReferencesPost**
> v1CodeReferencesPost(codeReferenceRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodeReferencesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.configcat.com");
    
    // Configure HTTP basic authorization: Basic
    HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
    Basic.setUsername("YOUR USERNAME");
    Basic.setPassword("YOUR PASSWORD");

    CodeReferencesApi apiInstance = new CodeReferencesApi(defaultClient);
    CodeReferenceRequest codeReferenceRequest = new CodeReferenceRequest(); // CodeReferenceRequest | 
    try {
      apiInstance.v1CodeReferencesPost(codeReferenceRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodeReferencesApi#v1CodeReferencesPost");
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
| **codeReferenceRequest** | [**CodeReferenceRequest**](CodeReferenceRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad request. |  -  |
| **401** | Unauthorized. In case of the Public Management API credentials are invalid. |  -  |
| **404** | Not found. |  -  |
| **429** | Too many requests. In case of the request rate exceeds the rate limits. |  -  |

