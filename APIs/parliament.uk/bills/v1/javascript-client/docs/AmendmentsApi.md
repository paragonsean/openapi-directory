# BillsApi.AmendmentsApi

All URIs are relative to *https://bills-api.parliament.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAmendment**](AmendmentsApi.md#getAmendment) | **GET** /api/v1/Bills/{billId}/Stages/{billStageId}/Amendments/{amendmentId} | Returns an amendment.
[**getAmendments**](AmendmentsApi.md#getAmendments) | **GET** /api/v1/Bills/{billId}/Stages/{billStageId}/Amendments | Returns a list of amendments.



## getAmendment

> AmendmentDetail getAmendment(billId, billStageId, amendmentId)

Returns an amendment.

### Example

```javascript
import BillsApi from 'bills_api';

let apiInstance = new BillsApi.AmendmentsApi();
let billId = 56; // Number | Amendment relating to a bill with bill ID specified
let billStageId = 56; // Number | Amendment relating to a bill stage with bill stage ID specified
let amendmentId = 56; // Number | Amendment with amendment ID specified
apiInstance.getAmendment(billId, billStageId, amendmentId, (error, data, response) => {
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
 **billId** | **Number**| Amendment relating to a bill with bill ID specified | 
 **billStageId** | **Number**| Amendment relating to a bill stage with bill stage ID specified | 
 **amendmentId** | **Number**| Amendment with amendment ID specified | 

### Return type

[**AmendmentDetail**](AmendmentDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## getAmendments

> AmendmentSearchItemSearchResult getAmendments(billId, billStageId, opts)

Returns a list of amendments.

### Example

```javascript
import BillsApi from 'bills_api';

let apiInstance = new BillsApi.AmendmentsApi();
let billId = 56; // Number | Amendments relating to a Bill with Bill ID specified
let billStageId = 56; // Number | Amendments relating to a Bill stage with Bill stage ID specified
let opts = {
  'searchTerm': "searchTerm_example", // String | 
  'decision': new BillsApi.Decision(), // Decision | 
  'memberId': 56, // Number | 
  'skip': 56, // Number | 
  'take': 56 // Number | 
};
apiInstance.getAmendments(billId, billStageId, opts, (error, data, response) => {
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
 **billId** | **Number**| Amendments relating to a Bill with Bill ID specified | 
 **billStageId** | **Number**| Amendments relating to a Bill stage with Bill stage ID specified | 
 **searchTerm** | **String**|  | [optional] 
 **decision** | [**Decision**](.md)|  | [optional] 
 **memberId** | **Number**|  | [optional] 
 **skip** | **Number**|  | [optional] 
 **take** | **Number**|  | [optional] 

### Return type

[**AmendmentSearchItemSearchResult**](AmendmentSearchItemSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

