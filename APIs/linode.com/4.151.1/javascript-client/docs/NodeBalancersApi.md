# LinodeApi.NodeBalancersApi

All URIs are relative to *https://api.linode.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNodeBalancer**](NodeBalancersApi.md#createNodeBalancer) | **POST** /nodebalancers | NodeBalancer Create
[**createNodeBalancerConfig**](NodeBalancersApi.md#createNodeBalancerConfig) | **POST** /nodebalancers/{nodeBalancerId}/configs | Config Create
[**createNodeBalancerNode**](NodeBalancersApi.md#createNodeBalancerNode) | **POST** /nodebalancers/{nodeBalancerId}/configs/{configId}/nodes | Node Create
[**deleteNodeBalancer**](NodeBalancersApi.md#deleteNodeBalancer) | **DELETE** /nodebalancers/{nodeBalancerId} | NodeBalancer Delete
[**deleteNodeBalancerConfig**](NodeBalancersApi.md#deleteNodeBalancerConfig) | **DELETE** /nodebalancers/{nodeBalancerId}/configs/{configId} | Config Delete
[**deleteNodeBalancerConfigNode**](NodeBalancersApi.md#deleteNodeBalancerConfigNode) | **DELETE** /nodebalancers/{nodeBalancerId}/configs/{configId}/nodes/{nodeId} | Node Delete
[**getNodeBalancer**](NodeBalancersApi.md#getNodeBalancer) | **GET** /nodebalancers/{nodeBalancerId} | NodeBalancer View
[**getNodeBalancerConfig**](NodeBalancersApi.md#getNodeBalancerConfig) | **GET** /nodebalancers/{nodeBalancerId}/configs/{configId} | Config View
[**getNodeBalancerConfigNodes**](NodeBalancersApi.md#getNodeBalancerConfigNodes) | **GET** /nodebalancers/{nodeBalancerId}/configs/{configId}/nodes | Nodes List
[**getNodeBalancerConfigs**](NodeBalancersApi.md#getNodeBalancerConfigs) | **GET** /nodebalancers/{nodeBalancerId}/configs | Configs List
[**getNodeBalancerNode**](NodeBalancersApi.md#getNodeBalancerNode) | **GET** /nodebalancers/{nodeBalancerId}/configs/{configId}/nodes/{nodeId} | Node View
[**getNodeBalancers**](NodeBalancersApi.md#getNodeBalancers) | **GET** /nodebalancers | NodeBalancers List
[**nodebalancersNodeBalancerIdStatsGet**](NodeBalancersApi.md#nodebalancersNodeBalancerIdStatsGet) | **GET** /nodebalancers/{nodeBalancerId}/stats | NodeBalancer Statistics View
[**rebuildNodeBalancerConfig**](NodeBalancersApi.md#rebuildNodeBalancerConfig) | **POST** /nodebalancers/{nodeBalancerId}/configs/{configId}/rebuild | Config Rebuild
[**updateNodeBalancer**](NodeBalancersApi.md#updateNodeBalancer) | **PUT** /nodebalancers/{nodeBalancerId} | NodeBalancer Update
[**updateNodeBalancerConfig**](NodeBalancersApi.md#updateNodeBalancerConfig) | **PUT** /nodebalancers/{nodeBalancerId}/configs/{configId} | Config Update
[**updateNodeBalancerNode**](NodeBalancersApi.md#updateNodeBalancerNode) | **PUT** /nodebalancers/{nodeBalancerId}/configs/{configId}/nodes/{nodeId} | Node Update



## createNodeBalancer

> NodeBalancer createNodeBalancer(createNodeBalancerRequest)

NodeBalancer Create

Creates a NodeBalancer in the requested Region.  NodeBalancers require a port Config with at least one backend Node to start serving requests.  When using the Linode CLI to create a NodeBalancer, first create a NodeBalancer without any Configs. Then, create Configs and Nodes for that NodeBalancer with the respective [Config Create](/docs/api/nodebalancers/#config-create) and [Node Create](/docs/api/nodebalancers/#node-create) commands. 

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

let apiInstance = new LinodeApi.NodeBalancersApi();
let createNodeBalancerRequest = new LinodeApi.CreateNodeBalancerRequest(); // CreateNodeBalancerRequest | Information about the NodeBalancer to create.
apiInstance.createNodeBalancer(createNodeBalancerRequest, (error, data, response) => {
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
 **createNodeBalancerRequest** | [**CreateNodeBalancerRequest**](CreateNodeBalancerRequest.md)| Information about the NodeBalancer to create. | 

### Return type

[**NodeBalancer**](NodeBalancer.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNodeBalancerConfig

> NodeBalancerConfig createNodeBalancerConfig(nodeBalancerId, opts)

Config Create

Creates a NodeBalancer Config, which allows the NodeBalancer to accept traffic on a new port. You will need to add NodeBalancer Nodes to the new Config before it can actually serve requests. 

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

let apiInstance = new LinodeApi.NodeBalancersApi();
let nodeBalancerId = 56; // Number | The ID of the NodeBalancer to access.
let opts = {
  'nodeBalancerConfig': new LinodeApi.NodeBalancerConfig() // NodeBalancerConfig | Information about the port to configure.
};
apiInstance.createNodeBalancerConfig(nodeBalancerId, opts, (error, data, response) => {
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
 **nodeBalancerId** | **Number**| The ID of the NodeBalancer to access. | 
 **nodeBalancerConfig** | [**NodeBalancerConfig**](NodeBalancerConfig.md)| Information about the port to configure. | [optional] 

### Return type

[**NodeBalancerConfig**](NodeBalancerConfig.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNodeBalancerNode

> NodeBalancerNode createNodeBalancerNode(nodeBalancerId, configId, nodeBalancerNode)

Node Create

Creates a NodeBalancer Node, a backend that can accept traffic for this NodeBalancer Config. Nodes are routed requests on the configured port based on their status. 

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

let apiInstance = new LinodeApi.NodeBalancersApi();
let nodeBalancerId = 56; // Number | The ID of the NodeBalancer to access.
let configId = 56; // Number | The ID of the NodeBalancer config to access.
let nodeBalancerNode = new LinodeApi.NodeBalancerNode(); // NodeBalancerNode | Information about the Node to create.
apiInstance.createNodeBalancerNode(nodeBalancerId, configId, nodeBalancerNode, (error, data, response) => {
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
 **nodeBalancerId** | **Number**| The ID of the NodeBalancer to access. | 
 **configId** | **Number**| The ID of the NodeBalancer config to access. | 
 **nodeBalancerNode** | [**NodeBalancerNode**](NodeBalancerNode.md)| Information about the Node to create. | 

### Return type

[**NodeBalancerNode**](NodeBalancerNode.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteNodeBalancer

> Object deleteNodeBalancer(nodeBalancerId)

NodeBalancer Delete

Deletes a NodeBalancer.  **This is a destructive action and cannot be undone.**  Deleting a NodeBalancer will also delete all associated Configs and Nodes, although the backend servers represented by the Nodes will not be changed or removed. Deleting a NodeBalancer will cause you to lose access to the IP Addresses assigned to this NodeBalancer. 

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

let apiInstance = new LinodeApi.NodeBalancersApi();
let nodeBalancerId = 56; // Number | The ID of the NodeBalancer to access.
apiInstance.deleteNodeBalancer(nodeBalancerId, (error, data, response) => {
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
 **nodeBalancerId** | **Number**| The ID of the NodeBalancer to access. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteNodeBalancerConfig

> Object deleteNodeBalancerConfig(nodeBalancerId, configId)

Config Delete

Deletes the Config for a port of this NodeBalancer.  **This cannot be undone.**  Once completed, this NodeBalancer will no longer respond to requests on the given port. This also deletes all associated NodeBalancerNodes, but the Linodes they were routing traffic to will be unchanged and will not be removed. 

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

let apiInstance = new LinodeApi.NodeBalancersApi();
let nodeBalancerId = 56; // Number | The ID of the NodeBalancer to access.
let configId = 56; // Number | The ID of the config to access.
apiInstance.deleteNodeBalancerConfig(nodeBalancerId, configId, (error, data, response) => {
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
 **nodeBalancerId** | **Number**| The ID of the NodeBalancer to access. | 
 **configId** | **Number**| The ID of the config to access. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteNodeBalancerConfigNode

> Object deleteNodeBalancerConfigNode(nodeBalancerId, configId, nodeId)

Node Delete

Deletes a Node from this Config. This backend will no longer receive traffic for the configured port of this NodeBalancer.  This does not change or remove the Linode whose address was used in the creation of this Node. 

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

let apiInstance = new LinodeApi.NodeBalancersApi();
let nodeBalancerId = 56; // Number | The ID of the NodeBalancer to access.
let configId = 56; // Number | The ID of the Config to access
let nodeId = 56; // Number | The ID of the Node to access
apiInstance.deleteNodeBalancerConfigNode(nodeBalancerId, configId, nodeId, (error, data, response) => {
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
 **nodeBalancerId** | **Number**| The ID of the NodeBalancer to access. | 
 **configId** | **Number**| The ID of the Config to access | 
 **nodeId** | **Number**| The ID of the Node to access | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNodeBalancer

> NodeBalancer getNodeBalancer(nodeBalancerId)

NodeBalancer View

Returns a single NodeBalancer you can access. 

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

let apiInstance = new LinodeApi.NodeBalancersApi();
let nodeBalancerId = 56; // Number | The ID of the NodeBalancer to access.
apiInstance.getNodeBalancer(nodeBalancerId, (error, data, response) => {
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
 **nodeBalancerId** | **Number**| The ID of the NodeBalancer to access. | 

### Return type

[**NodeBalancer**](NodeBalancer.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNodeBalancerConfig

> NodeBalancerConfig getNodeBalancerConfig(nodeBalancerId, configId)

Config View

Returns configuration information for a single port of this NodeBalancer. 

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

let apiInstance = new LinodeApi.NodeBalancersApi();
let nodeBalancerId = 56; // Number | The ID of the NodeBalancer to access.
let configId = 56; // Number | The ID of the config to access.
apiInstance.getNodeBalancerConfig(nodeBalancerId, configId, (error, data, response) => {
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
 **nodeBalancerId** | **Number**| The ID of the NodeBalancer to access. | 
 **configId** | **Number**| The ID of the config to access. | 

### Return type

[**NodeBalancerConfig**](NodeBalancerConfig.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNodeBalancerConfigNodes

> GetNodeBalancerConfigNodes200Response getNodeBalancerConfigNodes(nodeBalancerId, configId, opts)

Nodes List

Returns a paginated list of NodeBalancer nodes associated with this Config. These are the backends that will be sent traffic for this port. 

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

let apiInstance = new LinodeApi.NodeBalancersApi();
let nodeBalancerId = 56; // Number | The ID of the NodeBalancer to access.
let configId = 56; // Number | The ID of the NodeBalancer config to access.
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getNodeBalancerConfigNodes(nodeBalancerId, configId, opts, (error, data, response) => {
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
 **nodeBalancerId** | **Number**| The ID of the NodeBalancer to access. | 
 **configId** | **Number**| The ID of the NodeBalancer config to access. | 
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetNodeBalancerConfigNodes200Response**](GetNodeBalancerConfigNodes200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNodeBalancerConfigs

> GetNodeBalancerConfigs200Response getNodeBalancerConfigs(nodeBalancerId, opts)

Configs List

Returns a paginated list of NodeBalancer Configs associated with this NodeBalancer. NodeBalancer Configs represent individual ports that this NodeBalancer will accept traffic on, one Config per port.  For example, if you wanted to accept standard HTTP traffic, you would need a Config listening on port 80. 

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

let apiInstance = new LinodeApi.NodeBalancersApi();
let nodeBalancerId = 56; // Number | The ID of the NodeBalancer to access.
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getNodeBalancerConfigs(nodeBalancerId, opts, (error, data, response) => {
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
 **nodeBalancerId** | **Number**| The ID of the NodeBalancer to access. | 
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetNodeBalancerConfigs200Response**](GetNodeBalancerConfigs200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNodeBalancerNode

> NodeBalancerNode getNodeBalancerNode(nodeBalancerId, configId, nodeId)

Node View

Returns information about a single Node, a backend for this NodeBalancer&#39;s configured port. 

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

let apiInstance = new LinodeApi.NodeBalancersApi();
let nodeBalancerId = 56; // Number | The ID of the NodeBalancer to access.
let configId = 56; // Number | The ID of the Config to access
let nodeId = 56; // Number | The ID of the Node to access
apiInstance.getNodeBalancerNode(nodeBalancerId, configId, nodeId, (error, data, response) => {
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
 **nodeBalancerId** | **Number**| The ID of the NodeBalancer to access. | 
 **configId** | **Number**| The ID of the Config to access | 
 **nodeId** | **Number**| The ID of the Node to access | 

### Return type

[**NodeBalancerNode**](NodeBalancerNode.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNodeBalancers

> GetLinodeNodeBalancers200Response getNodeBalancers(opts)

NodeBalancers List

Returns a paginated list of NodeBalancers you have access to. 

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

let apiInstance = new LinodeApi.NodeBalancersApi();
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getNodeBalancers(opts, (error, data, response) => {
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
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetLinodeNodeBalancers200Response**](GetLinodeNodeBalancers200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nodebalancersNodeBalancerIdStatsGet

> NodeBalancerStats nodebalancersNodeBalancerIdStatsGet(nodeBalancerId)

NodeBalancer Statistics View

Returns detailed statistics about the requested NodeBalancer. 

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

let apiInstance = new LinodeApi.NodeBalancersApi();
let nodeBalancerId = 56; // Number | The ID of the NodeBalancer to access.
apiInstance.nodebalancersNodeBalancerIdStatsGet(nodeBalancerId, (error, data, response) => {
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
 **nodeBalancerId** | **Number**| The ID of the NodeBalancer to access. | 

### Return type

[**NodeBalancerStats**](NodeBalancerStats.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## rebuildNodeBalancerConfig

> NodeBalancerConfig rebuildNodeBalancerConfig(nodeBalancerId, configId, rebuildNodeBalancerConfigRequest)

Config Rebuild

Rebuilds a NodeBalancer Config and its Nodes that you have permission to modify.  Use this command to update a NodeBalancer&#39;s Config and Nodes with a single request. 

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

let apiInstance = new LinodeApi.NodeBalancersApi();
let nodeBalancerId = 56; // Number | The ID of the NodeBalancer to access.
let configId = 56; // Number | The ID of the Config to access.
let rebuildNodeBalancerConfigRequest = new LinodeApi.RebuildNodeBalancerConfigRequest(); // RebuildNodeBalancerConfigRequest | Information about the NodeBalancer Config to rebuild. 
apiInstance.rebuildNodeBalancerConfig(nodeBalancerId, configId, rebuildNodeBalancerConfigRequest, (error, data, response) => {
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
 **nodeBalancerId** | **Number**| The ID of the NodeBalancer to access. | 
 **configId** | **Number**| The ID of the Config to access. | 
 **rebuildNodeBalancerConfigRequest** | [**RebuildNodeBalancerConfigRequest**](RebuildNodeBalancerConfigRequest.md)| Information about the NodeBalancer Config to rebuild.  | 

### Return type

[**NodeBalancerConfig**](NodeBalancerConfig.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNodeBalancer

> NodeBalancer updateNodeBalancer(nodeBalancerId, nodeBalancer)

NodeBalancer Update

Updates information about a NodeBalancer you can access. 

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

let apiInstance = new LinodeApi.NodeBalancersApi();
let nodeBalancerId = 56; // Number | The ID of the NodeBalancer to access.
let nodeBalancer = new LinodeApi.NodeBalancer(); // NodeBalancer | The information to update.
apiInstance.updateNodeBalancer(nodeBalancerId, nodeBalancer, (error, data, response) => {
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
 **nodeBalancerId** | **Number**| The ID of the NodeBalancer to access. | 
 **nodeBalancer** | [**NodeBalancer**](NodeBalancer.md)| The information to update. | 

### Return type

[**NodeBalancer**](NodeBalancer.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNodeBalancerConfig

> NodeBalancerConfig updateNodeBalancerConfig(nodeBalancerId, configId, nodeBalancerConfig)

Config Update

Updates the configuration for a single port on a NodeBalancer. 

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

let apiInstance = new LinodeApi.NodeBalancersApi();
let nodeBalancerId = 56; // Number | The ID of the NodeBalancer to access.
let configId = 56; // Number | The ID of the config to access.
let nodeBalancerConfig = new LinodeApi.NodeBalancerConfig(); // NodeBalancerConfig | The fields to update.
apiInstance.updateNodeBalancerConfig(nodeBalancerId, configId, nodeBalancerConfig, (error, data, response) => {
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
 **nodeBalancerId** | **Number**| The ID of the NodeBalancer to access. | 
 **configId** | **Number**| The ID of the config to access. | 
 **nodeBalancerConfig** | [**NodeBalancerConfig**](NodeBalancerConfig.md)| The fields to update. | 

### Return type

[**NodeBalancerConfig**](NodeBalancerConfig.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNodeBalancerNode

> NodeBalancerNode updateNodeBalancerNode(nodeBalancerId, configId, nodeId, nodeBalancerNode)

Node Update

Updates information about a Node, a backend for this NodeBalancer&#39;s configured port. 

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

let apiInstance = new LinodeApi.NodeBalancersApi();
let nodeBalancerId = 56; // Number | The ID of the NodeBalancer to access.
let configId = 56; // Number | The ID of the Config to access
let nodeId = 56; // Number | The ID of the Node to access
let nodeBalancerNode = new LinodeApi.NodeBalancerNode(); // NodeBalancerNode | The fields to update.
apiInstance.updateNodeBalancerNode(nodeBalancerId, configId, nodeId, nodeBalancerNode, (error, data, response) => {
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
 **nodeBalancerId** | **Number**| The ID of the NodeBalancer to access. | 
 **configId** | **Number**| The ID of the Config to access | 
 **nodeId** | **Number**| The ID of the Node to access | 
 **nodeBalancerNode** | [**NodeBalancerNode**](NodeBalancerNode.md)| The fields to update. | 

### Return type

[**NodeBalancerNode**](NodeBalancerNode.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

