# SalesLoftPlatform.ActionDetailsCallInstructionsApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2ActionDetailsCallInstructionsIdJsonGet**](ActionDetailsCallInstructionsApi.md#v2ActionDetailsCallInstructionsIdJsonGet) | **GET** /v2/action_details/call_instructions/{id}.json | Fetch a call instructions
[**v2ActionDetailsCallInstructionsJsonGet**](ActionDetailsCallInstructionsApi.md#v2ActionDetailsCallInstructionsJsonGet) | **GET** /v2/action_details/call_instructions.json | List call instructions



## v2ActionDetailsCallInstructionsIdJsonGet

> CallInstruction v2ActionDetailsCallInstructionsIdJsonGet(id)

Fetch a call instructions

Fetches a call instruction, by ID only. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.ActionDetailsCallInstructionsApi();
let id = "id_example"; // String | Call instructions ID
apiInstance.v2ActionDetailsCallInstructionsIdJsonGet(id, (error, data, response) => {
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
 **id** | **String**| Call instructions ID | 

### Return type

[**CallInstruction**](CallInstruction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## v2ActionDetailsCallInstructionsJsonGet

> [CallInstruction] v2ActionDetailsCallInstructionsJsonGet(opts)

List call instructions

Fetches multiple call instruction records. The records can be filtered, paged, and sorted according to the respective parameters. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.ActionDetailsCallInstructionsApi();
let opts = {
  'ids': [null], // [Number] | IDs of call instructions to fetch.
  'sortBy': "sortBy_example", // String | Key to sort on, must be one of: created_at, updated_at. Defaults to updated_at
  'sortDirection': "sortDirection_example", // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
  'perPage': 56, // Number | How many records to show per page in the range [1, 100]. Defaults to 25
  'page': 56, // Number | The current page to fetch results from. Defaults to 1
  'includePagingCounts': true, // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
  'limitPagingCounts': true // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
};
apiInstance.v2ActionDetailsCallInstructionsJsonGet(opts, (error, data, response) => {
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
 **ids** | [**[Number]**](Number.md)| IDs of call instructions to fetch. | [optional] 
 **sortBy** | **String**| Key to sort on, must be one of: created_at, updated_at. Defaults to updated_at | [optional] 
 **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] 
 **perPage** | **Number**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] 
 **page** | **Number**| The current page to fetch results from. Defaults to 1 | [optional] 
 **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] 
 **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] 

### Return type

[**[CallInstruction]**](CallInstruction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

