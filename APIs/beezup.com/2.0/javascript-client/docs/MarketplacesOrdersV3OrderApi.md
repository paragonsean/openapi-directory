# BeezUpMerchantApi.MarketplacesOrdersV3OrderApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**changeOrderV3**](MarketplacesOrdersV3OrderApi.md#changeOrderV3) | **POST** /orders/v3/{marketplaceTechnicalCode}/{accountId}/{beezUPOrderId}/{changeOrderType} | Change your marketplace Order Information (accept, ship, etc.)
[**clearMerchantOrderInfoV3**](MarketplacesOrdersV3OrderApi.md#clearMerchantOrderInfoV3) | **POST** /orders/v3/{marketplaceTechnicalCode}/{accountId}/{beezUPOrderId}/clearMerchantOrderInfo | Clear an Order&#39;s merchant information
[**getOrderChangeReportingV3**](MarketplacesOrdersV3OrderApi.md#getOrderChangeReportingV3) | **GET** /orders/v3/{marketplaceTechnicalCode}/{accountId}/{beezUPOrderId}/history/{orderChangeExecutionUUID} | Get the order change reporting
[**getOrderHistoryV3**](MarketplacesOrdersV3OrderApi.md#getOrderHistoryV3) | **GET** /orders/v3/{marketplaceTechnicalCode}/{accountId}/{beezUPOrderId}/history | Get an Order&#39;s harvest and change history
[**getOrderV3**](MarketplacesOrdersV3OrderApi.md#getOrderV3) | **GET** /orders/v3/{marketplaceTechnicalCode}/{accountId}/{beezUPOrderId} | Get full Order and Order Item(s) properties
[**harvestAccount**](MarketplacesOrdersV3OrderApi.md#harvestAccount) | **POST** /orders/v3/{marketplaceTechnicalCode}/{accountId}/harvest | Send harvest request for an Account
[**harvestOrderV3**](MarketplacesOrdersV3OrderApi.md#harvestOrderV3) | **POST** /orders/v3/{marketplaceTechnicalCode}/{accountId}/{beezUPOrderId}/harvest | Send harvest request for a single Order
[**headOrderV3**](MarketplacesOrdersV3OrderApi.md#headOrderV3) | **HEAD** /orders/v3/{marketplaceTechnicalCode}/{accountId}/{beezUPOrderId} | Get the meta information about the order (ETag, Last-Modified)
[**setMerchantOrderInfoV3**](MarketplacesOrdersV3OrderApi.md#setMerchantOrderInfoV3) | **POST** /orders/v3/{marketplaceTechnicalCode}/{accountId}/{beezUPOrderId}/setMerchantOrderInfo | Set an Order&#39;s merchant information



## changeOrderV3

> changeOrderV3(marketplaceTechnicalCode, accountId, beezUPOrderId, changeOrderType, userName, opts)

Change your marketplace Order Information (accept, ship, etc.)

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersV3OrderApi();
let marketplaceTechnicalCode = "Amazon"; // String | The marketplace technical code
let accountId = 1001; // Number | 
let beezUPOrderId = "00000000000000000000000000000000000000000000000"; // String | The BeezUP Order identifier
let changeOrderType = "changeOrderType_example"; // String | The Order change type
let userName = "userName_example"; // String | Sometimes the user in the e-commerce application is not the same as user associated with the current subscription key. We recommend providing your application's user login.
let opts = {
  'testMode': false, // Boolean | If true, the operation will be not be sent to marketplace. But the validation will be taken in account.
  'requestBody': {key: "null"} // {String: String} | 
};
apiInstance.changeOrderV3(marketplaceTechnicalCode, accountId, beezUPOrderId, changeOrderType, userName, opts, (error, data, response) => {
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
 **testMode** | **Boolean**| If true, the operation will be not be sent to marketplace. But the validation will be taken in account. | [optional] [default to false]
 **requestBody** | [**{String: String}**](String.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## clearMerchantOrderInfoV3

> clearMerchantOrderInfoV3(marketplaceTechnicalCode, accountId, beezUPOrderId, opts)

Clear an Order&#39;s merchant information

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersV3OrderApi();
let marketplaceTechnicalCode = "Amazon"; // String | The marketplace technical code
let accountId = 1001; // Number | 
let beezUPOrderId = "00000000000000000000000000000000000000000000000"; // String | The BeezUP Order identifier
let opts = {
  'testMode': false // Boolean | If true, the operation will be not be sent to marketplace. But the validation will be taken in account.
};
apiInstance.clearMerchantOrderInfoV3(marketplaceTechnicalCode, accountId, beezUPOrderId, opts, (error, data, response) => {
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
 **testMode** | **Boolean**| If true, the operation will be not be sent to marketplace. But the validation will be taken in account. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrderChangeReportingV3

> ChangeOrderReporting getOrderChangeReportingV3(marketplaceTechnicalCode, accountId, beezUPOrderId, orderChangeExecutionUUID)

Get the order change reporting

This operation will help you to know the status of your order change operation

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersV3OrderApi();
let marketplaceTechnicalCode = "Amazon"; // String | The marketplace technical code
let accountId = 1001; // Number | 
let beezUPOrderId = "00000000000000000000000000000000000000000000000"; // String | The BeezUP Order identifier
let orderChangeExecutionUUID = "orderChangeExecutionUUID_example"; // String | The order change execution id
apiInstance.getOrderChangeReportingV3(marketplaceTechnicalCode, accountId, beezUPOrderId, orderChangeExecutionUUID, (error, data, response) => {
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
 **orderChangeExecutionUUID** | **String**| The order change execution id | 

### Return type

[**ChangeOrderReporting**](ChangeOrderReporting.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrderHistoryV3

> OrderHistory getOrderHistoryV3(marketplaceTechnicalCode, accountId, beezUPOrderId)

Get an Order&#39;s harvest and change history

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersV3OrderApi();
let marketplaceTechnicalCode = "Amazon"; // String | The marketplace technical code
let accountId = 1001; // Number | 
let beezUPOrderId = "00000000000000000000000000000000000000000000000"; // String | The BeezUP Order identifier
apiInstance.getOrderHistoryV3(marketplaceTechnicalCode, accountId, beezUPOrderId, (error, data, response) => {
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

### Return type

[**OrderHistory**](OrderHistory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrderV3

> OrderWithLinks getOrderV3(marketplaceTechnicalCode, accountId, beezUPOrderId, opts)

Get full Order and Order Item(s) properties

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersV3OrderApi();
let marketplaceTechnicalCode = "Amazon"; // String | The marketplace technical code
let accountId = 1001; // Number | 
let beezUPOrderId = "00000000000000000000000000000000000000000000000"; // String | The BeezUP Order identifier
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
};
apiInstance.getOrderV3(marketplaceTechnicalCode, accountId, beezUPOrderId, opts, (error, data, response) => {
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

[**OrderWithLinks**](OrderWithLinks.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## harvestAccount

> harvestAccount(marketplaceTechnicalCode, accountId, opts)

Send harvest request for an Account

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersV3OrderApi();
let marketplaceTechnicalCode = "Amazon"; // String | The marketplace technical code
let accountId = 1001; // Number | 
let opts = {
  'marketplaceOrderId': "marketplaceOrderId_example", // String | 
  'beezUPOrderId': "beezUPOrderId_example" // String | 
};
apiInstance.harvestAccount(marketplaceTechnicalCode, accountId, opts, (error, data, response) => {
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
 **marketplaceOrderId** | **String**|  | [optional] 
 **beezUPOrderId** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## harvestOrderV3

> harvestOrderV3(marketplaceTechnicalCode, accountId, beezUPOrderId)

Send harvest request for a single Order

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersV3OrderApi();
let marketplaceTechnicalCode = "Amazon"; // String | The marketplace technical code
let accountId = 1001; // Number | 
let beezUPOrderId = "00000000000000000000000000000000000000000000000"; // String | The BeezUP Order identifier
apiInstance.harvestOrderV3(marketplaceTechnicalCode, accountId, beezUPOrderId, (error, data, response) => {
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


## headOrderV3

> headOrderV3(marketplaceTechnicalCode, accountId, beezUPOrderId, opts)

Get the meta information about the order (ETag, Last-Modified)

The purpose of this operation is to reduce the bandwith usage by getting just the meta information about the order (ETag, Last-Modified) with the body. This could be useful 

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersV3OrderApi();
let marketplaceTechnicalCode = "Amazon"; // String | The marketplace technical code
let accountId = 1001; // Number | 
let beezUPOrderId = "00000000000000000000000000000000000000000000000"; // String | The BeezUP Order identifier
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
};
apiInstance.headOrderV3(marketplaceTechnicalCode, accountId, beezUPOrderId, opts, (error, data, response) => {
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


## setMerchantOrderInfoV3

> setMerchantOrderInfoV3(marketplaceTechnicalCode, accountId, beezUPOrderId, setMerchantOrderInfoRequest, opts)

Set an Order&#39;s merchant information

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersV3OrderApi();
let marketplaceTechnicalCode = "Amazon"; // String | The marketplace technical code
let accountId = 1001; // Number | 
let beezUPOrderId = "00000000000000000000000000000000000000000000000"; // String | The BeezUP Order identifier
let setMerchantOrderInfoRequest = new BeezUpMerchantApi.SetMerchantOrderInfoRequest(); // SetMerchantOrderInfoRequest | 
let opts = {
  'testMode': false // Boolean | If true, the operation will be not be sent to marketplace. But the validation will be taken in account.
};
apiInstance.setMerchantOrderInfoV3(marketplaceTechnicalCode, accountId, beezUPOrderId, setMerchantOrderInfoRequest, opts, (error, data, response) => {
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
 **testMode** | **Boolean**| If true, the operation will be not be sent to marketplace. But the validation will be taken in account. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

