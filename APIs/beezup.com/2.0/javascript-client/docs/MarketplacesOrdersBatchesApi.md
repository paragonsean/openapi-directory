# BeezUpMerchantApi.MarketplacesOrdersBatchesApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**changeOrderList**](MarketplacesOrdersBatchesApi.md#changeOrderList) | **POST** /v2/user/marketplaces/orders/batches/changeOrders/{changeOrderType} | [DEPRECATED] Send a batch of operations to change your marketplace Order information: accept, ship, etc.  (max 100 items per call)
[**clearMerchantOrderInfoList**](MarketplacesOrdersBatchesApi.md#clearMerchantOrderInfoList) | **POST** /v2/user/marketplaces/orders/batches/clearMerchantOrderInfos | [DEPRECATED] Send a batch of operations to clear an Order&#39;s merchant information (max 100 items per call)
[**setMerchantOrderInfoList**](MarketplacesOrdersBatchesApi.md#setMerchantOrderInfoList) | **POST** /v2/user/marketplaces/orders/batches/setMerchantOrderInfos | [DEPRECATED] Send a batch of operations to set an Order&#39;s merchant information  (max 100 items per call)



## changeOrderList

> BatchOrderOperationResponse changeOrderList(changeOrderType, userName, changeOrderListRequest, opts)

[DEPRECATED] Send a batch of operations to change your marketplace Order information: accept, ship, etc.  (max 100 items per call)

The purpose of this operation is to reduce the amount of request to the API.  Max 100 items per call. 

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersBatchesApi();
let changeOrderType = "changeOrderType_example"; // String | The Order change type
let userName = "userName_example"; // String | Sometimes the user in the e-commerce application is not the same as user associated with the current subscription key. We recommend providing your application's user login.
let changeOrderListRequest = new BeezUpMerchantApi.ChangeOrderListRequest(); // ChangeOrderListRequest | 
let opts = {
  'testMode': false // Boolean | If true, the operation will be not be sent to marketplace. But the validation will be taken in account.
};
apiInstance.changeOrderList(changeOrderType, userName, changeOrderListRequest, opts, (error, data, response) => {
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
 **changeOrderType** | **String**| The Order change type | 
 **userName** | **String**| Sometimes the user in the e-commerce application is not the same as user associated with the current subscription key. We recommend providing your application&#39;s user login. | 
 **changeOrderListRequest** | [**ChangeOrderListRequest**](ChangeOrderListRequest.md)|  | 
 **testMode** | **Boolean**| If true, the operation will be not be sent to marketplace. But the validation will be taken in account. | [optional] [default to false]

### Return type

[**BatchOrderOperationResponse**](BatchOrderOperationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## clearMerchantOrderInfoList

> BatchOrderOperationResponse clearMerchantOrderInfoList(clearMerchantOrderInfoListRequest)

[DEPRECATED] Send a batch of operations to clear an Order&#39;s merchant information (max 100 items per call)

The purpose of this operation is to reduce the amount of request to the API.

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersBatchesApi();
let clearMerchantOrderInfoListRequest = new BeezUpMerchantApi.ClearMerchantOrderInfoListRequest(); // ClearMerchantOrderInfoListRequest | 
apiInstance.clearMerchantOrderInfoList(clearMerchantOrderInfoListRequest, (error, data, response) => {
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
 **clearMerchantOrderInfoListRequest** | [**ClearMerchantOrderInfoListRequest**](ClearMerchantOrderInfoListRequest.md)|  | 

### Return type

[**BatchOrderOperationResponse**](BatchOrderOperationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setMerchantOrderInfoList

> BatchOrderOperationResponse setMerchantOrderInfoList(setMerchantOrderInfoListRequest)

[DEPRECATED] Send a batch of operations to set an Order&#39;s merchant information  (max 100 items per call)

The purpose of this operation is to reduce the amount of request to the API.

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersBatchesApi();
let setMerchantOrderInfoListRequest = new BeezUpMerchantApi.SetMerchantOrderInfoListRequest(); // SetMerchantOrderInfoListRequest | 
apiInstance.setMerchantOrderInfoList(setMerchantOrderInfoListRequest, (error, data, response) => {
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
 **setMerchantOrderInfoListRequest** | [**SetMerchantOrderInfoListRequest**](SetMerchantOrderInfoListRequest.md)|  | 

### Return type

[**BatchOrderOperationResponse**](BatchOrderOperationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

