# GiftCardApi.GiftCardApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createGiftCard**](GiftCardApi.md#createGiftCard) | **POST** /giftcards | Create GiftCard
[**getGiftCardbyID**](GiftCardApi.md#getGiftCardbyID) | **GET** /giftcards/{giftCardID} | Get GiftCard by ID
[**getGiftCardusingJSON**](GiftCardApi.md#getGiftCardusingJSON) | **POST** /giftcards/_search | Get GiftCard using JSON



## createGiftCard

> Response createGiftCard(contentType, accept, xVTEXAPIAppKey, xVTEXAPIAppToken, createGiftCardRequest)

Create GiftCard

Creates a GiftCard for a specific user

### Example

```javascript
import GiftCardApi from 'gift_card_api';
let defaultClient = GiftCardApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new GiftCardApi.GiftCardApi();
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let xVTEXAPIAppKey = "'{{X-VTEX-API-AppKey}}'"; // String | The AppKey configured by the merchant
let xVTEXAPIAppToken = "'{{X-VTEX-API-AppToken}}'"; // String | The AppToken configured by the merchant
let createGiftCardRequest = new GiftCardApi.CreateGiftCardRequest(); // CreateGiftCardRequest | 
apiInstance.createGiftCard(contentType, accept, xVTEXAPIAppKey, xVTEXAPIAppToken, createGiftCardRequest, (error, data, response) => {
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
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **xVTEXAPIAppKey** | **String**| The AppKey configured by the merchant | [default to &#39;{{X-VTEX-API-AppKey}}&#39;]
 **xVTEXAPIAppToken** | **String**| The AppToken configured by the merchant | [default to &#39;{{X-VTEX-API-AppToken}}&#39;]
 **createGiftCardRequest** | [**CreateGiftCardRequest**](CreateGiftCardRequest.md)|  | 

### Return type

[**Response**](Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/vnd.vtex.giftcard.v1+json
- **Accept**: application/json


## getGiftCardbyID

> Response getGiftCardbyID(accept, contentType, giftCardID)

Get GiftCard by ID

Returns associated data for a specified giftcardId.

### Example

```javascript
import GiftCardApi from 'gift_card_api';
let defaultClient = GiftCardApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new GiftCardApi.GiftCardApi();
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let giftCardID = "'2'"; // String | 
apiInstance.getGiftCardbyID(accept, contentType, giftCardID, (error, data, response) => {
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
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **giftCardID** | **String**|  | [default to &#39;2&#39;]

### Return type

[**Response**](Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGiftCardusingJSON

> Response2 getGiftCardusingJSON(accept, contentType, getGiftCardusingJSONRequest, opts)

Get GiftCard using JSON

Returns the giftcards based on the cart data.

### Example

```javascript
import GiftCardApi from 'gift_card_api';
let defaultClient = GiftCardApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new GiftCardApi.GiftCardApi();
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let getGiftCardusingJSONRequest = {"cart":{"discounts":0,"grandTotal":123.1,"items":[{"id":"1","name":"Product Name","price":100,"productId":"1","quantity":1,"refId":"12"}],"itemsTotal":100,"redemptionCode":null,"relationName":null,"shipping":0,"taxes":12},"client":{"document":"21301923110","email":"email@damoain.com","id":"019a0cc1-409a-4c16-859b-eefdb81f825e"}}; // GetGiftCardusingJSONRequest | 
let opts = {
  'rESTRange': "'giftcard=0-49'" // String | PaginationB control.B ThisB queryB variableB mustB followB theB formatB _resources={from}-{to}_.
};
apiInstance.getGiftCardusingJSON(accept, contentType, getGiftCardusingJSONRequest, opts, (error, data, response) => {
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
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **getGiftCardusingJSONRequest** | [**GetGiftCardusingJSONRequest**](GetGiftCardusingJSONRequest.md)|  | 
 **rESTRange** | **String**| PaginationB control.B ThisB queryB variableB mustB followB theB formatB _resources&#x3D;{from}-{to}_. | [optional] [default to &#39;giftcard&#x3D;0-49&#39;]

### Return type

[**Response2**](Response2.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

