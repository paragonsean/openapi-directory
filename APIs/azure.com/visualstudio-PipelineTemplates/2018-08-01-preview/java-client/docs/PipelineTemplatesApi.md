# PipelineTemplatesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**pipelineTemplatesList**](PipelineTemplatesApi.md#pipelineTemplatesList) | **GET** /providers/microsoft.visualstudio/pipelineTemplates | PipelineTemplates_List |


<a id="pipelineTemplatesList"></a>
# **pipelineTemplatesList**
> PipelineTemplateResourceListResult pipelineTemplatesList(apiVersion)

PipelineTemplates_List

Gets all pipeline templates which can be used to configure a CI/CD pipeline in a new or an existing Team Services project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelineTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PipelineTemplatesApi apiInstance = new PipelineTemplatesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      PipelineTemplateResourceListResult result = apiInstance.pipelineTemplatesList(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelineTemplatesApi#pipelineTemplatesList");
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
| **apiVersion** | **String**| API Version | |

### Return type

[**PipelineTemplateResourceListResult**](PipelineTemplateResourceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation succeeded. The response is a list of all pipeline templates which can be used to configure a CI/CD pipeline in a new or an existing Team Services project. |  -  |

