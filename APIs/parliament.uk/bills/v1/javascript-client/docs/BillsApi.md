# BillsApi.BillsApi

All URIs are relative to *https://bills-api.parliament.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1BillsBillIdStagesGet**](BillsApi.md#apiV1BillsBillIdStagesGet) | **GET** /api/v1/Bills/{billId}/Stages | Returns all Bill stages.
[**getBill**](BillsApi.md#getBill) | **GET** /api/v1/Bills/{billId} | Return a Bill.
[**getBillStageDetails**](BillsApi.md#getBillStageDetails) | **GET** /api/v1/Bills/{billId}/Stages/{billStageId} | Returns a Bill stage.
[**getBills**](BillsApi.md#getBills) | **GET** /api/v1/Bills | Returns a list of Bills.



## apiV1BillsBillIdStagesGet

> StageSummarySearchResult apiV1BillsBillIdStagesGet(billId, opts)

Returns all Bill stages.

### Example

```javascript
import BillsApi from 'bills_api';

let apiInstance = new BillsApi.BillsApi();
let billId = 56; // Number | Stages relating to a Bill with Bill ID specified
let opts = {
  'skip': 56, // Number | 
  'take': 56 // Number | 
};
apiInstance.apiV1BillsBillIdStagesGet(billId, opts, (error, data, response) => {
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
 **billId** | **Number**| Stages relating to a Bill with Bill ID specified | 
 **skip** | **Number**|  | [optional] 
 **take** | **Number**|  | [optional] 

### Return type

[**StageSummarySearchResult**](StageSummarySearchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## getBill

> Bill getBill(billId)

Return a Bill.

### Example

```javascript
import BillsApi from 'bills_api';

let apiInstance = new BillsApi.BillsApi();
let billId = 56; // Number | Bill with ID specified
apiInstance.getBill(billId, (error, data, response) => {
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
 **billId** | **Number**| Bill with ID specified | 

### Return type

[**Bill**](Bill.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## getBillStageDetails

> BillStageDetails getBillStageDetails(billId, billStageId)

Returns a Bill stage.

### Example

```javascript
import BillsApi from 'bills_api';

let apiInstance = new BillsApi.BillsApi();
let billId = 56; // Number | Bill stage relating to Bill with Bill ID specified
let billStageId = 56; // Number | Bill stage with ID specified
apiInstance.getBillStageDetails(billId, billStageId, (error, data, response) => {
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
 **billId** | **Number**| Bill stage relating to Bill with Bill ID specified | 
 **billStageId** | **Number**| Bill stage with ID specified | 

### Return type

[**BillStageDetails**](BillStageDetails.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## getBills

> BillSummarySearchResult getBills(opts)

Returns a list of Bills.

### Example

```javascript
import BillsApi from 'bills_api';

let apiInstance = new BillsApi.BillsApi();
let opts = {
  'searchTerm': "searchTerm_example", // String | 
  'session': 56, // Number | 
  'currentHouse': new BillsApi.House(), // House | 
  'originatingHouse': new BillsApi.OriginatingHouse(), // OriginatingHouse | 
  'memberId': 56, // Number | 
  'departmentId': 56, // Number | 
  'billStage': [null], // [Number] | 
  'billStagesExcluded': [null], // [Number] | 
  'isDefeated': true, // Boolean | 
  'isWithdrawn': true, // Boolean | 
  'billType': [null], // [Number] | 
  'sortOrder': new BillsApi.BillSortOrder(), // BillSortOrder | 
  'billIds': [null], // [Number] | 
  'skip': 56, // Number | 
  'take': 56 // Number | 
};
apiInstance.getBills(opts, (error, data, response) => {
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
 **searchTerm** | **String**|  | [optional] 
 **session** | **Number**|  | [optional] 
 **currentHouse** | [**House**](.md)|  | [optional] 
 **originatingHouse** | [**OriginatingHouse**](.md)|  | [optional] 
 **memberId** | **Number**|  | [optional] 
 **departmentId** | **Number**|  | [optional] 
 **billStage** | [**[Number]**](Number.md)|  | [optional] 
 **billStagesExcluded** | [**[Number]**](Number.md)|  | [optional] 
 **isDefeated** | **Boolean**|  | [optional] 
 **isWithdrawn** | **Boolean**|  | [optional] 
 **billType** | [**[Number]**](Number.md)|  | [optional] 
 **sortOrder** | [**BillSortOrder**](.md)|  | [optional] 
 **billIds** | [**[Number]**](Number.md)|  | [optional] 
 **skip** | **Number**|  | [optional] 
 **take** | **Number**|  | [optional] 

### Return type

[**BillSummarySearchResult**](BillSummarySearchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

