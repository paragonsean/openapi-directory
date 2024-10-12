# ChecksApi.ContinuousApi

All URIs are relative to *https://api.truora.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createContinuousCheck**](ContinuousApi.md#createContinuousCheck) | **POST** /v1/continuous-checks | 
[**getContinuousCheck**](ContinuousApi.md#getContinuousCheck) | **GET** /v1/continuous-checks/{continuous_check_id} | 
[**listContinuousChecks**](ContinuousApi.md#listContinuousChecks) | **GET** /v1/continuous-checks | 
[**updateContinuousCheck**](ContinuousApi.md#updateContinuousCheck) | **PUT** /v1/continuous-checks/{continuous_check_id} | 
[**v1ContinuousChecksContinuousCheckIdHistoryGet**](ContinuousApi.md#v1ContinuousChecksContinuousCheckIdHistoryGet) | **GET** /v1/continuous-checks/{continuous_check_id}/history | 



## createContinuousCheck

> ContinuousCheck createContinuousCheck(opts)



Creates a continuous check that will run background checks recurrently according to the frequency provided.

### Example

```javascript
import ChecksApi from 'checks_api';
let defaultClient = ChecksApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ChecksApi.ContinuousApi();
let opts = {
  'checkId': "checkId_example", // String | Background checks to be processed recurrently
  'frequency': "frequency_example", // String | Time between background checks. It can be daily, weekly, monthly, yearly or have a custom frequency written as a number accompanied by d: day, w: week, m: month, y: year for instance: 3d: every three days, 2w: every two weeks
  'status': "status_example" // String | Indicates whether the background checks must be processed recurrently (enabled | disabled)
};
apiInstance.createContinuousCheck(opts, (error, data, response) => {
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
 **checkId** | **String**| Background checks to be processed recurrently | [optional] 
 **frequency** | **String**| Time between background checks. It can be daily, weekly, monthly, yearly or have a custom frequency written as a number accompanied by d: day, w: week, m: month, y: year for instance: 3d: every three days, 2w: every two weeks | [optional] 
 **status** | **String**| Indicates whether the background checks must be processed recurrently (enabled | disabled) | [optional] 

### Return type

[**ContinuousCheck**](ContinuousCheck.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## getContinuousCheck

> ContinuousCheck getContinuousCheck(continuousCheckId)



Lists history associated with a Check. It can be paginated

### Example

```javascript
import ChecksApi from 'checks_api';
let defaultClient = ChecksApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ChecksApi.ContinuousApi();
let continuousCheckId = 3.4; // Number | ID resulting from calling CreateContinuousCheck
apiInstance.getContinuousCheck(continuousCheckId, (error, data, response) => {
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
 **continuousCheckId** | **Number**| ID resulting from calling CreateContinuousCheck | 

### Return type

[**ContinuousCheck**](ContinuousCheck.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listContinuousChecks

> ListContinuousChecksOutput listContinuousChecks()



Lists all continuous checks

### Example

```javascript
import ChecksApi from 'checks_api';
let defaultClient = ChecksApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ChecksApi.ContinuousApi();
apiInstance.listContinuousChecks((error, data, response) => {
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

[**ListContinuousChecksOutput**](ListContinuousChecksOutput.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateContinuousCheck

> ContinuousCheck updateContinuousCheck(continuousCheckId, frequency, status)



Updates a continuous check

### Example

```javascript
import ChecksApi from 'checks_api';
let defaultClient = ChecksApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ChecksApi.ContinuousApi();
let continuousCheckId = 3.4; // Number | ID resulting from calling CreateContinuousCheck
let frequency = "frequency_example"; // String | Time between background checks
let status = "status_example"; // String | Indicates whether the background checks must be processed recurrently
apiInstance.updateContinuousCheck(continuousCheckId, frequency, status, (error, data, response) => {
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
 **continuousCheckId** | **Number**| ID resulting from calling CreateContinuousCheck | 
 **frequency** | **String**| Time between background checks | 
 **status** | **String**| Indicates whether the background checks must be processed recurrently | 

### Return type

[**ContinuousCheck**](ContinuousCheck.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## v1ContinuousChecksContinuousCheckIdHistoryGet

> GetContiuousCheckHistoryOutput v1ContinuousChecksContinuousCheckIdHistoryGet(continuousCheckId)



Lists background check logs. It can be paginated  

### Example

```javascript
import ChecksApi from 'checks_api';
let defaultClient = ChecksApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ChecksApi.ContinuousApi();
let continuousCheckId = "continuousCheckId_example"; // String | 
apiInstance.v1ContinuousChecksContinuousCheckIdHistoryGet(continuousCheckId, (error, data, response) => {
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
 **continuousCheckId** | **String**|  | 

### Return type

[**GetContiuousCheckHistoryOutput**](GetContiuousCheckHistoryOutput.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

