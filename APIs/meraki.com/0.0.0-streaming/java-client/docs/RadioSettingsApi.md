# RadioSettingsApi

All URIs are relative to *https://api.meraki.com/api/v0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkWirelessRfProfile**](RadioSettingsApi.md#createNetworkWirelessRfProfile) | **POST** /networks/{networkId}/wireless/rfProfiles | Creates new RF profile for this network |
| [**deleteNetworkWirelessRfProfile**](RadioSettingsApi.md#deleteNetworkWirelessRfProfile) | **DELETE** /networks/{networkId}/wireless/rfProfiles/{rfProfileId} | Delete a RF Profile |
| [**getNetworkWirelessRfProfile**](RadioSettingsApi.md#getNetworkWirelessRfProfile) | **GET** /networks/{networkId}/wireless/rfProfiles/{rfProfileId} | Return a RF profile |
| [**getNetworkWirelessRfProfiles**](RadioSettingsApi.md#getNetworkWirelessRfProfiles) | **GET** /networks/{networkId}/wireless/rfProfiles | List the non-basic RF profiles for this network |
| [**updateNetworkWirelessRfProfile**](RadioSettingsApi.md#updateNetworkWirelessRfProfile) | **PUT** /networks/{networkId}/wireless/rfProfiles/{rfProfileId} | Updates specified RF profile for this network |


<a id="createNetworkWirelessRfProfile"></a>
# **createNetworkWirelessRfProfile**
> Object createNetworkWirelessRfProfile(networkId, createNetworkWirelessRfProfileRequest)

Creates new RF profile for this network

Creates new RF profile for this network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RadioSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RadioSettingsApi apiInstance = new RadioSettingsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkWirelessRfProfileRequest createNetworkWirelessRfProfileRequest = new CreateNetworkWirelessRfProfileRequest(); // CreateNetworkWirelessRfProfileRequest | 
    try {
      Object result = apiInstance.createNetworkWirelessRfProfile(networkId, createNetworkWirelessRfProfileRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RadioSettingsApi#createNetworkWirelessRfProfile");
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
| **createNetworkWirelessRfProfileRequest** | [**CreateNetworkWirelessRfProfileRequest**](CreateNetworkWirelessRfProfileRequest.md)|  | |

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

<a id="deleteNetworkWirelessRfProfile"></a>
# **deleteNetworkWirelessRfProfile**
> deleteNetworkWirelessRfProfile(networkId, rfProfileId)

Delete a RF Profile

Delete a RF Profile

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RadioSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RadioSettingsApi apiInstance = new RadioSettingsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String rfProfileId = "rfProfileId_example"; // String | 
    try {
      apiInstance.deleteNetworkWirelessRfProfile(networkId, rfProfileId);
    } catch (ApiException e) {
      System.err.println("Exception when calling RadioSettingsApi#deleteNetworkWirelessRfProfile");
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
| **rfProfileId** | **String**|  | |

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

<a id="getNetworkWirelessRfProfile"></a>
# **getNetworkWirelessRfProfile**
> Object getNetworkWirelessRfProfile(networkId, rfProfileId)

Return a RF profile

Return a RF profile

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RadioSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RadioSettingsApi apiInstance = new RadioSettingsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String rfProfileId = "rfProfileId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkWirelessRfProfile(networkId, rfProfileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RadioSettingsApi#getNetworkWirelessRfProfile");
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
| **rfProfileId** | **String**|  | |

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

<a id="getNetworkWirelessRfProfiles"></a>
# **getNetworkWirelessRfProfiles**
> List&lt;Object&gt; getNetworkWirelessRfProfiles(networkId, includeTemplateProfiles)

List the non-basic RF profiles for this network

List the non-basic RF profiles for this network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RadioSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RadioSettingsApi apiInstance = new RadioSettingsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    Boolean includeTemplateProfiles = true; // Boolean | If the network is bound to a template, this parameter controls whether or not the non-basic RF profiles defined on the template should be included in the response alongside the non-basic profiles defined on the bound network. Defaults to false.
    try {
      List<Object> result = apiInstance.getNetworkWirelessRfProfiles(networkId, includeTemplateProfiles);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RadioSettingsApi#getNetworkWirelessRfProfiles");
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
| **includeTemplateProfiles** | **Boolean**| If the network is bound to a template, this parameter controls whether or not the non-basic RF profiles defined on the template should be included in the response alongside the non-basic profiles defined on the bound network. Defaults to false. | [optional] |

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

<a id="updateNetworkWirelessRfProfile"></a>
# **updateNetworkWirelessRfProfile**
> Object updateNetworkWirelessRfProfile(networkId, rfProfileId, updateNetworkWirelessRfProfileRequest)

Updates specified RF profile for this network

Updates specified RF profile for this network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RadioSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RadioSettingsApi apiInstance = new RadioSettingsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String rfProfileId = "rfProfileId_example"; // String | 
    UpdateNetworkWirelessRfProfileRequest updateNetworkWirelessRfProfileRequest = new UpdateNetworkWirelessRfProfileRequest(); // UpdateNetworkWirelessRfProfileRequest | 
    try {
      Object result = apiInstance.updateNetworkWirelessRfProfile(networkId, rfProfileId, updateNetworkWirelessRfProfileRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RadioSettingsApi#updateNetworkWirelessRfProfile");
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
| **rfProfileId** | **String**|  | |
| **updateNetworkWirelessRfProfileRequest** | [**UpdateNetworkWirelessRfProfileRequest**](UpdateNetworkWirelessRfProfileRequest.md)|  | [optional] |

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

