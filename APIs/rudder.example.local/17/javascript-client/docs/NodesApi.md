# RudderApi.NodesApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applyPolicy**](NodesApi.md#applyPolicy) | **POST** /nodes/{nodeId}/applyPolicy | Trigger an agent run
[**applyPolicyAllNodes**](NodesApi.md#applyPolicyAllNodes) | **POST** /nodes/applyPolicy | Trigger an agent run on all nodes
[**changePendingNodeStatus**](NodesApi.md#changePendingNodeStatus) | **POST** /nodes/pending/{nodeId} | Update pending Node status
[**createNodes**](NodesApi.md#createNodes) | **PUT** /nodes | Create one or several new nodes
[**deleteNode**](NodesApi.md#deleteNode) | **DELETE** /nodes/{nodeId} | Delete a node
[**getNodesStatus**](NodesApi.md#getNodesStatus) | **GET** /nodes/status | Get nodes acceptation status
[**listAcceptedNodes**](NodesApi.md#listAcceptedNodes) | **GET** /nodes | List managed nodes
[**listPendingNodes**](NodesApi.md#listPendingNodes) | **GET** /nodes/pending | List pending nodes
[**nodeDetails**](NodesApi.md#nodeDetails) | **GET** /nodes/{nodeId} | Get information about a node
[**nodeInheritedProperties**](NodesApi.md#nodeInheritedProperties) | **GET** /nodes/{nodeId}/inheritedProperties | Get inherited node properties for a node
[**updateNode**](NodesApi.md#updateNode) | **POST** /nodes/{nodeId} | Update node settings and properties



## applyPolicy

> String applyPolicy(nodeId)

Trigger an agent run

This API allows to trigger an agent run on the target node. Response is a stream of the actual agent run on the node.

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.NodesApi();
let nodeId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the target node
apiInstance.applyPolicy(nodeId, (error, data, response) => {
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
 **nodeId** | **String**| Id of the target node | 

### Return type

**String**

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain


## applyPolicyAllNodes

> ApplyPolicyAllNodes200Response applyPolicyAllNodes()

Trigger an agent run on all nodes

This API allows to trigger an agent run on all nodes. Response contains a json stating if agent could be started on each node, but not if the run went fine and do not display any output from it. You can see the result of the run in Rudder web interface or in the each agent logs.

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.NodesApi();
apiInstance.applyPolicyAllNodes((error, data, response) => {
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

[**ApplyPolicyAllNodes200Response**](ApplyPolicyAllNodes200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## changePendingNodeStatus

> ChangePendingNodeStatus200Response changePendingNodeStatus(nodeId, opts)

Update pending Node status

Accept or refuse a pending node

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.NodesApi();
let nodeId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the target node
let opts = {
  'changePendingNodeStatusRequest': new RudderApi.ChangePendingNodeStatusRequest() // ChangePendingNodeStatusRequest | 
};
apiInstance.changePendingNodeStatus(nodeId, opts, (error, data, response) => {
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
 **nodeId** | **String**| Id of the target node | 
 **changePendingNodeStatusRequest** | [**ChangePendingNodeStatusRequest**](ChangePendingNodeStatusRequest.md)|  | [optional] 

### Return type

[**ChangePendingNodeStatus200Response**](ChangePendingNodeStatus200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNodes

> CreateNodes200Response createNodes(nodeAddInner)

Create one or several new nodes

Use the provided array of node information to create new nodes

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.NodesApi();
let nodeAddInner = [new RudderApi.NodeAddInner()]; // [NodeAddInner] | 
apiInstance.createNodes(nodeAddInner, (error, data, response) => {
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
 **nodeAddInner** | [**[NodeAddInner]**](NodeAddInner.md)|  | 

### Return type

[**CreateNodes200Response**](CreateNodes200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteNode

> DeleteNode200Response deleteNode(nodeId, opts)

Delete a node

Remove a node from the Rudder server. It won&#39;t be managed anymore.

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.NodesApi();
let nodeId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the target node
let opts = {
  'mode': "move" // String | Deletion mode to use, either move to trash ('move', default) or erase ('erase')
};
apiInstance.deleteNode(nodeId, opts, (error, data, response) => {
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
 **nodeId** | **String**| Id of the target node | 
 **mode** | **String**| Deletion mode to use, either move to trash (&#39;move&#39;, default) or erase (&#39;erase&#39;) | [optional] [default to &#39;move&#39;]

### Return type

[**DeleteNode200Response**](DeleteNode200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNodesStatus

> GetNodesStatus200Response getNodesStatus(ids)

Get nodes acceptation status

Get acceptation status (pending, accepted, deleted, unknown) of a list of nodes

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.NodesApi();
let ids = "8403353b-42c4-46f5-a08d-bc77a1a0bad9,root"; // String | Comma separated list of node Ids
apiInstance.getNodesStatus(ids, (error, data, response) => {
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
 **ids** | **String**| Comma separated list of node Ids | [default to &#39;default&#39;]

### Return type

[**GetNodesStatus200Response**](GetNodesStatus200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAcceptedNodes

> ListAcceptedNodes200Response listAcceptedNodes(opts)

List managed nodes

Get information about the nodes managed by the target server

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.NodesApi();
let opts = {
  'include': "minimal", // String | Level of information to include from the node inventory. Some base levels are defined (**minimal**, **default**, **full**). You can add fields you want to a base level by adding them to the list, possible values are keys from json answer. If you don't provide a base level, they will be added to `default` level, so if you only want os details, use `minimal,os` as the value for this parameter. * **minimal** includes: `id`, `hostname` and `status` * **default** includes **minimal** plus `architectureDescription`, `description`, `ipAddresses`, `lastRunDate`, `lastInventoryDate`, `machine`, `os`, `managementTechnology`, `policyServerId`, `properties` (be careful! Only node own properties, if you also need inherited properties, look at the dedicated `/nodes/{id}/inheritedProperties` endpoint), `policyMode `, `ram` and `timezone` * **full** includes: **default** plus `accounts`, `bios`, `controllers`, `environmentVariables`, `fileSystems`, `managementTechnologyDetails`, `memories`, `networkInterfaces`, `ports`, `processes`, `processors`, `slots`, `software`, `sound`, `storage`, `videos` and `virtualMachines`
  'query': null, // Object | The criterion you want to find for your nodes. Replaces the `where`, `composition` and `select` parameters in a single parameter.
  'where': [null], // [Object] | The criterion you want to find for your nodes
  'composition': "and", // String | Boolean operator to use between each  `where` criteria.
  'select': "'node'" // String | What kind of data we want to include. Here we can get policy servers/relay by setting `nodeAndPolicyServer`. Only used if `where` is defined.
};
apiInstance.listAcceptedNodes(opts, (error, data, response) => {
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
 **include** | **String**| Level of information to include from the node inventory. Some base levels are defined (**minimal**, **default**, **full**). You can add fields you want to a base level by adding them to the list, possible values are keys from json answer. If you don&#39;t provide a base level, they will be added to &#x60;default&#x60; level, so if you only want os details, use &#x60;minimal,os&#x60; as the value for this parameter. * **minimal** includes: &#x60;id&#x60;, &#x60;hostname&#x60; and &#x60;status&#x60; * **default** includes **minimal** plus &#x60;architectureDescription&#x60;, &#x60;description&#x60;, &#x60;ipAddresses&#x60;, &#x60;lastRunDate&#x60;, &#x60;lastInventoryDate&#x60;, &#x60;machine&#x60;, &#x60;os&#x60;, &#x60;managementTechnology&#x60;, &#x60;policyServerId&#x60;, &#x60;properties&#x60; (be careful! Only node own properties, if you also need inherited properties, look at the dedicated &#x60;/nodes/{id}/inheritedProperties&#x60; endpoint), &#x60;policyMode &#x60;, &#x60;ram&#x60; and &#x60;timezone&#x60; * **full** includes: **default** plus &#x60;accounts&#x60;, &#x60;bios&#x60;, &#x60;controllers&#x60;, &#x60;environmentVariables&#x60;, &#x60;fileSystems&#x60;, &#x60;managementTechnologyDetails&#x60;, &#x60;memories&#x60;, &#x60;networkInterfaces&#x60;, &#x60;ports&#x60;, &#x60;processes&#x60;, &#x60;processors&#x60;, &#x60;slots&#x60;, &#x60;software&#x60;, &#x60;sound&#x60;, &#x60;storage&#x60;, &#x60;videos&#x60; and &#x60;virtualMachines&#x60; | [optional] [default to &#39;default&#39;]
 **query** | [**Object**](.md)| The criterion you want to find for your nodes. Replaces the &#x60;where&#x60;, &#x60;composition&#x60; and &#x60;select&#x60; parameters in a single parameter. | [optional] 
 **where** | [**[Object]**](Object.md)| The criterion you want to find for your nodes | [optional] 
 **composition** | **String**| Boolean operator to use between each  &#x60;where&#x60; criteria. | [optional] [default to &#39;and&#39;]
 **select** | **String**| What kind of data we want to include. Here we can get policy servers/relay by setting &#x60;nodeAndPolicyServer&#x60;. Only used if &#x60;where&#x60; is defined. | [optional] [default to &#39;node&#39;]

### Return type

[**ListAcceptedNodes200Response**](ListAcceptedNodes200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPendingNodes

> ListPendingNodes200Response listPendingNodes(opts)

List pending nodes

Get information about the nodes pending acceptation

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.NodesApi();
let opts = {
  'include': "minimal", // String | Level of information to include from the node inventory. Some base levels are defined (**minimal**, **default**, **full**). You can add fields you want to a base level by adding them to the list, possible values are keys from json answer. If you don't provide a base level, they will be added to `default` level, so if you only want os details, use `minimal,os` as the value for this parameter. * **minimal** includes: `id`, `hostname` and `status` * **default** includes **minimal** plus `architectureDescription`, `description`, `ipAddresses`, `lastRunDate`, `lastInventoryDate`, `machine`, `os`, `managementTechnology`, `policyServerId`, `properties` (be careful! Only node own properties, if you also need inherited properties, look at the dedicated `/nodes/{id}/inheritedProperties` endpoint), `policyMode `, `ram` and `timezone` * **full** includes: **default** plus `accounts`, `bios`, `controllers`, `environmentVariables`, `fileSystems`, `managementTechnologyDetails`, `memories`, `networkInterfaces`, `ports`, `processes`, `processors`, `slots`, `software`, `sound`, `storage`, `videos` and `virtualMachines`
  'query': null, // Object | The criterion you want to find for your nodes. Replaces the `where`, `composition` and `select` parameters in a single parameter.
  'where': [null], // [Object] | The criterion you want to find for your nodes
  'composition': "and", // String | Boolean operator to use between each  `where` criteria.
  'select': "'node'" // String | What kind of data we want to include. Here we can get policy servers/relay by setting `nodeAndPolicyServer`. Only used if `where` is defined.
};
apiInstance.listPendingNodes(opts, (error, data, response) => {
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
 **include** | **String**| Level of information to include from the node inventory. Some base levels are defined (**minimal**, **default**, **full**). You can add fields you want to a base level by adding them to the list, possible values are keys from json answer. If you don&#39;t provide a base level, they will be added to &#x60;default&#x60; level, so if you only want os details, use &#x60;minimal,os&#x60; as the value for this parameter. * **minimal** includes: &#x60;id&#x60;, &#x60;hostname&#x60; and &#x60;status&#x60; * **default** includes **minimal** plus &#x60;architectureDescription&#x60;, &#x60;description&#x60;, &#x60;ipAddresses&#x60;, &#x60;lastRunDate&#x60;, &#x60;lastInventoryDate&#x60;, &#x60;machine&#x60;, &#x60;os&#x60;, &#x60;managementTechnology&#x60;, &#x60;policyServerId&#x60;, &#x60;properties&#x60; (be careful! Only node own properties, if you also need inherited properties, look at the dedicated &#x60;/nodes/{id}/inheritedProperties&#x60; endpoint), &#x60;policyMode &#x60;, &#x60;ram&#x60; and &#x60;timezone&#x60; * **full** includes: **default** plus &#x60;accounts&#x60;, &#x60;bios&#x60;, &#x60;controllers&#x60;, &#x60;environmentVariables&#x60;, &#x60;fileSystems&#x60;, &#x60;managementTechnologyDetails&#x60;, &#x60;memories&#x60;, &#x60;networkInterfaces&#x60;, &#x60;ports&#x60;, &#x60;processes&#x60;, &#x60;processors&#x60;, &#x60;slots&#x60;, &#x60;software&#x60;, &#x60;sound&#x60;, &#x60;storage&#x60;, &#x60;videos&#x60; and &#x60;virtualMachines&#x60; | [optional] [default to &#39;default&#39;]
 **query** | [**Object**](.md)| The criterion you want to find for your nodes. Replaces the &#x60;where&#x60;, &#x60;composition&#x60; and &#x60;select&#x60; parameters in a single parameter. | [optional] 
 **where** | [**[Object]**](Object.md)| The criterion you want to find for your nodes | [optional] 
 **composition** | **String**| Boolean operator to use between each  &#x60;where&#x60; criteria. | [optional] [default to &#39;and&#39;]
 **select** | **String**| What kind of data we want to include. Here we can get policy servers/relay by setting &#x60;nodeAndPolicyServer&#x60;. Only used if &#x60;where&#x60; is defined. | [optional] [default to &#39;node&#39;]

### Return type

[**ListPendingNodes200Response**](ListPendingNodes200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nodeDetails

> NodeDetails200Response nodeDetails(nodeId, opts)

Get information about a node

Get details about a given node

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.NodesApi();
let nodeId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the target node
let opts = {
  'include': "minimal" // String | Level of information to include from the node inventory. Some base levels are defined (**minimal**, **default**, **full**). You can add fields you want to a base level by adding them to the list, possible values are keys from json answer. If you don't provide a base level, they will be added to `default` level, so if you only want os details, use `minimal,os` as the value for this parameter. * **minimal** includes: `id`, `hostname` and `status` * **default** includes **minimal** plus `architectureDescription`, `description`, `ipAddresses`, `lastRunDate`, `lastInventoryDate`, `machine`, `os`, `managementTechnology`, `policyServerId`, `properties` (be careful! Only node own properties, if you also need inherited properties, look at the dedicated `/nodes/{id}/inheritedProperties` endpoint), `policyMode `, `ram` and `timezone` * **full** includes: **default** plus `accounts`, `bios`, `controllers`, `environmentVariables`, `fileSystems`, `managementTechnologyDetails`, `memories`, `networkInterfaces`, `ports`, `processes`, `processors`, `slots`, `software`, `sound`, `storage`, `videos` and `virtualMachines`
};
apiInstance.nodeDetails(nodeId, opts, (error, data, response) => {
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
 **nodeId** | **String**| Id of the target node | 
 **include** | **String**| Level of information to include from the node inventory. Some base levels are defined (**minimal**, **default**, **full**). You can add fields you want to a base level by adding them to the list, possible values are keys from json answer. If you don&#39;t provide a base level, they will be added to &#x60;default&#x60; level, so if you only want os details, use &#x60;minimal,os&#x60; as the value for this parameter. * **minimal** includes: &#x60;id&#x60;, &#x60;hostname&#x60; and &#x60;status&#x60; * **default** includes **minimal** plus &#x60;architectureDescription&#x60;, &#x60;description&#x60;, &#x60;ipAddresses&#x60;, &#x60;lastRunDate&#x60;, &#x60;lastInventoryDate&#x60;, &#x60;machine&#x60;, &#x60;os&#x60;, &#x60;managementTechnology&#x60;, &#x60;policyServerId&#x60;, &#x60;properties&#x60; (be careful! Only node own properties, if you also need inherited properties, look at the dedicated &#x60;/nodes/{id}/inheritedProperties&#x60; endpoint), &#x60;policyMode &#x60;, &#x60;ram&#x60; and &#x60;timezone&#x60; * **full** includes: **default** plus &#x60;accounts&#x60;, &#x60;bios&#x60;, &#x60;controllers&#x60;, &#x60;environmentVariables&#x60;, &#x60;fileSystems&#x60;, &#x60;managementTechnologyDetails&#x60;, &#x60;memories&#x60;, &#x60;networkInterfaces&#x60;, &#x60;ports&#x60;, &#x60;processes&#x60;, &#x60;processors&#x60;, &#x60;slots&#x60;, &#x60;software&#x60;, &#x60;sound&#x60;, &#x60;storage&#x60;, &#x60;videos&#x60; and &#x60;virtualMachines&#x60; | [optional] [default to &#39;default&#39;]

### Return type

[**NodeDetails200Response**](NodeDetails200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nodeInheritedProperties

> NodeInheritedProperties200Response nodeInheritedProperties(nodeId)

Get inherited node properties for a node

This API returns all node properties for a node, including group inherited ones.

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.NodesApi();
let nodeId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the target node
apiInstance.nodeInheritedProperties(nodeId, (error, data, response) => {
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
 **nodeId** | **String**| Id of the target node | 

### Return type

[**NodeInheritedProperties200Response**](NodeInheritedProperties200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateNode

> UpdateNode200Response updateNode(nodeId, opts)

Update node settings and properties

Update node settings and properties

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.NodesApi();
let nodeId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the target node
let opts = {
  'nodeSettings': new RudderApi.NodeSettings() // NodeSettings | 
};
apiInstance.updateNode(nodeId, opts, (error, data, response) => {
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
 **nodeId** | **String**| Id of the target node | 
 **nodeSettings** | [**NodeSettings**](NodeSettings.md)|  | [optional] 

### Return type

[**UpdateNode200Response**](UpdateNode200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

