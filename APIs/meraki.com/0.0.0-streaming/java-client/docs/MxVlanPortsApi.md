# MxVlanPortsApi

All URIs are relative to *https://api.meraki.com/api/v0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkAppliancePort**](MxVlanPortsApi.md#getNetworkAppliancePort) | **GET** /networks/{networkId}/appliancePorts/{appliancePortId} | Return per-port VLAN settings for a single MX port. |
| [**getNetworkAppliancePorts**](MxVlanPortsApi.md#getNetworkAppliancePorts) | **GET** /networks/{networkId}/appliancePorts | List per-port VLAN settings for all ports of a MX. |
| [**updateNetworkAppliancePort**](MxVlanPortsApi.md#updateNetworkAppliancePort) | **PUT** /networks/{networkId}/appliancePorts/{appliancePortId} | Update the per-port VLAN settings for a single MX port. |


<a id="getNetworkAppliancePort"></a>
# **getNetworkAppliancePort**
> Object getNetworkAppliancePort(networkId, appliancePortId)

Return per-port VLAN settings for a single MX port.

Return per-port VLAN settings for a single MX port.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MxVlanPortsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MxVlanPortsApi apiInstance = new MxVlanPortsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String appliancePortId = "appliancePortId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkAppliancePort(networkId, appliancePortId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MxVlanPortsApi#getNetworkAppliancePort");
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
| **appliancePortId** | **String**|  | |

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

<a id="getNetworkAppliancePorts"></a>
# **getNetworkAppliancePorts**
> List&lt;Object&gt; getNetworkAppliancePorts(networkId)

List per-port VLAN settings for all ports of a MX.

List per-port VLAN settings for all ports of a MX.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MxVlanPortsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MxVlanPortsApi apiInstance = new MxVlanPortsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkAppliancePorts(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MxVlanPortsApi#getNetworkAppliancePorts");
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

<a id="updateNetworkAppliancePort"></a>
# **updateNetworkAppliancePort**
> Object updateNetworkAppliancePort(networkId, appliancePortId, updateNetworkAppliancePortRequest)

Update the per-port VLAN settings for a single MX port.

Update the per-port VLAN settings for a single MX port.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MxVlanPortsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MxVlanPortsApi apiInstance = new MxVlanPortsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String appliancePortId = "appliancePortId_example"; // String | 
    UpdateNetworkAppliancePortRequest updateNetworkAppliancePortRequest = new UpdateNetworkAppliancePortRequest(); // UpdateNetworkAppliancePortRequest | 
    try {
      Object result = apiInstance.updateNetworkAppliancePort(networkId, appliancePortId, updateNetworkAppliancePortRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MxVlanPortsApi#updateNetworkAppliancePort");
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
| **appliancePortId** | **String**|  | |
| **updateNetworkAppliancePortRequest** | [**UpdateNetworkAppliancePortRequest**](UpdateNetworkAppliancePortRequest.md)|  | [optional] |

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

