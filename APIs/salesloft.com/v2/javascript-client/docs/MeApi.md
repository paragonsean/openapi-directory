# SalesLoftPlatform.MeApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2MeJsonGet**](MeApi.md#v2MeJsonGet) | **GET** /v2/me.json | Fetch current user



## v2MeJsonGet

> User v2MeJsonGet()

Fetch current user

Authenticated user information. This endpoint does not accept any parameters as it is represents your authenticated user. The \&quot;Users\&quot; resource provides user information for other users on the team. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.MeApi();
apiInstance.v2MeJsonGet((error, data, response) => {
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
- **Accept**: */*

