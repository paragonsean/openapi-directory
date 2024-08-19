# FulfillmentComApiv2.InventoryApi

All URIs are relative to *https://api.fulfillment.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getInventory**](InventoryApi.md#getInventory) | **GET** /inventory | List of Item Inventories



## getInventory

> ItemInventoryArrayV2 getInventory(opts)

List of Item Inventories

Retrieve inventory for one or more items. This API requires elevated permissions, please speak to your success manager.

### Example

```javascript
import FulfillmentComApiv2 from 'fulfillment_com_apiv2';
let defaultClient = FulfillmentComApiv2.ApiClient.instance;
// Configure OAuth2 access token for authorization: fdcAuth
let fdcAuth = defaultClient.authentications['fdcAuth'];
fdcAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: fdcAuth
let fdcAuth = defaultClient.authentications['fdcAuth'];
fdcAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FulfillmentComApiv2.InventoryApi();
let opts = {
  'page': 1, // Number | A multiplier of the number of items (limit parameter) to skip before returning results
  'limit': 80, // Number | The numbers of items to return
  'merchantIds': [null], // [Number] | A CSV of merchant id, '123' or '1,2,3'
  'warehouseIds': [null], // [Number] | A CSV of warehouse id, '123' or '1,2,3'
  'externalSkuNames': ["null"] // [String] | A CSV of sku reference names, 'skuName1' or 'skuName1,skuName2,skuName3'
};
apiInstance.getInventory(opts, (error, data, response) => {
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
 **page** | **Number**| A multiplier of the number of items (limit parameter) to skip before returning results | [optional] [default to 1]
 **limit** | **Number**| The numbers of items to return | [optional] [default to 80]
 **merchantIds** | [**[Number]**](Number.md)| A CSV of merchant id, &#39;123&#39; or &#39;1,2,3&#39; | [optional] 
 **warehouseIds** | [**[Number]**](Number.md)| A CSV of warehouse id, &#39;123&#39; or &#39;1,2,3&#39; | [optional] 
 **externalSkuNames** | [**[String]**](String.md)| A CSV of sku reference names, &#39;skuName1&#39; or &#39;skuName1,skuName2,skuName3&#39; | [optional] 

### Return type

[**ItemInventoryArrayV2**](ItemInventoryArrayV2.md)

### Authorization

[fdcAuth](../README.md#fdcAuth), [fdcAuth](../README.md#fdcAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

