# VaultApi.LogsApi

All URIs are relative to *https://unify.apideck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**logsAll**](LogsApi.md#logsAll) | **GET** /vault/logs | Get all consumer request logs



## logsAll

> GetLogsResponse logsAll(xApideckAppId, xApideckConsumerId, opts)

Get all consumer request logs

This endpoint includes all consumer request logs. 

### Example

```javascript
import VaultApi from 'vault_api';
let defaultClient = VaultApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new VaultApi.LogsApi();
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let opts = {
  'filter': new VaultApi.LogsFilter(), // LogsFilter | Filter results
  'cursor': "cursor_example", // String | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
  'limit': 20 // Number | Number of results to return. Minimum 1, Maximum 200, Default 20
};
apiInstance.logsAll(xApideckAppId, xApideckConsumerId, opts, (error, data, response) => {
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
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **filter** | [**LogsFilter**](.md)| Filter results | [optional] 
 **cursor** | **String**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional] 
 **limit** | **Number**| Number of results to return. Minimum 1, Maximum 200, Default 20 | [optional] [default to 20]

### Return type

[**GetLogsResponse**](GetLogsResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

