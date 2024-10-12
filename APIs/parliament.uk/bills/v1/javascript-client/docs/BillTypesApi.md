# BillsApi.BillTypesApi

All URIs are relative to *https://bills-api.parliament.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1BillTypesGet**](BillTypesApi.md#apiV1BillTypesGet) | **GET** /api/v1/BillTypes | Returns a list of Bill types.



## apiV1BillTypesGet

> BillTypeSearchResult apiV1BillTypesGet(opts)

Returns a list of Bill types.

### Example

```javascript
import BillsApi from 'bills_api';

let apiInstance = new BillsApi.BillTypesApi();
let opts = {
  'category': new BillsApi.BillTypeCategory(), // BillTypeCategory | 
  'skip': 56, // Number | 
  'take': 56 // Number | 
};
apiInstance.apiV1BillTypesGet(opts, (error, data, response) => {
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
 **category** | [**BillTypeCategory**](.md)|  | [optional] 
 **skip** | **Number**|  | [optional] 
 **take** | **Number**|  | [optional] 

### Return type

[**BillTypeSearchResult**](BillTypeSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

