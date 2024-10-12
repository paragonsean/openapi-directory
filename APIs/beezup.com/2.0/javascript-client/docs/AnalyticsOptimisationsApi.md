# BeezUpMerchantApi.AnalyticsOptimisationsApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copyOptimisation**](AnalyticsOptimisationsApi.md#copyOptimisation) | **POST** /v2/user/analytics/{storeId}/optimisations/copy | Copy product optimisations between 2 channels
[**optimise**](AnalyticsOptimisationsApi.md#optimise) | **POST** /v2/user/analytics/{storeId}/optimisations/{actionName} | Optimise products by page
[**optimiseAll**](AnalyticsOptimisationsApi.md#optimiseAll) | **POST** /v2/user/analytics/{storeId}/optimisations/all/{actionName} | Optimise all products
[**optimiseByCategory**](AnalyticsOptimisationsApi.md#optimiseByCategory) | **POST** /v2/user/analytics/{storeId}/optimisations/bycategory/{catalogCategoryId}/{actionName} | Optimise products by category
[**optimiseByChannel**](AnalyticsOptimisationsApi.md#optimiseByChannel) | **POST** /v2/user/analytics/{storeId}/optimisations/bychannel/{channelId}/{actionName} | Optimise products by channel
[**optimiseByProduct**](AnalyticsOptimisationsApi.md#optimiseByProduct) | **POST** /v2/user/analytics/{storeId}/optimisations/byproduct/{productId}/{actionName} | Optimise product



## copyOptimisation

> CopyOptimisationResponse copyOptimisation(storeId, copyOptimisationRequest)

Copy product optimisations between 2 channels

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.AnalyticsOptimisationsApi();
let storeId = "storeId_example"; // String | Your store identifier
let copyOptimisationRequest = new BeezUpMerchantApi.CopyOptimisationRequest(); // CopyOptimisationRequest | 
apiInstance.copyOptimisation(storeId, copyOptimisationRequest, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 
 **copyOptimisationRequest** | [**CopyOptimisationRequest**](CopyOptimisationRequest.md)|  | 

### Return type

[**CopyOptimisationResponse**](CopyOptimisationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## optimise

> optimise(storeId, actionName, optimiseRequest)

Optimise products by page

/!\\ WARNING /!\\ \\ Apply the operation on every product related to this request. \\ This operation is used at the bottom of the analytics page result. 

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.AnalyticsOptimisationsApi();
let storeId = "storeId_example"; // String | Your store identifier
let actionName = "actionName_example"; // String | 
let optimiseRequest = new BeezUpMerchantApi.OptimiseRequest(); // OptimiseRequest | 
apiInstance.optimise(storeId, actionName, optimiseRequest, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 
 **actionName** | **String**|  | 
 **optimiseRequest** | [**OptimiseRequest**](OptimiseRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## optimiseAll

> optimiseAll(storeId, actionName, optimiseAllRequest)

Optimise all products

/!\\ WARNING /!\\ \\ Apply the operation on every product related to this request. \\ This operation is used at the bottom of the analytics page result. 

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.AnalyticsOptimisationsApi();
let storeId = "storeId_example"; // String | Your store identifier
let actionName = "actionName_example"; // String | 
let optimiseAllRequest = new BeezUpMerchantApi.OptimiseAllRequest(); // OptimiseAllRequest | 
apiInstance.optimiseAll(storeId, actionName, optimiseAllRequest, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 
 **actionName** | **String**|  | 
 **optimiseAllRequest** | [**OptimiseAllRequest**](OptimiseAllRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## optimiseByCategory

> optimiseByCategory(storeId, catalogCategoryId, actionName, opts)

Optimise products by category

/!\\ WARNING /!\\ \\ This operation will reenable or disable products&#39;s category for every channel indicated in the body. 

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.AnalyticsOptimisationsApi();
let storeId = "storeId_example"; // String | Your store identifier
let catalogCategoryId = "catalogCategoryId_example"; // String | The category identifier concerned by this optimisation
let actionName = "actionName_example"; // String | 
let opts = {
  'requestBody': ["null"] // [String] | The channel identifier list concerned by this optimisation
};
apiInstance.optimiseByCategory(storeId, catalogCategoryId, actionName, opts, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 
 **catalogCategoryId** | **String**| The category identifier concerned by this optimisation | 
 **actionName** | **String**|  | 
 **requestBody** | [**[String]**](String.md)| The channel identifier list concerned by this optimisation | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## optimiseByChannel

> optimiseByChannel(storeId, channelId, actionName)

Optimise products by channel

/!\\ WARNING /!\\ \\ Apply the operation on every product on this channel. 

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.AnalyticsOptimisationsApi();
let storeId = "storeId_example"; // String | Your store identifier
let channelId = "channelId_example"; // String | The channel identifier concerned by this optimisation
let actionName = "actionName_example"; // String | 
apiInstance.optimiseByChannel(storeId, channelId, actionName, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 
 **channelId** | **String**| The channel identifier concerned by this optimisation | 
 **actionName** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## optimiseByProduct

> optimiseByProduct(storeId, productId, actionName, opts)

Optimise product

/!\\ WARNING /!\\ \\ This operation will reenable or disable this product for every channel indicated in the body. 

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.AnalyticsOptimisationsApi();
let storeId = "storeId_example"; // String | Your store identifier
let productId = "productId_example"; // String | The product identifier concerned by this optimisation
let actionName = "actionName_example"; // String | 
let opts = {
  'requestBody': ["null"] // [String] | The channel identifier list concerned by this optimisation
};
apiInstance.optimiseByProduct(storeId, productId, actionName, opts, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 
 **productId** | **String**| The product identifier concerned by this optimisation | 
 **actionName** | **String**|  | 
 **requestBody** | [**[String]**](String.md)| The channel identifier list concerned by this optimisation | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

