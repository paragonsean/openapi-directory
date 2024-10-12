# SalesLoftPlatform.TeamTemplateAttachmentsApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2TeamTemplateAttachmentsJsonGet**](TeamTemplateAttachmentsApi.md#v2TeamTemplateAttachmentsJsonGet) | **GET** /v2/team_template_attachments.json | List team template attachments



## v2TeamTemplateAttachmentsJsonGet

> [TeamTemplateAttachment] v2TeamTemplateAttachmentsJsonGet(opts)

List team template attachments

Fetches multiple team template attachment records. The records can be filtered and paged according to the respective parameters. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.TeamTemplateAttachmentsApi();
let opts = {
  'ids': [null], // [Number] | IDs of team template attachments to fetch. If a record can't be found, that record won't be returned and your request will be successful
  'teamTemplateId': [null], // [Number] | Filters template attachments by team template IDs
  'perPage': 56, // Number | How many records to show per page in the range [1, 100]. Defaults to 25
  'page': 56, // Number | The current page to fetch results from. Defaults to 1
  'includePagingCounts': true, // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
  'limitPagingCounts': true // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
};
apiInstance.v2TeamTemplateAttachmentsJsonGet(opts, (error, data, response) => {
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
 **ids** | [**[Number]**](Number.md)| IDs of team template attachments to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful | [optional] 
 **teamTemplateId** | [**[Number]**](Number.md)| Filters template attachments by team template IDs | [optional] 
 **perPage** | **Number**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] 
 **page** | **Number**| The current page to fetch results from. Defaults to 1 | [optional] 
 **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] 
 **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] 

### Return type

[**[TeamTemplateAttachment]**](TeamTemplateAttachment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

