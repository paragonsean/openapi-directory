# BillsApi.StagesApi

All URIs are relative to *https://bills-api.parliament.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1StagesGet**](StagesApi.md#apiV1StagesGet) | **GET** /api/v1/Stages | Returns a list of Bill stages.



## apiV1StagesGet

> StageReferenceSearchResult apiV1StagesGet(opts)

Returns a list of Bill stages.

### Example

```javascript
import BillsApi from 'bills_api';

let apiInstance = new BillsApi.StagesApi();
let opts = {
  'skip': 56, // Number | 
  'take': 56 // Number | 
};
apiInstance.apiV1StagesGet(opts, (error, data, response) => {
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
 **skip** | **Number**|  | [optional] 
 **take** | **Number**|  | [optional] 

### Return type

[**StageReferenceSearchResult**](StageReferenceSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

