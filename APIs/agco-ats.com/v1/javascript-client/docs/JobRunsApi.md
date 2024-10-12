# AgcoApi.JobRunsApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jobRunsDeleteJobRun**](JobRunsApi.md#jobRunsDeleteJobRun) | **DELETE** /api/v2/jobRuns/{jobRunID} | Delete a JobRun
[**jobRunsGetJobRun**](JobRunsApi.md#jobRunsGetJobRun) | **GET** /api/v2/jobRuns/{jobRunID} | Get a JobRun by ID
[**jobRunsGetJobRuns**](JobRunsApi.md#jobRunsGetJobRuns) | **GET** /api/v2/jobRuns | Get JobRuns
[**jobRunsPostJobRun**](JobRunsApi.md#jobRunsPostJobRun) | **POST** /api/v2/jobRuns | Create a JobRun
[**jobRunsPutJobRun**](JobRunsApi.md#jobRunsPutJobRun) | **PUT** /api/v2/jobRuns/{jobRunID} | Update a JobRun



## jobRunsDeleteJobRun

> jobRunsDeleteJobRun(jobRunID)

Delete a JobRun

Deletes a JobRun. When successful, the response is empty.  If unsuccessful, an appropriate              ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.JobRunsApi();
let jobRunID = 56; // Number | The id of the JobRun to delete
apiInstance.jobRunsDeleteJobRun(jobRunID, (error, data, response) => {
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
 **jobRunID** | **Number**| The id of the JobRun to delete | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## jobRunsGetJobRun

> BuildSystemSharedDTOJobRun jobRunsGetJobRun(jobRunID, opts)

Get a JobRun by ID

Gets a JobRun by ID. When successful, the response is the requested JobRun.              If unsuccessful, an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.JobRunsApi();
let jobRunID = 56; // Number | The ID of the JobRun to get.
let opts = {
  'includeActivityRunDetails': true // Boolean | Optional. Indicates whether to include ActivityRun details.  Defaults to false.
};
apiInstance.jobRunsGetJobRun(jobRunID, opts, (error, data, response) => {
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
 **jobRunID** | **Number**| The ID of the JobRun to get. | 
 **includeActivityRunDetails** | **Boolean**| Optional. Indicates whether to include ActivityRun details.  Defaults to false. | [optional] 

### Return type

[**BuildSystemSharedDTOJobRun**](BuildSystemSharedDTOJobRun.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## jobRunsGetJobRuns

> APIPagedResponseBuildSystemSharedDTOJobRun jobRunsGetJobRuns(opts)

Get JobRuns

Gets a collection of JobRuns. When successful, the response is a PagedResponse of JobRuns.              If unsuccessful, an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.JobRunsApi();
let opts = {
  'limit': 56, // Number | Optional. The page limit.  If not specified, the default page limit is 10.
  'offset': 56, // Number | Optional. The page offset.  If not specified, the default page offset is 0.
  'includeActivityRunDetails': true // Boolean | Optional. Indicates whether to include ActivityRun details.  Defaults to false.
};
apiInstance.jobRunsGetJobRuns(opts, (error, data, response) => {
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
 **includeActivityRunDetails** | **Boolean**| Optional. Indicates whether to include ActivityRun details.  Defaults to false. | [optional] 

### Return type

[**APIPagedResponseBuildSystemSharedDTOJobRun**](APIPagedResponseBuildSystemSharedDTOJobRun.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## jobRunsPostJobRun

> Number jobRunsPostJobRun(buildSystemSharedDTOJobRun)

Create a JobRun

Creates a JobRun.  The body of the POST is the JobRun to create.  The JobRunID will be assigned on              creation of the JobRun.  When successful, the response is the JobRunID.  If unsuccessful, an               appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.JobRunsApi();
let buildSystemSharedDTOJobRun = new AgcoApi.BuildSystemSharedDTOJobRun(); // BuildSystemSharedDTOJobRun | The JobRun to create.  The JobRunID will be assigned on creation of the JobRun.
apiInstance.jobRunsPostJobRun(buildSystemSharedDTOJobRun, (error, data, response) => {
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
 **buildSystemSharedDTOJobRun** | [**BuildSystemSharedDTOJobRun**](BuildSystemSharedDTOJobRun.md)| The JobRun to create.  The JobRunID will be assigned on creation of the JobRun. | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## jobRunsPutJobRun

> jobRunsPutJobRun(jobRunID, buildSystemSharedDTOJobRun)

Update a JobRun

///               Updates a JobRun.  The body of the PUT is the updated JobRun.              When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.JobRunsApi();
let jobRunID = 56; // Number | The id of the JobRun to update
let buildSystemSharedDTOJobRun = new AgcoApi.BuildSystemSharedDTOJobRun(); // BuildSystemSharedDTOJobRun | The updated JobRun
apiInstance.jobRunsPutJobRun(jobRunID, buildSystemSharedDTOJobRun, (error, data, response) => {
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
 **jobRunID** | **Number**| The id of the JobRun to update | 
 **buildSystemSharedDTOJobRun** | [**BuildSystemSharedDTOJobRun**](BuildSystemSharedDTOJobRun.md)| The updated JobRun | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*

