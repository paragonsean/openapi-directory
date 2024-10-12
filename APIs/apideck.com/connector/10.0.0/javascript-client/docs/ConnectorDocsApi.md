# ConnectorApi.ConnectorDocsApi

All URIs are relative to *https://unify.apideck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connectorDocsOne**](ConnectorDocsApi.md#connectorDocsOne) | **GET** /connector/connectors/{id}/docs/{doc_id} | Get Connector Doc content



## connectorDocsOne

> String connectorDocsOne(xApideckAppId, id, docId)

Get Connector Doc content

Get Connector Doc content

### Example

```javascript
import ConnectorApi from 'connector_api';
let defaultClient = ConnectorApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new ConnectorApi.ConnectorDocsApi();
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let id = "id_example"; // String | ID of the record you are acting upon.
let docId = "application_owner+oauth_credentials"; // String | ID of the Doc
apiInstance.connectorDocsOne(xApideckAppId, id, docId, (error, data, response) => {
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
 **docId** | **String**| ID of the Doc | 

### Return type

**String**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/markdown, application/json

