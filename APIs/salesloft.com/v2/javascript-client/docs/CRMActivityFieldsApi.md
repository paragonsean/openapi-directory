# SalesLoftPlatform.CRMActivityFieldsApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2CrmActivityFieldsJsonGet**](CRMActivityFieldsApi.md#v2CrmActivityFieldsJsonGet) | **GET** /v2/crm_activity_fields.json | List crm activity fields



## v2CrmActivityFieldsJsonGet

> [CrmActivityField] v2CrmActivityFieldsJsonGet(opts)

List crm activity fields

Fetches multiple crm activity field records. The records can be filtered, paged, and sorted according to the respective parameters. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.CRMActivityFieldsApi();
let opts = {
  'source': "source_example", // String | Return only records with this source
  'sortBy': "sortBy_example", // String | Key to sort on, must be one of: title, updated_at. Defaults to title
  'sortDirection': "sortDirection_example", // String | Direction to sort in, must be one of: ASC, DESC. Defaults to ASC
  'perPage': 56, // Number | How many records to show per page in the range [1, 100]. Defaults to 25
  'page': 56, // Number | The current page to fetch results from. Defaults to 1
  'includePagingCounts': true, // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
  'limitPagingCounts': true // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
};
apiInstance.v2CrmActivityFieldsJsonGet(opts, (error, data, response) => {
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
 **source** | **String**| Return only records with this source | [optional] 
 **sortBy** | **String**| Key to sort on, must be one of: title, updated_at. Defaults to title | [optional] 
 **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to ASC | [optional] 
 **perPage** | **Number**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] 
 **page** | **Number**| The current page to fetch results from. Defaults to 1 | [optional] 
 **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] 
 **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] 

### Return type

[**[CrmActivityField]**](CrmActivityField.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

