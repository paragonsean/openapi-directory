# AppCenterClient.DistributeApi

All URIs are relative to *https://api.appcenter.ms*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appleMappingCreate**](DistributeApi.md#appleMappingCreate) | **POST** /v0.1/apps/{owner_name}/{app_name}/apple_mapping | 
[**appleMappingDelete**](DistributeApi.md#appleMappingDelete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/apple_mapping | 
[**appleMappingGet**](DistributeApi.md#appleMappingGet) | **GET** /v0.1/apps/{owner_name}/{app_name}/apple_mapping | 
[**appleMappingTestFlightGroups**](DistributeApi.md#appleMappingTestFlightGroups) | **GET** /v0.1/apps/{owner_name}/{app_name}/apple_test_flight_groups | 
[**devicesDeviceDetails**](DistributeApi.md#devicesDeviceDetails) | **GET** /v0.1/user/devices/{device_udid} | 
[**devicesGetReleaseUpdateDevicesStatus**](DistributeApi.md#devicesGetReleaseUpdateDevicesStatus) | **GET** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/update_devices/{resign_id} | 
[**devicesList**](DistributeApi.md#devicesList) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/devices | 
[**devicesListCsvFormat**](DistributeApi.md#devicesListCsvFormat) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/devices/download_devices_list | 
[**devicesRegisterUserForDevice**](DistributeApi.md#devicesRegisterUserForDevice) | **POST** /v0.1/users/{user_id}/devices/register | 
[**devicesRemoveUserDevice**](DistributeApi.md#devicesRemoveUserDevice) | **DELETE** /v0.1/user/devices/{device_udid} | 
[**devicesUserDevicesList**](DistributeApi.md#devicesUserDevicesList) | **GET** /v0.1/user/devices | 
[**distibutionReleasesInstallAnalytics**](DistributeApi.md#distibutionReleasesInstallAnalytics) | **POST** /v0.1/public/apps/{owner_name}/{app_name}/install_analytics | 
[**provisioningProfile**](DistributeApi.md#provisioningProfile) | **GET** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/provisioning_profile | 
[**releasesAddDistributionGroup**](DistributeApi.md#releasesAddDistributionGroup) | **POST** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/groups | 
[**releasesAddStore**](DistributeApi.md#releasesAddStore) | **POST** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/stores | 
[**releasesAddTesters**](DistributeApi.md#releasesAddTesters) | **POST** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/testers | 
[**releasesAvailableToTester**](DistributeApi.md#releasesAvailableToTester) | **GET** /v0.1/apps/{owner_name}/{app_name}/releases/filter_by_tester | 
[**releasesCreateReleaseUpload**](DistributeApi.md#releasesCreateReleaseUpload) | **POST** /v0.1/apps/{owner_name}/{app_name}/uploads/releases | 
[**releasesDelete**](DistributeApi.md#releasesDelete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id} | 
[**releasesDeleteDistributionGroup**](DistributeApi.md#releasesDeleteDistributionGroup) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/groups/{group_id} | 
[**releasesDeleteDistributionStore**](DistributeApi.md#releasesDeleteDistributionStore) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/stores/{store_id} | 
[**releasesDeleteDistributionTester**](DistributeApi.md#releasesDeleteDistributionTester) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/testers/{tester_id} | 
[**releasesDeleteTesterFromDestinations**](DistributeApi.md#releasesDeleteTesterFromDestinations) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/testers/{tester_id} | 
[**releasesDeleteWithDistributionGroupId**](DistributeApi.md#releasesDeleteWithDistributionGroupId) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/releases/{release_id} | 
[**releasesGetIosManifest**](DistributeApi.md#releasesGetIosManifest) | **GET** /v0.1/public/apps/{app_id}/releases/{release_id}/ios_manifest | 
[**releasesGetLatestByDistributionGroup**](DistributeApi.md#releasesGetLatestByDistributionGroup) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/releases/{release_id} | 
[**releasesGetLatestByHash**](DistributeApi.md#releasesGetLatestByHash) | **GET** /v0.1/sdk/apps/{app_secret}/releases/{release_hash} | 
[**releasesGetLatestByPublicDistributionGroup**](DistributeApi.md#releasesGetLatestByPublicDistributionGroup) | **GET** /v0.1/public/sdk/apps/{app_secret}/distribution_groups/{distribution_group_id}/releases/latest | 
[**releasesGetLatestByUser**](DistributeApi.md#releasesGetLatestByUser) | **GET** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id} | 
[**releasesGetLatestPrivateRelease**](DistributeApi.md#releasesGetLatestPrivateRelease) | **GET** /v0.1/sdk/apps/{app_secret}/releases/private/latest | 
[**releasesGetLatestPublicRelease**](DistributeApi.md#releasesGetLatestPublicRelease) | **GET** /v0.1/public/sdk/apps/{app_secret}/releases/latest | 
[**releasesGetPublicGroupsForReleaseByHash**](DistributeApi.md#releasesGetPublicGroupsForReleaseByHash) | **GET** /v0.1/public/sdk/apps/{app_secret}/releases/{release_hash}/public_distribution_groups | 
[**releasesGetReleaseUploadStatus**](DistributeApi.md#releasesGetReleaseUploadStatus) | **GET** /v0.1/apps/{owner_name}/{app_name}/uploads/releases/{upload_id} | 
[**releasesGetSparkleFeed**](DistributeApi.md#releasesGetSparkleFeed) | **GET** /v0.1/public/sparkle/apps/{app_secret} | 
[**releasesList**](DistributeApi.md#releasesList) | **GET** /v0.1/apps/{owner_name}/{app_name}/releases | 
[**releasesListByDistributionGroup**](DistributeApi.md#releasesListByDistributionGroup) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/releases | 
[**releasesListLatest**](DistributeApi.md#releasesListLatest) | **GET** /v0.1/apps/{owner_name}/{app_name}/recent_releases | 
[**releasesPutDistributionGroup**](DistributeApi.md#releasesPutDistributionGroup) | **PUT** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/groups/{group_id} | 
[**releasesPutDistributionTester**](DistributeApi.md#releasesPutDistributionTester) | **PUT** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/testers/{tester_id} | 
[**releasesUpdate**](DistributeApi.md#releasesUpdate) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id} | 
[**releasesUpdateDetails**](DistributeApi.md#releasesUpdateDetails) | **PUT** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id} | 
[**releasesUpdateReleaseUploadStatus**](DistributeApi.md#releasesUpdateReleaseUploadStatus) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/uploads/releases/{upload_id} | 
[**storeNotificationsGetNotificationByAppId**](DistributeApi.md#storeNotificationsGetNotificationByAppId) | **GET** /v0.1/apps/{owner_name}/{app_name}/store_service_status | 
[**storeReleasePublishLogsGet**](DistributeApi.md#storeReleasePublishLogsGet) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name}/releases/{release_id}/publish_logs | 
[**storeReleasesDelete**](DistributeApi.md#storeReleasesDelete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name}/releases/{release_id} | 
[**storeReleasesGet**](DistributeApi.md#storeReleasesGet) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name}/releases/{release_id} | 
[**storeReleasesGetLatest**](DistributeApi.md#storeReleasesGetLatest) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name}/latest_release | 
[**storeReleasesGetPublishError**](DistributeApi.md#storeReleasesGetPublishError) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name}/releases/{release_id}/publish_error_details | 
[**storeReleasesGetRealTimeStatusByReleaseId**](DistributeApi.md#storeReleasesGetRealTimeStatusByReleaseId) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name}/releases/{release_id}/realtimestatus | 
[**storeReleasesList**](DistributeApi.md#storeReleasesList) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name}/releases | 
[**storesCreate**](DistributeApi.md#storesCreate) | **POST** /v0.1/apps/{owner_name}/{app_name}/distribution_stores | 
[**storesDelete**](DistributeApi.md#storesDelete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name} | 
[**storesGet**](DistributeApi.md#storesGet) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name} | 
[**storesList**](DistributeApi.md#storesList) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_stores | 
[**storesPatch**](DistributeApi.md#storesPatch) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name} | 



## appleMappingCreate

> AppleMappingGet200Response appleMappingCreate(ownerName, appName, appleMappingCreateRequest)



Create a mapping for an existing app in apple store for the specified application.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let appleMappingCreateRequest = new AppCenterClient.AppleMappingCreateRequest(); // AppleMappingCreateRequest | The apple app mapping object
apiInstance.appleMappingCreate(ownerName, appName, appleMappingCreateRequest, (error, data, response) => {
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
 **appleMappingCreateRequest** | [**AppleMappingCreateRequest**](AppleMappingCreateRequest.md)| The apple app mapping object | 

### Return type

[**AppleMappingGet200Response**](AppleMappingGet200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appleMappingDelete

> appleMappingDelete(ownerName, appName, opts)



Delete mapping of apple app to an existing app in apple store.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'body': "body_example" // String | 
};
apiInstance.appleMappingDelete(ownerName, appName, opts, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **body** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appleMappingGet

> AppleMappingGet200Response appleMappingGet(ownerName, appName)



Get mapping of apple app to an existing app in apple store.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.appleMappingGet(ownerName, appName, (error, data, response) => {
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

### Return type

[**AppleMappingGet200Response**](AppleMappingGet200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appleMappingTestFlightGroups

> [AppleMappingTestFlightGroups200ResponseInner] appleMappingTestFlightGroups(ownerName, appName)



Fetch all apple test flight groups

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.appleMappingTestFlightGroups(ownerName, appName, (error, data, response) => {
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

### Return type

[**[AppleMappingTestFlightGroups200ResponseInner]**](AppleMappingTestFlightGroups200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## devicesDeviceDetails

> DevicesList200ResponseInner devicesDeviceDetails(deviceUdid)



Returns the device details.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let deviceUdid = "deviceUdid_example"; // String | The UDID of the device
apiInstance.devicesDeviceDetails(deviceUdid, (error, data, response) => {
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
 **deviceUdid** | **String**| The UDID of the device | 

### Return type

[**DevicesList200ResponseInner**](DevicesList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## devicesGetReleaseUpdateDevicesStatus

> DevicesGetReleaseUpdateDevicesStatus200Response devicesGetReleaseUpdateDevicesStatus(releaseId, resignId, ownerName, appName, opts)



Returns the resign status to the caller

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let releaseId = "releaseId_example"; // String | The ID of the release.
let resignId = "resignId_example"; // String | The ID of the resign operation.
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'includeProvisioningProfile': true // Boolean | A boolean value that indicates if the provisioning profile should be return in addition to the status. When set to true, the provisioning profile will be returned only when status is 'complete' or 'preparing_for_testers'.
};
apiInstance.devicesGetReleaseUpdateDevicesStatus(releaseId, resignId, ownerName, appName, opts, (error, data, response) => {
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
 **releaseId** | **String**| The ID of the release. | 
 **resignId** | **String**| The ID of the resign operation. | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **includeProvisioningProfile** | **Boolean**| A boolean value that indicates if the provisioning profile should be return in addition to the status. When set to true, the provisioning profile will be returned only when status is &#39;complete&#39; or &#39;preparing_for_testers&#39;. | [optional] 

### Return type

[**DevicesGetReleaseUpdateDevicesStatus200Response**](DevicesGetReleaseUpdateDevicesStatus200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## devicesList

> [DevicesList200ResponseInner] devicesList(distributionGroupName, ownerName, appName, opts)



Returns all devices associated with the given distribution group

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group.
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'releaseId': 3.4 // Number | when provided, gets the provisioning state of the devices owned by users of this distribution group when compared to the provided release.
};
apiInstance.devicesList(distributionGroupName, ownerName, appName, opts, (error, data, response) => {
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
 **distributionGroupName** | **String**| The name of the distribution group. | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **releaseId** | **Number**| when provided, gets the provisioning state of the devices owned by users of this distribution group when compared to the provided release. | [optional] 

### Return type

[**[DevicesList200ResponseInner]**](DevicesList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## devicesListCsvFormat

> devicesListCsvFormat(distributionGroupName, ownerName, appName, opts)



Returns all devices associated with the given distribution group.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group.
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'unprovisionedOnly': false, // Boolean | when true, filters out provisioned devices
  'udids': ["null"] // [String] | multiple UDIDs which should be part of the resulting CSV.
};
apiInstance.devicesListCsvFormat(distributionGroupName, ownerName, appName, opts, (error, data, response) => {
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
 **distributionGroupName** | **String**| The name of the distribution group. | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **unprovisionedOnly** | **Boolean**| when true, filters out provisioned devices | [optional] [default to false]
 **udids** | [**[String]**](String.md)| multiple UDIDs which should be part of the resulting CSV. | [optional] 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/csv


## devicesRegisterUserForDevice

> DevicesList200ResponseInner devicesRegisterUserForDevice(userId, devicesRegisterUserForDeviceRequest)



Registers a user for an existing device

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let userId = "userId_example"; // String | The ID of the user
let devicesRegisterUserForDeviceRequest = new AppCenterClient.DevicesRegisterUserForDeviceRequest(); // DevicesRegisterUserForDeviceRequest | The device info.
apiInstance.devicesRegisterUserForDevice(userId, devicesRegisterUserForDeviceRequest, (error, data, response) => {
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
 **userId** | **String**| The ID of the user | 
 **devicesRegisterUserForDeviceRequest** | [**DevicesRegisterUserForDeviceRequest**](DevicesRegisterUserForDeviceRequest.md)| The device info. | 

### Return type

[**DevicesList200ResponseInner**](DevicesList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## devicesRemoveUserDevice

> devicesRemoveUserDevice(deviceUdid)



Removes an existing device from a user

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let deviceUdid = "deviceUdid_example"; // String | The UDID of the device
apiInstance.devicesRemoveUserDevice(deviceUdid, (error, data, response) => {
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
 **deviceUdid** | **String**| The UDID of the device | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## devicesUserDevicesList

> [DevicesList200ResponseInner] devicesUserDevicesList()



Returns all devices associated with the given user.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
apiInstance.devicesUserDevicesList((error, data, response) => {
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

[**[DevicesList200ResponseInner]**](DevicesList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## distibutionReleasesInstallAnalytics

> distibutionReleasesInstallAnalytics(ownerName, appName, distibutionReleasesInstallAnalyticsRequest)



Notify download(s) for the provided distribution release(s).

### Example

```javascript
import AppCenterClient from 'app_center_client';

let apiInstance = new AppCenterClient.DistributeApi();
let ownerName = "ownerName_example"; // String | The name of the app owner
let appName = "appName_example"; // String | The name of the app
let distibutionReleasesInstallAnalyticsRequest = new AppCenterClient.DistibutionReleasesInstallAnalyticsRequest(); // DistibutionReleasesInstallAnalyticsRequest | The install analytics request payload
apiInstance.distibutionReleasesInstallAnalytics(ownerName, appName, distibutionReleasesInstallAnalyticsRequest, (error, data, response) => {
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
 **ownerName** | **String**| The name of the app owner | 
 **appName** | **String**| The name of the app | 
 **distibutionReleasesInstallAnalyticsRequest** | [**DistibutionReleasesInstallAnalyticsRequest**](DistibutionReleasesInstallAnalyticsRequest.md)| The install analytics request payload | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## provisioningProfile

> ProvisioningProfileResponse provisioningProfile(releaseId, ownerName, appName)



Return information about the provisioning profile. Only available for iOS.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let releaseId = 56; // Number | The release_id
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.provisioningProfile(releaseId, ownerName, appName, (error, data, response) => {
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
 **releaseId** | **Number**| The release_id | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**ProvisioningProfileResponse**](ProvisioningProfileResponse.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## releasesAddDistributionGroup

> ReleasesAddDistributionGroup201Response releasesAddDistributionGroup(releaseId, ownerName, appName, releasesAddDistributionGroupRequest)



Distributes a release to a group

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let releaseId = 56; // Number | The ID of the release
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let releasesAddDistributionGroupRequest = new AppCenterClient.ReleasesAddDistributionGroupRequest(); // ReleasesAddDistributionGroupRequest | The release information.
apiInstance.releasesAddDistributionGroup(releaseId, ownerName, appName, releasesAddDistributionGroupRequest, (error, data, response) => {
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
 **releaseId** | **Number**| The ID of the release | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **releasesAddDistributionGroupRequest** | [**ReleasesAddDistributionGroupRequest**](ReleasesAddDistributionGroupRequest.md)| The release information. | 

### Return type

[**ReleasesAddDistributionGroup201Response**](ReleasesAddDistributionGroup201Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## releasesAddStore

> ReleasesAddStore201Response releasesAddStore(releaseId, ownerName, appName, releasesAddStoreRequest)



Distributes a release to a store

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let releaseId = 56; // Number | The ID of the release
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let releasesAddStoreRequest = new AppCenterClient.ReleasesAddStoreRequest(); // ReleasesAddStoreRequest | The release information.
apiInstance.releasesAddStore(releaseId, ownerName, appName, releasesAddStoreRequest, (error, data, response) => {
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
 **releaseId** | **Number**| The ID of the release | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **releasesAddStoreRequest** | [**ReleasesAddStoreRequest**](ReleasesAddStoreRequest.md)| The release information. | 

### Return type

[**ReleasesAddStore201Response**](ReleasesAddStore201Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## releasesAddTesters

> ReleasesAddDistributionGroup201Response releasesAddTesters(releaseId, ownerName, appName, releasesAddTestersRequest)



Distributes a release to a user

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let releaseId = 56; // Number | The ID of the release
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let releasesAddTestersRequest = new AppCenterClient.ReleasesAddTestersRequest(); // ReleasesAddTestersRequest | The release information.
apiInstance.releasesAddTesters(releaseId, ownerName, appName, releasesAddTestersRequest, (error, data, response) => {
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
 **releaseId** | **Number**| The ID of the release | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **releasesAddTestersRequest** | [**ReleasesAddTestersRequest**](ReleasesAddTestersRequest.md)| The release information. | 

### Return type

[**ReleasesAddDistributionGroup201Response**](ReleasesAddDistributionGroup201Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## releasesAvailableToTester

> [ReleasesListLatest200ResponseInner] releasesAvailableToTester(ownerName, appName, opts)



Return detailed information about releases avaiable to a tester.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'publishedOnly': true // Boolean | when *true*, filters out releases that were uploaded but were never distributed. Releases that under deleted distribution groups will not be filtered out.
};
apiInstance.releasesAvailableToTester(ownerName, appName, opts, (error, data, response) => {
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
 **publishedOnly** | **Boolean**| when *true*, filters out releases that were uploaded but were never distributed. Releases that under deleted distribution groups will not be filtered out. | [optional] 

### Return type

[**[ReleasesListLatest200ResponseInner]**](ReleasesListLatest200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## releasesCreateReleaseUpload

> ReleasesCreateReleaseUpload201Response releasesCreateReleaseUpload(ownerName, appName, opts)



Initiate a new release upload. This API is part of multi-step upload process.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'releasesCreateReleaseUploadRequest': new AppCenterClient.ReleasesCreateReleaseUploadRequest() // ReleasesCreateReleaseUploadRequest | Optional parameters to create releases with user defined metadata
};
apiInstance.releasesCreateReleaseUpload(ownerName, appName, opts, (error, data, response) => {
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
 **releasesCreateReleaseUploadRequest** | [**ReleasesCreateReleaseUploadRequest**](ReleasesCreateReleaseUploadRequest.md)| Optional parameters to create releases with user defined metadata | [optional] 

### Return type

[**ReleasesCreateReleaseUpload201Response**](ReleasesCreateReleaseUpload201Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## releasesDelete

> releasesDelete(releaseId, ownerName, appName)



Deletes a release.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let releaseId = 56; // Number | The ID of the release
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.releasesDelete(releaseId, ownerName, appName, (error, data, response) => {
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
 **releaseId** | **Number**| The ID of the release | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## releasesDeleteDistributionGroup

> releasesDeleteDistributionGroup(releaseId, groupId, ownerName, appName)



Delete the given distribution group from the release

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let releaseId = 56; // Number | The ID of the release
let groupId = "groupId_example"; // String | The id of the distribution group
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.releasesDeleteDistributionGroup(releaseId, groupId, ownerName, appName, (error, data, response) => {
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
 **releaseId** | **Number**| The ID of the release | 
 **groupId** | **String**| The id of the distribution group | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## releasesDeleteDistributionStore

> releasesDeleteDistributionStore(releaseId, storeId, ownerName, appName)



Delete the given distribution store from the release

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let releaseId = 56; // Number | The ID of the release
let storeId = "storeId_example"; // String | The id of the distribution store
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.releasesDeleteDistributionStore(releaseId, storeId, ownerName, appName, (error, data, response) => {
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
 **releaseId** | **Number**| The ID of the release | 
 **storeId** | **String**| The id of the distribution store | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## releasesDeleteDistributionTester

> releasesDeleteDistributionTester(releaseId, testerId, ownerName, appName)



Delete the given tester from the release

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let releaseId = 56; // Number | The ID of the release
let testerId = "testerId_example"; // String | The id of the tester
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.releasesDeleteDistributionTester(releaseId, testerId, ownerName, appName, (error, data, response) => {
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
 **releaseId** | **Number**| The ID of the release | 
 **testerId** | **String**| The id of the tester | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## releasesDeleteTesterFromDestinations

> releasesDeleteTesterFromDestinations(testerId, ownerName, appName)



Delete the given tester from the all releases

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let testerId = "testerId_example"; // String | The id of the tester
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.releasesDeleteTesterFromDestinations(testerId, ownerName, appName, (error, data, response) => {
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
 **testerId** | **String**| The id of the tester | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## releasesDeleteWithDistributionGroupId

> releasesDeleteWithDistributionGroupId(ownerName, appName, distributionGroupName, releaseId)



Deletes a release with id &#39;release_id&#39; in a given distribution group.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let ownerName = "ownerName_example"; // String | The name of the app owner
let appName = "appName_example"; // String | The name of the app
let distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group.
let releaseId = 56; // Number | The ID identifying the unique release.
apiInstance.releasesDeleteWithDistributionGroupId(ownerName, appName, distributionGroupName, releaseId, (error, data, response) => {
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
 **ownerName** | **String**| The name of the app owner | 
 **appName** | **String**| The name of the app | 
 **distributionGroupName** | **String**| The name of the distribution group. | 
 **releaseId** | **Number**| The ID identifying the unique release. | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## releasesGetIosManifest

> releasesGetIosManifest(appId, releaseId, token)



Returns the manifest.plist in XML format for installing the release on a device. Only available for iOS.

### Example

```javascript
import AppCenterClient from 'app_center_client';

let apiInstance = new AppCenterClient.DistributeApi();
let appId = "appId_example"; // String | The ID of the application
let releaseId = 56; // Number | The release_id
let token = "token_example"; // String | A hash that authorizes the download if it matches the release info.
apiInstance.releasesGetIosManifest(appId, releaseId, token, (error, data, response) => {
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
 **appId** | **String**| The ID of the application | 
 **releaseId** | **Number**| The release_id | 
 **token** | **String**| A hash that authorizes the download if it matches the release info. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## releasesGetLatestByDistributionGroup

> ReleasesGetLatestByDistributionGroup200Response releasesGetLatestByDistributionGroup(ownerName, appName, distributionGroupName, releaseId, opts)



Return detailed information about a distributed release in a given distribution group.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let ownerName = "ownerName_example"; // String | The name of the app owner
let appName = "appName_example"; // String | The name of the app
let distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group.
let releaseId = "releaseId_example"; // String | Also supports the constant `latest`, which will return the latest release in the distribution group.
let opts = {
  'isInstallPage': true // Boolean | The check if the request is from Install page
};
apiInstance.releasesGetLatestByDistributionGroup(ownerName, appName, distributionGroupName, releaseId, opts, (error, data, response) => {
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
 **ownerName** | **String**| The name of the app owner | 
 **appName** | **String**| The name of the app | 
 **distributionGroupName** | **String**| The name of the distribution group. | 
 **releaseId** | **String**| Also supports the constant &#x60;latest&#x60;, which will return the latest release in the distribution group. | 
 **isInstallPage** | **Boolean**| The check if the request is from Install page | [optional] 

### Return type

[**ReleasesGetLatestByDistributionGroup200Response**](ReleasesGetLatestByDistributionGroup200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## releasesGetLatestByHash

> ReleasesGetLatestByDistributionGroup200Response releasesGetLatestByHash(appSecret, releaseHash, opts)



If &#39;latest&#39; is not specified then it will return the specified release if it&#39;s enabled. If &#39;latest&#39; is specified, regardless of whether a release hash is provided, the latest enabled release is returned.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let appSecret = "appSecret_example"; // String | The secret of the target application
let releaseHash = "releaseHash_example"; // String | The hash of the release or 'latest' to get the latest release from all the distribution groups assigned to the current user.
let opts = {
  'udid': "udid_example" // String | When passing `udid` in the query string, a provisioning check for the given device ID will be done. Will be ignored for non-iOS platforms.
};
apiInstance.releasesGetLatestByHash(appSecret, releaseHash, opts, (error, data, response) => {
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
 **appSecret** | **String**| The secret of the target application | 
 **releaseHash** | **String**| The hash of the release or &#39;latest&#39; to get the latest release from all the distribution groups assigned to the current user. | 
 **udid** | **String**| When passing &#x60;udid&#x60; in the query string, a provisioning check for the given device ID will be done. Will be ignored for non-iOS platforms. | [optional] 

### Return type

[**ReleasesGetLatestByDistributionGroup200Response**](ReleasesGetLatestByDistributionGroup200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## releasesGetLatestByPublicDistributionGroup

> ReleasesGetLatestByDistributionGroup200Response releasesGetLatestByPublicDistributionGroup(appSecret, distributionGroupId, opts)



Get a release with &#39;latest&#39; for the given public group.

### Example

```javascript
import AppCenterClient from 'app_center_client';

let apiInstance = new AppCenterClient.DistributeApi();
let appSecret = "appSecret_example"; // String | The secret of the target application
let distributionGroupId = "distributionGroupId_example"; // String | the id for destination
let opts = {
  'isInstallPage': true // Boolean | The check if the request is from Install page
};
apiInstance.releasesGetLatestByPublicDistributionGroup(appSecret, distributionGroupId, opts, (error, data, response) => {
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
 **appSecret** | **String**| The secret of the target application | 
 **distributionGroupId** | **String**| the id for destination | 
 **isInstallPage** | **Boolean**| The check if the request is from Install page | [optional] 

### Return type

[**ReleasesGetLatestByDistributionGroup200Response**](ReleasesGetLatestByDistributionGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## releasesGetLatestByUser

> ReleasesGetLatestByDistributionGroup200Response releasesGetLatestByUser(releaseId, ownerName, appName, opts)



Get a release with id &#x60;release_id&#x60;. If &#x60;release_id&#x60; is &#x60;latest&#x60;, return the latest release that was distributed to the current user (from all the distribution groups).

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let releaseId = "releaseId_example"; // String | The ID of the release, or `latest` to get the latest release from all the distribution groups assigned to the current user.
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'udid': "udid_example", // String | when supplied, this call will also check if the given UDID is provisioned. Will be ignored for non-iOS platforms. The value will be returned in the property is_udid_provisioned.
  'isInstallPage': true // Boolean | The check if the request is from Install page
};
apiInstance.releasesGetLatestByUser(releaseId, ownerName, appName, opts, (error, data, response) => {
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
 **releaseId** | **String**| The ID of the release, or &#x60;latest&#x60; to get the latest release from all the distribution groups assigned to the current user. | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **udid** | **String**| when supplied, this call will also check if the given UDID is provisioned. Will be ignored for non-iOS platforms. The value will be returned in the property is_udid_provisioned. | [optional] 
 **isInstallPage** | **Boolean**| The check if the request is from Install page | [optional] 

### Return type

[**ReleasesGetLatestByDistributionGroup200Response**](ReleasesGetLatestByDistributionGroup200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## releasesGetLatestPrivateRelease

> ReleasesGetLatestByDistributionGroup200Response releasesGetLatestPrivateRelease(appSecret, opts)



Get the latest release distributed to a private group the given user is a member of for the given app.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let appSecret = "appSecret_example"; // String | The secret of the target application
let opts = {
  'udid': "udid_example" // String | When passing `udid` in the query string, a provisioning check for the given device ID will be done. Will be ignored for non-iOS platforms.
};
apiInstance.releasesGetLatestPrivateRelease(appSecret, opts, (error, data, response) => {
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
 **appSecret** | **String**| The secret of the target application | 
 **udid** | **String**| When passing &#x60;udid&#x60; in the query string, a provisioning check for the given device ID will be done. Will be ignored for non-iOS platforms. | [optional] 

### Return type

[**ReleasesGetLatestByDistributionGroup200Response**](ReleasesGetLatestByDistributionGroup200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## releasesGetLatestPublicRelease

> ReleasesGetLatestByDistributionGroup200Response releasesGetLatestPublicRelease(appSecret)



Get the latest public release for the given app.

### Example

```javascript
import AppCenterClient from 'app_center_client';

let apiInstance = new AppCenterClient.DistributeApi();
let appSecret = "appSecret_example"; // String | The secret of the target application
apiInstance.releasesGetLatestPublicRelease(appSecret, (error, data, response) => {
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
 **appSecret** | **String**| The secret of the target application | 

### Return type

[**ReleasesGetLatestByDistributionGroup200Response**](ReleasesGetLatestByDistributionGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## releasesGetPublicGroupsForReleaseByHash

> [ReleasesGetPublicGroupsForReleaseByHash200ResponseInner] releasesGetPublicGroupsForReleaseByHash(appSecret, releaseHash)



Get all public distribution groups that a given release has been distributed to

### Example

```javascript
import AppCenterClient from 'app_center_client';

let apiInstance = new AppCenterClient.DistributeApi();
let appSecret = "appSecret_example"; // String | The secret of the target application
let releaseHash = "releaseHash_example"; // String | The hash of the release
apiInstance.releasesGetPublicGroupsForReleaseByHash(appSecret, releaseHash, (error, data, response) => {
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
 **appSecret** | **String**| The secret of the target application | 
 **releaseHash** | **String**| The hash of the release | 

### Return type

[**[ReleasesGetPublicGroupsForReleaseByHash200ResponseInner]**](ReleasesGetPublicGroupsForReleaseByHash200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## releasesGetReleaseUploadStatus

> ReleasesGetReleaseUploadStatus200Response releasesGetReleaseUploadStatus(uploadId, ownerName, appName)



Get the current status of the release upload.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let uploadId = "uploadId_example"; // String | The ID of the release upload
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.releasesGetReleaseUploadStatus(uploadId, ownerName, appName, (error, data, response) => {
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
 **uploadId** | **String**| The ID of the release upload | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**ReleasesGetReleaseUploadStatus200Response**](ReleasesGetReleaseUploadStatus200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## releasesGetSparkleFeed

> releasesGetSparkleFeed(appSecret)



Gets the sparkle feed of the releases that are distributed to all the public distribution groups.

### Example

```javascript
import AppCenterClient from 'app_center_client';

let apiInstance = new AppCenterClient.DistributeApi();
let appSecret = "appSecret_example"; // String | The secret of the application.
apiInstance.releasesGetSparkleFeed(appSecret, (error, data, response) => {
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
 **appSecret** | **String**| The secret of the application. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## releasesList

> [ReleasesListLatest200ResponseInner] releasesList(ownerName, appName, opts)



Return basic information about releases.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'publishedOnly': true, // Boolean | When *true*, filters out releases that were uploaded but were never distributed. Releases that under deleted distribution groups will not be filtered out.
  'scope': "scope_example", // String | When the scope is 'tester', only includes releases that have been distributed to groups that the user belongs to.
  'top': 3.4, // Number | The number of releases to return
  'releaseId': 3.4 // Number | The id of a release
};
apiInstance.releasesList(ownerName, appName, opts, (error, data, response) => {
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
 **publishedOnly** | **Boolean**| When *true*, filters out releases that were uploaded but were never distributed. Releases that under deleted distribution groups will not be filtered out. | [optional] 
 **scope** | **String**| When the scope is &#39;tester&#39;, only includes releases that have been distributed to groups that the user belongs to. | [optional] 
 **top** | **Number**| The number of releases to return | [optional] 
 **releaseId** | **Number**| The id of a release | [optional] 

### Return type

[**[ReleasesListLatest200ResponseInner]**](ReleasesListLatest200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## releasesListByDistributionGroup

> [ReleasesListByDistributionGroup200ResponseInner] releasesListByDistributionGroup(distributionGroupName, ownerName, appName)



Return basic information about distributed releases in a given distribution group.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group.
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.releasesListByDistributionGroup(distributionGroupName, ownerName, appName, (error, data, response) => {
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
 **distributionGroupName** | **String**| The name of the distribution group. | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**[ReleasesListByDistributionGroup200ResponseInner]**](ReleasesListByDistributionGroup200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## releasesListLatest

> [ReleasesListLatest200ResponseInner] releasesListLatest(ownerName, appName)



Get the latest release from every distribution group associated with an application.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.releasesListLatest(ownerName, appName, (error, data, response) => {
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

### Return type

[**[ReleasesListLatest200ResponseInner]**](ReleasesListLatest200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## releasesPutDistributionGroup

> releasesPutDistributionGroup(releaseId, groupId, ownerName, appName, opts)



Update details about the specified distribution group associated with the release

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let releaseId = 56; // Number | The ID of the release
let groupId = "groupId_example"; // String | The id of the releases destination
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'releasesPutDistributionGroupRequest': new AppCenterClient.ReleasesPutDistributionGroupRequest() // ReleasesPutDistributionGroupRequest | 
};
apiInstance.releasesPutDistributionGroup(releaseId, groupId, ownerName, appName, opts, (error, data, response) => {
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
 **releaseId** | **Number**| The ID of the release | 
 **groupId** | **String**| The id of the releases destination | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **releasesPutDistributionGroupRequest** | [**ReleasesPutDistributionGroupRequest**](ReleasesPutDistributionGroupRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## releasesPutDistributionTester

> releasesPutDistributionTester(releaseId, testerId, ownerName, appName, opts)



Update details about the specified tester associated with the release

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let releaseId = 56; // Number | The ID of the release
let testerId = "testerId_example"; // String | The id of the tester
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'releasesPutDistributionGroupRequest': new AppCenterClient.ReleasesPutDistributionGroupRequest() // ReleasesPutDistributionGroupRequest | 
};
apiInstance.releasesPutDistributionTester(releaseId, testerId, ownerName, appName, opts, (error, data, response) => {
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
 **releaseId** | **Number**| The ID of the release | 
 **testerId** | **String**| The id of the tester | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **releasesPutDistributionGroupRequest** | [**ReleasesPutDistributionGroupRequest**](ReleasesPutDistributionGroupRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## releasesUpdate

> ReleasesUpdate200Response releasesUpdate(releaseId, ownerName, appName, releasesUpdateRequest)



Updates a release.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let releaseId = 56; // Number | The ID of the release
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let releasesUpdateRequest = new AppCenterClient.ReleasesUpdateRequest(); // ReleasesUpdateRequest | The release information.
apiInstance.releasesUpdate(releaseId, ownerName, appName, releasesUpdateRequest, (error, data, response) => {
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
 **releaseId** | **Number**| The ID of the release | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **releasesUpdateRequest** | [**ReleasesUpdateRequest**](ReleasesUpdateRequest.md)| The release information. | 

### Return type

[**ReleasesUpdate200Response**](ReleasesUpdate200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: application/json


## releasesUpdateDetails

> ReleasesUpdateDetails200Response releasesUpdateDetails(releaseId, ownerName, appName, releasesUpdateDetailsRequest)



Update details of a release.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let releaseId = 56; // Number | The ID of the release
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let releasesUpdateDetailsRequest = new AppCenterClient.ReleasesUpdateDetailsRequest(); // ReleasesUpdateDetailsRequest | The release information.
apiInstance.releasesUpdateDetails(releaseId, ownerName, appName, releasesUpdateDetailsRequest, (error, data, response) => {
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
 **releaseId** | **Number**| The ID of the release | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **releasesUpdateDetailsRequest** | [**ReleasesUpdateDetailsRequest**](ReleasesUpdateDetailsRequest.md)| The release information. | 

### Return type

[**ReleasesUpdateDetails200Response**](ReleasesUpdateDetails200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## releasesUpdateReleaseUploadStatus

> ReleasesUpdateReleaseUploadStatus200Response releasesUpdateReleaseUploadStatus(uploadId, ownerName, appName, releasesUpdateReleaseUploadStatusRequest, opts)



Update the current status of the release upload.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let uploadId = "uploadId_example"; // String | The ID of the release upload
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let releasesUpdateReleaseUploadStatusRequest = new AppCenterClient.ReleasesUpdateReleaseUploadStatusRequest(); // ReleasesUpdateReleaseUploadStatusRequest | The release upload status information.
let opts = {
  'extract': true // Boolean | A flag that indicates to extract release or not, true by default
};
apiInstance.releasesUpdateReleaseUploadStatus(uploadId, ownerName, appName, releasesUpdateReleaseUploadStatusRequest, opts, (error, data, response) => {
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
 **uploadId** | **String**| The ID of the release upload | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **releasesUpdateReleaseUploadStatusRequest** | [**ReleasesUpdateReleaseUploadStatusRequest**](ReleasesUpdateReleaseUploadStatusRequest.md)| The release upload status information. | 
 **extract** | **Boolean**| A flag that indicates to extract release or not, true by default | [optional] 

### Return type

[**ReleasesUpdateReleaseUploadStatus200Response**](ReleasesUpdateReleaseUploadStatus200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storeNotificationsGetNotificationByAppId

> StoreNotificationsGetNotificationByAppId200Response storeNotificationsGetNotificationByAppId(ownerName, appName)



Application specific store service status

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.storeNotificationsGetNotificationByAppId(ownerName, appName, (error, data, response) => {
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

### Return type

[**StoreNotificationsGetNotificationByAppId200Response**](StoreNotificationsGetNotificationByAppId200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storeReleasePublishLogsGet

> storeReleasePublishLogsGet(storeName, releaseId, ownerName, appName)



Returns publish logs for a particular release published to a particular store

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let storeName = "storeName_example"; // String | The name of the store
let releaseId = "releaseId_example"; // String | The ID of the realease
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.storeReleasePublishLogsGet(storeName, releaseId, ownerName, appName, (error, data, response) => {
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
 **storeName** | **String**| The name of the store | 
 **releaseId** | **String**| The ID of the realease | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storeReleasesDelete

> storeReleasesDelete(storeName, releaseId, ownerName, appName, opts)



delete the release with release Id

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let storeName = "storeName_example"; // String | The name of the store
let releaseId = "releaseId_example"; // String | The id of the release
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'body': "body_example" // String | 
};
apiInstance.storeReleasesDelete(storeName, releaseId, ownerName, appName, opts, (error, data, response) => {
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
 **storeName** | **String**| The name of the store | 
 **releaseId** | **String**| The id of the release | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **body** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storeReleasesGet

> [StoreReleasesGetLatest200ResponseInner] storeReleasesGet(storeName, releaseId, ownerName, appName)



Return releases published in a store for releaseId and storeId

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let storeName = "storeName_example"; // String | The name of the store
let releaseId = "releaseId_example"; // String | The name of the store
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.storeReleasesGet(storeName, releaseId, ownerName, appName, (error, data, response) => {
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
 **storeName** | **String**| The name of the store | 
 **releaseId** | **String**| The name of the store | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**[StoreReleasesGetLatest200ResponseInner]**](StoreReleasesGetLatest200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storeReleasesGetLatest

> [StoreReleasesGetLatest200ResponseInner] storeReleasesGetLatest(storeName, ownerName, appName)



Returns the latest release published in a store.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let storeName = "storeName_example"; // String | The name of the store
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.storeReleasesGetLatest(storeName, ownerName, appName, (error, data, response) => {
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
 **storeName** | **String**| The name of the store | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**[StoreReleasesGetLatest200ResponseInner]**](StoreReleasesGetLatest200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storeReleasesGetPublishError

> StoreReleasesGetPublishError200Response storeReleasesGetPublishError(storeName, releaseId, ownerName, appName)



Return the Error Details of release which failed in publishing.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let storeName = "storeName_example"; // String | The name of the store
let releaseId = 3.4; // Number | The id of the release
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.storeReleasesGetPublishError(storeName, releaseId, ownerName, appName, (error, data, response) => {
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
 **storeName** | **String**| The name of the store | 
 **releaseId** | **Number**| The id of the release | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**StoreReleasesGetPublishError200Response**](StoreReleasesGetPublishError200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storeReleasesGetRealTimeStatusByReleaseId

> StoreReleasesGetRealTimeStatusByReleaseId200Response storeReleasesGetRealTimeStatusByReleaseId(storeName, releaseId, ownerName, appName)



Return the Real time Status publishing of release from store.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let storeName = "storeName_example"; // String | The name of the store
let releaseId = 3.4; // Number | The id of the release
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.storeReleasesGetRealTimeStatusByReleaseId(storeName, releaseId, ownerName, appName, (error, data, response) => {
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
 **storeName** | **String**| The name of the store | 
 **releaseId** | **Number**| The id of the release | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**StoreReleasesGetRealTimeStatusByReleaseId200Response**](StoreReleasesGetRealTimeStatusByReleaseId200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storeReleasesList

> [StoreReleasesList200ResponseInner] storeReleasesList(storeName, ownerName, appName)



Return all releases published  in a store

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let storeName = "storeName_example"; // String | The name of the store
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.storeReleasesList(storeName, ownerName, appName, (error, data, response) => {
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
 **storeName** | **String**| The name of the store | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**[StoreReleasesList200ResponseInner]**](StoreReleasesList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storesCreate

> StoresList200ResponseInner storesCreate(ownerName, appName, storesCreateRequest)



Create a new external store for the specified application.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let storesCreateRequest = new AppCenterClient.StoresCreateRequest(); // StoresCreateRequest | The store request
apiInstance.storesCreate(ownerName, appName, storesCreateRequest, (error, data, response) => {
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
 **storesCreateRequest** | [**StoresCreateRequest**](StoresCreateRequest.md)| The store request | 

### Return type

[**StoresList200ResponseInner**](StoresList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storesDelete

> storesDelete(storeName, ownerName, appName, opts)



delete the store based on specific store name.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let storeName = "storeName_example"; // String | The name of the store
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'body': "body_example" // String | 
};
apiInstance.storesDelete(storeName, ownerName, appName, opts, (error, data, response) => {
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
 **storeName** | **String**| The name of the store | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **body** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storesGet

> StoresList200ResponseInner storesGet(storeName, ownerName, appName)



Return the store details for specified store name.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let storeName = "storeName_example"; // String | The name of the store
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.storesGet(storeName, ownerName, appName, (error, data, response) => {
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
 **storeName** | **String**| The name of the store | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**StoresList200ResponseInner**](StoresList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storesList

> [StoresList200ResponseInner] storesList(ownerName, appName)



Get all the store details from Storage store table for a particular application.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.storesList(ownerName, appName, (error, data, response) => {
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

### Return type

[**[StoresList200ResponseInner]**](StoresList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storesPatch

> storesPatch(storeName, ownerName, appName, storesPatchRequest)



Update the store.

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.DistributeApi();
let storeName = "storeName_example"; // String | The name of the store
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let storesPatchRequest = new AppCenterClient.StoresPatchRequest(); // StoresPatchRequest | Store update request
apiInstance.storesPatch(storeName, ownerName, appName, storesPatchRequest, (error, data, response) => {
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
 **storeName** | **String**| The name of the store | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **storesPatchRequest** | [**StoresPatchRequest**](StoresPatchRequest.md)| Store update request | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

