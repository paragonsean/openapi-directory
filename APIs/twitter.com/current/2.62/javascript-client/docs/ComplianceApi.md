# TwitterApiV2.ComplianceApi

All URIs are relative to *https://api.twitter.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createBatchComplianceJob**](ComplianceApi.md#createBatchComplianceJob) | **POST** /2/compliance/jobs | Create compliance job
[**getBatchComplianceJob**](ComplianceApi.md#getBatchComplianceJob) | **GET** /2/compliance/jobs/{id} | Get Compliance Job
[**getTweetsComplianceStream**](ComplianceApi.md#getTweetsComplianceStream) | **GET** /2/tweets/compliance/stream | Tweets Compliance stream
[**getTweetsLabelStream**](ComplianceApi.md#getTweetsLabelStream) | **GET** /2/tweets/label/stream | Tweets Label stream
[**getUsersComplianceStream**](ComplianceApi.md#getUsersComplianceStream) | **GET** /2/users/compliance/stream | Users Compliance stream
[**listBatchComplianceJobs**](ComplianceApi.md#listBatchComplianceJobs) | **GET** /2/compliance/jobs | List Compliance Jobs



## createBatchComplianceJob

> CreateComplianceJobResponse createBatchComplianceJob(createComplianceJobRequest)

Create compliance job

Creates a compliance for the given job type

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TwitterApiV2.ComplianceApi();
let createComplianceJobRequest = new TwitterApiV2.CreateComplianceJobRequest(); // CreateComplianceJobRequest | 
apiInstance.createBatchComplianceJob(createComplianceJobRequest, (error, data, response) => {
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
 **createComplianceJobRequest** | [**CreateComplianceJobRequest**](CreateComplianceJobRequest.md)|  | 

### Return type

[**CreateComplianceJobResponse**](CreateComplianceJobResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/problem+json


## getBatchComplianceJob

> Get2ComplianceJobsIdResponse getBatchComplianceJob(id, opts)

Get Compliance Job

Returns a single Compliance Job by ID

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TwitterApiV2.ComplianceApi();
let id = "id_example"; // String | The ID of the Compliance Job to retrieve.
let opts = {
  'complianceJobFields': ["null"] // [String] | A comma separated list of ComplianceJob fields to display.
};
apiInstance.getBatchComplianceJob(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the Compliance Job to retrieve. | 
 **complianceJobFields** | [**[String]**](String.md)| A comma separated list of ComplianceJob fields to display. | [optional] 

### Return type

[**Get2ComplianceJobsIdResponse**](Get2ComplianceJobsIdResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## getTweetsComplianceStream

> TweetComplianceStreamResponse getTweetsComplianceStream(partition, opts)

Tweets Compliance stream

Streams 100% of compliance data for Tweets

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TwitterApiV2.ComplianceApi();
let partition = 56; // Number | The partition number.
let opts = {
  'backfillMinutes': 56, // Number | The number of minutes of backfill requested.
  'startTime': new Date("2021-02-01T18:40:40.000Z"), // Date | YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Tweet Compliance events will be provided.
  'endTime': new Date("2021-02-14T18:40:40.000Z") // Date | YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Tweet Compliance events will be provided.
};
apiInstance.getTweetsComplianceStream(partition, opts, (error, data, response) => {
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
 **partition** | **Number**| The partition number. | 
 **backfillMinutes** | **Number**| The number of minutes of backfill requested. | [optional] 
 **startTime** | **Date**| YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Tweet Compliance events will be provided. | [optional] 
 **endTime** | **Date**| YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Tweet Compliance events will be provided. | [optional] 

### Return type

[**TweetComplianceStreamResponse**](TweetComplianceStreamResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## getTweetsLabelStream

> TweetLabelStreamResponse getTweetsLabelStream(opts)

Tweets Label stream

Streams 100% of labeling events applied to Tweets

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TwitterApiV2.ComplianceApi();
let opts = {
  'backfillMinutes': 56, // Number | The number of minutes of backfill requested.
  'startTime': new Date("2021-02-01T18:40:40.000Z"), // Date | YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Tweet labels will be provided.
  'endTime': new Date("2021-02-01T18:40:40.000Z") // Date | YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the Tweet labels will be provided.
};
apiInstance.getTweetsLabelStream(opts, (error, data, response) => {
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
 **backfillMinutes** | **Number**| The number of minutes of backfill requested. | [optional] 
 **startTime** | **Date**| YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Tweet labels will be provided. | [optional] 
 **endTime** | **Date**| YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the Tweet labels will be provided. | [optional] 

### Return type

[**TweetLabelStreamResponse**](TweetLabelStreamResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## getUsersComplianceStream

> UserComplianceStreamResponse getUsersComplianceStream(partition, opts)

Users Compliance stream

Streams 100% of compliance data for Users

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TwitterApiV2.ComplianceApi();
let partition = 56; // Number | The partition number.
let opts = {
  'backfillMinutes': 56, // Number | The number of minutes of backfill requested.
  'startTime': new Date("2021-02-01T18:40:40.000Z"), // Date | YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the User Compliance events will be provided.
  'endTime': new Date("2021-02-01T18:40:40.000Z") // Date | YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the User Compliance events will be provided.
};
apiInstance.getUsersComplianceStream(partition, opts, (error, data, response) => {
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
 **partition** | **Number**| The partition number. | 
 **backfillMinutes** | **Number**| The number of minutes of backfill requested. | [optional] 
 **startTime** | **Date**| YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the User Compliance events will be provided. | [optional] 
 **endTime** | **Date**| YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the User Compliance events will be provided. | [optional] 

### Return type

[**UserComplianceStreamResponse**](UserComplianceStreamResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## listBatchComplianceJobs

> Get2ComplianceJobsResponse listBatchComplianceJobs(type, opts)

List Compliance Jobs

Returns recent Compliance Jobs for a given job type and optional job status

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TwitterApiV2.ComplianceApi();
let type = "type_example"; // String | Type of Compliance Job to list.
let opts = {
  'status': "status_example", // String | Status of Compliance Job to list.
  'complianceJobFields': ["null"] // [String] | A comma separated list of ComplianceJob fields to display.
};
apiInstance.listBatchComplianceJobs(type, opts, (error, data, response) => {
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
 **type** | **String**| Type of Compliance Job to list. | 
 **status** | **String**| Status of Compliance Job to list. | [optional] 
 **complianceJobFields** | [**[String]**](String.md)| A comma separated list of ComplianceJob fields to display. | [optional] 

### Return type

[**Get2ComplianceJobsResponse**](Get2ComplianceJobsResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json

