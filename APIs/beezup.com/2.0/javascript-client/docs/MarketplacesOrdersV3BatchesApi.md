# BeezUpMerchantApi.MarketplacesOrdersV3BatchesApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**changeOrderListV2**](MarketplacesOrdersV3BatchesApi.md#changeOrderListV2) | **POST** /orders/v3/batches/changeOrders/{changeOrderType} | Send a batch of operations to change your marketplace Order information: accept, ship, etc.  (max 100 items per call)
[**changeOrderListV3**](MarketplacesOrdersV3BatchesApi.md#changeOrderListV3) | **POST** /orders/v3/batches/changeOrders | Send a batch of operations to change your marketplace Order information: accept, ship, etc.  (max 100 items per call)
[**clearMerchantOrderInfoListV3**](MarketplacesOrdersV3BatchesApi.md#clearMerchantOrderInfoListV3) | **POST** /orders/v3/batches/clearMerchantOrderInfos | Send a batch of operations to clear an Order&#39;s merchant information (max 100 items per call)
[**setMerchantOrderInfoListV3**](MarketplacesOrdersV3BatchesApi.md#setMerchantOrderInfoListV3) | **POST** /orders/v3/batches/setMerchantOrderInfos | Send a batch of operations to set an Order&#39;s merchant information  (max 100 items per call)



## changeOrderListV2

> BatchOrderOperationResponse changeOrderListV2(userName, changeOrderType, changeOrderListRequestV2, opts)

Send a batch of operations to change your marketplace Order information: accept, ship, etc.  (max 100 items per call)

The purpose of this operation is to reduce the amount of request to the API.  Max 100 items per call. 

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersV3BatchesApi();
let userName = "userName_example"; // String | Sometimes the user in the e-commerce application is not the same as user associated with the current subscription key. We recommend providing your application's user login.
let changeOrderType = "changeOrderType_example"; // String | The Order change type
let changeOrderListRequestV2 = new BeezUpMerchantApi.ChangeOrderListRequestV2(); // ChangeOrderListRequestV2 | 
let opts = {
  'testMode': false // Boolean | If true, the operation will be not be sent to marketplace. But the validation will be taken in account.
};
apiInstance.changeOrderListV2(userName, changeOrderType, changeOrderListRequestV2, opts, (error, data, response) => {
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
 **userName** | **String**| Sometimes the user in the e-commerce application is not the same as user associated with the current subscription key. We recommend providing your application&#39;s user login. | 
 **changeOrderType** | **String**| The Order change type | 
 **changeOrderListRequestV2** | [**ChangeOrderListRequestV2**](ChangeOrderListRequestV2.md)|  | 
 **testMode** | **Boolean**| If true, the operation will be not be sent to marketplace. But the validation will be taken in account. | [optional] [default to false]

### Return type

[**BatchOrderOperationResponse**](BatchOrderOperationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## changeOrderListV3

> BatchOrderOperationResponse changeOrderListV3(userName, changeOrderListRequest, opts)

Send a batch of operations to change your marketplace Order information: accept, ship, etc.  (max 100 items per call)

The purpose of this operation is to reduce the amount of request to the API.  Max 100 items per call. 

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersV3BatchesApi();
let userName = "userName_example"; // String | Sometimes the user in the e-commerce application is not the same as user associated with the current subscription key. We recommend providing your application's user login.
let changeOrderListRequest = new BeezUpMerchantApi.ChangeOrderListRequest(); // ChangeOrderListRequest | 
let opts = {
  'testMode': false // Boolean | If true, the operation will be not be sent to marketplace. But the validation will be taken in account.
};
apiInstance.changeOrderListV3(userName, changeOrderListRequest, opts, (error, data, response) => {
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


## clearMerchantOrderInfoListV3

> BatchOrderOperationResponse clearMerchantOrderInfoListV3(clearMerchantOrderInfoListRequest, opts)

Send a batch of operations to clear an Order&#39;s merchant information (max 100 items per call)

The purpose of this operation is to reduce the amount of request to the API.

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersV3BatchesApi();
let clearMerchantOrderInfoListRequest = new BeezUpMerchantApi.ClearMerchantOrderInfoListRequest(); // ClearMerchantOrderInfoListRequest | 
let opts = {
  'testMode': false // Boolean | If true, the operation will be not be sent to marketplace. But the validation will be taken in account.
};
apiInstance.clearMerchantOrderInfoListV3(clearMerchantOrderInfoListRequest, opts, (error, data, response) => {
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
 **testMode** | **Boolean**| If true, the operation will be not be sent to marketplace. But the validation will be taken in account. | [optional] [default to false]

### Return type

[**BatchOrderOperationResponse**](BatchOrderOperationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setMerchantOrderInfoListV3

> BatchOrderOperationResponse setMerchantOrderInfoListV3(setMerchantOrderInfoListRequest, opts)

Send a batch of operations to set an Order&#39;s merchant information  (max 100 items per call)

The purpose of this operation is to reduce the amount of request to the API.

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersV3BatchesApi();
let setMerchantOrderInfoListRequest = new BeezUpMerchantApi.SetMerchantOrderInfoListRequest(); // SetMerchantOrderInfoListRequest | 
let opts = {
  'testMode': false // Boolean | If true, the operation will be not be sent to marketplace. But the validation will be taken in account.
};
apiInstance.setMerchantOrderInfoListV3(setMerchantOrderInfoListRequest, opts, (error, data, response) => {
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
 **testMode** | **Boolean**| If true, the operation will be not be sent to marketplace. But the validation will be taken in account. | [optional] [default to false]

### Return type

[**BatchOrderOperationResponse**](BatchOrderOperationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

