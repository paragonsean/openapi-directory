# FilesComApi.PublicKeysApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletePublicKeysId**](PublicKeysApi.md#deletePublicKeysId) | **DELETE** /public_keys/{id} | Delete Public Key
[**getPublicKeys**](PublicKeysApi.md#getPublicKeys) | **GET** /public_keys | List Public Keys
[**getPublicKeysId**](PublicKeysApi.md#getPublicKeysId) | **GET** /public_keys/{id} | Show Public Key
[**patchPublicKeysId**](PublicKeysApi.md#patchPublicKeysId) | **PATCH** /public_keys/{id} | Update Public Key
[**postPublicKeys**](PublicKeysApi.md#postPublicKeys) | **POST** /public_keys | Create Public Key



## deletePublicKeysId

> deletePublicKeysId(id)

Delete Public Key

Delete Public Key

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.PublicKeysApi();
let id = 56; // Number | Public Key ID.
apiInstance.deletePublicKeysId(id, (error, data, response) => {
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
 **id** | **Number**| Public Key ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getPublicKeys

> [PublicKeyEntity] getPublicKeys(opts)

List Public Keys

List Public Keys

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.PublicKeysApi();
let opts = {
  'userId': 56, // Number | User ID.  Provide a value of `0` to operate the current session's user.
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56 // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
};
apiInstance.getPublicKeys(opts, (error, data, response) => {
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

### Return type

[**[PublicKeyEntity]**](PublicKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPublicKeysId

> PublicKeyEntity getPublicKeysId(id)

Show Public Key

Show Public Key

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.PublicKeysApi();
let id = 56; // Number | Public Key ID.
apiInstance.getPublicKeysId(id, (error, data, response) => {
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
 **id** | **Number**| Public Key ID. | 

### Return type

[**PublicKeyEntity**](PublicKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchPublicKeysId

> PublicKeyEntity patchPublicKeysId(id, title)

Update Public Key

Update Public Key

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.PublicKeysApi();
let id = 56; // Number | Public Key ID.
let title = "title_example"; // String | Internal reference for key.
apiInstance.patchPublicKeysId(id, title, (error, data, response) => {
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
 **id** | **Number**| Public Key ID. | 
 **title** | **String**| Internal reference for key. | 

### Return type

[**PublicKeyEntity**](PublicKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## postPublicKeys

> PublicKeyEntity postPublicKeys(publicKey, title, opts)

Create Public Key

Create Public Key

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.PublicKeysApi();
let publicKey = "publicKey_example"; // String | Actual contents of SSH key.
let title = "title_example"; // String | Internal reference for key.
let opts = {
  'userId': 56 // Number | User ID.  Provide a value of `0` to operate the current session's user.
};
apiInstance.postPublicKeys(publicKey, title, opts, (error, data, response) => {
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
 **publicKey** | **String**| Actual contents of SSH key. | 
 **title** | **String**| Internal reference for key. | 
 **userId** | **Number**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] 

### Return type

[**PublicKeyEntity**](PublicKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

