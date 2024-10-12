# HandwryttenApi.ProfileApi

All URIs are relative to *https://api.handwrytten.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**updateUserAddress**](ProfileApi.md#updateUserAddress) | **POST** /profile/updateAddress | update the user&#39;s return address information
[**userAddress**](ProfileApi.md#userAddress) | **POST** /profile/address | gets the user&#39;s return address information



## updateUserAddress

> UserAddress200Response updateUserAddress(body)

update the user&#39;s return address information

### Example

```javascript
import HandwryttenApi from 'handwrytten_api';

let apiInstance = new HandwryttenApi.ProfileApi();
let body = new HandwryttenApi.UpdateUserAddressRequest(); // UpdateUserAddressRequest | additional parameters
apiInstance.updateUserAddress(body, (error, data, response) => {
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
 **body** | [**UpdateUserAddressRequest**](UpdateUserAddressRequest.md)| additional parameters | 

### Return type

[**UserAddress200Response**](UserAddress200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## userAddress

> UserAddress200Response userAddress(opts)

gets the user&#39;s return address information

### Example

```javascript
import HandwryttenApi from 'handwrytten_api';

let apiInstance = new HandwryttenApi.ProfileApi();
let opts = {
  'body': new HandwryttenApi.UserAddressRequest() // UserAddressRequest | additional parameters
};
apiInstance.userAddress(opts, (error, data, response) => {
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
 **body** | [**UserAddressRequest**](UserAddressRequest.md)| additional parameters | [optional] 

### Return type

[**UserAddress200Response**](UserAddress200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

