# DelegatedApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkAppliancePrefixesDelegatedStatic_2**](DelegatedApi.md#createNetworkAppliancePrefixesDelegatedStatic_2) | **POST** /networks/{networkId}/appliance/prefixes/delegated/statics | Add a static delegated prefix from a network |
| [**deleteNetworkAppliancePrefixesDelegatedStatic_2**](DelegatedApi.md#deleteNetworkAppliancePrefixesDelegatedStatic_2) | **DELETE** /networks/{networkId}/appliance/prefixes/delegated/statics/{staticDelegatedPrefixId} | Delete a static delegated prefix from a network |
| [**getDeviceAppliancePrefixesDelegatedVlanAssignments_2**](DelegatedApi.md#getDeviceAppliancePrefixesDelegatedVlanAssignments_2) | **GET** /devices/{serial}/appliance/prefixes/delegated/vlanAssignments | Return prefixes assigned to all IPv6 enabled VLANs on an appliance. |
| [**getDeviceAppliancePrefixesDelegated_2**](DelegatedApi.md#getDeviceAppliancePrefixesDelegated_2) | **GET** /devices/{serial}/appliance/prefixes/delegated | Return current delegated IPv6 prefixes on an appliance. |
| [**getNetworkAppliancePrefixesDelegatedStatic_2**](DelegatedApi.md#getNetworkAppliancePrefixesDelegatedStatic_2) | **GET** /networks/{networkId}/appliance/prefixes/delegated/statics/{staticDelegatedPrefixId} | Return a static delegated prefix from a network |
| [**getNetworkAppliancePrefixesDelegatedStatics_2**](DelegatedApi.md#getNetworkAppliancePrefixesDelegatedStatics_2) | **GET** /networks/{networkId}/appliance/prefixes/delegated/statics | List static delegated prefixes for a network |
| [**updateNetworkAppliancePrefixesDelegatedStatic_2**](DelegatedApi.md#updateNetworkAppliancePrefixesDelegatedStatic_2) | **PUT** /networks/{networkId}/appliance/prefixes/delegated/statics/{staticDelegatedPrefixId} | Update a static delegated prefix from a network |


<a id="createNetworkAppliancePrefixesDelegatedStatic_2"></a>
# **createNetworkAppliancePrefixesDelegatedStatic_2**
> Object createNetworkAppliancePrefixesDelegatedStatic_2(networkId, createNetworkAppliancePrefixesDelegatedStaticRequest)

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
import org.openapitools.client.api.DelegatedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DelegatedApi apiInstance = new DelegatedApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkAppliancePrefixesDelegatedStaticRequest createNetworkAppliancePrefixesDelegatedStaticRequest = new CreateNetworkAppliancePrefixesDelegatedStaticRequest(); // CreateNetworkAppliancePrefixesDelegatedStaticRequest | 
    try {
      Object result = apiInstance.createNetworkAppliancePrefixesDelegatedStatic_2(networkId, createNetworkAppliancePrefixesDelegatedStaticRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DelegatedApi#createNetworkAppliancePrefixesDelegatedStatic_2");
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

<a id="deleteNetworkAppliancePrefixesDelegatedStatic_2"></a>
# **deleteNetworkAppliancePrefixesDelegatedStatic_2**
> deleteNetworkAppliancePrefixesDelegatedStatic_2(networkId, staticDelegatedPrefixId)

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
import org.openapitools.client.api.DelegatedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DelegatedApi apiInstance = new DelegatedApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String staticDelegatedPrefixId = "staticDelegatedPrefixId_example"; // String | 
    try {
      apiInstance.deleteNetworkAppliancePrefixesDelegatedStatic_2(networkId, staticDelegatedPrefixId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DelegatedApi#deleteNetworkAppliancePrefixesDelegatedStatic_2");
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

<a id="getDeviceAppliancePrefixesDelegatedVlanAssignments_2"></a>
# **getDeviceAppliancePrefixesDelegatedVlanAssignments_2**
> List&lt;Object&gt; getDeviceAppliancePrefixesDelegatedVlanAssignments_2(serial)

Return prefixes assigned to all IPv6 enabled VLANs on an appliance.

Return prefixes assigned to all IPv6 enabled VLANs on an appliance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DelegatedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DelegatedApi apiInstance = new DelegatedApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      List<Object> result = apiInstance.getDeviceAppliancePrefixesDelegatedVlanAssignments_2(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DelegatedApi#getDeviceAppliancePrefixesDelegatedVlanAssignments_2");
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

<a id="getDeviceAppliancePrefixesDelegated_2"></a>
# **getDeviceAppliancePrefixesDelegated_2**
> List&lt;Object&gt; getDeviceAppliancePrefixesDelegated_2(serial)

Return current delegated IPv6 prefixes on an appliance.

Return current delegated IPv6 prefixes on an appliance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DelegatedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DelegatedApi apiInstance = new DelegatedApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      List<Object> result = apiInstance.getDeviceAppliancePrefixesDelegated_2(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DelegatedApi#getDeviceAppliancePrefixesDelegated_2");
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

<a id="getNetworkAppliancePrefixesDelegatedStatic_2"></a>
# **getNetworkAppliancePrefixesDelegatedStatic_2**
> GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner getNetworkAppliancePrefixesDelegatedStatic_2(networkId, staticDelegatedPrefixId)

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
import org.openapitools.client.api.DelegatedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DelegatedApi apiInstance = new DelegatedApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String staticDelegatedPrefixId = "staticDelegatedPrefixId_example"; // String | 
    try {
      GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner result = apiInstance.getNetworkAppliancePrefixesDelegatedStatic_2(networkId, staticDelegatedPrefixId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DelegatedApi#getNetworkAppliancePrefixesDelegatedStatic_2");
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

<a id="getNetworkAppliancePrefixesDelegatedStatics_2"></a>
# **getNetworkAppliancePrefixesDelegatedStatics_2**
> List&lt;GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner&gt; getNetworkAppliancePrefixesDelegatedStatics_2(networkId)

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
import org.openapitools.client.api.DelegatedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DelegatedApi apiInstance = new DelegatedApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner> result = apiInstance.getNetworkAppliancePrefixesDelegatedStatics_2(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DelegatedApi#getNetworkAppliancePrefixesDelegatedStatics_2");
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

<a id="updateNetworkAppliancePrefixesDelegatedStatic_2"></a>
# **updateNetworkAppliancePrefixesDelegatedStatic_2**
> Object updateNetworkAppliancePrefixesDelegatedStatic_2(networkId, staticDelegatedPrefixId, updateNetworkAppliancePrefixesDelegatedStaticRequest)

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
import org.openapitools.client.api.DelegatedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DelegatedApi apiInstance = new DelegatedApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String staticDelegatedPrefixId = "staticDelegatedPrefixId_example"; // String | 
    UpdateNetworkAppliancePrefixesDelegatedStaticRequest updateNetworkAppliancePrefixesDelegatedStaticRequest = new UpdateNetworkAppliancePrefixesDelegatedStaticRequest(); // UpdateNetworkAppliancePrefixesDelegatedStaticRequest | 
    try {
      Object result = apiInstance.updateNetworkAppliancePrefixesDelegatedStatic_2(networkId, staticDelegatedPrefixId, updateNetworkAppliancePrefixesDelegatedStaticRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DelegatedApi#updateNetworkAppliancePrefixesDelegatedStatic_2");
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

