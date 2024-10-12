# SsidsApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkWirelessSsidIdentityPsk_1**](SsidsApi.md#createNetworkWirelessSsidIdentityPsk_1) | **POST** /networks/{networkId}/wireless/ssids/{number}/identityPsks | Create an Identity PSK |
| [**deleteNetworkWirelessSsidIdentityPsk_1**](SsidsApi.md#deleteNetworkWirelessSsidIdentityPsk_1) | **DELETE** /networks/{networkId}/wireless/ssids/{number}/identityPsks/{identityPskId} | Delete an Identity PSK |
| [**getNetworkApplianceSsid_1**](SsidsApi.md#getNetworkApplianceSsid_1) | **GET** /networks/{networkId}/appliance/ssids/{number} | Return a single MX SSID |
| [**getNetworkApplianceSsids_1**](SsidsApi.md#getNetworkApplianceSsids_1) | **GET** /networks/{networkId}/appliance/ssids | List the MX SSIDs in a network |
| [**getNetworkWirelessSsidBonjourForwarding_1**](SsidsApi.md#getNetworkWirelessSsidBonjourForwarding_1) | **GET** /networks/{networkId}/wireless/ssids/{number}/bonjourForwarding | List the Bonjour forwarding setting and rules for the SSID |
| [**getNetworkWirelessSsidDeviceTypeGroupPolicies_1**](SsidsApi.md#getNetworkWirelessSsidDeviceTypeGroupPolicies_1) | **GET** /networks/{networkId}/wireless/ssids/{number}/deviceTypeGroupPolicies | List the device type group policies for the SSID |
| [**getNetworkWirelessSsidEapOverride_1**](SsidsApi.md#getNetworkWirelessSsidEapOverride_1) | **GET** /networks/{networkId}/wireless/ssids/{number}/eapOverride | Return the EAP overridden parameters for an SSID |
| [**getNetworkWirelessSsidFirewallL3FirewallRules_1**](SsidsApi.md#getNetworkWirelessSsidFirewallL3FirewallRules_1) | **GET** /networks/{networkId}/wireless/ssids/{number}/firewall/l3FirewallRules | Return the L3 firewall rules for an SSID on an MR network |
| [**getNetworkWirelessSsidFirewallL7FirewallRules_1**](SsidsApi.md#getNetworkWirelessSsidFirewallL7FirewallRules_1) | **GET** /networks/{networkId}/wireless/ssids/{number}/firewall/l7FirewallRules | Return the L7 firewall rules for an SSID on an MR network |
| [**getNetworkWirelessSsidHotspot20_1**](SsidsApi.md#getNetworkWirelessSsidHotspot20_1) | **GET** /networks/{networkId}/wireless/ssids/{number}/hotspot20 | Return the Hotspot 2.0 settings for an SSID |
| [**getNetworkWirelessSsidIdentityPsk_1**](SsidsApi.md#getNetworkWirelessSsidIdentityPsk_1) | **GET** /networks/{networkId}/wireless/ssids/{number}/identityPsks/{identityPskId} | Return an Identity PSK |
| [**getNetworkWirelessSsidIdentityPsks_1**](SsidsApi.md#getNetworkWirelessSsidIdentityPsks_1) | **GET** /networks/{networkId}/wireless/ssids/{number}/identityPsks | List all Identity PSKs in a wireless network |
| [**getNetworkWirelessSsidSchedules_1**](SsidsApi.md#getNetworkWirelessSsidSchedules_1) | **GET** /networks/{networkId}/wireless/ssids/{number}/schedules | List the outage schedule for the SSID |
| [**getNetworkWirelessSsidSplashSettings_1**](SsidsApi.md#getNetworkWirelessSsidSplashSettings_1) | **GET** /networks/{networkId}/wireless/ssids/{number}/splash/settings | Display the splash page settings for the given SSID |
| [**getNetworkWirelessSsidTrafficShapingRules_1**](SsidsApi.md#getNetworkWirelessSsidTrafficShapingRules_1) | **GET** /networks/{networkId}/wireless/ssids/{number}/trafficShaping/rules | Display the traffic shaping settings for a SSID on an MR network |
| [**getNetworkWirelessSsidVpn_1**](SsidsApi.md#getNetworkWirelessSsidVpn_1) | **GET** /networks/{networkId}/wireless/ssids/{number}/vpn | List the VPN settings for the SSID. |
| [**getNetworkWirelessSsid_1**](SsidsApi.md#getNetworkWirelessSsid_1) | **GET** /networks/{networkId}/wireless/ssids/{number} | Return a single MR SSID |
| [**getNetworkWirelessSsids_1**](SsidsApi.md#getNetworkWirelessSsids_1) | **GET** /networks/{networkId}/wireless/ssids | List the MR SSIDs in a network |
| [**getOrganizationSummaryTopSsidsByUsage_3**](SsidsApi.md#getOrganizationSummaryTopSsidsByUsage_3) | **GET** /organizations/{organizationId}/summary/top/ssids/byUsage | Return metrics for organization&#39;s top 10 ssids by data usage over given time range |
| [**updateNetworkApplianceSsid_1**](SsidsApi.md#updateNetworkApplianceSsid_1) | **PUT** /networks/{networkId}/appliance/ssids/{number} | Update the attributes of an MX SSID |
| [**updateNetworkWirelessSsidBonjourForwarding_1**](SsidsApi.md#updateNetworkWirelessSsidBonjourForwarding_1) | **PUT** /networks/{networkId}/wireless/ssids/{number}/bonjourForwarding | Update the bonjour forwarding setting and rules for the SSID |
| [**updateNetworkWirelessSsidDeviceTypeGroupPolicies_1**](SsidsApi.md#updateNetworkWirelessSsidDeviceTypeGroupPolicies_1) | **PUT** /networks/{networkId}/wireless/ssids/{number}/deviceTypeGroupPolicies | Update the device type group policies for the SSID |
| [**updateNetworkWirelessSsidEapOverride_1**](SsidsApi.md#updateNetworkWirelessSsidEapOverride_1) | **PUT** /networks/{networkId}/wireless/ssids/{number}/eapOverride | Update the EAP overridden parameters for an SSID. |
| [**updateNetworkWirelessSsidFirewallL3FirewallRules_1**](SsidsApi.md#updateNetworkWirelessSsidFirewallL3FirewallRules_1) | **PUT** /networks/{networkId}/wireless/ssids/{number}/firewall/l3FirewallRules | Update the L3 firewall rules of an SSID on an MR network |
| [**updateNetworkWirelessSsidFirewallL7FirewallRules_1**](SsidsApi.md#updateNetworkWirelessSsidFirewallL7FirewallRules_1) | **PUT** /networks/{networkId}/wireless/ssids/{number}/firewall/l7FirewallRules | Update the L7 firewall rules of an SSID on an MR network |
| [**updateNetworkWirelessSsidHotspot20_1**](SsidsApi.md#updateNetworkWirelessSsidHotspot20_1) | **PUT** /networks/{networkId}/wireless/ssids/{number}/hotspot20 | Update the Hotspot 2.0 settings of an SSID |
| [**updateNetworkWirelessSsidIdentityPsk_1**](SsidsApi.md#updateNetworkWirelessSsidIdentityPsk_1) | **PUT** /networks/{networkId}/wireless/ssids/{number}/identityPsks/{identityPskId} | Update an Identity PSK |
| [**updateNetworkWirelessSsidSchedules_1**](SsidsApi.md#updateNetworkWirelessSsidSchedules_1) | **PUT** /networks/{networkId}/wireless/ssids/{number}/schedules | Update the outage schedule for the SSID |
| [**updateNetworkWirelessSsidSplashSettings_1**](SsidsApi.md#updateNetworkWirelessSsidSplashSettings_1) | **PUT** /networks/{networkId}/wireless/ssids/{number}/splash/settings | Modify the splash page settings for the given SSID |
| [**updateNetworkWirelessSsidTrafficShapingRules_1**](SsidsApi.md#updateNetworkWirelessSsidTrafficShapingRules_1) | **PUT** /networks/{networkId}/wireless/ssids/{number}/trafficShaping/rules | Update the traffic shaping settings for an SSID on an MR network |
| [**updateNetworkWirelessSsidVpn_1**](SsidsApi.md#updateNetworkWirelessSsidVpn_1) | **PUT** /networks/{networkId}/wireless/ssids/{number}/vpn | Update the VPN settings for the SSID |
| [**updateNetworkWirelessSsid_1**](SsidsApi.md#updateNetworkWirelessSsid_1) | **PUT** /networks/{networkId}/wireless/ssids/{number} | Update the attributes of an MR SSID |


<a id="createNetworkWirelessSsidIdentityPsk_1"></a>
# **createNetworkWirelessSsidIdentityPsk_1**
> Object createNetworkWirelessSsidIdentityPsk_1(networkId, number, createNetworkWirelessSsidIdentityPskRequest)

Create an Identity PSK

Create an Identity PSK

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SsidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SsidsApi apiInstance = new SsidsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    CreateNetworkWirelessSsidIdentityPskRequest createNetworkWirelessSsidIdentityPskRequest = new CreateNetworkWirelessSsidIdentityPskRequest(); // CreateNetworkWirelessSsidIdentityPskRequest | 
    try {
      Object result = apiInstance.createNetworkWirelessSsidIdentityPsk_1(networkId, number, createNetworkWirelessSsidIdentityPskRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsidsApi#createNetworkWirelessSsidIdentityPsk_1");
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
| **createNetworkWirelessSsidIdentityPskRequest** | [**CreateNetworkWirelessSsidIdentityPskRequest**](CreateNetworkWirelessSsidIdentityPskRequest.md)|  | |

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

<a id="deleteNetworkWirelessSsidIdentityPsk_1"></a>
# **deleteNetworkWirelessSsidIdentityPsk_1**
> deleteNetworkWirelessSsidIdentityPsk_1(networkId, number, identityPskId)

Delete an Identity PSK

Delete an Identity PSK

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SsidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SsidsApi apiInstance = new SsidsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    String identityPskId = "identityPskId_example"; // String | 
    try {
      apiInstance.deleteNetworkWirelessSsidIdentityPsk_1(networkId, number, identityPskId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsidsApi#deleteNetworkWirelessSsidIdentityPsk_1");
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
| **identityPskId** | **String**|  | |

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

<a id="getNetworkApplianceSsid_1"></a>
# **getNetworkApplianceSsid_1**
> GetNetworkApplianceSsids200ResponseInner getNetworkApplianceSsid_1(networkId, number)

Return a single MX SSID

Return a single MX SSID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SsidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SsidsApi apiInstance = new SsidsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    try {
      GetNetworkApplianceSsids200ResponseInner result = apiInstance.getNetworkApplianceSsid_1(networkId, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsidsApi#getNetworkApplianceSsid_1");
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

[**GetNetworkApplianceSsids200ResponseInner**](GetNetworkApplianceSsids200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceSsids_1"></a>
# **getNetworkApplianceSsids_1**
> List&lt;GetNetworkApplianceSsids200ResponseInner&gt; getNetworkApplianceSsids_1(networkId)

List the MX SSIDs in a network

List the MX SSIDs in a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SsidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SsidsApi apiInstance = new SsidsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<GetNetworkApplianceSsids200ResponseInner> result = apiInstance.getNetworkApplianceSsids_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsidsApi#getNetworkApplianceSsids_1");
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

[**List&lt;GetNetworkApplianceSsids200ResponseInner&gt;**](GetNetworkApplianceSsids200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkWirelessSsidBonjourForwarding_1"></a>
# **getNetworkWirelessSsidBonjourForwarding_1**
> Object getNetworkWirelessSsidBonjourForwarding_1(networkId, number)

List the Bonjour forwarding setting and rules for the SSID

List the Bonjour forwarding setting and rules for the SSID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SsidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SsidsApi apiInstance = new SsidsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    try {
      Object result = apiInstance.getNetworkWirelessSsidBonjourForwarding_1(networkId, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsidsApi#getNetworkWirelessSsidBonjourForwarding_1");
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

<a id="getNetworkWirelessSsidDeviceTypeGroupPolicies_1"></a>
# **getNetworkWirelessSsidDeviceTypeGroupPolicies_1**
> Object getNetworkWirelessSsidDeviceTypeGroupPolicies_1(networkId, number)

List the device type group policies for the SSID

List the device type group policies for the SSID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SsidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SsidsApi apiInstance = new SsidsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    try {
      Object result = apiInstance.getNetworkWirelessSsidDeviceTypeGroupPolicies_1(networkId, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsidsApi#getNetworkWirelessSsidDeviceTypeGroupPolicies_1");
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

<a id="getNetworkWirelessSsidEapOverride_1"></a>
# **getNetworkWirelessSsidEapOverride_1**
> GetNetworkWirelessSsidEapOverride200Response getNetworkWirelessSsidEapOverride_1(networkId, number)

Return the EAP overridden parameters for an SSID

Return the EAP overridden parameters for an SSID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SsidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SsidsApi apiInstance = new SsidsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    try {
      GetNetworkWirelessSsidEapOverride200Response result = apiInstance.getNetworkWirelessSsidEapOverride_1(networkId, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsidsApi#getNetworkWirelessSsidEapOverride_1");
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

[**GetNetworkWirelessSsidEapOverride200Response**](GetNetworkWirelessSsidEapOverride200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkWirelessSsidFirewallL3FirewallRules_1"></a>
# **getNetworkWirelessSsidFirewallL3FirewallRules_1**
> Object getNetworkWirelessSsidFirewallL3FirewallRules_1(networkId, number)

Return the L3 firewall rules for an SSID on an MR network

Return the L3 firewall rules for an SSID on an MR network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SsidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SsidsApi apiInstance = new SsidsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    try {
      Object result = apiInstance.getNetworkWirelessSsidFirewallL3FirewallRules_1(networkId, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsidsApi#getNetworkWirelessSsidFirewallL3FirewallRules_1");
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

<a id="getNetworkWirelessSsidFirewallL7FirewallRules_1"></a>
# **getNetworkWirelessSsidFirewallL7FirewallRules_1**
> Object getNetworkWirelessSsidFirewallL7FirewallRules_1(networkId, number)

Return the L7 firewall rules for an SSID on an MR network

Return the L7 firewall rules for an SSID on an MR network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SsidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SsidsApi apiInstance = new SsidsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    try {
      Object result = apiInstance.getNetworkWirelessSsidFirewallL7FirewallRules_1(networkId, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsidsApi#getNetworkWirelessSsidFirewallL7FirewallRules_1");
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

<a id="getNetworkWirelessSsidHotspot20_1"></a>
# **getNetworkWirelessSsidHotspot20_1**
> Object getNetworkWirelessSsidHotspot20_1(networkId, number)

Return the Hotspot 2.0 settings for an SSID

Return the Hotspot 2.0 settings for an SSID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SsidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SsidsApi apiInstance = new SsidsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    try {
      Object result = apiInstance.getNetworkWirelessSsidHotspot20_1(networkId, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsidsApi#getNetworkWirelessSsidHotspot20_1");
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

<a id="getNetworkWirelessSsidIdentityPsk_1"></a>
# **getNetworkWirelessSsidIdentityPsk_1**
> GetNetworkWirelessSsidIdentityPsks200ResponseInner getNetworkWirelessSsidIdentityPsk_1(networkId, number, identityPskId)

Return an Identity PSK

Return an Identity PSK

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SsidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SsidsApi apiInstance = new SsidsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    String identityPskId = "identityPskId_example"; // String | 
    try {
      GetNetworkWirelessSsidIdentityPsks200ResponseInner result = apiInstance.getNetworkWirelessSsidIdentityPsk_1(networkId, number, identityPskId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsidsApi#getNetworkWirelessSsidIdentityPsk_1");
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
| **identityPskId** | **String**|  | |

### Return type

[**GetNetworkWirelessSsidIdentityPsks200ResponseInner**](GetNetworkWirelessSsidIdentityPsks200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkWirelessSsidIdentityPsks_1"></a>
# **getNetworkWirelessSsidIdentityPsks_1**
> List&lt;GetNetworkWirelessSsidIdentityPsks200ResponseInner&gt; getNetworkWirelessSsidIdentityPsks_1(networkId, number)

List all Identity PSKs in a wireless network

List all Identity PSKs in a wireless network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SsidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SsidsApi apiInstance = new SsidsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    try {
      List<GetNetworkWirelessSsidIdentityPsks200ResponseInner> result = apiInstance.getNetworkWirelessSsidIdentityPsks_1(networkId, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsidsApi#getNetworkWirelessSsidIdentityPsks_1");
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

[**List&lt;GetNetworkWirelessSsidIdentityPsks200ResponseInner&gt;**](GetNetworkWirelessSsidIdentityPsks200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkWirelessSsidSchedules_1"></a>
# **getNetworkWirelessSsidSchedules_1**
> Object getNetworkWirelessSsidSchedules_1(networkId, number)

List the outage schedule for the SSID

List the outage schedule for the SSID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SsidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SsidsApi apiInstance = new SsidsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    try {
      Object result = apiInstance.getNetworkWirelessSsidSchedules_1(networkId, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsidsApi#getNetworkWirelessSsidSchedules_1");
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

<a id="getNetworkWirelessSsidSplashSettings_1"></a>
# **getNetworkWirelessSsidSplashSettings_1**
> GetNetworkWirelessSsidSplashSettings200Response getNetworkWirelessSsidSplashSettings_1(networkId, number)

Display the splash page settings for the given SSID

Display the splash page settings for the given SSID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SsidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SsidsApi apiInstance = new SsidsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    try {
      GetNetworkWirelessSsidSplashSettings200Response result = apiInstance.getNetworkWirelessSsidSplashSettings_1(networkId, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsidsApi#getNetworkWirelessSsidSplashSettings_1");
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

[**GetNetworkWirelessSsidSplashSettings200Response**](GetNetworkWirelessSsidSplashSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkWirelessSsidTrafficShapingRules_1"></a>
# **getNetworkWirelessSsidTrafficShapingRules_1**
> Object getNetworkWirelessSsidTrafficShapingRules_1(networkId, number)

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
import org.openapitools.client.api.SsidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SsidsApi apiInstance = new SsidsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    try {
      Object result = apiInstance.getNetworkWirelessSsidTrafficShapingRules_1(networkId, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsidsApi#getNetworkWirelessSsidTrafficShapingRules_1");
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

<a id="getNetworkWirelessSsidVpn_1"></a>
# **getNetworkWirelessSsidVpn_1**
> Object getNetworkWirelessSsidVpn_1(networkId, number)

List the VPN settings for the SSID.

List the VPN settings for the SSID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SsidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SsidsApi apiInstance = new SsidsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    try {
      Object result = apiInstance.getNetworkWirelessSsidVpn_1(networkId, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsidsApi#getNetworkWirelessSsidVpn_1");
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

<a id="getNetworkWirelessSsid_1"></a>
# **getNetworkWirelessSsid_1**
> Object getNetworkWirelessSsid_1(networkId, number)

Return a single MR SSID

Return a single MR SSID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SsidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SsidsApi apiInstance = new SsidsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    try {
      Object result = apiInstance.getNetworkWirelessSsid_1(networkId, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsidsApi#getNetworkWirelessSsid_1");
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

<a id="getNetworkWirelessSsids_1"></a>
# **getNetworkWirelessSsids_1**
> List&lt;Object&gt; getNetworkWirelessSsids_1(networkId)

List the MR SSIDs in a network

List the MR SSIDs in a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SsidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SsidsApi apiInstance = new SsidsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkWirelessSsids_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsidsApi#getNetworkWirelessSsids_1");
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

<a id="getOrganizationSummaryTopSsidsByUsage_3"></a>
# **getOrganizationSummaryTopSsidsByUsage_3**
> List&lt;GetOrganizationSummaryTopSsidsByUsage200ResponseInner&gt; getOrganizationSummaryTopSsidsByUsage_3(organizationId, t0, t1, timespan)

Return metrics for organization&#39;s top 10 ssids by data usage over given time range

Return metrics for organization&#39;s top 10 ssids by data usage over given time range. Default unit is megabytes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SsidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SsidsApi apiInstance = new SsidsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    try {
      List<GetOrganizationSummaryTopSsidsByUsage200ResponseInner> result = apiInstance.getOrganizationSummaryTopSsidsByUsage_3(organizationId, t0, t1, timespan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsidsApi#getOrganizationSummaryTopSsidsByUsage_3");
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
| **t0** | **String**| The beginning of the timespan for the data. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. | [optional] |

### Return type

[**List&lt;GetOrganizationSummaryTopSsidsByUsage200ResponseInner&gt;**](GetOrganizationSummaryTopSsidsByUsage200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceSsid_1"></a>
# **updateNetworkApplianceSsid_1**
> GetNetworkApplianceSsids200ResponseInner updateNetworkApplianceSsid_1(networkId, number, updateNetworkApplianceSsidRequest)

Update the attributes of an MX SSID

Update the attributes of an MX SSID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SsidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SsidsApi apiInstance = new SsidsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    UpdateNetworkApplianceSsidRequest updateNetworkApplianceSsidRequest = new UpdateNetworkApplianceSsidRequest(); // UpdateNetworkApplianceSsidRequest | 
    try {
      GetNetworkApplianceSsids200ResponseInner result = apiInstance.updateNetworkApplianceSsid_1(networkId, number, updateNetworkApplianceSsidRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsidsApi#updateNetworkApplianceSsid_1");
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
| **updateNetworkApplianceSsidRequest** | [**UpdateNetworkApplianceSsidRequest**](UpdateNetworkApplianceSsidRequest.md)|  | [optional] |

### Return type

[**GetNetworkApplianceSsids200ResponseInner**](GetNetworkApplianceSsids200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkWirelessSsidBonjourForwarding_1"></a>
# **updateNetworkWirelessSsidBonjourForwarding_1**
> Object updateNetworkWirelessSsidBonjourForwarding_1(networkId, number, updateNetworkWirelessSsidBonjourForwardingRequest)

Update the bonjour forwarding setting and rules for the SSID

Update the bonjour forwarding setting and rules for the SSID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SsidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SsidsApi apiInstance = new SsidsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    UpdateNetworkWirelessSsidBonjourForwardingRequest updateNetworkWirelessSsidBonjourForwardingRequest = new UpdateNetworkWirelessSsidBonjourForwardingRequest(); // UpdateNetworkWirelessSsidBonjourForwardingRequest | 
    try {
      Object result = apiInstance.updateNetworkWirelessSsidBonjourForwarding_1(networkId, number, updateNetworkWirelessSsidBonjourForwardingRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsidsApi#updateNetworkWirelessSsidBonjourForwarding_1");
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
| **updateNetworkWirelessSsidBonjourForwardingRequest** | [**UpdateNetworkWirelessSsidBonjourForwardingRequest**](UpdateNetworkWirelessSsidBonjourForwardingRequest.md)|  | [optional] |

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

<a id="updateNetworkWirelessSsidDeviceTypeGroupPolicies_1"></a>
# **updateNetworkWirelessSsidDeviceTypeGroupPolicies_1**
> Object updateNetworkWirelessSsidDeviceTypeGroupPolicies_1(networkId, number, updateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest)

Update the device type group policies for the SSID

Update the device type group policies for the SSID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SsidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SsidsApi apiInstance = new SsidsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    UpdateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest updateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest = new UpdateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest(); // UpdateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest | 
    try {
      Object result = apiInstance.updateNetworkWirelessSsidDeviceTypeGroupPolicies_1(networkId, number, updateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsidsApi#updateNetworkWirelessSsidDeviceTypeGroupPolicies_1");
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
| **updateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest** | [**UpdateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest**](UpdateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest.md)|  | [optional] |

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

<a id="updateNetworkWirelessSsidEapOverride_1"></a>
# **updateNetworkWirelessSsidEapOverride_1**
> GetNetworkWirelessSsidEapOverride200Response updateNetworkWirelessSsidEapOverride_1(networkId, number, updateNetworkWirelessSsidEapOverrideRequest)

Update the EAP overridden parameters for an SSID.

Update the EAP overridden parameters for an SSID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SsidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SsidsApi apiInstance = new SsidsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    UpdateNetworkWirelessSsidEapOverrideRequest updateNetworkWirelessSsidEapOverrideRequest = new UpdateNetworkWirelessSsidEapOverrideRequest(); // UpdateNetworkWirelessSsidEapOverrideRequest | 
    try {
      GetNetworkWirelessSsidEapOverride200Response result = apiInstance.updateNetworkWirelessSsidEapOverride_1(networkId, number, updateNetworkWirelessSsidEapOverrideRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsidsApi#updateNetworkWirelessSsidEapOverride_1");
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
| **updateNetworkWirelessSsidEapOverrideRequest** | [**UpdateNetworkWirelessSsidEapOverrideRequest**](UpdateNetworkWirelessSsidEapOverrideRequest.md)|  | [optional] |

### Return type

[**GetNetworkWirelessSsidEapOverride200Response**](GetNetworkWirelessSsidEapOverride200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkWirelessSsidFirewallL3FirewallRules_1"></a>
# **updateNetworkWirelessSsidFirewallL3FirewallRules_1**
> Object updateNetworkWirelessSsidFirewallL3FirewallRules_1(networkId, number, updateNetworkWirelessSsidFirewallL3FirewallRulesRequest)

Update the L3 firewall rules of an SSID on an MR network

Update the L3 firewall rules of an SSID on an MR network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SsidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SsidsApi apiInstance = new SsidsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest updateNetworkWirelessSsidFirewallL3FirewallRulesRequest = new UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest(); // UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest | 
    try {
      Object result = apiInstance.updateNetworkWirelessSsidFirewallL3FirewallRules_1(networkId, number, updateNetworkWirelessSsidFirewallL3FirewallRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsidsApi#updateNetworkWirelessSsidFirewallL3FirewallRules_1");
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
| **updateNetworkWirelessSsidFirewallL3FirewallRulesRequest** | [**UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest**](UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest.md)|  | [optional] |

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

<a id="updateNetworkWirelessSsidFirewallL7FirewallRules_1"></a>
# **updateNetworkWirelessSsidFirewallL7FirewallRules_1**
> Object updateNetworkWirelessSsidFirewallL7FirewallRules_1(networkId, number, updateNetworkWirelessSsidFirewallL7FirewallRulesRequest)

Update the L7 firewall rules of an SSID on an MR network

Update the L7 firewall rules of an SSID on an MR network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SsidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SsidsApi apiInstance = new SsidsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest updateNetworkWirelessSsidFirewallL7FirewallRulesRequest = new UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest(); // UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest | 
    try {
      Object result = apiInstance.updateNetworkWirelessSsidFirewallL7FirewallRules_1(networkId, number, updateNetworkWirelessSsidFirewallL7FirewallRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsidsApi#updateNetworkWirelessSsidFirewallL7FirewallRules_1");
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
| **updateNetworkWirelessSsidFirewallL7FirewallRulesRequest** | [**UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest**](UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest.md)|  | [optional] |

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

<a id="updateNetworkWirelessSsidHotspot20_1"></a>
# **updateNetworkWirelessSsidHotspot20_1**
> Object updateNetworkWirelessSsidHotspot20_1(networkId, number, updateNetworkWirelessSsidHotspot20Request)

Update the Hotspot 2.0 settings of an SSID

Update the Hotspot 2.0 settings of an SSID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SsidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SsidsApi apiInstance = new SsidsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    UpdateNetworkWirelessSsidHotspot20Request updateNetworkWirelessSsidHotspot20Request = new UpdateNetworkWirelessSsidHotspot20Request(); // UpdateNetworkWirelessSsidHotspot20Request | 
    try {
      Object result = apiInstance.updateNetworkWirelessSsidHotspot20_1(networkId, number, updateNetworkWirelessSsidHotspot20Request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsidsApi#updateNetworkWirelessSsidHotspot20_1");
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
| **updateNetworkWirelessSsidHotspot20Request** | [**UpdateNetworkWirelessSsidHotspot20Request**](UpdateNetworkWirelessSsidHotspot20Request.md)|  | [optional] |

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

<a id="updateNetworkWirelessSsidIdentityPsk_1"></a>
# **updateNetworkWirelessSsidIdentityPsk_1**
> Object updateNetworkWirelessSsidIdentityPsk_1(networkId, number, identityPskId, updateNetworkWirelessSsidIdentityPskRequest)

Update an Identity PSK

Update an Identity PSK

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SsidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SsidsApi apiInstance = new SsidsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    String identityPskId = "identityPskId_example"; // String | 
    UpdateNetworkWirelessSsidIdentityPskRequest updateNetworkWirelessSsidIdentityPskRequest = new UpdateNetworkWirelessSsidIdentityPskRequest(); // UpdateNetworkWirelessSsidIdentityPskRequest | 
    try {
      Object result = apiInstance.updateNetworkWirelessSsidIdentityPsk_1(networkId, number, identityPskId, updateNetworkWirelessSsidIdentityPskRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsidsApi#updateNetworkWirelessSsidIdentityPsk_1");
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
| **identityPskId** | **String**|  | |
| **updateNetworkWirelessSsidIdentityPskRequest** | [**UpdateNetworkWirelessSsidIdentityPskRequest**](UpdateNetworkWirelessSsidIdentityPskRequest.md)|  | [optional] |

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

<a id="updateNetworkWirelessSsidSchedules_1"></a>
# **updateNetworkWirelessSsidSchedules_1**
> Object updateNetworkWirelessSsidSchedules_1(networkId, number, updateNetworkWirelessSsidSchedulesRequest)

Update the outage schedule for the SSID

Update the outage schedule for the SSID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SsidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SsidsApi apiInstance = new SsidsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    UpdateNetworkWirelessSsidSchedulesRequest updateNetworkWirelessSsidSchedulesRequest = new UpdateNetworkWirelessSsidSchedulesRequest(); // UpdateNetworkWirelessSsidSchedulesRequest | 
    try {
      Object result = apiInstance.updateNetworkWirelessSsidSchedules_1(networkId, number, updateNetworkWirelessSsidSchedulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsidsApi#updateNetworkWirelessSsidSchedules_1");
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
| **updateNetworkWirelessSsidSchedulesRequest** | [**UpdateNetworkWirelessSsidSchedulesRequest**](UpdateNetworkWirelessSsidSchedulesRequest.md)|  | [optional] |

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

<a id="updateNetworkWirelessSsidSplashSettings_1"></a>
# **updateNetworkWirelessSsidSplashSettings_1**
> GetNetworkWirelessSsidSplashSettings200Response updateNetworkWirelessSsidSplashSettings_1(networkId, number, updateNetworkWirelessSsidSplashSettingsRequest)

Modify the splash page settings for the given SSID

Modify the splash page settings for the given SSID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SsidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SsidsApi apiInstance = new SsidsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    UpdateNetworkWirelessSsidSplashSettingsRequest updateNetworkWirelessSsidSplashSettingsRequest = new UpdateNetworkWirelessSsidSplashSettingsRequest(); // UpdateNetworkWirelessSsidSplashSettingsRequest | 
    try {
      GetNetworkWirelessSsidSplashSettings200Response result = apiInstance.updateNetworkWirelessSsidSplashSettings_1(networkId, number, updateNetworkWirelessSsidSplashSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsidsApi#updateNetworkWirelessSsidSplashSettings_1");
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
| **updateNetworkWirelessSsidSplashSettingsRequest** | [**UpdateNetworkWirelessSsidSplashSettingsRequest**](UpdateNetworkWirelessSsidSplashSettingsRequest.md)|  | [optional] |

### Return type

[**GetNetworkWirelessSsidSplashSettings200Response**](GetNetworkWirelessSsidSplashSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkWirelessSsidTrafficShapingRules_1"></a>
# **updateNetworkWirelessSsidTrafficShapingRules_1**
> Object updateNetworkWirelessSsidTrafficShapingRules_1(networkId, number, updateNetworkWirelessSsidTrafficShapingRulesRequest)

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
import org.openapitools.client.api.SsidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SsidsApi apiInstance = new SsidsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    UpdateNetworkWirelessSsidTrafficShapingRulesRequest updateNetworkWirelessSsidTrafficShapingRulesRequest = new UpdateNetworkWirelessSsidTrafficShapingRulesRequest(); // UpdateNetworkWirelessSsidTrafficShapingRulesRequest | 
    try {
      Object result = apiInstance.updateNetworkWirelessSsidTrafficShapingRules_1(networkId, number, updateNetworkWirelessSsidTrafficShapingRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsidsApi#updateNetworkWirelessSsidTrafficShapingRules_1");
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

<a id="updateNetworkWirelessSsidVpn_1"></a>
# **updateNetworkWirelessSsidVpn_1**
> Object updateNetworkWirelessSsidVpn_1(networkId, number, updateNetworkWirelessSsidVpnRequest)

Update the VPN settings for the SSID

Update the VPN settings for the SSID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SsidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SsidsApi apiInstance = new SsidsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    UpdateNetworkWirelessSsidVpnRequest updateNetworkWirelessSsidVpnRequest = new UpdateNetworkWirelessSsidVpnRequest(); // UpdateNetworkWirelessSsidVpnRequest | 
    try {
      Object result = apiInstance.updateNetworkWirelessSsidVpn_1(networkId, number, updateNetworkWirelessSsidVpnRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsidsApi#updateNetworkWirelessSsidVpn_1");
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
| **updateNetworkWirelessSsidVpnRequest** | [**UpdateNetworkWirelessSsidVpnRequest**](UpdateNetworkWirelessSsidVpnRequest.md)|  | [optional] |

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

<a id="updateNetworkWirelessSsid_1"></a>
# **updateNetworkWirelessSsid_1**
> Object updateNetworkWirelessSsid_1(networkId, number, updateNetworkWirelessSsidRequest)

Update the attributes of an MR SSID

Update the attributes of an MR SSID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SsidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SsidsApi apiInstance = new SsidsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    UpdateNetworkWirelessSsidRequest updateNetworkWirelessSsidRequest = new UpdateNetworkWirelessSsidRequest(); // UpdateNetworkWirelessSsidRequest | 
    try {
      Object result = apiInstance.updateNetworkWirelessSsid_1(networkId, number, updateNetworkWirelessSsidRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SsidsApi#updateNetworkWirelessSsid_1");
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
| **updateNetworkWirelessSsidRequest** | [**UpdateNetworkWirelessSsidRequest**](UpdateNetworkWirelessSsidRequest.md)|  | [optional] |

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

