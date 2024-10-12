# RudderApi.ScaleOutRelayApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**demoteToNode**](ScaleOutRelayApi.md#demoteToNode) | **POST** /scaleoutrelay/demote/{nodeId} | Demote a relay to simple node
[**promoteToRelay**](ScaleOutRelayApi.md#promoteToRelay) | **POST** /scaleoutrelay/promote/{nodeId} | Promote a node to relay



## demoteToNode

> DemoteToNode200Response demoteToNode(nodeId)

Demote a relay to simple node

Demote a relay to a simple node.

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.ScaleOutRelayApi();
let nodeId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the target node
apiInstance.demoteToNode(nodeId, (error, data, response) => {
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

[**DemoteToNode200Response**](DemoteToNode200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## promoteToRelay

> PromoteToRelay200Response promoteToRelay(nodeId)

Promote a node to relay

Promote a node to relay

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.ScaleOutRelayApi();
let nodeId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the target node
apiInstance.promoteToRelay(nodeId, (error, data, response) => {
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

[**PromoteToRelay200Response**](PromoteToRelay200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

