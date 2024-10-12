# MerakiDashboardApi.CustomAnalyticsApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createOrganizationCameraCustomAnalyticsArtifact_1**](CustomAnalyticsApi.md#createOrganizationCameraCustomAnalyticsArtifact_1) | **POST** /organizations/{organizationId}/camera/customAnalytics/artifacts | Create custom analytics artifact
[**deleteOrganizationCameraCustomAnalyticsArtifact_1**](CustomAnalyticsApi.md#deleteOrganizationCameraCustomAnalyticsArtifact_1) | **DELETE** /organizations/{organizationId}/camera/customAnalytics/artifacts/{artifactId} | Delete Custom Analytics Artifact
[**getDeviceCameraCustomAnalytics_1**](CustomAnalyticsApi.md#getDeviceCameraCustomAnalytics_1) | **GET** /devices/{serial}/camera/customAnalytics | Return custom analytics settings for a camera
[**getOrganizationCameraCustomAnalyticsArtifact_1**](CustomAnalyticsApi.md#getOrganizationCameraCustomAnalyticsArtifact_1) | **GET** /organizations/{organizationId}/camera/customAnalytics/artifacts/{artifactId} | Get Custom Analytics Artifact
[**getOrganizationCameraCustomAnalyticsArtifacts_1**](CustomAnalyticsApi.md#getOrganizationCameraCustomAnalyticsArtifacts_1) | **GET** /organizations/{organizationId}/camera/customAnalytics/artifacts | List Custom Analytics Artifacts
[**updateDeviceCameraCustomAnalytics_1**](CustomAnalyticsApi.md#updateDeviceCameraCustomAnalytics_1) | **PUT** /devices/{serial}/camera/customAnalytics | Update custom analytics settings for a camera



## createOrganizationCameraCustomAnalyticsArtifact_1

> Object createOrganizationCameraCustomAnalyticsArtifact_1(organizationId, opts)

Create custom analytics artifact

Create custom analytics artifact. Returns an artifact upload URL with expiry time. Upload the artifact file with a put request to the returned upload URL before its expiry.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.CustomAnalyticsApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'createOrganizationCameraCustomAnalyticsArtifactRequest': new MerakiDashboardApi.CreateOrganizationCameraCustomAnalyticsArtifactRequest() // CreateOrganizationCameraCustomAnalyticsArtifactRequest | 
};
apiInstance.createOrganizationCameraCustomAnalyticsArtifact_1(organizationId, opts, (error, data, response) => {
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
 **createOrganizationCameraCustomAnalyticsArtifactRequest** | [**CreateOrganizationCameraCustomAnalyticsArtifactRequest**](CreateOrganizationCameraCustomAnalyticsArtifactRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteOrganizationCameraCustomAnalyticsArtifact_1

> deleteOrganizationCameraCustomAnalyticsArtifact_1(organizationId, artifactId)

Delete Custom Analytics Artifact

Delete Custom Analytics Artifact

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.CustomAnalyticsApi();
let organizationId = "organizationId_example"; // String | 
let artifactId = "artifactId_example"; // String | 
apiInstance.deleteOrganizationCameraCustomAnalyticsArtifact_1(organizationId, artifactId, (error, data, response) => {
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
 **artifactId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getDeviceCameraCustomAnalytics_1

> Object getDeviceCameraCustomAnalytics_1(serial)

Return custom analytics settings for a camera

Return custom analytics settings for a camera

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.CustomAnalyticsApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceCameraCustomAnalytics_1(serial, (error, data, response) => {
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
 **serial** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationCameraCustomAnalyticsArtifact_1

> Object getOrganizationCameraCustomAnalyticsArtifact_1(organizationId, artifactId)

Get Custom Analytics Artifact

Get Custom Analytics Artifact

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.CustomAnalyticsApi();
let organizationId = "organizationId_example"; // String | 
let artifactId = "artifactId_example"; // String | 
apiInstance.getOrganizationCameraCustomAnalyticsArtifact_1(organizationId, artifactId, (error, data, response) => {
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
 **artifactId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationCameraCustomAnalyticsArtifacts_1

> [Object] getOrganizationCameraCustomAnalyticsArtifacts_1(organizationId)

List Custom Analytics Artifacts

List Custom Analytics Artifacts

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.CustomAnalyticsApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationCameraCustomAnalyticsArtifacts_1(organizationId, (error, data, response) => {
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


## updateDeviceCameraCustomAnalytics_1

> Object updateDeviceCameraCustomAnalytics_1(serial, opts)

Update custom analytics settings for a camera

Update custom analytics settings for a camera

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.CustomAnalyticsApi();
let serial = "serial_example"; // String | 
let opts = {
  'updateDeviceCameraCustomAnalyticsRequest': new MerakiDashboardApi.UpdateDeviceCameraCustomAnalyticsRequest() // UpdateDeviceCameraCustomAnalyticsRequest | 
};
apiInstance.updateDeviceCameraCustomAnalytics_1(serial, opts, (error, data, response) => {
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
 **serial** | **String**|  | 
 **updateDeviceCameraCustomAnalyticsRequest** | [**UpdateDeviceCameraCustomAnalyticsRequest**](UpdateDeviceCameraCustomAnalyticsRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

