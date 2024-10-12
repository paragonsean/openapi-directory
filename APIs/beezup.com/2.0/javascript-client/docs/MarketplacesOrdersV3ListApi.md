# BeezUpMerchantApi.MarketplacesOrdersV3ListApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getOrderListFullV3**](MarketplacesOrdersV3ListApi.md#getOrderListFullV3) | **POST** /orders/v3/list/full | Get a paginated list of all Orders with all Order and Order Item(s) properties
[**getOrderListLightV3**](MarketplacesOrdersV3ListApi.md#getOrderListLightV3) | **POST** /orders/v3/list/light | Get a paginated list of all Orders without details



## getOrderListFullV3

> OrderListFullWithLinks getOrderListFullV3(acceptEncoding, orderListRequest)

Get a paginated list of all Orders with all Order and Order Item(s) properties

The purpose of this operation is to reduce the amount of request to the API.\\ \\ Previous implmentation of this feature only returned a partial (light) version of the Orders. The purpose of this API is to reduce the number of incoming requests by returning the complete (full) Order and Order Item(s) properties. 

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersV3ListApi();
let acceptEncoding = "acceptEncoding_example"; // String | Allows the client to indicate wether it accepts a compressed encoding to reduce traffic size
let orderListRequest = new BeezUpMerchantApi.OrderListRequest(); // OrderListRequest | 
apiInstance.getOrderListFullV3(acceptEncoding, orderListRequest, (error, data, response) => {
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
 **acceptEncoding** | **String**| Allows the client to indicate wether it accepts a compressed encoding to reduce traffic size | 
 **orderListRequest** | [**OrderListRequest**](OrderListRequest.md)|  | 

### Return type

[**OrderListFullWithLinks**](OrderListFullWithLinks.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getOrderListLightV3

> OrderListLightWithLinks getOrderListLightV3(orderListRequest)

Get a paginated list of all Orders without details

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersV3ListApi();
let orderListRequest = new BeezUpMerchantApi.OrderListRequest(); // OrderListRequest | 
apiInstance.getOrderListLightV3(orderListRequest, (error, data, response) => {
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
 **orderListRequest** | [**OrderListRequest**](OrderListRequest.md)|  | 

### Return type

[**OrderListLightWithLinks**](OrderListLightWithLinks.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

