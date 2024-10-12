# GiftCardHubApi.ProviderApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createUpdateGiftCardProviderbyID**](ProviderApi.md#createUpdateGiftCardProviderbyID) | **PUT** /giftcardproviders/{giftCardProviderID} | Create/Update GiftCard Provider by ID
[**deleteGiftCardProviderbyID**](ProviderApi.md#deleteGiftCardProviderbyID) | **DELETE** /giftcardproviders/{giftCardProviderID} | Delete GiftCard Provider by ID
[**getGiftCardProviderbyID**](ProviderApi.md#getGiftCardProviderbyID) | **GET** /giftcardproviders/{giftCardProviderId} | Get GiftCard Provider by ID
[**listAllGiftCardProviders**](ProviderApi.md#listAllGiftCardProviders) | **GET** /giftcardproviders | List All GiftCard Providers



## createUpdateGiftCardProviderbyID

> Object createUpdateGiftCardProviderbyID(accept, contentType, xVTEXAPIAppKey, xVTEXAPIAppToken, giftCardProviderID, createUpdateGiftCardProviderbyIDRequest)

Create/Update GiftCard Provider by ID

Create or update a giftcard provider from a store.

### Example

```javascript
import GiftCardHubApi from 'gift_card_hub_api';
let defaultClient = GiftCardHubApi.ApiClient.instance;
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

let apiInstance = new GiftCardHubApi.ProviderApi();
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json.
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let xVTEXAPIAppKey = "'{{X-VTEX-API-AppKey}}'"; // String | VTEX API AppKey
let xVTEXAPIAppToken = "'{{X-VTEX-API-AppToken}}'"; // String | VTEX API AppToken
let giftCardProviderID = "'insert identifier here'"; // String | Gift Card provider's ID.
let createUpdateGiftCardProviderbyIDRequest = {"cancelEnabled":true,"oauthProvider":"vtex","preAuthEnabled":true,"serviceUrl":"https://api.vtex.com.br/basedevmkp"}; // CreateUpdateGiftCardProviderbyIDRequest | 
apiInstance.createUpdateGiftCardProviderbyID(accept, contentType, xVTEXAPIAppKey, xVTEXAPIAppToken, giftCardProviderID, createUpdateGiftCardProviderbyIDRequest, (error, data, response) => {
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
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json. | [default to &#39;application/json&#39;]
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **xVTEXAPIAppKey** | **String**| VTEX API AppKey | [default to &#39;{{X-VTEX-API-AppKey}}&#39;]
 **xVTEXAPIAppToken** | **String**| VTEX API AppToken | [default to &#39;{{X-VTEX-API-AppToken}}&#39;]
 **giftCardProviderID** | **String**| Gift Card provider&#39;s ID. | [default to &#39;insert identifier here&#39;]
 **createUpdateGiftCardProviderbyIDRequest** | [**CreateUpdateGiftCardProviderbyIDRequest**](CreateUpdateGiftCardProviderbyIDRequest.md)|  | 

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/vnd.vtex.giftcardproviders.v1+json
- **Accept**: text/plain


## deleteGiftCardProviderbyID

> Object deleteGiftCardProviderbyID(accept, contentType, xVTEXAPIAppKey, xVTEXAPIAppToken, giftCardProviderID)

Delete GiftCard Provider by ID

Delete a giftcard provider from a store.

### Example

```javascript
import GiftCardHubApi from 'gift_card_hub_api';
let defaultClient = GiftCardHubApi.ApiClient.instance;
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

let apiInstance = new GiftCardHubApi.ProviderApi();
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json.
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json.
let xVTEXAPIAppKey = "'{{X-VTEX-API-AppKey}}'"; // String | VTEX API AppKey
let xVTEXAPIAppToken = "'{{X-VTEX-API-AppToken}}'"; // String | VTEX API AppToken
let giftCardProviderID = "'insert identifier here'"; // String | Gift Card provider's ID.
apiInstance.deleteGiftCardProviderbyID(accept, contentType, xVTEXAPIAppKey, xVTEXAPIAppToken, giftCardProviderID, (error, data, response) => {
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
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json. | [default to &#39;application/json&#39;]
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json. | [default to &#39;application/json&#39;]
 **xVTEXAPIAppKey** | **String**| VTEX API AppKey | [default to &#39;{{X-VTEX-API-AppKey}}&#39;]
 **xVTEXAPIAppToken** | **String**| VTEX API AppToken | [default to &#39;{{X-VTEX-API-AppToken}}&#39;]
 **giftCardProviderID** | **String**| Gift Card provider&#39;s ID. | [default to &#39;insert identifier here&#39;]

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain


## getGiftCardProviderbyID

> Object getGiftCardProviderbyID(accept, contentType, xVTEXAPIAppKey, xVTEXAPIAppToken, giftCardProviderId)

Get GiftCard Provider by ID

Returns a giftcard provider from a store.

### Example

```javascript
import GiftCardHubApi from 'gift_card_hub_api';
let defaultClient = GiftCardHubApi.ApiClient.instance;
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

let apiInstance = new GiftCardHubApi.ProviderApi();
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json.
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json.
let xVTEXAPIAppKey = "'{{X-VTEX-API-AppKey}}'"; // String | VTEX API AppKey
let xVTEXAPIAppToken = "'{{X-VTEX-API-AppToken}}'"; // String | VTEX API AppToken
let giftCardProviderId = "'insert identifier here'"; // String | Gift Card provider's ID.
apiInstance.getGiftCardProviderbyID(accept, contentType, xVTEXAPIAppKey, xVTEXAPIAppToken, giftCardProviderId, (error, data, response) => {
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
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json. | [default to &#39;application/json&#39;]
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json. | [default to &#39;application/json&#39;]
 **xVTEXAPIAppKey** | **String**| VTEX API AppKey | [default to &#39;{{X-VTEX-API-AppKey}}&#39;]
 **xVTEXAPIAppToken** | **String**| VTEX API AppToken | [default to &#39;{{X-VTEX-API-AppToken}}&#39;]
 **giftCardProviderId** | **String**| Gift Card provider&#39;s ID. | [default to &#39;insert identifier here&#39;]

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain


## listAllGiftCardProviders

> Object listAllGiftCardProviders(accept, contentType, xVTEXAPIAppKey, xVTEXAPIAppToken, opts)

List All GiftCard Providers

Returns a collection of giftcard providers from a store.

### Example

```javascript
import GiftCardHubApi from 'gift_card_hub_api';

let apiInstance = new GiftCardHubApi.ProviderApi();
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json.
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json.
let xVTEXAPIAppKey = "'{{X-VTEX-API-AppKey}}'"; // String | VTEX API AppKey
let xVTEXAPIAppToken = "'{{X-VTEX-API-AppToken}}'"; // String | VTEX API AppToken
let opts = {
  'rESTRange': "'resources=0-49'" // String | Pagination control. This query variable must follow the format _resources={from}-{to}_.
};
apiInstance.listAllGiftCardProviders(accept, contentType, xVTEXAPIAppKey, xVTEXAPIAppToken, opts, (error, data, response) => {
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
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json. | [default to &#39;application/json&#39;]
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json. | [default to &#39;application/json&#39;]
 **xVTEXAPIAppKey** | **String**| VTEX API AppKey | [default to &#39;{{X-VTEX-API-AppKey}}&#39;]
 **xVTEXAPIAppToken** | **String**| VTEX API AppToken | [default to &#39;{{X-VTEX-API-AppToken}}&#39;]
 **rESTRange** | **String**| Pagination control. This query variable must follow the format _resources&#x3D;{from}-{to}_. | [optional] [default to &#39;resources&#x3D;0-49&#39;]

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain

