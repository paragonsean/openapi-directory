# MerakiDashboardApi.QualityRetentionProfilesApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNetworkCameraQualityRetentionProfile_1**](QualityRetentionProfilesApi.md#createNetworkCameraQualityRetentionProfile_1) | **POST** /networks/{networkId}/camera/qualityRetentionProfiles | Creates new quality retention profile for this network.
[**deleteNetworkCameraQualityRetentionProfile_1**](QualityRetentionProfilesApi.md#deleteNetworkCameraQualityRetentionProfile_1) | **DELETE** /networks/{networkId}/camera/qualityRetentionProfiles/{qualityRetentionProfileId} | Delete an existing quality retention profile for this network.
[**getNetworkCameraQualityRetentionProfile_1**](QualityRetentionProfilesApi.md#getNetworkCameraQualityRetentionProfile_1) | **GET** /networks/{networkId}/camera/qualityRetentionProfiles/{qualityRetentionProfileId} | Retrieve a single quality retention profile
[**getNetworkCameraQualityRetentionProfiles_1**](QualityRetentionProfilesApi.md#getNetworkCameraQualityRetentionProfiles_1) | **GET** /networks/{networkId}/camera/qualityRetentionProfiles | List the quality retention profiles for this network
[**updateNetworkCameraQualityRetentionProfile_1**](QualityRetentionProfilesApi.md#updateNetworkCameraQualityRetentionProfile_1) | **PUT** /networks/{networkId}/camera/qualityRetentionProfiles/{qualityRetentionProfileId} | Update an existing quality retention profile for this network.



## createNetworkCameraQualityRetentionProfile_1

> Object createNetworkCameraQualityRetentionProfile_1(networkId, createNetworkCameraQualityRetentionProfileRequest)

Creates new quality retention profile for this network.

Creates new quality retention profile for this network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.QualityRetentionProfilesApi();
let networkId = "networkId_example"; // String | 
let createNetworkCameraQualityRetentionProfileRequest = new MerakiDashboardApi.CreateNetworkCameraQualityRetentionProfileRequest(); // CreateNetworkCameraQualityRetentionProfileRequest | 
apiInstance.createNetworkCameraQualityRetentionProfile_1(networkId, createNetworkCameraQualityRetentionProfileRequest, (error, data, response) => {
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
 **networkId** | **String**|  | 
 **createNetworkCameraQualityRetentionProfileRequest** | [**CreateNetworkCameraQualityRetentionProfileRequest**](CreateNetworkCameraQualityRetentionProfileRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteNetworkCameraQualityRetentionProfile_1

> deleteNetworkCameraQualityRetentionProfile_1(networkId, qualityRetentionProfileId)

Delete an existing quality retention profile for this network.

Delete an existing quality retention profile for this network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.QualityRetentionProfilesApi();
let networkId = "networkId_example"; // String | 
let qualityRetentionProfileId = "qualityRetentionProfileId_example"; // String | 
apiInstance.deleteNetworkCameraQualityRetentionProfile_1(networkId, qualityRetentionProfileId, (error, data, response) => {
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
 **networkId** | **String**|  | 
 **qualityRetentionProfileId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNetworkCameraQualityRetentionProfile_1

> Object getNetworkCameraQualityRetentionProfile_1(networkId, qualityRetentionProfileId)

Retrieve a single quality retention profile

Retrieve a single quality retention profile

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.QualityRetentionProfilesApi();
let networkId = "networkId_example"; // String | 
let qualityRetentionProfileId = "qualityRetentionProfileId_example"; // String | 
apiInstance.getNetworkCameraQualityRetentionProfile_1(networkId, qualityRetentionProfileId, (error, data, response) => {
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
 **networkId** | **String**|  | 
 **qualityRetentionProfileId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkCameraQualityRetentionProfiles_1

> [Object] getNetworkCameraQualityRetentionProfiles_1(networkId)

List the quality retention profiles for this network

List the quality retention profiles for this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.QualityRetentionProfilesApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkCameraQualityRetentionProfiles_1(networkId, (error, data, response) => {
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
 **networkId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateNetworkCameraQualityRetentionProfile_1

> Object updateNetworkCameraQualityRetentionProfile_1(networkId, qualityRetentionProfileId, opts)

Update an existing quality retention profile for this network.

Update an existing quality retention profile for this network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.QualityRetentionProfilesApi();
let networkId = "networkId_example"; // String | 
let qualityRetentionProfileId = "qualityRetentionProfileId_example"; // String | 
let opts = {
  'updateNetworkCameraQualityRetentionProfileRequest': new MerakiDashboardApi.UpdateNetworkCameraQualityRetentionProfileRequest() // UpdateNetworkCameraQualityRetentionProfileRequest | 
};
apiInstance.updateNetworkCameraQualityRetentionProfile_1(networkId, qualityRetentionProfileId, opts, (error, data, response) => {
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
 **networkId** | **String**|  | 
 **qualityRetentionProfileId** | **String**|  | 
 **updateNetworkCameraQualityRetentionProfileRequest** | [**UpdateNetworkCameraQualityRetentionProfileRequest**](UpdateNetworkCameraQualityRetentionProfileRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

