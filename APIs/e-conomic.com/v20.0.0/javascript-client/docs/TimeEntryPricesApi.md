# VismaEConomicOpenApi.TimeEntryPricesApi

All URIs are relative to *https://apis.e-conomic.com/api/v20.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAllTimeEntryPrices**](TimeEntryPricesApi.md#getAllTimeEntryPrices) | **GET** /timeentryprices | Retrieve all Time entry prices
[**getPageOfTimeEntryPrices**](TimeEntryPricesApi.md#getPageOfTimeEntryPrices) | **GET** /timeentryprices/paged | Retrieve a page of Time entry prices
[**getTimeEntryPricesById**](TimeEntryPricesApi.md#getTimeEntryPricesById) | **GET** /timeentryprices/{number} | Retrieve single Time entry prices



## getAllTimeEntryPrices

> TimeEntryPricesCursorResults getAllTimeEntryPrices(opts)

Retrieve all Time entry prices

Use this endpoint to retrieve all Time entry prices in bulk.  Max number of items returned in a single call is 1000. Use the continuation cursor parameter to set the continuation cursor for retrieval of next set of data. [pagination instructions](#section/Retrieving-data/Pagination)

### Example

```javascript
import VismaEConomicOpenApi from 'visma_e_conomic_open_api';
let defaultClient = VismaEConomicOpenApi.ApiClient.instance;
// Configure API key authorization: X-AgreementGrantToken
let X-AgreementGrantToken = defaultClient.authentications['X-AgreementGrantToken'];
X-AgreementGrantToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AgreementGrantToken.apiKeyPrefix = 'Token';
// Configure API key authorization: X-AppSecretToken
let X-AppSecretToken = defaultClient.authentications['X-AppSecretToken'];
X-AppSecretToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AppSecretToken.apiKeyPrefix = 'Token';

let apiInstance = new VismaEConomicOpenApi.TimeEntryPricesApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'filter': "filter_example" // String | 
};
apiInstance.getAllTimeEntryPrices(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **filter** | **String**|  | [optional] 

### Return type

[**TimeEntryPricesCursorResults**](TimeEntryPricesCursorResults.md)

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPageOfTimeEntryPrices

> [TimeEntryPrices] getPageOfTimeEntryPrices(opts)

Retrieve a page of Time entry prices

Use this endpoint to load a page of Time entry prices.

### Example

```javascript
import VismaEConomicOpenApi from 'visma_e_conomic_open_api';
let defaultClient = VismaEConomicOpenApi.ApiClient.instance;
// Configure API key authorization: X-AgreementGrantToken
let X-AgreementGrantToken = defaultClient.authentications['X-AgreementGrantToken'];
X-AgreementGrantToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AgreementGrantToken.apiKeyPrefix = 'Token';
// Configure API key authorization: X-AppSecretToken
let X-AppSecretToken = defaultClient.authentications['X-AppSecretToken'];
X-AppSecretToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AppSecretToken.apiKeyPrefix = 'Token';

let apiInstance = new VismaEConomicOpenApi.TimeEntryPricesApi();
let opts = {
  'filter': "filter_example", // String | 
  'sort': "sort_example", // String | 
  'pageSize': 20, // Number | 
  'skipPages': 0 // Number | 
};
apiInstance.getPageOfTimeEntryPrices(opts, (error, data, response) => {
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
 **filter** | **String**|  | [optional] 
 **sort** | **String**|  | [optional] 
 **pageSize** | **Number**|  | [optional] [default to 20]
 **skipPages** | **Number**|  | [optional] [default to 0]

### Return type

[**[TimeEntryPrices]**](TimeEntryPrices.md)

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTimeEntryPricesById

> TimeEntryPrices getTimeEntryPricesById(number)

Retrieve single Time entry prices

Use this endpoint to load a single Time entry prices by id/number.

### Example

```javascript
import VismaEConomicOpenApi from 'visma_e_conomic_open_api';
let defaultClient = VismaEConomicOpenApi.ApiClient.instance;
// Configure API key authorization: X-AgreementGrantToken
let X-AgreementGrantToken = defaultClient.authentications['X-AgreementGrantToken'];
X-AgreementGrantToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AgreementGrantToken.apiKeyPrefix = 'Token';
// Configure API key authorization: X-AppSecretToken
let X-AppSecretToken = defaultClient.authentications['X-AppSecretToken'];
X-AppSecretToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AppSecretToken.apiKeyPrefix = 'Token';

let apiInstance = new VismaEConomicOpenApi.TimeEntryPricesApi();
let number = 56; // Number | 
apiInstance.getTimeEntryPricesById(number, (error, data, response) => {
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
 **number** | **Number**|  | 

### Return type

[**TimeEntryPrices**](TimeEntryPrices.md)

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

