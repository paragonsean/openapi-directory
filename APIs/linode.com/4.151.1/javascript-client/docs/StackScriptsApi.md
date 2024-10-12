# LinodeApi.StackScriptsApi

All URIs are relative to *https://api.linode.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addStackScript**](StackScriptsApi.md#addStackScript) | **POST** /linode/stackscripts | StackScript Create
[**deleteStackScript**](StackScriptsApi.md#deleteStackScript) | **DELETE** /linode/stackscripts/{stackscriptId} | StackScript Delete
[**getStackScript**](StackScriptsApi.md#getStackScript) | **GET** /linode/stackscripts/{stackscriptId} | StackScript View
[**getStackScripts**](StackScriptsApi.md#getStackScripts) | **GET** /linode/stackscripts | StackScripts List
[**updateStackScript**](StackScriptsApi.md#updateStackScript) | **PUT** /linode/stackscripts/{stackscriptId} | StackScript Update



## addStackScript

> StackScript addStackScript(stackScript)

StackScript Create

Creates a StackScript in your Account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.StackScriptsApi();
let stackScript = new LinodeApi.StackScript(); // StackScript | The properties to set for the new StackScript.
apiInstance.addStackScript(stackScript, (error, data, response) => {
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
 **stackScript** | [**StackScript**](StackScript.md)| The properties to set for the new StackScript. | 

### Return type

[**StackScript**](StackScript.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteStackScript

> Object deleteStackScript(stackscriptId)

StackScript Delete

Deletes a private StackScript you have permission to &#x60;read_write&#x60;. You cannot delete a public StackScript. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.StackScriptsApi();
let stackscriptId = "stackscriptId_example"; // String | The ID of the StackScript to look up.
apiInstance.deleteStackScript(stackscriptId, (error, data, response) => {
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
 **stackscriptId** | **String**| The ID of the StackScript to look up. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStackScript

> StackScript getStackScript(stackscriptId)

StackScript View

Returns all of the information about a specified StackScript, including the contents of the script. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.StackScriptsApi();
let stackscriptId = "stackscriptId_example"; // String | The ID of the StackScript to look up.
apiInstance.getStackScript(stackscriptId, (error, data, response) => {
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
 **stackscriptId** | **String**| The ID of the StackScript to look up. | 

### Return type

[**StackScript**](StackScript.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStackScripts

> GetStackScripts200Response getStackScripts(opts)

StackScripts List

If the request is not authenticated, only public StackScripts are returned.  For more information on StackScripts, please read our [StackScripts documentation](/docs/products/tools/stackscripts/). 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.StackScriptsApi();
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getStackScripts(opts, (error, data, response) => {
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
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetStackScripts200Response**](GetStackScripts200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateStackScript

> StackScript updateStackScript(stackscriptId, opts)

StackScript Update

Updates a StackScript.  **Once a StackScript is made public, it cannot be made private.** 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.StackScriptsApi();
let stackscriptId = "stackscriptId_example"; // String | The ID of the StackScript to look up.
let opts = {
  'stackScript': new LinodeApi.StackScript() // StackScript | The fields to update.
};
apiInstance.updateStackScript(stackscriptId, opts, (error, data, response) => {
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
 **stackscriptId** | **String**| The ID of the StackScript to look up. | 
 **stackScript** | [**StackScript**](StackScript.md)| The fields to update. | [optional] 

### Return type

[**StackScript**](StackScript.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

