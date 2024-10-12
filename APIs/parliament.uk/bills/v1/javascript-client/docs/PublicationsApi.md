# BillsApi.PublicationsApi

All URIs are relative to *https://bills-api.parliament.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1BillsBillIdStagesStageIdPublicationsGet**](PublicationsApi.md#apiV1BillsBillIdStagesStageIdPublicationsGet) | **GET** /api/v1/Bills/{billId}/Stages/{stageId}/Publications | Return a list of Bill stage publications.
[**getBillPublication**](PublicationsApi.md#getBillPublication) | **GET** /api/v1/Bills/{billId}/Publications | Return a list of Bill publications.



## apiV1BillsBillIdStagesStageIdPublicationsGet

> BillStagePublicationList apiV1BillsBillIdStagesStageIdPublicationsGet(billId, stageId)

Return a list of Bill stage publications.

### Example

```javascript
import BillsApi from 'bills_api';

let apiInstance = new BillsApi.PublicationsApi();
let billId = 56; // Number | 
let stageId = 56; // Number | 
apiInstance.apiV1BillsBillIdStagesStageIdPublicationsGet(billId, stageId, (error, data, response) => {
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
 **billId** | **Number**|  | 
 **stageId** | **Number**|  | 

### Return type

[**BillStagePublicationList**](BillStagePublicationList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## getBillPublication

> BillPublicationList getBillPublication(billId)

Return a list of Bill publications.

### Example

```javascript
import BillsApi from 'bills_api';

let apiInstance = new BillsApi.PublicationsApi();
let billId = 56; // Number | Publications relating to Bill with Bill ID specified
apiInstance.getBillPublication(billId, (error, data, response) => {
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
 **billId** | **Number**| Publications relating to Bill with Bill ID specified | 

### Return type

[**BillPublicationList**](BillPublicationList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

