# VlansApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkApplianceVlan_1**](VlansApi.md#createNetworkApplianceVlan_1) | **POST** /networks/{networkId}/appliance/vlans | Add a VLAN |
| [**deleteNetworkApplianceVlan_1**](VlansApi.md#deleteNetworkApplianceVlan_1) | **DELETE** /networks/{networkId}/appliance/vlans/{vlanId} | Delete a VLAN from a network |
| [**getNetworkApplianceVlan_1**](VlansApi.md#getNetworkApplianceVlan_1) | **GET** /networks/{networkId}/appliance/vlans/{vlanId} | Return a VLAN |
| [**getNetworkApplianceVlansSettings_1**](VlansApi.md#getNetworkApplianceVlansSettings_1) | **GET** /networks/{networkId}/appliance/vlans/settings | Returns the enabled status of VLANs for the network |
| [**getNetworkApplianceVlans_1**](VlansApi.md#getNetworkApplianceVlans_1) | **GET** /networks/{networkId}/appliance/vlans | List the VLANs for an MX network |
| [**updateNetworkApplianceVlan_1**](VlansApi.md#updateNetworkApplianceVlan_1) | **PUT** /networks/{networkId}/appliance/vlans/{vlanId} | Update a VLAN |
| [**updateNetworkApplianceVlansSettings_1**](VlansApi.md#updateNetworkApplianceVlansSettings_1) | **PUT** /networks/{networkId}/appliance/vlans/settings | Enable/Disable VLANs for the given network |


<a id="createNetworkApplianceVlan_1"></a>
# **createNetworkApplianceVlan_1**
> CreateNetworkApplianceVlan201Response createNetworkApplianceVlan_1(networkId, createNetworkApplianceVlanRequest)

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
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    VlansApi apiInstance = new VlansApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkApplianceVlanRequest createNetworkApplianceVlanRequest = new CreateNetworkApplianceVlanRequest(); // CreateNetworkApplianceVlanRequest | 
    try {
      CreateNetworkApplianceVlan201Response result = apiInstance.createNetworkApplianceVlan_1(networkId, createNetworkApplianceVlanRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VlansApi#createNetworkApplianceVlan_1");
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
| **createNetworkApplianceVlanRequest** | [**CreateNetworkApplianceVlanRequest**](CreateNetworkApplianceVlanRequest.md)|  | |

### Return type

[**CreateNetworkApplianceVlan201Response**](CreateNetworkApplianceVlan201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="deleteNetworkApplianceVlan_1"></a>
# **deleteNetworkApplianceVlan_1**
> deleteNetworkApplianceVlan_1(networkId, vlanId)

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
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    VlansApi apiInstance = new VlansApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String vlanId = "vlanId_example"; // String | 
    try {
      apiInstance.deleteNetworkApplianceVlan_1(networkId, vlanId);
    } catch (ApiException e) {
      System.err.println("Exception when calling VlansApi#deleteNetworkApplianceVlan_1");
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

<a id="getNetworkApplianceVlan_1"></a>
# **getNetworkApplianceVlan_1**
> GetNetworkApplianceVlans200ResponseInner getNetworkApplianceVlan_1(networkId, vlanId)

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
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    VlansApi apiInstance = new VlansApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String vlanId = "vlanId_example"; // String | 
    try {
      GetNetworkApplianceVlans200ResponseInner result = apiInstance.getNetworkApplianceVlan_1(networkId, vlanId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VlansApi#getNetworkApplianceVlan_1");
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

[**GetNetworkApplianceVlans200ResponseInner**](GetNetworkApplianceVlans200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceVlansSettings_1"></a>
# **getNetworkApplianceVlansSettings_1**
> Object getNetworkApplianceVlansSettings_1(networkId)

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
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    VlansApi apiInstance = new VlansApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceVlansSettings_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VlansApi#getNetworkApplianceVlansSettings_1");
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

<a id="getNetworkApplianceVlans_1"></a>
# **getNetworkApplianceVlans_1**
> List&lt;GetNetworkApplianceVlans200ResponseInner&gt; getNetworkApplianceVlans_1(networkId)

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
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    VlansApi apiInstance = new VlansApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<GetNetworkApplianceVlans200ResponseInner> result = apiInstance.getNetworkApplianceVlans_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VlansApi#getNetworkApplianceVlans_1");
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

[**List&lt;GetNetworkApplianceVlans200ResponseInner&gt;**](GetNetworkApplianceVlans200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceVlan_1"></a>
# **updateNetworkApplianceVlan_1**
> GetNetworkApplianceVlans200ResponseInner updateNetworkApplianceVlan_1(networkId, vlanId, updateNetworkApplianceVlanRequest)

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
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    VlansApi apiInstance = new VlansApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String vlanId = "vlanId_example"; // String | 
    UpdateNetworkApplianceVlanRequest updateNetworkApplianceVlanRequest = new UpdateNetworkApplianceVlanRequest(); // UpdateNetworkApplianceVlanRequest | 
    try {
      GetNetworkApplianceVlans200ResponseInner result = apiInstance.updateNetworkApplianceVlan_1(networkId, vlanId, updateNetworkApplianceVlanRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VlansApi#updateNetworkApplianceVlan_1");
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
| **updateNetworkApplianceVlanRequest** | [**UpdateNetworkApplianceVlanRequest**](UpdateNetworkApplianceVlanRequest.md)|  | [optional] |

### Return type

[**GetNetworkApplianceVlans200ResponseInner**](GetNetworkApplianceVlans200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceVlansSettings_1"></a>
# **updateNetworkApplianceVlansSettings_1**
> Object updateNetworkApplianceVlansSettings_1(networkId, updateNetworkApplianceVlansSettingsRequest)

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
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    VlansApi apiInstance = new VlansApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceVlansSettingsRequest updateNetworkApplianceVlansSettingsRequest = new UpdateNetworkApplianceVlansSettingsRequest(); // UpdateNetworkApplianceVlansSettingsRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceVlansSettings_1(networkId, updateNetworkApplianceVlansSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VlansApi#updateNetworkApplianceVlansSettings_1");
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
| **updateNetworkApplianceVlansSettingsRequest** | [**UpdateNetworkApplianceVlansSettingsRequest**](UpdateNetworkApplianceVlansSettingsRequest.md)|  | [optional] |

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

