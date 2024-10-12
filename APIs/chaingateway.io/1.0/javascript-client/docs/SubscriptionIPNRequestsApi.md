# ChaingatewayIo.SubscriptionIPNRequestsApi

All URIs are relative to *https://eu.eth.chaingateway.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listFailedIPNs**](SubscriptionIPNRequestsApi.md#listFailedIPNs) | **POST** /listFailedIPNs | listFailedIPNs
[**listSubscribedAddresses**](SubscriptionIPNRequestsApi.md#listSubscribedAddresses) | **POST** /listSubscribedAddresses | listSubscribedAddresses
[**resendFailedIPN**](SubscriptionIPNRequestsApi.md#resendFailedIPN) | **POST** /resendFailedIPN | resendFailedIPN
[**subscribeAddress**](SubscriptionIPNRequestsApi.md#subscribeAddress) | **POST** /subscribeAddress | subscribeAddress
[**unsubscribeAddress**](SubscriptionIPNRequestsApi.md#unsubscribeAddress) | **POST** /unsubscribeAddress | unsubscribeAddress



## listFailedIPNs

> ListFailedIPNs listFailedIPNs(contentType, authorization)

listFailedIPNs

Returns all subscriptions/IPNs created with an account.

### Example

```javascript
import ChaingatewayIo from 'chaingateway_io';

let apiInstance = new ChaingatewayIo.SubscriptionIPNRequestsApi();
let contentType = "application/json"; // String | 
let authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
apiInstance.listFailedIPNs(contentType, authorization, (error, data, response) => {
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
 **contentType** | **String**|  | 
 **authorization** | **String**| API Key | 

### Return type

[**ListFailedIPNs**](ListFailedIPNs.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSubscribedAddresses

> ListSubscribedAddresses listSubscribedAddresses(contentType, authorization)

listSubscribedAddresses

Returns all subscriptions/IPNs created with an account.

### Example

```javascript
import ChaingatewayIo from 'chaingateway_io';

let apiInstance = new ChaingatewayIo.SubscriptionIPNRequestsApi();
let contentType = "application/json"; // String | 
let authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
apiInstance.listSubscribedAddresses(contentType, authorization, (error, data, response) => {
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
 **contentType** | **String**|  | 
 **authorization** | **String**| API Key | 

### Return type

[**ListSubscribedAddresses**](ListSubscribedAddresses.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resendFailedIPN

> ResendFailedIPN resendFailedIPN(authorization, resendFailedIPNRequest)

resendFailedIPN

Returns all subscriptions/IPNs created with an account.

### Example

```javascript
import ChaingatewayIo from 'chaingateway_io';

let apiInstance = new ChaingatewayIo.SubscriptionIPNRequestsApi();
let authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
let resendFailedIPNRequest = {"id":17766}; // ResendFailedIPNRequest | 
apiInstance.resendFailedIPN(authorization, resendFailedIPNRequest, (error, data, response) => {
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
 **authorization** | **String**| API Key | 
 **resendFailedIPNRequest** | [**ResendFailedIPNRequest**](ResendFailedIPNRequest.md)|  | 

### Return type

[**ResendFailedIPN**](ResendFailedIPN.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## subscribeAddress

> SubscribeAddress subscribeAddress(authorization, subscribeAddressRequest)

subscribeAddress

Creates a new subscription/IPN for the given address (and contractaddress). You will receive a notification to the given url every time a deposit is received. Unsubscribe the address before sending tokens/ETH from it or you won&#39;t get reliable notifications anymore.  

### Example

```javascript
import ChaingatewayIo from 'chaingateway_io';

let apiInstance = new ChaingatewayIo.SubscriptionIPNRequestsApi();
let authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
let subscribeAddressRequest = {"contractaddress":"0x514910771af9ca656af840dff83e8264ecf986ca","ethereumaddress":"0xa2107fa5b38d9bbd2c461d6edf11b11a50f6b974","url":"https://yoururl.com/ipnreceiver.php"}; // SubscribeAddressRequest | 
apiInstance.subscribeAddress(authorization, subscribeAddressRequest, (error, data, response) => {
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
 **authorization** | **String**| API Key | 
 **subscribeAddressRequest** | [**SubscribeAddressRequest**](SubscribeAddressRequest.md)|  | 

### Return type

[**SubscribeAddress**](SubscribeAddress.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## unsubscribeAddress

> UnsubscribeAddress unsubscribeAddress(authorization, unsubscribeAddressRequest)

unsubscribeAddress

Deletes an existing subscription/IPN for the given address (and contractaddress).

### Example

```javascript
import ChaingatewayIo from 'chaingateway_io';

let apiInstance = new ChaingatewayIo.SubscriptionIPNRequestsApi();
let authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
let unsubscribeAddressRequest = {"contractaddress":"0x514910771af9ca656af840dff83e8264ecf986ca","ethereumaddress":"0xa2107fa5b38d9bbd2c461d6edf11b11a50f6b974","url":"https://yoururl.com/ipnreceiver.php"}; // UnsubscribeAddressRequest | 
apiInstance.unsubscribeAddress(authorization, unsubscribeAddressRequest, (error, data, response) => {
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
 **authorization** | **String**| API Key | 
 **unsubscribeAddressRequest** | [**UnsubscribeAddressRequest**](UnsubscribeAddressRequest.md)|  | 

### Return type

[**UnsubscribeAddress**](UnsubscribeAddress.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

