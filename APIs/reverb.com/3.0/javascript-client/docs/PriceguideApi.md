# Reverb.PriceguideApi

All URIs are relative to *https://api.reverb.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**priceguideIdTransactionsSummaryGet**](PriceguideApi.md#priceguideIdTransactionsSummaryGet) | **GET** /priceguide/{id}/transactions/summary | Get a summary of transactions for a given price guide



## priceguideIdTransactionsSummaryGet

> priceguideIdTransactionsSummaryGet(id, opts)

Get a summary of transactions for a given price guide

Get a summary of transactions for a given price guide

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.PriceguideApi();
let id = "id_example"; // String | 
let opts = {
  'numberOfMonths': 3, // Number | 
  'condition': "'used'" // String | 
};
apiInstance.priceguideIdTransactionsSummaryGet(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **numberOfMonths** | **Number**|  | [optional] [default to 3]
 **condition** | **String**|  | [optional] [default to &#39;used&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

