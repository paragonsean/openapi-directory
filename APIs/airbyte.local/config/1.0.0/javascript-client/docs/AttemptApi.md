# AirbyteConfigurationApi.AttemptApi

All URIs are relative to *http://airbyte.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**saveStats**](AttemptApi.md#saveStats) | **POST** /v1/attempt/save_stats | For worker to set sync stats of a running attempt.
[**saveSyncConfig**](AttemptApi.md#saveSyncConfig) | **POST** /v1/attempt/save_sync_config | For worker to save the AttemptSyncConfig for an attempt.
[**setWorkflowInAttempt**](AttemptApi.md#setWorkflowInAttempt) | **POST** /v1/attempt/set_workflow_in_attempt | For worker to register the workflow id in attempt.



## saveStats

> InternalOperationResult saveStats(saveStatsRequestBody)

For worker to set sync stats of a running attempt.

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.AttemptApi();
let saveStatsRequestBody = new AirbyteConfigurationApi.SaveStatsRequestBody(); // SaveStatsRequestBody | 
apiInstance.saveStats(saveStatsRequestBody, (error, data, response) => {
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
 **saveStatsRequestBody** | [**SaveStatsRequestBody**](SaveStatsRequestBody.md)|  | 

### Return type

[**InternalOperationResult**](InternalOperationResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## saveSyncConfig

> InternalOperationResult saveSyncConfig(saveAttemptSyncConfigRequestBody)

For worker to save the AttemptSyncConfig for an attempt.

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.AttemptApi();
let saveAttemptSyncConfigRequestBody = new AirbyteConfigurationApi.SaveAttemptSyncConfigRequestBody(); // SaveAttemptSyncConfigRequestBody | 
apiInstance.saveSyncConfig(saveAttemptSyncConfigRequestBody, (error, data, response) => {
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
 **saveAttemptSyncConfigRequestBody** | [**SaveAttemptSyncConfigRequestBody**](SaveAttemptSyncConfigRequestBody.md)|  | 

### Return type

[**InternalOperationResult**](InternalOperationResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setWorkflowInAttempt

> InternalOperationResult setWorkflowInAttempt(setWorkflowInAttemptRequestBody)

For worker to register the workflow id in attempt.

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.AttemptApi();
let setWorkflowInAttemptRequestBody = new AirbyteConfigurationApi.SetWorkflowInAttemptRequestBody(); // SetWorkflowInAttemptRequestBody | 
apiInstance.setWorkflowInAttempt(setWorkflowInAttemptRequestBody, (error, data, response) => {
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
 **setWorkflowInAttemptRequestBody** | [**SetWorkflowInAttemptRequestBody**](SetWorkflowInAttemptRequestBody.md)|  | 

### Return type

[**InternalOperationResult**](InternalOperationResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

