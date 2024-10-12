# AppCenterClient.BillingApi

All URIs are relative to *https://api.appcenter.ms*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billingAggregatedInformationGetAll**](BillingApi.md#billingAggregatedInformationGetAll) | **GET** /v0.1/billing/allAccountsAggregated | 
[**billingAggregatedInformationGetByApp**](BillingApi.md#billingAggregatedInformationGetByApp) | **GET** /v0.1/apps/{owner_name}/{app_name}/billing/aggregated | 
[**billingAggregatedInformationGetForOrg**](BillingApi.md#billingAggregatedInformationGetForOrg) | **GET** /v0.1/orgs/{orgName}/billing/aggregated | 



## billingAggregatedInformationGetAll

> BillingAggregatedInformationGetAll200Response billingAggregatedInformationGetAll(opts)



Aggregated Billing Information for the requesting user and the organizations in which the user is an admin.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.BillingApi();
let opts = {
  'service': "service_example", // String | Type of service that should be included in the Billing Information
  'period': "period_example", // String | Type of period that should be included in the Billing Information
  'showOriginalPlans': true // Boolean | Controls whether the API should show the original plan when Azure Subscription is not enabled
};
apiInstance.billingAggregatedInformationGetAll(opts, (error, data, response) => {
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
 **service** | **String**| Type of service that should be included in the Billing Information | [optional] 
 **period** | **String**| Type of period that should be included in the Billing Information | [optional] 
 **showOriginalPlans** | **Boolean**| Controls whether the API should show the original plan when Azure Subscription is not enabled | [optional] 

### Return type

[**BillingAggregatedInformationGetAll200Response**](BillingAggregatedInformationGetAll200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingAggregatedInformationGetByApp

> BillingAggregatedInformationGetByApp200Response billingAggregatedInformationGetByApp(ownerName, appName, opts)



Aggregated Billing Information for owner of a given app.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.BillingApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'service': "service_example", // String | Type of service that should be included in the Billing Information
  'period': "period_example", // String | Type of period that should be included in the Billing Information
  'showOriginalPlans': true // Boolean | Controls whether the API should show the original plan when Azure Subscription is not enabled
};
apiInstance.billingAggregatedInformationGetByApp(ownerName, appName, opts, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **service** | **String**| Type of service that should be included in the Billing Information | [optional] 
 **period** | **String**| Type of period that should be included in the Billing Information | [optional] 
 **showOriginalPlans** | **Boolean**| Controls whether the API should show the original plan when Azure Subscription is not enabled | [optional] 

### Return type

[**BillingAggregatedInformationGetByApp200Response**](BillingAggregatedInformationGetByApp200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingAggregatedInformationGetForOrg

> BillingAggregatedInformationGetByApp200Response billingAggregatedInformationGetForOrg(orgName, opts)



Aggregated Billing Information for a given Organization.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.BillingApi();
let orgName = "orgName_example"; // String | The name of the Organization
let opts = {
  'service': "service_example", // String | Type of service that should be included in the Billing Information
  'period': "period_example", // String | Type of period that should be included in the Billing Information
  'showOriginalPlans': true // Boolean | Controls whether the API should show the original plan when Azure Subscription is not enabled
};
apiInstance.billingAggregatedInformationGetForOrg(orgName, opts, (error, data, response) => {
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
 **orgName** | **String**| The name of the Organization | 
 **service** | **String**| Type of service that should be included in the Billing Information | [optional] 
 **period** | **String**| Type of period that should be included in the Billing Information | [optional] 
 **showOriginalPlans** | **Boolean**| Controls whether the API should show the original plan when Azure Subscription is not enabled | [optional] 

### Return type

[**BillingAggregatedInformationGetByApp200Response**](BillingAggregatedInformationGetByApp200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

