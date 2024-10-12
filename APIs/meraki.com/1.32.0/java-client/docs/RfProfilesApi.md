# RfProfilesApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkWirelessRfProfile_1**](RfProfilesApi.md#createNetworkWirelessRfProfile_1) | **POST** /networks/{networkId}/wireless/rfProfiles | Creates new RF profile for this network |
| [**deleteNetworkWirelessRfProfile_1**](RfProfilesApi.md#deleteNetworkWirelessRfProfile_1) | **DELETE** /networks/{networkId}/wireless/rfProfiles/{rfProfileId} | Delete a RF Profile |
| [**getNetworkWirelessRfProfile_1**](RfProfilesApi.md#getNetworkWirelessRfProfile_1) | **GET** /networks/{networkId}/wireless/rfProfiles/{rfProfileId} | Return a RF profile |
| [**getNetworkWirelessRfProfiles_1**](RfProfilesApi.md#getNetworkWirelessRfProfiles_1) | **GET** /networks/{networkId}/wireless/rfProfiles | List the non-basic RF profiles for this network |
| [**updateNetworkWirelessRfProfile_1**](RfProfilesApi.md#updateNetworkWirelessRfProfile_1) | **PUT** /networks/{networkId}/wireless/rfProfiles/{rfProfileId} | Updates specified RF profile for this network |


<a id="createNetworkWirelessRfProfile_1"></a>
# **createNetworkWirelessRfProfile_1**
> CreateNetworkWirelessRfProfile201Response createNetworkWirelessRfProfile_1(networkId, createNetworkWirelessRfProfileRequest)

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
import org.openapitools.client.api.RfProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RfProfilesApi apiInstance = new RfProfilesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkWirelessRfProfileRequest createNetworkWirelessRfProfileRequest = new CreateNetworkWirelessRfProfileRequest(); // CreateNetworkWirelessRfProfileRequest | 
    try {
      CreateNetworkWirelessRfProfile201Response result = apiInstance.createNetworkWirelessRfProfile_1(networkId, createNetworkWirelessRfProfileRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RfProfilesApi#createNetworkWirelessRfProfile_1");
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

[**CreateNetworkWirelessRfProfile201Response**](CreateNetworkWirelessRfProfile201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="deleteNetworkWirelessRfProfile_1"></a>
# **deleteNetworkWirelessRfProfile_1**
> deleteNetworkWirelessRfProfile_1(networkId, rfProfileId)

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
import org.openapitools.client.api.RfProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RfProfilesApi apiInstance = new RfProfilesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String rfProfileId = "rfProfileId_example"; // String | 
    try {
      apiInstance.deleteNetworkWirelessRfProfile_1(networkId, rfProfileId);
    } catch (ApiException e) {
      System.err.println("Exception when calling RfProfilesApi#deleteNetworkWirelessRfProfile_1");
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

<a id="getNetworkWirelessRfProfile_1"></a>
# **getNetworkWirelessRfProfile_1**
> Object getNetworkWirelessRfProfile_1(networkId, rfProfileId)

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
import org.openapitools.client.api.RfProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RfProfilesApi apiInstance = new RfProfilesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String rfProfileId = "rfProfileId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkWirelessRfProfile_1(networkId, rfProfileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RfProfilesApi#getNetworkWirelessRfProfile_1");
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

<a id="getNetworkWirelessRfProfiles_1"></a>
# **getNetworkWirelessRfProfiles_1**
> List&lt;Object&gt; getNetworkWirelessRfProfiles_1(networkId, includeTemplateProfiles)

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
import org.openapitools.client.api.RfProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RfProfilesApi apiInstance = new RfProfilesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    Boolean includeTemplateProfiles = true; // Boolean | If the network is bound to a template, this parameter controls whether or not the non-basic RF profiles defined on the template should be included in the response alongside the non-basic profiles defined on the bound network. Defaults to false.
    try {
      List<Object> result = apiInstance.getNetworkWirelessRfProfiles_1(networkId, includeTemplateProfiles);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RfProfilesApi#getNetworkWirelessRfProfiles_1");
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

<a id="updateNetworkWirelessRfProfile_1"></a>
# **updateNetworkWirelessRfProfile_1**
> CreateNetworkWirelessRfProfile201Response updateNetworkWirelessRfProfile_1(networkId, rfProfileId, updateNetworkWirelessRfProfileRequest)

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
import org.openapitools.client.api.RfProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RfProfilesApi apiInstance = new RfProfilesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String rfProfileId = "rfProfileId_example"; // String | 
    UpdateNetworkWirelessRfProfileRequest updateNetworkWirelessRfProfileRequest = new UpdateNetworkWirelessRfProfileRequest(); // UpdateNetworkWirelessRfProfileRequest | 
    try {
      CreateNetworkWirelessRfProfile201Response result = apiInstance.updateNetworkWirelessRfProfile_1(networkId, rfProfileId, updateNetworkWirelessRfProfileRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RfProfilesApi#updateNetworkWirelessRfProfile_1");
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

[**CreateNetworkWirelessRfProfile201Response**](CreateNetworkWirelessRfProfile201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

