# BeezUpMerchantApi.MarketplacesOrdersAutoTransitionsApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configureAutomaticTransitions**](MarketplacesOrdersAutoTransitionsApi.md#configureAutomaticTransitions) | **POST** /v2/user/marketplaces/orders/automaticTransitions | Configure new or existing automatic Order status transition
[**getAutomaticTransitions**](MarketplacesOrdersAutoTransitionsApi.md#getAutomaticTransitions) | **GET** /v2/user/marketplaces/orders/automaticTransitions | Get list of configured automatic Order status transitions



## configureAutomaticTransitions

> configureAutomaticTransitions(configureAutomaticTransitionRequest)

Configure new or existing automatic Order status transition

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersAutoTransitionsApi();
let configureAutomaticTransitionRequest = new BeezUpMerchantApi.ConfigureAutomaticTransitionRequest(); // ConfigureAutomaticTransitionRequest | 
apiInstance.configureAutomaticTransitions(configureAutomaticTransitionRequest, (error, data, response) => {
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
 **configureAutomaticTransitionRequest** | [**ConfigureAutomaticTransitionRequest**](ConfigureAutomaticTransitionRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAutomaticTransitions

> AutomaticTransitionInfoList getAutomaticTransitions(opts)

Get list of configured automatic Order status transitions

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersAutoTransitionsApi();
let opts = {
  'storeId': "04730364-9826-4ff3-92e4-51fccd02bf10", // String | The StoreId to filter by
  'ifNoneMatch': "ifNoneMatch_example" // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
};
apiInstance.getAutomaticTransitions(opts, (error, data, response) => {
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
 **storeId** | **String**| The StoreId to filter by | [optional] 
 **ifNoneMatch** | **String**| ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  | [optional] 

### Return type

[**AutomaticTransitionInfoList**](AutomaticTransitionInfoList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

