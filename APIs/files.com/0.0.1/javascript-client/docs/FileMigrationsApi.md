# FilesComApi.FileMigrationsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getFileMigrationsId**](FileMigrationsApi.md#getFileMigrationsId) | **GET** /file_migrations/{id} | Show File Migration



## getFileMigrationsId

> FileMigrationEntity getFileMigrationsId(id)

Show File Migration

Show File Migration

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.FileMigrationsApi();
let id = 56; // Number | File Migration ID.
apiInstance.getFileMigrationsId(id, (error, data, response) => {
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
 **id** | **Number**| File Migration ID. | 

### Return type

[**FileMigrationEntity**](FileMigrationEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

