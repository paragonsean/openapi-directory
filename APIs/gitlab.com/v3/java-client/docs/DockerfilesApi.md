# DockerfilesApi

All URIs are relative to *https://gitlab.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getV3Dockerfiles**](DockerfilesApi.md#getV3Dockerfiles) | **GET** /v3/dockerfiles | Get the list of the available template |
| [**getV3DockerfilesName**](DockerfilesApi.md#getV3DockerfilesName) | **GET** /v3/dockerfiles/{name} | Get the text for a specific template present in local filesystem |


<a id="getV3Dockerfiles"></a>
# **getV3Dockerfiles**
> TemplatesList getV3Dockerfiles()

Get the list of the available template

This feature was introduced in GitLab 8.15. This endpoint is deprecated and will be removed in GitLab 9.0.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DockerfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    DockerfilesApi apiInstance = new DockerfilesApi(defaultClient);
    try {
      TemplatesList result = apiInstance.getV3Dockerfiles();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DockerfilesApi#getV3Dockerfiles");
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

[**TemplatesList**](TemplatesList.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get the list of the available template |  -  |

<a id="getV3DockerfilesName"></a>
# **getV3DockerfilesName**
> Template getV3DockerfilesName(name)

Get the text for a specific template present in local filesystem

This feature was introduced in GitLab 8.15. This endpoint is deprecated and will be removed in GitLab 9.0.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DockerfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    DockerfilesApi apiInstance = new DockerfilesApi(defaultClient);
    String name = "name_example"; // String | The name of the template
    try {
      Template result = apiInstance.getV3DockerfilesName(name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DockerfilesApi#getV3DockerfilesName");
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
| **name** | **String**| The name of the template | |

### Return type

[**Template**](Template.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get the text for a specific template present in local filesystem |  -  |

