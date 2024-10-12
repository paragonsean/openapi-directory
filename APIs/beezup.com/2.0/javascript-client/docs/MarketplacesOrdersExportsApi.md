# BeezUpMerchantApi.MarketplacesOrdersExportsApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exportOrders**](MarketplacesOrdersExportsApi.md#exportOrders) | **POST** /v2/user/marketplaces/orders/exportations | Request a new Order report exportation to be generated
[**getOrderExportations**](MarketplacesOrdersExportsApi.md#getOrderExportations) | **GET** /v2/user/marketplaces/orders/exportations | Get a paginated list of Order report exportations



## exportOrders

> exportOrders(exportOrderListRequest)

Request a new Order report exportation to be generated

A new file will be generated containing a summary of all the Orders matching the requested filter settings.

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersExportsApi();
let exportOrderListRequest = new BeezUpMerchantApi.ExportOrderListRequest(); // ExportOrderListRequest | 
apiInstance.exportOrders(exportOrderListRequest, (error, data, response) => {
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
 **exportOrderListRequest** | [**ExportOrderListRequest**](ExportOrderListRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getOrderExportations

> OrderExportations getOrderExportations(pageNumber, pageSize, storeId, opts)

Get a paginated list of Order report exportations

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersExportsApi();
let pageNumber = 1; // Number | The page number you want to get
let pageSize = 25; // Number | The entry count you want to get
let storeId = "storeId_example"; // String | The store identifier to regroup the order exportations
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
};
apiInstance.getOrderExportations(pageNumber, pageSize, storeId, opts, (error, data, response) => {
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
 **pageNumber** | **Number**| The page number you want to get | 
 **pageSize** | **Number**| The entry count you want to get | 
 **storeId** | **String**| The store identifier to regroup the order exportations | 
 **ifNoneMatch** | **String**| ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  | [optional] 

### Return type

[**OrderExportations**](OrderExportations.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

