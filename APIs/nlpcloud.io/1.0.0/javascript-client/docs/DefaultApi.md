# NlpCloud.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**readDependenciesV1EnCoreWebSmDependenciesPost**](DefaultApi.md#readDependenciesV1EnCoreWebSmDependenciesPost) | **POST** /v1/en_core_web_sm/dependencies | Read Dependencies
[**readEntitiesV1EnCoreWebSmEntitiesPost**](DefaultApi.md#readEntitiesV1EnCoreWebSmEntitiesPost) | **POST** /v1/en_core_web_sm/entities | Read Entities
[**readRootV1EnCoreWebSmGet**](DefaultApi.md#readRootV1EnCoreWebSmGet) | **GET** /v1/en_core_web_sm/ | Read Root
[**readSentenceDependenciesV1EnCoreWebSmSentenceDependenciesPost**](DefaultApi.md#readSentenceDependenciesV1EnCoreWebSmSentenceDependenciesPost) | **POST** /v1/en_core_web_sm/sentence-dependencies | Read Sentence Dependencies
[**readVersionV1EnCoreWebSmVersionGet**](DefaultApi.md#readVersionV1EnCoreWebSmVersionGet) | **GET** /v1/en_core_web_sm/version | Read Version



## readDependenciesV1EnCoreWebSmDependenciesPost

> DependenciesOut readDependenciesV1EnCoreWebSmDependenciesPost(userRequestIn)

Read Dependencies

### Example

```javascript
import NlpCloud from 'nlp_cloud';
let defaultClient = NlpCloud.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new NlpCloud.DefaultApi();
let userRequestIn = new NlpCloud.UserRequestIn(); // UserRequestIn | 
apiInstance.readDependenciesV1EnCoreWebSmDependenciesPost(userRequestIn, (error, data, response) => {
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
 **userRequestIn** | [**UserRequestIn**](UserRequestIn.md)|  | 

### Return type

[**DependenciesOut**](DependenciesOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## readEntitiesV1EnCoreWebSmEntitiesPost

> EntitiesOut readEntitiesV1EnCoreWebSmEntitiesPost(userRequestIn)

Read Entities

### Example

```javascript
import NlpCloud from 'nlp_cloud';
let defaultClient = NlpCloud.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new NlpCloud.DefaultApi();
let userRequestIn = new NlpCloud.UserRequestIn(); // UserRequestIn | 
apiInstance.readEntitiesV1EnCoreWebSmEntitiesPost(userRequestIn, (error, data, response) => {
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
 **userRequestIn** | [**UserRequestIn**](UserRequestIn.md)|  | 

### Return type

[**EntitiesOut**](EntitiesOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## readRootV1EnCoreWebSmGet

> Object readRootV1EnCoreWebSmGet()

Read Root

### Example

```javascript
import NlpCloud from 'nlp_cloud';
let defaultClient = NlpCloud.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new NlpCloud.DefaultApi();
apiInstance.readRootV1EnCoreWebSmGet((error, data, response) => {
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

**Object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readSentenceDependenciesV1EnCoreWebSmSentenceDependenciesPost

> SentenceDependenciesOut readSentenceDependenciesV1EnCoreWebSmSentenceDependenciesPost(userRequestIn)

Read Sentence Dependencies

### Example

```javascript
import NlpCloud from 'nlp_cloud';
let defaultClient = NlpCloud.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new NlpCloud.DefaultApi();
let userRequestIn = new NlpCloud.UserRequestIn(); // UserRequestIn | 
apiInstance.readSentenceDependenciesV1EnCoreWebSmSentenceDependenciesPost(userRequestIn, (error, data, response) => {
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
 **userRequestIn** | [**UserRequestIn**](UserRequestIn.md)|  | 

### Return type

[**SentenceDependenciesOut**](SentenceDependenciesOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## readVersionV1EnCoreWebSmVersionGet

> VersionOut readVersionV1EnCoreWebSmVersionGet()

Read Version

### Example

```javascript
import NlpCloud from 'nlp_cloud';
let defaultClient = NlpCloud.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new NlpCloud.DefaultApi();
apiInstance.readVersionV1EnCoreWebSmVersionGet((error, data, response) => {
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

[**VersionOut**](VersionOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

