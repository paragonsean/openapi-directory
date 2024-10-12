# Signl4Api.ScriptsApi

All URIs are relative to *https://connect.signl4.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scriptsInstancesGet**](ScriptsApi.md#scriptsInstancesGet) | **GET** /scripts/instances | Returns all script instances of the SIGNL4 team
[**scriptsInstancesInstanceIdDataPut**](ScriptsApi.md#scriptsInstancesInstanceIdDataPut) | **PUT** /scripts/instances/{instanceId}/data | Updates custom data of a given script instance which includes its display name.
[**scriptsInstancesInstanceIdDelete**](ScriptsApi.md#scriptsInstancesInstanceIdDelete) | **DELETE** /scripts/instances/{instanceId} | Deletes a script instance.
[**scriptsInstancesInstanceIdDisablePost**](ScriptsApi.md#scriptsInstancesInstanceIdDisablePost) | **POST** /scripts/instances/{instanceId}/disable | Disables a given script instance.
[**scriptsInstancesInstanceIdEnablePost**](ScriptsApi.md#scriptsInstancesInstanceIdEnablePost) | **POST** /scripts/instances/{instanceId}/enable | Enables a script instance.
[**scriptsInstancesInstanceIdGet**](ScriptsApi.md#scriptsInstancesInstanceIdGet) | **GET** /scripts/instances/{instanceId} | Returns all information about a given script instance which includes its runtime status.
[**scriptsInstancesInstanceIdPut**](ScriptsApi.md#scriptsInstancesInstanceIdPut) | **PUT** /scripts/instances/{instanceId} | Updates a given script instance, typically used for updating the configuration of a script.
[**scriptsInstancesPost**](ScriptsApi.md#scriptsInstancesPost) | **POST** /scripts/instances | Creates a new script instance in the in the SIGNL4 team.
[**scriptsInventoryGet**](ScriptsApi.md#scriptsInventoryGet) | **GET** /scripts/inventory | Returns all available inventory scripts which can be added to a SIGNL4 subscription.
[**scriptsInventoryParsedGet**](ScriptsApi.md#scriptsInventoryParsedGet) | **GET** /scripts/inventory/parsed | Returns all inventory scripts.
[**scriptsInventoryParsedScriptIdGet**](ScriptsApi.md#scriptsInventoryParsedScriptIdGet) | **GET** /scripts/inventory/parsed/{scriptId} | Returns an inventory script by its id.



## scriptsInstancesGet

> [ScriptInstanceDetails] scriptsInstancesGet(opts)

Returns all script instances of the SIGNL4 team

Returns all script instances in the subscription.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.ScriptsApi();
let opts = {
  'teamId': "teamId_example" // String | 
};
apiInstance.scriptsInstancesGet(opts, (error, data, response) => {
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
 **teamId** | **String**|  | [optional] 

### Return type

[**[ScriptInstanceDetails]**](ScriptInstanceDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## scriptsInstancesInstanceIdDataPut

> ScriptInstanceDetails scriptsInstancesInstanceIdDataPut(instanceId, opts)

Updates custom data of a given script instance which includes its display name.

Updates the specified script instance.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.ScriptsApi();
let instanceId = "instanceId_example"; // String | InstanceId of the script to be updated.
let opts = {
  'scriptInstanceCustomUserData': new Signl4Api.ScriptInstanceCustomUserData() // ScriptInstanceCustomUserData | Script instance to be updated.
};
apiInstance.scriptsInstancesInstanceIdDataPut(instanceId, opts, (error, data, response) => {
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
 **instanceId** | **String**| InstanceId of the script to be updated. | 
 **scriptInstanceCustomUserData** | [**ScriptInstanceCustomUserData**](ScriptInstanceCustomUserData.md)| Script instance to be updated. | [optional] 

### Return type

[**ScriptInstanceDetails**](ScriptInstanceDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## scriptsInstancesInstanceIdDelete

> scriptsInstancesInstanceIdDelete(instanceId)

Deletes a script instance.

Gets the script instance specified by the passed instance id.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.ScriptsApi();
let instanceId = "instanceId_example"; // String | Instance Id of script instance to be returned.
apiInstance.scriptsInstancesInstanceIdDelete(instanceId, (error, data, response) => {
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
 **instanceId** | **String**| Instance Id of script instance to be returned. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## scriptsInstancesInstanceIdDisablePost

> ScriptInstanceDetails scriptsInstancesInstanceIdDisablePost(instanceId)

Disables a given script instance.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.ScriptsApi();
let instanceId = "instanceId_example"; // String | Id of the instance to be disabled.
apiInstance.scriptsInstancesInstanceIdDisablePost(instanceId, (error, data, response) => {
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
 **instanceId** | **String**| Id of the instance to be disabled. | 

### Return type

[**ScriptInstanceDetails**](ScriptInstanceDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## scriptsInstancesInstanceIdEnablePost

> ScriptInstanceDetails scriptsInstancesInstanceIdEnablePost(instanceId)

Enables a script instance.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.ScriptsApi();
let instanceId = "instanceId_example"; // String | Id of the instance to be enabled.
apiInstance.scriptsInstancesInstanceIdEnablePost(instanceId, (error, data, response) => {
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
 **instanceId** | **String**| Id of the instance to be enabled. | 

### Return type

[**ScriptInstanceDetails**](ScriptInstanceDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## scriptsInstancesInstanceIdGet

> ScriptInstanceDetails scriptsInstancesInstanceIdGet(instanceId)

Returns all information about a given script instance which includes its runtime status.

Gets the script instance specified by the passed instance id.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.ScriptsApi();
let instanceId = "instanceId_example"; // String | Instance Id of script instance to be returned.
apiInstance.scriptsInstancesInstanceIdGet(instanceId, (error, data, response) => {
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
 **instanceId** | **String**| Instance Id of script instance to be returned. | 

### Return type

[**ScriptInstanceDetails**](ScriptInstanceDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## scriptsInstancesInstanceIdPut

> ScriptInstanceDetails scriptsInstancesInstanceIdPut(instanceId, opts)

Updates a given script instance, typically used for updating the configuration of a script.

Updates the specified script instance.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.ScriptsApi();
let instanceId = "instanceId_example"; // String | InstanceId of the script to be updated.
let opts = {
  'scriptInstanceDetails': new Signl4Api.ScriptInstanceDetails() // ScriptInstanceDetails | Script instance to be updated.
};
apiInstance.scriptsInstancesInstanceIdPut(instanceId, opts, (error, data, response) => {
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
 **instanceId** | **String**| InstanceId of the script to be updated. | 
 **scriptInstanceDetails** | [**ScriptInstanceDetails**](ScriptInstanceDetails.md)| Script instance to be updated. | [optional] 

### Return type

[**ScriptInstanceDetails**](ScriptInstanceDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## scriptsInstancesPost

> ScriptInstanceDetails scriptsInstancesPost(opts)

Creates a new script instance in the in the SIGNL4 team.

Creates a new script instance of the script specified in the request body.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.ScriptsApi();
let opts = {
  'scriptInstanceDetails': new Signl4Api.ScriptInstanceDetails() // ScriptInstanceDetails | Script instance to be created.
};
apiInstance.scriptsInstancesPost(opts, (error, data, response) => {
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
 **scriptInstanceDetails** | [**ScriptInstanceDetails**](ScriptInstanceDetails.md)| Script instance to be created. | [optional] 

### Return type

[**ScriptInstanceDetails**](ScriptInstanceDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## scriptsInventoryGet

> [InventoryScriptInfo] scriptsInventoryGet()

Returns all available inventory scripts which can be added to a SIGNL4 subscription.

Returns all available inventory scripts which can be added to a SIGNL4 subscription.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.ScriptsApi();
apiInstance.scriptsInventoryGet((error, data, response) => {
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

[**[InventoryScriptInfo]**](InventoryScriptInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## scriptsInventoryParsedGet

> [InventoryScriptInfo] scriptsInventoryParsedGet(opts)

Returns all inventory scripts.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.ScriptsApi();
let opts = {
  'language': "language_example" // String | 
};
apiInstance.scriptsInventoryParsedGet(opts, (error, data, response) => {
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
 **language** | **String**|  | [optional] 

### Return type

[**[InventoryScriptInfo]**](InventoryScriptInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## scriptsInventoryParsedScriptIdGet

> ScriptInstanceDetails scriptsInventoryParsedScriptIdGet(scriptId, opts)

Returns an inventory script by its id.

Gets the script specified by the passed script id.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.ScriptsApi();
let scriptId = "scriptId_example"; // String | The Id of the script to be returned.
let opts = {
  'language': "language_example" // String | 
};
apiInstance.scriptsInventoryParsedScriptIdGet(scriptId, opts, (error, data, response) => {
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
 **scriptId** | **String**| The Id of the script to be returned. | 
 **language** | **String**|  | [optional] 

### Return type

[**ScriptInstanceDetails**](ScriptInstanceDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

