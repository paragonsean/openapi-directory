# BillsApi.PublicationTypesApi

All URIs are relative to *https://bills-api.parliament.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1PublicationTypesGet**](PublicationTypesApi.md#apiV1PublicationTypesGet) | **GET** /api/v1/PublicationTypes | Returns a list of publication types.



## apiV1PublicationTypesGet

> PublicationTypeSearchResult apiV1PublicationTypesGet(opts)

Returns a list of publication types.

### Example

```javascript
import BillsApi from 'bills_api';

let apiInstance = new BillsApi.PublicationTypesApi();
let opts = {
  'skip': 56, // Number | 
  'take': 56 // Number | 
};
apiInstance.apiV1PublicationTypesGet(opts, (error, data, response) => {
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

[**PublicationTypeSearchResult**](PublicationTypeSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

