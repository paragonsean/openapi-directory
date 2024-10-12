# SalesLoftPlatform.TagsApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2TagsJsonGet**](TagsApi.md#v2TagsJsonGet) | **GET** /v2/tags.json | List team tags



## v2TagsJsonGet

> [Tag] v2TagsJsonGet(opts)

List team tags

Fetches a list of the tags used for a team. The records can be filtered, paged, and sorted according to the respective parameters.  Tags can be applied to mulitple resource types. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.TagsApi();
let opts = {
  'search': "search_example", // String | Filters tags by name
  'ids': [null], // [Number] | Filters tags by their IDs
  'sortBy': "sortBy_example", // String | Key to sort on, must be one of: name. Defaults to name
  'sortDirection': "sortDirection_example", // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
  'perPage': 56, // Number | How many records to show per page in the range [1, 100]. Defaults to 25
  'page': 56, // Number | The current page to fetch results from. Defaults to 1
  'includePagingCounts': true, // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
  'limitPagingCounts': true // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
};
apiInstance.v2TagsJsonGet(opts, (error, data, response) => {
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
 **search** | **String**| Filters tags by name | [optional] 
 **ids** | [**[Number]**](Number.md)| Filters tags by their IDs | [optional] 
 **sortBy** | **String**| Key to sort on, must be one of: name. Defaults to name | [optional] 
 **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] 
 **perPage** | **Number**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] 
 **page** | **Number**| The current page to fetch results from. Defaults to 1 | [optional] 
 **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] 
 **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] 

### Return type

[**[Tag]**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

