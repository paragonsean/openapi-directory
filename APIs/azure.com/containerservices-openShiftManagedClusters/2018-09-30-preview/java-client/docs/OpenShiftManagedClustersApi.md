# OpenShiftManagedClustersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**openShiftManagedClustersCreateOrUpdate**](OpenShiftManagedClustersApi.md#openShiftManagedClustersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/openShiftManagedClusters/{resourceName} | Creates or updates an OpenShift managed cluster. |
| [**openShiftManagedClustersDelete**](OpenShiftManagedClustersApi.md#openShiftManagedClustersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/openShiftManagedClusters/{resourceName} | Deletes an OpenShift managed cluster. |
| [**openShiftManagedClustersGet**](OpenShiftManagedClustersApi.md#openShiftManagedClustersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/openShiftManagedClusters/{resourceName} | Gets a OpenShift managed cluster. |
| [**openShiftManagedClustersList**](OpenShiftManagedClustersApi.md#openShiftManagedClustersList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ContainerService/openShiftManagedClusters | Gets a list of OpenShift managed clusters in the specified subscription. |
| [**openShiftManagedClustersListByResourceGroup**](OpenShiftManagedClustersApi.md#openShiftManagedClustersListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/openShiftManagedClusters | Lists OpenShift managed clusters in the specified subscription and resource group. |
| [**openShiftManagedClustersUpdateTags**](OpenShiftManagedClustersApi.md#openShiftManagedClustersUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/openShiftManagedClusters/{resourceName} | Updates tags on an OpenShift managed cluster. |


<a id="openShiftManagedClustersCreateOrUpdate"></a>
# **openShiftManagedClustersCreateOrUpdate**
> OpenShiftManagedCluster openShiftManagedClustersCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, parameters)

Creates or updates an OpenShift managed cluster.

Creates or updates a OpenShift managed cluster with the specified configuration for agents and OpenShift version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpenShiftManagedClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OpenShiftManagedClustersApi apiInstance = new OpenShiftManagedClustersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String resourceName = "resourceName_example"; // String | The name of the OpenShift managed cluster resource.
    OpenShiftManagedCluster parameters = new OpenShiftManagedCluster(); // OpenShiftManagedCluster | Parameters supplied to the Create or Update an OpenShift Managed Cluster operation.
    try {
      OpenShiftManagedCluster result = apiInstance.openShiftManagedClustersCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpenShiftManagedClustersApi#openShiftManagedClustersCreateOrUpdate");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **resourceName** | **String**| The name of the OpenShift managed cluster resource. | |
| **parameters** | [**OpenShiftManagedCluster**](OpenShiftManagedCluster.md)| Parameters supplied to the Create or Update an OpenShift Managed Cluster operation. | |

### Return type

[**OpenShiftManagedCluster**](OpenShiftManagedCluster.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **0** | Error response describing why the operation failed. If the cluster doesn&#39;t exist, 404 (Not found) is returned.If any of the input parameters is wrong, 400(Bad Request) is returned. |  -  |

<a id="openShiftManagedClustersDelete"></a>
# **openShiftManagedClustersDelete**
> openShiftManagedClustersDelete(apiVersion, subscriptionId, resourceGroupName, resourceName)

Deletes an OpenShift managed cluster.

Deletes the OpenShift managed cluster with a specified resource group and name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpenShiftManagedClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OpenShiftManagedClustersApi apiInstance = new OpenShiftManagedClustersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String resourceName = "resourceName_example"; // String | The name of the OpenShift managed cluster resource.
    try {
      apiInstance.openShiftManagedClustersDelete(apiVersion, subscriptionId, resourceGroupName, resourceName);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpenShiftManagedClustersApi#openShiftManagedClustersDelete");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **resourceName** | **String**| The name of the OpenShift managed cluster resource. | |

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
| **202** | Accepted |  -  |
| **204** | NoContent |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="openShiftManagedClustersGet"></a>
# **openShiftManagedClustersGet**
> OpenShiftManagedCluster openShiftManagedClustersGet(apiVersion, subscriptionId, resourceGroupName, resourceName)

Gets a OpenShift managed cluster.

Gets the details of the managed OpenShift cluster with a specified resource group and name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpenShiftManagedClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OpenShiftManagedClustersApi apiInstance = new OpenShiftManagedClustersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String resourceName = "resourceName_example"; // String | The name of the OpenShift managed cluster resource.
    try {
      OpenShiftManagedCluster result = apiInstance.openShiftManagedClustersGet(apiVersion, subscriptionId, resourceGroupName, resourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpenShiftManagedClustersApi#openShiftManagedClustersGet");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **resourceName** | **String**| The name of the OpenShift managed cluster resource. | |

### Return type

[**OpenShiftManagedCluster**](OpenShiftManagedCluster.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. If the cluster doesn&#39;t exist, 404 (Not found) is returned. |  -  |

<a id="openShiftManagedClustersList"></a>
# **openShiftManagedClustersList**
> OpenShiftManagedClusterListResult openShiftManagedClustersList(apiVersion, subscriptionId)

Gets a list of OpenShift managed clusters in the specified subscription.

Gets a list of OpenShift managed clusters in the specified subscription. The operation returns properties of each OpenShift managed cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpenShiftManagedClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OpenShiftManagedClustersApi apiInstance = new OpenShiftManagedClustersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      OpenShiftManagedClusterListResult result = apiInstance.openShiftManagedClustersList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpenShiftManagedClustersApi#openShiftManagedClustersList");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**OpenShiftManagedClusterListResult**](OpenShiftManagedClusterListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="openShiftManagedClustersListByResourceGroup"></a>
# **openShiftManagedClustersListByResourceGroup**
> OpenShiftManagedClusterListResult openShiftManagedClustersListByResourceGroup(apiVersion, subscriptionId, resourceGroupName)

Lists OpenShift managed clusters in the specified subscription and resource group.

Lists OpenShift managed clusters in the specified subscription and resource group. The operation returns properties of each OpenShift managed cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpenShiftManagedClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OpenShiftManagedClustersApi apiInstance = new OpenShiftManagedClustersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    try {
      OpenShiftManagedClusterListResult result = apiInstance.openShiftManagedClustersListByResourceGroup(apiVersion, subscriptionId, resourceGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpenShiftManagedClustersApi#openShiftManagedClustersListByResourceGroup");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |

### Return type

[**OpenShiftManagedClusterListResult**](OpenShiftManagedClusterListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="openShiftManagedClustersUpdateTags"></a>
# **openShiftManagedClustersUpdateTags**
> OpenShiftManagedCluster openShiftManagedClustersUpdateTags(apiVersion, subscriptionId, resourceGroupName, resourceName, parameters)

Updates tags on an OpenShift managed cluster.

Updates an OpenShift managed cluster with the specified tags.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpenShiftManagedClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OpenShiftManagedClustersApi apiInstance = new OpenShiftManagedClustersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String resourceName = "resourceName_example"; // String | The name of the OpenShift managed cluster resource.
    TagsObject parameters = new TagsObject(); // TagsObject | Parameters supplied to the Update OpenShift Managed Cluster Tags operation.
    try {
      OpenShiftManagedCluster result = apiInstance.openShiftManagedClustersUpdateTags(apiVersion, subscriptionId, resourceGroupName, resourceName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpenShiftManagedClustersApi#openShiftManagedClustersUpdateTags");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **resourceName** | **String**| The name of the OpenShift managed cluster resource. | |
| **parameters** | [**TagsObject**](TagsObject.md)| Parameters supplied to the Update OpenShift Managed Cluster Tags operation. | |

### Return type

[**OpenShiftManagedCluster**](OpenShiftManagedCluster.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. If the cluster doesn&#39;t exist, 404 (Not found) is returned. If any of the input parameters is wrong, 400(Bad Request) is returned. |  -  |

