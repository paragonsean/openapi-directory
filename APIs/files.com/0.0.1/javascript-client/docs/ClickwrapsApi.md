# FilesComApi.ClickwrapsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteClickwrapsId**](ClickwrapsApi.md#deleteClickwrapsId) | **DELETE** /clickwraps/{id} | Delete Clickwrap
[**getClickwraps**](ClickwrapsApi.md#getClickwraps) | **GET** /clickwraps | List Clickwraps
[**getClickwrapsId**](ClickwrapsApi.md#getClickwrapsId) | **GET** /clickwraps/{id} | Show Clickwrap
[**patchClickwrapsId**](ClickwrapsApi.md#patchClickwrapsId) | **PATCH** /clickwraps/{id} | Update Clickwrap
[**postClickwraps**](ClickwrapsApi.md#postClickwraps) | **POST** /clickwraps | Create Clickwrap



## deleteClickwrapsId

> deleteClickwrapsId(id)

Delete Clickwrap

Delete Clickwrap

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.ClickwrapsApi();
let id = 56; // Number | Clickwrap ID.
apiInstance.deleteClickwrapsId(id, (error, data, response) => {
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
 **id** | **Number**| Clickwrap ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getClickwraps

> [ClickwrapEntity] getClickwraps(opts)

List Clickwraps

List Clickwraps

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.ClickwrapsApi();
let opts = {
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56 // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
};
apiInstance.getClickwraps(opts, (error, data, response) => {
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

### Return type

[**[ClickwrapEntity]**](ClickwrapEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getClickwrapsId

> ClickwrapEntity getClickwrapsId(id)

Show Clickwrap

Show Clickwrap

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.ClickwrapsApi();
let id = 56; // Number | Clickwrap ID.
apiInstance.getClickwrapsId(id, (error, data, response) => {
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
 **id** | **Number**| Clickwrap ID. | 

### Return type

[**ClickwrapEntity**](ClickwrapEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchClickwrapsId

> ClickwrapEntity patchClickwrapsId(id, opts)

Update Clickwrap

Update Clickwrap

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.ClickwrapsApi();
let id = 56; // Number | Clickwrap ID.
let opts = {
  'body': "body_example", // String | Body text of Clickwrap (supports Markdown formatting).
  'name': "name_example", // String | Name of the Clickwrap agreement (used when selecting from multiple Clickwrap agreements.)
  'useWithBundles': "useWithBundles_example", // String | Use this Clickwrap for Bundles?
  'useWithInboxes': "useWithInboxes_example", // String | Use this Clickwrap for Inboxes?
  'useWithUsers': "useWithUsers_example" // String | Use this Clickwrap for User Registrations?  Note: This only applies to User Registrations where the User is invited to your Files.com site using an E-Mail invitation process where they then set their own password.
};
apiInstance.patchClickwrapsId(id, opts, (error, data, response) => {
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
 **id** | **Number**| Clickwrap ID. | 
 **body** | **String**| Body text of Clickwrap (supports Markdown formatting). | [optional] 
 **name** | **String**| Name of the Clickwrap agreement (used when selecting from multiple Clickwrap agreements.) | [optional] 
 **useWithBundles** | **String**| Use this Clickwrap for Bundles? | [optional] 
 **useWithInboxes** | **String**| Use this Clickwrap for Inboxes? | [optional] 
 **useWithUsers** | **String**| Use this Clickwrap for User Registrations?  Note: This only applies to User Registrations where the User is invited to your Files.com site using an E-Mail invitation process where they then set their own password. | [optional] 

### Return type

[**ClickwrapEntity**](ClickwrapEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## postClickwraps

> ClickwrapEntity postClickwraps(opts)

Create Clickwrap

Create Clickwrap

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.ClickwrapsApi();
let opts = {
  'body': "body_example", // String | Body text of Clickwrap (supports Markdown formatting).
  'name': "name_example", // String | Name of the Clickwrap agreement (used when selecting from multiple Clickwrap agreements.)
  'useWithBundles': "useWithBundles_example", // String | Use this Clickwrap for Bundles?
  'useWithInboxes': "useWithInboxes_example", // String | Use this Clickwrap for Inboxes?
  'useWithUsers': "useWithUsers_example" // String | Use this Clickwrap for User Registrations?  Note: This only applies to User Registrations where the User is invited to your Files.com site using an E-Mail invitation process where they then set their own password.
};
apiInstance.postClickwraps(opts, (error, data, response) => {
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
 **body** | **String**| Body text of Clickwrap (supports Markdown formatting). | [optional] 
 **name** | **String**| Name of the Clickwrap agreement (used when selecting from multiple Clickwrap agreements.) | [optional] 
 **useWithBundles** | **String**| Use this Clickwrap for Bundles? | [optional] 
 **useWithInboxes** | **String**| Use this Clickwrap for Inboxes? | [optional] 
 **useWithUsers** | **String**| Use this Clickwrap for User Registrations?  Note: This only applies to User Registrations where the User is invited to your Files.com site using an E-Mail invitation process where they then set their own password. | [optional] 

### Return type

[**ClickwrapEntity**](ClickwrapEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

