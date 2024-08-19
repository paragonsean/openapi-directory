# KycApiDocumentation.V1PepsanctionApi

All URIs are relative to *https://api.kompany.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pepMonitorList**](V1PepsanctionApi.md#pepMonitorList) | **GET** /api/v1/pepsanction/monitor/list | Retrieves a list of monitor entries
[**pepMonitorUnregister**](V1PepsanctionApi.md#pepMonitorUnregister) | **POST** /api/v1/pepsanction/monitor/unregister/{id} | Deactive a pep sanction monitor
[**pepMonitorUpdate**](V1PepsanctionApi.md#pepMonitorUpdate) | **POST** /api/v1/pepsanction/monitor/update/{id} | Update details of active Pep Sanction monitor
[**pepOrder**](V1PepsanctionApi.md#pepOrder) | **POST** /api/v1/pepsanction/order/{type}/{search} | Orders a new Pep Sanction Check Report
[**pepRetrieve**](V1PepsanctionApi.md#pepRetrieve) | **GET** /api/v1/pepsanction/retrieve/{id} | Returns a json or pdf report



## pepMonitorList

> [PepMonitorList200ResponseInner] pepMonitorList()

Retrieves a list of monitor entries

Retrieve a list of all active Pep Sanction Report monitors for this account

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1PepsanctionApi();
apiInstance.pepMonitorList((error, data, response) => {
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

[**[PepMonitorList200ResponseInner]**](PepMonitorList200ResponseInner.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pepMonitorUnregister

> pepMonitorUnregister(id)

Deactive a pep sanction monitor

Unregister a previously created Pep Sanction Report Monitor

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1PepsanctionApi();
let id = "id_example"; // String | The identifier of the Monitor
apiInstance.pepMonitorUnregister(id, (error, data, response) => {
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
 **id** | **String**| The identifier of the Monitor | 

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## pepMonitorUpdate

> PepMonitorList200ResponseInner pepMonitorUpdate(id, opts)

Update details of active Pep Sanction monitor

Update the webhook URL of an active Pep Sanction Report Monitor

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1PepsanctionApi();
let id = "id_example"; // String | The identifier of the Monitor
let opts = {
  'webhook': "webhook_example" // String | If Monitoring is enabled this parameter is required. This is where updates will be sent to
};
apiInstance.pepMonitorUpdate(id, opts, (error, data, response) => {
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
 **id** | **String**| The identifier of the Monitor | 
 **webhook** | **String**| If Monitoring is enabled this parameter is required. This is where updates will be sent to | [optional] 

### Return type

[**PepMonitorList200ResponseInner**](PepMonitorList200ResponseInner.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## pepOrder

> pepOrder(type, search, opts)

Orders a new Pep Sanction Check Report

Order a new Pep Sanction Check by providing either a business or person name with some additional optional parameters.

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1PepsanctionApi();
let type = "type_example"; // String | Type (Business or Person) of the requested Pep Sanction Check
let search = "search_example"; // String | Search string for the Pep Sanction Check
let opts = {
  'aliases': "aliases_example", // String | Optional parameter for declaring alias names when doing a person search (seperated by commas)
  'country': "country_example", // String | Optional name of Country to assist in identifying matches based upon location/geography.
  'DOB': "DOB_example", // String | Optional parameter for date of birth name when doing a person search
  'familyName': "familyName_example", // String | Optional parameter for last name when doing a person search
  'filters': "filters_example", // String | Optional parameter for restricting search when doing a person search (seperated by commas)
  'givenName': "givenName_example", // String | Optional parameter for first name when doing a person search
  'LEI': "LEI_example", // String | Optional Legal Entity Identifier for additional business identifier verification.
  'locale': "locale_example", // String | Optional name of City or Locale to assist in identifying matches based upon location/geography.
  'medialists': "medialists_example", // String | Optional parameter for selecting only specific media lists. By default all lists are queried
  'middleName': "middleName_example", // String | Optional parameter for middle name when doing a person search
  'monitoring': true, // Boolean | If this Pep Sanction Check should be continuesly monitored.
  'peplists': "peplists_example", // String | Optional parameter for selecting only specific pep lists. By default all lists are queried
  'region': "region_example", // String | Optional name of Region or State to assist in identifying matches based upon location/geography.
  'smartMatch': true, // Boolean | Optional parameter for enabling SmartMatch to retrieve more results
  'watchlists': "watchlists_example", // String | Optional parameter for selecting only specific watch lists. By default all lists are queried
  'webhook': "webhook_example" // String | If Monitoring is enabled this parameter is required. This is where updates will be sent to
};
apiInstance.pepOrder(type, search, opts, (error, data, response) => {
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
 **type** | **String**| Type (Business or Person) of the requested Pep Sanction Check | 
 **search** | **String**| Search string for the Pep Sanction Check | 
 **aliases** | **String**| Optional parameter for declaring alias names when doing a person search (seperated by commas) | [optional] 
 **country** | **String**| Optional name of Country to assist in identifying matches based upon location/geography. | [optional] 
 **DOB** | **String**| Optional parameter for date of birth name when doing a person search | [optional] 
 **familyName** | **String**| Optional parameter for last name when doing a person search | [optional] 
 **filters** | **String**| Optional parameter for restricting search when doing a person search (seperated by commas) | [optional] 
 **givenName** | **String**| Optional parameter for first name when doing a person search | [optional] 
 **LEI** | **String**| Optional Legal Entity Identifier for additional business identifier verification. | [optional] 
 **locale** | **String**| Optional name of City or Locale to assist in identifying matches based upon location/geography. | [optional] 
 **medialists** | **String**| Optional parameter for selecting only specific media lists. By default all lists are queried | [optional] 
 **middleName** | **String**| Optional parameter for middle name when doing a person search | [optional] 
 **monitoring** | **Boolean**| If this Pep Sanction Check should be continuesly monitored. | [optional] 
 **peplists** | **String**| Optional parameter for selecting only specific pep lists. By default all lists are queried | [optional] 
 **region** | **String**| Optional name of Region or State to assist in identifying matches based upon location/geography. | [optional] 
 **smartMatch** | **Boolean**| Optional parameter for enabling SmartMatch to retrieve more results | [optional] 
 **watchlists** | **String**| Optional parameter for selecting only specific watch lists. By default all lists are queried | [optional] 
 **webhook** | **String**| If Monitoring is enabled this parameter is required. This is where updates will be sent to | [optional] 

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## pepRetrieve

> PepRetrieve200Response pepRetrieve(id, opts)

Returns a json or pdf report

Retrieve a completed Pep Sanction check structured or in pdf depending on given accept header

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1PepsanctionApi();
let id = "id_example"; // String | The id of the ordered Pep Sanction Check (id as returned by orderPepSanction call)
let opts = {
  'accept': "'application/json'" // String | The type (pdf or json) in which the check should be returned
};
apiInstance.pepRetrieve(id, opts, (error, data, response) => {
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
 **id** | **String**| The id of the ordered Pep Sanction Check (id as returned by orderPepSanction call) | 
 **accept** | **String**| The type (pdf or json) in which the check should be returned | [optional] [default to &#39;application/json&#39;]

### Return type

[**PepRetrieve200Response**](PepRetrieve200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

