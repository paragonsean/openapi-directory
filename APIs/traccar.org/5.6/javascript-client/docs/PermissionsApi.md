# Traccar.PermissionsApi

All URIs are relative to *https://demo.traccar.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**permissionsDelete**](PermissionsApi.md#permissionsDelete) | **DELETE** /permissions | Unlink an Object from another Object
[**permissionsPost**](PermissionsApi.md#permissionsPost) | **POST** /permissions | Link an Object to another Object



## permissionsDelete

> permissionsDelete(body)

Unlink an Object from another Object

### Example

```javascript
import Traccar from 'traccar';
let defaultClient = Traccar.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Traccar.PermissionsApi();
let body = new Traccar.Permission(); // Permission | 
apiInstance.permissionsDelete(body, (error, data, response) => {
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
 **body** | [**Permission**](Permission.md)|  | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## permissionsPost

> Permission permissionsPost(body)

Link an Object to another Object

### Example

```javascript
import Traccar from 'traccar';
let defaultClient = Traccar.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Traccar.PermissionsApi();
let body = new Traccar.Permission(); // Permission | 
apiInstance.permissionsPost(body, (error, data, response) => {
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
 **body** | [**Permission**](Permission.md)|  | 

### Return type

[**Permission**](Permission.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

