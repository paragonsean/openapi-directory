# Traccar.CommandsApi

All URIs are relative to *https://demo.traccar.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commandsGet**](CommandsApi.md#commandsGet) | **GET** /commands | Fetch a list of Saved Commands
[**commandsIdDelete**](CommandsApi.md#commandsIdDelete) | **DELETE** /commands/{id} | Delete a Saved Command
[**commandsIdPut**](CommandsApi.md#commandsIdPut) | **PUT** /commands/{id} | Update a Saved Command
[**commandsPost**](CommandsApi.md#commandsPost) | **POST** /commands | Create a Saved Command
[**commandsSendGet**](CommandsApi.md#commandsSendGet) | **GET** /commands/send | Fetch a list of Saved Commands supported by Device at the moment
[**commandsSendPost**](CommandsApi.md#commandsSendPost) | **POST** /commands/send | Dispatch commands to device
[**commandsTypesGet**](CommandsApi.md#commandsTypesGet) | **GET** /commands/types | Fetch a list of available Commands for the Device or all possible Commands if Device ommited



## commandsGet

> [Command] commandsGet(opts)

Fetch a list of Saved Commands

Without params, it returns a list of Saved Commands the user has access to

### Example

```javascript
import Traccar from 'traccar';
let defaultClient = Traccar.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Traccar.CommandsApi();
let opts = {
  'all': true, // Boolean | Can only be used by admins or managers to fetch all entities
  'userId': 56, // Number | Standard users can use this only with their own _userId_
  'deviceId': 56, // Number | Standard users can use this only with _deviceId_s, they have access to
  'groupId': 56, // Number | Standard users can use this only with _groupId_s, they have access to
  'refresh': true // Boolean | 
};
apiInstance.commandsGet(opts, (error, data, response) => {
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
 **all** | **Boolean**| Can only be used by admins or managers to fetch all entities | [optional] 
 **userId** | **Number**| Standard users can use this only with their own _userId_ | [optional] 
 **deviceId** | **Number**| Standard users can use this only with _deviceId_s, they have access to | [optional] 
 **groupId** | **Number**| Standard users can use this only with _groupId_s, they have access to | [optional] 
 **refresh** | **Boolean**|  | [optional] 

### Return type

[**[Command]**](Command.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## commandsIdDelete

> commandsIdDelete(id)

Delete a Saved Command

### Example

```javascript
import Traccar from 'traccar';
let defaultClient = Traccar.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Traccar.CommandsApi();
let id = 56; // Number | 
apiInstance.commandsIdDelete(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## commandsIdPut

> Command commandsIdPut(id, body)

Update a Saved Command

### Example

```javascript
import Traccar from 'traccar';
let defaultClient = Traccar.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Traccar.CommandsApi();
let id = 56; // Number | 
let body = new Traccar.Command(); // Command | 
apiInstance.commandsIdPut(id, body, (error, data, response) => {
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
 **id** | **Number**|  | 
 **body** | [**Command**](Command.md)|  | 

### Return type

[**Command**](Command.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## commandsPost

> Command commandsPost(body)

Create a Saved Command

### Example

```javascript
import Traccar from 'traccar';
let defaultClient = Traccar.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Traccar.CommandsApi();
let body = new Traccar.Command(); // Command | 
apiInstance.commandsPost(body, (error, data, response) => {
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
 **body** | [**Command**](Command.md)|  | 

### Return type

[**Command**](Command.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## commandsSendGet

> [Command] commandsSendGet(opts)

Fetch a list of Saved Commands supported by Device at the moment

Return a list of saved commands linked to Device and its groups, filtered by current Device protocol support

### Example

```javascript
import Traccar from 'traccar';
let defaultClient = Traccar.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Traccar.CommandsApi();
let opts = {
  'deviceId': 56 // Number | Standard users can use this only with _deviceId_s, they have access to
};
apiInstance.commandsSendGet(opts, (error, data, response) => {
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
 **deviceId** | **Number**| Standard users can use this only with _deviceId_s, they have access to | [optional] 

### Return type

[**[Command]**](Command.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## commandsSendPost

> Command commandsSendPost(body)

Dispatch commands to device

Dispatch a new command or Saved Command if _body.id_ set

### Example

```javascript
import Traccar from 'traccar';
let defaultClient = Traccar.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Traccar.CommandsApi();
let body = new Traccar.Command(); // Command | 
apiInstance.commandsSendPost(body, (error, data, response) => {
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
 **body** | [**Command**](Command.md)|  | 

### Return type

[**Command**](Command.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## commandsTypesGet

> [CommandType] commandsTypesGet(opts)

Fetch a list of available Commands for the Device or all possible Commands if Device ommited

### Example

```javascript
import Traccar from 'traccar';
let defaultClient = Traccar.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Traccar.CommandsApi();
let opts = {
  'deviceId': 56, // Number | Internal device identifier. Only works if device has already reported some locations
  'protocol': "protocol_example", // String | Protocol name. Can be used instead of device id
  'textChannel': true // Boolean | When `true` return SMS commands. If not specified or `false` return data commands
};
apiInstance.commandsTypesGet(opts, (error, data, response) => {
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
 **deviceId** | **Number**| Internal device identifier. Only works if device has already reported some locations | [optional] 
 **protocol** | **String**| Protocol name. Can be used instead of device id | [optional] 
 **textChannel** | **Boolean**| When &#x60;true&#x60; return SMS commands. If not specified or &#x60;false&#x60; return data commands | [optional] 

### Return type

[**[CommandType]**](CommandType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

