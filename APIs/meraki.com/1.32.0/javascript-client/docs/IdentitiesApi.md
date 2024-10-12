# MerakiDashboardApi.IdentitiesApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAdministeredIdentitiesMe_1**](IdentitiesApi.md#getAdministeredIdentitiesMe_1) | **GET** /administered/identities/me | Returns the identity of the current user.



## getAdministeredIdentitiesMe_1

> GetAdministeredIdentitiesMe200Response getAdministeredIdentitiesMe_1()

Returns the identity of the current user.

Returns the identity of the current user.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.IdentitiesApi();
apiInstance.getAdministeredIdentitiesMe_1((error, data, response) => {
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

[**GetAdministeredIdentitiesMe200Response**](GetAdministeredIdentitiesMe200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

