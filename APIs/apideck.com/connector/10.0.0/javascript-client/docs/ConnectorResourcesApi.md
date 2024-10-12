# ConnectorApi.ConnectorResourcesApi

All URIs are relative to *https://unify.apideck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connectorResourcesOne**](ConnectorResourcesApi.md#connectorResourcesOne) | **GET** /connector/connectors/{id}/resources/{resource_id} | Get Connector Resource



## connectorResourcesOne

> GetConnectorResourceResponse connectorResourcesOne(xApideckAppId, id, resourceId, opts)

Get Connector Resource

Get Connector Resource

### Example

```javascript
import ConnectorApi from 'connector_api';
let defaultClient = ConnectorApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new ConnectorApi.ConnectorResourcesApi();
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let id = "id_example"; // String | ID of the record you are acting upon.
let resourceId = "resourceId_example"; // String | ID of the resource you are acting upon.
let opts = {
  'unifiedApi': new ConnectorApi.UnifiedApiId() // UnifiedApiId | Specify unified API for the connector resource. This is useful when a resource appears in multiple APIs
};
apiInstance.connectorResourcesOne(xApideckAppId, id, resourceId, opts, (error, data, response) => {
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
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **id** | **String**| ID of the record you are acting upon. | 
 **resourceId** | **String**| ID of the resource you are acting upon. | 
 **unifiedApi** | [**UnifiedApiId**](.md)| Specify unified API for the connector resource. This is useful when a resource appears in multiple APIs | [optional] 

### Return type

[**GetConnectorResourceResponse**](GetConnectorResourceResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

