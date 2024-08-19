# PipelineTemplateDefinitionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**pipelineTemplateDefinitionsList**](PipelineTemplateDefinitionsApi.md#pipelineTemplateDefinitionsList) | **GET** /providers/Microsoft.DevOps/pipelineTemplateDefinitions |  |


<a id="pipelineTemplateDefinitionsList"></a>
# **pipelineTemplateDefinitionsList**
> PipelineTemplateDefinitionListResult pipelineTemplateDefinitionsList(apiVersion)



Lists all pipeline templates which can be used to configure an Azure Pipeline.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelineTemplateDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PipelineTemplateDefinitionsApi apiInstance = new PipelineTemplateDefinitionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version to be used with the HTTP request.
    try {
      PipelineTemplateDefinitionListResult result = apiInstance.pipelineTemplateDefinitionsList(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelineTemplateDefinitionsApi#pipelineTemplateDefinitionsList");
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
| **apiVersion** | **String**| API version to be used with the HTTP request. | |

### Return type

[**PipelineTemplateDefinitionListResult**](PipelineTemplateDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The pipeline template definitions have been fetched successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

