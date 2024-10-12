# SmartMe.UserApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**userDelete**](UserApi.md#userDelete) | **DELETE** /api/User | Triggers user account deletion.
[**userGet**](UserApi.md#userGet) | **GET** /api/User | Gets the informations for the user.



## userDelete

> Object userDelete()

Triggers user account deletion.

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.UserApi();
apiInstance.userDelete((error, data, response) => {
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

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## userGet

> User userGet()

Gets the informations for the user.

Gets the informations for the user.

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.UserApi();
apiInstance.userGet((error, data, response) => {
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

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

