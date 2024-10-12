# AirbyteConfigurationApi.InternalApi

All URIs are relative to *http://airbyte.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createOrUpdateState_0**](InternalApi.md#createOrUpdateState_0) | **POST** /v1/state/create_or_update | Create or update the state for a connection.
[**getAttemptNormalizationStatusesForJob_0**](InternalApi.md#getAttemptNormalizationStatusesForJob_0) | **POST** /v1/jobs/get_normalization_status | Get normalization status to determine if we can bypass normalization phase
[**saveStats_0**](InternalApi.md#saveStats_0) | **POST** /v1/attempt/save_stats | For worker to set sync stats of a running attempt.
[**saveSyncConfig_0**](InternalApi.md#saveSyncConfig_0) | **POST** /v1/attempt/save_sync_config | For worker to save the AttemptSyncConfig for an attempt.
[**setWorkflowInAttempt_0**](InternalApi.md#setWorkflowInAttempt_0) | **POST** /v1/attempt/set_workflow_in_attempt | For worker to register the workflow id in attempt.
[**writeDiscoverCatalogResult_0**](InternalApi.md#writeDiscoverCatalogResult_0) | **POST** /v1/sources/write_discover_catalog_result | Should only called from worker, to write result from discover activity back to DB.



## createOrUpdateState_0

> ConnectionState createOrUpdateState_0(connectionStateCreateOrUpdate)

Create or update the state for a connection.

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.InternalApi();
let connectionStateCreateOrUpdate = new AirbyteConfigurationApi.ConnectionStateCreateOrUpdate(); // ConnectionStateCreateOrUpdate | 
apiInstance.createOrUpdateState_0(connectionStateCreateOrUpdate, (error, data, response) => {
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
 **connectionStateCreateOrUpdate** | [**ConnectionStateCreateOrUpdate**](ConnectionStateCreateOrUpdate.md)|  | 

### Return type

[**ConnectionState**](ConnectionState.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAttemptNormalizationStatusesForJob_0

> AttemptNormalizationStatusReadList getAttemptNormalizationStatusesForJob_0(opts)

Get normalization status to determine if we can bypass normalization phase

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.InternalApi();
let opts = {
  'jobIdRequestBody': new AirbyteConfigurationApi.JobIdRequestBody() // JobIdRequestBody | 
};
apiInstance.getAttemptNormalizationStatusesForJob_0(opts, (error, data, response) => {
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
 **jobIdRequestBody** | [**JobIdRequestBody**](JobIdRequestBody.md)|  | [optional] 

### Return type

[**AttemptNormalizationStatusReadList**](AttemptNormalizationStatusReadList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## saveStats_0

> InternalOperationResult saveStats_0(saveStatsRequestBody)

For worker to set sync stats of a running attempt.

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.InternalApi();
let saveStatsRequestBody = new AirbyteConfigurationApi.SaveStatsRequestBody(); // SaveStatsRequestBody | 
apiInstance.saveStats_0(saveStatsRequestBody, (error, data, response) => {
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


## saveSyncConfig_0

> InternalOperationResult saveSyncConfig_0(saveAttemptSyncConfigRequestBody)

For worker to save the AttemptSyncConfig for an attempt.

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.InternalApi();
let saveAttemptSyncConfigRequestBody = new AirbyteConfigurationApi.SaveAttemptSyncConfigRequestBody(); // SaveAttemptSyncConfigRequestBody | 
apiInstance.saveSyncConfig_0(saveAttemptSyncConfigRequestBody, (error, data, response) => {
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


## setWorkflowInAttempt_0

> InternalOperationResult setWorkflowInAttempt_0(setWorkflowInAttemptRequestBody)

For worker to register the workflow id in attempt.

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.InternalApi();
let setWorkflowInAttemptRequestBody = new AirbyteConfigurationApi.SetWorkflowInAttemptRequestBody(); // SetWorkflowInAttemptRequestBody | 
apiInstance.setWorkflowInAttempt_0(setWorkflowInAttemptRequestBody, (error, data, response) => {
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


## writeDiscoverCatalogResult_0

> DiscoverCatalogResult writeDiscoverCatalogResult_0(sourceDiscoverSchemaWriteRequestBody)

Should only called from worker, to write result from discover activity back to DB.

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.InternalApi();
let sourceDiscoverSchemaWriteRequestBody = new AirbyteConfigurationApi.SourceDiscoverSchemaWriteRequestBody(); // SourceDiscoverSchemaWriteRequestBody | 
apiInstance.writeDiscoverCatalogResult_0(sourceDiscoverSchemaWriteRequestBody, (error, data, response) => {
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
 **sourceDiscoverSchemaWriteRequestBody** | [**SourceDiscoverSchemaWriteRequestBody**](SourceDiscoverSchemaWriteRequestBody.md)|  | 

### Return type

[**DiscoverCatalogResult**](DiscoverCatalogResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

