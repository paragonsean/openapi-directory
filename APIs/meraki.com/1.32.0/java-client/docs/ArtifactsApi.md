# ArtifactsApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createOrganizationCameraCustomAnalyticsArtifact_2**](ArtifactsApi.md#createOrganizationCameraCustomAnalyticsArtifact_2) | **POST** /organizations/{organizationId}/camera/customAnalytics/artifacts | Create custom analytics artifact |
| [**deleteOrganizationCameraCustomAnalyticsArtifact_2**](ArtifactsApi.md#deleteOrganizationCameraCustomAnalyticsArtifact_2) | **DELETE** /organizations/{organizationId}/camera/customAnalytics/artifacts/{artifactId} | Delete Custom Analytics Artifact |
| [**getOrganizationCameraCustomAnalyticsArtifact_2**](ArtifactsApi.md#getOrganizationCameraCustomAnalyticsArtifact_2) | **GET** /organizations/{organizationId}/camera/customAnalytics/artifacts/{artifactId} | Get Custom Analytics Artifact |
| [**getOrganizationCameraCustomAnalyticsArtifacts_2**](ArtifactsApi.md#getOrganizationCameraCustomAnalyticsArtifacts_2) | **GET** /organizations/{organizationId}/camera/customAnalytics/artifacts | List Custom Analytics Artifacts |


<a id="createOrganizationCameraCustomAnalyticsArtifact_2"></a>
# **createOrganizationCameraCustomAnalyticsArtifact_2**
> Object createOrganizationCameraCustomAnalyticsArtifact_2(organizationId, createOrganizationCameraCustomAnalyticsArtifactRequest)

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
import org.openapitools.client.api.ArtifactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ArtifactsApi apiInstance = new ArtifactsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CreateOrganizationCameraCustomAnalyticsArtifactRequest createOrganizationCameraCustomAnalyticsArtifactRequest = new CreateOrganizationCameraCustomAnalyticsArtifactRequest(); // CreateOrganizationCameraCustomAnalyticsArtifactRequest | 
    try {
      Object result = apiInstance.createOrganizationCameraCustomAnalyticsArtifact_2(organizationId, createOrganizationCameraCustomAnalyticsArtifactRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactsApi#createOrganizationCameraCustomAnalyticsArtifact_2");
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

<a id="deleteOrganizationCameraCustomAnalyticsArtifact_2"></a>
# **deleteOrganizationCameraCustomAnalyticsArtifact_2**
> deleteOrganizationCameraCustomAnalyticsArtifact_2(organizationId, artifactId)

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
import org.openapitools.client.api.ArtifactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ArtifactsApi apiInstance = new ArtifactsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String artifactId = "artifactId_example"; // String | 
    try {
      apiInstance.deleteOrganizationCameraCustomAnalyticsArtifact_2(organizationId, artifactId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactsApi#deleteOrganizationCameraCustomAnalyticsArtifact_2");
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

<a id="getOrganizationCameraCustomAnalyticsArtifact_2"></a>
# **getOrganizationCameraCustomAnalyticsArtifact_2**
> Object getOrganizationCameraCustomAnalyticsArtifact_2(organizationId, artifactId)

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
import org.openapitools.client.api.ArtifactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ArtifactsApi apiInstance = new ArtifactsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String artifactId = "artifactId_example"; // String | 
    try {
      Object result = apiInstance.getOrganizationCameraCustomAnalyticsArtifact_2(organizationId, artifactId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactsApi#getOrganizationCameraCustomAnalyticsArtifact_2");
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

<a id="getOrganizationCameraCustomAnalyticsArtifacts_2"></a>
# **getOrganizationCameraCustomAnalyticsArtifacts_2**
> List&lt;Object&gt; getOrganizationCameraCustomAnalyticsArtifacts_2(organizationId)

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
import org.openapitools.client.api.ArtifactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ArtifactsApi apiInstance = new ArtifactsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      List<Object> result = apiInstance.getOrganizationCameraCustomAnalyticsArtifacts_2(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactsApi#getOrganizationCameraCustomAnalyticsArtifacts_2");
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

