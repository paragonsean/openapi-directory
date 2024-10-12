# BillsApi.SittingsApi

All URIs are relative to *https://bills-api.parliament.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSittings**](SittingsApi.md#getSittings) | **GET** /api/v1/Sittings | Returns a list of Sittings.



## getSittings

> BillStageSittingSearchResult getSittings(opts)

Returns a list of Sittings.

### Example

```javascript
import BillsApi from 'bills_api';

let apiInstance = new BillsApi.SittingsApi();
let opts = {
  'house': new BillsApi.House(), // House | 
  'dateFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'dateTo': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'skip': 56, // Number | 
  'take': 56 // Number | 
};
apiInstance.getSittings(opts, (error, data, response) => {
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
 **house** | [**House**](.md)|  | [optional] 
 **dateFrom** | **Date**|  | [optional] 
 **dateTo** | **Date**|  | [optional] 
 **skip** | **Number**|  | [optional] 
 **take** | **Number**|  | [optional] 

### Return type

[**BillStageSittingSearchResult**](BillStageSittingSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

