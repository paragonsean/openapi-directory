# NetlifysApiDocumentation.SubmissionApi

All URIs are relative to *https://api.netlify.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteSubmission**](SubmissionApi.md#deleteSubmission) | **DELETE** /submissions/{submission_id} | 
[**listFormSubmission**](SubmissionApi.md#listFormSubmission) | **GET** /submissions/{submission_id} | 
[**listFormSubmissions**](SubmissionApi.md#listFormSubmissions) | **GET** /forms/{form_id}/submissions | 
[**listSiteSubmissions**](SubmissionApi.md#listSiteSubmissions) | **GET** /sites/{site_id}/submissions | 



## deleteSubmission

> deleteSubmission(submissionId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.SubmissionApi();
let submissionId = "submissionId_example"; // String | 
apiInstance.deleteSubmission(submissionId, (error, data, response) => {
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
 **submissionId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listFormSubmission

> [Submission] listFormSubmission(submissionId, opts)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.SubmissionApi();
let submissionId = "submissionId_example"; // String | 
let opts = {
  'query': "query_example", // String | 
  'page': 56, // Number | 
  'perPage': 56 // Number | 
};
apiInstance.listFormSubmission(submissionId, opts, (error, data, response) => {
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
 **submissionId** | **String**|  | 
 **query** | **String**|  | [optional] 
 **page** | **Number**|  | [optional] 
 **perPage** | **Number**|  | [optional] 

### Return type

[**[Submission]**](Submission.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listFormSubmissions

> [Submission] listFormSubmissions(formId, opts)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.SubmissionApi();
let formId = "formId_example"; // String | 
let opts = {
  'page': 56, // Number | 
  'perPage': 56 // Number | 
};
apiInstance.listFormSubmissions(formId, opts, (error, data, response) => {
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
 **formId** | **String**|  | 
 **page** | **Number**|  | [optional] 
 **perPage** | **Number**|  | [optional] 

### Return type

[**[Submission]**](Submission.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSiteSubmissions

> [Submission] listSiteSubmissions(siteId, opts)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.SubmissionApi();
let siteId = "siteId_example"; // String | 
let opts = {
  'page': 56, // Number | 
  'perPage': 56 // Number | 
};
apiInstance.listSiteSubmissions(siteId, opts, (error, data, response) => {
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
 **siteId** | **String**|  | 
 **page** | **Number**|  | [optional] 
 **perPage** | **Number**|  | [optional] 

### Return type

[**[Submission]**](Submission.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

