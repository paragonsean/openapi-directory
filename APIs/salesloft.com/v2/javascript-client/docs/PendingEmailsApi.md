# SalesLoftPlatform.PendingEmailsApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2PendingEmailsIdJsonPut**](PendingEmailsApi.md#v2PendingEmailsIdJsonPut) | **PUT** /v2/pending_emails/{id}.json | Updates the status of an email sent by an External Email Client
[**v2PendingEmailsJsonGet**](PendingEmailsApi.md#v2PendingEmailsJsonGet) | **GET** /v2/pending_emails.json | Fetches a list of emails ready to be sent by an external email service. Only emails sent with an External Email Client will appear here.



## v2PendingEmailsIdJsonPut

> PendingEmail v2PendingEmailsIdJsonPut(id, messageId, status, opts)

Updates the status of an email sent by an External Email Client

Updates the status of an email sent by an External Email Client. Does not affect lofted emails. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.PendingEmailsApi();
let id = "id_example"; // String | Email ID
let messageId = "messageId_example"; // String | The message id of the email that was sent
let status = "status_example"; // String | Delivery status of the email.  Valid statuses are 'sent' and 'failed'
let opts = {
  'errorMessage': "errorMessage_example", // String | The error message indicating why the email failed to send
  'sentAt': "sentAt_example" // String | The time that the email was actually sent in iso8601 format
};
apiInstance.v2PendingEmailsIdJsonPut(id, messageId, status, opts, (error, data, response) => {
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
 **id** | **String**| Email ID | 
 **messageId** | **String**| The message id of the email that was sent | 
 **status** | **String**| Delivery status of the email.  Valid statuses are &#39;sent&#39; and &#39;failed&#39; | 
 **errorMessage** | **String**| The error message indicating why the email failed to send | [optional] 
 **sentAt** | **String**| The time that the email was actually sent in iso8601 format | [optional] 

### Return type

[**PendingEmail**](PendingEmail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*


## v2PendingEmailsJsonGet

> [PendingEmail] v2PendingEmailsJsonGet(opts)

Fetches a list of emails ready to be sent by an external email service. Only emails sent with an External Email Client will appear here.

Fetches a list of emails ready to be sent by an external email service. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.PendingEmailsApi();
let opts = {
  'perPage': 56, // Number | How many records to show per page in the range [1, 100]. Defaults to 25
  'page': 56, // Number | The current page to fetch results from. Defaults to 1
  'includePagingCounts': true, // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
  'limitPagingCounts': true // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
};
apiInstance.v2PendingEmailsJsonGet(opts, (error, data, response) => {
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
 **perPage** | **Number**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] 
 **page** | **Number**| The current page to fetch results from. Defaults to 1 | [optional] 
 **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] 
 **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] 

### Return type

[**[PendingEmail]**](PendingEmail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

