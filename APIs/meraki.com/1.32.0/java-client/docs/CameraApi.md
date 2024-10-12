# CameraApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkCameraQualityRetentionProfile**](CameraApi.md#createNetworkCameraQualityRetentionProfile) | **POST** /networks/{networkId}/camera/qualityRetentionProfiles | Creates new quality retention profile for this network. |
| [**createNetworkCameraWirelessProfile**](CameraApi.md#createNetworkCameraWirelessProfile) | **POST** /networks/{networkId}/camera/wirelessProfiles | Creates a new camera wireless profile for this network. |
| [**createOrganizationCameraCustomAnalyticsArtifact**](CameraApi.md#createOrganizationCameraCustomAnalyticsArtifact) | **POST** /organizations/{organizationId}/camera/customAnalytics/artifacts | Create custom analytics artifact |
| [**deleteNetworkCameraQualityRetentionProfile**](CameraApi.md#deleteNetworkCameraQualityRetentionProfile) | **DELETE** /networks/{networkId}/camera/qualityRetentionProfiles/{qualityRetentionProfileId} | Delete an existing quality retention profile for this network. |
| [**deleteNetworkCameraWirelessProfile**](CameraApi.md#deleteNetworkCameraWirelessProfile) | **DELETE** /networks/{networkId}/camera/wirelessProfiles/{wirelessProfileId} | Delete an existing camera wireless profile for this network. |
| [**deleteOrganizationCameraCustomAnalyticsArtifact**](CameraApi.md#deleteOrganizationCameraCustomAnalyticsArtifact) | **DELETE** /organizations/{organizationId}/camera/customAnalytics/artifacts/{artifactId} | Delete Custom Analytics Artifact |
| [**generateDeviceCameraSnapshot**](CameraApi.md#generateDeviceCameraSnapshot) | **POST** /devices/{serial}/camera/generateSnapshot | Generate a snapshot of what the camera sees at the specified time and return a link to that image. |
| [**getDeviceCameraAnalyticsLive**](CameraApi.md#getDeviceCameraAnalyticsLive) | **GET** /devices/{serial}/camera/analytics/live | Returns live state from camera of analytics zones |
| [**getDeviceCameraAnalyticsOverview**](CameraApi.md#getDeviceCameraAnalyticsOverview) | **GET** /devices/{serial}/camera/analytics/overview | Returns an overview of aggregate analytics data for a timespan |
| [**getDeviceCameraAnalyticsRecent**](CameraApi.md#getDeviceCameraAnalyticsRecent) | **GET** /devices/{serial}/camera/analytics/recent | Returns most recent record for analytics zones |
| [**getDeviceCameraAnalyticsZoneHistory**](CameraApi.md#getDeviceCameraAnalyticsZoneHistory) | **GET** /devices/{serial}/camera/analytics/zones/{zoneId}/history | Return historical records for analytic zones |
| [**getDeviceCameraAnalyticsZones**](CameraApi.md#getDeviceCameraAnalyticsZones) | **GET** /devices/{serial}/camera/analytics/zones | Returns all configured analytic zones for this camera |
| [**getDeviceCameraCustomAnalytics**](CameraApi.md#getDeviceCameraCustomAnalytics) | **GET** /devices/{serial}/camera/customAnalytics | Return custom analytics settings for a camera |
| [**getDeviceCameraQualityAndRetention**](CameraApi.md#getDeviceCameraQualityAndRetention) | **GET** /devices/{serial}/camera/qualityAndRetention | Returns quality and retention settings for the given camera |
| [**getDeviceCameraSense**](CameraApi.md#getDeviceCameraSense) | **GET** /devices/{serial}/camera/sense | Returns sense settings for a given camera |
| [**getDeviceCameraSenseObjectDetectionModels**](CameraApi.md#getDeviceCameraSenseObjectDetectionModels) | **GET** /devices/{serial}/camera/sense/objectDetectionModels | Returns the MV Sense object detection model list for the given camera |
| [**getDeviceCameraVideoLink**](CameraApi.md#getDeviceCameraVideoLink) | **GET** /devices/{serial}/camera/videoLink | Returns video link to the specified camera |
| [**getDeviceCameraVideoSettings**](CameraApi.md#getDeviceCameraVideoSettings) | **GET** /devices/{serial}/camera/video/settings | Returns video settings for the given camera |
| [**getDeviceCameraWirelessProfiles**](CameraApi.md#getDeviceCameraWirelessProfiles) | **GET** /devices/{serial}/camera/wirelessProfiles | Returns wireless profile assigned to the given camera |
| [**getNetworkCameraQualityRetentionProfile**](CameraApi.md#getNetworkCameraQualityRetentionProfile) | **GET** /networks/{networkId}/camera/qualityRetentionProfiles/{qualityRetentionProfileId} | Retrieve a single quality retention profile |
| [**getNetworkCameraQualityRetentionProfiles**](CameraApi.md#getNetworkCameraQualityRetentionProfiles) | **GET** /networks/{networkId}/camera/qualityRetentionProfiles | List the quality retention profiles for this network |
| [**getNetworkCameraSchedules**](CameraApi.md#getNetworkCameraSchedules) | **GET** /networks/{networkId}/camera/schedules | Returns a list of all camera recording schedules. |
| [**getNetworkCameraWirelessProfile**](CameraApi.md#getNetworkCameraWirelessProfile) | **GET** /networks/{networkId}/camera/wirelessProfiles/{wirelessProfileId} | Retrieve a single camera wireless profile. |
| [**getNetworkCameraWirelessProfiles**](CameraApi.md#getNetworkCameraWirelessProfiles) | **GET** /networks/{networkId}/camera/wirelessProfiles | List the camera wireless profiles for this network. |
| [**getOrganizationCameraCustomAnalyticsArtifact**](CameraApi.md#getOrganizationCameraCustomAnalyticsArtifact) | **GET** /organizations/{organizationId}/camera/customAnalytics/artifacts/{artifactId} | Get Custom Analytics Artifact |
| [**getOrganizationCameraCustomAnalyticsArtifacts**](CameraApi.md#getOrganizationCameraCustomAnalyticsArtifacts) | **GET** /organizations/{organizationId}/camera/customAnalytics/artifacts | List Custom Analytics Artifacts |
| [**getOrganizationCameraOnboardingStatuses**](CameraApi.md#getOrganizationCameraOnboardingStatuses) | **GET** /organizations/{organizationId}/camera/onboarding/statuses | Fetch onboarding status of cameras |
| [**updateDeviceCameraCustomAnalytics**](CameraApi.md#updateDeviceCameraCustomAnalytics) | **PUT** /devices/{serial}/camera/customAnalytics | Update custom analytics settings for a camera |
| [**updateDeviceCameraQualityAndRetention**](CameraApi.md#updateDeviceCameraQualityAndRetention) | **PUT** /devices/{serial}/camera/qualityAndRetention | Update quality and retention settings for the given camera |
| [**updateDeviceCameraSense**](CameraApi.md#updateDeviceCameraSense) | **PUT** /devices/{serial}/camera/sense | Update sense settings for the given camera |
| [**updateDeviceCameraVideoSettings**](CameraApi.md#updateDeviceCameraVideoSettings) | **PUT** /devices/{serial}/camera/video/settings | Update video settings for the given camera |
| [**updateDeviceCameraWirelessProfiles**](CameraApi.md#updateDeviceCameraWirelessProfiles) | **PUT** /devices/{serial}/camera/wirelessProfiles | Assign wireless profiles to the given camera |
| [**updateNetworkCameraQualityRetentionProfile**](CameraApi.md#updateNetworkCameraQualityRetentionProfile) | **PUT** /networks/{networkId}/camera/qualityRetentionProfiles/{qualityRetentionProfileId} | Update an existing quality retention profile for this network. |
| [**updateNetworkCameraWirelessProfile**](CameraApi.md#updateNetworkCameraWirelessProfile) | **PUT** /networks/{networkId}/camera/wirelessProfiles/{wirelessProfileId} | Update an existing camera wireless profile in this network. |
| [**updateOrganizationCameraOnboardingStatuses**](CameraApi.md#updateOrganizationCameraOnboardingStatuses) | **PUT** /organizations/{organizationId}/camera/onboarding/statuses | Notify that credential handoff to camera has completed |


<a id="createNetworkCameraQualityRetentionProfile"></a>
# **createNetworkCameraQualityRetentionProfile**
> Object createNetworkCameraQualityRetentionProfile(networkId, createNetworkCameraQualityRetentionProfileRequest)

Creates new quality retention profile for this network.

Creates new quality retention profile for this network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CameraApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CameraApi apiInstance = new CameraApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkCameraQualityRetentionProfileRequest createNetworkCameraQualityRetentionProfileRequest = new CreateNetworkCameraQualityRetentionProfileRequest(); // CreateNetworkCameraQualityRetentionProfileRequest | 
    try {
      Object result = apiInstance.createNetworkCameraQualityRetentionProfile(networkId, createNetworkCameraQualityRetentionProfileRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CameraApi#createNetworkCameraQualityRetentionProfile");
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
| **networkId** | **String**|  | |
| **createNetworkCameraQualityRetentionProfileRequest** | [**CreateNetworkCameraQualityRetentionProfileRequest**](CreateNetworkCameraQualityRetentionProfileRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="createNetworkCameraWirelessProfile"></a>
# **createNetworkCameraWirelessProfile**
> Object createNetworkCameraWirelessProfile(networkId, createNetworkCameraWirelessProfileRequest)

Creates a new camera wireless profile for this network.

Creates a new camera wireless profile for this network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CameraApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CameraApi apiInstance = new CameraApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkCameraWirelessProfileRequest createNetworkCameraWirelessProfileRequest = new CreateNetworkCameraWirelessProfileRequest(); // CreateNetworkCameraWirelessProfileRequest | 
    try {
      Object result = apiInstance.createNetworkCameraWirelessProfile(networkId, createNetworkCameraWirelessProfileRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CameraApi#createNetworkCameraWirelessProfile");
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
| **networkId** | **String**|  | |
| **createNetworkCameraWirelessProfileRequest** | [**CreateNetworkCameraWirelessProfileRequest**](CreateNetworkCameraWirelessProfileRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="createOrganizationCameraCustomAnalyticsArtifact"></a>
# **createOrganizationCameraCustomAnalyticsArtifact**
> Object createOrganizationCameraCustomAnalyticsArtifact(organizationId, createOrganizationCameraCustomAnalyticsArtifactRequest)

Create custom analytics artifact

Create custom analytics artifact. Returns an artifact upload URL with expiry time. Upload the artifact file with a put request to the returned upload URL before its expiry.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CameraApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CameraApi apiInstance = new CameraApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CreateOrganizationCameraCustomAnalyticsArtifactRequest createOrganizationCameraCustomAnalyticsArtifactRequest = new CreateOrganizationCameraCustomAnalyticsArtifactRequest(); // CreateOrganizationCameraCustomAnalyticsArtifactRequest | 
    try {
      Object result = apiInstance.createOrganizationCameraCustomAnalyticsArtifact(organizationId, createOrganizationCameraCustomAnalyticsArtifactRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CameraApi#createOrganizationCameraCustomAnalyticsArtifact");
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
| **organizationId** | **String**|  | |
| **createOrganizationCameraCustomAnalyticsArtifactRequest** | [**CreateOrganizationCameraCustomAnalyticsArtifactRequest**](CreateOrganizationCameraCustomAnalyticsArtifactRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="deleteNetworkCameraQualityRetentionProfile"></a>
# **deleteNetworkCameraQualityRetentionProfile**
> deleteNetworkCameraQualityRetentionProfile(networkId, qualityRetentionProfileId)

Delete an existing quality retention profile for this network.

Delete an existing quality retention profile for this network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CameraApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CameraApi apiInstance = new CameraApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String qualityRetentionProfileId = "qualityRetentionProfileId_example"; // String | 
    try {
      apiInstance.deleteNetworkCameraQualityRetentionProfile(networkId, qualityRetentionProfileId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CameraApi#deleteNetworkCameraQualityRetentionProfile");
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
| **networkId** | **String**|  | |
| **qualityRetentionProfileId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful operation |  -  |

<a id="deleteNetworkCameraWirelessProfile"></a>
# **deleteNetworkCameraWirelessProfile**
> deleteNetworkCameraWirelessProfile(networkId, wirelessProfileId)

Delete an existing camera wireless profile for this network.

Delete an existing camera wireless profile for this network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CameraApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CameraApi apiInstance = new CameraApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String wirelessProfileId = "wirelessProfileId_example"; // String | 
    try {
      apiInstance.deleteNetworkCameraWirelessProfile(networkId, wirelessProfileId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CameraApi#deleteNetworkCameraWirelessProfile");
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
| **networkId** | **String**|  | |
| **wirelessProfileId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful operation |  -  |

<a id="deleteOrganizationCameraCustomAnalyticsArtifact"></a>
# **deleteOrganizationCameraCustomAnalyticsArtifact**
> deleteOrganizationCameraCustomAnalyticsArtifact(organizationId, artifactId)

Delete Custom Analytics Artifact

Delete Custom Analytics Artifact

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CameraApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CameraApi apiInstance = new CameraApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String artifactId = "artifactId_example"; // String | 
    try {
      apiInstance.deleteOrganizationCameraCustomAnalyticsArtifact(organizationId, artifactId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CameraApi#deleteOrganizationCameraCustomAnalyticsArtifact");
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
| **organizationId** | **String**|  | |
| **artifactId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful operation |  -  |

<a id="generateDeviceCameraSnapshot"></a>
# **generateDeviceCameraSnapshot**
> Object generateDeviceCameraSnapshot(serial, generateDeviceCameraSnapshotRequest)

Generate a snapshot of what the camera sees at the specified time and return a link to that image.

Generate a snapshot of what the camera sees at the specified time and return a link to that image.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CameraApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CameraApi apiInstance = new CameraApi(defaultClient);
    String serial = "serial_example"; // String | 
    GenerateDeviceCameraSnapshotRequest generateDeviceCameraSnapshotRequest = new GenerateDeviceCameraSnapshotRequest(); // GenerateDeviceCameraSnapshotRequest | 
    try {
      Object result = apiInstance.generateDeviceCameraSnapshot(serial, generateDeviceCameraSnapshotRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CameraApi#generateDeviceCameraSnapshot");
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
| **serial** | **String**|  | |
| **generateDeviceCameraSnapshotRequest** | [**GenerateDeviceCameraSnapshotRequest**](GenerateDeviceCameraSnapshotRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Successful operation |  -  |

<a id="getDeviceCameraAnalyticsLive"></a>
# **getDeviceCameraAnalyticsLive**
> Object getDeviceCameraAnalyticsLive(serial)

Returns live state from camera of analytics zones

Returns live state from camera of analytics zones

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CameraApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CameraApi apiInstance = new CameraApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      Object result = apiInstance.getDeviceCameraAnalyticsLive(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CameraApi#getDeviceCameraAnalyticsLive");
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
| **serial** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getDeviceCameraAnalyticsOverview"></a>
# **getDeviceCameraAnalyticsOverview**
> List&lt;Object&gt; getDeviceCameraAnalyticsOverview(serial, t0, t1, timespan, objectType)

Returns an overview of aggregate analytics data for a timespan

Returns an overview of aggregate analytics data for a timespan

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CameraApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CameraApi apiInstance = new CameraApi(defaultClient);
    String serial = "serial_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 1 hour.
    String objectType = "person"; // String | [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle].
    try {
      List<Object> result = apiInstance.getDeviceCameraAnalyticsOverview(serial, t0, t1, timespan, objectType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CameraApi#getDeviceCameraAnalyticsOverview");
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
| **serial** | **String**|  | |
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 365 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 1 hour. | [optional] |
| **objectType** | **String**| [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle]. | [optional] [enum: person, vehicle] |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getDeviceCameraAnalyticsRecent"></a>
# **getDeviceCameraAnalyticsRecent**
> List&lt;Object&gt; getDeviceCameraAnalyticsRecent(serial, objectType)

Returns most recent record for analytics zones

Returns most recent record for analytics zones

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CameraApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CameraApi apiInstance = new CameraApi(defaultClient);
    String serial = "serial_example"; // String | 
    String objectType = "person"; // String | [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle].
    try {
      List<Object> result = apiInstance.getDeviceCameraAnalyticsRecent(serial, objectType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CameraApi#getDeviceCameraAnalyticsRecent");
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
| **serial** | **String**|  | |
| **objectType** | **String**| [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle]. | [optional] [enum: person, vehicle] |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getDeviceCameraAnalyticsZoneHistory"></a>
# **getDeviceCameraAnalyticsZoneHistory**
> List&lt;Object&gt; getDeviceCameraAnalyticsZoneHistory(serial, zoneId, t0, t1, timespan, resolution, objectType)

Return historical records for analytic zones

Return historical records for analytic zones

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CameraApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CameraApi apiInstance = new CameraApi(defaultClient);
    String serial = "serial_example"; // String | 
    String zoneId = "zoneId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 14 hours after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 14 hours. The default is 1 hour.
    Integer resolution = 56; // Integer | The time resolution in seconds for returned data. The valid resolutions are: 60. The default is 60.
    String objectType = "person"; // String | [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle].
    try {
      List<Object> result = apiInstance.getDeviceCameraAnalyticsZoneHistory(serial, zoneId, t0, t1, timespan, resolution, objectType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CameraApi#getDeviceCameraAnalyticsZoneHistory");
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
| **serial** | **String**|  | |
| **zoneId** | **String**|  | |
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 365 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 14 hours after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 14 hours. The default is 1 hour. | [optional] |
| **resolution** | **Integer**| The time resolution in seconds for returned data. The valid resolutions are: 60. The default is 60. | [optional] |
| **objectType** | **String**| [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle]. | [optional] [enum: person, vehicle] |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getDeviceCameraAnalyticsZones"></a>
# **getDeviceCameraAnalyticsZones**
> List&lt;Object&gt; getDeviceCameraAnalyticsZones(serial)

Returns all configured analytic zones for this camera

Returns all configured analytic zones for this camera

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CameraApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CameraApi apiInstance = new CameraApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      List<Object> result = apiInstance.getDeviceCameraAnalyticsZones(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CameraApi#getDeviceCameraAnalyticsZones");
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
| **serial** | **String**|  | |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getDeviceCameraCustomAnalytics"></a>
# **getDeviceCameraCustomAnalytics**
> Object getDeviceCameraCustomAnalytics(serial)

Return custom analytics settings for a camera

Return custom analytics settings for a camera

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CameraApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CameraApi apiInstance = new CameraApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      Object result = apiInstance.getDeviceCameraCustomAnalytics(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CameraApi#getDeviceCameraCustomAnalytics");
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
| **serial** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getDeviceCameraQualityAndRetention"></a>
# **getDeviceCameraQualityAndRetention**
> Object getDeviceCameraQualityAndRetention(serial)

Returns quality and retention settings for the given camera

Returns quality and retention settings for the given camera

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CameraApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CameraApi apiInstance = new CameraApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      Object result = apiInstance.getDeviceCameraQualityAndRetention(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CameraApi#getDeviceCameraQualityAndRetention");
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
| **serial** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getDeviceCameraSense"></a>
# **getDeviceCameraSense**
> Object getDeviceCameraSense(serial)

Returns sense settings for a given camera

Returns sense settings for a given camera

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CameraApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CameraApi apiInstance = new CameraApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      Object result = apiInstance.getDeviceCameraSense(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CameraApi#getDeviceCameraSense");
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
| **serial** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getDeviceCameraSenseObjectDetectionModels"></a>
# **getDeviceCameraSenseObjectDetectionModels**
> List&lt;Object&gt; getDeviceCameraSenseObjectDetectionModels(serial)

Returns the MV Sense object detection model list for the given camera

Returns the MV Sense object detection model list for the given camera

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CameraApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CameraApi apiInstance = new CameraApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      List<Object> result = apiInstance.getDeviceCameraSenseObjectDetectionModels(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CameraApi#getDeviceCameraSenseObjectDetectionModels");
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
| **serial** | **String**|  | |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getDeviceCameraVideoLink"></a>
# **getDeviceCameraVideoLink**
> Object getDeviceCameraVideoLink(serial, timestamp)

Returns video link to the specified camera

Returns video link to the specified camera. If a timestamp is supplied, it links to that timestamp.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CameraApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CameraApi apiInstance = new CameraApi(defaultClient);
    String serial = "serial_example"; // String | 
    OffsetDateTime timestamp = OffsetDateTime.now(); // OffsetDateTime | [optional] The video link will start at this time. The timestamp should be a string in ISO8601 format. If no timestamp is specified, we will assume current time.
    try {
      Object result = apiInstance.getDeviceCameraVideoLink(serial, timestamp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CameraApi#getDeviceCameraVideoLink");
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
| **serial** | **String**|  | |
| **timestamp** | **OffsetDateTime**| [optional] The video link will start at this time. The timestamp should be a string in ISO8601 format. If no timestamp is specified, we will assume current time. | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getDeviceCameraVideoSettings"></a>
# **getDeviceCameraVideoSettings**
> Object getDeviceCameraVideoSettings(serial)

Returns video settings for the given camera

Returns video settings for the given camera

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CameraApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CameraApi apiInstance = new CameraApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      Object result = apiInstance.getDeviceCameraVideoSettings(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CameraApi#getDeviceCameraVideoSettings");
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
| **serial** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getDeviceCameraWirelessProfiles"></a>
# **getDeviceCameraWirelessProfiles**
> Object getDeviceCameraWirelessProfiles(serial)

Returns wireless profile assigned to the given camera

Returns wireless profile assigned to the given camera

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CameraApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CameraApi apiInstance = new CameraApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      Object result = apiInstance.getDeviceCameraWirelessProfiles(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CameraApi#getDeviceCameraWirelessProfiles");
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
| **serial** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkCameraQualityRetentionProfile"></a>
# **getNetworkCameraQualityRetentionProfile**
> Object getNetworkCameraQualityRetentionProfile(networkId, qualityRetentionProfileId)

Retrieve a single quality retention profile

Retrieve a single quality retention profile

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CameraApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CameraApi apiInstance = new CameraApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String qualityRetentionProfileId = "qualityRetentionProfileId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkCameraQualityRetentionProfile(networkId, qualityRetentionProfileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CameraApi#getNetworkCameraQualityRetentionProfile");
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
| **networkId** | **String**|  | |
| **qualityRetentionProfileId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkCameraQualityRetentionProfiles"></a>
# **getNetworkCameraQualityRetentionProfiles**
> List&lt;Object&gt; getNetworkCameraQualityRetentionProfiles(networkId)

List the quality retention profiles for this network

List the quality retention profiles for this network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CameraApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CameraApi apiInstance = new CameraApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkCameraQualityRetentionProfiles(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CameraApi#getNetworkCameraQualityRetentionProfiles");
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
| **networkId** | **String**|  | |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkCameraSchedules"></a>
# **getNetworkCameraSchedules**
> List&lt;Object&gt; getNetworkCameraSchedules(networkId)

Returns a list of all camera recording schedules.

Returns a list of all camera recording schedules.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CameraApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CameraApi apiInstance = new CameraApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkCameraSchedules(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CameraApi#getNetworkCameraSchedules");
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
| **networkId** | **String**|  | |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkCameraWirelessProfile"></a>
# **getNetworkCameraWirelessProfile**
> Object getNetworkCameraWirelessProfile(networkId, wirelessProfileId)

Retrieve a single camera wireless profile.

Retrieve a single camera wireless profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CameraApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CameraApi apiInstance = new CameraApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String wirelessProfileId = "wirelessProfileId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkCameraWirelessProfile(networkId, wirelessProfileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CameraApi#getNetworkCameraWirelessProfile");
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
| **networkId** | **String**|  | |
| **wirelessProfileId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkCameraWirelessProfiles"></a>
# **getNetworkCameraWirelessProfiles**
> List&lt;Object&gt; getNetworkCameraWirelessProfiles(networkId)

List the camera wireless profiles for this network.

List the camera wireless profiles for this network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CameraApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CameraApi apiInstance = new CameraApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkCameraWirelessProfiles(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CameraApi#getNetworkCameraWirelessProfiles");
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
| **networkId** | **String**|  | |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationCameraCustomAnalyticsArtifact"></a>
# **getOrganizationCameraCustomAnalyticsArtifact**
> Object getOrganizationCameraCustomAnalyticsArtifact(organizationId, artifactId)

Get Custom Analytics Artifact

Get Custom Analytics Artifact

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CameraApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CameraApi apiInstance = new CameraApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String artifactId = "artifactId_example"; // String | 
    try {
      Object result = apiInstance.getOrganizationCameraCustomAnalyticsArtifact(organizationId, artifactId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CameraApi#getOrganizationCameraCustomAnalyticsArtifact");
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
| **organizationId** | **String**|  | |
| **artifactId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationCameraCustomAnalyticsArtifacts"></a>
# **getOrganizationCameraCustomAnalyticsArtifacts**
> List&lt;Object&gt; getOrganizationCameraCustomAnalyticsArtifacts(organizationId)

List Custom Analytics Artifacts

List Custom Analytics Artifacts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CameraApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CameraApi apiInstance = new CameraApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      List<Object> result = apiInstance.getOrganizationCameraCustomAnalyticsArtifacts(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CameraApi#getOrganizationCameraCustomAnalyticsArtifacts");
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
| **organizationId** | **String**|  | |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationCameraOnboardingStatuses"></a>
# **getOrganizationCameraOnboardingStatuses**
> List&lt;Object&gt; getOrganizationCameraOnboardingStatuses(organizationId, serials, networkIds)

Fetch onboarding status of cameras

Fetch onboarding status of cameras

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CameraApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CameraApi apiInstance = new CameraApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    List<String> serials = Arrays.asList(); // List<String> | A list of serial numbers. The returned cameras will be filtered to only include these serials.
    List<String> networkIds = Arrays.asList(); // List<String> | A list of network IDs. The returned cameras will be filtered to only include these networks.
    try {
      List<Object> result = apiInstance.getOrganizationCameraOnboardingStatuses(organizationId, serials, networkIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CameraApi#getOrganizationCameraOnboardingStatuses");
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
| **organizationId** | **String**|  | |
| **serials** | [**List&lt;String&gt;**](String.md)| A list of serial numbers. The returned cameras will be filtered to only include these serials. | [optional] |
| **networkIds** | [**List&lt;String&gt;**](String.md)| A list of network IDs. The returned cameras will be filtered to only include these networks. | [optional] |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateDeviceCameraCustomAnalytics"></a>
# **updateDeviceCameraCustomAnalytics**
> Object updateDeviceCameraCustomAnalytics(serial, updateDeviceCameraCustomAnalyticsRequest)

Update custom analytics settings for a camera

Update custom analytics settings for a camera

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CameraApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CameraApi apiInstance = new CameraApi(defaultClient);
    String serial = "serial_example"; // String | 
    UpdateDeviceCameraCustomAnalyticsRequest updateDeviceCameraCustomAnalyticsRequest = new UpdateDeviceCameraCustomAnalyticsRequest(); // UpdateDeviceCameraCustomAnalyticsRequest | 
    try {
      Object result = apiInstance.updateDeviceCameraCustomAnalytics(serial, updateDeviceCameraCustomAnalyticsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CameraApi#updateDeviceCameraCustomAnalytics");
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
| **serial** | **String**|  | |
| **updateDeviceCameraCustomAnalyticsRequest** | [**UpdateDeviceCameraCustomAnalyticsRequest**](UpdateDeviceCameraCustomAnalyticsRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateDeviceCameraQualityAndRetention"></a>
# **updateDeviceCameraQualityAndRetention**
> Object updateDeviceCameraQualityAndRetention(serial, updateDeviceCameraQualityAndRetentionRequest)

Update quality and retention settings for the given camera

Update quality and retention settings for the given camera

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CameraApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CameraApi apiInstance = new CameraApi(defaultClient);
    String serial = "serial_example"; // String | 
    UpdateDeviceCameraQualityAndRetentionRequest updateDeviceCameraQualityAndRetentionRequest = new UpdateDeviceCameraQualityAndRetentionRequest(); // UpdateDeviceCameraQualityAndRetentionRequest | 
    try {
      Object result = apiInstance.updateDeviceCameraQualityAndRetention(serial, updateDeviceCameraQualityAndRetentionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CameraApi#updateDeviceCameraQualityAndRetention");
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
| **serial** | **String**|  | |
| **updateDeviceCameraQualityAndRetentionRequest** | [**UpdateDeviceCameraQualityAndRetentionRequest**](UpdateDeviceCameraQualityAndRetentionRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateDeviceCameraSense"></a>
# **updateDeviceCameraSense**
> Object updateDeviceCameraSense(serial, updateDeviceCameraSenseRequest)

Update sense settings for the given camera

Update sense settings for the given camera

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CameraApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CameraApi apiInstance = new CameraApi(defaultClient);
    String serial = "serial_example"; // String | 
    UpdateDeviceCameraSenseRequest updateDeviceCameraSenseRequest = new UpdateDeviceCameraSenseRequest(); // UpdateDeviceCameraSenseRequest | 
    try {
      Object result = apiInstance.updateDeviceCameraSense(serial, updateDeviceCameraSenseRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CameraApi#updateDeviceCameraSense");
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
| **serial** | **String**|  | |
| **updateDeviceCameraSenseRequest** | [**UpdateDeviceCameraSenseRequest**](UpdateDeviceCameraSenseRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateDeviceCameraVideoSettings"></a>
# **updateDeviceCameraVideoSettings**
> Object updateDeviceCameraVideoSettings(serial, updateDeviceCameraVideoSettingsRequest)

Update video settings for the given camera

Update video settings for the given camera

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CameraApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CameraApi apiInstance = new CameraApi(defaultClient);
    String serial = "serial_example"; // String | 
    UpdateDeviceCameraVideoSettingsRequest updateDeviceCameraVideoSettingsRequest = new UpdateDeviceCameraVideoSettingsRequest(); // UpdateDeviceCameraVideoSettingsRequest | 
    try {
      Object result = apiInstance.updateDeviceCameraVideoSettings(serial, updateDeviceCameraVideoSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CameraApi#updateDeviceCameraVideoSettings");
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
| **serial** | **String**|  | |
| **updateDeviceCameraVideoSettingsRequest** | [**UpdateDeviceCameraVideoSettingsRequest**](UpdateDeviceCameraVideoSettingsRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateDeviceCameraWirelessProfiles"></a>
# **updateDeviceCameraWirelessProfiles**
> Object updateDeviceCameraWirelessProfiles(serial, updateDeviceCameraWirelessProfilesRequest)

Assign wireless profiles to the given camera

Assign wireless profiles to the given camera. Incremental updates are not supported, all profile assignment need to be supplied at once.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CameraApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CameraApi apiInstance = new CameraApi(defaultClient);
    String serial = "serial_example"; // String | 
    UpdateDeviceCameraWirelessProfilesRequest updateDeviceCameraWirelessProfilesRequest = new UpdateDeviceCameraWirelessProfilesRequest(); // UpdateDeviceCameraWirelessProfilesRequest | 
    try {
      Object result = apiInstance.updateDeviceCameraWirelessProfiles(serial, updateDeviceCameraWirelessProfilesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CameraApi#updateDeviceCameraWirelessProfiles");
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
| **serial** | **String**|  | |
| **updateDeviceCameraWirelessProfilesRequest** | [**UpdateDeviceCameraWirelessProfilesRequest**](UpdateDeviceCameraWirelessProfilesRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkCameraQualityRetentionProfile"></a>
# **updateNetworkCameraQualityRetentionProfile**
> Object updateNetworkCameraQualityRetentionProfile(networkId, qualityRetentionProfileId, updateNetworkCameraQualityRetentionProfileRequest)

Update an existing quality retention profile for this network.

Update an existing quality retention profile for this network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CameraApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CameraApi apiInstance = new CameraApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String qualityRetentionProfileId = "qualityRetentionProfileId_example"; // String | 
    UpdateNetworkCameraQualityRetentionProfileRequest updateNetworkCameraQualityRetentionProfileRequest = new UpdateNetworkCameraQualityRetentionProfileRequest(); // UpdateNetworkCameraQualityRetentionProfileRequest | 
    try {
      Object result = apiInstance.updateNetworkCameraQualityRetentionProfile(networkId, qualityRetentionProfileId, updateNetworkCameraQualityRetentionProfileRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CameraApi#updateNetworkCameraQualityRetentionProfile");
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
| **networkId** | **String**|  | |
| **qualityRetentionProfileId** | **String**|  | |
| **updateNetworkCameraQualityRetentionProfileRequest** | [**UpdateNetworkCameraQualityRetentionProfileRequest**](UpdateNetworkCameraQualityRetentionProfileRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkCameraWirelessProfile"></a>
# **updateNetworkCameraWirelessProfile**
> Object updateNetworkCameraWirelessProfile(networkId, wirelessProfileId, updateNetworkCameraWirelessProfileRequest)

Update an existing camera wireless profile in this network.

Update an existing camera wireless profile in this network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CameraApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CameraApi apiInstance = new CameraApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String wirelessProfileId = "wirelessProfileId_example"; // String | 
    UpdateNetworkCameraWirelessProfileRequest updateNetworkCameraWirelessProfileRequest = new UpdateNetworkCameraWirelessProfileRequest(); // UpdateNetworkCameraWirelessProfileRequest | 
    try {
      Object result = apiInstance.updateNetworkCameraWirelessProfile(networkId, wirelessProfileId, updateNetworkCameraWirelessProfileRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CameraApi#updateNetworkCameraWirelessProfile");
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
| **networkId** | **String**|  | |
| **wirelessProfileId** | **String**|  | |
| **updateNetworkCameraWirelessProfileRequest** | [**UpdateNetworkCameraWirelessProfileRequest**](UpdateNetworkCameraWirelessProfileRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateOrganizationCameraOnboardingStatuses"></a>
# **updateOrganizationCameraOnboardingStatuses**
> Object updateOrganizationCameraOnboardingStatuses(organizationId, updateOrganizationCameraOnboardingStatusesRequest)

Notify that credential handoff to camera has completed

Notify that credential handoff to camera has completed

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CameraApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CameraApi apiInstance = new CameraApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    UpdateOrganizationCameraOnboardingStatusesRequest updateOrganizationCameraOnboardingStatusesRequest = new UpdateOrganizationCameraOnboardingStatusesRequest(); // UpdateOrganizationCameraOnboardingStatusesRequest | 
    try {
      Object result = apiInstance.updateOrganizationCameraOnboardingStatuses(organizationId, updateOrganizationCameraOnboardingStatusesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CameraApi#updateOrganizationCameraOnboardingStatuses");
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
| **organizationId** | **String**|  | |
| **updateOrganizationCameraOnboardingStatusesRequest** | [**UpdateOrganizationCameraOnboardingStatusesRequest**](UpdateOrganizationCameraOnboardingStatusesRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

