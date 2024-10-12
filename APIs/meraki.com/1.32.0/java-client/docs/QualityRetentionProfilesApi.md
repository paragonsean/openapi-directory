# QualityRetentionProfilesApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkCameraQualityRetentionProfile_1**](QualityRetentionProfilesApi.md#createNetworkCameraQualityRetentionProfile_1) | **POST** /networks/{networkId}/camera/qualityRetentionProfiles | Creates new quality retention profile for this network. |
| [**deleteNetworkCameraQualityRetentionProfile_1**](QualityRetentionProfilesApi.md#deleteNetworkCameraQualityRetentionProfile_1) | **DELETE** /networks/{networkId}/camera/qualityRetentionProfiles/{qualityRetentionProfileId} | Delete an existing quality retention profile for this network. |
| [**getNetworkCameraQualityRetentionProfile_1**](QualityRetentionProfilesApi.md#getNetworkCameraQualityRetentionProfile_1) | **GET** /networks/{networkId}/camera/qualityRetentionProfiles/{qualityRetentionProfileId} | Retrieve a single quality retention profile |
| [**getNetworkCameraQualityRetentionProfiles_1**](QualityRetentionProfilesApi.md#getNetworkCameraQualityRetentionProfiles_1) | **GET** /networks/{networkId}/camera/qualityRetentionProfiles | List the quality retention profiles for this network |
| [**updateNetworkCameraQualityRetentionProfile_1**](QualityRetentionProfilesApi.md#updateNetworkCameraQualityRetentionProfile_1) | **PUT** /networks/{networkId}/camera/qualityRetentionProfiles/{qualityRetentionProfileId} | Update an existing quality retention profile for this network. |


<a id="createNetworkCameraQualityRetentionProfile_1"></a>
# **createNetworkCameraQualityRetentionProfile_1**
> Object createNetworkCameraQualityRetentionProfile_1(networkId, createNetworkCameraQualityRetentionProfileRequest)

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
import org.openapitools.client.api.QualityRetentionProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    QualityRetentionProfilesApi apiInstance = new QualityRetentionProfilesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkCameraQualityRetentionProfileRequest createNetworkCameraQualityRetentionProfileRequest = new CreateNetworkCameraQualityRetentionProfileRequest(); // CreateNetworkCameraQualityRetentionProfileRequest | 
    try {
      Object result = apiInstance.createNetworkCameraQualityRetentionProfile_1(networkId, createNetworkCameraQualityRetentionProfileRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QualityRetentionProfilesApi#createNetworkCameraQualityRetentionProfile_1");
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

<a id="deleteNetworkCameraQualityRetentionProfile_1"></a>
# **deleteNetworkCameraQualityRetentionProfile_1**
> deleteNetworkCameraQualityRetentionProfile_1(networkId, qualityRetentionProfileId)

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
import org.openapitools.client.api.QualityRetentionProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    QualityRetentionProfilesApi apiInstance = new QualityRetentionProfilesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String qualityRetentionProfileId = "qualityRetentionProfileId_example"; // String | 
    try {
      apiInstance.deleteNetworkCameraQualityRetentionProfile_1(networkId, qualityRetentionProfileId);
    } catch (ApiException e) {
      System.err.println("Exception when calling QualityRetentionProfilesApi#deleteNetworkCameraQualityRetentionProfile_1");
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

<a id="getNetworkCameraQualityRetentionProfile_1"></a>
# **getNetworkCameraQualityRetentionProfile_1**
> Object getNetworkCameraQualityRetentionProfile_1(networkId, qualityRetentionProfileId)

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
import org.openapitools.client.api.QualityRetentionProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    QualityRetentionProfilesApi apiInstance = new QualityRetentionProfilesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String qualityRetentionProfileId = "qualityRetentionProfileId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkCameraQualityRetentionProfile_1(networkId, qualityRetentionProfileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QualityRetentionProfilesApi#getNetworkCameraQualityRetentionProfile_1");
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

<a id="getNetworkCameraQualityRetentionProfiles_1"></a>
# **getNetworkCameraQualityRetentionProfiles_1**
> List&lt;Object&gt; getNetworkCameraQualityRetentionProfiles_1(networkId)

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
import org.openapitools.client.api.QualityRetentionProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    QualityRetentionProfilesApi apiInstance = new QualityRetentionProfilesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkCameraQualityRetentionProfiles_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QualityRetentionProfilesApi#getNetworkCameraQualityRetentionProfiles_1");
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

<a id="updateNetworkCameraQualityRetentionProfile_1"></a>
# **updateNetworkCameraQualityRetentionProfile_1**
> Object updateNetworkCameraQualityRetentionProfile_1(networkId, qualityRetentionProfileId, updateNetworkCameraQualityRetentionProfileRequest)

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
import org.openapitools.client.api.QualityRetentionProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    QualityRetentionProfilesApi apiInstance = new QualityRetentionProfilesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String qualityRetentionProfileId = "qualityRetentionProfileId_example"; // String | 
    UpdateNetworkCameraQualityRetentionProfileRequest updateNetworkCameraQualityRetentionProfileRequest = new UpdateNetworkCameraQualityRetentionProfileRequest(); // UpdateNetworkCameraQualityRetentionProfileRequest | 
    try {
      Object result = apiInstance.updateNetworkCameraQualityRetentionProfile_1(networkId, qualityRetentionProfileId, updateNetworkCameraQualityRetentionProfileRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QualityRetentionProfilesApi#updateNetworkCameraQualityRetentionProfile_1");
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

