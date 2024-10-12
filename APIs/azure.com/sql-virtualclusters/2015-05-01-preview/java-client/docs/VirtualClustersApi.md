# VirtualClustersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**virtualClustersDelete**](VirtualClustersApi.md#virtualClustersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/virtualClusters/{virtualClusterName} |  |
| [**virtualClustersGet**](VirtualClustersApi.md#virtualClustersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/virtualClusters/{virtualClusterName} |  |
| [**virtualClustersList**](VirtualClustersApi.md#virtualClustersList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Sql/virtualClusters |  |
| [**virtualClustersListByResourceGroup**](VirtualClustersApi.md#virtualClustersListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/virtualClusters |  |
| [**virtualClustersUpdate**](VirtualClustersApi.md#virtualClustersUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/virtualClusters/{virtualClusterName} |  |


<a id="virtualClustersDelete"></a>
# **virtualClustersDelete**
> virtualClustersDelete(resourceGroupName, virtualClusterName, subscriptionId, apiVersion)



Deletes a virtual cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    VirtualClustersApi apiInstance = new VirtualClustersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String virtualClusterName = "virtualClusterName_example"; // String | The name of the virtual cluster.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      apiInstance.virtualClustersDelete(resourceGroupName, virtualClusterName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualClustersApi#virtualClustersDelete");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **virtualClusterName** | **String**| The name of the virtual cluster. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully deleted the virtual cluster. |  -  |
| **202** | Deleting the virtual cluster is in progress. |  -  |
| **204** | The specified virtual cluster does not exist. |  -  |
| **0** | *** Error Responses: ***   * 400 SubscriptionNotFound - The requested subscription was not found.   * 400 ManagementServiceFeatureDisabled - User attempted to use a feature which is disabled.   * 404 ResourceDoesNotExist - Resource with the name &#39;{0}&#39; does not exist. To continue, specify a valid resource name.   * 404 VirtualClusterNotInSubscriptionResourceGroup - specified virtual cluster does not exist in the specified resource group and subscription.   * 404 SubscriptionDoesNotHaveVirtualCluster - The requested virtual cluster was not found   * 404 OperationIdNotFound - The operation with Id does not exist.   * 404 ResourceNotFound - The requested resource was not found.   * 409 ConflictingVirtualClusterOperation - An operation is currently in progress for the virtual cluster.   * 409 OperationCancelled - The operation has been cancelled by user.   * 409 OperationInterrupted - The operation on the resource could not be completed because it was interrupted by another operation on the same resource.   * 429 ConflictingSubscriptionOperation - An operation is currently in progress for the subscription.   * 500 OperationTimedOut - The operation timed out and automatically rolled back. Please retry the operation. |  -  |

<a id="virtualClustersGet"></a>
# **virtualClustersGet**
> VirtualCluster virtualClustersGet(resourceGroupName, virtualClusterName, subscriptionId, apiVersion)



Gets a virtual cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    VirtualClustersApi apiInstance = new VirtualClustersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String virtualClusterName = "virtualClusterName_example"; // String | The name of the virtual cluster.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      VirtualCluster result = apiInstance.virtualClustersGet(resourceGroupName, virtualClusterName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualClustersApi#virtualClustersGet");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **virtualClusterName** | **String**| The name of the virtual cluster. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**VirtualCluster**](VirtualCluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the specified virtual cluster. |  -  |
| **0** | *** Error Responses: ***   * 400 SubscriptionNotFound - The requested subscription was not found.   * 400 ManagementServiceFeatureDisabled - User attempted to use a feature which is disabled.   * 404 ResourceDoesNotExist - Resource with the name &#39;{0}&#39; does not exist. To continue, specify a valid resource name.   * 404 VirtualClusterNotInSubscriptionResourceGroup - specified virtual cluster does not exist in the specified resource group and subscription.   * 404 SubscriptionDoesNotHaveVirtualCluster - The requested virtual cluster was not found   * 404 ResourceNotFound - The requested resource was not found.   * 409 ConflictingVirtualClusterOperation - An operation is currently in progress for the virtual cluster.   * 429 ConflictingSubscriptionOperation - An operation is currently in progress for the subscription. |  -  |

<a id="virtualClustersList"></a>
# **virtualClustersList**
> VirtualClusterListResult virtualClustersList(subscriptionId, apiVersion)



Gets a list of all virtualClusters in the subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    VirtualClustersApi apiInstance = new VirtualClustersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      VirtualClusterListResult result = apiInstance.virtualClustersList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualClustersApi#virtualClustersList");
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
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**VirtualClusterListResult**](VirtualClusterListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of virtual clusters. |  -  |
| **0** | *** Error Responses: *** |  -  |

<a id="virtualClustersListByResourceGroup"></a>
# **virtualClustersListByResourceGroup**
> VirtualClusterListResult virtualClustersListByResourceGroup(resourceGroupName, subscriptionId, apiVersion)



Gets a list of virtual clusters in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    VirtualClustersApi apiInstance = new VirtualClustersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      VirtualClusterListResult result = apiInstance.virtualClustersListByResourceGroup(resourceGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualClustersApi#virtualClustersListByResourceGroup");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**VirtualClusterListResult**](VirtualClusterListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of virtual clusters. |  -  |
| **0** | *** Error Responses: ***   * 400 SubscriptionNotFound - The requested subscription was not found.   * 400 ManagementServiceFeatureDisabled - User attempted to use a feature which is disabled.   * 404 ResourceDoesNotExist - Resource with the name &#39;{0}&#39; does not exist. To continue, specify a valid resource name.   * 404 VirtualClusterNotInSubscriptionResourceGroup - specified virtual cluster does not exist in the specified resource group and subscription.   * 404 SubscriptionDoesNotHaveVirtualCluster - The requested virtual cluster was not found   * 404 ResourceNotFound - The requested resource was not found.   * 409 ConflictingVirtualClusterOperation - An operation is currently in progress for the virtual cluster.   * 429 ConflictingSubscriptionOperation - An operation is currently in progress for the subscription. |  -  |

<a id="virtualClustersUpdate"></a>
# **virtualClustersUpdate**
> VirtualCluster virtualClustersUpdate(resourceGroupName, virtualClusterName, subscriptionId, apiVersion, parameters)



Updates a virtual cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    VirtualClustersApi apiInstance = new VirtualClustersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String virtualClusterName = "virtualClusterName_example"; // String | The name of the virtual cluster.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    VirtualClusterUpdate parameters = new VirtualClusterUpdate(); // VirtualClusterUpdate | The requested managed instance resource state.
    try {
      VirtualCluster result = apiInstance.virtualClustersUpdate(resourceGroupName, virtualClusterName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualClustersApi#virtualClustersUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **virtualClusterName** | **String**| The name of the virtual cluster. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**VirtualClusterUpdate**](VirtualClusterUpdate.md)| The requested managed instance resource state. | |

### Return type

[**VirtualCluster**](VirtualCluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the virtual cluster. |  -  |
| **202** | Accepted |  -  |
| **0** | *** Error Responses: ***   * 400 SubscriptionNotFound - The requested subscription was not found.   * 400 ManagementServiceFeatureDisabled - User attempted to use a feature which is disabled.   * 404 ResourceDoesNotExist - Resource with the name &#39;{0}&#39; does not exist. To continue, specify a valid resource name.   * 404 VirtualClusterNotInSubscriptionResourceGroup - specified virtual cluster does not exist in the specified resource group and subscription.   * 404 SubscriptionDoesNotHaveVirtualCluster - The requested virtual cluster was not found   * 404 ResourceNotFound - The requested resource was not found.   * 409 ConflictingVirtualClusterOperation - An operation is currently in progress for the virtual cluster.   * 429 ConflictingSubscriptionOperation - An operation is currently in progress for the subscription. |  -  |

