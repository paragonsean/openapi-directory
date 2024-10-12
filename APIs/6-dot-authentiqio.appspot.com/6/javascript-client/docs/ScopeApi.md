# AuthentiqApi.ScopeApi

All URIs are relative to *https://6-dot-authentiqio.appspot.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**signConfirm**](ScopeApi.md#signConfirm) | **POST** /scope/{job} | 
[**signDelete**](ScopeApi.md#signDelete) | **DELETE** /scope/{job} | 
[**signRequest**](ScopeApi.md#signRequest) | **POST** /scope | 
[**signRetrieve**](ScopeApi.md#signRetrieve) | **GET** /scope/{job} | 
[**signRetrieveHead**](ScopeApi.md#signRetrieveHead) | **HEAD** /scope/{job} | 
[**signUpdate**](ScopeApi.md#signUpdate) | **PUT** /scope/{job} | 



## signConfirm

> KeyBind200Response signConfirm(job)



this is a scope confirmation

### Example

```javascript
import AuthentiqApi from 'authentiq_api';

let apiInstance = new AuthentiqApi.ScopeApi();
let job = "job_example"; // String | Job ID (20 chars)
apiInstance.signConfirm(job, (error, data, response) => {
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
 **job** | **String**| Job ID (20 chars) | 

### Return type

[**KeyBind200Response**](KeyBind200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## signDelete

> KeyRevoke200Response signDelete(job)



delete a verification job

### Example

```javascript
import AuthentiqApi from 'authentiq_api';

let apiInstance = new AuthentiqApi.ScopeApi();
let job = "job_example"; // String | Job ID (20 chars)
apiInstance.signDelete(job, (error, data, response) => {
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
 **job** | **String**| Job ID (20 chars) | 

### Return type

[**KeyRevoke200Response**](KeyRevoke200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## signRequest

> SignRequest201Response signRequest(claims, opts)



scope verification request See: https://github.com/skion/authentiq/wiki/JWT-Examples 

### Example

```javascript
import AuthentiqApi from 'authentiq_api';

let apiInstance = new AuthentiqApi.ScopeApi();
let claims = new AuthentiqApi.Claims(); // Claims | Claims of scope
let opts = {
  'test': 56 // Number | test only mode, using test issuer
};
apiInstance.signRequest(claims, opts, (error, data, response) => {
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
 **claims** | [**Claims**](Claims.md)| Claims of scope | 
 **test** | **Number**| test only mode, using test issuer | [optional] 

### Return type

[**SignRequest201Response**](SignRequest201Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/jwt
- **Accept**: application/json, */*


## signRetrieve

> JWT1 signRetrieve(job)



get the status / current content of a verification job

### Example

```javascript
import AuthentiqApi from 'authentiq_api';

let apiInstance = new AuthentiqApi.ScopeApi();
let job = "job_example"; // String | Job ID (20 chars)
apiInstance.signRetrieve(job, (error, data, response) => {
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
 **job** | **String**| Job ID (20 chars) | 

### Return type

[**JWT1**](JWT1.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/jwt, */*


## signRetrieveHead

> signRetrieveHead(job)



HEAD to get the status of a verification job

### Example

```javascript
import AuthentiqApi from 'authentiq_api';

let apiInstance = new AuthentiqApi.ScopeApi();
let job = "job_example"; // String | Job ID (20 chars)
apiInstance.signRetrieveHead(job, (error, data, response) => {
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
 **job** | **String**| Job ID (20 chars) | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## signUpdate

> SignUpdate200Response signUpdate(job)



authority updates a JWT with its signature See: https://github.com/skion/authentiq/wiki/JWT-Examples 

### Example

```javascript
import AuthentiqApi from 'authentiq_api';

let apiInstance = new AuthentiqApi.ScopeApi();
let job = "job_example"; // String | Job ID (20 chars)
apiInstance.signUpdate(job, (error, data, response) => {
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
 **job** | **String**| Job ID (20 chars) | 

### Return type

[**SignUpdate200Response**](SignUpdate200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/jwt, */*

