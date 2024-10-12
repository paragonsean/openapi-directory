# Reverb.ShopApi

All URIs are relative to *https://api.reverb.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**shopGet**](ShopApi.md#shopGet) | **GET** /shop | Get your own shop details
[**shopListingConditionsGet**](ShopApi.md#shopListingConditionsGet) | **GET** /shop/listing_conditions | List of supported product conditions
[**shopPaymentMethodsGet**](ShopApi.md#shopPaymentMethodsGet) | **GET** /shop/payment_methods | Get accepted payment methods
[**shopPut**](ShopApi.md#shopPut) | **PUT** /shop | Update your shop profile
[**shopVacationDelete**](ShopApi.md#shopVacationDelete) | **DELETE** /shop/vacation | Disable vacation mode. All listings will be re-enabled.
[**shopVacationGet**](ShopApi.md#shopVacationGet) | **GET** /shop/vacation | Returns shop vacation status
[**shopVacationPost**](ShopApi.md#shopVacationPost) | **POST** /shop/vacation | Enable vacation mode. All listings will be unavailable until vacation mode is turned off.



## shopGet

> shopGet()

Get your own shop details

Get your own shop details

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.ShopApi();
apiInstance.shopGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## shopListingConditionsGet

> shopListingConditionsGet()

List of supported product conditions

List of supported product conditions

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.ShopApi();
apiInstance.shopListingConditionsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## shopPaymentMethodsGet

> shopPaymentMethodsGet()

Get accepted payment methods

Get accepted payment methods

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.ShopApi();
apiInstance.shopPaymentMethodsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## shopPut

> shopPut(opts)

Update your shop profile

Update your shop profile

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.ShopApi();
let opts = {
  'shopPutRequest': new Reverb.ShopPutRequest() // ShopPutRequest | the content of the request
};
apiInstance.shopPut(opts, (error, data, response) => {
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
 **shopPutRequest** | [**ShopPutRequest**](ShopPutRequest.md)| the content of the request | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## shopVacationDelete

> shopVacationDelete()

Disable vacation mode. All listings will be re-enabled.

Disable vacation mode. All listings will be re-enabled.

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.ShopApi();
apiInstance.shopVacationDelete((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## shopVacationGet

> shopVacationGet()

Returns shop vacation status

Returns shop vacation status

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.ShopApi();
apiInstance.shopVacationGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## shopVacationPost

> shopVacationPost()

Enable vacation mode. All listings will be unavailable until vacation mode is turned off.

Enable vacation mode. All listings will be unavailable until vacation mode is turned off.

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.ShopApi();
apiInstance.shopVacationPost((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

