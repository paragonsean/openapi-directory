# MerakiDashboardApi.ImportsApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createOrganizationInventoryOnboardingCloudMonitoringImport_4**](ImportsApi.md#createOrganizationInventoryOnboardingCloudMonitoringImport_4) | **POST** /organizations/{organizationId}/inventory/onboarding/cloudMonitoring/imports | Commits the import operation to complete the onboarding of a device into Dashboard for monitoring.
[**getOrganizationInventoryOnboardingCloudMonitoringImports_4**](ImportsApi.md#getOrganizationInventoryOnboardingCloudMonitoringImports_4) | **GET** /organizations/{organizationId}/inventory/onboarding/cloudMonitoring/imports | Check the status of a committed Import operation



## createOrganizationInventoryOnboardingCloudMonitoringImport_4

> [CreateOrganizationInventoryOnboardingCloudMonitoringImport201ResponseInner] createOrganizationInventoryOnboardingCloudMonitoringImport_4(organizationId, createOrganizationInventoryOnboardingCloudMonitoringImportRequest)

Commits the import operation to complete the onboarding of a device into Dashboard for monitoring.

Commits the import operation to complete the onboarding of a device into Dashboard for monitoring.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ImportsApi();
let organizationId = "organizationId_example"; // String | 
let createOrganizationInventoryOnboardingCloudMonitoringImportRequest = new MerakiDashboardApi.CreateOrganizationInventoryOnboardingCloudMonitoringImportRequest(); // CreateOrganizationInventoryOnboardingCloudMonitoringImportRequest | 
apiInstance.createOrganizationInventoryOnboardingCloudMonitoringImport_4(organizationId, createOrganizationInventoryOnboardingCloudMonitoringImportRequest, (error, data, response) => {
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
 **createOrganizationInventoryOnboardingCloudMonitoringImportRequest** | [**CreateOrganizationInventoryOnboardingCloudMonitoringImportRequest**](CreateOrganizationInventoryOnboardingCloudMonitoringImportRequest.md)|  | 

### Return type

[**[CreateOrganizationInventoryOnboardingCloudMonitoringImport201ResponseInner]**](CreateOrganizationInventoryOnboardingCloudMonitoringImport201ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getOrganizationInventoryOnboardingCloudMonitoringImports_4

> [GetOrganizationInventoryOnboardingCloudMonitoringImports200ResponseInner] getOrganizationInventoryOnboardingCloudMonitoringImports_4(organizationId, importIds)

Check the status of a committed Import operation

Check the status of a committed Import operation

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ImportsApi();
let organizationId = "organizationId_example"; // String | 
let importIds = ["null"]; // [String] | import ids from an imports
apiInstance.getOrganizationInventoryOnboardingCloudMonitoringImports_4(organizationId, importIds, (error, data, response) => {
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
 **importIds** | [**[String]**](String.md)| import ids from an imports | 

### Return type

[**[GetOrganizationInventoryOnboardingCloudMonitoringImports200ResponseInner]**](GetOrganizationInventoryOnboardingCloudMonitoringImports200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

