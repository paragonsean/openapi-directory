# GitlabCiYmlsApi

All URIs are relative to *https://gitlab.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getV3GitlabCiYmls**](GitlabCiYmlsApi.md#getV3GitlabCiYmls) | **GET** /v3/gitlab_ci_ymls | Get the list of the available template |
| [**getV3GitlabCiYmlsName**](GitlabCiYmlsApi.md#getV3GitlabCiYmlsName) | **GET** /v3/gitlab_ci_ymls/{name} | Get the text for a specific template present in local filesystem |


<a id="getV3GitlabCiYmls"></a>
# **getV3GitlabCiYmls**
> TemplatesList getV3GitlabCiYmls()

Get the list of the available template

This feature was introduced in GitLab 8.9. This endpoint is deprecated and will be removed in GitLab 9.0.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GitlabCiYmlsApi;

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

    GitlabCiYmlsApi apiInstance = new GitlabCiYmlsApi(defaultClient);
    try {
      TemplatesList result = apiInstance.getV3GitlabCiYmls();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GitlabCiYmlsApi#getV3GitlabCiYmls");
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

<a id="getV3GitlabCiYmlsName"></a>
# **getV3GitlabCiYmlsName**
> Template getV3GitlabCiYmlsName(name)

Get the text for a specific template present in local filesystem

This feature was introduced in GitLab 8.9. This endpoint is deprecated and will be removed in GitLab 9.0.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GitlabCiYmlsApi;

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

    GitlabCiYmlsApi apiInstance = new GitlabCiYmlsApi(defaultClient);
    String name = "name_example"; // String | The name of the template
    try {
      Template result = apiInstance.getV3GitlabCiYmlsName(name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GitlabCiYmlsApi#getV3GitlabCiYmlsName");
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

