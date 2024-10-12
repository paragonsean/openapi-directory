# MerakiDashboardApi.ExportEventsApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createOrganizationInventoryOnboardingCloudMonitoringExportEvent_4**](ExportEventsApi.md#createOrganizationInventoryOnboardingCloudMonitoringExportEvent_4) | **POST** /organizations/{organizationId}/inventory/onboarding/cloudMonitoring/exportEvents | Imports event logs related to the onboarding app into elastisearch



## createOrganizationInventoryOnboardingCloudMonitoringExportEvent_4

> Object createOrganizationInventoryOnboardingCloudMonitoringExportEvent_4(organizationId, createOrganizationInventoryOnboardingCloudMonitoringExportEventRequest)

Imports event logs related to the onboarding app into elastisearch

Imports event logs related to the onboarding app into elastisearch

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ExportEventsApi();
let organizationId = "organizationId_example"; // String | 
let createOrganizationInventoryOnboardingCloudMonitoringExportEventRequest = new MerakiDashboardApi.CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest(); // CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest | 
apiInstance.createOrganizationInventoryOnboardingCloudMonitoringExportEvent_4(organizationId, createOrganizationInventoryOnboardingCloudMonitoringExportEventRequest, (error, data, response) => {
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
 **createOrganizationInventoryOnboardingCloudMonitoringExportEventRequest** | [**CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest**](CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

