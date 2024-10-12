# IntrusionSettingsApi

All URIs are relative to *https://api.meraki.com/api/v0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkSecurityIntrusionSettings**](IntrusionSettingsApi.md#getNetworkSecurityIntrusionSettings) | **GET** /networks/{networkId}/security/intrusionSettings | Returns all supported intrusion settings for an MX network |
| [**getOrganizationSecurityIntrusionSettings**](IntrusionSettingsApi.md#getOrganizationSecurityIntrusionSettings) | **GET** /organizations/{organizationId}/security/intrusionSettings | Returns all supported intrusion settings for an organization |
| [**updateNetworkSecurityIntrusionSettings**](IntrusionSettingsApi.md#updateNetworkSecurityIntrusionSettings) | **PUT** /networks/{networkId}/security/intrusionSettings | Set the supported intrusion settings for an MX network |
| [**updateOrganizationSecurityIntrusionSettings**](IntrusionSettingsApi.md#updateOrganizationSecurityIntrusionSettings) | **PUT** /organizations/{organizationId}/security/intrusionSettings | Sets supported intrusion settings for an organization |


<a id="getNetworkSecurityIntrusionSettings"></a>
# **getNetworkSecurityIntrusionSettings**
> Object getNetworkSecurityIntrusionSettings(networkId)

Returns all supported intrusion settings for an MX network

Returns all supported intrusion settings for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntrusionSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    IntrusionSettingsApi apiInstance = new IntrusionSettingsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSecurityIntrusionSettings(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntrusionSettingsApi#getNetworkSecurityIntrusionSettings");
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

<a id="getOrganizationSecurityIntrusionSettings"></a>
# **getOrganizationSecurityIntrusionSettings**
> Object getOrganizationSecurityIntrusionSettings(organizationId)

Returns all supported intrusion settings for an organization

Returns all supported intrusion settings for an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntrusionSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    IntrusionSettingsApi apiInstance = new IntrusionSettingsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      Object result = apiInstance.getOrganizationSecurityIntrusionSettings(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntrusionSettingsApi#getOrganizationSecurityIntrusionSettings");
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

<a id="updateNetworkSecurityIntrusionSettings"></a>
# **updateNetworkSecurityIntrusionSettings**
> Object updateNetworkSecurityIntrusionSettings(networkId, updateNetworkSecurityIntrusionSettingsRequest)

Set the supported intrusion settings for an MX network

Set the supported intrusion settings for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntrusionSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    IntrusionSettingsApi apiInstance = new IntrusionSettingsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkSecurityIntrusionSettingsRequest updateNetworkSecurityIntrusionSettingsRequest = new UpdateNetworkSecurityIntrusionSettingsRequest(); // UpdateNetworkSecurityIntrusionSettingsRequest | 
    try {
      Object result = apiInstance.updateNetworkSecurityIntrusionSettings(networkId, updateNetworkSecurityIntrusionSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntrusionSettingsApi#updateNetworkSecurityIntrusionSettings");
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
| **updateNetworkSecurityIntrusionSettingsRequest** | [**UpdateNetworkSecurityIntrusionSettingsRequest**](UpdateNetworkSecurityIntrusionSettingsRequest.md)|  | [optional] |

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

<a id="updateOrganizationSecurityIntrusionSettings"></a>
# **updateOrganizationSecurityIntrusionSettings**
> Object updateOrganizationSecurityIntrusionSettings(organizationId, updateOrganizationSecurityIntrusionSettingsRequest)

Sets supported intrusion settings for an organization

Sets supported intrusion settings for an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntrusionSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    IntrusionSettingsApi apiInstance = new IntrusionSettingsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    UpdateOrganizationSecurityIntrusionSettingsRequest updateOrganizationSecurityIntrusionSettingsRequest = new UpdateOrganizationSecurityIntrusionSettingsRequest(); // UpdateOrganizationSecurityIntrusionSettingsRequest | 
    try {
      Object result = apiInstance.updateOrganizationSecurityIntrusionSettings(organizationId, updateOrganizationSecurityIntrusionSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntrusionSettingsApi#updateOrganizationSecurityIntrusionSettings");
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
| **updateOrganizationSecurityIntrusionSettingsRequest** | [**UpdateOrganizationSecurityIntrusionSettingsRequest**](UpdateOrganizationSecurityIntrusionSettingsRequest.md)|  | |

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

