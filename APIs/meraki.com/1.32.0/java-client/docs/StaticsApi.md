# StaticsApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkAppliancePrefixesDelegatedStatic_3**](StaticsApi.md#createNetworkAppliancePrefixesDelegatedStatic_3) | **POST** /networks/{networkId}/appliance/prefixes/delegated/statics | Add a static delegated prefix from a network |
| [**deleteNetworkAppliancePrefixesDelegatedStatic_3**](StaticsApi.md#deleteNetworkAppliancePrefixesDelegatedStatic_3) | **DELETE** /networks/{networkId}/appliance/prefixes/delegated/statics/{staticDelegatedPrefixId} | Delete a static delegated prefix from a network |
| [**getNetworkAppliancePrefixesDelegatedStatic_3**](StaticsApi.md#getNetworkAppliancePrefixesDelegatedStatic_3) | **GET** /networks/{networkId}/appliance/prefixes/delegated/statics/{staticDelegatedPrefixId} | Return a static delegated prefix from a network |
| [**getNetworkAppliancePrefixesDelegatedStatics_3**](StaticsApi.md#getNetworkAppliancePrefixesDelegatedStatics_3) | **GET** /networks/{networkId}/appliance/prefixes/delegated/statics | List static delegated prefixes for a network |
| [**updateNetworkAppliancePrefixesDelegatedStatic_3**](StaticsApi.md#updateNetworkAppliancePrefixesDelegatedStatic_3) | **PUT** /networks/{networkId}/appliance/prefixes/delegated/statics/{staticDelegatedPrefixId} | Update a static delegated prefix from a network |


<a id="createNetworkAppliancePrefixesDelegatedStatic_3"></a>
# **createNetworkAppliancePrefixesDelegatedStatic_3**
> Object createNetworkAppliancePrefixesDelegatedStatic_3(networkId, createNetworkAppliancePrefixesDelegatedStaticRequest)

Add a static delegated prefix from a network

Add a static delegated prefix from a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StaticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StaticsApi apiInstance = new StaticsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkAppliancePrefixesDelegatedStaticRequest createNetworkAppliancePrefixesDelegatedStaticRequest = new CreateNetworkAppliancePrefixesDelegatedStaticRequest(); // CreateNetworkAppliancePrefixesDelegatedStaticRequest | 
    try {
      Object result = apiInstance.createNetworkAppliancePrefixesDelegatedStatic_3(networkId, createNetworkAppliancePrefixesDelegatedStaticRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StaticsApi#createNetworkAppliancePrefixesDelegatedStatic_3");
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
| **createNetworkAppliancePrefixesDelegatedStaticRequest** | [**CreateNetworkAppliancePrefixesDelegatedStaticRequest**](CreateNetworkAppliancePrefixesDelegatedStaticRequest.md)|  | |

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

<a id="deleteNetworkAppliancePrefixesDelegatedStatic_3"></a>
# **deleteNetworkAppliancePrefixesDelegatedStatic_3**
> deleteNetworkAppliancePrefixesDelegatedStatic_3(networkId, staticDelegatedPrefixId)

Delete a static delegated prefix from a network

Delete a static delegated prefix from a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StaticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StaticsApi apiInstance = new StaticsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String staticDelegatedPrefixId = "staticDelegatedPrefixId_example"; // String | 
    try {
      apiInstance.deleteNetworkAppliancePrefixesDelegatedStatic_3(networkId, staticDelegatedPrefixId);
    } catch (ApiException e) {
      System.err.println("Exception when calling StaticsApi#deleteNetworkAppliancePrefixesDelegatedStatic_3");
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
| **staticDelegatedPrefixId** | **String**|  | |

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

<a id="getNetworkAppliancePrefixesDelegatedStatic_3"></a>
# **getNetworkAppliancePrefixesDelegatedStatic_3**
> GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner getNetworkAppliancePrefixesDelegatedStatic_3(networkId, staticDelegatedPrefixId)

Return a static delegated prefix from a network

Return a static delegated prefix from a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StaticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StaticsApi apiInstance = new StaticsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String staticDelegatedPrefixId = "staticDelegatedPrefixId_example"; // String | 
    try {
      GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner result = apiInstance.getNetworkAppliancePrefixesDelegatedStatic_3(networkId, staticDelegatedPrefixId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StaticsApi#getNetworkAppliancePrefixesDelegatedStatic_3");
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
| **staticDelegatedPrefixId** | **String**|  | |

### Return type

[**GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner**](GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkAppliancePrefixesDelegatedStatics_3"></a>
# **getNetworkAppliancePrefixesDelegatedStatics_3**
> List&lt;GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner&gt; getNetworkAppliancePrefixesDelegatedStatics_3(networkId)

List static delegated prefixes for a network

List static delegated prefixes for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StaticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StaticsApi apiInstance = new StaticsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner> result = apiInstance.getNetworkAppliancePrefixesDelegatedStatics_3(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StaticsApi#getNetworkAppliancePrefixesDelegatedStatics_3");
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

[**List&lt;GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner&gt;**](GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkAppliancePrefixesDelegatedStatic_3"></a>
# **updateNetworkAppliancePrefixesDelegatedStatic_3**
> Object updateNetworkAppliancePrefixesDelegatedStatic_3(networkId, staticDelegatedPrefixId, updateNetworkAppliancePrefixesDelegatedStaticRequest)

Update a static delegated prefix from a network

Update a static delegated prefix from a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StaticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StaticsApi apiInstance = new StaticsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String staticDelegatedPrefixId = "staticDelegatedPrefixId_example"; // String | 
    UpdateNetworkAppliancePrefixesDelegatedStaticRequest updateNetworkAppliancePrefixesDelegatedStaticRequest = new UpdateNetworkAppliancePrefixesDelegatedStaticRequest(); // UpdateNetworkAppliancePrefixesDelegatedStaticRequest | 
    try {
      Object result = apiInstance.updateNetworkAppliancePrefixesDelegatedStatic_3(networkId, staticDelegatedPrefixId, updateNetworkAppliancePrefixesDelegatedStaticRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StaticsApi#updateNetworkAppliancePrefixesDelegatedStatic_3");
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
| **staticDelegatedPrefixId** | **String**|  | |
| **updateNetworkAppliancePrefixesDelegatedStaticRequest** | [**UpdateNetworkAppliancePrefixesDelegatedStaticRequest**](UpdateNetworkAppliancePrefixesDelegatedStaticRequest.md)|  | [optional] |

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

