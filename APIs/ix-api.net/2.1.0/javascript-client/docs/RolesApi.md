# IxApi.RolesApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rolesList**](RolesApi.md#rolesList) | **GET** /roles | 
[**rolesRead**](RolesApi.md#rolesRead) | **GET** /roles/{id} | 



## rolesList

> [Role] rolesList(opts)



List all roles available.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.RolesApi();
let opts = {
  'id': ["null"], // [String] | Filter by id
  'name': "name_example", // String | Filter by name
  'contact': "contact_example" // String | Filter by contact
};
apiInstance.rolesList(opts, (error, data, response) => {
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
 **id** | [**[String]**](String.md)| Filter by id | [optional] 
 **name** | **String**| Filter by name | [optional] 
 **contact** | **String**| Filter by contact | [optional] 

### Return type

[**[Role]**](Role.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## rolesRead

> Role rolesRead(id, opts)



Get a single &#x60;Role&#x60;.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.RolesApi();
let id = "id_example"; // String | Get by id
let opts = {
  'id2': ["null"], // [String] | Filter by id
  'name': "name_example" // String | Filter by name
};
apiInstance.rolesRead(id, opts, (error, data, response) => {
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
 **id** | **String**| Get by id | 
 **id2** | [**[String]**](String.md)| Filter by id | [optional] 
 **name** | **String**| Filter by name | [optional] 

### Return type

[**Role**](Role.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

