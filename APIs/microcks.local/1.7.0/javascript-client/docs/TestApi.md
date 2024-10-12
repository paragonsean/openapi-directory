# MicrocksApiV17.TestApi

All URIs are relative to *http://microcks.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createTest**](TestApi.md#createTest) | **POST** /tests | Create a new Test
[**getEventsByTestCase**](TestApi.md#getEventsByTestCase) | **GET** /tests/{id}/events/{testCaseId} | Get events for TestCase
[**getMessagesByTestCase**](TestApi.md#getMessagesByTestCase) | **GET** /tests/{id}/messages/{testCaseId} | Get messages for TestCase
[**getTestResult**](TestApi.md#getTestResult) | **GET** /tests/{id} | Get TestResult
[**getTestResultsByService**](TestApi.md#getTestResultsByService) | **GET** /tests/service/{serviceId} | Get TestResults by Service
[**getTestResultsByServiceCounter**](TestApi.md#getTestResultsByServiceCounter) | **GET** /tests/service/{serviceId}/count | Get the TestResults for Service counter
[**reportTestCaseResult**](TestApi.md#reportTestCaseResult) | **POST** /tests/{id}/testCaseResult | Report and create a new TestCaseResult



## createTest

> TestResult createTest(testRequest)

Create a new Test

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.TestApi();
let testRequest = new MicrocksApiV17.TestRequest(); // TestRequest | 
apiInstance.createTest(testRequest, (error, data, response) => {
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
 **testRequest** | [**TestRequest**](TestRequest.md)|  | 

### Return type

[**TestResult**](TestResult.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getEventsByTestCase

> [UnidirectionalEvent] getEventsByTestCase(id, testCaseId)

Get events for TestCase

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.TestApi();
let id = "id_example"; // String | Unique identifier of TestResult to manage
let testCaseId = "testCaseId_example"; // String | Unique identifier of TetsCaseResult to manage
apiInstance.getEventsByTestCase(id, testCaseId, (error, data, response) => {
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
 **id** | **String**| Unique identifier of TestResult to manage | 
 **testCaseId** | **String**| Unique identifier of TetsCaseResult to manage | 

### Return type

[**[UnidirectionalEvent]**](UnidirectionalEvent.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMessagesByTestCase

> [RequestResponsePair] getMessagesByTestCase(id, testCaseId)

Get messages for TestCase

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.TestApi();
let id = "id_example"; // String | Unique identifier of TestResult to manage
let testCaseId = "testCaseId_example"; // String | Unique identifier of TetsCaseResult to manage
apiInstance.getMessagesByTestCase(id, testCaseId, (error, data, response) => {
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
 **id** | **String**| Unique identifier of TestResult to manage | 
 **testCaseId** | **String**| Unique identifier of TetsCaseResult to manage | 

### Return type

[**[RequestResponsePair]**](RequestResponsePair.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTestResult

> TestResult getTestResult(id)

Get TestResult



### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.TestApi();
let id = "id_example"; // String | Unique identifier of TestResult to manage
apiInstance.getTestResult(id, (error, data, response) => {
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
 **id** | **String**| Unique identifier of TestResult to manage | 

### Return type

[**TestResult**](TestResult.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTestResultsByService

> [TestResult] getTestResultsByService(serviceId)

Get TestResults by Service

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.TestApi();
let serviceId = "serviceId_example"; // String | Unique identifier of Service to manage TestResults for
apiInstance.getTestResultsByService(serviceId, (error, data, response) => {
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
 **serviceId** | **String**| Unique identifier of Service to manage TestResults for | 

### Return type

[**[TestResult]**](TestResult.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTestResultsByServiceCounter

> Counter getTestResultsByServiceCounter(serviceId)

Get the TestResults for Service counter

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.TestApi();
let serviceId = "serviceId_example"; // String | Unique identifier of Service to manage TestResults for
apiInstance.getTestResultsByServiceCounter(serviceId, (error, data, response) => {
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
 **serviceId** | **String**| Unique identifier of Service to manage TestResults for | 

### Return type

[**Counter**](Counter.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reportTestCaseResult

> TestCaseResult reportTestCaseResult(id, testCaseReturnDTO)

Report and create a new TestCaseResult

Report a TestCaseResult (typically used by a Test runner)

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.TestApi();
let id = "id_example"; // String | Unique identifier of TestResult to manage
let testCaseReturnDTO = new MicrocksApiV17.TestCaseReturnDTO(); // TestCaseReturnDTO | TestCase return wrapper object
apiInstance.reportTestCaseResult(id, testCaseReturnDTO, (error, data, response) => {
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
 **id** | **String**| Unique identifier of TestResult to manage | 
 **testCaseReturnDTO** | [**TestCaseReturnDTO**](TestCaseReturnDTO.md)| TestCase return wrapper object | 

### Return type

[**TestCaseResult**](TestCaseResult.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

