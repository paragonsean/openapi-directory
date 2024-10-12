# FilesComApi.InboxRegistrationsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getInboxRegistrations**](InboxRegistrationsApi.md#getInboxRegistrations) | **GET** /inbox_registrations | List Inbox Registrations



## getInboxRegistrations

> [InboxRegistrationEntity] getInboxRegistrations(opts)

List Inbox Registrations

List Inbox Registrations

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.InboxRegistrationsApi();
let opts = {
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56, // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
  'folderBehaviorId': 56 // Number | ID of the associated Inbox.
};
apiInstance.getInboxRegistrations(opts, (error, data, response) => {
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
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 
 **folderBehaviorId** | **Number**| ID of the associated Inbox. | [optional] 

### Return type

[**[InboxRegistrationEntity]**](InboxRegistrationEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

