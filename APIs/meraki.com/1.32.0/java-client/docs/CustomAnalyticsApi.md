# CustomAnalyticsApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createOrganizationCameraCustomAnalyticsArtifact_1**](CustomAnalyticsApi.md#createOrganizationCameraCustomAnalyticsArtifact_1) | **POST** /organizations/{organizationId}/camera/customAnalytics/artifacts | Create custom analytics artifact |
| [**deleteOrganizationCameraCustomAnalyticsArtifact_1**](CustomAnalyticsApi.md#deleteOrganizationCameraCustomAnalyticsArtifact_1) | **DELETE** /organizations/{organizationId}/camera/customAnalytics/artifacts/{artifactId} | Delete Custom Analytics Artifact |
| [**getDeviceCameraCustomAnalytics_1**](CustomAnalyticsApi.md#getDeviceCameraCustomAnalytics_1) | **GET** /devices/{serial}/camera/customAnalytics | Return custom analytics settings for a camera |
| [**getOrganizationCameraCustomAnalyticsArtifact_1**](CustomAnalyticsApi.md#getOrganizationCameraCustomAnalyticsArtifact_1) | **GET** /organizations/{organizationId}/camera/customAnalytics/artifacts/{artifactId} | Get Custom Analytics Artifact |
| [**getOrganizationCameraCustomAnalyticsArtifacts_1**](CustomAnalyticsApi.md#getOrganizationCameraCustomAnalyticsArtifacts_1) | **GET** /organizations/{organizationId}/camera/customAnalytics/artifacts | List Custom Analytics Artifacts |
| [**updateDeviceCameraCustomAnalytics_1**](CustomAnalyticsApi.md#updateDeviceCameraCustomAnalytics_1) | **PUT** /devices/{serial}/camera/customAnalytics | Update custom analytics settings for a camera |


<a id="createOrganizationCameraCustomAnalyticsArtifact_1"></a>
# **createOrganizationCameraCustomAnalyticsArtifact_1**
> Object createOrganizationCameraCustomAnalyticsArtifact_1(organizationId, createOrganizationCameraCustomAnalyticsArtifactRequest)

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
import org.openapitools.client.api.CustomAnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CustomAnalyticsApi apiInstance = new CustomAnalyticsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CreateOrganizationCameraCustomAnalyticsArtifactRequest createOrganizationCameraCustomAnalyticsArtifactRequest = new CreateOrganizationCameraCustomAnalyticsArtifactRequest(); // CreateOrganizationCameraCustomAnalyticsArtifactRequest | 
    try {
      Object result = apiInstance.createOrganizationCameraCustomAnalyticsArtifact_1(organizationId, createOrganizationCameraCustomAnalyticsArtifactRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomAnalyticsApi#createOrganizationCameraCustomAnalyticsArtifact_1");
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

<a id="deleteOrganizationCameraCustomAnalyticsArtifact_1"></a>
# **deleteOrganizationCameraCustomAnalyticsArtifact_1**
> deleteOrganizationCameraCustomAnalyticsArtifact_1(organizationId, artifactId)

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
import org.openapitools.client.api.CustomAnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CustomAnalyticsApi apiInstance = new CustomAnalyticsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String artifactId = "artifactId_example"; // String | 
    try {
      apiInstance.deleteOrganizationCameraCustomAnalyticsArtifact_1(organizationId, artifactId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomAnalyticsApi#deleteOrganizationCameraCustomAnalyticsArtifact_1");
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

<a id="getDeviceCameraCustomAnalytics_1"></a>
# **getDeviceCameraCustomAnalytics_1**
> Object getDeviceCameraCustomAnalytics_1(serial)

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
import org.openapitools.client.api.CustomAnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CustomAnalyticsApi apiInstance = new CustomAnalyticsApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      Object result = apiInstance.getDeviceCameraCustomAnalytics_1(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomAnalyticsApi#getDeviceCameraCustomAnalytics_1");
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

<a id="getOrganizationCameraCustomAnalyticsArtifact_1"></a>
# **getOrganizationCameraCustomAnalyticsArtifact_1**
> Object getOrganizationCameraCustomAnalyticsArtifact_1(organizationId, artifactId)

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
import org.openapitools.client.api.CustomAnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CustomAnalyticsApi apiInstance = new CustomAnalyticsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String artifactId = "artifactId_example"; // String | 
    try {
      Object result = apiInstance.getOrganizationCameraCustomAnalyticsArtifact_1(organizationId, artifactId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomAnalyticsApi#getOrganizationCameraCustomAnalyticsArtifact_1");
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

<a id="getOrganizationCameraCustomAnalyticsArtifacts_1"></a>
# **getOrganizationCameraCustomAnalyticsArtifacts_1**
> List&lt;Object&gt; getOrganizationCameraCustomAnalyticsArtifacts_1(organizationId)

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
import org.openapitools.client.api.CustomAnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CustomAnalyticsApi apiInstance = new CustomAnalyticsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      List<Object> result = apiInstance.getOrganizationCameraCustomAnalyticsArtifacts_1(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomAnalyticsApi#getOrganizationCameraCustomAnalyticsArtifacts_1");
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

<a id="updateDeviceCameraCustomAnalytics_1"></a>
# **updateDeviceCameraCustomAnalytics_1**
> Object updateDeviceCameraCustomAnalytics_1(serial, updateDeviceCameraCustomAnalyticsRequest)

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
import org.openapitools.client.api.CustomAnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CustomAnalyticsApi apiInstance = new CustomAnalyticsApi(defaultClient);
    String serial = "serial_example"; // String | 
    UpdateDeviceCameraCustomAnalyticsRequest updateDeviceCameraCustomAnalyticsRequest = new UpdateDeviceCameraCustomAnalyticsRequest(); // UpdateDeviceCameraCustomAnalyticsRequest | 
    try {
      Object result = apiInstance.updateDeviceCameraCustomAnalytics_1(serial, updateDeviceCameraCustomAnalyticsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomAnalyticsApi#updateDeviceCameraCustomAnalytics_1");
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

