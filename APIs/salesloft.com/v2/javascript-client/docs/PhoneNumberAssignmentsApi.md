# SalesLoftPlatform.PhoneNumberAssignmentsApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2PhoneNumberAssignmentsIdJsonGet**](PhoneNumberAssignmentsApi.md#v2PhoneNumberAssignmentsIdJsonGet) | **GET** /v2/phone_number_assignments/{id}.json | Fetch a phone number assignment
[**v2PhoneNumberAssignmentsJsonGet**](PhoneNumberAssignmentsApi.md#v2PhoneNumberAssignmentsJsonGet) | **GET** /v2/phone_number_assignments.json | List phone number assignments



## v2PhoneNumberAssignmentsIdJsonGet

> PhoneNumberAssignment v2PhoneNumberAssignmentsIdJsonGet(id)

Fetch a phone number assignment

Fetches a phone number assignment, by ID only. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.PhoneNumberAssignmentsApi();
let id = "id_example"; // String | PhoneNumberAssignment ID
apiInstance.v2PhoneNumberAssignmentsIdJsonGet(id, (error, data, response) => {
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
 **id** | **String**| PhoneNumberAssignment ID | 

### Return type

[**PhoneNumberAssignment**](PhoneNumberAssignment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## v2PhoneNumberAssignmentsJsonGet

> [PhoneNumberAssignment] v2PhoneNumberAssignmentsJsonGet(opts)

List phone number assignments

Fetches multiple phone number assignment records. The records can be filtered, paged, and sorted according to the respective parameters. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.PhoneNumberAssignmentsApi();
let opts = {
  'ids': [null], // [Number] | IDs of phone number assignments to fetch
  'sortBy': "sortBy_example", // String | Key to sort on, must be one of: created_at, updated_at. Defaults to updated_at
  'sortDirection': "sortDirection_example", // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
  'perPage': 56, // Number | How many records to show per page in the range [1, 100]. Defaults to 25
  'page': 56, // Number | The current page to fetch results from. Defaults to 1
  'includePagingCounts': true, // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
  'limitPagingCounts': true // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
};
apiInstance.v2PhoneNumberAssignmentsJsonGet(opts, (error, data, response) => {
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
 **ids** | [**[Number]**](Number.md)| IDs of phone number assignments to fetch | [optional] 
 **sortBy** | **String**| Key to sort on, must be one of: created_at, updated_at. Defaults to updated_at | [optional] 
 **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] 
 **perPage** | **Number**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] 
 **page** | **Number**| The current page to fetch results from. Defaults to 1 | [optional] 
 **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] 
 **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] 

### Return type

[**[PhoneNumberAssignment]**](PhoneNumberAssignment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

