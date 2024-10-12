# Traccar.GroupsApi

All URIs are relative to *https://demo.traccar.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groupsGet**](GroupsApi.md#groupsGet) | **GET** /groups | Fetch a list of Groups
[**groupsIdDelete**](GroupsApi.md#groupsIdDelete) | **DELETE** /groups/{id} | Delete a Group
[**groupsIdPut**](GroupsApi.md#groupsIdPut) | **PUT** /groups/{id} | Update a Group
[**groupsPost**](GroupsApi.md#groupsPost) | **POST** /groups | Create a Group



## groupsGet

> [Group] groupsGet(opts)

Fetch a list of Groups

Without any params, returns a list of the Groups the user belongs to

### Example

```javascript
import Traccar from 'traccar';
let defaultClient = Traccar.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Traccar.GroupsApi();
let opts = {
  'all': true, // Boolean | Can only be used by admins or managers to fetch all entities
  'userId': 56 // Number | Standard users can use this only with their own _userId_
};
apiInstance.groupsGet(opts, (error, data, response) => {
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

### Return type

[**[Group]**](Group.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## groupsIdDelete

> groupsIdDelete(id)

Delete a Group

### Example

```javascript
import Traccar from 'traccar';
let defaultClient = Traccar.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Traccar.GroupsApi();
let id = 56; // Number | 
apiInstance.groupsIdDelete(id, (error, data, response) => {
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


## groupsIdPut

> Group groupsIdPut(id, body)

Update a Group

### Example

```javascript
import Traccar from 'traccar';
let defaultClient = Traccar.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Traccar.GroupsApi();
let id = 56; // Number | 
let body = new Traccar.Group(); // Group | 
apiInstance.groupsIdPut(id, body, (error, data, response) => {
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
 **body** | [**Group**](Group.md)|  | 

### Return type

[**Group**](Group.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## groupsPost

> Group groupsPost(body)

Create a Group

### Example

```javascript
import Traccar from 'traccar';
let defaultClient = Traccar.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Traccar.GroupsApi();
let body = new Traccar.Group(); // Group | 
apiInstance.groupsPost(body, (error, data, response) => {
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
 **body** | [**Group**](Group.md)|  | 

### Return type

[**Group**](Group.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

