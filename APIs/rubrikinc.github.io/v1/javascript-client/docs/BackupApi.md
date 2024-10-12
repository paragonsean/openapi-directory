# RubrikRestApi.BackupApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createBackupRemediationAsyncTask**](BackupApi.md#createBackupRemediationAsyncTask) | **POST** /backup/retry | Reschedule unsuccessful backup tasks
[**getBackupRemediationAsyncTaskStatus**](BackupApi.md#getBackupRemediationAsyncTaskStatus) | **GET** /backup/retry/{id} | Get status of reschedule attempt
[**getBackupVerificationAsyncRequestStatus**](BackupApi.md#getBackupVerificationAsyncRequestStatus) | **GET** /backup/verify/{id} | Get asynchronous request details for Backup Verification
[**verifySnapshot**](BackupApi.md#verifySnapshot) | **POST** /backup/verify | Trigger a job for snapshot verification



## createBackupRemediationAsyncTask

> RemediationResponse createBackupRemediationAsyncTask(remediationRequest)

Reschedule unsuccessful backup tasks

Create an asynchronous task for rescheduling unsuccessful backup tasks. 

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.BackupApi();
let remediationRequest = new RubrikRestApi.RemediationRequest(); // RemediationRequest | Parameters required to reschedule unsuccessful backup tasks. 
apiInstance.createBackupRemediationAsyncTask(remediationRequest, (error, data, response) => {
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
 **remediationRequest** | [**RemediationRequest**](RemediationRequest.md)| Parameters required to reschedule unsuccessful backup tasks.  | 

### Return type

[**RemediationResponse**](RemediationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getBackupRemediationAsyncTaskStatus

> AsyncRequestStatus getBackupRemediationAsyncTaskStatus(id)

Get status of reschedule attempt

Retrieve the details of a specified asynchronous task to use for rescheduling unsuccessful tasks. 

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.BackupApi();
let id = "id_example"; // String | Async request id.
apiInstance.getBackupRemediationAsyncTaskStatus(id, (error, data, response) => {
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
 **id** | **String**| Async request id. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBackupVerificationAsyncRequestStatus

> VerificationResponse getBackupVerificationAsyncRequestStatus(id)

Get asynchronous request details for Backup Verification

Get the details of an asynchronous request for a backup verification job. 

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.BackupApi();
let id = "id_example"; // String | ID of the asynchronous request.
apiInstance.getBackupVerificationAsyncRequestStatus(id, (error, data, response) => {
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
 **id** | **String**| ID of the asynchronous request. | 

### Return type

[**VerificationResponse**](VerificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## verifySnapshot

> VerificationResponse verifySnapshot(verificationParameters)

Trigger a job for snapshot verification

This REST API triggers the job \&quot;BACKUP_INTEGRITY_VERIFICATION\&quot;, which verifies whether or not the specified snapshot is restorable. 

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.BackupApi();
let verificationParameters = new RubrikRestApi.VerificationParameters(); // VerificationParameters | Parameters needed to schedule a snapshot verification job. 
apiInstance.verifySnapshot(verificationParameters, (error, data, response) => {
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
 **verificationParameters** | [**VerificationParameters**](VerificationParameters.md)| Parameters needed to schedule a snapshot verification job.  | 

### Return type

[**VerificationResponse**](VerificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

