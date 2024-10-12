# ClustersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**clustersCreateOrUpdate**](ClustersApi.md#clustersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/clusters/{clusterName} |  |
| [**clustersDelete**](ClustersApi.md#clustersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/clusters/{clusterName} |  |
| [**clustersGet**](ClustersApi.md#clustersGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/clusters/{clusterName} |  |
| [**clustersList**](ClustersApi.md#clustersList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.OperationalInsights/clusters |  |
| [**clustersListByResourceGroup**](ClustersApi.md#clustersListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/clusters |  |
| [**clustersUpdate**](ClustersApi.md#clustersUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/clusters/{clusterName} |  |


<a id="clustersCreateOrUpdate"></a>
# **clustersCreateOrUpdate**
> Cluster clustersCreateOrUpdate(resourceGroupName, clusterName, apiVersion, subscriptionId, parameters)



Create or update a Log Analytics cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ClustersApi apiInstance = new ClustersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the Log Analytics cluster.
    String clusterName = "clusterName_example"; // String | The name of the Log Analytics cluster.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    Cluster parameters = new Cluster(); // Cluster | The parameters required to create or update a Log Analytics cluster.
    try {
      Cluster result = apiInstance.clustersCreateOrUpdate(resourceGroupName, clusterName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClustersApi#clustersCreateOrUpdate");
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
| **resourceGroupName** | **String**| The resource group name of the Log Analytics cluster. | |
| **clusterName** | **String**| The name of the Log Analytics cluster. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**Cluster**](Cluster.md)| The parameters required to create or update a Log Analytics cluster. | |

### Return type

[**Cluster**](Cluster.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |
| **201** | Created response definition. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="clustersDelete"></a>
# **clustersDelete**
> clustersDelete(resourceGroupName, clusterName, apiVersion, subscriptionId)



Deletes a cluster instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ClustersApi apiInstance = new ClustersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the Log Analytics cluster.
    String clusterName = "clusterName_example"; // String | Name of the Log Analytics Cluster.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.clustersDelete(resourceGroupName, clusterName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClustersApi#clustersDelete");
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
| **resourceGroupName** | **String**| The resource group name of the Log Analytics cluster. | |
| **clusterName** | **String**| Name of the Log Analytics Cluster. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
| **200** | OK response definition. |  -  |
| **204** | NoContent response definition. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="clustersGet"></a>
# **clustersGet**
> Cluster clustersGet(resourceGroupName, clusterName, apiVersion, subscriptionId)



Gets a Log Analytics cluster instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ClustersApi apiInstance = new ClustersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the Log Analytics cluster.
    String clusterName = "clusterName_example"; // String | Name of the Log Analytics Cluster.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      Cluster result = apiInstance.clustersGet(resourceGroupName, clusterName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClustersApi#clustersGet");
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
| **resourceGroupName** | **String**| The resource group name of the Log Analytics cluster. | |
| **clusterName** | **String**| Name of the Log Analytics Cluster. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**Cluster**](Cluster.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="clustersList"></a>
# **clustersList**
> ClusterListResult clustersList(apiVersion, subscriptionId)



Gets the Log Analytics clusters in a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ClustersApi apiInstance = new ClustersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ClusterListResult result = apiInstance.clustersList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClustersApi#clustersList");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ClusterListResult**](ClusterListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="clustersListByResourceGroup"></a>
# **clustersListByResourceGroup**
> ClusterListResult clustersListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Gets Log Analytics clusters in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ClustersApi apiInstance = new ClustersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ClusterListResult result = apiInstance.clustersListByResourceGroup(resourceGroupName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClustersApi#clustersListByResourceGroup");
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
| **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ClusterListResult**](ClusterListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="clustersUpdate"></a>
# **clustersUpdate**
> Cluster clustersUpdate(resourceGroupName, clusterName, apiVersion, subscriptionId, parameters)



Updates a Log Analytics cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ClustersApi apiInstance = new ClustersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the cluster.
    String clusterName = "clusterName_example"; // String | The name of the cluster.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    ClusterPatch parameters = new ClusterPatch(); // ClusterPatch | The parameters required to patch a Log Analytics cluster.
    try {
      Cluster result = apiInstance.clustersUpdate(resourceGroupName, clusterName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClustersApi#clustersUpdate");
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
| **resourceGroupName** | **String**| The resource group name of the cluster. | |
| **clusterName** | **String**| The name of the cluster. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**ClusterPatch**](ClusterPatch.md)| The parameters required to patch a Log Analytics cluster. | |

### Return type

[**Cluster**](Cluster.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The existing cluster was successfully updated. Check provisioningStatus to see detailed status. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

