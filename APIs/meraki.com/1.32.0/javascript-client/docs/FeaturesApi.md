# MerakiDashboardApi.FeaturesApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createOrganizationEarlyAccessFeaturesOptIn_2**](FeaturesApi.md#createOrganizationEarlyAccessFeaturesOptIn_2) | **POST** /organizations/{organizationId}/earlyAccess/features/optIns | Create a new early access feature opt-in for an organization
[**deleteOrganizationEarlyAccessFeaturesOptIn_2**](FeaturesApi.md#deleteOrganizationEarlyAccessFeaturesOptIn_2) | **DELETE** /organizations/{organizationId}/earlyAccess/features/optIns/{optInId} | Delete an early access feature opt-in
[**getOrganizationEarlyAccessFeaturesOptIn_2**](FeaturesApi.md#getOrganizationEarlyAccessFeaturesOptIn_2) | **GET** /organizations/{organizationId}/earlyAccess/features/optIns/{optInId} | Show an early access feature opt-in for an organization
[**getOrganizationEarlyAccessFeaturesOptIns_2**](FeaturesApi.md#getOrganizationEarlyAccessFeaturesOptIns_2) | **GET** /organizations/{organizationId}/earlyAccess/features/optIns | List the early access feature opt-ins for an organization
[**getOrganizationEarlyAccessFeatures_2**](FeaturesApi.md#getOrganizationEarlyAccessFeatures_2) | **GET** /organizations/{organizationId}/earlyAccess/features | List the available early access features for organization
[**updateOrganizationEarlyAccessFeaturesOptIn_2**](FeaturesApi.md#updateOrganizationEarlyAccessFeaturesOptIn_2) | **PUT** /organizations/{organizationId}/earlyAccess/features/optIns/{optInId} | Update an early access feature opt-in for an organization



## createOrganizationEarlyAccessFeaturesOptIn_2

> Object createOrganizationEarlyAccessFeaturesOptIn_2(organizationId, createOrganizationEarlyAccessFeaturesOptInRequest)

Create a new early access feature opt-in for an organization

Create a new early access feature opt-in for an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.FeaturesApi();
let organizationId = "organizationId_example"; // String | 
let createOrganizationEarlyAccessFeaturesOptInRequest = new MerakiDashboardApi.CreateOrganizationEarlyAccessFeaturesOptInRequest(); // CreateOrganizationEarlyAccessFeaturesOptInRequest | 
apiInstance.createOrganizationEarlyAccessFeaturesOptIn_2(organizationId, createOrganizationEarlyAccessFeaturesOptInRequest, (error, data, response) => {
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
 **organizationId** | **String**|  | 
 **createOrganizationEarlyAccessFeaturesOptInRequest** | [**CreateOrganizationEarlyAccessFeaturesOptInRequest**](CreateOrganizationEarlyAccessFeaturesOptInRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteOrganizationEarlyAccessFeaturesOptIn_2

> deleteOrganizationEarlyAccessFeaturesOptIn_2(organizationId, optInId)

Delete an early access feature opt-in

Delete an early access feature opt-in

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.FeaturesApi();
let organizationId = "organizationId_example"; // String | 
let optInId = "optInId_example"; // String | 
apiInstance.deleteOrganizationEarlyAccessFeaturesOptIn_2(organizationId, optInId, (error, data, response) => {
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
 **organizationId** | **String**|  | 
 **optInId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrganizationEarlyAccessFeaturesOptIn_2

> Object getOrganizationEarlyAccessFeaturesOptIn_2(organizationId, optInId)

Show an early access feature opt-in for an organization

Show an early access feature opt-in for an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.FeaturesApi();
let organizationId = "organizationId_example"; // String | 
let optInId = "optInId_example"; // String | 
apiInstance.getOrganizationEarlyAccessFeaturesOptIn_2(organizationId, optInId, (error, data, response) => {
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
 **organizationId** | **String**|  | 
 **optInId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationEarlyAccessFeaturesOptIns_2

> [Object] getOrganizationEarlyAccessFeaturesOptIns_2(organizationId)

List the early access feature opt-ins for an organization

List the early access feature opt-ins for an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.FeaturesApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationEarlyAccessFeaturesOptIns_2(organizationId, (error, data, response) => {
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
 **organizationId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationEarlyAccessFeatures_2

> [Object] getOrganizationEarlyAccessFeatures_2(organizationId)

List the available early access features for organization

List the available early access features for organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.FeaturesApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationEarlyAccessFeatures_2(organizationId, (error, data, response) => {
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
 **organizationId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateOrganizationEarlyAccessFeaturesOptIn_2

> Object updateOrganizationEarlyAccessFeaturesOptIn_2(organizationId, optInId, opts)

Update an early access feature opt-in for an organization

Update an early access feature opt-in for an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.FeaturesApi();
let organizationId = "organizationId_example"; // String | 
let optInId = "optInId_example"; // String | 
let opts = {
  'updateOrganizationEarlyAccessFeaturesOptInRequest': new MerakiDashboardApi.UpdateOrganizationEarlyAccessFeaturesOptInRequest() // UpdateOrganizationEarlyAccessFeaturesOptInRequest | 
};
apiInstance.updateOrganizationEarlyAccessFeaturesOptIn_2(organizationId, optInId, opts, (error, data, response) => {
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
 **organizationId** | **String**|  | 
 **optInId** | **String**|  | 
 **updateOrganizationEarlyAccessFeaturesOptInRequest** | [**UpdateOrganizationEarlyAccessFeaturesOptInRequest**](UpdateOrganizationEarlyAccessFeaturesOptInRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

