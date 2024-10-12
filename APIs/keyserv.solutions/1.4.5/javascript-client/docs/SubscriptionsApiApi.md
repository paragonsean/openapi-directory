# KeyServ.SubscriptionsApiApi

All URIs are relative to *https://keyserv.solutions*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscriptionsApiCount**](SubscriptionsApiApi.md#subscriptionsApiCount) | **POST** /v1/SubscriptionsApi/Count | 
[**subscriptionsApiDeleteSubscription**](SubscriptionsApiApi.md#subscriptionsApiDeleteSubscription) | **DELETE** /v1/SubscriptionsApi/{serial} | 
[**subscriptionsApiDeleteSubscription2**](SubscriptionsApiApi.md#subscriptionsApiDeleteSubscription2) | **POST** /v1/SubscriptionsApi/{serial} | 
[**subscriptionsApiDisable**](SubscriptionsApiApi.md#subscriptionsApiDisable) | **PATCH** /v1/SubscriptionsApi/Disable | 
[**subscriptionsApiDisable2**](SubscriptionsApiApi.md#subscriptionsApiDisable2) | **POST** /v1/SubscriptionsApi/Disable | 
[**subscriptionsApiEnable**](SubscriptionsApiApi.md#subscriptionsApiEnable) | **PATCH** /v1/SubscriptionsApi/Enable | 
[**subscriptionsApiEnable2**](SubscriptionsApiApi.md#subscriptionsApiEnable2) | **POST** /v1/SubscriptionsApi/Enable | 
[**subscriptionsApiFind**](SubscriptionsApiApi.md#subscriptionsApiFind) | **POST** /v1/SubscriptionsApi/Find | 
[**subscriptionsApiList**](SubscriptionsApiApi.md#subscriptionsApiList) | **POST** /v1/SubscriptionsApi/List | 
[**subscriptionsApiPutSubscription**](SubscriptionsApiApi.md#subscriptionsApiPutSubscription) | **PUT** /v1/SubscriptionsApi | 
[**subscriptionsApiPutSubscription2**](SubscriptionsApiApi.md#subscriptionsApiPutSubscription2) | **POST** /v1/SubscriptionsApi | 
[**subscriptionsApiSave**](SubscriptionsApiApi.md#subscriptionsApiSave) | **POST** /v1/SubscriptionsApi/Save | 



## subscriptionsApiCount

> ProductsApiCount200Response subscriptionsApiCount(subscriptionsApiCountRequest)



### Example

```javascript
import KeyServ from 'key_serv';

let apiInstance = new KeyServ.SubscriptionsApiApi();
let subscriptionsApiCountRequest = new KeyServ.SubscriptionsApiCountRequest(); // SubscriptionsApiCountRequest | 
apiInstance.subscriptionsApiCount(subscriptionsApiCountRequest, (error, data, response) => {
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
 **subscriptionsApiCountRequest** | [**SubscriptionsApiCountRequest**](SubscriptionsApiCountRequest.md)|  | 

### Return type

[**ProductsApiCount200Response**](ProductsApiCount200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## subscriptionsApiDeleteSubscription

> subscriptionsApiDeleteSubscription(xApiKey, serial, keep)



### Example

```javascript
import KeyServ from 'key_serv';

let apiInstance = new KeyServ.SubscriptionsApiApi();
let xApiKey = "xApiKey_example"; // String | 
let serial = "serial_example"; // String | 
let keep = true; // Boolean | 
apiInstance.subscriptionsApiDeleteSubscription(xApiKey, serial, keep, (error, data, response) => {
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
 **xApiKey** | **String**|  | 
 **serial** | **String**|  | 
 **keep** | **Boolean**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## subscriptionsApiDeleteSubscription2

> subscriptionsApiDeleteSubscription2(xApiKey, serial, keep)



### Example

```javascript
import KeyServ from 'key_serv';

let apiInstance = new KeyServ.SubscriptionsApiApi();
let xApiKey = "xApiKey_example"; // String | 
let serial = "serial_example"; // String | 
let keep = true; // Boolean | 
apiInstance.subscriptionsApiDeleteSubscription2(xApiKey, serial, keep, (error, data, response) => {
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
 **xApiKey** | **String**|  | 
 **serial** | **String**|  | 
 **keep** | **Boolean**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## subscriptionsApiDisable

> subscriptionsApiDisable(productsApiFindRequest)



### Example

```javascript
import KeyServ from 'key_serv';

let apiInstance = new KeyServ.SubscriptionsApiApi();
let productsApiFindRequest = new KeyServ.ProductsApiFindRequest(); // ProductsApiFindRequest | 
apiInstance.subscriptionsApiDisable(productsApiFindRequest, (error, data, response) => {
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
 **productsApiFindRequest** | [**ProductsApiFindRequest**](ProductsApiFindRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## subscriptionsApiDisable2

> subscriptionsApiDisable2(productsApiFindRequest)



### Example

```javascript
import KeyServ from 'key_serv';

let apiInstance = new KeyServ.SubscriptionsApiApi();
let productsApiFindRequest = new KeyServ.ProductsApiFindRequest(); // ProductsApiFindRequest | 
apiInstance.subscriptionsApiDisable2(productsApiFindRequest, (error, data, response) => {
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
 **productsApiFindRequest** | [**ProductsApiFindRequest**](ProductsApiFindRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## subscriptionsApiEnable

> subscriptionsApiEnable(productsApiFindRequest)



### Example

```javascript
import KeyServ from 'key_serv';

let apiInstance = new KeyServ.SubscriptionsApiApi();
let productsApiFindRequest = new KeyServ.ProductsApiFindRequest(); // ProductsApiFindRequest | 
apiInstance.subscriptionsApiEnable(productsApiFindRequest, (error, data, response) => {
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
 **productsApiFindRequest** | [**ProductsApiFindRequest**](ProductsApiFindRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## subscriptionsApiEnable2

> subscriptionsApiEnable2(productsApiFindRequest)



### Example

```javascript
import KeyServ from 'key_serv';

let apiInstance = new KeyServ.SubscriptionsApiApi();
let productsApiFindRequest = new KeyServ.ProductsApiFindRequest(); // ProductsApiFindRequest | 
apiInstance.subscriptionsApiEnable2(productsApiFindRequest, (error, data, response) => {
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
 **productsApiFindRequest** | [**ProductsApiFindRequest**](ProductsApiFindRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## subscriptionsApiFind

> SubscriptionsApiFind200Response subscriptionsApiFind(productsApiFindRequest)



### Example

```javascript
import KeyServ from 'key_serv';

let apiInstance = new KeyServ.SubscriptionsApiApi();
let productsApiFindRequest = new KeyServ.ProductsApiFindRequest(); // ProductsApiFindRequest | 
apiInstance.subscriptionsApiFind(productsApiFindRequest, (error, data, response) => {
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
 **productsApiFindRequest** | [**ProductsApiFindRequest**](ProductsApiFindRequest.md)|  | 

### Return type

[**SubscriptionsApiFind200Response**](SubscriptionsApiFind200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## subscriptionsApiList

> [SubscriptionView] subscriptionsApiList(productsApiFindRequest, opts)



### Example

```javascript
import KeyServ from 'key_serv';

let apiInstance = new KeyServ.SubscriptionsApiApi();
let productsApiFindRequest = new KeyServ.ProductsApiFindRequest(); // ProductsApiFindRequest | 
let opts = {
  'page': 56 // Number | 
};
apiInstance.subscriptionsApiList(productsApiFindRequest, opts, (error, data, response) => {
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
 **productsApiFindRequest** | [**ProductsApiFindRequest**](ProductsApiFindRequest.md)|  | 
 **page** | **Number**|  | [optional] 

### Return type

[**[SubscriptionView]**](SubscriptionView.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## subscriptionsApiPutSubscription

> subscriptionsApiPutSubscription(subscriptionsApiPutSubscriptionRequest)



### Example

```javascript
import KeyServ from 'key_serv';

let apiInstance = new KeyServ.SubscriptionsApiApi();
let subscriptionsApiPutSubscriptionRequest = new KeyServ.SubscriptionsApiPutSubscriptionRequest(); // SubscriptionsApiPutSubscriptionRequest | 
apiInstance.subscriptionsApiPutSubscription(subscriptionsApiPutSubscriptionRequest, (error, data, response) => {
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
 **subscriptionsApiPutSubscriptionRequest** | [**SubscriptionsApiPutSubscriptionRequest**](SubscriptionsApiPutSubscriptionRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## subscriptionsApiPutSubscription2

> subscriptionsApiPutSubscription2(subscriptionsApiPutSubscriptionRequest)



### Example

```javascript
import KeyServ from 'key_serv';

let apiInstance = new KeyServ.SubscriptionsApiApi();
let subscriptionsApiPutSubscriptionRequest = new KeyServ.SubscriptionsApiPutSubscriptionRequest(); // SubscriptionsApiPutSubscriptionRequest | 
apiInstance.subscriptionsApiPutSubscription2(subscriptionsApiPutSubscriptionRequest, (error, data, response) => {
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
 **subscriptionsApiPutSubscriptionRequest** | [**SubscriptionsApiPutSubscriptionRequest**](SubscriptionsApiPutSubscriptionRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## subscriptionsApiSave

> KeysApiFind200Response subscriptionsApiSave(subscriptionsApiPutSubscriptionRequest)



### Example

```javascript
import KeyServ from 'key_serv';

let apiInstance = new KeyServ.SubscriptionsApiApi();
let subscriptionsApiPutSubscriptionRequest = new KeyServ.SubscriptionsApiPutSubscriptionRequest(); // SubscriptionsApiPutSubscriptionRequest | 
apiInstance.subscriptionsApiSave(subscriptionsApiPutSubscriptionRequest, (error, data, response) => {
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
 **subscriptionsApiPutSubscriptionRequest** | [**SubscriptionsApiPutSubscriptionRequest**](SubscriptionsApiPutSubscriptionRequest.md)|  | 

### Return type

[**KeysApiFind200Response**](KeysApiFind200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

