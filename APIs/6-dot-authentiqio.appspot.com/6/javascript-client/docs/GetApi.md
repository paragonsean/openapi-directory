# AuthentiqApi.GetApi

All URIs are relative to *https://6-dot-authentiqio.appspot.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**keyRetrieve_0**](GetApi.md#keyRetrieve_0) | **GET** /key/{PK} | 
[**signRetrieve_0**](GetApi.md#signRetrieve_0) | **GET** /scope/{job} | 



## keyRetrieve_0

> JWT keyRetrieve_0(PK)



Get public details of an Authentiq ID. 

### Example

```javascript
import AuthentiqApi from 'authentiq_api';

let apiInstance = new AuthentiqApi.GetApi();
let PK = "PK_example"; // String | Public Signing Key - Authentiq ID (43 chars)
apiInstance.keyRetrieve_0(PK, (error, data, response) => {
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
 **PK** | **String**| Public Signing Key - Authentiq ID (43 chars) | 

### Return type

[**JWT**](JWT.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## signRetrieve_0

> JWT1 signRetrieve_0(job)



get the status / current content of a verification job

### Example

```javascript
import AuthentiqApi from 'authentiq_api';

let apiInstance = new AuthentiqApi.GetApi();
let job = "job_example"; // String | Job ID (20 chars)
apiInstance.signRetrieve_0(job, (error, data, response) => {
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

