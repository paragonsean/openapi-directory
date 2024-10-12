# WireMock.RecordingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adminRecordingsSnapshotPost**](RecordingsApi.md#adminRecordingsSnapshotPost) | **POST** /__admin/recordings/snapshot | Take a snapshot recording
[**adminRecordingsStartPost**](RecordingsApi.md#adminRecordingsStartPost) | **POST** /__admin/recordings/start | Start recording
[**adminRecordingsStatusGet**](RecordingsApi.md#adminRecordingsStatusGet) | **GET** /__admin/recordings/status | Get recording status
[**adminRecordingsStopPost**](RecordingsApi.md#adminRecordingsStopPost) | **POST** /__admin/recordings/stop | Stop recording



## adminRecordingsSnapshotPost

> AdminMappingsGet200Response adminRecordingsSnapshotPost(adminRecordingsSnapshotPostRequest)

Take a snapshot recording

### Example

```javascript
import WireMock from 'wire_mock';

let apiInstance = new WireMock.RecordingsApi();
let adminRecordingsSnapshotPostRequest = {"captureHeaders":{"Accept":{},"Content-Type":{"caseInsensitive":true}},"extractBodyCriteria":{"binarySizeThreshold":"1 Mb","textSizeThreshold":"2 kb"},"filters":{"ids":["40a93c4a-d378-4e07-8321-6158d5dbcb29"],"method":"GET","urlPathPattern":"/api/.*"},"outputFormat":"FULL","persist":false,"repeatsAsScenarios":false,"requestBodyPattern":{"ignoreArrayOrder":false,"ignoreExtraElements":true,"matcher":"equalToJson"},"transformerParameters":{"headerValue":"123"},"transformers":["modify-response-header"]}; // AdminRecordingsSnapshotPostRequest | 
apiInstance.adminRecordingsSnapshotPost(adminRecordingsSnapshotPostRequest, (error, data, response) => {
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
 **adminRecordingsSnapshotPostRequest** | [**AdminRecordingsSnapshotPostRequest**](AdminRecordingsSnapshotPostRequest.md)|  | 

### Return type

[**AdminMappingsGet200Response**](AdminMappingsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## adminRecordingsStartPost

> adminRecordingsStartPost(adminRecordingsStartPostRequest)

Start recording

Begin recording stub mappings

### Example

```javascript
import WireMock from 'wire_mock';

let apiInstance = new WireMock.RecordingsApi();
let adminRecordingsStartPostRequest = {"captureHeaders":{"Accept":{},"Content-Type":{"caseInsensitive":true}},"extractBodyCriteria":{"binarySizeThreshold":"10240","textSizeThreshold":"2048"},"filters":{"method":"GET","urlPathPattern":"/api/.*"},"persist":false,"repeatsAsScenarios":false,"requestBodyPattern":{"ignoreArrayOrder":false,"ignoreExtraElements":true,"matcher":"equalToJson"},"targetBaseUrl":"http://example.mocklab.io","transformerParameters":{"headerValue":"123"},"transformers":["modify-response-header"]}; // AdminRecordingsStartPostRequest | 
apiInstance.adminRecordingsStartPost(adminRecordingsStartPostRequest, (error, data, response) => {
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
 **adminRecordingsStartPostRequest** | [**AdminRecordingsStartPostRequest**](AdminRecordingsStartPostRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## adminRecordingsStatusGet

> AdminRecordingsStatusGet200Response adminRecordingsStatusGet()

Get recording status

### Example

```javascript
import WireMock from 'wire_mock';

let apiInstance = new WireMock.RecordingsApi();
apiInstance.adminRecordingsStatusGet((error, data, response) => {
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

[**AdminRecordingsStatusGet200Response**](AdminRecordingsStatusGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## adminRecordingsStopPost

> AdminMappingsGet200Response adminRecordingsStopPost()

Stop recording

End recording of stub mappings

### Example

```javascript
import WireMock from 'wire_mock';

let apiInstance = new WireMock.RecordingsApi();
apiInstance.adminRecordingsStopPost((error, data, response) => {
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

[**AdminMappingsGet200Response**](AdminMappingsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

