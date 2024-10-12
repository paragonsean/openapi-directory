# BeezUpMerchantApi.MarketplacesOrdersListApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getOrderListFull**](MarketplacesOrdersListApi.md#getOrderListFull) | **POST** /v2/user/marketplaces/orders/list/full | [DEPRECATED] Get a paginated list of all Orders with all Order and Order Item(s) properties
[**getOrderListLight**](MarketplacesOrdersListApi.md#getOrderListLight) | **POST** /v2/user/marketplaces/orders/list/light | [DEPRECATED] Get a paginated list of all Orders without details



## getOrderListFull

> OrderListFull getOrderListFull(acceptEncoding, orderListRequest)

[DEPRECATED] Get a paginated list of all Orders with all Order and Order Item(s) properties

DEPRECATED - Use /orders/v3 instead The purpose of this operation is to reduce the amount of request to the API.\\ \\ Previous implmentation of this feature only returned a partial (light) version of the Orders. The purpose of this API is to reduce the number of incoming requests by returning the complete (full) Order and Order Item(s) properties. 

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersListApi();
let acceptEncoding = ["null"]; // [String] | Allows the client to indicate wether it accepts a compressed encoding to reduce traffic size
let orderListRequest = new BeezUpMerchantApi.OrderListRequest(); // OrderListRequest | 
apiInstance.getOrderListFull(acceptEncoding, orderListRequest, (error, data, response) => {
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
 **acceptEncoding** | [**[String]**](String.md)| Allows the client to indicate wether it accepts a compressed encoding to reduce traffic size | 
 **orderListRequest** | [**OrderListRequest**](OrderListRequest.md)|  | 

### Return type

[**OrderListFull**](OrderListFull.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getOrderListLight

> OrderListLight getOrderListLight(orderListRequest)

[DEPRECATED] Get a paginated list of all Orders without details

Use /orders/v3 instead

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersListApi();
let orderListRequest = new BeezUpMerchantApi.OrderListRequest(); // OrderListRequest | 
apiInstance.getOrderListLight(orderListRequest, (error, data, response) => {
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

[**OrderListLight**](OrderListLight.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

