# RubrikRestApi.JobMonitoringApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createMonitoringSubscription**](JobMonitoringApi.md#createMonitoringSubscription) | **POST** /job_monitoring/subscription | Create an email subscription to the job monitoring page
[**deleteMonitoringSubscription**](JobMonitoringApi.md#deleteMonitoringSubscription) | **DELETE** /job_monitoring/subscription/{subscription_id} | Delete a monitoring page email subscription
[**getJobMonitoringInfo**](JobMonitoringApi.md#getJobMonitoringInfo) | **GET** /job_monitoring | Get job monitoring information
[**getJobMonitoringInfoCsvDownloadLink**](JobMonitoringApi.md#getJobMonitoringInfoCsvDownloadLink) | **GET** /job_monitoring/csv_download_link | Download job monitoring information as a CSV file
[**getMonitoringJobCountByJobState**](JobMonitoringApi.md#getMonitoringJobCountByJobState) | **GET** /job_monitoring/summary_by_job_state | Get job monitoring summary information separated by job state
[**getMonitoringJobCountByJobType**](JobMonitoringApi.md#getMonitoringJobCountByJobType) | **GET** /job_monitoring/summary_by_job_type | Get job monitoring summary information separated by job type
[**getMonitoringSubscription**](JobMonitoringApi.md#getMonitoringSubscription) | **GET** /job_monitoring/subscription/{subscription_id} | Get a specific monitoring email subscription by id
[**getMonitoringSubscriptions**](JobMonitoringApi.md#getMonitoringSubscriptions) | **GET** /job_monitoring/subscription | Returns all email subscriptions for the monitoring page
[**updateMonitoringSubscription**](JobMonitoringApi.md#updateMonitoringSubscription) | **PATCH** /job_monitoring/subscription/{subscription_id} | Update a monitoring email subscription



## createMonitoringSubscription

> MonitoringSubscriptionSummary createMonitoringSubscription(monitoringEmailSubscriptionRequest)

Create an email subscription to the job monitoring page

Creates an email subscription to the job monitoring page, which provides information on jobs based on their type (active, in progress, canceled, scheduled, or succeeded). Users can choose which job states to include in the subscription. The email summarizes the job counts by type in the body, and includes the option to include CSV attachments for every job state selected.

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

let apiInstance = new RubrikRestApi.JobMonitoringApi();
let monitoringEmailSubscriptionRequest = new RubrikRestApi.MonitoringEmailSubscriptionRequest(); // MonitoringEmailSubscriptionRequest | All information required to create a job-monitoring email subscription.
apiInstance.createMonitoringSubscription(monitoringEmailSubscriptionRequest, (error, data, response) => {
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
 **monitoringEmailSubscriptionRequest** | [**MonitoringEmailSubscriptionRequest**](MonitoringEmailSubscriptionRequest.md)| All information required to create a job-monitoring email subscription. | 

### Return type

[**MonitoringSubscriptionSummary**](MonitoringSubscriptionSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteMonitoringSubscription

> deleteMonitoringSubscription(subscriptionId)

Delete a monitoring page email subscription

Deletes the specified monitoring page email subscription.

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

let apiInstance = new RubrikRestApi.JobMonitoringApi();
let subscriptionId = "subscriptionId_example"; // String | ID of the monitoring subscription to delete.
apiInstance.deleteMonitoringSubscription(subscriptionId, (error, data, response) => {
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
 **subscriptionId** | **String**| ID of the monitoring subscription to delete. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getJobMonitoringInfo

> JobMonitoringResponse getJobMonitoringInfo(opts)

Get job monitoring information

Get the job summary for protection and recovery jobs that are currently running, scheduled to run, or completed in the past 24 hours.

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

let apiInstance = new RubrikRestApi.JobMonitoringApi();
let opts = {
  'limit': 56, // Number | Maximum number of entries to retrieve. The default value is 25. Value needs to be a positive number.
  'jobEventStatus': ["null"], // [String] | Filters results by the current event status of the job. The filters should be separated by ','.
  'jobType': "jobType_example", // String | Filters results by job type.
  'shouldIncludeLogRelatedJob': true, // Boolean | A Boolean that specifies whether or not to include log- related jobs. Default value is 'false'.
  'isFirstFull': true, // Boolean | Filter results by first full status.
  'objectType': "objectType_example", // String | Filters results by a specified object type.
  'objectName': "objectName_example", // String | Filters results by the provided value for object_name, using infix search.
  'nodeName': "nodeName_example", // String | Filter results by node name.
  'effectiveSlaDomainId': "effectiveSlaDomainId_example", // String | Filters results by the provided sla doimain id.
  'isOnDemand': true, // Boolean | Filters results according to their on-demand status.
  'lastUpdateTime': new Date("2013-10-20T19:20:30+01:00"), // Date | All rows updated at or after this time will be returned.
  'afterId': "afterId_example", // String | Fetches all rows after given row cursor.
  'sortBy': "sortBy_example", // String | The column by which to sort the entries.
  'sortOrder': "sortOrder_example" // String | The sorting order.
};
apiInstance.getJobMonitoringInfo(opts, (error, data, response) => {
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
 **limit** | **Number**| Maximum number of entries to retrieve. The default value is 25. Value needs to be a positive number. | [optional] 
 **jobEventStatus** | [**[String]**](String.md)| Filters results by the current event status of the job. The filters should be separated by &#39;,&#39;. | [optional] 
 **jobType** | **String**| Filters results by job type. | [optional] 
 **shouldIncludeLogRelatedJob** | **Boolean**| A Boolean that specifies whether or not to include log- related jobs. Default value is &#39;false&#39;. | [optional] 
 **isFirstFull** | **Boolean**| Filter results by first full status. | [optional] 
 **objectType** | **String**| Filters results by a specified object type. | [optional] 
 **objectName** | **String**| Filters results by the provided value for object_name, using infix search. | [optional] 
 **nodeName** | **String**| Filter results by node name. | [optional] 
 **effectiveSlaDomainId** | **String**| Filters results by the provided sla doimain id. | [optional] 
 **isOnDemand** | **Boolean**| Filters results according to their on-demand status. | [optional] 
 **lastUpdateTime** | **Date**| All rows updated at or after this time will be returned. | [optional] 
 **afterId** | **String**| Fetches all rows after given row cursor. | [optional] 
 **sortBy** | **String**| The column by which to sort the entries. | [optional] 
 **sortOrder** | **String**| The sorting order. | [optional] 

### Return type

[**JobMonitoringResponse**](JobMonitoringResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getJobMonitoringInfoCsvDownloadLink

> JobMonitoringCsvDownloadResponse getJobMonitoringInfoCsvDownloadLink(jobMonitoringState, opts)

Download job monitoring information as a CSV file

Download the job summary for protection and recovery jobs that are currently running, scheduled to run, or completed in the past 24 hours as a CSV file. This is a synchronous operation.

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

let apiInstance = new RubrikRestApi.JobMonitoringApi();
let jobMonitoringState = "jobMonitoringState_example"; // String | State of the jobs in the CSV.
let opts = {
  'jobEventStatus': "jobEventStatus_example", // String | Filters results by the current event status of the job.
  'jobType': "jobType_example", // String | Filters results by job type.
  'shouldIncludeLogRelatedJob': true, // Boolean | A Boolean that specifies whether or not to include log- related jobs. Default value is 'false'.
  'objectType': "objectType_example", // String | Filters results by a specified object type.
  'objectName': "objectName_example" // String | Filters results by the provided value for object_name, using infix search.
};
apiInstance.getJobMonitoringInfoCsvDownloadLink(jobMonitoringState, opts, (error, data, response) => {
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
 **jobMonitoringState** | **String**| State of the jobs in the CSV. | 
 **jobEventStatus** | **String**| Filters results by the current event status of the job. | [optional] 
 **jobType** | **String**| Filters results by job type. | [optional] 
 **shouldIncludeLogRelatedJob** | **Boolean**| A Boolean that specifies whether or not to include log- related jobs. Default value is &#39;false&#39;. | [optional] 
 **objectType** | **String**| Filters results by a specified object type. | [optional] 
 **objectName** | **String**| Filters results by the provided value for object_name, using infix search. | [optional] 

### Return type

[**JobMonitoringCsvDownloadResponse**](JobMonitoringCsvDownloadResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMonitoringJobCountByJobState

> JobMonitoringSummaryByState getMonitoringJobCountByJobState(opts)

Get job monitoring summary information separated by job state

Get job summary separated by job state for all running jobs, jobs that have been scheduled and jobs that are complete, for protection and recovery jobs in the past 24 hours.

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

let apiInstance = new RubrikRestApi.JobMonitoringApi();
let opts = {
  'jobTypes': ["null"] // [String] | Filter by a comma separated list of job types.
};
apiInstance.getMonitoringJobCountByJobState(opts, (error, data, response) => {
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
 **jobTypes** | [**[String]**](String.md)| Filter by a comma separated list of job types. | [optional] 

### Return type

[**JobMonitoringSummaryByState**](JobMonitoringSummaryByState.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMonitoringJobCountByJobType

> JobMonitoringSummaryByType getMonitoringJobCountByJobType(jobMonitoringState)

Get job monitoring summary information separated by job type

Get job summaries for protection and recovery jobs, separated by job type, that have been scheduled, are currently running, or completed in the past 24 hours.

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

let apiInstance = new RubrikRestApi.JobMonitoringApi();
let jobMonitoringState = "jobMonitoringState_example"; // String | Filter by job state.
apiInstance.getMonitoringJobCountByJobType(jobMonitoringState, (error, data, response) => {
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
 **jobMonitoringState** | **String**| Filter by job state. | 

### Return type

[**JobMonitoringSummaryByType**](JobMonitoringSummaryByType.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMonitoringSubscription

> MonitoringSubscriptionSummary getMonitoringSubscription(subscriptionId)

Get a specific monitoring email subscription by id

Returns a summary of the provided monitoring subscription.

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

let apiInstance = new RubrikRestApi.JobMonitoringApi();
let subscriptionId = "subscriptionId_example"; // String | ID of the monitoring subscription to acquire.
apiInstance.getMonitoringSubscription(subscriptionId, (error, data, response) => {
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
 **subscriptionId** | **String**| ID of the monitoring subscription to acquire. | 

### Return type

[**MonitoringSubscriptionSummary**](MonitoringSubscriptionSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMonitoringSubscriptions

> [MonitoringSubscriptionSummary] getMonitoringSubscriptions()

Returns all email subscriptions for the monitoring page

Return all unarchived email subscriptions for monitoring page in a list of summaries sorted by creation time (earliest created first). Each summary contains information for each subscription -- Time attributes - when to send the email -- Email addresses - who to send the email -- Attachments - what attachments should the email include -- Job states - which job states to include in the email (Failure, Scheduled, Success, Active, Canceled). -- Id - the tring that identifies the subscription -- Status - the status of the subscription (Active, Suspended, or Unknown) -- Owner - information about the owner of the subscription -- user id - unique id used to identify the owner -- user name - human-readable name of user the time schedule to send the subscription.

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

let apiInstance = new RubrikRestApi.JobMonitoringApi();
apiInstance.getMonitoringSubscriptions((error, data, response) => {
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

[**[MonitoringSubscriptionSummary]**](MonitoringSubscriptionSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateMonitoringSubscription

> MonitoringSubscriptionSummary updateMonitoringSubscription(subscriptionId, monitoringEmailSubscriptionUpdate)

Update a monitoring email subscription

Updates the monitoring email subscription with the subscription ID provided.

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

let apiInstance = new RubrikRestApi.JobMonitoringApi();
let subscriptionId = "subscriptionId_example"; // String | ID of the monitoring subscription.
let monitoringEmailSubscriptionUpdate = new RubrikRestApi.MonitoringEmailSubscriptionUpdate(); // MonitoringEmailSubscriptionUpdate | Information required to update a monitoring subscription.
apiInstance.updateMonitoringSubscription(subscriptionId, monitoringEmailSubscriptionUpdate, (error, data, response) => {
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
 **subscriptionId** | **String**| ID of the monitoring subscription. | 
 **monitoringEmailSubscriptionUpdate** | [**MonitoringEmailSubscriptionUpdate**](MonitoringEmailSubscriptionUpdate.md)| Information required to update a monitoring subscription. | 

### Return type

[**MonitoringSubscriptionSummary**](MonitoringSubscriptionSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

