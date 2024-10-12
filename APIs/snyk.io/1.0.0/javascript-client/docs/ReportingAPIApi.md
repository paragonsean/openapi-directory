# SnykApi.ReportingAPIApi

All URIs are relative to *https://api.snyk.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getIssueCounts**](ReportingAPIApi.md#getIssueCounts) | **POST** /reporting/counts/issues | Get issue counts
[**getLatestIssueCounts**](ReportingAPIApi.md#getLatestIssueCounts) | **POST** /reporting/counts/issues/latest | Get latest issue counts
[**getLatestProjectCounts**](ReportingAPIApi.md#getLatestProjectCounts) | **POST** /reporting/counts/projects/latest | Get latest project counts
[**getListOfIssues**](ReportingAPIApi.md#getListOfIssues) | **POST** /reporting/issues/ | Get list of issues
[**getListOfLatestIssues**](ReportingAPIApi.md#getListOfLatestIssues) | **POST** /reporting/issues/latest | Get list of latest issues
[**getProjectCounts**](ReportingAPIApi.md#getProjectCounts) | **POST** /reporting/counts/projects | Get project counts
[**getTestCounts**](ReportingAPIApi.md#getTestCounts) | **POST** /reporting/counts/tests | Get test counts



## getIssueCounts

> GetIssueCounts200Response getIssueCounts(from, to, opts)

Get issue counts



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.ReportingAPIApi();
let from = "2017-07-01"; // String | The date you wish to fetch results from, in the format `YYYY-MM-DD`
let to = "2017-07-03"; // String | The date you wish to fetch results until, in the format `YYYY-MM-DD`
let opts = {
  'groupBy': "severity", // String | The field to group results by
  'getIssueCountsRequest': new SnykApi.GetIssueCountsRequest() // GetIssueCountsRequest | 
};
apiInstance.getIssueCounts(from, to, opts, (error, data, response) => {
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
 **from** | **String**| The date you wish to fetch results from, in the format &#x60;YYYY-MM-DD&#x60; | 
 **to** | **String**| The date you wish to fetch results until, in the format &#x60;YYYY-MM-DD&#x60; | 
 **groupBy** | **String**| The field to group results by | [optional] 
 **getIssueCountsRequest** | [**GetIssueCountsRequest**](GetIssueCountsRequest.md)|  | [optional] 

### Return type

[**GetIssueCounts200Response**](GetIssueCounts200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## getLatestIssueCounts

> GetIssueCounts200Response getLatestIssueCounts(opts)

Get latest issue counts



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.ReportingAPIApi();
let opts = {
  'groupBy': "severity", // String | The field to group results by
  'getIssueCountsRequest': new SnykApi.GetIssueCountsRequest() // GetIssueCountsRequest | 
};
apiInstance.getLatestIssueCounts(opts, (error, data, response) => {
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
 **groupBy** | **String**| The field to group results by | [optional] 
 **getIssueCountsRequest** | [**GetIssueCountsRequest**](GetIssueCountsRequest.md)|  | [optional] 

### Return type

[**GetIssueCounts200Response**](GetIssueCounts200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## getLatestProjectCounts

> GetProjectCounts200Response getLatestProjectCounts(opts)

Get latest project counts



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.ReportingAPIApi();
let opts = {
  'getProjectCountsRequest': new SnykApi.GetProjectCountsRequest() // GetProjectCountsRequest | 
};
apiInstance.getLatestProjectCounts(opts, (error, data, response) => {
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
 **getProjectCountsRequest** | [**GetProjectCountsRequest**](GetProjectCountsRequest.md)|  | [optional] 

### Return type

[**GetProjectCounts200Response**](GetProjectCounts200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## getListOfIssues

> GetListOfIssues200Response getListOfIssues(from, to, opts)

Get list of issues



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.ReportingAPIApi();
let from = "2017-07-01"; // String | The date you wish to fetch results from, in the format `YYYY-MM-DD`
let to = "2017-07-07"; // String | The date you wish to fetch results until, in the format `YYYY-MM-DD`
let opts = {
  'page': 1, // Number | The page of results to request
  'perPage': 100, // Number | The number of results to return per page (Maximum: 1000)
  'sortBy': "issueTitle", // String | The key to sort results by
  'order': "asc", // String | The direction to sort results.
  'groupBy': "issue", // String | Set to issue to group the same issue in multiple projects
  'getListOfIssuesRequest': new SnykApi.GetListOfIssuesRequest() // GetListOfIssuesRequest | 
};
apiInstance.getListOfIssues(from, to, opts, (error, data, response) => {
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
 **from** | **String**| The date you wish to fetch results from, in the format &#x60;YYYY-MM-DD&#x60; | 
 **to** | **String**| The date you wish to fetch results until, in the format &#x60;YYYY-MM-DD&#x60; | 
 **page** | **Number**| The page of results to request | [optional] 
 **perPage** | **Number**| The number of results to return per page (Maximum: 1000) | [optional] 
 **sortBy** | **String**| The key to sort results by | [optional] 
 **order** | **String**| The direction to sort results. | [optional] 
 **groupBy** | **String**| Set to issue to group the same issue in multiple projects | [optional] 
 **getListOfIssuesRequest** | [**GetListOfIssuesRequest**](GetListOfIssuesRequest.md)|  | [optional] 

### Return type

[**GetListOfIssues200Response**](GetListOfIssues200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## getListOfLatestIssues

> GetListOfIssues200Response getListOfLatestIssues(opts)

Get list of latest issues



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.ReportingAPIApi();
let opts = {
  'page': 1, // Number | The page of results to request
  'perPage': 100, // Number | The number of results to return per page (Maximum: 1000)
  'sortBy': "issueTitle", // String | The key to sort results by
  'order': "asc", // String | The direction to sort results.
  'groupBy': "issue", // String | Set to issue to group the same issue in multiple projects
  'getListOfIssuesRequest': new SnykApi.GetListOfIssuesRequest() // GetListOfIssuesRequest | 
};
apiInstance.getListOfLatestIssues(opts, (error, data, response) => {
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
 **page** | **Number**| The page of results to request | [optional] 
 **perPage** | **Number**| The number of results to return per page (Maximum: 1000) | [optional] 
 **sortBy** | **String**| The key to sort results by | [optional] 
 **order** | **String**| The direction to sort results. | [optional] 
 **groupBy** | **String**| Set to issue to group the same issue in multiple projects | [optional] 
 **getListOfIssuesRequest** | [**GetListOfIssuesRequest**](GetListOfIssuesRequest.md)|  | [optional] 

### Return type

[**GetListOfIssues200Response**](GetListOfIssues200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## getProjectCounts

> GetProjectCounts200Response getProjectCounts(from, to, opts)

Get project counts



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.ReportingAPIApi();
let from = "2017-07-01"; // String | The date you wish to fetch results from, in the format `YYYY-MM-DD`
let to = "2017-07-03"; // String | The date you wish to fetch results until, in the format `YYYY-MM-DD`
let opts = {
  'getProjectCountsRequest': new SnykApi.GetProjectCountsRequest() // GetProjectCountsRequest | 
};
apiInstance.getProjectCounts(from, to, opts, (error, data, response) => {
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
 **from** | **String**| The date you wish to fetch results from, in the format &#x60;YYYY-MM-DD&#x60; | 
 **to** | **String**| The date you wish to fetch results until, in the format &#x60;YYYY-MM-DD&#x60; | 
 **getProjectCountsRequest** | [**GetProjectCountsRequest**](GetProjectCountsRequest.md)|  | [optional] 

### Return type

[**GetProjectCounts200Response**](GetProjectCounts200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## getTestCounts

> GetTestCounts200Response getTestCounts(from, to, opts)

Get test counts



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.ReportingAPIApi();
let from = "2017-07-01"; // String | The date you wish to count tests from, in the format `YYYY-MM-DD`
let to = "2017-07-03"; // String | The date you wish to count tests until, in the format `YYYY-MM-DD`
let opts = {
  'groupBy': "isPrivate", // String | The field to group results by
  'getTestCountsRequest': new SnykApi.GetTestCountsRequest() // GetTestCountsRequest | 
};
apiInstance.getTestCounts(from, to, opts, (error, data, response) => {
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
 **from** | **String**| The date you wish to count tests from, in the format &#x60;YYYY-MM-DD&#x60; | 
 **to** | **String**| The date you wish to count tests until, in the format &#x60;YYYY-MM-DD&#x60; | 
 **groupBy** | **String**| The field to group results by | [optional] 
 **getTestCountsRequest** | [**GetTestCountsRequest**](GetTestCountsRequest.md)|  | [optional] 

### Return type

[**GetTestCounts200Response**](GetTestCounts200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8

