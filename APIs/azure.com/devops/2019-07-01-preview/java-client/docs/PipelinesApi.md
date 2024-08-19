# PipelinesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**pipelinesCreateOrUpdate**](PipelinesApi.md#pipelinesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevOps/pipelines/{pipelineName} |  |
| [**pipelinesDelete**](PipelinesApi.md#pipelinesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevOps/pipelines/{pipelineName} |  |
| [**pipelinesGet**](PipelinesApi.md#pipelinesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevOps/pipelines/{pipelineName} |  |
| [**pipelinesListByResourceGroup**](PipelinesApi.md#pipelinesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevOps/pipelines |  |
| [**pipelinesListBySubscription**](PipelinesApi.md#pipelinesListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DevOps/pipelines |  |
| [**pipelinesUpdate**](PipelinesApi.md#pipelinesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevOps/pipelines/{pipelineName} |  |


<a id="pipelinesCreateOrUpdate"></a>
# **pipelinesCreateOrUpdate**
> Pipeline pipelinesCreateOrUpdate(subscriptionId, resourceGroupName, apiVersion, pipelineName, createOperationParameters)



Creates or updates an Azure Pipeline.

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
    String subscriptionId = "subscriptionId_example"; // String | Unique identifier of the Azure subscription. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String apiVersion = "apiVersion_example"; // String | API version to be used with the HTTP request.
    String pipelineName = "pipelineName_example"; // String | The name of the Azure Pipeline resource in ARM.
    Pipeline createOperationParameters = new Pipeline(); // Pipeline | The request payload to create the Azure Pipeline.
    try {
      Pipeline result = apiInstance.pipelinesCreateOrUpdate(subscriptionId, resourceGroupName, apiVersion, pipelineName, createOperationParameters);
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
| **subscriptionId** | **String**| Unique identifier of the Azure subscription. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **apiVersion** | **String**| API version to be used with the HTTP request. | |
| **pipelineName** | **String**| The name of the Azure Pipeline resource in ARM. | |
| **createOperationParameters** | [**Pipeline**](Pipeline.md)| The request payload to create the Azure Pipeline. | |

### Return type

[**Pipeline**](Pipeline.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Azure Pipeline has been configured successfully. |  -  |
| **202** | The request has been accepted for processing and the Azure Pipeline will be configured asynchronously. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="pipelinesDelete"></a>
# **pipelinesDelete**
> pipelinesDelete(subscriptionId, resourceGroupName, apiVersion, pipelineName)



Deletes an Azure Pipeline.

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
    String subscriptionId = "subscriptionId_example"; // String | Unique identifier of the Azure subscription. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String apiVersion = "apiVersion_example"; // String | API version to be used with the HTTP request.
    String pipelineName = "pipelineName_example"; // String | The name of the Azure Pipeline resource.
    try {
      apiInstance.pipelinesDelete(subscriptionId, resourceGroupName, apiVersion, pipelineName);
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
| **subscriptionId** | **String**| Unique identifier of the Azure subscription. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **apiVersion** | **String**| API version to be used with the HTTP request. | |
| **pipelineName** | **String**| The name of the Azure Pipeline resource. | |

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
| **200** | The Azure Pipeline has been deleted successfully. |  -  |
| **204** | The Azure Pipeline is not found or has been deleted already. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="pipelinesGet"></a>
# **pipelinesGet**
> Pipeline pipelinesGet(subscriptionId, resourceGroupName, apiVersion, pipelineName)



Gets an existing Azure Pipeline.

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
    String subscriptionId = "subscriptionId_example"; // String | Unique identifier of the Azure subscription. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String apiVersion = "apiVersion_example"; // String | API version to be used with the HTTP request.
    String pipelineName = "pipelineName_example"; // String | The name of the Azure Pipeline resource in ARM.
    try {
      Pipeline result = apiInstance.pipelinesGet(subscriptionId, resourceGroupName, apiVersion, pipelineName);
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
| **subscriptionId** | **String**| Unique identifier of the Azure subscription. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **apiVersion** | **String**| API version to be used with the HTTP request. | |
| **pipelineName** | **String**| The name of the Azure Pipeline resource in ARM. | |

### Return type

[**Pipeline**](Pipeline.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Azure Pipeline has been fetched successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="pipelinesListByResourceGroup"></a>
# **pipelinesListByResourceGroup**
> PipelineListResult pipelinesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Lists all Azure Pipelines under the specified resource group.

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
    String subscriptionId = "subscriptionId_example"; // String | Unique identifier of the Azure subscription. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String apiVersion = "apiVersion_example"; // String | API version to be used with the HTTP request.
    try {
      PipelineListResult result = apiInstance.pipelinesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#pipelinesListByResourceGroup");
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
| **subscriptionId** | **String**| Unique identifier of the Azure subscription. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **apiVersion** | **String**| API version to be used with the HTTP request. | |

### Return type

[**PipelineListResult**](PipelineListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Azure Pipelines have been fetched successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="pipelinesListBySubscription"></a>
# **pipelinesListBySubscription**
> PipelineListResult pipelinesListBySubscription(subscriptionId, apiVersion)



Lists all Azure Pipelines under the specified subscription.

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
    String subscriptionId = "subscriptionId_example"; // String | Unique identifier of the Azure subscription. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API version to be used with the HTTP request.
    try {
      PipelineListResult result = apiInstance.pipelinesListBySubscription(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#pipelinesListBySubscription");
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
| **subscriptionId** | **String**| Unique identifier of the Azure subscription. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API version to be used with the HTTP request. | |

### Return type

[**PipelineListResult**](PipelineListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Azure Pipelines have been fetched successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="pipelinesUpdate"></a>
# **pipelinesUpdate**
> Pipeline pipelinesUpdate(subscriptionId, resourceGroupName, apiVersion, pipelineName, updateOperationParameters)



Updates the properties of an Azure Pipeline. Currently, only tags can be updated.

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
    String subscriptionId = "subscriptionId_example"; // String | Unique identifier of the Azure subscription. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String apiVersion = "apiVersion_example"; // String | API version to be used with the HTTP request.
    String pipelineName = "pipelineName_example"; // String | The name of the Azure Pipeline resource.
    PipelineUpdateParameters updateOperationParameters = new PipelineUpdateParameters(); // PipelineUpdateParameters | The request payload containing the properties to update in the Azure Pipeline.
    try {
      Pipeline result = apiInstance.pipelinesUpdate(subscriptionId, resourceGroupName, apiVersion, pipelineName, updateOperationParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PipelinesApi#pipelinesUpdate");
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
| **subscriptionId** | **String**| Unique identifier of the Azure subscription. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **apiVersion** | **String**| API version to be used with the HTTP request. | |
| **pipelineName** | **String**| The name of the Azure Pipeline resource. | |
| **updateOperationParameters** | [**PipelineUpdateParameters**](PipelineUpdateParameters.md)| The request payload containing the properties to update in the Azure Pipeline. | |

### Return type

[**Pipeline**](Pipeline.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Azure Pipeline has been updated successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

