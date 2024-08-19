# JumpsellerApi.HooksApi

All URIs are relative to *https://api.jumpseller.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hooksIdJsonDelete**](HooksApi.md#hooksIdJsonDelete) | **DELETE** /hooks/{id}.json | Delete an existing Hook.
[**hooksIdJsonGet**](HooksApi.md#hooksIdJsonGet) | **GET** /hooks/{id}.json | Retrieve a single Hook.
[**hooksIdJsonPut**](HooksApi.md#hooksIdJsonPut) | **PUT** /hooks/{id}.json | Update a Hook.
[**hooksJsonGet**](HooksApi.md#hooksJsonGet) | **GET** /hooks.json | Retrieve all Hooks.
[**hooksJsonPost**](HooksApi.md#hooksJsonPost) | **POST** /hooks.json | Create a new Hook.



## hooksIdJsonDelete

> String hooksIdJsonDelete(login, authtoken, id)

Delete an existing Hook.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.HooksApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Hook
apiInstance.hooksIdJsonDelete(login, authtoken, id, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 
 **id** | **Number**| Id of the Hook | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## hooksIdJsonGet

> Hook hooksIdJsonGet(login, authtoken, id)

Retrieve a single Hook.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.HooksApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Hook
apiInstance.hooksIdJsonGet(login, authtoken, id, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 
 **id** | **Number**| Id of the Hook | 

### Return type

[**Hook**](Hook.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## hooksIdJsonPut

> Hook hooksIdJsonPut(login, authtoken, id, hookEdit)

Update a Hook.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.HooksApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Hook
let hookEdit = new JumpsellerApi.HookEdit(); // HookEdit | Hook parameters.
apiInstance.hooksIdJsonPut(login, authtoken, id, hookEdit, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 
 **id** | **Number**| Id of the Hook | 
 **hookEdit** | [**HookEdit**](HookEdit.md)| Hook parameters. | 

### Return type

[**Hook**](Hook.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## hooksJsonGet

> [Hook] hooksJsonGet(login, authtoken, opts)

Retrieve all Hooks.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.HooksApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let opts = {
  'limit': 50, // Number | List restriction
  'page': 1 // Number | List page
};
apiInstance.hooksJsonGet(login, authtoken, opts, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 
 **limit** | **Number**| List restriction | [optional] [default to 50]
 **page** | **Number**| List page | [optional] [default to 1]

### Return type

[**[Hook]**](Hook.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## hooksJsonPost

> Hook hooksJsonPost(login, authtoken, hookEdit)

Create a new Hook.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.HooksApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let hookEdit = new JumpsellerApi.HookEdit(); // HookEdit | Hook parameters.
apiInstance.hooksJsonPost(login, authtoken, hookEdit, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 
 **hookEdit** | [**HookEdit**](HookEdit.md)| Hook parameters. | 

### Return type

[**Hook**](Hook.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

