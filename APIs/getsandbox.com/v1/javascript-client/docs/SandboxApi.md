# SandboxApi.SandboxApi

All URIs are relative to *https://getsandbox.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSandbox**](SandboxApi.md#createSandbox) | **POST** /1/sandboxes | createSandbox
[**deleteSandbox**](SandboxApi.md#deleteSandbox) | **DELETE** /1/sandboxes/{sandboxName} | deleteSandbox
[**deleteSandboxState**](SandboxApi.md#deleteSandboxState) | **DELETE** /1/sandboxes/{sandboxName}/state | deleteSandboxState
[**forkSandbox**](SandboxApi.md#forkSandbox) | **GET** /1/sandboxes/{sandboxName}/fork | forkSandbox
[**getSandbox**](SandboxApi.md#getSandbox) | **GET** /1/sandboxes/{sandboxName} | getSandbox
[**getSandboxState**](SandboxApi.md#getSandboxState) | **GET** /1/sandboxes/{sandboxName}/state | getSandboxState
[**getSandboxes**](SandboxApi.md#getSandboxes) | **GET** /1/sandboxes | getSandboxes
[**updateSandbox**](SandboxApi.md#updateSandbox) | **PUT** /1/sandboxes/{sandboxName} | updateSandbox



## createSandbox

> Sandbox createSandbox(body)

createSandbox

### Example

```javascript
import SandboxApi from 'sandbox_api';

let apiInstance = new SandboxApi.SandboxApi();
let body = new SandboxApi.CreateSandbox(); // CreateSandbox | Sandbox to be created
apiInstance.createSandbox(body, (error, data, response) => {
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
 **body** | [**CreateSandbox**](CreateSandbox.md)| Sandbox to be created | 

### Return type

[**Sandbox**](Sandbox.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteSandbox

> deleteSandbox(sandboxName)

deleteSandbox

### Example

```javascript
import SandboxApi from 'sandbox_api';

let apiInstance = new SandboxApi.SandboxApi();
let sandboxName = "sandboxName_example"; // String | Name of the Sandbox
apiInstance.deleteSandbox(sandboxName, (error, data, response) => {
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
 **sandboxName** | **String**| Name of the Sandbox | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteSandboxState

> deleteSandboxState(sandboxName)

deleteSandboxState

### Example

```javascript
import SandboxApi from 'sandbox_api';

let apiInstance = new SandboxApi.SandboxApi();
let sandboxName = "sandboxName_example"; // String | Name of the Sandbox
apiInstance.deleteSandboxState(sandboxName, (error, data, response) => {
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
 **sandboxName** | **String**| Name of the Sandbox | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## forkSandbox

> Sandbox forkSandbox(sandboxName)

forkSandbox

### Example

```javascript
import SandboxApi from 'sandbox_api';

let apiInstance = new SandboxApi.SandboxApi();
let sandboxName = "sandboxName_example"; // String | Name of the Sandbox
apiInstance.forkSandbox(sandboxName, (error, data, response) => {
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
 **sandboxName** | **String**| Name of the Sandbox | 

### Return type

[**Sandbox**](Sandbox.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSandbox

> Sandbox getSandbox(sandboxName)

getSandbox

### Example

```javascript
import SandboxApi from 'sandbox_api';

let apiInstance = new SandboxApi.SandboxApi();
let sandboxName = "sandboxName_example"; // String | Name of the Sandbox
apiInstance.getSandbox(sandboxName, (error, data, response) => {
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
 **sandboxName** | **String**| Name of the Sandbox | 

### Return type

[**Sandbox**](Sandbox.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSandboxState

> getSandboxState(sandboxName)

getSandboxState

### Example

```javascript
import SandboxApi from 'sandbox_api';

let apiInstance = new SandboxApi.SandboxApi();
let sandboxName = "sandboxName_example"; // String | Name of the Sandbox
apiInstance.getSandboxState(sandboxName, (error, data, response) => {
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
 **sandboxName** | **String**| Name of the Sandbox | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSandboxes

> [Sandbox] getSandboxes(opts)

getSandboxes

### Example

```javascript
import SandboxApi from 'sandbox_api';

let apiInstance = new SandboxApi.SandboxApi();
let opts = {
  'filterType': "filterType_example" // String | 
};
apiInstance.getSandboxes(opts, (error, data, response) => {
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
 **filterType** | **String**|  | [optional] 

### Return type

[**[Sandbox]**](Sandbox.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSandbox

> Sandbox updateSandbox(sandboxName, body)

updateSandbox

### Example

```javascript
import SandboxApi from 'sandbox_api';

let apiInstance = new SandboxApi.SandboxApi();
let sandboxName = "sandboxName_example"; // String | Name of the Sandbox
let body = new SandboxApi.Sandbox(); // Sandbox | Fields to updated on given Sandbox
apiInstance.updateSandbox(sandboxName, body, (error, data, response) => {
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
 **sandboxName** | **String**| Name of the Sandbox | 
 **body** | [**Sandbox**](Sandbox.md)| Fields to updated on given Sandbox | 

### Return type

[**Sandbox**](Sandbox.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

