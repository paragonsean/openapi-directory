# MerakiDashboardApi.OnboardingApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createOrganizationInventoryOnboardingCloudMonitoringExportEvent_2**](OnboardingApi.md#createOrganizationInventoryOnboardingCloudMonitoringExportEvent_2) | **POST** /organizations/{organizationId}/inventory/onboarding/cloudMonitoring/exportEvents | Imports event logs related to the onboarding app into elastisearch
[**createOrganizationInventoryOnboardingCloudMonitoringImport_2**](OnboardingApi.md#createOrganizationInventoryOnboardingCloudMonitoringImport_2) | **POST** /organizations/{organizationId}/inventory/onboarding/cloudMonitoring/imports | Commits the import operation to complete the onboarding of a device into Dashboard for monitoring.
[**createOrganizationInventoryOnboardingCloudMonitoringPrepare_2**](OnboardingApi.md#createOrganizationInventoryOnboardingCloudMonitoringPrepare_2) | **POST** /organizations/{organizationId}/inventory/onboarding/cloudMonitoring/prepare | Initiates or updates an import session
[**getOrganizationCameraOnboardingStatuses_1**](OnboardingApi.md#getOrganizationCameraOnboardingStatuses_1) | **GET** /organizations/{organizationId}/camera/onboarding/statuses | Fetch onboarding status of cameras
[**getOrganizationInventoryOnboardingCloudMonitoringImports_2**](OnboardingApi.md#getOrganizationInventoryOnboardingCloudMonitoringImports_2) | **GET** /organizations/{organizationId}/inventory/onboarding/cloudMonitoring/imports | Check the status of a committed Import operation
[**getOrganizationInventoryOnboardingCloudMonitoringNetworks_2**](OnboardingApi.md#getOrganizationInventoryOnboardingCloudMonitoringNetworks_2) | **GET** /organizations/{organizationId}/inventory/onboarding/cloudMonitoring/networks | Returns list of networks eligible for adding cloud monitored device
[**updateOrganizationCameraOnboardingStatuses_1**](OnboardingApi.md#updateOrganizationCameraOnboardingStatuses_1) | **PUT** /organizations/{organizationId}/camera/onboarding/statuses | Notify that credential handoff to camera has completed



## createOrganizationInventoryOnboardingCloudMonitoringExportEvent_2

> Object createOrganizationInventoryOnboardingCloudMonitoringExportEvent_2(organizationId, createOrganizationInventoryOnboardingCloudMonitoringExportEventRequest)

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

let apiInstance = new MerakiDashboardApi.OnboardingApi();
let organizationId = "organizationId_example"; // String | 
let createOrganizationInventoryOnboardingCloudMonitoringExportEventRequest = new MerakiDashboardApi.CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest(); // CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest | 
apiInstance.createOrganizationInventoryOnboardingCloudMonitoringExportEvent_2(organizationId, createOrganizationInventoryOnboardingCloudMonitoringExportEventRequest, (error, data, response) => {
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


## createOrganizationInventoryOnboardingCloudMonitoringImport_2

> [CreateOrganizationInventoryOnboardingCloudMonitoringImport201ResponseInner] createOrganizationInventoryOnboardingCloudMonitoringImport_2(organizationId, createOrganizationInventoryOnboardingCloudMonitoringImportRequest)

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

let apiInstance = new MerakiDashboardApi.OnboardingApi();
let organizationId = "organizationId_example"; // String | 
let createOrganizationInventoryOnboardingCloudMonitoringImportRequest = new MerakiDashboardApi.CreateOrganizationInventoryOnboardingCloudMonitoringImportRequest(); // CreateOrganizationInventoryOnboardingCloudMonitoringImportRequest | 
apiInstance.createOrganizationInventoryOnboardingCloudMonitoringImport_2(organizationId, createOrganizationInventoryOnboardingCloudMonitoringImportRequest, (error, data, response) => {
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


## createOrganizationInventoryOnboardingCloudMonitoringPrepare_2

> [CreateOrganizationInventoryOnboardingCloudMonitoringPrepare201ResponseInner] createOrganizationInventoryOnboardingCloudMonitoringPrepare_2(organizationId, createOrganizationInventoryOnboardingCloudMonitoringPrepareRequest)

Initiates or updates an import session

Initiates or updates an import session. An import ID will be generated and used when you are ready to commit the import.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.OnboardingApi();
let organizationId = "organizationId_example"; // String | 
let createOrganizationInventoryOnboardingCloudMonitoringPrepareRequest = new MerakiDashboardApi.CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequest(); // CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequest | 
apiInstance.createOrganizationInventoryOnboardingCloudMonitoringPrepare_2(organizationId, createOrganizationInventoryOnboardingCloudMonitoringPrepareRequest, (error, data, response) => {
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
 **createOrganizationInventoryOnboardingCloudMonitoringPrepareRequest** | [**CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequest**](CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequest.md)|  | 

### Return type

[**[CreateOrganizationInventoryOnboardingCloudMonitoringPrepare201ResponseInner]**](CreateOrganizationInventoryOnboardingCloudMonitoringPrepare201ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getOrganizationCameraOnboardingStatuses_1

> [Object] getOrganizationCameraOnboardingStatuses_1(organizationId, opts)

Fetch onboarding status of cameras

Fetch onboarding status of cameras

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.OnboardingApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'serials': ["null"], // [String] | A list of serial numbers. The returned cameras will be filtered to only include these serials.
  'networkIds': ["null"] // [String] | A list of network IDs. The returned cameras will be filtered to only include these networks.
};
apiInstance.getOrganizationCameraOnboardingStatuses_1(organizationId, opts, (error, data, response) => {
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
 **serials** | [**[String]**](String.md)| A list of serial numbers. The returned cameras will be filtered to only include these serials. | [optional] 
 **networkIds** | [**[String]**](String.md)| A list of network IDs. The returned cameras will be filtered to only include these networks. | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationInventoryOnboardingCloudMonitoringImports_2

> [GetOrganizationInventoryOnboardingCloudMonitoringImports200ResponseInner] getOrganizationInventoryOnboardingCloudMonitoringImports_2(organizationId, importIds)

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

let apiInstance = new MerakiDashboardApi.OnboardingApi();
let organizationId = "organizationId_example"; // String | 
let importIds = ["null"]; // [String] | import ids from an imports
apiInstance.getOrganizationInventoryOnboardingCloudMonitoringImports_2(organizationId, importIds, (error, data, response) => {
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


## getOrganizationInventoryOnboardingCloudMonitoringNetworks_2

> [GetNetwork200Response] getOrganizationInventoryOnboardingCloudMonitoringNetworks_2(organizationId, deviceType, opts)

Returns list of networks eligible for adding cloud monitored device

Returns list of networks eligible for adding cloud monitored device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.OnboardingApi();
let organizationId = "organizationId_example"; // String | 
let deviceType = "deviceType_example"; // String | Device Type switch or wireless controller
let opts = {
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 3 - 100000. Default is 1000.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example" // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
};
apiInstance.getOrganizationInventoryOnboardingCloudMonitoringNetworks_2(organizationId, deviceType, opts, (error, data, response) => {
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
 **deviceType** | **String**| Device Type switch or wireless controller | 
 **perPage** | **Number**| The number of entries per page returned. Acceptable range is 3 - 100000. Default is 1000. | [optional] 
 **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 

### Return type

[**[GetNetwork200Response]**](GetNetwork200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateOrganizationCameraOnboardingStatuses_1

> Object updateOrganizationCameraOnboardingStatuses_1(organizationId, opts)

Notify that credential handoff to camera has completed

Notify that credential handoff to camera has completed

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.OnboardingApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'updateOrganizationCameraOnboardingStatusesRequest': new MerakiDashboardApi.UpdateOrganizationCameraOnboardingStatusesRequest() // UpdateOrganizationCameraOnboardingStatusesRequest | 
};
apiInstance.updateOrganizationCameraOnboardingStatuses_1(organizationId, opts, (error, data, response) => {
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
 **updateOrganizationCameraOnboardingStatusesRequest** | [**UpdateOrganizationCameraOnboardingStatusesRequest**](UpdateOrganizationCameraOnboardingStatusesRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

