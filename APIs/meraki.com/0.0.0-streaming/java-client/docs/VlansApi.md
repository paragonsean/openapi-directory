# VlansApi

All URIs are relative to *https://api.meraki.com/api/v0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkVlan**](VlansApi.md#createNetworkVlan) | **POST** /networks/{networkId}/vlans | Add a VLAN |
| [**deleteNetworkVlan**](VlansApi.md#deleteNetworkVlan) | **DELETE** /networks/{networkId}/vlans/{vlanId} | Delete a VLAN from a network |
| [**getNetworkVlan**](VlansApi.md#getNetworkVlan) | **GET** /networks/{networkId}/vlans/{vlanId} | Return a VLAN |
| [**getNetworkVlans**](VlansApi.md#getNetworkVlans) | **GET** /networks/{networkId}/vlans | List the VLANs for an MX network |
| [**getNetworkVlansEnabledState**](VlansApi.md#getNetworkVlansEnabledState) | **GET** /networks/{networkId}/vlansEnabledState | Returns the enabled status of VLANs for the network |
| [**updateNetworkVlan**](VlansApi.md#updateNetworkVlan) | **PUT** /networks/{networkId}/vlans/{vlanId} | Update a VLAN |
| [**updateNetworkVlansEnabledState**](VlansApi.md#updateNetworkVlansEnabledState) | **PUT** /networks/{networkId}/vlansEnabledState | Enable/Disable VLANs for the given network |


<a id="createNetworkVlan"></a>
# **createNetworkVlan**
> Object createNetworkVlan(networkId, createNetworkVlanRequest)

Add a VLAN

Add a VLAN

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    VlansApi apiInstance = new VlansApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkVlanRequest createNetworkVlanRequest = new CreateNetworkVlanRequest(); // CreateNetworkVlanRequest | 
    try {
      Object result = apiInstance.createNetworkVlan(networkId, createNetworkVlanRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VlansApi#createNetworkVlan");
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
| **createNetworkVlanRequest** | [**CreateNetworkVlanRequest**](CreateNetworkVlanRequest.md)|  | |

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

<a id="deleteNetworkVlan"></a>
# **deleteNetworkVlan**
> deleteNetworkVlan(networkId, vlanId)

Delete a VLAN from a network

Delete a VLAN from a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    VlansApi apiInstance = new VlansApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String vlanId = "vlanId_example"; // String | 
    try {
      apiInstance.deleteNetworkVlan(networkId, vlanId);
    } catch (ApiException e) {
      System.err.println("Exception when calling VlansApi#deleteNetworkVlan");
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
| **vlanId** | **String**|  | |

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

<a id="getNetworkVlan"></a>
# **getNetworkVlan**
> Object getNetworkVlan(networkId, vlanId)

Return a VLAN

Return a VLAN

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    VlansApi apiInstance = new VlansApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String vlanId = "vlanId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkVlan(networkId, vlanId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VlansApi#getNetworkVlan");
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
| **vlanId** | **String**|  | |

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

<a id="getNetworkVlans"></a>
# **getNetworkVlans**
> List&lt;Object&gt; getNetworkVlans(networkId)

List the VLANs for an MX network

List the VLANs for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    VlansApi apiInstance = new VlansApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkVlans(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VlansApi#getNetworkVlans");
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

<a id="getNetworkVlansEnabledState"></a>
# **getNetworkVlansEnabledState**
> Object getNetworkVlansEnabledState(networkId)

Returns the enabled status of VLANs for the network

Returns the enabled status of VLANs for the network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    VlansApi apiInstance = new VlansApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkVlansEnabledState(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VlansApi#getNetworkVlansEnabledState");
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

<a id="updateNetworkVlan"></a>
# **updateNetworkVlan**
> Object updateNetworkVlan(networkId, vlanId, updateNetworkVlanRequest)

Update a VLAN

Update a VLAN

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    VlansApi apiInstance = new VlansApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String vlanId = "vlanId_example"; // String | 
    UpdateNetworkVlanRequest updateNetworkVlanRequest = new UpdateNetworkVlanRequest(); // UpdateNetworkVlanRequest | 
    try {
      Object result = apiInstance.updateNetworkVlan(networkId, vlanId, updateNetworkVlanRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VlansApi#updateNetworkVlan");
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
| **vlanId** | **String**|  | |
| **updateNetworkVlanRequest** | [**UpdateNetworkVlanRequest**](UpdateNetworkVlanRequest.md)|  | [optional] |

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

<a id="updateNetworkVlansEnabledState"></a>
# **updateNetworkVlansEnabledState**
> Object updateNetworkVlansEnabledState(networkId, updateNetworkVlansEnabledStateRequest)

Enable/Disable VLANs for the given network

Enable/Disable VLANs for the given network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    VlansApi apiInstance = new VlansApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkVlansEnabledStateRequest updateNetworkVlansEnabledStateRequest = new UpdateNetworkVlansEnabledStateRequest(); // UpdateNetworkVlansEnabledStateRequest | 
    try {
      Object result = apiInstance.updateNetworkVlansEnabledState(networkId, updateNetworkVlansEnabledStateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VlansApi#updateNetworkVlansEnabledState");
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
| **updateNetworkVlansEnabledStateRequest** | [**UpdateNetworkVlansEnabledStateRequest**](UpdateNetworkVlansEnabledStateRequest.md)|  | |

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

