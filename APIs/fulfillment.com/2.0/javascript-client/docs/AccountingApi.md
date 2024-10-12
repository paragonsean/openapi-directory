# FulfillmentComApiv2.AccountingApi

All URIs are relative to *https://api.fulfillment.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAccounting**](AccountingApi.md#getAccounting) | **GET** /accounting | List Order Accounting



## getAccounting

> AccountingArrayV2 getAccounting(fromDate, toDate, hydrate, opts)

List Order Accounting

Retrieves accounting activity during the queried timespan.

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

let apiInstance = new FulfillmentComApiv2.AccountingApi();
let fromDate = "fromDate_example"; // String | Orders invoice date. Date-time in ISO 8601 format for selecting orders after, or at, the specified time
let toDate = "toDate_example"; // String | Orders invoice date. Date-time in ISO 8601 format for selecting orders before, or at, the specified time
let hydrate = ["null"]; // [String] | Adds additional information to the response, uses a CSV format for multiple values.
let opts = {
  'page': 1, // Number | A multiplier of the number of items (limit parameter) to skip before returning results
  'limit': 80, // Number | The numbers of items to return
  'warehouseIds': [null], // [Number] | A CSV of warehouse id, '123' or '1,2,3'
  'orderIds': [null] // [Number] | A CSV of FDC order id, '123' or '1,2,3'
};
apiInstance.getAccounting(fromDate, toDate, hydrate, opts, (error, data, response) => {
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
 **fromDate** | **String**| Orders invoice date. Date-time in ISO 8601 format for selecting orders after, or at, the specified time | 
 **toDate** | **String**| Orders invoice date. Date-time in ISO 8601 format for selecting orders before, or at, the specified time | 
 **hydrate** | [**[String]**](String.md)| Adds additional information to the response, uses a CSV format for multiple values. | 
 **page** | **Number**| A multiplier of the number of items (limit parameter) to skip before returning results | [optional] [default to 1]
 **limit** | **Number**| The numbers of items to return | [optional] [default to 80]
 **warehouseIds** | [**[Number]**](Number.md)| A CSV of warehouse id, &#39;123&#39; or &#39;1,2,3&#39; | [optional] 
 **orderIds** | [**[Number]**](Number.md)| A CSV of FDC order id, &#39;123&#39; or &#39;1,2,3&#39; | [optional] 

### Return type

[**AccountingArrayV2**](AccountingArrayV2.md)

### Authorization

[fdcAuth](../README.md#fdcAuth), [fdcAuth](../README.md#fdcAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

