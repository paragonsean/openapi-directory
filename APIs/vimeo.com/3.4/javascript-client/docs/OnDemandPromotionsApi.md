# Vimeo.OnDemandPromotionsApi

All URIs are relative to *https://api.vimeo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createVodPromotion**](OnDemandPromotionsApi.md#createVodPromotion) | **POST** /ondemand/pages/{ondemand_id}/promotions | Add a promotion to an On Demand page
[**deleteVodPromotion**](OnDemandPromotionsApi.md#deleteVodPromotion) | **DELETE** /ondemand/pages/{ondemand_id}/promotions/{promotion_id} | Remove a promotion from an On Demand page
[**getVodPromotion**](OnDemandPromotionsApi.md#getVodPromotion) | **GET** /ondemand/pages/{ondemand_id}/promotions/{promotion_id} | Get a specific promotion on an On Demand page
[**getVodPromotionCodes**](OnDemandPromotionsApi.md#getVodPromotionCodes) | **GET** /ondemand/pages/{ondemand_id}/promotions/{promotion_id}/codes | Get all the codes of a promotion on an On Demand page
[**getVodPromotions**](OnDemandPromotionsApi.md#getVodPromotions) | **GET** /ondemand/pages/{ondemand_id}/promotions | Get all the promotions on an On Demand page



## createVodPromotion

> OnDemandPromotion createVodPromotion(ondemandId, createVodPromotionRequest)

Add a promotion to an On Demand page

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.OnDemandPromotionsApi();
let ondemandId = 61326; // Number | The ID of the On Demand.
let createVodPromotionRequest = new Vimeo.CreateVodPromotionRequest(); // CreateVodPromotionRequest | 
apiInstance.createVodPromotion(ondemandId, createVodPromotionRequest, (error, data, response) => {
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
 **ondemandId** | **Number**| The ID of the On Demand. | 
 **createVodPromotionRequest** | [**CreateVodPromotionRequest**](CreateVodPromotionRequest.md)|  | 

### Return type

[**OnDemandPromotion**](OnDemandPromotion.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.ondemand.promotion+json
- **Accept**: application/vnd.vimeo.ondemand.promotion+json


## deleteVodPromotion

> deleteVodPromotion(ondemandId, promotionId)

Remove a promotion from an On Demand page

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.OnDemandPromotionsApi();
let ondemandId = 61326; // Number | The ID of the On Demand.
let promotionId = 12345; // Number | The ID of the promotion.
apiInstance.deleteVodPromotion(ondemandId, promotionId, (error, data, response) => {
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
 **ondemandId** | **Number**| The ID of the On Demand. | 
 **promotionId** | **Number**| The ID of the promotion. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVodPromotion

> OnDemandPromotion getVodPromotion(ondemandId, promotionId)

Get a specific promotion on an On Demand page

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.OnDemandPromotionsApi();
let ondemandId = 61326; // Number | The ID of the On Demand.
let promotionId = 12345; // Number | The ID of the promotion.
apiInstance.getVodPromotion(ondemandId, promotionId, (error, data, response) => {
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
 **ondemandId** | **Number**| The ID of the On Demand. | 
 **promotionId** | **Number**| The ID of the promotion. | 

### Return type

[**OnDemandPromotion**](OnDemandPromotion.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.ondemand.promotion+json


## getVodPromotionCodes

> OnDemandPromotionCode getVodPromotionCodes(ondemandId, promotionId, opts)

Get all the codes of a promotion on an On Demand page

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.OnDemandPromotionsApi();
let ondemandId = 61326; // Number | The ID of the On Demand.
let promotionId = 12345; // Number | The ID of the promotion.
let opts = {
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10 // Number | The number of items to show on each page of results, up to a maximum of 100.
};
apiInstance.getVodPromotionCodes(ondemandId, promotionId, opts, (error, data, response) => {
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
 **ondemandId** | **Number**| The ID of the On Demand. | 
 **promotionId** | **Number**| The ID of the promotion. | 
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 

### Return type

[**OnDemandPromotionCode**](OnDemandPromotionCode.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.ondemand.promocode+json


## getVodPromotions

> OnDemandPromotion getVodPromotions(ondemandId, filter, opts)

Get all the promotions on an On Demand page

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.OnDemandPromotionsApi();
let ondemandId = 61326; // Number | The ID of the On Demand.
let filter = "filter_example"; // String | The filter to apply to the results.
let opts = {
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10 // Number | The number of items to show on each page of results, up to a maximum of 100.
};
apiInstance.getVodPromotions(ondemandId, filter, opts, (error, data, response) => {
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
 **ondemandId** | **Number**| The ID of the On Demand. | 
 **filter** | **String**| The filter to apply to the results. | 
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 

### Return type

[**OnDemandPromotion**](OnDemandPromotion.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.ondemand.promotion+json

