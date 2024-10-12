# MerakiDashboardApi.ArtifactsApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createOrganizationCameraCustomAnalyticsArtifact_2**](ArtifactsApi.md#createOrganizationCameraCustomAnalyticsArtifact_2) | **POST** /organizations/{organizationId}/camera/customAnalytics/artifacts | Create custom analytics artifact
[**deleteOrganizationCameraCustomAnalyticsArtifact_2**](ArtifactsApi.md#deleteOrganizationCameraCustomAnalyticsArtifact_2) | **DELETE** /organizations/{organizationId}/camera/customAnalytics/artifacts/{artifactId} | Delete Custom Analytics Artifact
[**getOrganizationCameraCustomAnalyticsArtifact_2**](ArtifactsApi.md#getOrganizationCameraCustomAnalyticsArtifact_2) | **GET** /organizations/{organizationId}/camera/customAnalytics/artifacts/{artifactId} | Get Custom Analytics Artifact
[**getOrganizationCameraCustomAnalyticsArtifacts_2**](ArtifactsApi.md#getOrganizationCameraCustomAnalyticsArtifacts_2) | **GET** /organizations/{organizationId}/camera/customAnalytics/artifacts | List Custom Analytics Artifacts



## createOrganizationCameraCustomAnalyticsArtifact_2

> Object createOrganizationCameraCustomAnalyticsArtifact_2(organizationId, opts)

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

let apiInstance = new MerakiDashboardApi.ArtifactsApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'createOrganizationCameraCustomAnalyticsArtifactRequest': new MerakiDashboardApi.CreateOrganizationCameraCustomAnalyticsArtifactRequest() // CreateOrganizationCameraCustomAnalyticsArtifactRequest | 
};
apiInstance.createOrganizationCameraCustomAnalyticsArtifact_2(organizationId, opts, (error, data, response) => {
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


## deleteOrganizationCameraCustomAnalyticsArtifact_2

> deleteOrganizationCameraCustomAnalyticsArtifact_2(organizationId, artifactId)

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

let apiInstance = new MerakiDashboardApi.ArtifactsApi();
let organizationId = "organizationId_example"; // String | 
let artifactId = "artifactId_example"; // String | 
apiInstance.deleteOrganizationCameraCustomAnalyticsArtifact_2(organizationId, artifactId, (error, data, response) => {
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


## getOrganizationCameraCustomAnalyticsArtifact_2

> Object getOrganizationCameraCustomAnalyticsArtifact_2(organizationId, artifactId)

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

let apiInstance = new MerakiDashboardApi.ArtifactsApi();
let organizationId = "organizationId_example"; // String | 
let artifactId = "artifactId_example"; // String | 
apiInstance.getOrganizationCameraCustomAnalyticsArtifact_2(organizationId, artifactId, (error, data, response) => {
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


## getOrganizationCameraCustomAnalyticsArtifacts_2

> [Object] getOrganizationCameraCustomAnalyticsArtifacts_2(organizationId)

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

let apiInstance = new MerakiDashboardApi.ArtifactsApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationCameraCustomAnalyticsArtifacts_2(organizationId, (error, data, response) => {
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

