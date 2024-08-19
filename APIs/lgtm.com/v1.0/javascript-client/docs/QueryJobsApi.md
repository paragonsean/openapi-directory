# LgtmApiSpecification.QueryJobsApi

All URIs are relative to *https://lgtm.com/api/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createQueryJob**](QueryJobsApi.md#createQueryJob) | **POST** /queryjobs | Run a CodeQL query on one or more projects
[**getQueryJob**](QueryJobsApi.md#getQueryJob) | **GET** /queryjobs/{queryjob-id} | Get the status of a query job
[**getQueryJobResultsForProject**](QueryJobsApi.md#getQueryJobResultsForProject) | **GET** /queryjobs/{queryjob-id}/results/{project-id} | Fetch the results of a query job for a specific project
[**getQueryJobResultsOverview**](QueryJobsApi.md#getQueryJobResultsOverview) | **GET** /queryjobs/{queryjob-id}/results | Provide a summary of results for the projects in the query job



## createQueryJob

> Operation createQueryJob(language, body, opts)

Run a CodeQL query on one or more projects

Submit a query to run on one or more projects on LGTM. The query is included in the body of the request. 

### Example

```javascript
import LgtmApiSpecification from 'lgtm_api_specification';
let defaultClient = LgtmApiSpecification.ApiClient.instance;
// Configure Bearer access token for authorization: access-token
let access-token = defaultClient.authentications['access-token'];
access-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new LgtmApiSpecification.QueryJobsApi();
let language = "language_example"; // String | The [language](https://lgtm.com/help/lgtm/analysis-faqs#which-languages-are-supported) you want to analyze. 
let body = select "hello", "world"; // String | The query to run.
let opts = {
  'projectId': [null], // [Number] | The identifier of the project to analyze. Either `project-id` or `projects-list` must be specified.
  'projectsList': "projectsList_example" // String | Name of the list containing the projects to analyze. Either `project-id` or `projects-list` must be specified.
};
apiInstance.createQueryJob(language, body, opts, (error, data, response) => {
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
 **language** | **String**| The [language](https://lgtm.com/help/lgtm/analysis-faqs#which-languages-are-supported) you want to analyze.  | 
 **body** | **String**| The query to run. | 
 **projectId** | [**[Number]**](Number.md)| The identifier of the project to analyze. Either &#x60;project-id&#x60; or &#x60;projects-list&#x60; must be specified. | [optional] 
 **projectsList** | **String**| Name of the list containing the projects to analyze. Either &#x60;project-id&#x60; or &#x60;projects-list&#x60; must be specified. | [optional] 

### Return type

[**Operation**](Operation.md)

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: application/json


## getQueryJob

> Queryjob getQueryJob(queryjobId)

Get the status of a query job

Get the status of a query job using the query job identifier for the task.  When you create a query job, the response includes a task result URL of the form: &#x60;/queryjobs/{queryjob-id}&#x60;. 

### Example

```javascript
import LgtmApiSpecification from 'lgtm_api_specification';
let defaultClient = LgtmApiSpecification.ApiClient.instance;
// Configure Bearer access token for authorization: access-token
let access-token = defaultClient.authentications['access-token'];
access-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new LgtmApiSpecification.QueryJobsApi();
let queryjobId = "queryjobId_example"; // String | The identifier of the query job, from the `task-result` given in the response to the initial `POST /queryjobs` request.
apiInstance.getQueryJob(queryjobId, (error, data, response) => {
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
 **queryjobId** | **String**| The identifier of the query job, from the &#x60;task-result&#x60; given in the response to the initial &#x60;POST /queryjobs&#x60; request. | 

### Return type

[**Queryjob**](Queryjob.md)

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getQueryJobResultsForProject

> QueryjobProjectResults getQueryJobResultsForProject(queryjobId, projectId, opts)

Fetch the results of a query job for a specific project

Fetch the results for a specific project. The endpoint succeeds only if the query was successful,  and returns a &#x60;404&#x60; error otherwise.  By default, the endpoint provides only results that are within the source tree. To obtain all results, specify the &#x60;nofilter&#x60; parameter. 

### Example

```javascript
import LgtmApiSpecification from 'lgtm_api_specification';
let defaultClient = LgtmApiSpecification.ApiClient.instance;
// Configure Bearer access token for authorization: access-token
let access-token = defaultClient.authentications['access-token'];
access-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new LgtmApiSpecification.QueryJobsApi();
let queryjobId = "queryjobId_example"; // String | The identifier of the query job, from the `task-result` given in the response to the initial `POST /queryjobs` request.
let projectId = "projectId_example"; // String | The identifier for the project.
let opts = {
  'start': 56, // Number | Start point for the page of results.
  'limit': 100, // Number | The maximum number of results to display (less than 100).
  'nofilter': false // Boolean | Include results that are not part of the source tree. These results are filtered out by default.
};
apiInstance.getQueryJobResultsForProject(queryjobId, projectId, opts, (error, data, response) => {
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
 **queryjobId** | **String**| The identifier of the query job, from the &#x60;task-result&#x60; given in the response to the initial &#x60;POST /queryjobs&#x60; request. | 
 **projectId** | **String**| The identifier for the project. | 
 **start** | **Number**| Start point for the page of results. | [optional] 
 **limit** | **Number**| The maximum number of results to display (less than 100). | [optional] [default to 100]
 **nofilter** | **Boolean**| Include results that are not part of the source tree. These results are filtered out by default. | [optional] [default to false]

### Return type

[**QueryjobProjectResults**](QueryjobProjectResults.md)

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getQueryJobResultsOverview

> QueryjobResultsOverview getQueryJobResultsOverview(queryjobId, opts)

Provide a summary of results for the projects in the query job

This endpoint provides a summary of the results generated by completed query runs for each  project specified in the the POST /queryjobs endpoint.  For completed query jobs, the summary includes:    * The number of results for successful query runs.   * Error information for failed query runs.  No information is included in the response for any project for which the query  run is still in progress. 

### Example

```javascript
import LgtmApiSpecification from 'lgtm_api_specification';
let defaultClient = LgtmApiSpecification.ApiClient.instance;
// Configure Bearer access token for authorization: access-token
let access-token = defaultClient.authentications['access-token'];
access-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new LgtmApiSpecification.QueryJobsApi();
let queryjobId = "queryjobId_example"; // String | The identifier of the query job, from the `task-result` given in the response to the initial `POST /queryjobs` request.
let opts = {
  'start': "start_example", // String | An opaque identifier generated by the API used for pagination.  This identifier will be included as part of the response for this endpoint whenever more than one page of results is available.  
  'limit': 100, // Number | The number of results to return. Useful for pagination.
  'filter': "filter_example" // String | Only return a subset of results. Legal values are `w-results`, `wo-results`, `error`.
};
apiInstance.getQueryJobResultsOverview(queryjobId, opts, (error, data, response) => {
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
 **queryjobId** | **String**| The identifier of the query job, from the &#x60;task-result&#x60; given in the response to the initial &#x60;POST /queryjobs&#x60; request. | 
 **start** | **String**| An opaque identifier generated by the API used for pagination.  This identifier will be included as part of the response for this endpoint whenever more than one page of results is available.   | [optional] 
 **limit** | **Number**| The number of results to return. Useful for pagination. | [optional] [default to 100]
 **filter** | **String**| Only return a subset of results. Legal values are &#x60;w-results&#x60;, &#x60;wo-results&#x60;, &#x60;error&#x60;. | [optional] 

### Return type

[**QueryjobResultsOverview**](QueryjobResultsOverview.md)

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

