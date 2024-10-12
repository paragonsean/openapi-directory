# RulesApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkApplianceTrafficShapingRules_2**](RulesApi.md#getNetworkApplianceTrafficShapingRules_2) | **GET** /networks/{networkId}/appliance/trafficShaping/rules | Display the traffic shaping settings rules for an MX network |
| [**getNetworkWirelessSsidTrafficShapingRules_3**](RulesApi.md#getNetworkWirelessSsidTrafficShapingRules_3) | **GET** /networks/{networkId}/wireless/ssids/{number}/trafficShaping/rules | Display the traffic shaping settings for a SSID on an MR network |
| [**updateNetworkApplianceTrafficShapingRules_2**](RulesApi.md#updateNetworkApplianceTrafficShapingRules_2) | **PUT** /networks/{networkId}/appliance/trafficShaping/rules | Update the traffic shaping settings rules for an MX network |
| [**updateNetworkWirelessSsidTrafficShapingRules_3**](RulesApi.md#updateNetworkWirelessSsidTrafficShapingRules_3) | **PUT** /networks/{networkId}/wireless/ssids/{number}/trafficShaping/rules | Update the traffic shaping settings for an SSID on an MR network |


<a id="getNetworkApplianceTrafficShapingRules_2"></a>
# **getNetworkApplianceTrafficShapingRules_2**
> Object getNetworkApplianceTrafficShapingRules_2(networkId)

Display the traffic shaping settings rules for an MX network

Display the traffic shaping settings rules for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RulesApi apiInstance = new RulesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceTrafficShapingRules_2(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RulesApi#getNetworkApplianceTrafficShapingRules_2");
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

<a id="getNetworkWirelessSsidTrafficShapingRules_3"></a>
# **getNetworkWirelessSsidTrafficShapingRules_3**
> Object getNetworkWirelessSsidTrafficShapingRules_3(networkId, number)

Display the traffic shaping settings for a SSID on an MR network

Display the traffic shaping settings for a SSID on an MR network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RulesApi apiInstance = new RulesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    try {
      Object result = apiInstance.getNetworkWirelessSsidTrafficShapingRules_3(networkId, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RulesApi#getNetworkWirelessSsidTrafficShapingRules_3");
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
| **number** | **String**|  | |

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

<a id="updateNetworkApplianceTrafficShapingRules_2"></a>
# **updateNetworkApplianceTrafficShapingRules_2**
> Object updateNetworkApplianceTrafficShapingRules_2(networkId, updateNetworkApplianceTrafficShapingRulesRequest)

Update the traffic shaping settings rules for an MX network

Update the traffic shaping settings rules for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RulesApi apiInstance = new RulesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceTrafficShapingRulesRequest updateNetworkApplianceTrafficShapingRulesRequest = new UpdateNetworkApplianceTrafficShapingRulesRequest(); // UpdateNetworkApplianceTrafficShapingRulesRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceTrafficShapingRules_2(networkId, updateNetworkApplianceTrafficShapingRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RulesApi#updateNetworkApplianceTrafficShapingRules_2");
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
| **updateNetworkApplianceTrafficShapingRulesRequest** | [**UpdateNetworkApplianceTrafficShapingRulesRequest**](UpdateNetworkApplianceTrafficShapingRulesRequest.md)|  | [optional] |

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

<a id="updateNetworkWirelessSsidTrafficShapingRules_3"></a>
# **updateNetworkWirelessSsidTrafficShapingRules_3**
> Object updateNetworkWirelessSsidTrafficShapingRules_3(networkId, number, updateNetworkWirelessSsidTrafficShapingRulesRequest)

Update the traffic shaping settings for an SSID on an MR network

Update the traffic shaping settings for an SSID on an MR network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RulesApi apiInstance = new RulesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    UpdateNetworkWirelessSsidTrafficShapingRulesRequest updateNetworkWirelessSsidTrafficShapingRulesRequest = new UpdateNetworkWirelessSsidTrafficShapingRulesRequest(); // UpdateNetworkWirelessSsidTrafficShapingRulesRequest | 
    try {
      Object result = apiInstance.updateNetworkWirelessSsidTrafficShapingRules_3(networkId, number, updateNetworkWirelessSsidTrafficShapingRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RulesApi#updateNetworkWirelessSsidTrafficShapingRules_3");
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
| **number** | **String**|  | |
| **updateNetworkWirelessSsidTrafficShapingRulesRequest** | [**UpdateNetworkWirelessSsidTrafficShapingRulesRequest**](UpdateNetworkWirelessSsidTrafficShapingRulesRequest.md)|  | [optional] |

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

