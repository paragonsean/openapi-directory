# VRealizeNetworkInsightApiReference.InfrastructureApi

All URIs are relative to *http://vmware.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNode**](InfrastructureApi.md#getNode) | **GET** /infra/nodes/{id} | Show node details
[**listNodes**](InfrastructureApi.md#listNodes) | **GET** /infra/nodes | List nodes



## getNode

> Node getNode(id)

Show node details

Get details of infrastructure nodes. Only admin users can get this information. The proxy id is required for adding a data source for selecting appropriate proxy node to add the data source.

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.InfrastructureApi();
let id = "id_example"; // String | entity id
apiInstance.getNode(id, (error, data, response) => {
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
 **id** | **String**| entity id | 

### Return type

[**Node**](Node.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, entity_type, id, ip_address, node_id, node_type


## listNodes

> NodeListResult listNodes()

List nodes

Get list of infrastructure nodes. Only admin users can retrieve this information.

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.InfrastructureApi();
apiInstance.listNodes((error, data, response) => {
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

[**NodeListResult**](NodeListResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, results, total_count

