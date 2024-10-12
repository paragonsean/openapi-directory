# WirelessProfilesApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkCameraWirelessProfile_1**](WirelessProfilesApi.md#createNetworkCameraWirelessProfile_1) | **POST** /networks/{networkId}/camera/wirelessProfiles | Creates a new camera wireless profile for this network. |
| [**deleteNetworkCameraWirelessProfile_1**](WirelessProfilesApi.md#deleteNetworkCameraWirelessProfile_1) | **DELETE** /networks/{networkId}/camera/wirelessProfiles/{wirelessProfileId} | Delete an existing camera wireless profile for this network. |
| [**getDeviceCameraWirelessProfiles_1**](WirelessProfilesApi.md#getDeviceCameraWirelessProfiles_1) | **GET** /devices/{serial}/camera/wirelessProfiles | Returns wireless profile assigned to the given camera |
| [**getNetworkCameraWirelessProfile_1**](WirelessProfilesApi.md#getNetworkCameraWirelessProfile_1) | **GET** /networks/{networkId}/camera/wirelessProfiles/{wirelessProfileId} | Retrieve a single camera wireless profile. |
| [**getNetworkCameraWirelessProfiles_1**](WirelessProfilesApi.md#getNetworkCameraWirelessProfiles_1) | **GET** /networks/{networkId}/camera/wirelessProfiles | List the camera wireless profiles for this network. |
| [**updateDeviceCameraWirelessProfiles_1**](WirelessProfilesApi.md#updateDeviceCameraWirelessProfiles_1) | **PUT** /devices/{serial}/camera/wirelessProfiles | Assign wireless profiles to the given camera |
| [**updateNetworkCameraWirelessProfile_1**](WirelessProfilesApi.md#updateNetworkCameraWirelessProfile_1) | **PUT** /networks/{networkId}/camera/wirelessProfiles/{wirelessProfileId} | Update an existing camera wireless profile in this network. |


<a id="createNetworkCameraWirelessProfile_1"></a>
# **createNetworkCameraWirelessProfile_1**
> Object createNetworkCameraWirelessProfile_1(networkId, createNetworkCameraWirelessProfileRequest)

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
import org.openapitools.client.api.WirelessProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessProfilesApi apiInstance = new WirelessProfilesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkCameraWirelessProfileRequest createNetworkCameraWirelessProfileRequest = new CreateNetworkCameraWirelessProfileRequest(); // CreateNetworkCameraWirelessProfileRequest | 
    try {
      Object result = apiInstance.createNetworkCameraWirelessProfile_1(networkId, createNetworkCameraWirelessProfileRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessProfilesApi#createNetworkCameraWirelessProfile_1");
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

<a id="deleteNetworkCameraWirelessProfile_1"></a>
# **deleteNetworkCameraWirelessProfile_1**
> deleteNetworkCameraWirelessProfile_1(networkId, wirelessProfileId)

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
import org.openapitools.client.api.WirelessProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessProfilesApi apiInstance = new WirelessProfilesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String wirelessProfileId = "wirelessProfileId_example"; // String | 
    try {
      apiInstance.deleteNetworkCameraWirelessProfile_1(networkId, wirelessProfileId);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessProfilesApi#deleteNetworkCameraWirelessProfile_1");
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

<a id="getDeviceCameraWirelessProfiles_1"></a>
# **getDeviceCameraWirelessProfiles_1**
> Object getDeviceCameraWirelessProfiles_1(serial)

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
import org.openapitools.client.api.WirelessProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessProfilesApi apiInstance = new WirelessProfilesApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      Object result = apiInstance.getDeviceCameraWirelessProfiles_1(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessProfilesApi#getDeviceCameraWirelessProfiles_1");
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

<a id="getNetworkCameraWirelessProfile_1"></a>
# **getNetworkCameraWirelessProfile_1**
> Object getNetworkCameraWirelessProfile_1(networkId, wirelessProfileId)

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
import org.openapitools.client.api.WirelessProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessProfilesApi apiInstance = new WirelessProfilesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String wirelessProfileId = "wirelessProfileId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkCameraWirelessProfile_1(networkId, wirelessProfileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessProfilesApi#getNetworkCameraWirelessProfile_1");
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

<a id="getNetworkCameraWirelessProfiles_1"></a>
# **getNetworkCameraWirelessProfiles_1**
> List&lt;Object&gt; getNetworkCameraWirelessProfiles_1(networkId)

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
import org.openapitools.client.api.WirelessProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessProfilesApi apiInstance = new WirelessProfilesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkCameraWirelessProfiles_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessProfilesApi#getNetworkCameraWirelessProfiles_1");
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

<a id="updateDeviceCameraWirelessProfiles_1"></a>
# **updateDeviceCameraWirelessProfiles_1**
> Object updateDeviceCameraWirelessProfiles_1(serial, updateDeviceCameraWirelessProfilesRequest)

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
import org.openapitools.client.api.WirelessProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessProfilesApi apiInstance = new WirelessProfilesApi(defaultClient);
    String serial = "serial_example"; // String | 
    UpdateDeviceCameraWirelessProfilesRequest updateDeviceCameraWirelessProfilesRequest = new UpdateDeviceCameraWirelessProfilesRequest(); // UpdateDeviceCameraWirelessProfilesRequest | 
    try {
      Object result = apiInstance.updateDeviceCameraWirelessProfiles_1(serial, updateDeviceCameraWirelessProfilesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessProfilesApi#updateDeviceCameraWirelessProfiles_1");
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

<a id="updateNetworkCameraWirelessProfile_1"></a>
# **updateNetworkCameraWirelessProfile_1**
> Object updateNetworkCameraWirelessProfile_1(networkId, wirelessProfileId, updateNetworkCameraWirelessProfileRequest)

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
import org.openapitools.client.api.WirelessProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessProfilesApi apiInstance = new WirelessProfilesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String wirelessProfileId = "wirelessProfileId_example"; // String | 
    UpdateNetworkCameraWirelessProfileRequest updateNetworkCameraWirelessProfileRequest = new UpdateNetworkCameraWirelessProfileRequest(); // UpdateNetworkCameraWirelessProfileRequest | 
    try {
      Object result = apiInstance.updateNetworkCameraWirelessProfile_1(networkId, wirelessProfileId, updateNetworkCameraWirelessProfileRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessProfilesApi#updateNetworkCameraWirelessProfile_1");
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

