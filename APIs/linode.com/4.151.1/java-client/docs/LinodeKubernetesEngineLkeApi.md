# LinodeKubernetesEngineLkeApi

All URIs are relative to *https://api.linode.com/v4*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createLKECluster**](LinodeKubernetesEngineLkeApi.md#createLKECluster) | **POST** /lke/clusters | Kubernetes Cluster Create |
| [**deleteLKECluster**](LinodeKubernetesEngineLkeApi.md#deleteLKECluster) | **DELETE** /lke/clusters/{clusterId} | Kubernetes Cluster Delete |
| [**deleteLKEClusterKubeconfig**](LinodeKubernetesEngineLkeApi.md#deleteLKEClusterKubeconfig) | **DELETE** /lke/clusters/{clusterId}/kubeconfig | Kubeconfig Delete |
| [**deleteLKEClusterNode**](LinodeKubernetesEngineLkeApi.md#deleteLKEClusterNode) | **DELETE** /lke/clusters/{clusterId}/nodes/{nodeId} | Node Delete |
| [**deleteLKENodePool**](LinodeKubernetesEngineLkeApi.md#deleteLKENodePool) | **DELETE** /lke/clusters/{clusterId}/pools/{poolId} | Node Pool Delete |
| [**getLKECluster**](LinodeKubernetesEngineLkeApi.md#getLKECluster) | **GET** /lke/clusters/{clusterId} | Kubernetes Cluster View |
| [**getLKEClusterAPIEndpoints**](LinodeKubernetesEngineLkeApi.md#getLKEClusterAPIEndpoints) | **GET** /lke/clusters/{clusterId}/api-endpoints | Kubernetes API Endpoints List |
| [**getLKEClusterDashboard**](LinodeKubernetesEngineLkeApi.md#getLKEClusterDashboard) | **GET** /lke/clusters/{clusterId}/dashboard | Kubernetes Cluster Dashboard URL View |
| [**getLKEClusterKubeconfig**](LinodeKubernetesEngineLkeApi.md#getLKEClusterKubeconfig) | **GET** /lke/clusters/{clusterId}/kubeconfig | Kubeconfig View |
| [**getLKEClusterNode**](LinodeKubernetesEngineLkeApi.md#getLKEClusterNode) | **GET** /lke/clusters/{clusterId}/nodes/{nodeId} | Node View |
| [**getLKEClusterPools**](LinodeKubernetesEngineLkeApi.md#getLKEClusterPools) | **GET** /lke/clusters/{clusterId}/pools | Node Pools List |
| [**getLKEClusters**](LinodeKubernetesEngineLkeApi.md#getLKEClusters) | **GET** /lke/clusters | Kubernetes Clusters List |
| [**getLKENodePool**](LinodeKubernetesEngineLkeApi.md#getLKENodePool) | **GET** /lke/clusters/{clusterId}/pools/{poolId} | Node Pool View |
| [**getLKEVersion**](LinodeKubernetesEngineLkeApi.md#getLKEVersion) | **GET** /lke/versions/{version} | Kubernetes Version View |
| [**getLKEVersions**](LinodeKubernetesEngineLkeApi.md#getLKEVersions) | **GET** /lke/versions | Kubernetes Versions List |
| [**postLKECServiceTokenDelete**](LinodeKubernetesEngineLkeApi.md#postLKECServiceTokenDelete) | **DELETE** /lke/clusters/{clusterId}/servicetoken | Service Token Delete |
| [**postLKEClusterNodeRecycle**](LinodeKubernetesEngineLkeApi.md#postLKEClusterNodeRecycle) | **POST** /lke/clusters/{clusterId}/nodes/{nodeId}/recycle | Node Recycle |
| [**postLKEClusterPoolRecycle**](LinodeKubernetesEngineLkeApi.md#postLKEClusterPoolRecycle) | **POST** /lke/clusters/{clusterId}/pools/{poolId}/recycle | Node Pool Recycle |
| [**postLKEClusterPools**](LinodeKubernetesEngineLkeApi.md#postLKEClusterPools) | **POST** /lke/clusters/{clusterId}/pools | Node Pool Create |
| [**postLKEClusterRecycle**](LinodeKubernetesEngineLkeApi.md#postLKEClusterRecycle) | **POST** /lke/clusters/{clusterId}/recycle | Cluster Nodes Recycle |
| [**postLKEClusterRegenerate**](LinodeKubernetesEngineLkeApi.md#postLKEClusterRegenerate) | **POST** /lke/clusters/{clusterId}/regenerate | Kubernetes Cluster Regenerate |
| [**putLKECluster**](LinodeKubernetesEngineLkeApi.md#putLKECluster) | **PUT** /lke/clusters/{clusterId} | Kubernetes Cluster Update |
| [**putLKENodePool**](LinodeKubernetesEngineLkeApi.md#putLKENodePool) | **PUT** /lke/clusters/{clusterId}/pools/{poolId} | Node Pool Update |


<a id="createLKECluster"></a>
# **createLKECluster**
> LKECluster createLKECluster(createLKEClusterRequest)

Kubernetes Cluster Create

Creates a Kubernetes cluster. The Kubernetes cluster will be created asynchronously. You can use the events system to determine when the Kubernetes cluster is ready to use. Please note that it often takes 2-5 minutes before the [Kubernetes API server endpoint](/docs/api/linode-kubernetes-engine-lke/#kubernetes-api-endpoints-list) and the [Kubeconfig file](/docs/api/linode-kubernetes-engine-lke/#kubeconfig-view) for the new cluster are ready. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeKubernetesEngineLkeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeKubernetesEngineLkeApi apiInstance = new LinodeKubernetesEngineLkeApi(defaultClient);
    CreateLKEClusterRequest createLKEClusterRequest = new CreateLKEClusterRequest(); // CreateLKEClusterRequest | Configuration for the Kubernetes cluster
    try {
      LKECluster result = apiInstance.createLKECluster(createLKEClusterRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeKubernetesEngineLkeApi#createLKECluster");
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
| **createLKEClusterRequest** | [**CreateLKEClusterRequest**](CreateLKEClusterRequest.md)| Configuration for the Kubernetes cluster | [optional] |

### Return type

[**LKECluster**](LKECluster.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Kubernetes cluster creation has started. |  -  |
| **0** | Error |  -  |

<a id="deleteLKECluster"></a>
# **deleteLKECluster**
> Object deleteLKECluster(clusterId)

Kubernetes Cluster Delete

Deletes a Cluster you have permission to &#x60;read_write&#x60;.  **Deleting a Cluster is a destructive action and cannot be undone.**  Deleting a Cluster:   - Deletes all Linodes in all pools within this Kubernetes cluster   - Deletes all supporting Kubernetes services for this Kubernetes     cluster (API server, etcd, etc)   - Deletes all NodeBalancers created by this Kubernetes cluster   - Does not delete any of the volumes created by this Kubernetes     cluster 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeKubernetesEngineLkeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeKubernetesEngineLkeApi apiInstance = new LinodeKubernetesEngineLkeApi(defaultClient);
    Integer clusterId = 56; // Integer | ID of the Kubernetes cluster to look up.
    try {
      Object result = apiInstance.deleteLKECluster(clusterId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeKubernetesEngineLkeApi#deleteLKECluster");
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
| **clusterId** | **Integer**| ID of the Kubernetes cluster to look up. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delete successful |  -  |
| **0** | Error |  -  |

<a id="deleteLKEClusterKubeconfig"></a>
# **deleteLKEClusterKubeconfig**
> Object deleteLKEClusterKubeconfig(clusterId)

Kubeconfig Delete

Delete and regenerate the Kubeconfig file for a Cluster. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeKubernetesEngineLkeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeKubernetesEngineLkeApi apiInstance = new LinodeKubernetesEngineLkeApi(defaultClient);
    Integer clusterId = 56; // Integer | ID of the Kubernetes cluster to look up.
    try {
      Object result = apiInstance.deleteLKEClusterKubeconfig(clusterId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeKubernetesEngineLkeApi#deleteLKEClusterKubeconfig");
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
| **clusterId** | **Integer**| ID of the Kubernetes cluster to look up. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Kubeconfig file deleted and regenerated successfully. |  -  |
| **0** | Error |  -  |

<a id="deleteLKEClusterNode"></a>
# **deleteLKEClusterNode**
> Object deleteLKEClusterNode(clusterId, nodeId)

Node Delete

Deletes a specific Node from a Node Pool.  **Deleting a Node is a destructive action and cannot be undone.**  Deleting a Node will reduce the size of the Node Pool it belongs to. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeKubernetesEngineLkeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeKubernetesEngineLkeApi apiInstance = new LinodeKubernetesEngineLkeApi(defaultClient);
    Integer clusterId = 56; // Integer | ID of the Kubernetes cluster containing the Node.
    String nodeId = "nodeId_example"; // String | ID of the Node to look up.
    try {
      Object result = apiInstance.deleteLKEClusterNode(clusterId, nodeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeKubernetesEngineLkeApi#deleteLKEClusterNode");
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
| **clusterId** | **Integer**| ID of the Kubernetes cluster containing the Node. | |
| **nodeId** | **String**| ID of the Node to look up. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delete successful |  -  |
| **0** | Error |  -  |

<a id="deleteLKENodePool"></a>
# **deleteLKENodePool**
> Object deleteLKENodePool(clusterId, poolId)

Node Pool Delete

Delete a specific Node Pool from a Kubernetes cluster.  **Deleting a Node Pool is a destructive action and cannot be undone.**  Deleting a Node Pool will delete all Linodes within that Pool. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeKubernetesEngineLkeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeKubernetesEngineLkeApi apiInstance = new LinodeKubernetesEngineLkeApi(defaultClient);
    Integer clusterId = 56; // Integer | ID of the Kubernetes cluster to look up.
    Integer poolId = 56; // Integer | ID of the Pool to look up
    try {
      Object result = apiInstance.deleteLKENodePool(clusterId, poolId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeKubernetesEngineLkeApi#deleteLKENodePool");
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
| **clusterId** | **Integer**| ID of the Kubernetes cluster to look up. | |
| **poolId** | **Integer**| ID of the Pool to look up | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delete successful |  -  |
| **0** | Error |  -  |

<a id="getLKECluster"></a>
# **getLKECluster**
> LKECluster getLKECluster(clusterId)

Kubernetes Cluster View

Get a specific Cluster by ID. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeKubernetesEngineLkeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeKubernetesEngineLkeApi apiInstance = new LinodeKubernetesEngineLkeApi(defaultClient);
    Integer clusterId = 56; // Integer | ID of the Kubernetes cluster to look up.
    try {
      LKECluster result = apiInstance.getLKECluster(clusterId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeKubernetesEngineLkeApi#getLKECluster");
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
| **clusterId** | **Integer**| ID of the Kubernetes cluster to look up. | |

### Return type

[**LKECluster**](LKECluster.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a single Kubernetes cluster. |  -  |
| **0** | Error |  -  |

<a id="getLKEClusterAPIEndpoints"></a>
# **getLKEClusterAPIEndpoints**
> GetLKEClusterAPIEndpoints200Response getLKEClusterAPIEndpoints(clusterId)

Kubernetes API Endpoints List

List the Kubernetes API server endpoints for this cluster. Please note that it often takes 2-5 minutes before the endpoint is ready after first [creating a new cluster](/docs/api/linode-kubernetes-engine-lke/#kubernetes-cluster-create). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeKubernetesEngineLkeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeKubernetesEngineLkeApi apiInstance = new LinodeKubernetesEngineLkeApi(defaultClient);
    Integer clusterId = 56; // Integer | ID of the Kubernetes cluster to look up.
    try {
      GetLKEClusterAPIEndpoints200Response result = apiInstance.getLKEClusterAPIEndpoints(clusterId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeKubernetesEngineLkeApi#getLKEClusterAPIEndpoints");
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
| **clusterId** | **Integer**| ID of the Kubernetes cluster to look up. | |

### Return type

[**GetLKEClusterAPIEndpoints200Response**](GetLKEClusterAPIEndpoints200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the Kubernetes API server endpoints for this cluster. |  -  |
| **0** | Error |  -  |

<a id="getLKEClusterDashboard"></a>
# **getLKEClusterDashboard**
> GetLKEClusterDashboard200Response getLKEClusterDashboard(clusterId)

Kubernetes Cluster Dashboard URL View

Get a [Kubernetes Dashboard](https://github.com/kubernetes/dashboard) access URL for this Cluster, which enables performance of administrative tasks through a web interface.  Dashboards are installed for Clusters by default.  To access the Cluster Dashboard login prompt, enter the URL in a web browser. Select either **Token** or **Kubeconfig** authentication, then select **Sign in**.  For additional guidance on using the Cluster Dashboard, see the [Navigating the Cluster Dashboard](/docs/guides/using-the-kubernetes-dashboard-on-lke/#navigating-the-cluster-dashboard) section of our guide on [Using the Kubernetes Dashboard on LKE](/docs/guides/using-the-kubernetes-dashboard-on-lke/). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeKubernetesEngineLkeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeKubernetesEngineLkeApi apiInstance = new LinodeKubernetesEngineLkeApi(defaultClient);
    Integer clusterId = 56; // Integer | ID of the Kubernetes cluster to look up.
    try {
      GetLKEClusterDashboard200Response result = apiInstance.getLKEClusterDashboard(clusterId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeKubernetesEngineLkeApi#getLKEClusterDashboard");
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
| **clusterId** | **Integer**| ID of the Kubernetes cluster to look up. | |

### Return type

[**GetLKEClusterDashboard200Response**](GetLKEClusterDashboard200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a Kubernetes Cluster Dashboard URL. |  -  |
| **0** | Error |  -  |

<a id="getLKEClusterKubeconfig"></a>
# **getLKEClusterKubeconfig**
> GetLKEClusterKubeconfig200Response getLKEClusterKubeconfig(clusterId)

Kubeconfig View

Get the Kubeconfig file for a Cluster. Please note that it often takes 2-5 minutes before the Kubeconfig file is ready after first [creating a new cluster](/docs/api/linode-kubernetes-engine-lke/#kubernetes-cluster-create). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeKubernetesEngineLkeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeKubernetesEngineLkeApi apiInstance = new LinodeKubernetesEngineLkeApi(defaultClient);
    Integer clusterId = 56; // Integer | ID of the Kubernetes cluster to look up.
    try {
      GetLKEClusterKubeconfig200Response result = apiInstance.getLKEClusterKubeconfig(clusterId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeKubernetesEngineLkeApi#getLKEClusterKubeconfig");
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
| **clusterId** | **Integer**| ID of the Kubernetes cluster to look up. | |

### Return type

[**GetLKEClusterKubeconfig200Response**](GetLKEClusterKubeconfig200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the Base64-encoded Kubeconfig file for this Kubernetes cluster. |  -  |
| **0** | Error |  -  |

<a id="getLKEClusterNode"></a>
# **getLKEClusterNode**
> GetLKEClusterNode200Response getLKEClusterNode(clusterId, nodeId)

Node View

Returns the values for a specified node object. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeKubernetesEngineLkeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeKubernetesEngineLkeApi apiInstance = new LinodeKubernetesEngineLkeApi(defaultClient);
    Integer clusterId = 56; // Integer | ID of the Kubernetes cluster containing the Node.
    String nodeId = "nodeId_example"; // String | ID of the Node to look up.
    try {
      GetLKEClusterNode200Response result = apiInstance.getLKEClusterNode(clusterId, nodeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeKubernetesEngineLkeApi#getLKEClusterNode");
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
| **clusterId** | **Integer**| ID of the Kubernetes cluster containing the Node. | |
| **nodeId** | **String**| ID of the Node to look up. | |

### Return type

[**GetLKEClusterNode200Response**](GetLKEClusterNode200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the values of a node object in the form that it appears currently in the node pool array. |  -  |
| **0** | Error |  -  |

<a id="getLKEClusterPools"></a>
# **getLKEClusterPools**
> GetLKEClusterPools200Response getLKEClusterPools(clusterId)

Node Pools List

Returns all active Node Pools on a Kubernetes cluster. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeKubernetesEngineLkeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeKubernetesEngineLkeApi apiInstance = new LinodeKubernetesEngineLkeApi(defaultClient);
    Integer clusterId = 56; // Integer | ID of the Kubernetes cluster to look up.
    try {
      GetLKEClusterPools200Response result = apiInstance.getLKEClusterPools(clusterId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeKubernetesEngineLkeApi#getLKEClusterPools");
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
| **clusterId** | **Integer**| ID of the Kubernetes cluster to look up. | |

### Return type

[**GetLKEClusterPools200Response**](GetLKEClusterPools200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of all Pools in this Kubernetes cluster. |  -  |
| **0** | Error |  -  |

<a id="getLKEClusters"></a>
# **getLKEClusters**
> GetLKEClusters200Response getLKEClusters()

Kubernetes Clusters List

Lists current Kubernetes clusters available on your account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeKubernetesEngineLkeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeKubernetesEngineLkeApi apiInstance = new LinodeKubernetesEngineLkeApi(defaultClient);
    try {
      GetLKEClusters200Response result = apiInstance.getLKEClusters();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeKubernetesEngineLkeApi#getLKEClusters");
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

[**GetLKEClusters200Response**](GetLKEClusters200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of all Kubernetes clusters on your Account. |  -  |
| **0** | Error |  -  |

<a id="getLKENodePool"></a>
# **getLKENodePool**
> LKENodePool getLKENodePool(clusterId, poolId)

Node Pool View

Get a specific Node Pool by ID. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeKubernetesEngineLkeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeKubernetesEngineLkeApi apiInstance = new LinodeKubernetesEngineLkeApi(defaultClient);
    Integer clusterId = 56; // Integer | ID of the Kubernetes cluster to look up.
    Integer poolId = 56; // Integer | ID of the Pool to look up
    try {
      LKENodePool result = apiInstance.getLKENodePool(clusterId, poolId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeKubernetesEngineLkeApi#getLKENodePool");
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
| **clusterId** | **Integer**| ID of the Kubernetes cluster to look up. | |
| **poolId** | **Integer**| ID of the Pool to look up | |

### Return type

[**LKENodePool**](LKENodePool.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the requested Node Pool. |  -  |

<a id="getLKEVersion"></a>
# **getLKEVersion**
> LKEVersion getLKEVersion(version)

Kubernetes Version View

View a Kubernetes version available for deployment to a Kubernetes cluster. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeKubernetesEngineLkeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeKubernetesEngineLkeApi apiInstance = new LinodeKubernetesEngineLkeApi(defaultClient);
    String version = "version_example"; // String | The LKE version to view.
    try {
      LKEVersion result = apiInstance.getLKEVersion(version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeKubernetesEngineLkeApi#getLKEVersion");
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
| **version** | **String**| The LKE version to view. | |

### Return type

[**LKEVersion**](LKEVersion.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a Kubernetes version object that is available for deployment to a Kubernetes cluster.  |  -  |
| **0** | Error |  -  |

<a id="getLKEVersions"></a>
# **getLKEVersions**
> GetLKEVersions200Response getLKEVersions()

Kubernetes Versions List

List the Kubernetes versions available for deployment to a Kubernetes cluster. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeKubernetesEngineLkeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeKubernetesEngineLkeApi apiInstance = new LinodeKubernetesEngineLkeApi(defaultClient);
    try {
      GetLKEVersions200Response result = apiInstance.getLKEVersions();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeKubernetesEngineLkeApi#getLKEVersions");
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

[**GetLKEVersions200Response**](GetLKEVersions200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a list of Kubernetes versions available for deployment to a Kubernetes cluster.  |  -  |
| **0** | Error |  -  |

<a id="postLKECServiceTokenDelete"></a>
# **postLKECServiceTokenDelete**
> Object postLKECServiceTokenDelete(clusterId)

Service Token Delete

Delete and regenerate the service account token for a Cluster.  **Note**: When regenerating a service account token, the Cluster&#39;s control plane components and Linode CSI drivers are also restarted and configured with the new token. High Availability Clusters should not experience any disruption, while standard Clusters may experience brief control plane downtime while components are restarted. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeKubernetesEngineLkeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeKubernetesEngineLkeApi apiInstance = new LinodeKubernetesEngineLkeApi(defaultClient);
    Integer clusterId = 56; // Integer | ID of the target Kubernetes cluster.
    try {
      Object result = apiInstance.postLKECServiceTokenDelete(clusterId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeKubernetesEngineLkeApi#postLKECServiceTokenDelete");
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
| **clusterId** | **Integer**| ID of the target Kubernetes cluster. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Service token deleted and regenerated successfully. |  -  |
| **0** | Error |  -  |

<a id="postLKEClusterNodeRecycle"></a>
# **postLKEClusterNodeRecycle**
> Object postLKEClusterNodeRecycle(clusterId, nodeId)

Node Recycle

Recycles an individual Node in the designated Kubernetes Cluster. The Node will be deleted and replaced with a new Linode, which may take a few minutes. Replacement Nodes are installed with the latest available patch for the Cluster&#39;s Kubernetes Version.  **Any local storage on deleted Linodes (such as \&quot;hostPath\&quot; and \&quot;emptyDir\&quot; volumes, or \&quot;local\&quot; PersistentVolumes) will be erased.** 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeKubernetesEngineLkeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeKubernetesEngineLkeApi apiInstance = new LinodeKubernetesEngineLkeApi(defaultClient);
    Integer clusterId = 56; // Integer | ID of the Kubernetes cluster containing the Node.
    String nodeId = "nodeId_example"; // String | ID of the Node to be recycled.
    try {
      Object result = apiInstance.postLKEClusterNodeRecycle(clusterId, nodeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeKubernetesEngineLkeApi#postLKEClusterNodeRecycle");
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
| **clusterId** | **Integer**| ID of the Kubernetes cluster containing the Node. | |
| **nodeId** | **String**| ID of the Node to be recycled. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Recycle request succeeded and is in progress. |  -  |
| **0** | Error |  -  |

<a id="postLKEClusterPoolRecycle"></a>
# **postLKEClusterPoolRecycle**
> Object postLKEClusterPoolRecycle(clusterId, poolId)

Node Pool Recycle

Recycles a Node Pool for the designated Kubernetes Cluster. All Linodes within the Node Pool will be deleted and replaced with new Linodes on a rolling basis, which may take several minutes. Replacement Nodes are installed with the latest available patch for the Cluster&#39;s Kubernetes Version.  **Any local storage on deleted Linodes (such as \&quot;hostPath\&quot; and \&quot;emptyDir\&quot; volumes, or \&quot;local\&quot; PersistentVolumes) will be erased.** 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeKubernetesEngineLkeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeKubernetesEngineLkeApi apiInstance = new LinodeKubernetesEngineLkeApi(defaultClient);
    Integer clusterId = 56; // Integer | ID of the Kubernetes cluster this Node Pool is attached to.
    Integer poolId = 56; // Integer | ID of the Node Pool to be recycled.
    try {
      Object result = apiInstance.postLKEClusterPoolRecycle(clusterId, poolId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeKubernetesEngineLkeApi#postLKEClusterPoolRecycle");
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
| **clusterId** | **Integer**| ID of the Kubernetes cluster this Node Pool is attached to. | |
| **poolId** | **Integer**| ID of the Node Pool to be recycled. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Recycle request succeeded and is in progress. |  -  |
| **0** | Error |  -  |

<a id="postLKEClusterPools"></a>
# **postLKEClusterPools**
> LKENodePool postLKEClusterPools(clusterId, UNKNOWN_BASE_TYPE)

Node Pool Create

Creates a new Node Pool for the designated Kubernetes cluster. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeKubernetesEngineLkeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeKubernetesEngineLkeApi apiInstance = new LinodeKubernetesEngineLkeApi(defaultClient);
    Integer clusterId = 56; // Integer | ID of the Kubernetes cluster to look up.
    UNKNOWN_BASE_TYPE UNKNOWN_BASE_TYPE = new HashMap(); // UNKNOWN_BASE_TYPE | Configuration for the Node Pool
    try {
      LKENodePool result = apiInstance.postLKEClusterPools(clusterId, UNKNOWN_BASE_TYPE);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeKubernetesEngineLkeApi#postLKEClusterPools");
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
| **clusterId** | **Integer**| ID of the Kubernetes cluster to look up. | |
| **UNKNOWN_BASE_TYPE** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| Configuration for the Node Pool | |

### Return type

[**LKENodePool**](LKENodePool.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Node Pool has been created. |  -  |
| **0** | Error |  -  |

<a id="postLKEClusterRecycle"></a>
# **postLKEClusterRecycle**
> Object postLKEClusterRecycle(clusterId)

Cluster Nodes Recycle

Recycles all nodes in all pools of a designated Kubernetes Cluster. All Linodes within the Cluster will be deleted and replaced with new Linodes on a rolling basis, which may take several minutes. Replacement Nodes are installed with the latest available [patch version](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/release/versioning.md#kubernetes-release-versioning) for the Cluster&#39;s current Kubernetes minor release.  **Any local storage on deleted Linodes (such as \&quot;hostPath\&quot; and \&quot;emptyDir\&quot; volumes, or \&quot;local\&quot; PersistentVolumes) will be erased.** 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeKubernetesEngineLkeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeKubernetesEngineLkeApi apiInstance = new LinodeKubernetesEngineLkeApi(defaultClient);
    Integer clusterId = 56; // Integer | ID of the Kubernetes cluster which contains nodes to be recycled.
    try {
      Object result = apiInstance.postLKEClusterRecycle(clusterId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeKubernetesEngineLkeApi#postLKEClusterRecycle");
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
| **clusterId** | **Integer**| ID of the Kubernetes cluster which contains nodes to be recycled. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Recycle request succeeded and is in progress. |  -  |
| **0** | Error |  -  |

<a id="postLKEClusterRegenerate"></a>
# **postLKEClusterRegenerate**
> Object postLKEClusterRegenerate(clusterId, postLKEClusterRegenerateRequest)

Kubernetes Cluster Regenerate

Regenerate the Kubeconfig file and/or the service account token for a Cluster.  This is a helper command that allows performing both the [Kubeconfig Delete](#kubeconfig-delete) and the [Service Token Delete](#service-token-delete) actions with a single request.  When using this command, at least one of &#x60;kubeconfig&#x60; or &#x60;servicetoken&#x60; is required.  **Note**: When regenerating a service account token, the Cluster&#39;s control plane components and Linode CSI drivers are also restarted and configured with the new token. High Availability Clusters should not experience any disruption, while standard Clusters may experience brief control plane downtime while components are restarted. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeKubernetesEngineLkeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeKubernetesEngineLkeApi apiInstance = new LinodeKubernetesEngineLkeApi(defaultClient);
    Integer clusterId = 56; // Integer | ID of the target Kubernetes cluster.
    PostLKEClusterRegenerateRequest postLKEClusterRegenerateRequest = new PostLKEClusterRegenerateRequest(); // PostLKEClusterRegenerateRequest | The Kubernetes Cluster Regenerate request object.
    try {
      Object result = apiInstance.postLKEClusterRegenerate(clusterId, postLKEClusterRegenerateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeKubernetesEngineLkeApi#postLKEClusterRegenerate");
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
| **clusterId** | **Integer**| ID of the target Kubernetes cluster. | |
| **postLKEClusterRegenerateRequest** | [**PostLKEClusterRegenerateRequest**](PostLKEClusterRegenerateRequest.md)| The Kubernetes Cluster Regenerate request object. | [optional] |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Regenerate request successful. |  -  |
| **0** | Error |  -  |

<a id="putLKECluster"></a>
# **putLKECluster**
> PutLKECluster200Response putLKECluster(clusterId, putLKEClusterRequest)

Kubernetes Cluster Update

Updates a Kubernetes cluster. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeKubernetesEngineLkeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeKubernetesEngineLkeApi apiInstance = new LinodeKubernetesEngineLkeApi(defaultClient);
    Integer clusterId = 56; // Integer | ID of the Kubernetes cluster to look up.
    PutLKEClusterRequest putLKEClusterRequest = new PutLKEClusterRequest(); // PutLKEClusterRequest | The fields to update the Kubernetes cluster.
    try {
      PutLKECluster200Response result = apiInstance.putLKECluster(clusterId, putLKEClusterRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeKubernetesEngineLkeApi#putLKECluster");
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
| **clusterId** | **Integer**| ID of the Kubernetes cluster to look up. | |
| **putLKEClusterRequest** | [**PutLKEClusterRequest**](PutLKEClusterRequest.md)| The fields to update the Kubernetes cluster. | [optional] |

### Return type

[**PutLKECluster200Response**](PutLKECluster200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a single Kubernetes cluster. |  -  |

<a id="putLKENodePool"></a>
# **putLKENodePool**
> LKENodePool putLKENodePool(clusterId, poolId, putLKENodePoolRequest)

Node Pool Update

Updates a Node Pool&#39;s count and autoscaler configuration.  Linodes will be created or deleted to match changes to the Node Pool&#39;s count.  **Any local storage on deleted Linodes (such as \&quot;hostPath\&quot; and \&quot;emptyDir\&quot; volumes, or \&quot;local\&quot; PersistentVolumes) will be erased.** 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeKubernetesEngineLkeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeKubernetesEngineLkeApi apiInstance = new LinodeKubernetesEngineLkeApi(defaultClient);
    Integer clusterId = 56; // Integer | ID of the Kubernetes cluster to look up.
    Integer poolId = 56; // Integer | ID of the Pool to look up
    PutLKENodePoolRequest putLKENodePoolRequest = new PutLKENodePoolRequest(); // PutLKENodePoolRequest | The fields to update
    try {
      LKENodePool result = apiInstance.putLKENodePool(clusterId, poolId, putLKENodePoolRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeKubernetesEngineLkeApi#putLKENodePool");
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
| **clusterId** | **Integer**| ID of the Kubernetes cluster to look up. | |
| **poolId** | **Integer**| ID of the Pool to look up | |
| **putLKENodePoolRequest** | [**PutLKENodePoolRequest**](PutLKENodePoolRequest.md)| The fields to update | [optional] |

### Return type

[**LKENodePool**](LKENodePool.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Node Pool was successfully modified. |  -  |

