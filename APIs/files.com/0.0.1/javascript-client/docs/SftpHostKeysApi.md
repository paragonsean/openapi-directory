# FilesComApi.SftpHostKeysApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteSftpHostKeysId**](SftpHostKeysApi.md#deleteSftpHostKeysId) | **DELETE** /sftp_host_keys/{id} | Delete Sftp Host Key
[**getSftpHostKeys**](SftpHostKeysApi.md#getSftpHostKeys) | **GET** /sftp_host_keys | List Sftp Host Keys
[**getSftpHostKeysId**](SftpHostKeysApi.md#getSftpHostKeysId) | **GET** /sftp_host_keys/{id} | Show Sftp Host Key
[**patchSftpHostKeysId**](SftpHostKeysApi.md#patchSftpHostKeysId) | **PATCH** /sftp_host_keys/{id} | Update Sftp Host Key
[**postSftpHostKeys**](SftpHostKeysApi.md#postSftpHostKeys) | **POST** /sftp_host_keys | Create Sftp Host Key



## deleteSftpHostKeysId

> deleteSftpHostKeysId(id)

Delete Sftp Host Key

Delete Sftp Host Key

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.SftpHostKeysApi();
let id = 56; // Number | Sftp Host Key ID.
apiInstance.deleteSftpHostKeysId(id, (error, data, response) => {
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
 **id** | **Number**| Sftp Host Key ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSftpHostKeys

> [SftpHostKeyEntity] getSftpHostKeys(opts)

List Sftp Host Keys

List Sftp Host Keys

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.SftpHostKeysApi();
let opts = {
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56 // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
};
apiInstance.getSftpHostKeys(opts, (error, data, response) => {
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

[**[SftpHostKeyEntity]**](SftpHostKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSftpHostKeysId

> SftpHostKeyEntity getSftpHostKeysId(id)

Show Sftp Host Key

Show Sftp Host Key

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.SftpHostKeysApi();
let id = 56; // Number | Sftp Host Key ID.
apiInstance.getSftpHostKeysId(id, (error, data, response) => {
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
 **id** | **Number**| Sftp Host Key ID. | 

### Return type

[**SftpHostKeyEntity**](SftpHostKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchSftpHostKeysId

> SftpHostKeyEntity patchSftpHostKeysId(id, opts)

Update Sftp Host Key

Update Sftp Host Key

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.SftpHostKeysApi();
let id = 56; // Number | Sftp Host Key ID.
let opts = {
  'name': "name_example", // String | The friendly name of this SFTP Host Key.
  'privateKey': "privateKey_example" // String | The private key data.
};
apiInstance.patchSftpHostKeysId(id, opts, (error, data, response) => {
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
 **id** | **Number**| Sftp Host Key ID. | 
 **name** | **String**| The friendly name of this SFTP Host Key. | [optional] 
 **privateKey** | **String**| The private key data. | [optional] 

### Return type

[**SftpHostKeyEntity**](SftpHostKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## postSftpHostKeys

> SftpHostKeyEntity postSftpHostKeys(opts)

Create Sftp Host Key

Create Sftp Host Key

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.SftpHostKeysApi();
let opts = {
  'name': "name_example", // String | The friendly name of this SFTP Host Key.
  'privateKey': "privateKey_example" // String | The private key data.
};
apiInstance.postSftpHostKeys(opts, (error, data, response) => {
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
 **name** | **String**| The friendly name of this SFTP Host Key. | [optional] 
 **privateKey** | **String**| The private key data. | [optional] 

### Return type

[**SftpHostKeyEntity**](SftpHostKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

