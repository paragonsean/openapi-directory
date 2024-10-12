# FilesComApi.InboxRecipientsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getInboxRecipients**](InboxRecipientsApi.md#getInboxRecipients) | **GET** /inbox_recipients | List Inbox Recipients
[**postInboxRecipients**](InboxRecipientsApi.md#postInboxRecipients) | **POST** /inbox_recipients | Create Inbox Recipient



## getInboxRecipients

> [InboxRecipientEntity] getInboxRecipients(inboxId, opts)

List Inbox Recipients

List Inbox Recipients

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.InboxRecipientsApi();
let inboxId = 56; // Number | List recipients for the inbox with this ID.
let opts = {
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56, // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
  'sortBy': {key: null}, // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[has_registrations]=desc`). Valid fields are `has_registrations`.
  'filter': {key: null} // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `has_registrations`.
};
apiInstance.getInboxRecipients(inboxId, opts, (error, data, response) => {
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
 **inboxId** | **Number**| List recipients for the inbox with this ID. | 
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 
 **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[has_registrations]&#x3D;desc&#x60;). Valid fields are &#x60;has_registrations&#x60;. | [optional] 
 **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;has_registrations&#x60;. | [optional] 

### Return type

[**[InboxRecipientEntity]**](InboxRecipientEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postInboxRecipients

> InboxRecipientEntity postInboxRecipients(inboxId, recipient, opts)

Create Inbox Recipient

Create Inbox Recipient

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.InboxRecipientsApi();
let inboxId = 56; // Number | Inbox to share.
let recipient = "recipient_example"; // String | Email address to share this inbox with.
let opts = {
  'company': "company_example", // String | Company of recipient.
  'name': "name_example", // String | Name of recipient.
  'note': "note_example", // String | Note to include in email.
  'shareAfterCreate': true // Boolean | Set to true to share the link with the recipient upon creation.
};
apiInstance.postInboxRecipients(inboxId, recipient, opts, (error, data, response) => {
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
 **inboxId** | **Number**| Inbox to share. | 
 **recipient** | **String**| Email address to share this inbox with. | 
 **company** | **String**| Company of recipient. | [optional] 
 **name** | **String**| Name of recipient. | [optional] 
 **note** | **String**| Note to include in email. | [optional] 
 **shareAfterCreate** | **Boolean**| Set to true to share the link with the recipient upon creation. | [optional] 

### Return type

[**InboxRecipientEntity**](InboxRecipientEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

