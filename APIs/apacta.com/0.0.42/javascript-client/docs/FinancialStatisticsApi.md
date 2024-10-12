# Apacta.FinancialStatisticsApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**financialStatisticsWorkingHoursGet**](FinancialStatisticsApi.md#financialStatisticsWorkingHoursGet) | **GET** /financial_statistics/workingHours | Get Total working hours grouped by time entry type
[**getExpensesSalesPrice**](FinancialStatisticsApi.md#getExpensesSalesPrice) | **GET** /financial_statistics/expensesSalesPrice | Get expenses sales price
[**getFinancialStatistics**](FinancialStatisticsApi.md#getFinancialStatistics) | **GET** /financial_statistics | Get general statistics
[**getFinancialStatisticsOverview**](FinancialStatisticsApi.md#getFinancialStatisticsOverview) | **GET** /financial_statistics/overview | Get statistics overview
[**getInvoicedAmount**](FinancialStatisticsApi.md#getInvoicedAmount) | **GET** /financial_statistics/invoicedAmount | Get invoiced amount
[**getMargin**](FinancialStatisticsApi.md#getMargin) | **GET** /financial_statistics/margin | Get margin
[**getMaterialRentalsCostPrice**](FinancialStatisticsApi.md#getMaterialRentalsCostPrice) | **GET** /financial_statistics/materialRentalsCostPrice | Get products material rentals cost price
[**getProductsCostPrice**](FinancialStatisticsApi.md#getProductsCostPrice) | **GET** /financial_statistics/productsCostPrice | Get products cost price



## financialStatisticsWorkingHoursGet

> FinancialStatisticsWorkingHoursGet200Response financialStatisticsWorkingHoursGet(opts)

Get Total working hours grouped by time entry type

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.FinancialStatisticsApi();
let opts = {
  'dateFrom': new Date("2013-10-20"), // Date | 
  'dateTo': new Date("2013-10-20"), // Date | 
  'projectId': "projectId_example" // String | 
};
apiInstance.financialStatisticsWorkingHoursGet(opts, (error, data, response) => {
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
 **dateFrom** | **Date**|  | [optional] 
 **dateTo** | **Date**|  | [optional] 
 **projectId** | **String**|  | [optional] 

### Return type

[**FinancialStatisticsWorkingHoursGet200Response**](FinancialStatisticsWorkingHoursGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getExpensesSalesPrice

> GetExpensesSalesPrice200Response getExpensesSalesPrice(opts)

Get expenses sales price

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.FinancialStatisticsApi();
let opts = {
  'dateFrom': new Date("2013-10-20"), // Date | 
  'dateTo': new Date("2013-10-20"), // Date | 
  'projectId': "projectId_example" // String | 
};
apiInstance.getExpensesSalesPrice(opts, (error, data, response) => {
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
 **dateFrom** | **Date**|  | [optional] 
 **dateTo** | **Date**|  | [optional] 
 **projectId** | **String**|  | [optional] 

### Return type

[**GetExpensesSalesPrice200Response**](GetExpensesSalesPrice200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFinancialStatistics

> GetFinancialStatistics200Response getFinancialStatistics(opts)

Get general statistics

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.FinancialStatisticsApi();
let opts = {
  'dateFrom': new Date("2013-10-20"), // Date | 
  'dateTo': new Date("2013-10-20"), // Date | 
  'projectId': "projectId_example", // String | 
  'projectStatusIds': "projectStatusIds_example", // String | 
  'onlyNotInvoiced': true, // Boolean | 
  'details': true // Boolean | 
};
apiInstance.getFinancialStatistics(opts, (error, data, response) => {
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
 **dateFrom** | **Date**|  | [optional] 
 **dateTo** | **Date**|  | [optional] 
 **projectId** | **String**|  | [optional] 
 **projectStatusIds** | **String**|  | [optional] 
 **onlyNotInvoiced** | **Boolean**|  | [optional] 
 **details** | **Boolean**|  | [optional] 

### Return type

[**GetFinancialStatistics200Response**](GetFinancialStatistics200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFinancialStatisticsOverview

> GetFinancialStatisticsOverview200Response getFinancialStatisticsOverview(opts)

Get statistics overview

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.FinancialStatisticsApi();
let opts = {
  'dateFrom': new Date("2013-10-20"), // Date | 
  'dateTo': new Date("2013-10-20"), // Date | 
  'projectId': "projectId_example" // String | 
};
apiInstance.getFinancialStatisticsOverview(opts, (error, data, response) => {
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
 **dateFrom** | **Date**|  | [optional] 
 **dateTo** | **Date**|  | [optional] 
 **projectId** | **String**|  | [optional] 

### Return type

[**GetFinancialStatisticsOverview200Response**](GetFinancialStatisticsOverview200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInvoicedAmount

> GetInvoicedAmount200Response getInvoicedAmount(opts)

Get invoiced amount

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.FinancialStatisticsApi();
let opts = {
  'dateFrom': new Date("2013-10-20"), // Date | 
  'dateTo': new Date("2013-10-20"), // Date | 
  'projectId': "projectId_example" // String | 
};
apiInstance.getInvoicedAmount(opts, (error, data, response) => {
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
 **dateFrom** | **Date**|  | [optional] 
 **dateTo** | **Date**|  | [optional] 
 **projectId** | **String**|  | [optional] 

### Return type

[**GetInvoicedAmount200Response**](GetInvoicedAmount200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMargin

> GetMargin200Response getMargin(opts)

Get margin

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.FinancialStatisticsApi();
let opts = {
  'dateFrom': new Date("2013-10-20"), // Date | 
  'dateTo': new Date("2013-10-20"), // Date | 
  'projectId': "projectId_example" // String | 
};
apiInstance.getMargin(opts, (error, data, response) => {
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
 **dateFrom** | **Date**|  | [optional] 
 **dateTo** | **Date**|  | [optional] 
 **projectId** | **String**|  | [optional] 

### Return type

[**GetMargin200Response**](GetMargin200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMaterialRentalsCostPrice

> GetMaterialRentalsCostPrice200Response getMaterialRentalsCostPrice(opts)

Get products material rentals cost price

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.FinancialStatisticsApi();
let opts = {
  'dateFrom': new Date("2013-10-20"), // Date | 
  'dateTo': new Date("2013-10-20"), // Date | 
  'projectId': "projectId_example" // String | 
};
apiInstance.getMaterialRentalsCostPrice(opts, (error, data, response) => {
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
 **dateFrom** | **Date**|  | [optional] 
 **dateTo** | **Date**|  | [optional] 
 **projectId** | **String**|  | [optional] 

### Return type

[**GetMaterialRentalsCostPrice200Response**](GetMaterialRentalsCostPrice200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProductsCostPrice

> GetProductsCostPrice200Response getProductsCostPrice(opts)

Get products cost price

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.FinancialStatisticsApi();
let opts = {
  'dateFrom': new Date("2013-10-20"), // Date | 
  'dateTo': new Date("2013-10-20"), // Date | 
  'projectId': "projectId_example" // String | 
};
apiInstance.getProductsCostPrice(opts, (error, data, response) => {
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
 **dateFrom** | **Date**|  | [optional] 
 **dateTo** | **Date**|  | [optional] 
 **projectId** | **String**|  | [optional] 

### Return type

[**GetProductsCostPrice200Response**](GetProductsCostPrice200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

