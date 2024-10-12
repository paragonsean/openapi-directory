# PipelinesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**pipelinesCreateOrUpdate**](PipelinesApi.md#pipelinesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/pipelines/{pipelineName} |  |
| [**pipelinesCreateRun**](PipelinesApi.md#pipelinesCreateRun) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/pipelines/{pipelineName}/createRun |  |
| [**pipelinesDelete**](PipelinesApi.md#pipelinesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/pipelines/{pipelineName} |  |
| [**pipelinesGet**](PipelinesApi.md#pipelinesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/pipelines/{pipelineName} |  |
| [**pipelinesListByFactory**](PipelinesApi.md#pipelinesListByFactory) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/pipelines |  |


<a id="pipelinesCreateOrUpdate"></a>
# **pipelinesCreateOrUpdate**
> PipelineResource pipelinesCreateOrUpdate(subscriptionId, resourceGroupName, factoryName, pipelineName, apiVersion, pipeline, ifMatch)



Creates or updates a pipeline.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String pipelineName = "pipelineName_example"; // String | The pipeline name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    PipelineResource pipeline = new PipelineResource(); // PipelineResource | Pipeline resource definition.
    String ifMatch = "ifMatch_example"; // String | ETag of the pipeline entity.  Should only be specified for update, for which it should match existing entity or can be * for unconditional update.
    try {
      PipelineResource result = apiInstance.pipelinesCreateOrUpdate(subscriptionId, resourceGroupName, factoryName, pipelineName, apiVersion, pipeline, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#pipelinesCreateOrUpdate");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **pipelineName** | **String**| The pipeline name. | |
| **apiVersion** | **String**| The API version. | |
| **pipeline** | [**PipelineResource**](PipelineResource.md)| Pipeline resource definition. | |
| **ifMatch** | **String**| ETag of the pipeline entity.  Should only be specified for update, for which it should match existing entity or can be * for unconditional update. | [optional] |

### Return type

[**PipelineResource**](PipelineResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="pipelinesCreateRun"></a>
# **pipelinesCreateRun**
> CreateRunResponse pipelinesCreateRun(subscriptionId, resourceGroupName, factoryName, pipelineName, apiVersion, parameters)



Creates a run of a pipeline.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String pipelineName = "pipelineName_example"; // String | The pipeline name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    Map<String, Object> parameters = null; // Map<String, Object> | Parameters of the pipeline run.
    try {
      CreateRunResponse result = apiInstance.pipelinesCreateRun(subscriptionId, resourceGroupName, factoryName, pipelineName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#pipelinesCreateRun");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **pipelineName** | **String**| The pipeline name. | |
| **apiVersion** | **String**| The API version. | |
| **parameters** | [**Map&lt;String, Object&gt;**](Object.md)| Parameters of the pipeline run. | [optional] |

### Return type

[**CreateRunResponse**](CreateRunResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="pipelinesDelete"></a>
# **pipelinesDelete**
> pipelinesDelete(subscriptionId, resourceGroupName, factoryName, pipelineName, apiVersion)



Deletes a pipeline.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String pipelineName = "pipelineName_example"; // String | The pipeline name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.pipelinesDelete(subscriptionId, resourceGroupName, factoryName, pipelineName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#pipelinesDelete");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **pipelineName** | **String**| The pipeline name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **204** | No Content. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="pipelinesGet"></a>
# **pipelinesGet**
> PipelineResource pipelinesGet(subscriptionId, resourceGroupName, factoryName, pipelineName, apiVersion)



Gets a pipeline.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String pipelineName = "pipelineName_example"; // String | The pipeline name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      PipelineResource result = apiInstance.pipelinesGet(subscriptionId, resourceGroupName, factoryName, pipelineName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#pipelinesGet");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **pipelineName** | **String**| The pipeline name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**PipelineResource**](PipelineResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="pipelinesListByFactory"></a>
# **pipelinesListByFactory**
> PipelineListResponse pipelinesListByFactory(subscriptionId, resourceGroupName, factoryName, apiVersion)



Lists pipelines.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PipelinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PipelinesApi apiInstance = new PipelinesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      PipelineListResponse result = apiInstance.pipelinesListByFactory(subscriptionId, resourceGroupName, factoryName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#pipelinesListByFactory");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**PipelineListResponse**](PipelineListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

