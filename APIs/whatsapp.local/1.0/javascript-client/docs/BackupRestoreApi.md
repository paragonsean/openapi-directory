# WhatsAppBusinessApi.BackupRestoreApi

All URIs are relative to *http://whatsapp.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backupSettings**](BackupRestoreApi.md#backupSettings) | **POST** /settings/backup | Backup-Settings
[**restoreSettings**](BackupRestoreApi.md#restoreSettings) | **POST** /settings/restore | Restore-Settings



## backupSettings

> BackupSettingsResponse backupSettings(backupSettingsRequestBody)

Backup-Settings

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.BackupRestoreApi();
let backupSettingsRequestBody = {"password":"<Password for Backup>"}; // BackupSettingsRequestBody | 
apiInstance.backupSettings(backupSettingsRequestBody, (error, data, response) => {
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
 **backupSettingsRequestBody** | [**BackupSettingsRequestBody**](BackupSettingsRequestBody.md)|  | 

### Return type

[**BackupSettingsResponse**](BackupSettingsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## restoreSettings

> restoreSettings(restoreSettingsRequestBody)

Restore-Settings

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.BackupRestoreApi();
let restoreSettingsRequestBody = {"data":"<Data to Restore, from Backup API>","password":"<Password for Backup>"}; // RestoreSettingsRequestBody | 
apiInstance.restoreSettings(restoreSettingsRequestBody, (error, data, response) => {
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
 **restoreSettingsRequestBody** | [**RestoreSettingsRequestBody**](RestoreSettingsRequestBody.md)|  | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

