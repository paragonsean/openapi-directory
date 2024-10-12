# FilesComApi.BundlesApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteBundlesId**](BundlesApi.md#deleteBundlesId) | **DELETE** /bundles/{id} | Delete Bundle
[**getBundles**](BundlesApi.md#getBundles) | **GET** /bundles | List Bundles
[**getBundlesId**](BundlesApi.md#getBundlesId) | **GET** /bundles/{id} | Show Bundle
[**patchBundlesId**](BundlesApi.md#patchBundlesId) | **PATCH** /bundles/{id} | Update Bundle
[**postBundles**](BundlesApi.md#postBundles) | **POST** /bundles | Create Bundle
[**postBundlesIdShare**](BundlesApi.md#postBundlesIdShare) | **POST** /bundles/{id}/share | Send email(s) with a link to bundle



## deleteBundlesId

> deleteBundlesId(id)

Delete Bundle

Delete Bundle

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.BundlesApi();
let id = 56; // Number | Bundle ID.
apiInstance.deleteBundlesId(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| Bundle ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getBundles

> [BundleEntity] getBundles(opts)

List Bundles

List Bundles

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.BundlesApi();
let opts = {
  'userId': 56, // Number | User ID.  Provide a value of `0` to operate the current session's user.
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56, // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
  'sortBy': {key: null}, // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[created_at]=desc`). Valid fields are `created_at` and `code`.
  'filter': {key: null}, // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `created_at`.
  'filterGt': {key: null}, // Object | If set, return records where the specified field is greater than the supplied value. Valid fields are `created_at`.
  'filterGteq': {key: null}, // Object | If set, return records where the specified field is greater than or equal the supplied value. Valid fields are `created_at`.
  'filterLt': {key: null}, // Object | If set, return records where the specified field is less than the supplied value. Valid fields are `created_at`.
  'filterLteq': {key: null} // Object | If set, return records where the specified field is less than or equal the supplied value. Valid fields are `created_at`.
};
apiInstance.getBundles(opts, (error, data, response) => {
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
 **userId** | **Number**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] 
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 
 **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[created_at]&#x3D;desc&#x60;). Valid fields are &#x60;created_at&#x60; and &#x60;code&#x60;. | [optional] 
 **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;created_at&#x60;. | [optional] 
 **filterGt** | [**Object**](.md)| If set, return records where the specified field is greater than the supplied value. Valid fields are &#x60;created_at&#x60;. | [optional] 
 **filterGteq** | [**Object**](.md)| If set, return records where the specified field is greater than or equal the supplied value. Valid fields are &#x60;created_at&#x60;. | [optional] 
 **filterLt** | [**Object**](.md)| If set, return records where the specified field is less than the supplied value. Valid fields are &#x60;created_at&#x60;. | [optional] 
 **filterLteq** | [**Object**](.md)| If set, return records where the specified field is less than or equal the supplied value. Valid fields are &#x60;created_at&#x60;. | [optional] 

### Return type

[**[BundleEntity]**](BundleEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBundlesId

> BundleEntity getBundlesId(id)

Show Bundle

Show Bundle

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.BundlesApi();
let id = 56; // Number | Bundle ID.
apiInstance.getBundlesId(id, (error, data, response) => {
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
 **id** | **Number**| Bundle ID. | 

### Return type

[**BundleEntity**](BundleEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchBundlesId

> BundleEntity patchBundlesId(id, opts)

Update Bundle

Update Bundle

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.BundlesApi();
let id = 56; // Number | Bundle ID.
let opts = {
  'clickwrapId': 56, // Number | ID of the clickwrap to use with this bundle.
  'code': "code_example", // String | Bundle code.  This code forms the end part of the Public URL.
  'description': "description_example", // String | Public description
  'dontSeparateSubmissionsByFolder': true, // Boolean | Do not create subfolders for files uploaded to this share. Note: there are subtle security pitfalls with allowing anonymous uploads from multiple users to live in the same folder. We strongly discourage use of this option unless absolutely required.
  'expiresAt': new Date("2013-10-20T19:20:30+01:00"), // Date | Bundle expiration date/time
  'formFieldSetId': 56, // Number | Id of Form Field Set to use with this bundle
  'inboxId': 56, // Number | ID of the associated inbox, if available.
  'maxUses': 56, // Number | Maximum number of times bundle can be accessed
  'note': "note_example", // String | Bundle internal note
  'password': "password_example", // String | Password for this bundle.
  'pathTemplate': "pathTemplate_example", // String | Template for creating submission subfolders. Can use the uploader's name, email address, ip, company, and any custom form data.
  'paths': ["null"], // [String] | A list of paths to include in this bundle.
  'permissions': "permissions_example", // String | Permissions that apply to Folders in this Share Link.
  'previewOnly': true, // Boolean | Restrict users to previewing files only?
  'requireRegistration': true, // Boolean | Show a registration page that captures the downloader's name and email address?
  'requireShareRecipient': true, // Boolean | Only allow access to recipients who have explicitly received the share via an email sent through the Files.com UI?
  'sendEmailReceiptToUploader': true, // Boolean | Send delivery receipt to the uploader. Note: For writable share only
  'skipCompany': true, // Boolean | BundleRegistrations can be saved without providing company?
  'skipEmail': true, // Boolean | BundleRegistrations can be saved without providing email?
  'skipName': true, // Boolean | BundleRegistrations can be saved without providing name?
  'watermarkAttachmentDelete': true, // Boolean | If true, will delete the file stored in watermark_attachment
  'watermarkAttachmentFile': "/path/to/file" // File | Preview watermark image applied to all bundle items.
};
apiInstance.patchBundlesId(id, opts, (error, data, response) => {
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
 **id** | **Number**| Bundle ID. | 
 **clickwrapId** | **Number**| ID of the clickwrap to use with this bundle. | [optional] 
 **code** | **String**| Bundle code.  This code forms the end part of the Public URL. | [optional] 
 **description** | **String**| Public description | [optional] 
 **dontSeparateSubmissionsByFolder** | **Boolean**| Do not create subfolders for files uploaded to this share. Note: there are subtle security pitfalls with allowing anonymous uploads from multiple users to live in the same folder. We strongly discourage use of this option unless absolutely required. | [optional] 
 **expiresAt** | **Date**| Bundle expiration date/time | [optional] 
 **formFieldSetId** | **Number**| Id of Form Field Set to use with this bundle | [optional] 
 **inboxId** | **Number**| ID of the associated inbox, if available. | [optional] 
 **maxUses** | **Number**| Maximum number of times bundle can be accessed | [optional] 
 **note** | **String**| Bundle internal note | [optional] 
 **password** | **String**| Password for this bundle. | [optional] 
 **pathTemplate** | **String**| Template for creating submission subfolders. Can use the uploader&#39;s name, email address, ip, company, and any custom form data. | [optional] 
 **paths** | [**[String]**](String.md)| A list of paths to include in this bundle. | [optional] 
 **permissions** | **String**| Permissions that apply to Folders in this Share Link. | [optional] 
 **previewOnly** | **Boolean**| Restrict users to previewing files only? | [optional] 
 **requireRegistration** | **Boolean**| Show a registration page that captures the downloader&#39;s name and email address? | [optional] 
 **requireShareRecipient** | **Boolean**| Only allow access to recipients who have explicitly received the share via an email sent through the Files.com UI? | [optional] 
 **sendEmailReceiptToUploader** | **Boolean**| Send delivery receipt to the uploader. Note: For writable share only | [optional] 
 **skipCompany** | **Boolean**| BundleRegistrations can be saved without providing company? | [optional] 
 **skipEmail** | **Boolean**| BundleRegistrations can be saved without providing email? | [optional] 
 **skipName** | **Boolean**| BundleRegistrations can be saved without providing name? | [optional] 
 **watermarkAttachmentDelete** | **Boolean**| If true, will delete the file stored in watermark_attachment | [optional] 
 **watermarkAttachmentFile** | **File**| Preview watermark image applied to all bundle items. | [optional] 

### Return type

[**BundleEntity**](BundleEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## postBundles

> BundleEntity postBundles(paths, opts)

Create Bundle

Create Bundle

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.BundlesApi();
let paths = ["null"]; // [String] | A list of paths to include in this bundle.
let opts = {
  'clickwrapId': 56, // Number | ID of the clickwrap to use with this bundle.
  'code': "code_example", // String | Bundle code.  This code forms the end part of the Public URL.
  'description': "description_example", // String | Public description
  'dontSeparateSubmissionsByFolder': true, // Boolean | Do not create subfolders for files uploaded to this share. Note: there are subtle security pitfalls with allowing anonymous uploads from multiple users to live in the same folder. We strongly discourage use of this option unless absolutely required.
  'expiresAt': new Date("2013-10-20T19:20:30+01:00"), // Date | Bundle expiration date/time
  'formFieldSetId': 56, // Number | Id of Form Field Set to use with this bundle
  'inboxId': 56, // Number | ID of the associated inbox, if available.
  'maxUses': 56, // Number | Maximum number of times bundle can be accessed
  'note': "note_example", // String | Bundle internal note
  'password': "password_example", // String | Password for this bundle.
  'pathTemplate': "pathTemplate_example", // String | Template for creating submission subfolders. Can use the uploader's name, email address, ip, company, and any custom form data.
  'permissions': "permissions_example", // String | Permissions that apply to Folders in this Share Link.
  'previewOnly': true, // Boolean | Restrict users to previewing files only?
  'requireRegistration': true, // Boolean | Show a registration page that captures the downloader's name and email address?
  'requireShareRecipient': true, // Boolean | Only allow access to recipients who have explicitly received the share via an email sent through the Files.com UI?
  'sendEmailReceiptToUploader': true, // Boolean | Send delivery receipt to the uploader. Note: For writable share only
  'skipCompany': true, // Boolean | BundleRegistrations can be saved without providing company?
  'skipEmail': true, // Boolean | BundleRegistrations can be saved without providing email?
  'skipName': true, // Boolean | BundleRegistrations can be saved without providing name?
  'userId': 56, // Number | User ID.  Provide a value of `0` to operate the current session's user.
  'watermarkAttachmentFile': "/path/to/file" // File | Preview watermark image applied to all bundle items.
};
apiInstance.postBundles(paths, opts, (error, data, response) => {
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
 **paths** | [**[String]**](String.md)| A list of paths to include in this bundle. | 
 **clickwrapId** | **Number**| ID of the clickwrap to use with this bundle. | [optional] 
 **code** | **String**| Bundle code.  This code forms the end part of the Public URL. | [optional] 
 **description** | **String**| Public description | [optional] 
 **dontSeparateSubmissionsByFolder** | **Boolean**| Do not create subfolders for files uploaded to this share. Note: there are subtle security pitfalls with allowing anonymous uploads from multiple users to live in the same folder. We strongly discourage use of this option unless absolutely required. | [optional] 
 **expiresAt** | **Date**| Bundle expiration date/time | [optional] 
 **formFieldSetId** | **Number**| Id of Form Field Set to use with this bundle | [optional] 
 **inboxId** | **Number**| ID of the associated inbox, if available. | [optional] 
 **maxUses** | **Number**| Maximum number of times bundle can be accessed | [optional] 
 **note** | **String**| Bundle internal note | [optional] 
 **password** | **String**| Password for this bundle. | [optional] 
 **pathTemplate** | **String**| Template for creating submission subfolders. Can use the uploader&#39;s name, email address, ip, company, and any custom form data. | [optional] 
 **permissions** | **String**| Permissions that apply to Folders in this Share Link. | [optional] 
 **previewOnly** | **Boolean**| Restrict users to previewing files only? | [optional] 
 **requireRegistration** | **Boolean**| Show a registration page that captures the downloader&#39;s name and email address? | [optional] 
 **requireShareRecipient** | **Boolean**| Only allow access to recipients who have explicitly received the share via an email sent through the Files.com UI? | [optional] 
 **sendEmailReceiptToUploader** | **Boolean**| Send delivery receipt to the uploader. Note: For writable share only | [optional] 
 **skipCompany** | **Boolean**| BundleRegistrations can be saved without providing company? | [optional] 
 **skipEmail** | **Boolean**| BundleRegistrations can be saved without providing email? | [optional] 
 **skipName** | **Boolean**| BundleRegistrations can be saved without providing name? | [optional] 
 **userId** | **Number**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] 
 **watermarkAttachmentFile** | **File**| Preview watermark image applied to all bundle items. | [optional] 

### Return type

[**BundleEntity**](BundleEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## postBundlesIdShare

> postBundlesIdShare(id, opts)

Send email(s) with a link to bundle

Send email(s) with a link to bundle

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.BundlesApi();
let id = 56; // Number | Bundle ID.
let opts = {
  'note': "note_example", // String | Note to include in email.
  'recipients': [null], // [Object] | A list of recipients to share this bundle with. Required unless `to` is used.
  'to': ["null"] // [String] | A list of email addresses to share this bundle with. Required unless `recipients` is used.
};
apiInstance.postBundlesIdShare(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| Bundle ID. | 
 **note** | **String**| Note to include in email. | [optional] 
 **recipients** | [**[Object]**](Object.md)| A list of recipients to share this bundle with. Required unless &#x60;to&#x60; is used. | [optional] 
 **to** | [**[String]**](String.md)| A list of email addresses to share this bundle with. Required unless &#x60;recipients&#x60; is used. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined

