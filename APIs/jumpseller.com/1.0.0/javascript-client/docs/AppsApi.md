# JumpsellerApi.AppsApi

All URIs are relative to *https://api.jumpseller.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jsappsCodeJsonDelete**](AppsApi.md#jsappsCodeJsonDelete) | **DELETE** /jsapps/{code}.json | Delete an existing JSApp.
[**jsappsCodeJsonGet**](AppsApi.md#jsappsCodeJsonGet) | **GET** /jsapps/{code}.json | Retrieve a JSApp.
[**jsappsJsonGet**](AppsApi.md#jsappsJsonGet) | **GET** /jsapps.json | Retrieve all the Store&#39;s JSApps.
[**jsappsJsonPost**](AppsApi.md#jsappsJsonPost) | **POST** /jsapps.json | Create a Store JSApp.



## jsappsCodeJsonDelete

> String jsappsCodeJsonDelete(login, authtoken, code)

Delete an existing JSApp.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.AppsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let code = "code_example"; // String | Code of the App
apiInstance.jsappsCodeJsonDelete(login, authtoken, code, (error, data, response) => {
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
 **code** | **String**| Code of the App | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jsappsCodeJsonGet

> JSApp jsappsCodeJsonGet(login, authtoken, code)

Retrieve a JSApp.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.AppsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let code = "code_example"; // String | Code of the App
apiInstance.jsappsCodeJsonGet(login, authtoken, code, (error, data, response) => {
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
 **code** | **String**| Code of the App | 

### Return type

[**JSApp**](JSApp.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jsappsJsonGet

> App jsappsJsonGet(login, authtoken)

Retrieve all the Store&#39;s JSApps.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.AppsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
apiInstance.jsappsJsonGet(login, authtoken, (error, data, response) => {
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

### Return type

[**App**](App.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jsappsJsonPost

> JSApp jsappsJsonPost(login, authtoken, jSAppEdit)

Create a Store JSApp.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.AppsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let jSAppEdit = new JumpsellerApi.JSAppEdit(); // JSAppEdit | JSApp parameters to create
apiInstance.jsappsJsonPost(login, authtoken, jSAppEdit, (error, data, response) => {
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
 **jSAppEdit** | [**JSAppEdit**](JSAppEdit.md)| JSApp parameters to create | 

### Return type

[**JSApp**](JSApp.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

