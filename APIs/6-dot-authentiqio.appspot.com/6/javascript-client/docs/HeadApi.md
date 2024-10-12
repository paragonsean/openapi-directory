# AuthentiqApi.HeadApi

All URIs are relative to *https://6-dot-authentiqio.appspot.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**keyPKHead_0**](HeadApi.md#keyPKHead_0) | **HEAD** /key/{PK} | 
[**signRetrieveHead_0**](HeadApi.md#signRetrieveHead_0) | **HEAD** /scope/{job} | 



## keyPKHead_0

> keyPKHead_0(PK)



HEAD info on Authentiq ID 

### Example

```javascript
import AuthentiqApi from 'authentiq_api';

let apiInstance = new AuthentiqApi.HeadApi();
let PK = "PK_example"; // String | Public Signing Key - Authentiq ID (43 chars)
apiInstance.keyPKHead_0(PK, (error, data, response) => {
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
 **PK** | **String**| Public Signing Key - Authentiq ID (43 chars) | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## signRetrieveHead_0

> signRetrieveHead_0(job)



HEAD to get the status of a verification job

### Example

```javascript
import AuthentiqApi from 'authentiq_api';

let apiInstance = new AuthentiqApi.HeadApi();
let job = "job_example"; // String | Job ID (20 chars)
apiInstance.signRetrieveHead_0(job, (error, data, response) => {
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

