# BeezUpMerchantApi.MarketplacesOrdersOrderApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**changeOrder**](MarketplacesOrdersOrderApi.md#changeOrder) | **POST** /v2/user/marketplaces/orders/{marketplaceTechnicalCode}/{accountId}/{beezUPOrderId}/{changeOrderType} | [DEPRECATED] Change your marketplace Order Information (accept, ship, etc.)
[**clearMerchantOrderInfo**](MarketplacesOrdersOrderApi.md#clearMerchantOrderInfo) | **POST** /v2/user/marketplaces/orders/{marketplaceTechnicalCode}/{accountId}/{beezUPOrderId}/clearMerchantOrderInfo | [DEPRECATED] Clear an Order&#39;s merchant information
[**getOrder**](MarketplacesOrdersOrderApi.md#getOrder) | **GET** /v2/user/marketplaces/orders/{marketplaceTechnicalCode}/{accountId}/{beezUPOrderId} | [DEPRECATED] DEPRECATED - Get full Order and Order Item(s) properties
[**getOrderHistory**](MarketplacesOrdersOrderApi.md#getOrderHistory) | **GET** /v2/user/marketplaces/orders/{marketplaceTechnicalCode}/{accountId}/{beezUPOrderId}/history | [DEPRECATED] Get an Order&#39;s harvest and change history
[**harvestOrder**](MarketplacesOrdersOrderApi.md#harvestOrder) | **POST** /v2/user/marketplaces/orders/{marketplaceTechnicalCode}/{accountId}/{beezUPOrderId}/harvest | [DEPRECATED] Send harvest request for a single Order
[**headOrder**](MarketplacesOrdersOrderApi.md#headOrder) | **HEAD** /v2/user/marketplaces/orders/{marketplaceTechnicalCode}/{accountId}/{beezUPOrderId} | [DEPRECATED] DEPRECATED - Get the meta information about the order (ETag, Last-Modified)
[**setMerchantOrderInfo**](MarketplacesOrdersOrderApi.md#setMerchantOrderInfo) | **POST** /v2/user/marketplaces/orders/{marketplaceTechnicalCode}/{accountId}/{beezUPOrderId}/setMerchantOrderInfo | [DEPRECATED] Set an Order&#39;s merchant information



## changeOrder

> changeOrder(marketplaceTechnicalCode, accountId, beezUPOrderId, changeOrderType, userName, ifMatch, opts)

[DEPRECATED] Change your marketplace Order Information (accept, ship, etc.)

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersOrderApi();
let marketplaceTechnicalCode = "Amazon"; // String | The marketplace technical code
let accountId = 1001; // Number | 
let beezUPOrderId = "00000000000000000000000000000000000000000000000"; // String | The BeezUP Order identifier
let changeOrderType = "changeOrderType_example"; // String | The Order change type
let userName = "userName_example"; // String | Sometimes the user in the e-commerce application is not the same as user associated with the current subscription key. We recommend providing your application's user login.
let ifMatch = "ifMatch_example"; // String | ETag value to identify the last known version of requested resource.\\ To ensure that you are making a change on the lastest version of the resource.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
let opts = {
  'testMode': false, // Boolean | If true, the operation will be not be sent to marketplace. But the validation will be taken in account.
  'requestBody': {key: "null"} // {String: String} | 
};
apiInstance.changeOrder(marketplaceTechnicalCode, accountId, beezUPOrderId, changeOrderType, userName, ifMatch, opts, (error, data, response) => {
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
 **marketplaceTechnicalCode** | **String**| The marketplace technical code | 
 **accountId** | **Number**|  | 
 **beezUPOrderId** | **String**| The BeezUP Order identifier | 
 **changeOrderType** | **String**| The Order change type | 
 **userName** | **String**| Sometimes the user in the e-commerce application is not the same as user associated with the current subscription key. We recommend providing your application&#39;s user login. | 
 **ifMatch** | **String**| ETag value to identify the last known version of requested resource.\\ To ensure that you are making a change on the lastest version of the resource.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  | 
 **testMode** | **Boolean**| If true, the operation will be not be sent to marketplace. But the validation will be taken in account. | [optional] [default to false]
 **requestBody** | [**{String: String}**](String.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## clearMerchantOrderInfo

> clearMerchantOrderInfo(marketplaceTechnicalCode, accountId, beezUPOrderId)

[DEPRECATED] Clear an Order&#39;s merchant information

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersOrderApi();
let marketplaceTechnicalCode = "Amazon"; // String | The marketplace technical code
let accountId = 1001; // Number | 
let beezUPOrderId = "00000000000000000000000000000000000000000000000"; // String | The BeezUP Order identifier
apiInstance.clearMerchantOrderInfo(marketplaceTechnicalCode, accountId, beezUPOrderId, (error, data, response) => {
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
 **marketplaceTechnicalCode** | **String**| The marketplace technical code | 
 **accountId** | **Number**|  | 
 **beezUPOrderId** | **String**| The BeezUP Order identifier | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrder

> Order getOrder(marketplaceTechnicalCode, accountId, beezUPOrderId, opts)

[DEPRECATED] DEPRECATED - Get full Order and Order Item(s) properties

DEPRECATED - Use /orders/v3 instead

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersOrderApi();
let marketplaceTechnicalCode = "Amazon"; // String | The marketplace technical code
let accountId = 1001; // Number | 
let beezUPOrderId = "00000000000000000000000000000000000000000000000"; // String | The BeezUP Order identifier
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
};
apiInstance.getOrder(marketplaceTechnicalCode, accountId, beezUPOrderId, opts, (error, data, response) => {
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
 **marketplaceTechnicalCode** | **String**| The marketplace technical code | 
 **accountId** | **Number**|  | 
 **beezUPOrderId** | **String**| The BeezUP Order identifier | 
 **ifNoneMatch** | **String**| ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  | [optional] 

### Return type

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrderHistory

> OrderHistory getOrderHistory(marketplaceTechnicalCode, accountId, beezUPOrderId, opts)

[DEPRECATED] Get an Order&#39;s harvest and change history

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersOrderApi();
let marketplaceTechnicalCode = "Amazon"; // String | The marketplace technical code
let accountId = 1001; // Number | 
let beezUPOrderId = "00000000000000000000000000000000000000000000000"; // String | The BeezUP Order identifier
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
};
apiInstance.getOrderHistory(marketplaceTechnicalCode, accountId, beezUPOrderId, opts, (error, data, response) => {
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
 **marketplaceTechnicalCode** | **String**| The marketplace technical code | 
 **accountId** | **Number**|  | 
 **beezUPOrderId** | **String**| The BeezUP Order identifier | 
 **ifNoneMatch** | **String**| ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  | [optional] 

### Return type

[**OrderHistory**](OrderHistory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## harvestOrder

> harvestOrder(marketplaceTechnicalCode, accountId, beezUPOrderId)

[DEPRECATED] Send harvest request for a single Order

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersOrderApi();
let marketplaceTechnicalCode = "Amazon"; // String | The marketplace technical code
let accountId = 1001; // Number | 
let beezUPOrderId = "00000000000000000000000000000000000000000000000"; // String | The BeezUP Order identifier
apiInstance.harvestOrder(marketplaceTechnicalCode, accountId, beezUPOrderId, (error, data, response) => {
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
 **marketplaceTechnicalCode** | **String**| The marketplace technical code | 
 **accountId** | **Number**|  | 
 **beezUPOrderId** | **String**| The BeezUP Order identifier | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## headOrder

> headOrder(marketplaceTechnicalCode, accountId, beezUPOrderId, opts)

[DEPRECATED] DEPRECATED - Get the meta information about the order (ETag, Last-Modified)

DEPRECATED - Use /orders/v3 instead The purpose of this operation is to reduce the bandwith usage by getting just the meta information about the order (ETag, Last-Modified) with the body. This could be useful 

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersOrderApi();
let marketplaceTechnicalCode = "Amazon"; // String | The marketplace technical code
let accountId = 1001; // Number | 
let beezUPOrderId = "00000000000000000000000000000000000000000000000"; // String | The BeezUP Order identifier
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
};
apiInstance.headOrder(marketplaceTechnicalCode, accountId, beezUPOrderId, opts, (error, data, response) => {
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
 **marketplaceTechnicalCode** | **String**| The marketplace technical code | 
 **accountId** | **Number**|  | 
 **beezUPOrderId** | **String**| The BeezUP Order identifier | 
 **ifNoneMatch** | **String**| ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setMerchantOrderInfo

> setMerchantOrderInfo(marketplaceTechnicalCode, accountId, beezUPOrderId, setMerchantOrderInfoRequest)

[DEPRECATED] Set an Order&#39;s merchant information

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersOrderApi();
let marketplaceTechnicalCode = "Amazon"; // String | The marketplace technical code
let accountId = 1001; // Number | 
let beezUPOrderId = "00000000000000000000000000000000000000000000000"; // String | The BeezUP Order identifier
let setMerchantOrderInfoRequest = new BeezUpMerchantApi.SetMerchantOrderInfoRequest(); // SetMerchantOrderInfoRequest | 
apiInstance.setMerchantOrderInfo(marketplaceTechnicalCode, accountId, beezUPOrderId, setMerchantOrderInfoRequest, (error, data, response) => {
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
 **marketplaceTechnicalCode** | **String**| The marketplace technical code | 
 **accountId** | **Number**|  | 
 **beezUPOrderId** | **String**| The BeezUP Order identifier | 
 **setMerchantOrderInfoRequest** | [**SetMerchantOrderInfoRequest**](SetMerchantOrderInfoRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

