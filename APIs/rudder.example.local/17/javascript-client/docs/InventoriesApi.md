# RudderApi.InventoriesApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fileWatcherRestart**](InventoriesApi.md#fileWatcherRestart) | **POST** /inventories/watcher/restart | Restart inventory watcher
[**fileWatcherStart**](InventoriesApi.md#fileWatcherStart) | **POST** /inventories/watcher/start | Start inventory watcher
[**fileWatcherStop**](InventoriesApi.md#fileWatcherStop) | **POST** /inventories/watcher/stop | Stop inventory watcher
[**queueInformation**](InventoriesApi.md#queueInformation) | **GET** /inventories/info | Get information about inventory processing queue
[**uploadInventory**](InventoriesApi.md#uploadInventory) | **POST** /inventories/upload | Upload an inventory for processing



## fileWatcherRestart

> FileWatcherRestart200Response fileWatcherRestart()

Restart inventory watcher

Restart the inventory watcher if necessary

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.InventoriesApi();
apiInstance.fileWatcherRestart((error, data, response) => {
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

[**FileWatcherRestart200Response**](FileWatcherRestart200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fileWatcherStart

> FileWatcherStart200Response fileWatcherStart()

Start inventory watcher

Start the inventory watcher if necessary

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.InventoriesApi();
apiInstance.fileWatcherStart((error, data, response) => {
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

[**FileWatcherStart200Response**](FileWatcherStart200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fileWatcherStop

> FileWatcherStop200Response fileWatcherStop()

Stop inventory watcher

Stop the inventory watcher if necessary

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.InventoriesApi();
apiInstance.fileWatcherStop((error, data, response) => {
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

[**FileWatcherStop200Response**](FileWatcherStop200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queueInformation

> QueueInformation200Response queueInformation()

Get information about inventory processing queue

Provide information about the current state of the inventory processor

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.InventoriesApi();
apiInstance.queueInformation((error, data, response) => {
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

[**QueueInformation200Response**](QueueInformation200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## uploadInventory

> UploadInventory200Response uploadInventory(opts)

Upload an inventory for processing

Upload an inventory to the web application

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.InventoriesApi();
let opts = {
  'file': "/path/to/file", // File | The inventory file. The original file name is used to check extension, that should be .xml[.gz] or .ocs[.gz]
  'signature': "/path/to/file" // File | The signature file. The original file name is used to check extension, that should be ${originalInventoryFileName}.sign[.gz]
};
apiInstance.uploadInventory(opts, (error, data, response) => {
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
 **file** | **File**| The inventory file. The original file name is used to check extension, that should be .xml[.gz] or .ocs[.gz] | [optional] 
 **signature** | **File**| The signature file. The original file name is used to check extension, that should be ${originalInventoryFileName}.sign[.gz] | [optional] 

### Return type

[**UploadInventory200Response**](UploadInventory200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

