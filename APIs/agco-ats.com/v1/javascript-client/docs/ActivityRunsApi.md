# AgcoApi.ActivityRunsApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activityRunsGetActivityRun**](ActivityRunsApi.md#activityRunsGetActivityRun) | **GET** /api/v2/activityRuns/{activityRunID} | Get an ActivityRun by ID
[**activityRunsGetActivityRunStatus**](ActivityRunsApi.md#activityRunsGetActivityRunStatus) | **GET** /api/v2/activityRuns/{activityRunID}/status | Get the ActivityRunStatus of an ActivityRun
[**activityRunsGetActivityRuns**](ActivityRunsApi.md#activityRunsGetActivityRuns) | **GET** /api/v2/activityRuns | Get ActivityRuns
[**activityRunsPutActivityRun**](ActivityRunsApi.md#activityRunsPutActivityRun) | **PUT** /api/v2/activityRuns/{activityRunID} | Update an ActivityRun
[**activityRunsPutActivityRunStatus**](ActivityRunsApi.md#activityRunsPutActivityRunStatus) | **PUT** /api/v2/activityRuns/{activityRunID}/status | Update the ActivityRunStatus of an ActivityRun



## activityRunsGetActivityRun

> BuildSystemSharedDTOActivityRun activityRunsGetActivityRun(activityRunID)

Get an ActivityRun by ID

Gets an ActivityRun by ID. When successful, the response is the requested ActivityRun.  If unsuccessful,              an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ActivityRunsApi();
let activityRunID = 56; // Number | The ID of the ActivityRun to get.
apiInstance.activityRunsGetActivityRun(activityRunID, (error, data, response) => {
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
 **activityRunID** | **Number**| The ID of the ActivityRun to get. | 

### Return type

[**BuildSystemSharedDTOActivityRun**](BuildSystemSharedDTOActivityRun.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## activityRunsGetActivityRunStatus

> BuildSystemSharedDTOActivityRunStatus activityRunsGetActivityRunStatus(activityRunID)

Get the ActivityRunStatus of an ActivityRun

Gets the ActivityRunStatus of an ActivityRun.  When successful, the response is the requested ActivityRunStatus.              If unsuccessful, an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ActivityRunsApi();
let activityRunID = 56; // Number | The ID of the ActivityRun to get ActivityRunStatus for.
apiInstance.activityRunsGetActivityRunStatus(activityRunID, (error, data, response) => {
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
 **activityRunID** | **Number**| The ID of the ActivityRun to get ActivityRunStatus for. | 

### Return type

[**BuildSystemSharedDTOActivityRunStatus**](BuildSystemSharedDTOActivityRunStatus.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## activityRunsGetActivityRuns

> APIPagedResponseBuildSystemSharedDTOActivityRun activityRunsGetActivityRuns(opts)

Get ActivityRuns

Gets a collection of ActivityRuns. When successful, the response is a PagedResponse of ActivityRuns.                If unsuccessful, an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ActivityRunsApi();
let opts = {
  'limit': 56, // Number | Optional. The page limit.  If not specified, the default page limit is 10.
  'offset': 56, // Number | Optional. The page offset.  If not specified, the default page offset is 0.
  'status': "status_example" // String | Optional. Filter activity runs by status.  Value should be a comma separated list of status to include.              If not specified, the default status filter is “InProgress”.
};
apiInstance.activityRunsGetActivityRuns(opts, (error, data, response) => {
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
 **limit** | **Number**| Optional. The page limit.  If not specified, the default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset.  If not specified, the default page offset is 0. | [optional] 
 **status** | **String**| Optional. Filter activity runs by status.  Value should be a comma separated list of status to include.              If not specified, the default status filter is “InProgress”. | [optional] 

### Return type

[**APIPagedResponseBuildSystemSharedDTOActivityRun**](APIPagedResponseBuildSystemSharedDTOActivityRun.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## activityRunsPutActivityRun

> activityRunsPutActivityRun(activityRunID, buildSystemSharedDTOActivityRun)

Update an ActivityRun

Updates the ActivityRunStatus of an ActivityRun.  The body of the PUT is the updated ActivityRunStatus.              When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ActivityRunsApi();
let activityRunID = 56; // Number | The ID of the ActivityRun to update ActivityRunStatus for.
let buildSystemSharedDTOActivityRun = new AgcoApi.BuildSystemSharedDTOActivityRun(); // BuildSystemSharedDTOActivityRun | The updated ActivityRun.
apiInstance.activityRunsPutActivityRun(activityRunID, buildSystemSharedDTOActivityRun, (error, data, response) => {
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
 **activityRunID** | **Number**| The ID of the ActivityRun to update ActivityRunStatus for. | 
 **buildSystemSharedDTOActivityRun** | [**BuildSystemSharedDTOActivityRun**](BuildSystemSharedDTOActivityRun.md)| The updated ActivityRun. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*


## activityRunsPutActivityRunStatus

> activityRunsPutActivityRunStatus(activityRunID, buildSystemSharedDTOActivityRunStatus)

Update the ActivityRunStatus of an ActivityRun

Updates the ActivityRunStatus of an ActivityRun.  The body of the PUT is the updated ActivityRunStatus.              When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ActivityRunsApi();
let activityRunID = 56; // Number | The ID of the ActivityRun to update ActivityRunStatus for.
let buildSystemSharedDTOActivityRunStatus = new AgcoApi.BuildSystemSharedDTOActivityRunStatus(); // BuildSystemSharedDTOActivityRunStatus | The updated ActivityRunStatus.
apiInstance.activityRunsPutActivityRunStatus(activityRunID, buildSystemSharedDTOActivityRunStatus, (error, data, response) => {
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
 **activityRunID** | **Number**| The ID of the ActivityRun to update ActivityRunStatus for. | 
 **buildSystemSharedDTOActivityRunStatus** | [**BuildSystemSharedDTOActivityRunStatus**](BuildSystemSharedDTOActivityRunStatus.md)| The updated ActivityRunStatus. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*

