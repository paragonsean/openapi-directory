# LinodeApi.LinodeKubernetesEngineLKEApi

All URIs are relative to *https://api.linode.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createLKECluster**](LinodeKubernetesEngineLKEApi.md#createLKECluster) | **POST** /lke/clusters | Kubernetes Cluster Create
[**deleteLKECluster**](LinodeKubernetesEngineLKEApi.md#deleteLKECluster) | **DELETE** /lke/clusters/{clusterId} | Kubernetes Cluster Delete
[**deleteLKEClusterKubeconfig**](LinodeKubernetesEngineLKEApi.md#deleteLKEClusterKubeconfig) | **DELETE** /lke/clusters/{clusterId}/kubeconfig | Kubeconfig Delete
[**deleteLKEClusterNode**](LinodeKubernetesEngineLKEApi.md#deleteLKEClusterNode) | **DELETE** /lke/clusters/{clusterId}/nodes/{nodeId} | Node Delete
[**deleteLKENodePool**](LinodeKubernetesEngineLKEApi.md#deleteLKENodePool) | **DELETE** /lke/clusters/{clusterId}/pools/{poolId} | Node Pool Delete
[**getLKECluster**](LinodeKubernetesEngineLKEApi.md#getLKECluster) | **GET** /lke/clusters/{clusterId} | Kubernetes Cluster View
[**getLKEClusterAPIEndpoints**](LinodeKubernetesEngineLKEApi.md#getLKEClusterAPIEndpoints) | **GET** /lke/clusters/{clusterId}/api-endpoints | Kubernetes API Endpoints List
[**getLKEClusterDashboard**](LinodeKubernetesEngineLKEApi.md#getLKEClusterDashboard) | **GET** /lke/clusters/{clusterId}/dashboard | Kubernetes Cluster Dashboard URL View
[**getLKEClusterKubeconfig**](LinodeKubernetesEngineLKEApi.md#getLKEClusterKubeconfig) | **GET** /lke/clusters/{clusterId}/kubeconfig | Kubeconfig View
[**getLKEClusterNode**](LinodeKubernetesEngineLKEApi.md#getLKEClusterNode) | **GET** /lke/clusters/{clusterId}/nodes/{nodeId} | Node View
[**getLKEClusterPools**](LinodeKubernetesEngineLKEApi.md#getLKEClusterPools) | **GET** /lke/clusters/{clusterId}/pools | Node Pools List
[**getLKEClusters**](LinodeKubernetesEngineLKEApi.md#getLKEClusters) | **GET** /lke/clusters | Kubernetes Clusters List
[**getLKENodePool**](LinodeKubernetesEngineLKEApi.md#getLKENodePool) | **GET** /lke/clusters/{clusterId}/pools/{poolId} | Node Pool View
[**getLKEVersion**](LinodeKubernetesEngineLKEApi.md#getLKEVersion) | **GET** /lke/versions/{version} | Kubernetes Version View
[**getLKEVersions**](LinodeKubernetesEngineLKEApi.md#getLKEVersions) | **GET** /lke/versions | Kubernetes Versions List
[**postLKECServiceTokenDelete**](LinodeKubernetesEngineLKEApi.md#postLKECServiceTokenDelete) | **DELETE** /lke/clusters/{clusterId}/servicetoken | Service Token Delete
[**postLKEClusterNodeRecycle**](LinodeKubernetesEngineLKEApi.md#postLKEClusterNodeRecycle) | **POST** /lke/clusters/{clusterId}/nodes/{nodeId}/recycle | Node Recycle
[**postLKEClusterPoolRecycle**](LinodeKubernetesEngineLKEApi.md#postLKEClusterPoolRecycle) | **POST** /lke/clusters/{clusterId}/pools/{poolId}/recycle | Node Pool Recycle
[**postLKEClusterPools**](LinodeKubernetesEngineLKEApi.md#postLKEClusterPools) | **POST** /lke/clusters/{clusterId}/pools | Node Pool Create
[**postLKEClusterRecycle**](LinodeKubernetesEngineLKEApi.md#postLKEClusterRecycle) | **POST** /lke/clusters/{clusterId}/recycle | Cluster Nodes Recycle
[**postLKEClusterRegenerate**](LinodeKubernetesEngineLKEApi.md#postLKEClusterRegenerate) | **POST** /lke/clusters/{clusterId}/regenerate | Kubernetes Cluster Regenerate
[**putLKECluster**](LinodeKubernetesEngineLKEApi.md#putLKECluster) | **PUT** /lke/clusters/{clusterId} | Kubernetes Cluster Update
[**putLKENodePool**](LinodeKubernetesEngineLKEApi.md#putLKENodePool) | **PUT** /lke/clusters/{clusterId}/pools/{poolId} | Node Pool Update



## createLKECluster

> LKECluster createLKECluster(opts)

Kubernetes Cluster Create

Creates a Kubernetes cluster. The Kubernetes cluster will be created asynchronously. You can use the events system to determine when the Kubernetes cluster is ready to use. Please note that it often takes 2-5 minutes before the [Kubernetes API server endpoint](/docs/api/linode-kubernetes-engine-lke/#kubernetes-api-endpoints-list) and the [Kubeconfig file](/docs/api/linode-kubernetes-engine-lke/#kubeconfig-view) for the new cluster are ready. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeKubernetesEngineLKEApi();
let opts = {
  'createLKEClusterRequest': new LinodeApi.CreateLKEClusterRequest() // CreateLKEClusterRequest | Configuration for the Kubernetes cluster
};
apiInstance.createLKECluster(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createLKEClusterRequest** | [**CreateLKEClusterRequest**](CreateLKEClusterRequest.md)| Configuration for the Kubernetes cluster | [optional] 

### Return type

[**LKECluster**](LKECluster.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteLKECluster

> Object deleteLKECluster(clusterId)

Kubernetes Cluster Delete

Deletes a Cluster you have permission to &#x60;read_write&#x60;.  **Deleting a Cluster is a destructive action and cannot be undone.**  Deleting a Cluster:   - Deletes all Linodes in all pools within this Kubernetes cluster   - Deletes all supporting Kubernetes services for this Kubernetes     cluster (API server, etcd, etc)   - Deletes all NodeBalancers created by this Kubernetes cluster   - Does not delete any of the volumes created by this Kubernetes     cluster 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeKubernetesEngineLKEApi();
let clusterId = 56; // Number | ID of the Kubernetes cluster to look up.
apiInstance.deleteLKECluster(clusterId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **Number**| ID of the Kubernetes cluster to look up. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteLKEClusterKubeconfig

> Object deleteLKEClusterKubeconfig(clusterId)

Kubeconfig Delete

Delete and regenerate the Kubeconfig file for a Cluster. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeKubernetesEngineLKEApi();
let clusterId = 56; // Number | ID of the Kubernetes cluster to look up.
apiInstance.deleteLKEClusterKubeconfig(clusterId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **Number**| ID of the Kubernetes cluster to look up. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteLKEClusterNode

> Object deleteLKEClusterNode(clusterId, nodeId)

Node Delete

Deletes a specific Node from a Node Pool.  **Deleting a Node is a destructive action and cannot be undone.**  Deleting a Node will reduce the size of the Node Pool it belongs to. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeKubernetesEngineLKEApi();
let clusterId = 56; // Number | ID of the Kubernetes cluster containing the Node.
let nodeId = "nodeId_example"; // String | ID of the Node to look up.
apiInstance.deleteLKEClusterNode(clusterId, nodeId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **Number**| ID of the Kubernetes cluster containing the Node. | 
 **nodeId** | **String**| ID of the Node to look up. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteLKENodePool

> Object deleteLKENodePool(clusterId, poolId)

Node Pool Delete

Delete a specific Node Pool from a Kubernetes cluster.  **Deleting a Node Pool is a destructive action and cannot be undone.**  Deleting a Node Pool will delete all Linodes within that Pool. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeKubernetesEngineLKEApi();
let clusterId = 56; // Number | ID of the Kubernetes cluster to look up.
let poolId = 56; // Number | ID of the Pool to look up
apiInstance.deleteLKENodePool(clusterId, poolId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **Number**| ID of the Kubernetes cluster to look up. | 
 **poolId** | **Number**| ID of the Pool to look up | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLKECluster

> LKECluster getLKECluster(clusterId)

Kubernetes Cluster View

Get a specific Cluster by ID. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeKubernetesEngineLKEApi();
let clusterId = 56; // Number | ID of the Kubernetes cluster to look up.
apiInstance.getLKECluster(clusterId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **Number**| ID of the Kubernetes cluster to look up. | 

### Return type

[**LKECluster**](LKECluster.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLKEClusterAPIEndpoints

> GetLKEClusterAPIEndpoints200Response getLKEClusterAPIEndpoints(clusterId)

Kubernetes API Endpoints List

List the Kubernetes API server endpoints for this cluster. Please note that it often takes 2-5 minutes before the endpoint is ready after first [creating a new cluster](/docs/api/linode-kubernetes-engine-lke/#kubernetes-cluster-create). 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeKubernetesEngineLKEApi();
let clusterId = 56; // Number | ID of the Kubernetes cluster to look up.
apiInstance.getLKEClusterAPIEndpoints(clusterId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **Number**| ID of the Kubernetes cluster to look up. | 

### Return type

[**GetLKEClusterAPIEndpoints200Response**](GetLKEClusterAPIEndpoints200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLKEClusterDashboard

> GetLKEClusterDashboard200Response getLKEClusterDashboard(clusterId)

Kubernetes Cluster Dashboard URL View

Get a [Kubernetes Dashboard](https://github.com/kubernetes/dashboard) access URL for this Cluster, which enables performance of administrative tasks through a web interface.  Dashboards are installed for Clusters by default.  To access the Cluster Dashboard login prompt, enter the URL in a web browser. Select either **Token** or **Kubeconfig** authentication, then select **Sign in**.  For additional guidance on using the Cluster Dashboard, see the [Navigating the Cluster Dashboard](/docs/guides/using-the-kubernetes-dashboard-on-lke/#navigating-the-cluster-dashboard) section of our guide on [Using the Kubernetes Dashboard on LKE](/docs/guides/using-the-kubernetes-dashboard-on-lke/). 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeKubernetesEngineLKEApi();
let clusterId = 56; // Number | ID of the Kubernetes cluster to look up.
apiInstance.getLKEClusterDashboard(clusterId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **Number**| ID of the Kubernetes cluster to look up. | 

### Return type

[**GetLKEClusterDashboard200Response**](GetLKEClusterDashboard200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLKEClusterKubeconfig

> GetLKEClusterKubeconfig200Response getLKEClusterKubeconfig(clusterId)

Kubeconfig View

Get the Kubeconfig file for a Cluster. Please note that it often takes 2-5 minutes before the Kubeconfig file is ready after first [creating a new cluster](/docs/api/linode-kubernetes-engine-lke/#kubernetes-cluster-create). 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeKubernetesEngineLKEApi();
let clusterId = 56; // Number | ID of the Kubernetes cluster to look up.
apiInstance.getLKEClusterKubeconfig(clusterId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **Number**| ID of the Kubernetes cluster to look up. | 

### Return type

[**GetLKEClusterKubeconfig200Response**](GetLKEClusterKubeconfig200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLKEClusterNode

> GetLKEClusterNode200Response getLKEClusterNode(clusterId, nodeId)

Node View

Returns the values for a specified node object. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeKubernetesEngineLKEApi();
let clusterId = 56; // Number | ID of the Kubernetes cluster containing the Node.
let nodeId = "nodeId_example"; // String | ID of the Node to look up.
apiInstance.getLKEClusterNode(clusterId, nodeId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **Number**| ID of the Kubernetes cluster containing the Node. | 
 **nodeId** | **String**| ID of the Node to look up. | 

### Return type

[**GetLKEClusterNode200Response**](GetLKEClusterNode200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLKEClusterPools

> GetLKEClusterPools200Response getLKEClusterPools(clusterId)

Node Pools List

Returns all active Node Pools on a Kubernetes cluster. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeKubernetesEngineLKEApi();
let clusterId = 56; // Number | ID of the Kubernetes cluster to look up.
apiInstance.getLKEClusterPools(clusterId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **Number**| ID of the Kubernetes cluster to look up. | 

### Return type

[**GetLKEClusterPools200Response**](GetLKEClusterPools200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLKEClusters

> GetLKEClusters200Response getLKEClusters()

Kubernetes Clusters List

Lists current Kubernetes clusters available on your account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeKubernetesEngineLKEApi();
apiInstance.getLKEClusters((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## getLKENodePool

> LKENodePool getLKENodePool(clusterId, poolId)

Node Pool View

Get a specific Node Pool by ID. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeKubernetesEngineLKEApi();
let clusterId = 56; // Number | ID of the Kubernetes cluster to look up.
let poolId = 56; // Number | ID of the Pool to look up
apiInstance.getLKENodePool(clusterId, poolId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **Number**| ID of the Kubernetes cluster to look up. | 
 **poolId** | **Number**| ID of the Pool to look up | 

### Return type

[**LKENodePool**](LKENodePool.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLKEVersion

> LKEVersion getLKEVersion(version)

Kubernetes Version View

View a Kubernetes version available for deployment to a Kubernetes cluster. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeKubernetesEngineLKEApi();
let version = "version_example"; // String | The LKE version to view.
apiInstance.getLKEVersion(version, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **String**| The LKE version to view. | 

### Return type

[**LKEVersion**](LKEVersion.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLKEVersions

> GetLKEVersions200Response getLKEVersions()

Kubernetes Versions List

List the Kubernetes versions available for deployment to a Kubernetes cluster. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeKubernetesEngineLKEApi();
apiInstance.getLKEVersions((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## postLKECServiceTokenDelete

> Object postLKECServiceTokenDelete(clusterId)

Service Token Delete

Delete and regenerate the service account token for a Cluster.  **Note**: When regenerating a service account token, the Cluster&#39;s control plane components and Linode CSI drivers are also restarted and configured with the new token. High Availability Clusters should not experience any disruption, while standard Clusters may experience brief control plane downtime while components are restarted. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeKubernetesEngineLKEApi();
let clusterId = 56; // Number | ID of the target Kubernetes cluster.
apiInstance.postLKECServiceTokenDelete(clusterId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **Number**| ID of the target Kubernetes cluster. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postLKEClusterNodeRecycle

> Object postLKEClusterNodeRecycle(clusterId, nodeId)

Node Recycle

Recycles an individual Node in the designated Kubernetes Cluster. The Node will be deleted and replaced with a new Linode, which may take a few minutes. Replacement Nodes are installed with the latest available patch for the Cluster&#39;s Kubernetes Version.  **Any local storage on deleted Linodes (such as \&quot;hostPath\&quot; and \&quot;emptyDir\&quot; volumes, or \&quot;local\&quot; PersistentVolumes) will be erased.** 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeKubernetesEngineLKEApi();
let clusterId = 56; // Number | ID of the Kubernetes cluster containing the Node.
let nodeId = "nodeId_example"; // String | ID of the Node to be recycled.
apiInstance.postLKEClusterNodeRecycle(clusterId, nodeId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **Number**| ID of the Kubernetes cluster containing the Node. | 
 **nodeId** | **String**| ID of the Node to be recycled. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postLKEClusterPoolRecycle

> Object postLKEClusterPoolRecycle(clusterId, poolId)

Node Pool Recycle

Recycles a Node Pool for the designated Kubernetes Cluster. All Linodes within the Node Pool will be deleted and replaced with new Linodes on a rolling basis, which may take several minutes. Replacement Nodes are installed with the latest available patch for the Cluster&#39;s Kubernetes Version.  **Any local storage on deleted Linodes (such as \&quot;hostPath\&quot; and \&quot;emptyDir\&quot; volumes, or \&quot;local\&quot; PersistentVolumes) will be erased.** 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeKubernetesEngineLKEApi();
let clusterId = 56; // Number | ID of the Kubernetes cluster this Node Pool is attached to.
let poolId = 56; // Number | ID of the Node Pool to be recycled.
apiInstance.postLKEClusterPoolRecycle(clusterId, poolId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **Number**| ID of the Kubernetes cluster this Node Pool is attached to. | 
 **poolId** | **Number**| ID of the Node Pool to be recycled. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postLKEClusterPools

> LKENodePool postLKEClusterPools(clusterId, UNKNOWN_BASE_TYPE)

Node Pool Create

Creates a new Node Pool for the designated Kubernetes cluster. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeKubernetesEngineLKEApi();
let clusterId = 56; // Number | ID of the Kubernetes cluster to look up.
let UNKNOWN_BASE_TYPE = {key: null}; // UNKNOWN_BASE_TYPE | Configuration for the Node Pool
apiInstance.postLKEClusterPools(clusterId, UNKNOWN_BASE_TYPE, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **Number**| ID of the Kubernetes cluster to look up. | 
 **UNKNOWN_BASE_TYPE** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| Configuration for the Node Pool | 

### Return type

[**LKENodePool**](LKENodePool.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postLKEClusterRecycle

> Object postLKEClusterRecycle(clusterId)

Cluster Nodes Recycle

Recycles all nodes in all pools of a designated Kubernetes Cluster. All Linodes within the Cluster will be deleted and replaced with new Linodes on a rolling basis, which may take several minutes. Replacement Nodes are installed with the latest available [patch version](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/release/versioning.md#kubernetes-release-versioning) for the Cluster&#39;s current Kubernetes minor release.  **Any local storage on deleted Linodes (such as \&quot;hostPath\&quot; and \&quot;emptyDir\&quot; volumes, or \&quot;local\&quot; PersistentVolumes) will be erased.** 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeKubernetesEngineLKEApi();
let clusterId = 56; // Number | ID of the Kubernetes cluster which contains nodes to be recycled.
apiInstance.postLKEClusterRecycle(clusterId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **Number**| ID of the Kubernetes cluster which contains nodes to be recycled. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postLKEClusterRegenerate

> Object postLKEClusterRegenerate(clusterId, opts)

Kubernetes Cluster Regenerate

Regenerate the Kubeconfig file and/or the service account token for a Cluster.  This is a helper command that allows performing both the [Kubeconfig Delete](#kubeconfig-delete) and the [Service Token Delete](#service-token-delete) actions with a single request.  When using this command, at least one of &#x60;kubeconfig&#x60; or &#x60;servicetoken&#x60; is required.  **Note**: When regenerating a service account token, the Cluster&#39;s control plane components and Linode CSI drivers are also restarted and configured with the new token. High Availability Clusters should not experience any disruption, while standard Clusters may experience brief control plane downtime while components are restarted. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeKubernetesEngineLKEApi();
let clusterId = 56; // Number | ID of the target Kubernetes cluster.
let opts = {
  'postLKEClusterRegenerateRequest': new LinodeApi.PostLKEClusterRegenerateRequest() // PostLKEClusterRegenerateRequest | The Kubernetes Cluster Regenerate request object.
};
apiInstance.postLKEClusterRegenerate(clusterId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **Number**| ID of the target Kubernetes cluster. | 
 **postLKEClusterRegenerateRequest** | [**PostLKEClusterRegenerateRequest**](PostLKEClusterRegenerateRequest.md)| The Kubernetes Cluster Regenerate request object. | [optional] 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putLKECluster

> PutLKECluster200Response putLKECluster(clusterId, opts)

Kubernetes Cluster Update

Updates a Kubernetes cluster. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeKubernetesEngineLKEApi();
let clusterId = 56; // Number | ID of the Kubernetes cluster to look up.
let opts = {
  'putLKEClusterRequest': new LinodeApi.PutLKEClusterRequest() // PutLKEClusterRequest | The fields to update the Kubernetes cluster.
};
apiInstance.putLKECluster(clusterId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **Number**| ID of the Kubernetes cluster to look up. | 
 **putLKEClusterRequest** | [**PutLKEClusterRequest**](PutLKEClusterRequest.md)| The fields to update the Kubernetes cluster. | [optional] 

### Return type

[**PutLKECluster200Response**](PutLKECluster200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putLKENodePool

> LKENodePool putLKENodePool(clusterId, poolId, opts)

Node Pool Update

Updates a Node Pool&#39;s count and autoscaler configuration.  Linodes will be created or deleted to match changes to the Node Pool&#39;s count.  **Any local storage on deleted Linodes (such as \&quot;hostPath\&quot; and \&quot;emptyDir\&quot; volumes, or \&quot;local\&quot; PersistentVolumes) will be erased.** 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeKubernetesEngineLKEApi();
let clusterId = 56; // Number | ID of the Kubernetes cluster to look up.
let poolId = 56; // Number | ID of the Pool to look up
let opts = {
  'putLKENodePoolRequest': new LinodeApi.PutLKENodePoolRequest() // PutLKENodePoolRequest | The fields to update
};
apiInstance.putLKENodePool(clusterId, poolId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **Number**| ID of the Kubernetes cluster to look up. | 
 **poolId** | **Number**| ID of the Pool to look up | 
 **putLKENodePoolRequest** | [**PutLKENodePoolRequest**](PutLKENodePoolRequest.md)| The fields to update | [optional] 

### Return type

[**LKENodePool**](LKENodePool.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

