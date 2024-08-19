# YnabApiEndpoints.PayeeLocationsApi

All URIs are relative to *https://api.ynab.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPayeeLocationById**](PayeeLocationsApi.md#getPayeeLocationById) | **GET** /budgets/{budget_id}/payee_locations/{payee_location_id} | Single payee location
[**getPayeeLocations**](PayeeLocationsApi.md#getPayeeLocations) | **GET** /budgets/{budget_id}/payee_locations | List payee locations
[**getPayeeLocationsByPayee**](PayeeLocationsApi.md#getPayeeLocationsByPayee) | **GET** /budgets/{budget_id}/payees/{payee_id}/payee_locations | List locations for a payee



## getPayeeLocationById

> PayeeLocationResponse getPayeeLocationById(budgetId, payeeLocationId)

Single payee location

Returns a single payee location

### Example

```javascript
import YnabApiEndpoints from 'ynab_api_endpoints';
let defaultClient = YnabApiEndpoints.ApiClient.instance;
// Configure API key authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//bearer.apiKeyPrefix = 'Token';

let apiInstance = new YnabApiEndpoints.PayeeLocationsApi();
let budgetId = "budgetId_example"; // String | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).
let payeeLocationId = "payeeLocationId_example"; // String | id of payee location
apiInstance.getPayeeLocationById(budgetId, payeeLocationId, (error, data, response) => {
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
 **budgetId** | **String**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget). | 
 **payeeLocationId** | **String**| id of payee location | 

### Return type

[**PayeeLocationResponse**](PayeeLocationResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPayeeLocations

> PayeeLocationsResponse getPayeeLocations(budgetId)

List payee locations

Returns all payee locations

### Example

```javascript
import YnabApiEndpoints from 'ynab_api_endpoints';
let defaultClient = YnabApiEndpoints.ApiClient.instance;
// Configure API key authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//bearer.apiKeyPrefix = 'Token';

let apiInstance = new YnabApiEndpoints.PayeeLocationsApi();
let budgetId = "budgetId_example"; // String | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).
apiInstance.getPayeeLocations(budgetId, (error, data, response) => {
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
 **budgetId** | **String**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget). | 

### Return type

[**PayeeLocationsResponse**](PayeeLocationsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPayeeLocationsByPayee

> PayeeLocationsResponse getPayeeLocationsByPayee(budgetId, payeeId)

List locations for a payee

Returns all payee locations for a specified payee

### Example

```javascript
import YnabApiEndpoints from 'ynab_api_endpoints';
let defaultClient = YnabApiEndpoints.ApiClient.instance;
// Configure API key authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//bearer.apiKeyPrefix = 'Token';

let apiInstance = new YnabApiEndpoints.PayeeLocationsApi();
let budgetId = "budgetId_example"; // String | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).
let payeeId = "payeeId_example"; // String | id of payee
apiInstance.getPayeeLocationsByPayee(budgetId, payeeId, (error, data, response) => {
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
 **budgetId** | **String**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget). | 
 **payeeId** | **String**| id of payee | 

### Return type

[**PayeeLocationsResponse**](PayeeLocationsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

