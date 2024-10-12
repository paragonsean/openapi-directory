# GoToTraining.RecordingsApi

All URIs are relative to *https://api.getgo.com/G2T/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getRecordingDownloadById**](RecordingsApi.md#getRecordingDownloadById) | **GET** /trainings/{trainingKey}/recordings/{recordingId} | Get Download for Online Recordings
[**getRecordingsForTraining**](RecordingsApi.md#getRecordingsForTraining) | **GET** /trainings/{trainingKey}/recordings | Get Online Recordings for Training



## getRecordingDownloadById

> getRecordingDownloadById(authorization, trainingKey, recordingId)

Get Download for Online Recordings

This call provides the download for the given recording by returning a 302 redirect to the original file.

### Example

```javascript
import GoToTraining from 'go_to_training';

let apiInstance = new GoToTraining.RecordingsApi();
let authorization = "authorization_example"; // String | Access token
let trainingKey = 789; // Number | The key of the training
let recordingId = 789; // Number | the unique id of the recording
apiInstance.getRecordingDownloadById(authorization, trainingKey, recordingId, (error, data, response) => {
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
 **authorization** | **String**| Access token | 
 **trainingKey** | **Number**| The key of the training | 
 **recordingId** | **Number**| the unique id of the recording | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getRecordingsForTraining

> RecordingsListForTraining getRecordingsForTraining(authorization, trainingKey)

Get Online Recordings for Training

This call retrieves information on all online recordings for a given training. If there are none, it returns an empty list.

### Example

```javascript
import GoToTraining from 'go_to_training';

let apiInstance = new GoToTraining.RecordingsApi();
let authorization = "authorization_example"; // String | Access token
let trainingKey = 789; // Number | The key of the training
apiInstance.getRecordingsForTraining(authorization, trainingKey, (error, data, response) => {
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
 **authorization** | **String**| Access token | 
 **trainingKey** | **Number**| The key of the training | 

### Return type

[**RecordingsListForTraining**](RecordingsListForTraining.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

