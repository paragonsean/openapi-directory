# DiscourseApiDocumentation.BackupsApi

All URIs are relative to *http://discourse.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createBackup**](BackupsApi.md#createBackup) | **POST** /admin/backups.json | Create backup
[**downloadBackup**](BackupsApi.md#downloadBackup) | **GET** /admin/backups/{filename} | Download backup
[**getBackups**](BackupsApi.md#getBackups) | **GET** /admin/backups.json | List backups
[**sendDownloadBackupEmail**](BackupsApi.md#sendDownloadBackupEmail) | **PUT** /admin/backups/{filename} | Send download backup email



## createBackup

> CreateBackup200Response createBackup(opts)

Create backup

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.BackupsApi();
let opts = {
  'createBackupRequest': new DiscourseApiDocumentation.CreateBackupRequest() // CreateBackupRequest | 
};
apiInstance.createBackup(opts, (error, data, response) => {
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
 **createBackupRequest** | [**CreateBackupRequest**](CreateBackupRequest.md)|  | [optional] 

### Return type

[**CreateBackup200Response**](CreateBackup200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## downloadBackup

> downloadBackup(filename, token)

Download backup

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.BackupsApi();
let filename = "filename_example"; // String | 
let token = "token_example"; // String | 
apiInstance.downloadBackup(filename, token, (error, data, response) => {
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
 **filename** | **String**|  | 
 **token** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getBackups

> [GetBackups200ResponseInner] getBackups()

List backups

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.BackupsApi();
apiInstance.getBackups((error, data, response) => {
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

[**[GetBackups200ResponseInner]**](GetBackups200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sendDownloadBackupEmail

> sendDownloadBackupEmail(filename)

Send download backup email

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.BackupsApi();
let filename = "filename_example"; // String | 
apiInstance.sendDownloadBackupEmail(filename, (error, data, response) => {
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
 **filename** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

