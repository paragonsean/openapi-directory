# 1PasswordConnect.FilesApi

All URIs are relative to *http://1password.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**downloadFileByID**](FilesApi.md#downloadFileByID) | **GET** /vaults/{vaultUuid}/items/{itemUuid}/files/{fileUuid}/content | Get the content of a File
[**getDetailsOfFileById**](FilesApi.md#getDetailsOfFileById) | **GET** /vaults/{vaultUuid}/items/{itemUuid}/files/{fileUuid} | Get the details of a File
[**getItemFiles**](FilesApi.md#getItemFiles) | **GET** /vaults/{vaultUuid}/items/{itemUuid}/files | Get all the files inside an Item



## downloadFileByID

> File downloadFileByID(vaultUuid, itemUuid, fileUuid)

Get the content of a File

### Example

```javascript
import 1PasswordConnect from '1_password_connect';
let defaultClient = 1PasswordConnect.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: ConnectToken
let ConnectToken = defaultClient.authentications['ConnectToken'];
ConnectToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new 1PasswordConnect.FilesApi();
let vaultUuid = "vaultUuid_example"; // String | The UUID of the Vault the item is in
let itemUuid = "itemUuid_example"; // String | The UUID of the Item the File is in
let fileUuid = "fileUuid_example"; // String | UUID of the file to get content from
apiInstance.downloadFileByID(vaultUuid, itemUuid, fileUuid, (error, data, response) => {
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
 **vaultUuid** | **String**| The UUID of the Vault the item is in | 
 **itemUuid** | **String**| The UUID of the Item the File is in | 
 **fileUuid** | **String**| UUID of the file to get content from | 

### Return type

**File**

### Authorization

[ConnectToken](../README.md#ConnectToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, application/json


## getDetailsOfFileById

> File getDetailsOfFileById(vaultUuid, itemUuid, fileUuid, opts)

Get the details of a File

### Example

```javascript
import 1PasswordConnect from '1_password_connect';
let defaultClient = 1PasswordConnect.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: ConnectToken
let ConnectToken = defaultClient.authentications['ConnectToken'];
ConnectToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new 1PasswordConnect.FilesApi();
let vaultUuid = "vaultUuid_example"; // String | The UUID of the Vault to fetch Item from
let itemUuid = "itemUuid_example"; // String | The UUID of the Item to fetch File from
let fileUuid = "fileUuid_example"; // String | The UUID of the File to fetch
let opts = {
  'inlineFiles': true // Boolean | Tells server to return the base64-encoded file contents in the response.
};
apiInstance.getDetailsOfFileById(vaultUuid, itemUuid, fileUuid, opts, (error, data, response) => {
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
 **vaultUuid** | **String**| The UUID of the Vault to fetch Item from | 
 **itemUuid** | **String**| The UUID of the Item to fetch File from | 
 **fileUuid** | **String**| The UUID of the File to fetch | 
 **inlineFiles** | **Boolean**| Tells server to return the base64-encoded file contents in the response. | [optional] 

### Return type

**File**

### Authorization

[ConnectToken](../README.md#ConnectToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getItemFiles

> [File] getItemFiles(vaultUuid, itemUuid, opts)

Get all the files inside an Item

### Example

```javascript
import 1PasswordConnect from '1_password_connect';
let defaultClient = 1PasswordConnect.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: ConnectToken
let ConnectToken = defaultClient.authentications['ConnectToken'];
ConnectToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new 1PasswordConnect.FilesApi();
let vaultUuid = "vaultUuid_example"; // String | The UUID of the Vault to fetch Items from
let itemUuid = "itemUuid_example"; // String | The UUID of the Item to fetch files from
let opts = {
  'inlineFiles': true // Boolean | Tells server to return the base64-encoded file contents in the response.
};
apiInstance.getItemFiles(vaultUuid, itemUuid, opts, (error, data, response) => {
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
 **vaultUuid** | **String**| The UUID of the Vault to fetch Items from | 
 **itemUuid** | **String**| The UUID of the Item to fetch files from | 
 **inlineFiles** | **Boolean**| Tells server to return the base64-encoded file contents in the response. | [optional] 

### Return type

**[File]**

### Authorization

[ConnectToken](../README.md#ConnectToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

