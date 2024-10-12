# FilesComApi.BundleRecipientsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getBundleRecipients**](BundleRecipientsApi.md#getBundleRecipients) | **GET** /bundle_recipients | List Bundle Recipients
[**postBundleRecipients**](BundleRecipientsApi.md#postBundleRecipients) | **POST** /bundle_recipients | Create Bundle Recipient



## getBundleRecipients

> [BundleRecipientEntity] getBundleRecipients(bundleId, opts)

List Bundle Recipients

List Bundle Recipients

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.BundleRecipientsApi();
let bundleId = 56; // Number | List recipients for the bundle with this ID.
let opts = {
  'userId': 56, // Number | User ID.  Provide a value of `0` to operate the current session's user.
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56, // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
  'sortBy': {key: null}, // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[has_registrations]=desc`). Valid fields are `has_registrations`.
  'filter': {key: null} // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `has_registrations`.
};
apiInstance.getBundleRecipients(bundleId, opts, (error, data, response) => {
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
 **bundleId** | **Number**| List recipients for the bundle with this ID. | 
 **userId** | **Number**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] 
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 
 **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[has_registrations]&#x3D;desc&#x60;). Valid fields are &#x60;has_registrations&#x60;. | [optional] 
 **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;has_registrations&#x60;. | [optional] 

### Return type

[**[BundleRecipientEntity]**](BundleRecipientEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postBundleRecipients

> BundleRecipientEntity postBundleRecipients(bundleId, recipient, opts)

Create Bundle Recipient

Create Bundle Recipient

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.BundleRecipientsApi();
let bundleId = 56; // Number | Bundle to share.
let recipient = "recipient_example"; // String | Email addresses to share this bundle with.
let opts = {
  'company': "company_example", // String | Company of recipient.
  'name': "name_example", // String | Name of recipient.
  'note': "note_example", // String | Note to include in email.
  'shareAfterCreate': true, // Boolean | Set to true to share the link with the recipient upon creation.
  'userId': 56 // Number | User ID.  Provide a value of `0` to operate the current session's user.
};
apiInstance.postBundleRecipients(bundleId, recipient, opts, (error, data, response) => {
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
 **bundleId** | **Number**| Bundle to share. | 
 **recipient** | **String**| Email addresses to share this bundle with. | 
 **company** | **String**| Company of recipient. | [optional] 
 **name** | **String**| Name of recipient. | [optional] 
 **note** | **String**| Note to include in email. | [optional] 
 **shareAfterCreate** | **Boolean**| Set to true to share the link with the recipient upon creation. | [optional] 
 **userId** | **Number**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] 

### Return type

[**BundleRecipientEntity**](BundleRecipientEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

