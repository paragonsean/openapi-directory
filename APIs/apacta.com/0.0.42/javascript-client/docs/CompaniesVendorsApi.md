# Apacta.CompaniesVendorsApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addCompaniesVendor**](CompaniesVendorsApi.md#addCompaniesVendor) | **POST** /companies_vendors | Add a new companies vendor
[**bulkCompaniesVendors**](CompaniesVendorsApi.md#bulkCompaniesVendors) | **DELETE** /companies_vendors/bulkDelete | Bulk delete companies vendors
[**companiesVendorsCompaniesVendorIdDelete**](CompaniesVendorsApi.md#companiesVendorsCompaniesVendorIdDelete) | **DELETE** /companies_vendors/{companies_vendor_id} | Delete a companies vendor
[**editCompaniesVendor**](CompaniesVendorsApi.md#editCompaniesVendor) | **PUT** /companies_vendors/{companies_vendor_id} | Edit a companies vendor
[**getCompaiesVendorsList**](CompaniesVendorsApi.md#getCompaiesVendorsList) | **GET** /companies_vendors | Get a list of companies vendors
[**getCompaniesVendor**](CompaniesVendorsApi.md#getCompaniesVendor) | **GET** /companies_vendors/{companies_vendor_id} | Get a companies vendor
[**getCompaniesVendorsExpenseStatistics**](CompaniesVendorsApi.md#getCompaniesVendorsExpenseStatistics) | **GET** /companies_vendors/{companies_vendor_id}/expense_statistics | Get companies vendor expense statistics



## addCompaniesVendor

> ClockingRecordsPost201Response addCompaniesVendor(opts)

Add a new companies vendor

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

let apiInstance = new Apacta.CompaniesVendorsApi();
let opts = {
  'addCompaniesVendorRequest': new Apacta.AddCompaniesVendorRequest() // AddCompaniesVendorRequest | 
};
apiInstance.addCompaniesVendor(opts, (error, data, response) => {
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
 **addCompaniesVendorRequest** | [**AddCompaniesVendorRequest**](AddCompaniesVendorRequest.md)|  | [optional] 

### Return type

[**ClockingRecordsPost201Response**](ClockingRecordsPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bulkCompaniesVendors

> EmptySuccessResponse bulkCompaniesVendors(bulkActionRequestBody)

Bulk delete companies vendors

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

let apiInstance = new Apacta.CompaniesVendorsApi();
let bulkActionRequestBody = new Apacta.BulkActionRequestBody(); // BulkActionRequestBody | Companies vendors ids
apiInstance.bulkCompaniesVendors(bulkActionRequestBody, (error, data, response) => {
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
 **bulkActionRequestBody** | [**BulkActionRequestBody**](BulkActionRequestBody.md)| Companies vendors ids | 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## companiesVendorsCompaniesVendorIdDelete

> ClockingRecordsClockingRecordIdDelete200Response companiesVendorsCompaniesVendorIdDelete(companiesVendorId)

Delete a companies vendor

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

let apiInstance = new Apacta.CompaniesVendorsApi();
let companiesVendorId = "companiesVendorId_example"; // String | 
apiInstance.companiesVendorsCompaniesVendorIdDelete(companiesVendorId, (error, data, response) => {
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
 **companiesVendorId** | **String**|  | 

### Return type

[**ClockingRecordsClockingRecordIdDelete200Response**](ClockingRecordsClockingRecordIdDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## editCompaniesVendor

> ClockingRecordsClockingRecordIdPut200Response editCompaniesVendor(companiesVendorId, opts)

Edit a companies vendor

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

let apiInstance = new Apacta.CompaniesVendorsApi();
let companiesVendorId = "companiesVendorId_example"; // String | 
let opts = {
  'addCompaniesVendorRequest': new Apacta.AddCompaniesVendorRequest() // AddCompaniesVendorRequest | 
};
apiInstance.editCompaniesVendor(companiesVendorId, opts, (error, data, response) => {
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
 **companiesVendorId** | **String**|  | 
 **addCompaniesVendorRequest** | [**AddCompaniesVendorRequest**](AddCompaniesVendorRequest.md)|  | [optional] 

### Return type

[**ClockingRecordsClockingRecordIdPut200Response**](ClockingRecordsClockingRecordIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getCompaiesVendorsList

> GetCompaiesVendorsList200Response getCompaiesVendorsList()

Get a list of companies vendors

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

let apiInstance = new Apacta.CompaniesVendorsApi();
apiInstance.getCompaiesVendorsList((error, data, response) => {
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

[**GetCompaiesVendorsList200Response**](GetCompaiesVendorsList200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCompaniesVendor

> GetCompaniesVendor200Response getCompaniesVendor(companiesVendorId)

Get a companies vendor

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

let apiInstance = new Apacta.CompaniesVendorsApi();
let companiesVendorId = "companiesVendorId_example"; // String | 
apiInstance.getCompaniesVendor(companiesVendorId, (error, data, response) => {
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
 **companiesVendorId** | **String**|  | 

### Return type

[**GetCompaniesVendor200Response**](GetCompaniesVendor200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCompaniesVendorsExpenseStatistics

> GetCompaniesVendorsExpenseStatistics200Response getCompaniesVendorsExpenseStatistics(companiesVendorId)

Get companies vendor expense statistics

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

let apiInstance = new Apacta.CompaniesVendorsApi();
let companiesVendorId = "companiesVendorId_example"; // String | 
apiInstance.getCompaniesVendorsExpenseStatistics(companiesVendorId, (error, data, response) => {
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
 **companiesVendorId** | **String**|  | 

### Return type

[**GetCompaniesVendorsExpenseStatistics200Response**](GetCompaniesVendorsExpenseStatistics200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

