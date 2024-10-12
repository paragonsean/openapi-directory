# DistributeApi

All URIs are relative to *https://api.appcenter.ms*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appleMappingCreate**](DistributeApi.md#appleMappingCreate) | **POST** /v0.1/apps/{owner_name}/{app_name}/apple_mapping |  |
| [**appleMappingDelete**](DistributeApi.md#appleMappingDelete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/apple_mapping |  |
| [**appleMappingGet**](DistributeApi.md#appleMappingGet) | **GET** /v0.1/apps/{owner_name}/{app_name}/apple_mapping |  |
| [**appleMappingTestFlightGroups**](DistributeApi.md#appleMappingTestFlightGroups) | **GET** /v0.1/apps/{owner_name}/{app_name}/apple_test_flight_groups |  |
| [**devicesDeviceDetails**](DistributeApi.md#devicesDeviceDetails) | **GET** /v0.1/user/devices/{device_udid} |  |
| [**devicesGetReleaseUpdateDevicesStatus**](DistributeApi.md#devicesGetReleaseUpdateDevicesStatus) | **GET** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/update_devices/{resign_id} |  |
| [**devicesList**](DistributeApi.md#devicesList) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/devices |  |
| [**devicesListCsvFormat**](DistributeApi.md#devicesListCsvFormat) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/devices/download_devices_list |  |
| [**devicesRegisterUserForDevice**](DistributeApi.md#devicesRegisterUserForDevice) | **POST** /v0.1/users/{user_id}/devices/register |  |
| [**devicesRemoveUserDevice**](DistributeApi.md#devicesRemoveUserDevice) | **DELETE** /v0.1/user/devices/{device_udid} |  |
| [**devicesUserDevicesList**](DistributeApi.md#devicesUserDevicesList) | **GET** /v0.1/user/devices |  |
| [**distibutionReleasesInstallAnalytics**](DistributeApi.md#distibutionReleasesInstallAnalytics) | **POST** /v0.1/public/apps/{owner_name}/{app_name}/install_analytics |  |
| [**provisioningProfile**](DistributeApi.md#provisioningProfile) | **GET** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/provisioning_profile |  |
| [**releasesAddDistributionGroup**](DistributeApi.md#releasesAddDistributionGroup) | **POST** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/groups |  |
| [**releasesAddStore**](DistributeApi.md#releasesAddStore) | **POST** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/stores |  |
| [**releasesAddTesters**](DistributeApi.md#releasesAddTesters) | **POST** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/testers |  |
| [**releasesAvailableToTester**](DistributeApi.md#releasesAvailableToTester) | **GET** /v0.1/apps/{owner_name}/{app_name}/releases/filter_by_tester |  |
| [**releasesCreateReleaseUpload**](DistributeApi.md#releasesCreateReleaseUpload) | **POST** /v0.1/apps/{owner_name}/{app_name}/uploads/releases |  |
| [**releasesDelete**](DistributeApi.md#releasesDelete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id} |  |
| [**releasesDeleteDistributionGroup**](DistributeApi.md#releasesDeleteDistributionGroup) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/groups/{group_id} |  |
| [**releasesDeleteDistributionStore**](DistributeApi.md#releasesDeleteDistributionStore) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/stores/{store_id} |  |
| [**releasesDeleteDistributionTester**](DistributeApi.md#releasesDeleteDistributionTester) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/testers/{tester_id} |  |
| [**releasesDeleteTesterFromDestinations**](DistributeApi.md#releasesDeleteTesterFromDestinations) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/testers/{tester_id} |  |
| [**releasesDeleteWithDistributionGroupId**](DistributeApi.md#releasesDeleteWithDistributionGroupId) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/releases/{release_id} |  |
| [**releasesGetIosManifest**](DistributeApi.md#releasesGetIosManifest) | **GET** /v0.1/public/apps/{app_id}/releases/{release_id}/ios_manifest |  |
| [**releasesGetLatestByDistributionGroup**](DistributeApi.md#releasesGetLatestByDistributionGroup) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/releases/{release_id} |  |
| [**releasesGetLatestByHash**](DistributeApi.md#releasesGetLatestByHash) | **GET** /v0.1/sdk/apps/{app_secret}/releases/{release_hash} |  |
| [**releasesGetLatestByPublicDistributionGroup**](DistributeApi.md#releasesGetLatestByPublicDistributionGroup) | **GET** /v0.1/public/sdk/apps/{app_secret}/distribution_groups/{distribution_group_id}/releases/latest |  |
| [**releasesGetLatestByUser**](DistributeApi.md#releasesGetLatestByUser) | **GET** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id} |  |
| [**releasesGetLatestPrivateRelease**](DistributeApi.md#releasesGetLatestPrivateRelease) | **GET** /v0.1/sdk/apps/{app_secret}/releases/private/latest |  |
| [**releasesGetLatestPublicRelease**](DistributeApi.md#releasesGetLatestPublicRelease) | **GET** /v0.1/public/sdk/apps/{app_secret}/releases/latest |  |
| [**releasesGetPublicGroupsForReleaseByHash**](DistributeApi.md#releasesGetPublicGroupsForReleaseByHash) | **GET** /v0.1/public/sdk/apps/{app_secret}/releases/{release_hash}/public_distribution_groups |  |
| [**releasesGetReleaseUploadStatus**](DistributeApi.md#releasesGetReleaseUploadStatus) | **GET** /v0.1/apps/{owner_name}/{app_name}/uploads/releases/{upload_id} |  |
| [**releasesGetSparkleFeed**](DistributeApi.md#releasesGetSparkleFeed) | **GET** /v0.1/public/sparkle/apps/{app_secret} |  |
| [**releasesList**](DistributeApi.md#releasesList) | **GET** /v0.1/apps/{owner_name}/{app_name}/releases |  |
| [**releasesListByDistributionGroup**](DistributeApi.md#releasesListByDistributionGroup) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/releases |  |
| [**releasesListLatest**](DistributeApi.md#releasesListLatest) | **GET** /v0.1/apps/{owner_name}/{app_name}/recent_releases |  |
| [**releasesPutDistributionGroup**](DistributeApi.md#releasesPutDistributionGroup) | **PUT** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/groups/{group_id} |  |
| [**releasesPutDistributionTester**](DistributeApi.md#releasesPutDistributionTester) | **PUT** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/testers/{tester_id} |  |
| [**releasesUpdate**](DistributeApi.md#releasesUpdate) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id} |  |
| [**releasesUpdateDetails**](DistributeApi.md#releasesUpdateDetails) | **PUT** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id} |  |
| [**releasesUpdateReleaseUploadStatus**](DistributeApi.md#releasesUpdateReleaseUploadStatus) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/uploads/releases/{upload_id} |  |
| [**storeNotificationsGetNotificationByAppId**](DistributeApi.md#storeNotificationsGetNotificationByAppId) | **GET** /v0.1/apps/{owner_name}/{app_name}/store_service_status |  |
| [**storeReleasePublishLogsGet**](DistributeApi.md#storeReleasePublishLogsGet) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name}/releases/{release_id}/publish_logs |  |
| [**storeReleasesDelete**](DistributeApi.md#storeReleasesDelete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name}/releases/{release_id} |  |
| [**storeReleasesGet**](DistributeApi.md#storeReleasesGet) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name}/releases/{release_id} |  |
| [**storeReleasesGetLatest**](DistributeApi.md#storeReleasesGetLatest) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name}/latest_release |  |
| [**storeReleasesGetPublishError**](DistributeApi.md#storeReleasesGetPublishError) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name}/releases/{release_id}/publish_error_details |  |
| [**storeReleasesGetRealTimeStatusByReleaseId**](DistributeApi.md#storeReleasesGetRealTimeStatusByReleaseId) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name}/releases/{release_id}/realtimestatus |  |
| [**storeReleasesList**](DistributeApi.md#storeReleasesList) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name}/releases |  |
| [**storesCreate**](DistributeApi.md#storesCreate) | **POST** /v0.1/apps/{owner_name}/{app_name}/distribution_stores |  |
| [**storesDelete**](DistributeApi.md#storesDelete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name} |  |
| [**storesGet**](DistributeApi.md#storesGet) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name} |  |
| [**storesList**](DistributeApi.md#storesList) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_stores |  |
| [**storesPatch**](DistributeApi.md#storesPatch) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name} |  |


<a id="appleMappingCreate"></a>
# **appleMappingCreate**
> AppleMappingGet200Response appleMappingCreate(ownerName, appName, appleMappingCreateRequest)



Create a mapping for an existing app in apple store for the specified application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    AppleMappingCreateRequest appleMappingCreateRequest = new AppleMappingCreateRequest(); // AppleMappingCreateRequest | The apple app mapping object
    try {
      AppleMappingGet200Response result = apiInstance.appleMappingCreate(ownerName, appName, appleMappingCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#appleMappingCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **appleMappingCreateRequest** | [**AppleMappingCreateRequest**](AppleMappingCreateRequest.md)| The apple app mapping object | |

### Return type

[**AppleMappingGet200Response**](AppleMappingGet200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **0** | Error |  -  |

<a id="appleMappingDelete"></a>
# **appleMappingDelete**
> appleMappingDelete(ownerName, appName, body)



Delete mapping of apple app to an existing app in apple store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    String body = "body_example"; // String | 
    try {
      apiInstance.appleMappingDelete(ownerName, appName, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#appleMappingDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **body** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="appleMappingGet"></a>
# **appleMappingGet**
> AppleMappingGet200Response appleMappingGet(ownerName, appName)



Get mapping of apple app to an existing app in apple store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      AppleMappingGet200Response result = apiInstance.appleMappingGet(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#appleMappingGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**AppleMappingGet200Response**](AppleMappingGet200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="appleMappingTestFlightGroups"></a>
# **appleMappingTestFlightGroups**
> List&lt;AppleMappingTestFlightGroups200ResponseInner&gt; appleMappingTestFlightGroups(ownerName, appName)



Fetch all apple test flight groups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      List<AppleMappingTestFlightGroups200ResponseInner> result = apiInstance.appleMappingTestFlightGroups(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#appleMappingTestFlightGroups");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**List&lt;AppleMappingTestFlightGroups200ResponseInner&gt;**](AppleMappingTestFlightGroups200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="devicesDeviceDetails"></a>
# **devicesDeviceDetails**
> DevicesList200ResponseInner devicesDeviceDetails(deviceUdid)



Returns the device details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String deviceUdid = "deviceUdid_example"; // String | The UDID of the device
    try {
      DevicesList200ResponseInner result = apiInstance.devicesDeviceDetails(deviceUdid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#devicesDeviceDetails");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **deviceUdid** | **String**| The UDID of the device | |

### Return type

[**DevicesList200ResponseInner**](DevicesList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | &lt;b&gt;bad_request&lt;/b&gt;: Devices information can only be requested for iOS apps.  |  -  |
| **403** | &lt;b&gt;forbidden&lt;/b&gt;: The user is not allowed to view someone else&#39;s device.  |  -  |
| **404** | &lt;b&gt;not_found&lt;/b&gt;: The user or device can&#39;t be found.  |  -  |

<a id="devicesGetReleaseUpdateDevicesStatus"></a>
# **devicesGetReleaseUpdateDevicesStatus**
> DevicesGetReleaseUpdateDevicesStatus200Response devicesGetReleaseUpdateDevicesStatus(releaseId, resignId, ownerName, appName, includeProvisioningProfile)



Returns the resign status to the caller

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String releaseId = "releaseId_example"; // String | The ID of the release.
    String resignId = "resignId_example"; // String | The ID of the resign operation.
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    Boolean includeProvisioningProfile = true; // Boolean | A boolean value that indicates if the provisioning profile should be return in addition to the status. When set to true, the provisioning profile will be returned only when status is 'complete' or 'preparing_for_testers'.
    try {
      DevicesGetReleaseUpdateDevicesStatus200Response result = apiInstance.devicesGetReleaseUpdateDevicesStatus(releaseId, resignId, ownerName, appName, includeProvisioningProfile);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#devicesGetReleaseUpdateDevicesStatus");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **releaseId** | **String**| The ID of the release. | |
| **resignId** | **String**| The ID of the resign operation. | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **includeProvisioningProfile** | **Boolean**| A boolean value that indicates if the provisioning profile should be return in addition to the status. When set to true, the provisioning profile will be returned only when status is &#39;complete&#39; or &#39;preparing_for_testers&#39;. | [optional] |

### Return type

[**DevicesGetReleaseUpdateDevicesStatus200Response**](DevicesGetReleaseUpdateDevicesStatus200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Error |  -  |
| **404** | &lt;b&gt;not_found&lt;/b&gt;: A distribution group can&#39;t be found.  |  -  |

<a id="devicesList"></a>
# **devicesList**
> List&lt;DevicesList200ResponseInner&gt; devicesList(distributionGroupName, ownerName, appName, releaseId)



Returns all devices associated with the given distribution group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group.
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    BigDecimal releaseId = new BigDecimal(78); // BigDecimal | when provided, gets the provisioning state of the devices owned by users of this distribution group when compared to the provided release.
    try {
      List<DevicesList200ResponseInner> result = apiInstance.devicesList(distributionGroupName, ownerName, appName, releaseId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#devicesList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **distributionGroupName** | **String**| The name of the distribution group. | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **releaseId** | **BigDecimal**| when provided, gets the provisioning state of the devices owned by users of this distribution group when compared to the provided release. | [optional] |

### Return type

[**List&lt;DevicesList200ResponseInner&gt;**](DevicesList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | &lt;b&gt;bad_request&lt;/b&gt;: Devices information can only be requested for iOS apps.  |  -  |
| **404** | &lt;b&gt;not_found&lt;/b&gt;: A distribution group can&#39;t be found.  |  -  |

<a id="devicesListCsvFormat"></a>
# **devicesListCsvFormat**
> devicesListCsvFormat(distributionGroupName, ownerName, appName, unprovisionedOnly, udids)



Returns all devices associated with the given distribution group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group.
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    Boolean unprovisionedOnly = false; // Boolean | when true, filters out provisioned devices
    List<String> udids = Arrays.asList(); // List<String> | multiple UDIDs which should be part of the resulting CSV.
    try {
      apiInstance.devicesListCsvFormat(distributionGroupName, ownerName, appName, unprovisionedOnly, udids);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#devicesListCsvFormat");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **distributionGroupName** | **String**| The name of the distribution group. | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **unprovisionedOnly** | **Boolean**| when true, filters out provisioned devices | [optional] [default to false] |
| **udids** | [**List&lt;String&gt;**](String.md)| multiple UDIDs which should be part of the resulting CSV. | [optional] |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | &lt;b&gt;bad_request&lt;/b&gt;: Devices information can only be requested for iOS apps.  |  -  |
| **404** | &lt;b&gt;not_found&lt;/b&gt;: A distribution group can&#39;t be found.  |  -  |
| **500** | An internal error. |  -  |

<a id="devicesRegisterUserForDevice"></a>
# **devicesRegisterUserForDevice**
> DevicesList200ResponseInner devicesRegisterUserForDevice(userId, devicesRegisterUserForDeviceRequest)



Registers a user for an existing device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String userId = "userId_example"; // String | The ID of the user
    DevicesRegisterUserForDeviceRequest devicesRegisterUserForDeviceRequest = new DevicesRegisterUserForDeviceRequest(); // DevicesRegisterUserForDeviceRequest | The device info.
    try {
      DevicesList200ResponseInner result = apiInstance.devicesRegisterUserForDevice(userId, devicesRegisterUserForDeviceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#devicesRegisterUserForDevice");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **userId** | **String**| The ID of the user | |
| **devicesRegisterUserForDeviceRequest** | [**DevicesRegisterUserForDeviceRequest**](DevicesRegisterUserForDeviceRequest.md)| The device info. | |

### Return type

[**DevicesList200ResponseInner**](DevicesList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | &lt;b&gt;not_found&lt;/b&gt;: The user or the device can&#39;t be found.  |  -  |

<a id="devicesRemoveUserDevice"></a>
# **devicesRemoveUserDevice**
> devicesRemoveUserDevice(deviceUdid)



Removes an existing device from a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String deviceUdid = "deviceUdid_example"; // String | The UDID of the device
    try {
      apiInstance.devicesRemoveUserDevice(deviceUdid);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#devicesRemoveUserDevice");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **deviceUdid** | **String**| The UDID of the device | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | &lt;b&gt;forbidden&lt;/b&gt;: The user is not allowed to delete someone else&#39;s device.  |  -  |
| **404** | &lt;b&gt;not_found&lt;/b&gt;: The user or the device can&#39;t be found.  |  -  |

<a id="devicesUserDevicesList"></a>
# **devicesUserDevicesList**
> List&lt;DevicesList200ResponseInner&gt; devicesUserDevicesList()



Returns all devices associated with the given user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    try {
      List<DevicesList200ResponseInner> result = apiInstance.devicesUserDevicesList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#devicesUserDevicesList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;DevicesList200ResponseInner&gt;**](DevicesList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | &lt;b&gt;bad_request&lt;/b&gt;: Devices information can only be requested for iOS apps.  |  -  |
| **403** | &lt;b&gt;forbidden&lt;/b&gt;: The user is not allowed to view someone else&#39;s devices.  |  -  |

<a id="distibutionReleasesInstallAnalytics"></a>
# **distibutionReleasesInstallAnalytics**
> distibutionReleasesInstallAnalytics(ownerName, appName, distibutionReleasesInstallAnalyticsRequest)



Notify download(s) for the provided distribution release(s).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the app owner
    String appName = "appName_example"; // String | The name of the app
    DistibutionReleasesInstallAnalyticsRequest distibutionReleasesInstallAnalyticsRequest = new DistibutionReleasesInstallAnalyticsRequest(); // DistibutionReleasesInstallAnalyticsRequest | The install analytics request payload
    try {
      apiInstance.distibutionReleasesInstallAnalytics(ownerName, appName, distibutionReleasesInstallAnalyticsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#distibutionReleasesInstallAnalytics");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ownerName** | **String**| The name of the app owner | |
| **appName** | **String**| The name of the app | |
| **distibutionReleasesInstallAnalyticsRequest** | [**DistibutionReleasesInstallAnalyticsRequest**](DistibutionReleasesInstallAnalyticsRequest.md)| The install analytics request payload | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Install Analytics Notification Sent Successfully. |  -  |

<a id="provisioningProfile"></a>
# **provisioningProfile**
> ProvisioningProfileResponse provisioningProfile(releaseId, ownerName, appName)



Return information about the provisioning profile. Only available for iOS.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    Integer releaseId = 56; // Integer | The release_id
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      ProvisioningProfileResponse result = apiInstance.provisioningProfile(releaseId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#provisioningProfile");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **releaseId** | **Integer**| The release_id | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**ProvisioningProfileResponse**](ProvisioningProfileResponse.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | The app&#39;s OS is not iOS. |  -  |

<a id="releasesAddDistributionGroup"></a>
# **releasesAddDistributionGroup**
> ReleasesAddDistributionGroup201Response releasesAddDistributionGroup(releaseId, ownerName, appName, releasesAddDistributionGroupRequest)



Distributes a release to a group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    Integer releaseId = 56; // Integer | The ID of the release
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    ReleasesAddDistributionGroupRequest releasesAddDistributionGroupRequest = new ReleasesAddDistributionGroupRequest(); // ReleasesAddDistributionGroupRequest | The release information.
    try {
      ReleasesAddDistributionGroup201Response result = apiInstance.releasesAddDistributionGroup(releaseId, ownerName, appName, releasesAddDistributionGroupRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#releasesAddDistributionGroup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **releaseId** | **Integer**| The ID of the release | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **releasesAddDistributionGroupRequest** | [**ReleasesAddDistributionGroupRequest**](ReleasesAddDistributionGroupRequest.md)| The release information. | |

### Return type

[**ReleasesAddDistributionGroup201Response**](ReleasesAddDistributionGroup201Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Failure |  -  |
| **404** | Release not found |  -  |

<a id="releasesAddStore"></a>
# **releasesAddStore**
> ReleasesAddStore201Response releasesAddStore(releaseId, ownerName, appName, releasesAddStoreRequest)



Distributes a release to a store

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    Integer releaseId = 56; // Integer | The ID of the release
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    ReleasesAddStoreRequest releasesAddStoreRequest = new ReleasesAddStoreRequest(); // ReleasesAddStoreRequest | The release information.
    try {
      ReleasesAddStore201Response result = apiInstance.releasesAddStore(releaseId, ownerName, appName, releasesAddStoreRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#releasesAddStore");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **releaseId** | **Integer**| The ID of the release | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **releasesAddStoreRequest** | [**ReleasesAddStoreRequest**](ReleasesAddStoreRequest.md)| The release information. | |

### Return type

[**ReleasesAddStore201Response**](ReleasesAddStore201Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Failure |  -  |
| **404** | Release not found |  -  |

<a id="releasesAddTesters"></a>
# **releasesAddTesters**
> ReleasesAddDistributionGroup201Response releasesAddTesters(releaseId, ownerName, appName, releasesAddTestersRequest)



Distributes a release to a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    Integer releaseId = 56; // Integer | The ID of the release
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    ReleasesAddTestersRequest releasesAddTestersRequest = new ReleasesAddTestersRequest(); // ReleasesAddTestersRequest | The release information.
    try {
      ReleasesAddDistributionGroup201Response result = apiInstance.releasesAddTesters(releaseId, ownerName, appName, releasesAddTestersRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#releasesAddTesters");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **releaseId** | **Integer**| The ID of the release | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **releasesAddTestersRequest** | [**ReleasesAddTestersRequest**](ReleasesAddTestersRequest.md)| The release information. | |

### Return type

[**ReleasesAddDistributionGroup201Response**](ReleasesAddDistributionGroup201Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Failure |  -  |
| **404** | Release not found |  -  |

<a id="releasesAvailableToTester"></a>
# **releasesAvailableToTester**
> List&lt;ReleasesListLatest200ResponseInner&gt; releasesAvailableToTester(ownerName, appName, publishedOnly)



Return detailed information about releases avaiable to a tester.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    Boolean publishedOnly = true; // Boolean | when *true*, filters out releases that were uploaded but were never distributed. Releases that under deleted distribution groups will not be filtered out.
    try {
      List<ReleasesListLatest200ResponseInner> result = apiInstance.releasesAvailableToTester(ownerName, appName, publishedOnly);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#releasesAvailableToTester");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **publishedOnly** | **Boolean**| when *true*, filters out releases that were uploaded but were never distributed. Releases that under deleted distribution groups will not be filtered out. | [optional] |

### Return type

[**List&lt;ReleasesListLatest200ResponseInner&gt;**](ReleasesListLatest200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="releasesCreateReleaseUpload"></a>
# **releasesCreateReleaseUpload**
> ReleasesCreateReleaseUpload201Response releasesCreateReleaseUpload(ownerName, appName, releasesCreateReleaseUploadRequest)



Initiate a new release upload. This API is part of multi-step upload process.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    ReleasesCreateReleaseUploadRequest releasesCreateReleaseUploadRequest = new ReleasesCreateReleaseUploadRequest(); // ReleasesCreateReleaseUploadRequest | Optional parameters to create releases with user defined metadata
    try {
      ReleasesCreateReleaseUpload201Response result = apiInstance.releasesCreateReleaseUpload(ownerName, appName, releasesCreateReleaseUploadRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#releasesCreateReleaseUpload");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **releasesCreateReleaseUploadRequest** | [**ReleasesCreateReleaseUploadRequest**](ReleasesCreateReleaseUploadRequest.md)| Optional parameters to create releases with user defined metadata | [optional] |

### Return type

[**ReleasesCreateReleaseUpload201Response**](ReleasesCreateReleaseUpload201Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | The request contained invalid properties. |  -  |
| **404** | Error codes: - &#x60;not_found&#x60; - The app doesn&#39;t exist.  |  -  |

<a id="releasesDelete"></a>
# **releasesDelete**
> releasesDelete(releaseId, ownerName, appName)



Deletes a release.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    Integer releaseId = 56; // Integer | The ID of the release
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      apiInstance.releasesDelete(releaseId, ownerName, appName);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#releasesDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **releaseId** | **Integer**| The ID of the release | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | An app or a release couldn&#39;t be found  |  -  |
| **500** | An internal error. if delete has partially failed **partially_deleted** error_code will be returned. - &#x60;partially_deleted&#x60;: Release was removed from all distribution groups, but couldn&#39;t be deleted from App Center.  |  -  |

<a id="releasesDeleteDistributionGroup"></a>
# **releasesDeleteDistributionGroup**
> releasesDeleteDistributionGroup(releaseId, groupId, ownerName, appName)



Delete the given distribution group from the release

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    Integer releaseId = 56; // Integer | The ID of the release
    String groupId = "groupId_example"; // String | The id of the distribution group
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      apiInstance.releasesDeleteDistributionGroup(releaseId, groupId, ownerName, appName);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#releasesDeleteDistributionGroup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **releaseId** | **Integer**| The ID of the release | |
| **groupId** | **String**| The id of the distribution group | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Distribution group destination can&#39;t be found.  |  -  |

<a id="releasesDeleteDistributionStore"></a>
# **releasesDeleteDistributionStore**
> releasesDeleteDistributionStore(releaseId, storeId, ownerName, appName)



Delete the given distribution store from the release

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    Integer releaseId = 56; // Integer | The ID of the release
    String storeId = "storeId_example"; // String | The id of the distribution store
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      apiInstance.releasesDeleteDistributionStore(releaseId, storeId, ownerName, appName);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#releasesDeleteDistributionStore");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **releaseId** | **Integer**| The ID of the release | |
| **storeId** | **String**| The id of the distribution store | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Distribution store destination can&#39;t be found.  |  -  |

<a id="releasesDeleteDistributionTester"></a>
# **releasesDeleteDistributionTester**
> releasesDeleteDistributionTester(releaseId, testerId, ownerName, appName)



Delete the given tester from the release

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    Integer releaseId = 56; // Integer | The ID of the release
    String testerId = "testerId_example"; // String | The id of the tester
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      apiInstance.releasesDeleteDistributionTester(releaseId, testerId, ownerName, appName);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#releasesDeleteDistributionTester");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **releaseId** | **Integer**| The ID of the release | |
| **testerId** | **String**| The id of the tester | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Tester can&#39;t be found  |  -  |

<a id="releasesDeleteTesterFromDestinations"></a>
# **releasesDeleteTesterFromDestinations**
> releasesDeleteTesterFromDestinations(testerId, ownerName, appName)



Delete the given tester from the all releases

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String testerId = "testerId_example"; // String | The id of the tester
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      apiInstance.releasesDeleteTesterFromDestinations(testerId, ownerName, appName);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#releasesDeleteTesterFromDestinations");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **testerId** | **String**| The id of the tester | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Tester can&#39;t be found  |  -  |

<a id="releasesDeleteWithDistributionGroupId"></a>
# **releasesDeleteWithDistributionGroupId**
> releasesDeleteWithDistributionGroupId(ownerName, appName, distributionGroupName, releaseId)



Deletes a release with id &#39;release_id&#39; in a given distribution group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the app owner
    String appName = "appName_example"; // String | The name of the app
    String distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group.
    Integer releaseId = 56; // Integer | The ID identifying the unique release.
    try {
      apiInstance.releasesDeleteWithDistributionGroupId(ownerName, appName, distributionGroupName, releaseId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#releasesDeleteWithDistributionGroupId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ownerName** | **String**| The name of the app owner | |
| **appName** | **String**| The name of the app | |
| **distributionGroupName** | **String**| The name of the distribution group. | |
| **releaseId** | **Integer**| The ID identifying the unique release. | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Error codes: - &#x60;distribution_group_not_found&#x60; - Distribution group or the app doesn&#39;t exist. - &#x60;not_found&#x60; - release isn&#39;t found.  |  -  |

<a id="releasesGetIosManifest"></a>
# **releasesGetIosManifest**
> releasesGetIosManifest(appId, releaseId, token)



Returns the manifest.plist in XML format for installing the release on a device. Only available for iOS.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String appId = "appId_example"; // String | The ID of the application
    Integer releaseId = 56; // Integer | The release_id
    String token = "token_example"; // String | A hash that authorizes the download if it matches the release info.
    try {
      apiInstance.releasesGetIosManifest(appId, releaseId, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#releasesGetIosManifest");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **String**| The ID of the application | |
| **releaseId** | **Integer**| The release_id | |
| **token** | **String**| A hash that authorizes the download if it matches the release info. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | The app&#39;s OS is not iOS. |  -  |
| **403** | Forbidden - The token provided doesn&#39;t match the release&#39;s token. |  -  |
| **404** | The app or release can&#39;t be found. |  -  |

<a id="releasesGetLatestByDistributionGroup"></a>
# **releasesGetLatestByDistributionGroup**
> ReleasesGetLatestByDistributionGroup200Response releasesGetLatestByDistributionGroup(ownerName, appName, distributionGroupName, releaseId, isInstallPage)



Return detailed information about a distributed release in a given distribution group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the app owner
    String appName = "appName_example"; // String | The name of the app
    String distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group.
    String releaseId = "releaseId_example"; // String | Also supports the constant `latest`, which will return the latest release in the distribution group.
    Boolean isInstallPage = true; // Boolean | The check if the request is from Install page
    try {
      ReleasesGetLatestByDistributionGroup200Response result = apiInstance.releasesGetLatestByDistributionGroup(ownerName, appName, distributionGroupName, releaseId, isInstallPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#releasesGetLatestByDistributionGroup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ownerName** | **String**| The name of the app owner | |
| **appName** | **String**| The name of the app | |
| **distributionGroupName** | **String**| The name of the distribution group. | |
| **releaseId** | **String**| Also supports the constant &#x60;latest&#x60;, which will return the latest release in the distribution group. | |
| **isInstallPage** | **Boolean**| The check if the request is from Install page | [optional] |

### Return type

[**ReleasesGetLatestByDistributionGroup200Response**](ReleasesGetLatestByDistributionGroup200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Error Codes: - &#x60;not_found&#x60; - Distribution group or the app doesn&#39;t exist - &#x60;no_releases_for_app&#x60; - App has no releases.  |  -  |
| **501** | Requesting a specific release_id is not supported.  |  -  |

<a id="releasesGetLatestByHash"></a>
# **releasesGetLatestByHash**
> ReleasesGetLatestByDistributionGroup200Response releasesGetLatestByHash(appSecret, releaseHash, udid)



If &#39;latest&#39; is not specified then it will return the specified release if it&#39;s enabled. If &#39;latest&#39; is specified, regardless of whether a release hash is provided, the latest enabled release is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String appSecret = "appSecret_example"; // String | The secret of the target application
    String releaseHash = "releaseHash_example"; // String | The hash of the release or 'latest' to get the latest release from all the distribution groups assigned to the current user.
    String udid = "udid_example"; // String | When passing `udid` in the query string, a provisioning check for the given device ID will be done. Will be ignored for non-iOS platforms.
    try {
      ReleasesGetLatestByDistributionGroup200Response result = apiInstance.releasesGetLatestByHash(appSecret, releaseHash, udid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#releasesGetLatestByHash");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appSecret** | **String**| The secret of the target application | |
| **releaseHash** | **String**| The hash of the release or &#39;latest&#39; to get the latest release from all the distribution groups assigned to the current user. | |
| **udid** | **String**| When passing &#x60;udid&#x60; in the query string, a provisioning check for the given device ID will be done. Will be ignored for non-iOS platforms. | [optional] |

### Return type

[**ReleasesGetLatestByDistributionGroup200Response**](ReleasesGetLatestByDistributionGroup200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | If called with a specific &#x60;release_hash&#x60; return the app&#39;s &#39;display_name&#39;&#39; and &#39;buildIdentifier&#39;. If &#39;release_hash&#39; is &#39;latest&#39; return the full release details of the latest release that was distributed to the current user (from all the distribution groups). |  -  |
| **404** | Error codes: - &#x60;not_found&#x60; - A release or an app can&#39;t be found. - &#x60;no_releases_for_user&#x60; - No releases available for that user (will only be returned when &#x60;release_hash&#x60; is &#x60;latest&#x60;)  |  -  |

<a id="releasesGetLatestByPublicDistributionGroup"></a>
# **releasesGetLatestByPublicDistributionGroup**
> ReleasesGetLatestByDistributionGroup200Response releasesGetLatestByPublicDistributionGroup(appSecret, distributionGroupId, isInstallPage)



Get a release with &#39;latest&#39; for the given public group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String appSecret = "appSecret_example"; // String | The secret of the target application
    String distributionGroupId = "distributionGroupId_example"; // String | the id for destination
    Boolean isInstallPage = true; // Boolean | The check if the request is from Install page
    try {
      ReleasesGetLatestByDistributionGroup200Response result = apiInstance.releasesGetLatestByPublicDistributionGroup(appSecret, distributionGroupId, isInstallPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#releasesGetLatestByPublicDistributionGroup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appSecret** | **String**| The secret of the target application | |
| **distributionGroupId** | **String**| the id for destination | |
| **isInstallPage** | **Boolean**| The check if the request is from Install page | [optional] |

### Return type

[**ReleasesGetLatestByDistributionGroup200Response**](ReleasesGetLatestByDistributionGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The full release details of the latest release that was distributed from the given public group. |  -  |
| **403** | Error Codes: - &#x60;forbidden&#x60; - Unauthorized to access private distribution group  |  -  |
| **404** | Error Codes: - &#x60;not_found&#x60; - Distribution group or the app doesn&#39;t exist - &#x60;no_releases_for_app&#x60; - App has no releases.  |  -  |

<a id="releasesGetLatestByUser"></a>
# **releasesGetLatestByUser**
> ReleasesGetLatestByDistributionGroup200Response releasesGetLatestByUser(releaseId, ownerName, appName, udid, isInstallPage)



Get a release with id &#x60;release_id&#x60;. If &#x60;release_id&#x60; is &#x60;latest&#x60;, return the latest release that was distributed to the current user (from all the distribution groups).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String releaseId = "releaseId_example"; // String | The ID of the release, or `latest` to get the latest release from all the distribution groups assigned to the current user.
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    String udid = "udid_example"; // String | when supplied, this call will also check if the given UDID is provisioned. Will be ignored for non-iOS platforms. The value will be returned in the property is_udid_provisioned.
    Boolean isInstallPage = true; // Boolean | The check if the request is from Install page
    try {
      ReleasesGetLatestByDistributionGroup200Response result = apiInstance.releasesGetLatestByUser(releaseId, ownerName, appName, udid, isInstallPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#releasesGetLatestByUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **releaseId** | **String**| The ID of the release, or &#x60;latest&#x60; to get the latest release from all the distribution groups assigned to the current user. | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **udid** | **String**| when supplied, this call will also check if the given UDID is provisioned. Will be ignored for non-iOS platforms. The value will be returned in the property is_udid_provisioned. | [optional] |
| **isInstallPage** | **Boolean**| The check if the request is from Install page | [optional] |

### Return type

[**ReleasesGetLatestByDistributionGroup200Response**](ReleasesGetLatestByDistributionGroup200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | &#x60;release_id&#x60; is not an integer or the string &#x60;latest&#x60;.  |  -  |
| **404** | Error codes: - &#x60;not_found&#x60; - A release or an app can&#39;t be found. - &#x60;no_releases_for_user&#x60; - No releases available for that user (will only be returned when &#x60;release_id&#x60; is &#x60;latest&#x60;)  |  -  |

<a id="releasesGetLatestPrivateRelease"></a>
# **releasesGetLatestPrivateRelease**
> ReleasesGetLatestByDistributionGroup200Response releasesGetLatestPrivateRelease(appSecret, udid)



Get the latest release distributed to a private group the given user is a member of for the given app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String appSecret = "appSecret_example"; // String | The secret of the target application
    String udid = "udid_example"; // String | When passing `udid` in the query string, a provisioning check for the given device ID will be done. Will be ignored for non-iOS platforms.
    try {
      ReleasesGetLatestByDistributionGroup200Response result = apiInstance.releasesGetLatestPrivateRelease(appSecret, udid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#releasesGetLatestPrivateRelease");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appSecret** | **String**| The secret of the target application | |
| **udid** | **String**| When passing &#x60;udid&#x60; in the query string, a provisioning check for the given device ID will be done. Will be ignored for non-iOS platforms. | [optional] |

### Return type

[**ReleasesGetLatestByDistributionGroup200Response**](ReleasesGetLatestByDistributionGroup200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return the full release details of the latest release that was distributed to the current user (from all the private distribution groups). |  -  |
| **404** | Error codes: - &#x60;not_found&#x60; - A release or an app can&#39;t be found. - &#x60;no_releases_for_user&#x60; - No releases available for that user.  |  -  |

<a id="releasesGetLatestPublicRelease"></a>
# **releasesGetLatestPublicRelease**
> ReleasesGetLatestByDistributionGroup200Response releasesGetLatestPublicRelease(appSecret)



Get the latest public release for the given app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String appSecret = "appSecret_example"; // String | The secret of the target application
    try {
      ReleasesGetLatestByDistributionGroup200Response result = apiInstance.releasesGetLatestPublicRelease(appSecret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#releasesGetLatestPublicRelease");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appSecret** | **String**| The secret of the target application | |

### Return type

[**ReleasesGetLatestByDistributionGroup200Response**](ReleasesGetLatestByDistributionGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The full release details of the latest release that was distributed to a public group. |  -  |
| **404** | Error Codes: - &#x60;not_found&#x60; - The app doesn&#39;t exist - &#x60;no_releases_for_app&#x60; - The app has no public releases.  |  -  |

<a id="releasesGetPublicGroupsForReleaseByHash"></a>
# **releasesGetPublicGroupsForReleaseByHash**
> List&lt;ReleasesGetPublicGroupsForReleaseByHash200ResponseInner&gt; releasesGetPublicGroupsForReleaseByHash(appSecret, releaseHash)



Get all public distribution groups that a given release has been distributed to

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String appSecret = "appSecret_example"; // String | The secret of the target application
    String releaseHash = "releaseHash_example"; // String | The hash of the release
    try {
      List<ReleasesGetPublicGroupsForReleaseByHash200ResponseInner> result = apiInstance.releasesGetPublicGroupsForReleaseByHash(appSecret, releaseHash);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#releasesGetPublicGroupsForReleaseByHash");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appSecret** | **String**| The secret of the target application | |
| **releaseHash** | **String**| The hash of the release | |

### Return type

[**List&lt;ReleasesGetPublicGroupsForReleaseByHash200ResponseInner&gt;**](ReleasesGetPublicGroupsForReleaseByHash200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The public distribution groups that the release has been distributed to |  -  |
| **404** | Error Codes: - &#x60;not_found&#x60; - The app doesn&#39;t exist  |  -  |

<a id="releasesGetReleaseUploadStatus"></a>
# **releasesGetReleaseUploadStatus**
> ReleasesGetReleaseUploadStatus200Response releasesGetReleaseUploadStatus(uploadId, ownerName, appName)



Get the current status of the release upload.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    UUID uploadId = UUID.randomUUID(); // UUID | The ID of the release upload
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      ReleasesGetReleaseUploadStatus200Response result = apiInstance.releasesGetReleaseUploadStatus(uploadId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#releasesGetReleaseUploadStatus");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **uploadId** | **UUID**| The ID of the release upload | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**ReleasesGetReleaseUploadStatus200Response**](ReleasesGetReleaseUploadStatus200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | The request contained invalid properties. |  -  |
| **404** | Error codes: - &#x60;not_found&#x60; - The app or upload doesn&#39;t exist.  |  -  |

<a id="releasesGetSparkleFeed"></a>
# **releasesGetSparkleFeed**
> releasesGetSparkleFeed(appSecret)



Gets the sparkle feed of the releases that are distributed to all the public distribution groups.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String appSecret = "appSecret_example"; // String | The secret of the application.
    try {
      apiInstance.releasesGetSparkleFeed(appSecret);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#releasesGetSparkleFeed");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appSecret** | **String**| The secret of the application. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The RSS feed of releases. |  -  |
| **0** | Error |  -  |

<a id="releasesList"></a>
# **releasesList**
> List&lt;ReleasesListLatest200ResponseInner&gt; releasesList(ownerName, appName, publishedOnly, scope, top, releaseId)



Return basic information about releases.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    Boolean publishedOnly = true; // Boolean | When *true*, filters out releases that were uploaded but were never distributed. Releases that under deleted distribution groups will not be filtered out.
    String scope = "scope_example"; // String | When the scope is 'tester', only includes releases that have been distributed to groups that the user belongs to.
    BigDecimal top = new BigDecimal(78); // BigDecimal | The number of releases to return
    BigDecimal releaseId = new BigDecimal(78); // BigDecimal | The id of a release
    try {
      List<ReleasesListLatest200ResponseInner> result = apiInstance.releasesList(ownerName, appName, publishedOnly, scope, top, releaseId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#releasesList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **publishedOnly** | **Boolean**| When *true*, filters out releases that were uploaded but were never distributed. Releases that under deleted distribution groups will not be filtered out. | [optional] |
| **scope** | **String**| When the scope is &#39;tester&#39;, only includes releases that have been distributed to groups that the user belongs to. | [optional] |
| **top** | **BigDecimal**| The number of releases to return | [optional] |
| **releaseId** | **BigDecimal**| The id of a release | [optional] |

### Return type

[**List&lt;ReleasesListLatest200ResponseInner&gt;**](ReleasesListLatest200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="releasesListByDistributionGroup"></a>
# **releasesListByDistributionGroup**
> List&lt;ReleasesListByDistributionGroup200ResponseInner&gt; releasesListByDistributionGroup(distributionGroupName, ownerName, appName)



Return basic information about distributed releases in a given distribution group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group.
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      List<ReleasesListByDistributionGroup200ResponseInner> result = apiInstance.releasesListByDistributionGroup(distributionGroupName, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#releasesListByDistributionGroup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **distributionGroupName** | **String**| The name of the distribution group. | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**List&lt;ReleasesListByDistributionGroup200ResponseInner&gt;**](ReleasesListByDistributionGroup200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | A distribution group can&#39;t be found.  |  -  |

<a id="releasesListLatest"></a>
# **releasesListLatest**
> List&lt;ReleasesListLatest200ResponseInner&gt; releasesListLatest(ownerName, appName)



Get the latest release from every distribution group associated with an application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      List<ReleasesListLatest200ResponseInner> result = apiInstance.releasesListLatest(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#releasesListLatest");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**List&lt;ReleasesListLatest200ResponseInner&gt;**](ReleasesListLatest200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="releasesPutDistributionGroup"></a>
# **releasesPutDistributionGroup**
> releasesPutDistributionGroup(releaseId, groupId, ownerName, appName, releasesPutDistributionGroupRequest)



Update details about the specified distribution group associated with the release

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    Integer releaseId = 56; // Integer | The ID of the release
    UUID groupId = UUID.randomUUID(); // UUID | The id of the releases destination
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    ReleasesPutDistributionGroupRequest releasesPutDistributionGroupRequest = new ReleasesPutDistributionGroupRequest(); // ReleasesPutDistributionGroupRequest | 
    try {
      apiInstance.releasesPutDistributionGroup(releaseId, groupId, ownerName, appName, releasesPutDistributionGroupRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#releasesPutDistributionGroup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **releaseId** | **Integer**| The ID of the release | |
| **groupId** | **UUID**| The id of the releases destination | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **releasesPutDistributionGroupRequest** | [**ReleasesPutDistributionGroupRequest**](ReleasesPutDistributionGroupRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | A destination can&#39;t be found.  |  -  |

<a id="releasesPutDistributionTester"></a>
# **releasesPutDistributionTester**
> releasesPutDistributionTester(releaseId, testerId, ownerName, appName, releasesPutDistributionGroupRequest)



Update details about the specified tester associated with the release

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    Integer releaseId = 56; // Integer | The ID of the release
    UUID testerId = UUID.randomUUID(); // UUID | The id of the tester
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    ReleasesPutDistributionGroupRequest releasesPutDistributionGroupRequest = new ReleasesPutDistributionGroupRequest(); // ReleasesPutDistributionGroupRequest | 
    try {
      apiInstance.releasesPutDistributionTester(releaseId, testerId, ownerName, appName, releasesPutDistributionGroupRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#releasesPutDistributionTester");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **releaseId** | **Integer**| The ID of the release | |
| **testerId** | **UUID**| The id of the tester | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **releasesPutDistributionGroupRequest** | [**ReleasesPutDistributionGroupRequest**](ReleasesPutDistributionGroupRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | A destination can&#39;t be found.  |  -  |

<a id="releasesUpdate"></a>
# **releasesUpdate**
> ReleasesUpdate200Response releasesUpdate(releaseId, ownerName, appName, releasesUpdateRequest)



Updates a release.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    Integer releaseId = 56; // Integer | The ID of the release
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    ReleasesUpdateRequest releasesUpdateRequest = new ReleasesUpdateRequest(); // ReleasesUpdateRequest | The release information.
    try {
      ReleasesUpdate200Response result = apiInstance.releasesUpdate(releaseId, ownerName, appName, releasesUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#releasesUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **releaseId** | **Integer**| The ID of the release | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **releasesUpdateRequest** | [**ReleasesUpdateRequest**](ReleasesUpdateRequest.md)| The release information. | |

### Return type

[**ReleasesUpdate200Response**](ReleasesUpdate200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Failure |  -  |
| **404** | Release not found |  -  |

<a id="releasesUpdateDetails"></a>
# **releasesUpdateDetails**
> ReleasesUpdateDetails200Response releasesUpdateDetails(releaseId, ownerName, appName, releasesUpdateDetailsRequest)



Update details of a release.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    Integer releaseId = 56; // Integer | The ID of the release
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    ReleasesUpdateDetailsRequest releasesUpdateDetailsRequest = new ReleasesUpdateDetailsRequest(); // ReleasesUpdateDetailsRequest | The release information.
    try {
      ReleasesUpdateDetails200Response result = apiInstance.releasesUpdateDetails(releaseId, ownerName, appName, releasesUpdateDetailsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#releasesUpdateDetails");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **releaseId** | **Integer**| The ID of the release | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **releasesUpdateDetailsRequest** | [**ReleasesUpdateDetailsRequest**](ReleasesUpdateDetailsRequest.md)| The release information. | |

### Return type

[**ReleasesUpdateDetails200Response**](ReleasesUpdateDetails200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Failure |  -  |
| **404** | Release not found |  -  |

<a id="releasesUpdateReleaseUploadStatus"></a>
# **releasesUpdateReleaseUploadStatus**
> ReleasesUpdateReleaseUploadStatus200Response releasesUpdateReleaseUploadStatus(uploadId, ownerName, appName, releasesUpdateReleaseUploadStatusRequest, extract)



Update the current status of the release upload.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    UUID uploadId = UUID.randomUUID(); // UUID | The ID of the release upload
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    ReleasesUpdateReleaseUploadStatusRequest releasesUpdateReleaseUploadStatusRequest = new ReleasesUpdateReleaseUploadStatusRequest(); // ReleasesUpdateReleaseUploadStatusRequest | The release upload status information.
    Boolean extract = true; // Boolean | A flag that indicates to extract release or not, true by default
    try {
      ReleasesUpdateReleaseUploadStatus200Response result = apiInstance.releasesUpdateReleaseUploadStatus(uploadId, ownerName, appName, releasesUpdateReleaseUploadStatusRequest, extract);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#releasesUpdateReleaseUploadStatus");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **uploadId** | **UUID**| The ID of the release upload | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **releasesUpdateReleaseUploadStatusRequest** | [**ReleasesUpdateReleaseUploadStatusRequest**](ReleasesUpdateReleaseUploadStatusRequest.md)| The release upload status information. | |
| **extract** | **Boolean**| A flag that indicates to extract release or not, true by default | [optional] |

### Return type

[**ReleasesUpdateReleaseUploadStatus200Response**](ReleasesUpdateReleaseUploadStatus200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | The request contained invalid properties. |  -  |
| **404** | Error codes: - &#x60;not_found&#x60; - The app or upload doesn&#39;t exist.  |  -  |

<a id="storeNotificationsGetNotificationByAppId"></a>
# **storeNotificationsGetNotificationByAppId**
> StoreNotificationsGetNotificationByAppId200Response storeNotificationsGetNotificationByAppId(ownerName, appName)



Application specific store service status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      StoreNotificationsGetNotificationByAppId200Response result = apiInstance.storeNotificationsGetNotificationByAppId(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#storeNotificationsGetNotificationByAppId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**StoreNotificationsGetNotificationByAppId200Response**](StoreNotificationsGetNotificationByAppId200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. Availability for store service status is stored in response schema. |  -  |
| **0** | Error |  -  |

<a id="storeReleasePublishLogsGet"></a>
# **storeReleasePublishLogsGet**
> storeReleasePublishLogsGet(storeName, releaseId, ownerName, appName)



Returns publish logs for a particular release published to a particular store

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String storeName = "storeName_example"; // String | The name of the store
    String releaseId = "releaseId_example"; // String | The ID of the realease
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      apiInstance.storeReleasePublishLogsGet(storeName, releaseId, ownerName, appName);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#storeReleasePublishLogsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **storeName** | **String**| The name of the store | |
| **releaseId** | **String**| The ID of the realease | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="storeReleasesDelete"></a>
# **storeReleasesDelete**
> storeReleasesDelete(storeName, releaseId, ownerName, appName, body)



delete the release with release Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String storeName = "storeName_example"; // String | The name of the store
    String releaseId = "releaseId_example"; // String | The id of the release
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    String body = "body_example"; // String | 
    try {
      apiInstance.storeReleasesDelete(storeName, releaseId, ownerName, appName, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#storeReleasesDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **storeName** | **String**| The name of the store | |
| **releaseId** | **String**| The id of the release | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **body** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="storeReleasesGet"></a>
# **storeReleasesGet**
> List&lt;StoreReleasesGetLatest200ResponseInner&gt; storeReleasesGet(storeName, releaseId, ownerName, appName)



Return releases published in a store for releaseId and storeId

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String storeName = "storeName_example"; // String | The name of the store
    String releaseId = "releaseId_example"; // String | The name of the store
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      List<StoreReleasesGetLatest200ResponseInner> result = apiInstance.storeReleasesGet(storeName, releaseId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#storeReleasesGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **storeName** | **String**| The name of the store | |
| **releaseId** | **String**| The name of the store | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**List&lt;StoreReleasesGetLatest200ResponseInner&gt;**](StoreReleasesGetLatest200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="storeReleasesGetLatest"></a>
# **storeReleasesGetLatest**
> List&lt;StoreReleasesGetLatest200ResponseInner&gt; storeReleasesGetLatest(storeName, ownerName, appName)



Returns the latest release published in a store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String storeName = "storeName_example"; // String | The name of the store
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      List<StoreReleasesGetLatest200ResponseInner> result = apiInstance.storeReleasesGetLatest(storeName, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#storeReleasesGetLatest");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **storeName** | **String**| The name of the store | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**List&lt;StoreReleasesGetLatest200ResponseInner&gt;**](StoreReleasesGetLatest200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="storeReleasesGetPublishError"></a>
# **storeReleasesGetPublishError**
> StoreReleasesGetPublishError200Response storeReleasesGetPublishError(storeName, releaseId, ownerName, appName)



Return the Error Details of release which failed in publishing.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String storeName = "storeName_example"; // String | The name of the store
    BigDecimal releaseId = new BigDecimal(78); // BigDecimal | The id of the release
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      StoreReleasesGetPublishError200Response result = apiInstance.storeReleasesGetPublishError(storeName, releaseId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#storeReleasesGetPublishError");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **storeName** | **String**| The name of the store | |
| **releaseId** | **BigDecimal**| The id of the release | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**StoreReleasesGetPublishError200Response**](StoreReleasesGetPublishError200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="storeReleasesGetRealTimeStatusByReleaseId"></a>
# **storeReleasesGetRealTimeStatusByReleaseId**
> StoreReleasesGetRealTimeStatusByReleaseId200Response storeReleasesGetRealTimeStatusByReleaseId(storeName, releaseId, ownerName, appName)



Return the Real time Status publishing of release from store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String storeName = "storeName_example"; // String | The name of the store
    BigDecimal releaseId = new BigDecimal(78); // BigDecimal | The id of the release
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      StoreReleasesGetRealTimeStatusByReleaseId200Response result = apiInstance.storeReleasesGetRealTimeStatusByReleaseId(storeName, releaseId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#storeReleasesGetRealTimeStatusByReleaseId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **storeName** | **String**| The name of the store | |
| **releaseId** | **BigDecimal**| The id of the release | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**StoreReleasesGetRealTimeStatusByReleaseId200Response**](StoreReleasesGetRealTimeStatusByReleaseId200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="storeReleasesList"></a>
# **storeReleasesList**
> List&lt;StoreReleasesList200ResponseInner&gt; storeReleasesList(storeName, ownerName, appName)



Return all releases published  in a store

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String storeName = "storeName_example"; // String | The name of the store
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      List<StoreReleasesList200ResponseInner> result = apiInstance.storeReleasesList(storeName, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#storeReleasesList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **storeName** | **String**| The name of the store | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**List&lt;StoreReleasesList200ResponseInner&gt;**](StoreReleasesList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="storesCreate"></a>
# **storesCreate**
> StoresList200ResponseInner storesCreate(ownerName, appName, storesCreateRequest)



Create a new external store for the specified application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    StoresCreateRequest storesCreateRequest = new StoresCreateRequest(); // StoresCreateRequest | The store request
    try {
      StoresList200ResponseInner result = apiInstance.storesCreate(ownerName, appName, storesCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#storesCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **storesCreateRequest** | [**StoresCreateRequest**](StoresCreateRequest.md)| The store request | |

### Return type

[**StoresList200ResponseInner**](StoresList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **0** | Error |  -  |

<a id="storesDelete"></a>
# **storesDelete**
> storesDelete(storeName, ownerName, appName, body)



delete the store based on specific store name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String storeName = "storeName_example"; // String | The name of the store
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    String body = "body_example"; // String | 
    try {
      apiInstance.storesDelete(storeName, ownerName, appName, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#storesDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **storeName** | **String**| The name of the store | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **body** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="storesGet"></a>
# **storesGet**
> StoresList200ResponseInner storesGet(storeName, ownerName, appName)



Return the store details for specified store name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String storeName = "storeName_example"; // String | The name of the store
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      StoresList200ResponseInner result = apiInstance.storesGet(storeName, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#storesGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **storeName** | **String**| The name of the store | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**StoresList200ResponseInner**](StoresList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="storesList"></a>
# **storesList**
> List&lt;StoresList200ResponseInner&gt; storesList(ownerName, appName)



Get all the store details from Storage store table for a particular application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      List<StoresList200ResponseInner> result = apiInstance.storesList(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#storesList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**List&lt;StoresList200ResponseInner&gt;**](StoresList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="storesPatch"></a>
# **storesPatch**
> storesPatch(storeName, ownerName, appName, storesPatchRequest)



Update the store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    DistributeApi apiInstance = new DistributeApi(defaultClient);
    String storeName = "storeName_example"; // String | The name of the store
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    StoresPatchRequest storesPatchRequest = new StoresPatchRequest(); // StoresPatchRequest | Store update request
    try {
      apiInstance.storesPatch(storeName, ownerName, appName, storesPatchRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistributeApi#storesPatch");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **storeName** | **String**| The name of the store | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **storesPatchRequest** | [**StoresPatchRequest**](StoresPatchRequest.md)| Store update request | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

