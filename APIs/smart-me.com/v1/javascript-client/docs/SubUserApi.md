# SmartMe.SubUserApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subUserDelete**](SubUserApi.md#subUserDelete) | **DELETE** /api/SubUser/{id} | Delete a subuser
[**subUserGet**](SubUserApi.md#subUserGet) | **GET** /api/SubUser/{id} | Get a sub user. The user must be assigend to the user that makes this call.
[**subUserPost**](SubUserApi.md#subUserPost) | **POST** /api/SubUser | Creates or updates a subuser.              To create a new user set no ID (empty)



## subUserDelete

> subUserDelete(id)

Delete a subuser

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.SubUserApi();
let id = "id_example"; // String | 
apiInstance.subUserDelete(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## subUserGet

> SubUserData subUserGet(id)

Get a sub user. The user must be assigend to the user that makes this call.

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.SubUserApi();
let id = "id_example"; // String | 
apiInstance.subUserGet(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**SubUserData**](SubUserData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## subUserPost

> subUserPost(subUserData)

Creates or updates a subuser.              To create a new user set no ID (empty)

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.SubUserApi();
let subUserData = new SmartMe.SubUserData(); // SubUserData | 
apiInstance.subUserPost(subUserData, (error, data, response) => {
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
 **subUserData** | [**SubUserData**](SubUserData.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: Not defined

