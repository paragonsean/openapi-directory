# MidjourneyRestApiByUseapiNet.DefaultApi

All URIs are relative to *https://api.useapi.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountGet**](DefaultApi.md#accountGet) | **GET** /account | 
[**jobsBlendPost**](DefaultApi.md#jobsBlendPost) | **POST** /jobs/blend | 
[**jobsButtonPost**](DefaultApi.md#jobsButtonPost) | **POST** /jobs/button | 
[**jobsCancelGet**](DefaultApi.md#jobsCancelGet) | **GET** /jobs/cancel/ | 
[**jobsDescribePost**](DefaultApi.md#jobsDescribePost) | **POST** /jobs/describe | 
[**jobsGet**](DefaultApi.md#jobsGet) | **GET** /jobs | 
[**jobsGet_0**](DefaultApi.md#jobsGet_0) | **GET** /jobs/ | 
[**jobsImaginePost**](DefaultApi.md#jobsImaginePost) | **POST** /jobs/imagine | 



## accountGet

> AccountResponse accountGet()



Retrieve account information

### Example

```javascript
import MidjourneyRestApiByUseapiNet from 'midjourney_rest_api_by_useapi_net';
let defaultClient = MidjourneyRestApiByUseapiNet.ApiClient.instance;
// Configure Bearer access token for authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MidjourneyRestApiByUseapiNet.DefaultApi();
apiInstance.accountGet((error, data, response) => {
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

[**AccountResponse**](AccountResponse.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobsBlendPost

> BlendResponse jobsBlendPost(jobsBlendPostRequest)



Submit the Midjourney /blend command

### Example

```javascript
import MidjourneyRestApiByUseapiNet from 'midjourney_rest_api_by_useapi_net';
let defaultClient = MidjourneyRestApiByUseapiNet.ApiClient.instance;
// Configure Bearer access token for authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MidjourneyRestApiByUseapiNet.DefaultApi();
let jobsBlendPostRequest = new MidjourneyRestApiByUseapiNet.JobsBlendPostRequest(); // JobsBlendPostRequest | 
apiInstance.jobsBlendPost(jobsBlendPostRequest, (error, data, response) => {
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
 **jobsBlendPostRequest** | [**JobsBlendPostRequest**](JobsBlendPostRequest.md)|  | 

### Return type

[**BlendResponse**](BlendResponse.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## jobsButtonPost

> ButtonResponse jobsButtonPost(jobsButtonPostRequest)



Submit the Midjourney /imagine command

### Example

```javascript
import MidjourneyRestApiByUseapiNet from 'midjourney_rest_api_by_useapi_net';
let defaultClient = MidjourneyRestApiByUseapiNet.ApiClient.instance;
// Configure Bearer access token for authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MidjourneyRestApiByUseapiNet.DefaultApi();
let jobsButtonPostRequest = new MidjourneyRestApiByUseapiNet.JobsButtonPostRequest(); // JobsButtonPostRequest | 
apiInstance.jobsButtonPost(jobsButtonPostRequest, (error, data, response) => {
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
 **jobsButtonPostRequest** | [**JobsButtonPostRequest**](JobsButtonPostRequest.md)|  | 

### Return type

[**ButtonResponse**](ButtonResponse.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## jobsCancelGet

> JobCancelResponse jobsCancelGet(jobid)



Cancel execution of job created by jobs/imagine, jobs/button, jobs/blend or jobs/describe

### Example

```javascript
import MidjourneyRestApiByUseapiNet from 'midjourney_rest_api_by_useapi_net';
let defaultClient = MidjourneyRestApiByUseapiNet.ApiClient.instance;
// Configure Bearer access token for authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MidjourneyRestApiByUseapiNet.DefaultApi();
let jobid = "jobid_example"; // String | jobid value returned by jobs/imagine, jobs/button, jobs/blend or jobs/describe
apiInstance.jobsCancelGet(jobid, (error, data, response) => {
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
 **jobid** | **String**| jobid value returned by jobs/imagine, jobs/button, jobs/blend or jobs/describe | 

### Return type

[**JobCancelResponse**](JobCancelResponse.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobsDescribePost

> DescribeResponse jobsDescribePost(jobsDescribePostRequest)



Submit the Midjourney /describe command

### Example

```javascript
import MidjourneyRestApiByUseapiNet from 'midjourney_rest_api_by_useapi_net';
let defaultClient = MidjourneyRestApiByUseapiNet.ApiClient.instance;
// Configure Bearer access token for authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MidjourneyRestApiByUseapiNet.DefaultApi();
let jobsDescribePostRequest = new MidjourneyRestApiByUseapiNet.JobsDescribePostRequest(); // JobsDescribePostRequest | 
apiInstance.jobsDescribePost(jobsDescribePostRequest, (error, data, response) => {
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
 **jobsDescribePostRequest** | [**JobsDescribePostRequest**](JobsDescribePostRequest.md)|  | 

### Return type

[**DescribeResponse**](DescribeResponse.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## jobsGet

> [String] jobsGet()



Get list of currently executing jobs

### Example

```javascript
import MidjourneyRestApiByUseapiNet from 'midjourney_rest_api_by_useapi_net';
let defaultClient = MidjourneyRestApiByUseapiNet.ApiClient.instance;
// Configure Bearer access token for authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MidjourneyRestApiByUseapiNet.DefaultApi();
apiInstance.jobsGet((error, data, response) => {
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

**[String]**

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobsGet_0

> JobResponse jobsGet_0(jobid)



Retrieve status and results of jobs/imagine, jobs/button, jobs/blend or jobs/describe

### Example

```javascript
import MidjourneyRestApiByUseapiNet from 'midjourney_rest_api_by_useapi_net';
let defaultClient = MidjourneyRestApiByUseapiNet.ApiClient.instance;
// Configure Bearer access token for authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MidjourneyRestApiByUseapiNet.DefaultApi();
let jobid = "jobid_example"; // String | jobid value returned by jobs/imagine, jobs/button, jobs/blend or jobs/describe
apiInstance.jobsGet_0(jobid, (error, data, response) => {
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
 **jobid** | **String**| jobid value returned by jobs/imagine, jobs/button, jobs/blend or jobs/describe | 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobsImaginePost

> ImagineResponse jobsImaginePost(jobsImaginePostRequest)



Submit the Midjourney /imagine command

### Example

```javascript
import MidjourneyRestApiByUseapiNet from 'midjourney_rest_api_by_useapi_net';
let defaultClient = MidjourneyRestApiByUseapiNet.ApiClient.instance;
// Configure Bearer access token for authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MidjourneyRestApiByUseapiNet.DefaultApi();
let jobsImaginePostRequest = new MidjourneyRestApiByUseapiNet.JobsImaginePostRequest(); // JobsImaginePostRequest | 
apiInstance.jobsImaginePost(jobsImaginePostRequest, (error, data, response) => {
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
 **jobsImaginePostRequest** | [**JobsImaginePostRequest**](JobsImaginePostRequest.md)|  | 

### Return type

[**ImagineResponse**](ImagineResponse.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

