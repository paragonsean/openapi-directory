# OperationalizationClustersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**machineLearningComputeCreateOrUpdate**](OperationalizationClustersApi.md#machineLearningComputeCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/computes/{computeName} |  |
| [**machineLearningComputeDelete**](OperationalizationClustersApi.md#machineLearningComputeDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/computes/{computeName} |  |
| [**machineLearningComputeGet**](OperationalizationClustersApi.md#machineLearningComputeGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/computes/{computeName} |  |
| [**machineLearningComputeListByWorkspace**](OperationalizationClustersApi.md#machineLearningComputeListByWorkspace) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/computes |  |
| [**machineLearningComputeListKeys**](OperationalizationClustersApi.md#machineLearningComputeListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/computes/{computeName}/listKeys |  |
| [**machineLearningComputeUpdate**](OperationalizationClustersApi.md#machineLearningComputeUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/computes/{computeName} |  |


<a id="machineLearningComputeCreateOrUpdate"></a>
# **machineLearningComputeCreateOrUpdate**
> ComputeResource machineLearningComputeCreateOrUpdate(subscriptionId, resourceGroupName, workspaceName, computeName, apiVersion, parameters)



Creates or updates compute. This call will overwrite a compute if it exists. This is a nonrecoverable operation. If your intent is to create a new compute, do a GET first to verify that it does not exist yet.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperationalizationClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OperationalizationClustersApi apiInstance = new OperationalizationClustersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
    String workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
    String computeName = "computeName_example"; // String | Name of the Azure Machine Learning compute.
    String apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
    ComputeResource parameters = new ComputeResource(); // ComputeResource | Payload with Machine Learning compute definition.
    try {
      ComputeResource result = apiInstance.machineLearningComputeCreateOrUpdate(subscriptionId, resourceGroupName, workspaceName, computeName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperationalizationClustersApi#machineLearningComputeCreateOrUpdate");
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
| **subscriptionId** | **String**| Azure subscription identifier. | |
| **resourceGroupName** | **String**| Name of the resource group in which workspace is located. | |
| **workspaceName** | **String**| Name of Azure Machine Learning workspace. | |
| **computeName** | **String**| Name of the Azure Machine Learning compute. | |
| **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | |
| **parameters** | [**ComputeResource**](ComputeResource.md)| Payload with Machine Learning compute definition. | |

### Return type

[**ComputeResource**](ComputeResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Compute creation or update initiated. |  -  |
| **201** | Compute creation or update initiated. |  * Azure-AsyncOperation - URI to poll for asynchronous operation status. <br>  |
| **0** | Error response describing why the request failed. |  -  |

<a id="machineLearningComputeDelete"></a>
# **machineLearningComputeDelete**
> machineLearningComputeDelete(subscriptionId, resourceGroupName, workspaceName, computeName, apiVersion, underlyingResourceAction)



Deletes specified Machine Learning compute.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperationalizationClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OperationalizationClustersApi apiInstance = new OperationalizationClustersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
    String workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
    String computeName = "computeName_example"; // String | Name of the Azure Machine Learning compute.
    String apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
    String underlyingResourceAction = "Delete"; // String | Delete the underlying compute if 'Delete', or detach the underlying compute from workspace if 'Detach'.
    try {
      apiInstance.machineLearningComputeDelete(subscriptionId, resourceGroupName, workspaceName, computeName, apiVersion, underlyingResourceAction);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperationalizationClustersApi#machineLearningComputeDelete");
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
| **subscriptionId** | **String**| Azure subscription identifier. | |
| **resourceGroupName** | **String**| Name of the resource group in which workspace is located. | |
| **workspaceName** | **String**| Name of Azure Machine Learning workspace. | |
| **computeName** | **String**| Name of the Azure Machine Learning compute. | |
| **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | |
| **underlyingResourceAction** | **String**| Delete the underlying compute if &#39;Delete&#39;, or detach the underlying compute from workspace if &#39;Detach&#39;. | [enum: Delete, Detach] |

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
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **202** | Compute deletion initiated. |  * Azure-AsyncOperation - URI to poll for asynchronous operation status. <br>  * Location - URI to poll for asynchronous operation result. <br>  |
| **0** | Error response describing why the request failed. |  -  |

<a id="machineLearningComputeGet"></a>
# **machineLearningComputeGet**
> ComputeResource machineLearningComputeGet(subscriptionId, resourceGroupName, workspaceName, computeName, apiVersion)



Gets compute definition by its name. Any secrets (storage keys, service credentials, etc) are not returned - use &#39;keys&#39; nested resource to get them.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperationalizationClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OperationalizationClustersApi apiInstance = new OperationalizationClustersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
    String workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
    String computeName = "computeName_example"; // String | Name of the Azure Machine Learning compute.
    String apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
    try {
      ComputeResource result = apiInstance.machineLearningComputeGet(subscriptionId, resourceGroupName, workspaceName, computeName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperationalizationClustersApi#machineLearningComputeGet");
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
| **subscriptionId** | **String**| Azure subscription identifier. | |
| **resourceGroupName** | **String**| Name of the resource group in which workspace is located. | |
| **workspaceName** | **String**| Name of Azure Machine Learning workspace. | |
| **computeName** | **String**| Name of the Azure Machine Learning compute. | |
| **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | |

### Return type

[**ComputeResource**](ComputeResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. |  -  |
| **0** | Error response describing why the request failed. |  -  |

<a id="machineLearningComputeListByWorkspace"></a>
# **machineLearningComputeListByWorkspace**
> PaginatedComputeResourcesList machineLearningComputeListByWorkspace(subscriptionId, resourceGroupName, workspaceName, apiVersion, $skiptoken)



Gets computes in specified workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperationalizationClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OperationalizationClustersApi apiInstance = new OperationalizationClustersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
    String workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
    String apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
    String $skiptoken = "$skiptoken_example"; // String | Continuation token for pagination.
    try {
      PaginatedComputeResourcesList result = apiInstance.machineLearningComputeListByWorkspace(subscriptionId, resourceGroupName, workspaceName, apiVersion, $skiptoken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperationalizationClustersApi#machineLearningComputeListByWorkspace");
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
| **subscriptionId** | **String**| Azure subscription identifier. | |
| **resourceGroupName** | **String**| Name of the resource group in which workspace is located. | |
| **workspaceName** | **String**| Name of Azure Machine Learning workspace. | |
| **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | |
| **$skiptoken** | **String**| Continuation token for pagination. | [optional] |

### Return type

[**PaginatedComputeResourcesList**](PaginatedComputeResourcesList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response includes a paginated array of Machine Learning computes and a URI to the next set of results, if any. For the more information the limits of the number of items in a resource group, see https://azure.microsoft.com/en-us/documentation/articles/azure-subscription-service-limits/. |  -  |
| **0** | Error response describing why the request failed. |  -  |

<a id="machineLearningComputeListKeys"></a>
# **machineLearningComputeListKeys**
> ComputeSecrets machineLearningComputeListKeys(subscriptionId, resourceGroupName, workspaceName, computeName, apiVersion)



Gets secrets related to Machine Learning compute (storage keys, service credentials, etc).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperationalizationClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OperationalizationClustersApi apiInstance = new OperationalizationClustersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
    String workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
    String computeName = "computeName_example"; // String | Name of the Azure Machine Learning compute.
    String apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
    try {
      ComputeSecrets result = apiInstance.machineLearningComputeListKeys(subscriptionId, resourceGroupName, workspaceName, computeName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperationalizationClustersApi#machineLearningComputeListKeys");
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
| **subscriptionId** | **String**| Azure subscription identifier. | |
| **resourceGroupName** | **String**| Name of the resource group in which workspace is located. | |
| **workspaceName** | **String**| Name of Azure Machine Learning workspace. | |
| **computeName** | **String**| Name of the Azure Machine Learning compute. | |
| **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | |

### Return type

[**ComputeSecrets**](ComputeSecrets.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="machineLearningComputeUpdate"></a>
# **machineLearningComputeUpdate**
> ComputeResource machineLearningComputeUpdate(subscriptionId, resourceGroupName, workspaceName, computeName, apiVersion, parameters)



Updates properties of a compute. This call will overwrite a compute if it exists. This is a nonrecoverable operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperationalizationClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OperationalizationClustersApi apiInstance = new OperationalizationClustersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
    String workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
    String computeName = "computeName_example"; // String | Name of the Azure Machine Learning compute.
    String apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
    ClusterUpdateParameters parameters = new ClusterUpdateParameters(); // ClusterUpdateParameters | Additional parameters for cluster update.
    try {
      ComputeResource result = apiInstance.machineLearningComputeUpdate(subscriptionId, resourceGroupName, workspaceName, computeName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperationalizationClustersApi#machineLearningComputeUpdate");
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
| **subscriptionId** | **String**| Azure subscription identifier. | |
| **resourceGroupName** | **String**| Name of the resource group in which workspace is located. | |
| **workspaceName** | **String**| Name of Azure Machine Learning workspace. | |
| **computeName** | **String**| Name of the Azure Machine Learning compute. | |
| **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | |
| **parameters** | [**ClusterUpdateParameters**](ClusterUpdateParameters.md)| Additional parameters for cluster update. | |

### Return type

[**ComputeResource**](ComputeResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Compute update initiated. |  -  |
| **0** | Error response describing why the request failed. |  -  |

