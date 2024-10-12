# FilesComApi.ApiKeyApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiKeyDeleteCurrent**](ApiKeyApi.md#apiKeyDeleteCurrent) | **DELETE** /api_key | Delete current API key.  (Requires current API connection to be using an API key.)
[**apiKeyFindCurrent**](ApiKeyApi.md#apiKeyFindCurrent) | **GET** /api_key | Show information about current API key.  (Requires current API connection to be using an API key.)
[**apiKeyUpdateCurrent**](ApiKeyApi.md#apiKeyUpdateCurrent) | **PATCH** /api_key | Update current API key.  (Requires current API connection to be using an API key.)



## apiKeyDeleteCurrent

> apiKeyDeleteCurrent()

Delete current API key.  (Requires current API connection to be using an API key.)

Delete current API key.  (Requires current API connection to be using an API key.)

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.ApiKeyApi();
apiInstance.apiKeyDeleteCurrent((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiKeyFindCurrent

> ApiKeyEntity apiKeyFindCurrent()

Show information about current API key.  (Requires current API connection to be using an API key.)

Show information about current API key.  (Requires current API connection to be using an API key.)

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.ApiKeyApi();
apiInstance.apiKeyFindCurrent((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiKeyEntity**](ApiKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiKeyUpdateCurrent

> ApiKeyEntity apiKeyUpdateCurrent(opts)

Update current API key.  (Requires current API connection to be using an API key.)

Update current API key.  (Requires current API connection to be using an API key.)

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.ApiKeyApi();
let opts = {
  'expiresAt': new Date("2013-10-20T19:20:30+01:00"), // Date | API Key expiration date
  'name': "name_example", // String | Internal name for the API Key.  For your use.
  'permissionSet': "permissionSet_example" // String | Permissions for this API Key.  Keys with the `desktop_app` permission set only have the ability to do the functions provided in our Desktop App (File and Share Link operations).  Additional permission sets may become available in the future, such as for a Site Admin to give a key with no administrator privileges.  If you have ideas for permission sets, please let us know.
};
apiInstance.apiKeyUpdateCurrent(opts, (error, data, response) => {
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
 **expiresAt** | **Date**| API Key expiration date | [optional] 
 **name** | **String**| Internal name for the API Key.  For your use. | [optional] 
 **permissionSet** | **String**| Permissions for this API Key.  Keys with the &#x60;desktop_app&#x60; permission set only have the ability to do the functions provided in our Desktop App (File and Share Link operations).  Additional permission sets may become available in the future, such as for a Site Admin to give a key with no administrator privileges.  If you have ideas for permission sets, please let us know. | [optional] 

### Return type

[**ApiKeyEntity**](ApiKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

