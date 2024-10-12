# SalesLoftPlatform.CallSentimentsApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2CallSentimentsJsonGet**](CallSentimentsApi.md#v2CallSentimentsJsonGet) | **GET** /v2/call_sentiments.json | List call sentiments



## v2CallSentimentsJsonGet

> [CallSentiment] v2CallSentimentsJsonGet(opts)

List call sentiments

Fetches multiple call sentiment records. The records can be sorted according to the respective parameters. Call sentiments must be configured in application. This will change in the future, but please contact us if you have a pressing use case. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.CallSentimentsApi();
let opts = {
  'name': "name_example", // String | Filters call sentiments by name
  'sortBy': "sortBy_example", // String | Key to sort on, must be one of: name, updated_at. Defaults to name
  'sortDirection': "sortDirection_example", // String | Direction to sort in, must be one of: ASC, DESC. Defaults to ASC
  'perPage': 56, // Number | How many records to show per page in the range [1, 100]. Defaults to 25
  'page': 56, // Number | The current page to fetch results from. Defaults to 1
  'includePagingCounts': true, // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
  'limitPagingCounts': true // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
};
apiInstance.v2CallSentimentsJsonGet(opts, (error, data, response) => {
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
 **name** | **String**| Filters call sentiments by name | [optional] 
 **sortBy** | **String**| Key to sort on, must be one of: name, updated_at. Defaults to name | [optional] 
 **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to ASC | [optional] 
 **perPage** | **Number**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] 
 **page** | **Number**| The current page to fetch results from. Defaults to 1 | [optional] 
 **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] 
 **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] 

### Return type

[**[CallSentiment]**](CallSentiment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

