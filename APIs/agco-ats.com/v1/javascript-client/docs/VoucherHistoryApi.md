# AgcoApi.VoucherHistoryApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**voucherHistoryGetVoucherHistory**](VoucherHistoryApi.md#voucherHistoryGetVoucherHistory) | **GET** /api/v2/VoucherHistory | Gets voucher history data



## voucherHistoryGetVoucherHistory

> APIPagedResponseDealerDBModelsVoucherHistory voucherHistoryGetVoucherHistory(opts)

Gets voucher history data

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.VoucherHistoryApi();
let opts = {
  'voucherCode': "voucherCode_example", // String | Optional. Filter history data by Voucher Code.
  'changedBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional. Filter history data where changes occured before provided date.
  'changedAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional. Filter history data where changes occured after provided date.
  'limit': 56, // Number | Optional. The page limit. The default page limit is 10.
  'offset': 56 // Number | Optional. The page offset. The default page offset is 0.
};
apiInstance.voucherHistoryGetVoucherHistory(opts, (error, data, response) => {
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
 **voucherCode** | **String**| Optional. Filter history data by Voucher Code. | [optional] 
 **changedBefore** | **Date**| Optional. Filter history data where changes occured before provided date. | [optional] 
 **changedAfter** | **Date**| Optional. Filter history data where changes occured after provided date. | [optional] 
 **limit** | **Number**| Optional. The page limit. The default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset. The default page offset is 0. | [optional] 

### Return type

[**APIPagedResponseDealerDBModelsVoucherHistory**](APIPagedResponseDealerDBModelsVoucherHistory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

