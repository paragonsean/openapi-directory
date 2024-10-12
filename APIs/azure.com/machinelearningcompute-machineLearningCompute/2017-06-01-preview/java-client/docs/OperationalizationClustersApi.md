# OperationalizationClustersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**operationalizationClustersCheckUpdate**](OperationalizationClustersApi.md#operationalizationClustersCheckUpdate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningCompute/operationalizationClusters/{clusterName}/checkUpdate |  |
| [**operationalizationClustersCreateOrUpdate**](OperationalizationClustersApi.md#operationalizationClustersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningCompute/operationalizationClusters/{clusterName} |  |
| [**operationalizationClustersDelete**](OperationalizationClustersApi.md#operationalizationClustersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningCompute/operationalizationClusters/{clusterName} |  |
| [**operationalizationClustersGet**](OperationalizationClustersApi.md#operationalizationClustersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningCompute/operationalizationClusters/{clusterName} |  |
| [**operationalizationClustersListByResourceGroup**](OperationalizationClustersApi.md#operationalizationClustersListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningCompute/operationalizationClusters |  |
| [**operationalizationClustersListBySubscriptionId**](OperationalizationClustersApi.md#operationalizationClustersListBySubscriptionId) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.MachineLearningCompute/operationalizationClusters |  |
| [**operationalizationClustersListKeys**](OperationalizationClustersApi.md#operationalizationClustersListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningCompute/operationalizationClusters/{clusterName}/listKeys |  |
| [**operationalizationClustersUpdate**](OperationalizationClustersApi.md#operationalizationClustersUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningCompute/operationalizationClusters/{clusterName} |  |
| [**operationalizationClustersUpdateSystem**](OperationalizationClustersApi.md#operationalizationClustersUpdateSystem) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningCompute/operationalizationClusters/{clusterName}/updateSystem |  |


<a id="operationalizationClustersCheckUpdate"></a>
# **operationalizationClustersCheckUpdate**
> CheckUpdateResponse operationalizationClustersCheckUpdate(apiVersion, subscriptionId, resourceGroupName, clusterName)



Checks if updates are available for system services in the cluster

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperationalizationClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    OperationalizationClustersApi apiInstance = new OperationalizationClustersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearningCompute resource provider API to use.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which the cluster is located.
    String clusterName = "clusterName_example"; // String | The name of the cluster.
    try {
      CheckUpdateResponse result = apiInstance.operationalizationClustersCheckUpdate(apiVersion, subscriptionId, resourceGroupName, clusterName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperationalizationClustersApi#operationalizationClustersCheckUpdate");
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
| **apiVersion** | **String**| The version of the Microsoft.MachineLearningCompute resource provider API to use. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of the resource group in which the cluster is located. | |
| **clusterName** | **String**| The name of the cluster. | |

### Return type

[**CheckUpdateResponse**](CheckUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request completed successfully. |  -  |
| **202** | The request was accepted and will complete asynchronously. The know the progress of the async operation do a GET call on the URI in the Location header. For more information about Asynchronous Operations, see https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-manager-async-operations. |  * Location - URI of the async operation. <br>  |

<a id="operationalizationClustersCreateOrUpdate"></a>
# **operationalizationClustersCreateOrUpdate**
> OperationalizationCluster operationalizationClustersCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, clusterName, parameters)



Create or update an operationalization cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperationalizationClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    OperationalizationClustersApi apiInstance = new OperationalizationClustersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearningCompute resource provider API to use.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which the cluster is located.
    String clusterName = "clusterName_example"; // String | The name of the cluster.
    OperationalizationCluster parameters = new OperationalizationCluster(); // OperationalizationCluster | Parameters supplied to create or update an Operationalization cluster.
    try {
      OperationalizationCluster result = apiInstance.operationalizationClustersCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, clusterName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperationalizationClustersApi#operationalizationClustersCreateOrUpdate");
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
| **apiVersion** | **String**| The version of the Microsoft.MachineLearningCompute resource provider API to use. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of the resource group in which the cluster is located. | |
| **clusterName** | **String**| The name of the cluster. | |
| **parameters** | [**OperationalizationCluster**](OperationalizationCluster.md)| Parameters supplied to create or update an Operationalization cluster. | |

### Return type

[**OperationalizationCluster**](OperationalizationCluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The create or update succeeded. |  -  |
| **201** | The request was accepted and will complete asynchronously. To get the progress of the operation, call GET operation on the URL in Azure-AsyncOperation header field. For more information about Asynchronous Operations, see https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-manager-async-operations. |  * Azure-AsyncOperation -  <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="operationalizationClustersDelete"></a>
# **operationalizationClustersDelete**
> operationalizationClustersDelete(apiVersion, subscriptionId, resourceGroupName, clusterName)



Deletes the specified cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperationalizationClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    OperationalizationClustersApi apiInstance = new OperationalizationClustersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearningCompute resource provider API to use.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which the cluster is located.
    String clusterName = "clusterName_example"; // String | The name of the cluster.
    try {
      apiInstance.operationalizationClustersDelete(apiVersion, subscriptionId, resourceGroupName, clusterName);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperationalizationClustersApi#operationalizationClustersDelete");
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
| **apiVersion** | **String**| The version of the Microsoft.MachineLearningCompute resource provider API to use. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of the resource group in which the cluster is located. | |
| **clusterName** | **String**| The name of the cluster. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The cluster existed and was deleted successfully. |  -  |
| **202** | The delete request was accepted and will complete asynchronously. The know the progress of the delete operation do a GET call on the URI in the Location header. For more information about Asynchronous Operations, see https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-manager-async-operations. |  * Location - URI of the async operation. <br>  |
| **204** | No Content. The cluster did not exist but the request was well formed. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="operationalizationClustersGet"></a>
# **operationalizationClustersGet**
> OperationalizationCluster operationalizationClustersGet(apiVersion, subscriptionId, resourceGroupName, clusterName)



Gets the operationalization cluster resource view. Note that the credentials are not returned by this call. Call ListKeys to get them.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperationalizationClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    OperationalizationClustersApi apiInstance = new OperationalizationClustersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearningCompute resource provider API to use.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which the cluster is located.
    String clusterName = "clusterName_example"; // String | The name of the cluster.
    try {
      OperationalizationCluster result = apiInstance.operationalizationClustersGet(apiVersion, subscriptionId, resourceGroupName, clusterName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperationalizationClustersApi#operationalizationClustersGet");
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
| **apiVersion** | **String**| The version of the Microsoft.MachineLearningCompute resource provider API to use. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of the resource group in which the cluster is located. | |
| **clusterName** | **String**| The name of the cluster. | |

### Return type

[**OperationalizationCluster**](OperationalizationCluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="operationalizationClustersListByResourceGroup"></a>
# **operationalizationClustersListByResourceGroup**
> PaginatedOperationalizationClustersList operationalizationClustersListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, $skiptoken)



Gets the clusters in the specified resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperationalizationClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    OperationalizationClustersApi apiInstance = new OperationalizationClustersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearningCompute resource provider API to use.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which the cluster is located.
    String $skiptoken = "$skiptoken_example"; // String | Continuation token for pagination.
    try {
      PaginatedOperationalizationClustersList result = apiInstance.operationalizationClustersListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, $skiptoken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperationalizationClustersApi#operationalizationClustersListByResourceGroup");
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
| **apiVersion** | **String**| The version of the Microsoft.MachineLearningCompute resource provider API to use. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of the resource group in which the cluster is located. | |
| **$skiptoken** | **String**| Continuation token for pagination. | [optional] |

### Return type

[**PaginatedOperationalizationClustersList**](PaginatedOperationalizationClustersList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The response includes a paginated array of cluster objects and a URI to the next set of results, if any. For the more information the limits of the number of items in a resource group, see https://azure.microsoft.com/en-us/documentation/articles/azure-subscription-service-limits/. Note that the cluster objects are sparsely populated to conserve space in the response content. To get the full cluster object, call the GET operation on the cluster. |  -  |

<a id="operationalizationClustersListBySubscriptionId"></a>
# **operationalizationClustersListBySubscriptionId**
> PaginatedOperationalizationClustersList operationalizationClustersListBySubscriptionId(apiVersion, subscriptionId, $skiptoken)



Gets the operationalization clusters in the specified subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperationalizationClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    OperationalizationClustersApi apiInstance = new OperationalizationClustersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearningCompute resource provider API to use.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String $skiptoken = "$skiptoken_example"; // String | Continuation token for pagination.
    try {
      PaginatedOperationalizationClustersList result = apiInstance.operationalizationClustersListBySubscriptionId(apiVersion, subscriptionId, $skiptoken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperationalizationClustersApi#operationalizationClustersListBySubscriptionId");
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
| **apiVersion** | **String**| The version of the Microsoft.MachineLearningCompute resource provider API to use. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **$skiptoken** | **String**| Continuation token for pagination. | [optional] |

### Return type

[**PaginatedOperationalizationClustersList**](PaginatedOperationalizationClustersList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The response includes a paginated array of cluster objects and a URI to the next set of results, if any. Note that the cluster objects are sparsely populated to conserve space in the response content. To get the full cluster object, call the GET operation on the cluster. |  -  |

<a id="operationalizationClustersListKeys"></a>
# **operationalizationClustersListKeys**
> OperationalizationClusterCredentials operationalizationClustersListKeys(apiVersion, subscriptionId, resourceGroupName, clusterName)



Gets the credentials for the specified cluster such as Storage, ACR and ACS credentials. This is a long running operation because it fetches keys from dependencies.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperationalizationClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    OperationalizationClustersApi apiInstance = new OperationalizationClustersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearningCompute resource provider API to use.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which the cluster is located.
    String clusterName = "clusterName_example"; // String | The name of the cluster.
    try {
      OperationalizationClusterCredentials result = apiInstance.operationalizationClustersListKeys(apiVersion, subscriptionId, resourceGroupName, clusterName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperationalizationClustersApi#operationalizationClustersListKeys");
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
| **apiVersion** | **String**| The version of the Microsoft.MachineLearningCompute resource provider API to use. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of the resource group in which the cluster is located. | |
| **clusterName** | **String**| The name of the cluster. | |

### Return type

[**OperationalizationClusterCredentials**](OperationalizationClusterCredentials.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request completed successfully. |  -  |
| **202** | The request was accepted and will complete asynchronously. The know the progress of the async operation do a GET call on the URI in the Location header. For more information about Asynchronous Operations, see https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-manager-async-operations. |  * Location - URI of the async operation. <br>  |

<a id="operationalizationClustersUpdate"></a>
# **operationalizationClustersUpdate**
> OperationalizationCluster operationalizationClustersUpdate(apiVersion, subscriptionId, resourceGroupName, clusterName, parameters)



The PATCH operation can be used to update only the tags for a cluster. Use PUT operation to update other properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperationalizationClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    OperationalizationClustersApi apiInstance = new OperationalizationClustersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearningCompute resource provider API to use.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which the cluster is located.
    String clusterName = "clusterName_example"; // String | The name of the cluster.
    OperationalizationClusterUpdateParameters parameters = new OperationalizationClusterUpdateParameters(); // OperationalizationClusterUpdateParameters | The parameters supplied to patch the cluster.
    try {
      OperationalizationCluster result = apiInstance.operationalizationClustersUpdate(apiVersion, subscriptionId, resourceGroupName, clusterName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperationalizationClustersApi#operationalizationClustersUpdate");
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
| **apiVersion** | **String**| The version of the Microsoft.MachineLearningCompute resource provider API to use. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of the resource group in which the cluster is located. | |
| **clusterName** | **String**| The name of the cluster. | |
| **parameters** | [**OperationalizationClusterUpdateParameters**](OperationalizationClusterUpdateParameters.md)| The parameters supplied to patch the cluster. | |

### Return type

[**OperationalizationCluster**](OperationalizationCluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The update completed successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="operationalizationClustersUpdateSystem"></a>
# **operationalizationClustersUpdateSystem**
> UpdateSystemResponse operationalizationClustersUpdateSystem(apiVersion, subscriptionId, resourceGroupName, clusterName)



Updates system services in a cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperationalizationClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    OperationalizationClustersApi apiInstance = new OperationalizationClustersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearningCompute resource provider API to use.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which the cluster is located.
    String clusterName = "clusterName_example"; // String | The name of the cluster.
    try {
      UpdateSystemResponse result = apiInstance.operationalizationClustersUpdateSystem(apiVersion, subscriptionId, resourceGroupName, clusterName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperationalizationClustersApi#operationalizationClustersUpdateSystem");
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
| **apiVersion** | **String**| The version of the Microsoft.MachineLearningCompute resource provider API to use. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of the resource group in which the cluster is located. | |
| **clusterName** | **String**| The name of the cluster. | |

### Return type

[**UpdateSystemResponse**](UpdateSystemResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request completed successfully. Check the response body for update details. |  -  |
| **202** | The request was accepted and will complete asynchronously. The know the progress of the async operation do a GET call on the URI in the Location header. For more information about Asynchronous Operations, see https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-manager-async-operations. |  * Location - URI of the async operation. <br>  |

