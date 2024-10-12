# SalesLoftPlatform.EmailTemplateAttachmentsApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2EmailTemplateAttachmentsJsonGet**](EmailTemplateAttachmentsApi.md#v2EmailTemplateAttachmentsJsonGet) | **GET** /v2/email_template_attachments.json | List email template attachments



## v2EmailTemplateAttachmentsJsonGet

> [EmailTemplateAttachment] v2EmailTemplateAttachmentsJsonGet(opts)

List email template attachments

Fetches multiple email template attachment records. The records can be filtered and paged according to the respective parameters. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.EmailTemplateAttachmentsApi();
let opts = {
  'ids': [null], // [Number] | IDs of email template attachments to fetch. If a record can't be found, that record won't be returned and your request will be successful
  'emailTemplateId': [null], // [Number] | Filters email template attachments by email template IDs
  'perPage': 56, // Number | How many records to show per page in the range [1, 100]. Defaults to 25
  'page': 56, // Number | The current page to fetch results from. Defaults to 1
  'includePagingCounts': true, // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
  'limitPagingCounts': true // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
};
apiInstance.v2EmailTemplateAttachmentsJsonGet(opts, (error, data, response) => {
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
 **ids** | [**[Number]**](Number.md)| IDs of email template attachments to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful | [optional] 
 **emailTemplateId** | [**[Number]**](Number.md)| Filters email template attachments by email template IDs | [optional] 
 **perPage** | **Number**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] 
 **page** | **Number**| The current page to fetch results from. Defaults to 1 | [optional] 
 **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] 
 **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] 

### Return type

[**[EmailTemplateAttachment]**](EmailTemplateAttachment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

