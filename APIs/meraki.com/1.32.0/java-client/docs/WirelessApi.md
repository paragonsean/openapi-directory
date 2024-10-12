# WirelessApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkWirelessRfProfile**](WirelessApi.md#createNetworkWirelessRfProfile) | **POST** /networks/{networkId}/wireless/rfProfiles | Creates new RF profile for this network |
| [**createNetworkWirelessSsidIdentityPsk**](WirelessApi.md#createNetworkWirelessSsidIdentityPsk) | **POST** /networks/{networkId}/wireless/ssids/{number}/identityPsks | Create an Identity PSK |
| [**deleteNetworkWirelessRfProfile**](WirelessApi.md#deleteNetworkWirelessRfProfile) | **DELETE** /networks/{networkId}/wireless/rfProfiles/{rfProfileId} | Delete a RF Profile |
| [**deleteNetworkWirelessSsidIdentityPsk**](WirelessApi.md#deleteNetworkWirelessSsidIdentityPsk) | **DELETE** /networks/{networkId}/wireless/ssids/{number}/identityPsks/{identityPskId} | Delete an Identity PSK |
| [**getDeviceWirelessBluetoothSettings**](WirelessApi.md#getDeviceWirelessBluetoothSettings) | **GET** /devices/{serial}/wireless/bluetooth/settings | Return the bluetooth settings for a wireless device |
| [**getDeviceWirelessConnectionStats**](WirelessApi.md#getDeviceWirelessConnectionStats) | **GET** /devices/{serial}/wireless/connectionStats | Aggregated connectivity info for a given AP on this network |
| [**getDeviceWirelessLatencyStats**](WirelessApi.md#getDeviceWirelessLatencyStats) | **GET** /devices/{serial}/wireless/latencyStats | Aggregated latency info for a given AP on this network |
| [**getDeviceWirelessRadioSettings**](WirelessApi.md#getDeviceWirelessRadioSettings) | **GET** /devices/{serial}/wireless/radio/settings | Return the radio settings of a device |
| [**getDeviceWirelessStatus**](WirelessApi.md#getDeviceWirelessStatus) | **GET** /devices/{serial}/wireless/status | Return the SSID statuses of an access point |
| [**getNetworkWirelessAirMarshal**](WirelessApi.md#getNetworkWirelessAirMarshal) | **GET** /networks/{networkId}/wireless/airMarshal | List Air Marshal scan results from a network |
| [**getNetworkWirelessAlternateManagementInterface**](WirelessApi.md#getNetworkWirelessAlternateManagementInterface) | **GET** /networks/{networkId}/wireless/alternateManagementInterface | Return alternate management interface and devices with IP assigned |
| [**getNetworkWirelessBilling**](WirelessApi.md#getNetworkWirelessBilling) | **GET** /networks/{networkId}/wireless/billing | Return the billing settings of this network |
| [**getNetworkWirelessBluetoothSettings**](WirelessApi.md#getNetworkWirelessBluetoothSettings) | **GET** /networks/{networkId}/wireless/bluetooth/settings | Return the Bluetooth settings for a network. &lt;a href&#x3D;\&quot;https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\&quot;&gt;Bluetooth settings&lt;/a&gt; must be enabled on the network. |
| [**getNetworkWirelessChannelUtilizationHistory**](WirelessApi.md#getNetworkWirelessChannelUtilizationHistory) | **GET** /networks/{networkId}/wireless/channelUtilizationHistory | Return AP channel utilization over time for a device or network client |
| [**getNetworkWirelessClientConnectionStats**](WirelessApi.md#getNetworkWirelessClientConnectionStats) | **GET** /networks/{networkId}/wireless/clients/{clientId}/connectionStats | Aggregated connectivity info for a given client on this network |
| [**getNetworkWirelessClientConnectivityEvents**](WirelessApi.md#getNetworkWirelessClientConnectivityEvents) | **GET** /networks/{networkId}/wireless/clients/{clientId}/connectivityEvents | List the wireless connectivity events for a client within a network in the timespan. |
| [**getNetworkWirelessClientCountHistory**](WirelessApi.md#getNetworkWirelessClientCountHistory) | **GET** /networks/{networkId}/wireless/clientCountHistory | Return wireless client counts over time for a network, device, or network client |
| [**getNetworkWirelessClientLatencyHistory**](WirelessApi.md#getNetworkWirelessClientLatencyHistory) | **GET** /networks/{networkId}/wireless/clients/{clientId}/latencyHistory | Return the latency history for a client |
| [**getNetworkWirelessClientLatencyStats**](WirelessApi.md#getNetworkWirelessClientLatencyStats) | **GET** /networks/{networkId}/wireless/clients/{clientId}/latencyStats | Aggregated latency info for a given client on this network |
| [**getNetworkWirelessClientsConnectionStats**](WirelessApi.md#getNetworkWirelessClientsConnectionStats) | **GET** /networks/{networkId}/wireless/clients/connectionStats | Aggregated connectivity info for this network, grouped by clients |
| [**getNetworkWirelessClientsLatencyStats**](WirelessApi.md#getNetworkWirelessClientsLatencyStats) | **GET** /networks/{networkId}/wireless/clients/latencyStats | Aggregated latency info for this network, grouped by clients |
| [**getNetworkWirelessConnectionStats**](WirelessApi.md#getNetworkWirelessConnectionStats) | **GET** /networks/{networkId}/wireless/connectionStats | Aggregated connectivity info for this network |
| [**getNetworkWirelessDataRateHistory**](WirelessApi.md#getNetworkWirelessDataRateHistory) | **GET** /networks/{networkId}/wireless/dataRateHistory | Return PHY data rates over time for a network, device, or network client |
| [**getNetworkWirelessDevicesConnectionStats**](WirelessApi.md#getNetworkWirelessDevicesConnectionStats) | **GET** /networks/{networkId}/wireless/devices/connectionStats | Aggregated connectivity info for this network, grouped by node |
| [**getNetworkWirelessDevicesLatencyStats**](WirelessApi.md#getNetworkWirelessDevicesLatencyStats) | **GET** /networks/{networkId}/wireless/devices/latencyStats | Aggregated latency info for this network, grouped by node |
| [**getNetworkWirelessFailedConnections**](WirelessApi.md#getNetworkWirelessFailedConnections) | **GET** /networks/{networkId}/wireless/failedConnections | List of all failed client connection events on this network in a given time range |
| [**getNetworkWirelessLatencyHistory**](WirelessApi.md#getNetworkWirelessLatencyHistory) | **GET** /networks/{networkId}/wireless/latencyHistory | Return average wireless latency over time for a network, device, or network client |
| [**getNetworkWirelessLatencyStats**](WirelessApi.md#getNetworkWirelessLatencyStats) | **GET** /networks/{networkId}/wireless/latencyStats | Aggregated latency info for this network |
| [**getNetworkWirelessMeshStatuses**](WirelessApi.md#getNetworkWirelessMeshStatuses) | **GET** /networks/{networkId}/wireless/meshStatuses | List wireless mesh statuses for repeaters |
| [**getNetworkWirelessRfProfile**](WirelessApi.md#getNetworkWirelessRfProfile) | **GET** /networks/{networkId}/wireless/rfProfiles/{rfProfileId} | Return a RF profile |
| [**getNetworkWirelessRfProfiles**](WirelessApi.md#getNetworkWirelessRfProfiles) | **GET** /networks/{networkId}/wireless/rfProfiles | List the non-basic RF profiles for this network |
| [**getNetworkWirelessSettings**](WirelessApi.md#getNetworkWirelessSettings) | **GET** /networks/{networkId}/wireless/settings | Return the wireless settings for a network |
| [**getNetworkWirelessSignalQualityHistory**](WirelessApi.md#getNetworkWirelessSignalQualityHistory) | **GET** /networks/{networkId}/wireless/signalQualityHistory | Return signal quality (SNR/RSSI) over time for a device or network client |
| [**getNetworkWirelessSsid**](WirelessApi.md#getNetworkWirelessSsid) | **GET** /networks/{networkId}/wireless/ssids/{number} | Return a single MR SSID |
| [**getNetworkWirelessSsidBonjourForwarding**](WirelessApi.md#getNetworkWirelessSsidBonjourForwarding) | **GET** /networks/{networkId}/wireless/ssids/{number}/bonjourForwarding | List the Bonjour forwarding setting and rules for the SSID |
| [**getNetworkWirelessSsidDeviceTypeGroupPolicies**](WirelessApi.md#getNetworkWirelessSsidDeviceTypeGroupPolicies) | **GET** /networks/{networkId}/wireless/ssids/{number}/deviceTypeGroupPolicies | List the device type group policies for the SSID |
| [**getNetworkWirelessSsidEapOverride**](WirelessApi.md#getNetworkWirelessSsidEapOverride) | **GET** /networks/{networkId}/wireless/ssids/{number}/eapOverride | Return the EAP overridden parameters for an SSID |
| [**getNetworkWirelessSsidFirewallL3FirewallRules**](WirelessApi.md#getNetworkWirelessSsidFirewallL3FirewallRules) | **GET** /networks/{networkId}/wireless/ssids/{number}/firewall/l3FirewallRules | Return the L3 firewall rules for an SSID on an MR network |
| [**getNetworkWirelessSsidFirewallL7FirewallRules**](WirelessApi.md#getNetworkWirelessSsidFirewallL7FirewallRules) | **GET** /networks/{networkId}/wireless/ssids/{number}/firewall/l7FirewallRules | Return the L7 firewall rules for an SSID on an MR network |
| [**getNetworkWirelessSsidHotspot20**](WirelessApi.md#getNetworkWirelessSsidHotspot20) | **GET** /networks/{networkId}/wireless/ssids/{number}/hotspot20 | Return the Hotspot 2.0 settings for an SSID |
| [**getNetworkWirelessSsidIdentityPsk**](WirelessApi.md#getNetworkWirelessSsidIdentityPsk) | **GET** /networks/{networkId}/wireless/ssids/{number}/identityPsks/{identityPskId} | Return an Identity PSK |
| [**getNetworkWirelessSsidIdentityPsks**](WirelessApi.md#getNetworkWirelessSsidIdentityPsks) | **GET** /networks/{networkId}/wireless/ssids/{number}/identityPsks | List all Identity PSKs in a wireless network |
| [**getNetworkWirelessSsidSchedules**](WirelessApi.md#getNetworkWirelessSsidSchedules) | **GET** /networks/{networkId}/wireless/ssids/{number}/schedules | List the outage schedule for the SSID |
| [**getNetworkWirelessSsidSplashSettings**](WirelessApi.md#getNetworkWirelessSsidSplashSettings) | **GET** /networks/{networkId}/wireless/ssids/{number}/splash/settings | Display the splash page settings for the given SSID |
| [**getNetworkWirelessSsidTrafficShapingRules**](WirelessApi.md#getNetworkWirelessSsidTrafficShapingRules) | **GET** /networks/{networkId}/wireless/ssids/{number}/trafficShaping/rules | Display the traffic shaping settings for a SSID on an MR network |
| [**getNetworkWirelessSsidVpn**](WirelessApi.md#getNetworkWirelessSsidVpn) | **GET** /networks/{networkId}/wireless/ssids/{number}/vpn | List the VPN settings for the SSID. |
| [**getNetworkWirelessSsids**](WirelessApi.md#getNetworkWirelessSsids) | **GET** /networks/{networkId}/wireless/ssids | List the MR SSIDs in a network |
| [**getNetworkWirelessUsageHistory**](WirelessApi.md#getNetworkWirelessUsageHistory) | **GET** /networks/{networkId}/wireless/usageHistory | Return AP usage over time for a device or network client |
| [**getOrganizationWirelessDevicesEthernetStatuses**](WirelessApi.md#getOrganizationWirelessDevicesEthernetStatuses) | **GET** /organizations/{organizationId}/wireless/devices/ethernet/statuses | Endpoint to see power status for wireless devices |
| [**updateDeviceWirelessBluetoothSettings**](WirelessApi.md#updateDeviceWirelessBluetoothSettings) | **PUT** /devices/{serial}/wireless/bluetooth/settings | Update the bluetooth settings for a wireless device |
| [**updateDeviceWirelessRadioSettings**](WirelessApi.md#updateDeviceWirelessRadioSettings) | **PUT** /devices/{serial}/wireless/radio/settings | Update the radio settings of a device |
| [**updateNetworkWirelessAlternateManagementInterface**](WirelessApi.md#updateNetworkWirelessAlternateManagementInterface) | **PUT** /networks/{networkId}/wireless/alternateManagementInterface | Update alternate management interface and device static IP |
| [**updateNetworkWirelessBilling**](WirelessApi.md#updateNetworkWirelessBilling) | **PUT** /networks/{networkId}/wireless/billing | Update the billing settings |
| [**updateNetworkWirelessBluetoothSettings**](WirelessApi.md#updateNetworkWirelessBluetoothSettings) | **PUT** /networks/{networkId}/wireless/bluetooth/settings | Update the Bluetooth settings for a network |
| [**updateNetworkWirelessRfProfile**](WirelessApi.md#updateNetworkWirelessRfProfile) | **PUT** /networks/{networkId}/wireless/rfProfiles/{rfProfileId} | Updates specified RF profile for this network |
| [**updateNetworkWirelessSettings**](WirelessApi.md#updateNetworkWirelessSettings) | **PUT** /networks/{networkId}/wireless/settings | Update the wireless settings for a network |
| [**updateNetworkWirelessSsid**](WirelessApi.md#updateNetworkWirelessSsid) | **PUT** /networks/{networkId}/wireless/ssids/{number} | Update the attributes of an MR SSID |
| [**updateNetworkWirelessSsidBonjourForwarding**](WirelessApi.md#updateNetworkWirelessSsidBonjourForwarding) | **PUT** /networks/{networkId}/wireless/ssids/{number}/bonjourForwarding | Update the bonjour forwarding setting and rules for the SSID |
| [**updateNetworkWirelessSsidDeviceTypeGroupPolicies**](WirelessApi.md#updateNetworkWirelessSsidDeviceTypeGroupPolicies) | **PUT** /networks/{networkId}/wireless/ssids/{number}/deviceTypeGroupPolicies | Update the device type group policies for the SSID |
| [**updateNetworkWirelessSsidEapOverride**](WirelessApi.md#updateNetworkWirelessSsidEapOverride) | **PUT** /networks/{networkId}/wireless/ssids/{number}/eapOverride | Update the EAP overridden parameters for an SSID. |
| [**updateNetworkWirelessSsidFirewallL3FirewallRules**](WirelessApi.md#updateNetworkWirelessSsidFirewallL3FirewallRules) | **PUT** /networks/{networkId}/wireless/ssids/{number}/firewall/l3FirewallRules | Update the L3 firewall rules of an SSID on an MR network |
| [**updateNetworkWirelessSsidFirewallL7FirewallRules**](WirelessApi.md#updateNetworkWirelessSsidFirewallL7FirewallRules) | **PUT** /networks/{networkId}/wireless/ssids/{number}/firewall/l7FirewallRules | Update the L7 firewall rules of an SSID on an MR network |
| [**updateNetworkWirelessSsidHotspot20**](WirelessApi.md#updateNetworkWirelessSsidHotspot20) | **PUT** /networks/{networkId}/wireless/ssids/{number}/hotspot20 | Update the Hotspot 2.0 settings of an SSID |
| [**updateNetworkWirelessSsidIdentityPsk**](WirelessApi.md#updateNetworkWirelessSsidIdentityPsk) | **PUT** /networks/{networkId}/wireless/ssids/{number}/identityPsks/{identityPskId} | Update an Identity PSK |
| [**updateNetworkWirelessSsidSchedules**](WirelessApi.md#updateNetworkWirelessSsidSchedules) | **PUT** /networks/{networkId}/wireless/ssids/{number}/schedules | Update the outage schedule for the SSID |
| [**updateNetworkWirelessSsidSplashSettings**](WirelessApi.md#updateNetworkWirelessSsidSplashSettings) | **PUT** /networks/{networkId}/wireless/ssids/{number}/splash/settings | Modify the splash page settings for the given SSID |
| [**updateNetworkWirelessSsidTrafficShapingRules**](WirelessApi.md#updateNetworkWirelessSsidTrafficShapingRules) | **PUT** /networks/{networkId}/wireless/ssids/{number}/trafficShaping/rules | Update the traffic shaping settings for an SSID on an MR network |
| [**updateNetworkWirelessSsidVpn**](WirelessApi.md#updateNetworkWirelessSsidVpn) | **PUT** /networks/{networkId}/wireless/ssids/{number}/vpn | Update the VPN settings for the SSID |


<a id="createNetworkWirelessRfProfile"></a>
# **createNetworkWirelessRfProfile**
> CreateNetworkWirelessRfProfile201Response createNetworkWirelessRfProfile(networkId, createNetworkWirelessRfProfileRequest)

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
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkWirelessRfProfileRequest createNetworkWirelessRfProfileRequest = new CreateNetworkWirelessRfProfileRequest(); // CreateNetworkWirelessRfProfileRequest | 
    try {
      CreateNetworkWirelessRfProfile201Response result = apiInstance.createNetworkWirelessRfProfile(networkId, createNetworkWirelessRfProfileRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#createNetworkWirelessRfProfile");
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

<a id="createNetworkWirelessSsidIdentityPsk"></a>
# **createNetworkWirelessSsidIdentityPsk**
> Object createNetworkWirelessSsidIdentityPsk(networkId, number, createNetworkWirelessSsidIdentityPskRequest)

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
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    CreateNetworkWirelessSsidIdentityPskRequest createNetworkWirelessSsidIdentityPskRequest = new CreateNetworkWirelessSsidIdentityPskRequest(); // CreateNetworkWirelessSsidIdentityPskRequest | 
    try {
      Object result = apiInstance.createNetworkWirelessSsidIdentityPsk(networkId, number, createNetworkWirelessSsidIdentityPskRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#createNetworkWirelessSsidIdentityPsk");
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
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String rfProfileId = "rfProfileId_example"; // String | 
    try {
      apiInstance.deleteNetworkWirelessRfProfile(networkId, rfProfileId);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#deleteNetworkWirelessRfProfile");
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

<a id="deleteNetworkWirelessSsidIdentityPsk"></a>
# **deleteNetworkWirelessSsidIdentityPsk**
> deleteNetworkWirelessSsidIdentityPsk(networkId, number, identityPskId)

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
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    String identityPskId = "identityPskId_example"; // String | 
    try {
      apiInstance.deleteNetworkWirelessSsidIdentityPsk(networkId, number, identityPskId);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#deleteNetworkWirelessSsidIdentityPsk");
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

<a id="getDeviceWirelessBluetoothSettings"></a>
# **getDeviceWirelessBluetoothSettings**
> GetDeviceWirelessBluetoothSettings200Response getDeviceWirelessBluetoothSettings(serial)

Return the bluetooth settings for a wireless device

Return the bluetooth settings for a wireless device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      GetDeviceWirelessBluetoothSettings200Response result = apiInstance.getDeviceWirelessBluetoothSettings(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getDeviceWirelessBluetoothSettings");
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

[**GetDeviceWirelessBluetoothSettings200Response**](GetDeviceWirelessBluetoothSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getDeviceWirelessConnectionStats"></a>
# **getDeviceWirelessConnectionStats**
> GetDeviceWirelessConnectionStats200Response getDeviceWirelessConnectionStats(serial, t0, t1, timespan, band, ssid, vlan, apTag)

Aggregated connectivity info for a given AP on this network

Aggregated connectivity info for a given AP on this network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String serial = "serial_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    String band = "2.4"; // String | Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
    Integer ssid = 56; // Integer | Filter results by SSID
    Integer vlan = 56; // Integer | Filter results by VLAN
    String apTag = "apTag_example"; // String | Filter results by AP Tag
    try {
      GetDeviceWirelessConnectionStats200Response result = apiInstance.getDeviceWirelessConnectionStats(serial, t0, t1, timespan, band, ssid, vlan, apTag);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getDeviceWirelessConnectionStats");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] |
| **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information. | [optional] [enum: 2.4, 5, 6] |
| **ssid** | **Integer**| Filter results by SSID | [optional] |
| **vlan** | **Integer**| Filter results by VLAN | [optional] |
| **apTag** | **String**| Filter results by AP Tag | [optional] |

### Return type

[**GetDeviceWirelessConnectionStats200Response**](GetDeviceWirelessConnectionStats200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getDeviceWirelessLatencyStats"></a>
# **getDeviceWirelessLatencyStats**
> Object getDeviceWirelessLatencyStats(serial, t0, t1, timespan, band, ssid, vlan, apTag, fields)

Aggregated latency info for a given AP on this network

Aggregated latency info for a given AP on this network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String serial = "serial_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    String band = "2.4"; // String | Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
    Integer ssid = 56; // Integer | Filter results by SSID
    Integer vlan = 56; // Integer | Filter results by VLAN
    String apTag = "apTag_example"; // String | Filter results by AP Tag
    String fields = "fields_example"; // String | Partial selection: If present, this call will return only the selected fields of [\"rawDistribution\", \"avg\"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
    try {
      Object result = apiInstance.getDeviceWirelessLatencyStats(serial, t0, t1, timespan, band, ssid, vlan, apTag, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getDeviceWirelessLatencyStats");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] |
| **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information. | [optional] [enum: 2.4, 5, 6] |
| **ssid** | **Integer**| Filter results by SSID | [optional] |
| **vlan** | **Integer**| Filter results by VLAN | [optional] |
| **apTag** | **String**| Filter results by AP Tag | [optional] |
| **fields** | **String**| Partial selection: If present, this call will return only the selected fields of [\&quot;rawDistribution\&quot;, \&quot;avg\&quot;]. All fields will be returned by default. Selected fields must be entered as a comma separated string. | [optional] |

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

<a id="getDeviceWirelessRadioSettings"></a>
# **getDeviceWirelessRadioSettings**
> Object getDeviceWirelessRadioSettings(serial)

Return the radio settings of a device

Return the radio settings of a device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      Object result = apiInstance.getDeviceWirelessRadioSettings(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getDeviceWirelessRadioSettings");
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

<a id="getDeviceWirelessStatus"></a>
# **getDeviceWirelessStatus**
> Object getDeviceWirelessStatus(serial)

Return the SSID statuses of an access point

Return the SSID statuses of an access point

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      Object result = apiInstance.getDeviceWirelessStatus(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getDeviceWirelessStatus");
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

<a id="getNetworkWirelessAirMarshal"></a>
# **getNetworkWirelessAirMarshal**
> List&lt;Object&gt; getNetworkWirelessAirMarshal(networkId, t0, timespan)

List Air Marshal scan results from a network

List Air Marshal scan results from a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
    try {
      List<Object> result = apiInstance.getNetworkWirelessAirMarshal(networkId, t0, timespan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessAirMarshal");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 7 days. | [optional] |

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

<a id="getNetworkWirelessAlternateManagementInterface"></a>
# **getNetworkWirelessAlternateManagementInterface**
> Object getNetworkWirelessAlternateManagementInterface(networkId)

Return alternate management interface and devices with IP assigned

Return alternate management interface and devices with IP assigned

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkWirelessAlternateManagementInterface(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessAlternateManagementInterface");
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

<a id="getNetworkWirelessBilling"></a>
# **getNetworkWirelessBilling**
> Object getNetworkWirelessBilling(networkId)

Return the billing settings of this network

Return the billing settings of this network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkWirelessBilling(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessBilling");
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

<a id="getNetworkWirelessBluetoothSettings"></a>
# **getNetworkWirelessBluetoothSettings**
> GetNetworkWirelessBluetoothSettings200Response getNetworkWirelessBluetoothSettings(networkId)

Return the Bluetooth settings for a network. &lt;a href&#x3D;\&quot;https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\&quot;&gt;Bluetooth settings&lt;/a&gt; must be enabled on the network.

Return the Bluetooth settings for a network. &lt;a href&#x3D;\&quot;https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\&quot;&gt;Bluetooth settings&lt;/a&gt; must be enabled on the network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkWirelessBluetoothSettings200Response result = apiInstance.getNetworkWirelessBluetoothSettings(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessBluetoothSettings");
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

[**GetNetworkWirelessBluetoothSettings200Response**](GetNetworkWirelessBluetoothSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkWirelessChannelUtilizationHistory"></a>
# **getNetworkWirelessChannelUtilizationHistory**
> List&lt;GetNetworkWirelessChannelUtilizationHistory200ResponseInner&gt; getNetworkWirelessChannelUtilizationHistory(networkId, t0, t1, timespan, resolution, autoResolution, clientId, deviceSerial, apTag, band)

Return AP channel utilization over time for a device or network client

Return AP channel utilization over time for a device or network client

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
    Integer resolution = 56; // Integer | The time resolution in seconds for returned data. The valid resolutions are: 600, 1200, 3600, 14400, 86400. The default is 86400.
    Boolean autoResolution = true; // Boolean | Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false.
    String clientId = "clientId_example"; // String | Filter results by network client to return per-device, per-band AP channel utilization metrics inner joined by the queried client's connection history.
    String deviceSerial = "deviceSerial_example"; // String | Filter results by device to return AP channel utilization metrics for the queried device; either :band or :clientId must be jointly specified.
    String apTag = "apTag_example"; // String | Filter results by AP tag to return AP channel utilization metrics for devices labeled with the given tag; either :clientId or :deviceSerial must be jointly specified.
    String band = "2.4"; // String | Filter results by band (either '2.4', '5' or '6').
    try {
      List<GetNetworkWirelessChannelUtilizationHistory200ResponseInner> result = apiInstance.getNetworkWirelessChannelUtilizationHistory(networkId, t0, t1, timespan, resolution, autoResolution, clientId, deviceSerial, apTag, band);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessChannelUtilizationHistory");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days. | [optional] |
| **resolution** | **Integer**| The time resolution in seconds for returned data. The valid resolutions are: 600, 1200, 3600, 14400, 86400. The default is 86400. | [optional] |
| **autoResolution** | **Boolean**| Automatically select a data resolution based on the given timespan; this overrides the value specified by the &#39;resolution&#39; parameter. The default setting is false. | [optional] |
| **clientId** | **String**| Filter results by network client to return per-device, per-band AP channel utilization metrics inner joined by the queried client&#39;s connection history. | [optional] |
| **deviceSerial** | **String**| Filter results by device to return AP channel utilization metrics for the queried device; either :band or :clientId must be jointly specified. | [optional] |
| **apTag** | **String**| Filter results by AP tag to return AP channel utilization metrics for devices labeled with the given tag; either :clientId or :deviceSerial must be jointly specified. | [optional] |
| **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). | [optional] [enum: 2.4, 5, 6] |

### Return type

[**List&lt;GetNetworkWirelessChannelUtilizationHistory200ResponseInner&gt;**](GetNetworkWirelessChannelUtilizationHistory200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkWirelessClientConnectionStats"></a>
# **getNetworkWirelessClientConnectionStats**
> Object getNetworkWirelessClientConnectionStats(networkId, clientId, t0, t1, timespan, band, ssid, vlan, apTag)

Aggregated connectivity info for a given client on this network

Aggregated connectivity info for a given client on this network. Clients are identified by their MAC.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String clientId = "clientId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    String band = "2.4"; // String | Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
    Integer ssid = 56; // Integer | Filter results by SSID
    Integer vlan = 56; // Integer | Filter results by VLAN
    String apTag = "apTag_example"; // String | Filter results by AP Tag
    try {
      Object result = apiInstance.getNetworkWirelessClientConnectionStats(networkId, clientId, t0, t1, timespan, band, ssid, vlan, apTag);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessClientConnectionStats");
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
| **clientId** | **String**|  | |
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] |
| **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information. | [optional] [enum: 2.4, 5, 6] |
| **ssid** | **Integer**| Filter results by SSID | [optional] |
| **vlan** | **Integer**| Filter results by VLAN | [optional] |
| **apTag** | **String**| Filter results by AP Tag | [optional] |

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

<a id="getNetworkWirelessClientConnectivityEvents"></a>
# **getNetworkWirelessClientConnectivityEvents**
> List&lt;Object&gt; getNetworkWirelessClientConnectivityEvents(networkId, clientId, perPage, startingAfter, endingBefore, t0, t1, timespan, types, includedSeverities, band, ssidNumber, deviceSerial)

List the wireless connectivity events for a client within a network in the timespan.

List the wireless connectivity events for a client within a network in the timespan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String clientId = "clientId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    List<String> types = Arrays.asList(); // List<String> | A list of event types to include. If not specified, events of all types will be returned. Valid types are 'assoc', 'disassoc', 'auth', 'deauth', 'dns', 'dhcp', 'roam', 'connection' and/or 'sticky'.
    List<String> includedSeverities = Arrays.asList(); // List<String> | A list of severities to include. If not specified, events of all severities will be returned. Valid severities are 'good', 'info', 'warn' and/or 'bad'.
    String band = "2.4"; // String | Filter results by band (either '2.4', '5', '6').
    Integer ssidNumber = 0; // Integer | An SSID number to include. If not specified, events for all SSIDs will be returned.
    String deviceSerial = "deviceSerial_example"; // String | Filter results by an AP's serial number.
    try {
      List<Object> result = apiInstance.getNetworkWirelessClientConnectivityEvents(networkId, clientId, perPage, startingAfter, endingBefore, t0, t1, timespan, types, includedSeverities, band, ssidNumber, deviceSerial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessClientConnectivityEvents");
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
| **clientId** | **String**|  | |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. | [optional] |
| **types** | [**List&lt;String&gt;**](String.md)| A list of event types to include. If not specified, events of all types will be returned. Valid types are &#39;assoc&#39;, &#39;disassoc&#39;, &#39;auth&#39;, &#39;deauth&#39;, &#39;dns&#39;, &#39;dhcp&#39;, &#39;roam&#39;, &#39;connection&#39; and/or &#39;sticky&#39;. | [optional] [enum: assoc, auth, connection, deauth, dhcp, disassoc, dns, roam, sticky] |
| **includedSeverities** | [**List&lt;String&gt;**](String.md)| A list of severities to include. If not specified, events of all severities will be returned. Valid severities are &#39;good&#39;, &#39;info&#39;, &#39;warn&#39; and/or &#39;bad&#39;. | [optional] [enum: bad, good, info, warn] |
| **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39;, &#39;6&#39;). | [optional] [enum: 2.4, 5, 6] |
| **ssidNumber** | **Integer**| An SSID number to include. If not specified, events for all SSIDs will be returned. | [optional] [enum: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] |
| **deviceSerial** | **String**| Filter results by an AP&#39;s serial number. | [optional] |

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
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getNetworkWirelessClientCountHistory"></a>
# **getNetworkWirelessClientCountHistory**
> List&lt;GetNetworkWirelessClientCountHistory200ResponseInner&gt; getNetworkWirelessClientCountHistory(networkId, t0, t1, timespan, resolution, autoResolution, clientId, deviceSerial, apTag, band, ssid)

Return wireless client counts over time for a network, device, or network client

Return wireless client counts over time for a network, device, or network client

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
    Integer resolution = 56; // Integer | The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400.
    Boolean autoResolution = true; // Boolean | Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false.
    String clientId = "clientId_example"; // String | Filter results by network client to return per-device client counts over time inner joined by the queried client's connection history.
    String deviceSerial = "deviceSerial_example"; // String | Filter results by device.
    String apTag = "apTag_example"; // String | Filter results by AP tag.
    String band = "2.4"; // String | Filter results by band (either '2.4', '5' or '6').
    Integer ssid = 56; // Integer | Filter results by SSID number.
    try {
      List<GetNetworkWirelessClientCountHistory200ResponseInner> result = apiInstance.getNetworkWirelessClientCountHistory(networkId, t0, t1, timespan, resolution, autoResolution, clientId, deviceSerial, apTag, band, ssid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessClientCountHistory");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days. | [optional] |
| **resolution** | **Integer**| The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400. | [optional] |
| **autoResolution** | **Boolean**| Automatically select a data resolution based on the given timespan; this overrides the value specified by the &#39;resolution&#39; parameter. The default setting is false. | [optional] |
| **clientId** | **String**| Filter results by network client to return per-device client counts over time inner joined by the queried client&#39;s connection history. | [optional] |
| **deviceSerial** | **String**| Filter results by device. | [optional] |
| **apTag** | **String**| Filter results by AP tag. | [optional] |
| **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). | [optional] [enum: 2.4, 5, 6] |
| **ssid** | **Integer**| Filter results by SSID number. | [optional] |

### Return type

[**List&lt;GetNetworkWirelessClientCountHistory200ResponseInner&gt;**](GetNetworkWirelessClientCountHistory200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkWirelessClientLatencyHistory"></a>
# **getNetworkWirelessClientLatencyHistory**
> List&lt;Object&gt; getNetworkWirelessClientLatencyHistory(networkId, clientId, t0, t1, timespan, resolution)

Return the latency history for a client

Return the latency history for a client. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP. The latency data is from a sample of 2% of packets and is grouped into 4 traffic categories: background, best effort, video, voice. Within these categories the sampled packet counters are bucketed by latency in milliseconds.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String clientId = "clientId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 791 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 791 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 791 days. The default is 1 day.
    Integer resolution = 56; // Integer | The time resolution in seconds for returned data. The valid resolutions are: 86400. The default is 86400.
    try {
      List<Object> result = apiInstance.getNetworkWirelessClientLatencyHistory(networkId, clientId, t0, t1, timespan, resolution);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessClientLatencyHistory");
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
| **clientId** | **String**|  | |
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 791 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 791 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 791 days. The default is 1 day. | [optional] |
| **resolution** | **Integer**| The time resolution in seconds for returned data. The valid resolutions are: 86400. The default is 86400. | [optional] |

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

<a id="getNetworkWirelessClientLatencyStats"></a>
# **getNetworkWirelessClientLatencyStats**
> Object getNetworkWirelessClientLatencyStats(networkId, clientId, t0, t1, timespan, band, ssid, vlan, apTag, fields)

Aggregated latency info for a given client on this network

Aggregated latency info for a given client on this network. Clients are identified by their MAC.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String clientId = "clientId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    String band = "2.4"; // String | Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
    Integer ssid = 56; // Integer | Filter results by SSID
    Integer vlan = 56; // Integer | Filter results by VLAN
    String apTag = "apTag_example"; // String | Filter results by AP Tag
    String fields = "fields_example"; // String | Partial selection: If present, this call will return only the selected fields of [\"rawDistribution\", \"avg\"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
    try {
      Object result = apiInstance.getNetworkWirelessClientLatencyStats(networkId, clientId, t0, t1, timespan, band, ssid, vlan, apTag, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessClientLatencyStats");
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
| **clientId** | **String**|  | |
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] |
| **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information. | [optional] [enum: 2.4, 5, 6] |
| **ssid** | **Integer**| Filter results by SSID | [optional] |
| **vlan** | **Integer**| Filter results by VLAN | [optional] |
| **apTag** | **String**| Filter results by AP Tag | [optional] |
| **fields** | **String**| Partial selection: If present, this call will return only the selected fields of [\&quot;rawDistribution\&quot;, \&quot;avg\&quot;]. All fields will be returned by default. Selected fields must be entered as a comma separated string. | [optional] |

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

<a id="getNetworkWirelessClientsConnectionStats"></a>
# **getNetworkWirelessClientsConnectionStats**
> List&lt;Object&gt; getNetworkWirelessClientsConnectionStats(networkId, t0, t1, timespan, band, ssid, vlan, apTag)

Aggregated connectivity info for this network, grouped by clients

Aggregated connectivity info for this network, grouped by clients

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    String band = "2.4"; // String | Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
    Integer ssid = 56; // Integer | Filter results by SSID
    Integer vlan = 56; // Integer | Filter results by VLAN
    String apTag = "apTag_example"; // String | Filter results by AP Tag
    try {
      List<Object> result = apiInstance.getNetworkWirelessClientsConnectionStats(networkId, t0, t1, timespan, band, ssid, vlan, apTag);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessClientsConnectionStats");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] |
| **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information. | [optional] [enum: 2.4, 5, 6] |
| **ssid** | **Integer**| Filter results by SSID | [optional] |
| **vlan** | **Integer**| Filter results by VLAN | [optional] |
| **apTag** | **String**| Filter results by AP Tag | [optional] |

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

<a id="getNetworkWirelessClientsLatencyStats"></a>
# **getNetworkWirelessClientsLatencyStats**
> List&lt;Object&gt; getNetworkWirelessClientsLatencyStats(networkId, t0, t1, timespan, band, ssid, vlan, apTag, fields)

Aggregated latency info for this network, grouped by clients

Aggregated latency info for this network, grouped by clients

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    String band = "2.4"; // String | Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
    Integer ssid = 56; // Integer | Filter results by SSID
    Integer vlan = 56; // Integer | Filter results by VLAN
    String apTag = "apTag_example"; // String | Filter results by AP Tag
    String fields = "fields_example"; // String | Partial selection: If present, this call will return only the selected fields of [\"rawDistribution\", \"avg\"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
    try {
      List<Object> result = apiInstance.getNetworkWirelessClientsLatencyStats(networkId, t0, t1, timespan, band, ssid, vlan, apTag, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessClientsLatencyStats");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] |
| **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information. | [optional] [enum: 2.4, 5, 6] |
| **ssid** | **Integer**| Filter results by SSID | [optional] |
| **vlan** | **Integer**| Filter results by VLAN | [optional] |
| **apTag** | **String**| Filter results by AP Tag | [optional] |
| **fields** | **String**| Partial selection: If present, this call will return only the selected fields of [\&quot;rawDistribution\&quot;, \&quot;avg\&quot;]. All fields will be returned by default. Selected fields must be entered as a comma separated string. | [optional] |

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

<a id="getNetworkWirelessConnectionStats"></a>
# **getNetworkWirelessConnectionStats**
> GetNetworkWirelessConnectionStats200Response getNetworkWirelessConnectionStats(networkId, t0, t1, timespan, band, ssid, vlan, apTag)

Aggregated connectivity info for this network

Aggregated connectivity info for this network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    String band = "2.4"; // String | Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
    Integer ssid = 56; // Integer | Filter results by SSID
    Integer vlan = 56; // Integer | Filter results by VLAN
    String apTag = "apTag_example"; // String | Filter results by AP Tag
    try {
      GetNetworkWirelessConnectionStats200Response result = apiInstance.getNetworkWirelessConnectionStats(networkId, t0, t1, timespan, band, ssid, vlan, apTag);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessConnectionStats");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] |
| **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information. | [optional] [enum: 2.4, 5, 6] |
| **ssid** | **Integer**| Filter results by SSID | [optional] |
| **vlan** | **Integer**| Filter results by VLAN | [optional] |
| **apTag** | **String**| Filter results by AP Tag | [optional] |

### Return type

[**GetNetworkWirelessConnectionStats200Response**](GetNetworkWirelessConnectionStats200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkWirelessDataRateHistory"></a>
# **getNetworkWirelessDataRateHistory**
> List&lt;GetNetworkWirelessDataRateHistory200ResponseInner&gt; getNetworkWirelessDataRateHistory(networkId, t0, t1, timespan, resolution, autoResolution, clientId, deviceSerial, apTag, band, ssid)

Return PHY data rates over time for a network, device, or network client

Return PHY data rates over time for a network, device, or network client

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
    Integer resolution = 56; // Integer | The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400.
    Boolean autoResolution = true; // Boolean | Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false.
    String clientId = "clientId_example"; // String | Filter results by network client.
    String deviceSerial = "deviceSerial_example"; // String | Filter results by device.
    String apTag = "apTag_example"; // String | Filter results by AP tag.
    String band = "2.4"; // String | Filter results by band (either '2.4', '5' or '6').
    Integer ssid = 56; // Integer | Filter results by SSID number.
    try {
      List<GetNetworkWirelessDataRateHistory200ResponseInner> result = apiInstance.getNetworkWirelessDataRateHistory(networkId, t0, t1, timespan, resolution, autoResolution, clientId, deviceSerial, apTag, band, ssid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessDataRateHistory");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days. | [optional] |
| **resolution** | **Integer**| The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400. | [optional] |
| **autoResolution** | **Boolean**| Automatically select a data resolution based on the given timespan; this overrides the value specified by the &#39;resolution&#39; parameter. The default setting is false. | [optional] |
| **clientId** | **String**| Filter results by network client. | [optional] |
| **deviceSerial** | **String**| Filter results by device. | [optional] |
| **apTag** | **String**| Filter results by AP tag. | [optional] |
| **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). | [optional] [enum: 2.4, 5, 6] |
| **ssid** | **Integer**| Filter results by SSID number. | [optional] |

### Return type

[**List&lt;GetNetworkWirelessDataRateHistory200ResponseInner&gt;**](GetNetworkWirelessDataRateHistory200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkWirelessDevicesConnectionStats"></a>
# **getNetworkWirelessDevicesConnectionStats**
> List&lt;GetDeviceWirelessConnectionStats200Response&gt; getNetworkWirelessDevicesConnectionStats(networkId, t0, t1, timespan, band, ssid, vlan, apTag)

Aggregated connectivity info for this network, grouped by node

Aggregated connectivity info for this network, grouped by node

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    String band = "2.4"; // String | Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
    Integer ssid = 56; // Integer | Filter results by SSID
    Integer vlan = 56; // Integer | Filter results by VLAN
    String apTag = "apTag_example"; // String | Filter results by AP Tag
    try {
      List<GetDeviceWirelessConnectionStats200Response> result = apiInstance.getNetworkWirelessDevicesConnectionStats(networkId, t0, t1, timespan, band, ssid, vlan, apTag);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessDevicesConnectionStats");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] |
| **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information. | [optional] [enum: 2.4, 5, 6] |
| **ssid** | **Integer**| Filter results by SSID | [optional] |
| **vlan** | **Integer**| Filter results by VLAN | [optional] |
| **apTag** | **String**| Filter results by AP Tag | [optional] |

### Return type

[**List&lt;GetDeviceWirelessConnectionStats200Response&gt;**](GetDeviceWirelessConnectionStats200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkWirelessDevicesLatencyStats"></a>
# **getNetworkWirelessDevicesLatencyStats**
> List&lt;Object&gt; getNetworkWirelessDevicesLatencyStats(networkId, t0, t1, timespan, band, ssid, vlan, apTag, fields)

Aggregated latency info for this network, grouped by node

Aggregated latency info for this network, grouped by node

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    String band = "2.4"; // String | Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
    Integer ssid = 56; // Integer | Filter results by SSID
    Integer vlan = 56; // Integer | Filter results by VLAN
    String apTag = "apTag_example"; // String | Filter results by AP Tag
    String fields = "fields_example"; // String | Partial selection: If present, this call will return only the selected fields of [\"rawDistribution\", \"avg\"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
    try {
      List<Object> result = apiInstance.getNetworkWirelessDevicesLatencyStats(networkId, t0, t1, timespan, band, ssid, vlan, apTag, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessDevicesLatencyStats");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] |
| **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information. | [optional] [enum: 2.4, 5, 6] |
| **ssid** | **Integer**| Filter results by SSID | [optional] |
| **vlan** | **Integer**| Filter results by VLAN | [optional] |
| **apTag** | **String**| Filter results by AP Tag | [optional] |
| **fields** | **String**| Partial selection: If present, this call will return only the selected fields of [\&quot;rawDistribution\&quot;, \&quot;avg\&quot;]. All fields will be returned by default. Selected fields must be entered as a comma separated string. | [optional] |

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

<a id="getNetworkWirelessFailedConnections"></a>
# **getNetworkWirelessFailedConnections**
> List&lt;GetNetworkWirelessFailedConnections200ResponseInner&gt; getNetworkWirelessFailedConnections(networkId, t0, t1, timespan, band, ssid, vlan, apTag, serial, clientId)

List of all failed client connection events on this network in a given time range

List of all failed client connection events on this network in a given time range

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    String band = "2.4"; // String | Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
    Integer ssid = 56; // Integer | Filter results by SSID
    Integer vlan = 56; // Integer | Filter results by VLAN
    String apTag = "apTag_example"; // String | Filter results by AP Tag
    String serial = "serial_example"; // String | Filter by AP
    String clientId = "clientId_example"; // String | Filter by client MAC
    try {
      List<GetNetworkWirelessFailedConnections200ResponseInner> result = apiInstance.getNetworkWirelessFailedConnections(networkId, t0, t1, timespan, band, ssid, vlan, apTag, serial, clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessFailedConnections");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] |
| **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information. | [optional] [enum: 2.4, 5, 6] |
| **ssid** | **Integer**| Filter results by SSID | [optional] |
| **vlan** | **Integer**| Filter results by VLAN | [optional] |
| **apTag** | **String**| Filter results by AP Tag | [optional] |
| **serial** | **String**| Filter by AP | [optional] |
| **clientId** | **String**| Filter by client MAC | [optional] |

### Return type

[**List&lt;GetNetworkWirelessFailedConnections200ResponseInner&gt;**](GetNetworkWirelessFailedConnections200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkWirelessLatencyHistory"></a>
# **getNetworkWirelessLatencyHistory**
> List&lt;GetNetworkWirelessLatencyHistory200ResponseInner&gt; getNetworkWirelessLatencyHistory(networkId, t0, t1, timespan, resolution, autoResolution, clientId, deviceSerial, apTag, band, ssid, accessCategory)

Return average wireless latency over time for a network, device, or network client

Return average wireless latency over time for a network, device, or network client

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
    Integer resolution = 56; // Integer | The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400.
    Boolean autoResolution = true; // Boolean | Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false.
    String clientId = "clientId_example"; // String | Filter results by network client.
    String deviceSerial = "deviceSerial_example"; // String | Filter results by device.
    String apTag = "apTag_example"; // String | Filter results by AP tag.
    String band = "2.4"; // String | Filter results by band (either '2.4', '5' or '6').
    Integer ssid = 56; // Integer | Filter results by SSID number.
    String accessCategory = "backgroundTraffic"; // String | Filter by access category.
    try {
      List<GetNetworkWirelessLatencyHistory200ResponseInner> result = apiInstance.getNetworkWirelessLatencyHistory(networkId, t0, t1, timespan, resolution, autoResolution, clientId, deviceSerial, apTag, band, ssid, accessCategory);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessLatencyHistory");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days. | [optional] |
| **resolution** | **Integer**| The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400. | [optional] |
| **autoResolution** | **Boolean**| Automatically select a data resolution based on the given timespan; this overrides the value specified by the &#39;resolution&#39; parameter. The default setting is false. | [optional] |
| **clientId** | **String**| Filter results by network client. | [optional] |
| **deviceSerial** | **String**| Filter results by device. | [optional] |
| **apTag** | **String**| Filter results by AP tag. | [optional] |
| **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). | [optional] [enum: 2.4, 5, 6] |
| **ssid** | **Integer**| Filter results by SSID number. | [optional] |
| **accessCategory** | **String**| Filter by access category. | [optional] [enum: backgroundTraffic, bestEffortTraffic, videoTraffic, voiceTraffic] |

### Return type

[**List&lt;GetNetworkWirelessLatencyHistory200ResponseInner&gt;**](GetNetworkWirelessLatencyHistory200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkWirelessLatencyStats"></a>
# **getNetworkWirelessLatencyStats**
> Object getNetworkWirelessLatencyStats(networkId, t0, t1, timespan, band, ssid, vlan, apTag, fields)

Aggregated latency info for this network

Aggregated latency info for this network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    String band = "2.4"; // String | Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
    Integer ssid = 56; // Integer | Filter results by SSID
    Integer vlan = 56; // Integer | Filter results by VLAN
    String apTag = "apTag_example"; // String | Filter results by AP Tag
    String fields = "fields_example"; // String | Partial selection: If present, this call will return only the selected fields of [\"rawDistribution\", \"avg\"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
    try {
      Object result = apiInstance.getNetworkWirelessLatencyStats(networkId, t0, t1, timespan, band, ssid, vlan, apTag, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessLatencyStats");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] |
| **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information. | [optional] [enum: 2.4, 5, 6] |
| **ssid** | **Integer**| Filter results by SSID | [optional] |
| **vlan** | **Integer**| Filter results by VLAN | [optional] |
| **apTag** | **String**| Filter results by AP Tag | [optional] |
| **fields** | **String**| Partial selection: If present, this call will return only the selected fields of [\&quot;rawDistribution\&quot;, \&quot;avg\&quot;]. All fields will be returned by default. Selected fields must be entered as a comma separated string. | [optional] |

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

<a id="getNetworkWirelessMeshStatuses"></a>
# **getNetworkWirelessMeshStatuses**
> Object getNetworkWirelessMeshStatuses(networkId, perPage, startingAfter, endingBefore)

List wireless mesh statuses for repeaters

List wireless mesh statuses for repeaters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 500. Default is 50.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    try {
      Object result = apiInstance.getNetworkWirelessMeshStatuses(networkId, perPage, startingAfter, endingBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessMeshStatuses");
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
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 500. Default is 50. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |

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
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

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
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String rfProfileId = "rfProfileId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkWirelessRfProfile(networkId, rfProfileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessRfProfile");
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
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    Boolean includeTemplateProfiles = true; // Boolean | If the network is bound to a template, this parameter controls whether or not the non-basic RF profiles defined on the template should be included in the response alongside the non-basic profiles defined on the bound network. Defaults to false.
    try {
      List<Object> result = apiInstance.getNetworkWirelessRfProfiles(networkId, includeTemplateProfiles);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessRfProfiles");
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

<a id="getNetworkWirelessSettings"></a>
# **getNetworkWirelessSettings**
> GetNetworkWirelessSettings200Response getNetworkWirelessSettings(networkId)

Return the wireless settings for a network

Return the wireless settings for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkWirelessSettings200Response result = apiInstance.getNetworkWirelessSettings(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessSettings");
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

[**GetNetworkWirelessSettings200Response**](GetNetworkWirelessSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkWirelessSignalQualityHistory"></a>
# **getNetworkWirelessSignalQualityHistory**
> List&lt;GetNetworkWirelessSignalQualityHistory200ResponseInner&gt; getNetworkWirelessSignalQualityHistory(networkId, t0, t1, timespan, resolution, autoResolution, clientId, deviceSerial, apTag, band, ssid)

Return signal quality (SNR/RSSI) over time for a device or network client

Return signal quality (SNR/RSSI) over time for a device or network client

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
    Integer resolution = 56; // Integer | The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400.
    Boolean autoResolution = true; // Boolean | Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false.
    String clientId = "clientId_example"; // String | Filter results by network client.
    String deviceSerial = "deviceSerial_example"; // String | Filter results by device.
    String apTag = "apTag_example"; // String | Filter results by AP tag; either :clientId or :deviceSerial must be jointly specified.
    String band = "2.4"; // String | Filter results by band (either '2.4', '5' or '6').
    Integer ssid = 56; // Integer | Filter results by SSID number.
    try {
      List<GetNetworkWirelessSignalQualityHistory200ResponseInner> result = apiInstance.getNetworkWirelessSignalQualityHistory(networkId, t0, t1, timespan, resolution, autoResolution, clientId, deviceSerial, apTag, band, ssid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessSignalQualityHistory");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days. | [optional] |
| **resolution** | **Integer**| The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400. | [optional] |
| **autoResolution** | **Boolean**| Automatically select a data resolution based on the given timespan; this overrides the value specified by the &#39;resolution&#39; parameter. The default setting is false. | [optional] |
| **clientId** | **String**| Filter results by network client. | [optional] |
| **deviceSerial** | **String**| Filter results by device. | [optional] |
| **apTag** | **String**| Filter results by AP tag; either :clientId or :deviceSerial must be jointly specified. | [optional] |
| **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). | [optional] [enum: 2.4, 5, 6] |
| **ssid** | **Integer**| Filter results by SSID number. | [optional] |

### Return type

[**List&lt;GetNetworkWirelessSignalQualityHistory200ResponseInner&gt;**](GetNetworkWirelessSignalQualityHistory200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkWirelessSsid"></a>
# **getNetworkWirelessSsid**
> Object getNetworkWirelessSsid(networkId, number)

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
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    try {
      Object result = apiInstance.getNetworkWirelessSsid(networkId, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessSsid");
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

<a id="getNetworkWirelessSsidBonjourForwarding"></a>
# **getNetworkWirelessSsidBonjourForwarding**
> Object getNetworkWirelessSsidBonjourForwarding(networkId, number)

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
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    try {
      Object result = apiInstance.getNetworkWirelessSsidBonjourForwarding(networkId, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessSsidBonjourForwarding");
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

<a id="getNetworkWirelessSsidDeviceTypeGroupPolicies"></a>
# **getNetworkWirelessSsidDeviceTypeGroupPolicies**
> Object getNetworkWirelessSsidDeviceTypeGroupPolicies(networkId, number)

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
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    try {
      Object result = apiInstance.getNetworkWirelessSsidDeviceTypeGroupPolicies(networkId, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessSsidDeviceTypeGroupPolicies");
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

<a id="getNetworkWirelessSsidEapOverride"></a>
# **getNetworkWirelessSsidEapOverride**
> GetNetworkWirelessSsidEapOverride200Response getNetworkWirelessSsidEapOverride(networkId, number)

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
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    try {
      GetNetworkWirelessSsidEapOverride200Response result = apiInstance.getNetworkWirelessSsidEapOverride(networkId, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessSsidEapOverride");
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

<a id="getNetworkWirelessSsidFirewallL3FirewallRules"></a>
# **getNetworkWirelessSsidFirewallL3FirewallRules**
> Object getNetworkWirelessSsidFirewallL3FirewallRules(networkId, number)

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
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    try {
      Object result = apiInstance.getNetworkWirelessSsidFirewallL3FirewallRules(networkId, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessSsidFirewallL3FirewallRules");
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

<a id="getNetworkWirelessSsidFirewallL7FirewallRules"></a>
# **getNetworkWirelessSsidFirewallL7FirewallRules**
> Object getNetworkWirelessSsidFirewallL7FirewallRules(networkId, number)

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
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    try {
      Object result = apiInstance.getNetworkWirelessSsidFirewallL7FirewallRules(networkId, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessSsidFirewallL7FirewallRules");
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

<a id="getNetworkWirelessSsidHotspot20"></a>
# **getNetworkWirelessSsidHotspot20**
> Object getNetworkWirelessSsidHotspot20(networkId, number)

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
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    try {
      Object result = apiInstance.getNetworkWirelessSsidHotspot20(networkId, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessSsidHotspot20");
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

<a id="getNetworkWirelessSsidIdentityPsk"></a>
# **getNetworkWirelessSsidIdentityPsk**
> GetNetworkWirelessSsidIdentityPsks200ResponseInner getNetworkWirelessSsidIdentityPsk(networkId, number, identityPskId)

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
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    String identityPskId = "identityPskId_example"; // String | 
    try {
      GetNetworkWirelessSsidIdentityPsks200ResponseInner result = apiInstance.getNetworkWirelessSsidIdentityPsk(networkId, number, identityPskId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessSsidIdentityPsk");
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

<a id="getNetworkWirelessSsidIdentityPsks"></a>
# **getNetworkWirelessSsidIdentityPsks**
> List&lt;GetNetworkWirelessSsidIdentityPsks200ResponseInner&gt; getNetworkWirelessSsidIdentityPsks(networkId, number)

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
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    try {
      List<GetNetworkWirelessSsidIdentityPsks200ResponseInner> result = apiInstance.getNetworkWirelessSsidIdentityPsks(networkId, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessSsidIdentityPsks");
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

<a id="getNetworkWirelessSsidSchedules"></a>
# **getNetworkWirelessSsidSchedules**
> Object getNetworkWirelessSsidSchedules(networkId, number)

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
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    try {
      Object result = apiInstance.getNetworkWirelessSsidSchedules(networkId, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessSsidSchedules");
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

<a id="getNetworkWirelessSsidSplashSettings"></a>
# **getNetworkWirelessSsidSplashSettings**
> GetNetworkWirelessSsidSplashSettings200Response getNetworkWirelessSsidSplashSettings(networkId, number)

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
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    try {
      GetNetworkWirelessSsidSplashSettings200Response result = apiInstance.getNetworkWirelessSsidSplashSettings(networkId, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessSsidSplashSettings");
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

<a id="getNetworkWirelessSsidTrafficShapingRules"></a>
# **getNetworkWirelessSsidTrafficShapingRules**
> Object getNetworkWirelessSsidTrafficShapingRules(networkId, number)

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
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    try {
      Object result = apiInstance.getNetworkWirelessSsidTrafficShapingRules(networkId, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessSsidTrafficShapingRules");
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

<a id="getNetworkWirelessSsidVpn"></a>
# **getNetworkWirelessSsidVpn**
> Object getNetworkWirelessSsidVpn(networkId, number)

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
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    try {
      Object result = apiInstance.getNetworkWirelessSsidVpn(networkId, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessSsidVpn");
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

<a id="getNetworkWirelessSsids"></a>
# **getNetworkWirelessSsids**
> List&lt;Object&gt; getNetworkWirelessSsids(networkId)

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
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkWirelessSsids(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessSsids");
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

<a id="getNetworkWirelessUsageHistory"></a>
# **getNetworkWirelessUsageHistory**
> List&lt;GetNetworkWirelessUsageHistory200ResponseInner&gt; getNetworkWirelessUsageHistory(networkId, t0, t1, timespan, resolution, autoResolution, clientId, deviceSerial, apTag, band, ssid)

Return AP usage over time for a device or network client

Return AP usage over time for a device or network client

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
    Integer resolution = 56; // Integer | The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400.
    Boolean autoResolution = true; // Boolean | Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false.
    String clientId = "clientId_example"; // String | Filter results by network client to return per-device AP usage over time inner joined by the queried client's connection history.
    String deviceSerial = "deviceSerial_example"; // String | Filter results by device. Requires :band.
    String apTag = "apTag_example"; // String | Filter results by AP tag; either :clientId or :deviceSerial must be jointly specified.
    String band = "2.4"; // String | Filter results by band (either '2.4', '5' or '6').
    Integer ssid = 56; // Integer | Filter results by SSID number.
    try {
      List<GetNetworkWirelessUsageHistory200ResponseInner> result = apiInstance.getNetworkWirelessUsageHistory(networkId, t0, t1, timespan, resolution, autoResolution, clientId, deviceSerial, apTag, band, ssid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getNetworkWirelessUsageHistory");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days. | [optional] |
| **resolution** | **Integer**| The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400. | [optional] |
| **autoResolution** | **Boolean**| Automatically select a data resolution based on the given timespan; this overrides the value specified by the &#39;resolution&#39; parameter. The default setting is false. | [optional] |
| **clientId** | **String**| Filter results by network client to return per-device AP usage over time inner joined by the queried client&#39;s connection history. | [optional] |
| **deviceSerial** | **String**| Filter results by device. Requires :band. | [optional] |
| **apTag** | **String**| Filter results by AP tag; either :clientId or :deviceSerial must be jointly specified. | [optional] |
| **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). | [optional] [enum: 2.4, 5, 6] |
| **ssid** | **Integer**| Filter results by SSID number. | [optional] |

### Return type

[**List&lt;GetNetworkWirelessUsageHistory200ResponseInner&gt;**](GetNetworkWirelessUsageHistory200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationWirelessDevicesEthernetStatuses"></a>
# **getOrganizationWirelessDevicesEthernetStatuses**
> List&lt;GetOrganizationWirelessDevicesEthernetStatuses200ResponseInner&gt; getOrganizationWirelessDevicesEthernetStatuses(organizationId, perPage, startingAfter, endingBefore, networkIds)

Endpoint to see power status for wireless devices

Endpoint to see power status for wireless devices

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    List<String> networkIds = Arrays.asList(); // List<String> | A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]=N_12345678&networkIds[]=L_3456
    try {
      List<GetOrganizationWirelessDevicesEthernetStatuses200ResponseInner> result = apiInstance.getOrganizationWirelessDevicesEthernetStatuses(organizationId, perPage, startingAfter, endingBefore, networkIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#getOrganizationWirelessDevicesEthernetStatuses");
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
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **networkIds** | [**List&lt;String&gt;**](String.md)| A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]&#x3D;N_12345678&amp;networkIds[]&#x3D;L_3456 | [optional] |

### Return type

[**List&lt;GetOrganizationWirelessDevicesEthernetStatuses200ResponseInner&gt;**](GetOrganizationWirelessDevicesEthernetStatuses200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="updateDeviceWirelessBluetoothSettings"></a>
# **updateDeviceWirelessBluetoothSettings**
> GetDeviceWirelessBluetoothSettings200Response updateDeviceWirelessBluetoothSettings(serial, updateDeviceWirelessBluetoothSettingsRequest)

Update the bluetooth settings for a wireless device

Update the bluetooth settings for a wireless device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String serial = "serial_example"; // String | 
    UpdateDeviceWirelessBluetoothSettingsRequest updateDeviceWirelessBluetoothSettingsRequest = new UpdateDeviceWirelessBluetoothSettingsRequest(); // UpdateDeviceWirelessBluetoothSettingsRequest | 
    try {
      GetDeviceWirelessBluetoothSettings200Response result = apiInstance.updateDeviceWirelessBluetoothSettings(serial, updateDeviceWirelessBluetoothSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#updateDeviceWirelessBluetoothSettings");
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
| **updateDeviceWirelessBluetoothSettingsRequest** | [**UpdateDeviceWirelessBluetoothSettingsRequest**](UpdateDeviceWirelessBluetoothSettingsRequest.md)|  | [optional] |

### Return type

[**GetDeviceWirelessBluetoothSettings200Response**](GetDeviceWirelessBluetoothSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateDeviceWirelessRadioSettings"></a>
# **updateDeviceWirelessRadioSettings**
> Object updateDeviceWirelessRadioSettings(serial, updateDeviceWirelessRadioSettingsRequest)

Update the radio settings of a device

Update the radio settings of a device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String serial = "serial_example"; // String | 
    UpdateDeviceWirelessRadioSettingsRequest updateDeviceWirelessRadioSettingsRequest = new UpdateDeviceWirelessRadioSettingsRequest(); // UpdateDeviceWirelessRadioSettingsRequest | 
    try {
      Object result = apiInstance.updateDeviceWirelessRadioSettings(serial, updateDeviceWirelessRadioSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#updateDeviceWirelessRadioSettings");
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
| **updateDeviceWirelessRadioSettingsRequest** | [**UpdateDeviceWirelessRadioSettingsRequest**](UpdateDeviceWirelessRadioSettingsRequest.md)|  | [optional] |

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

<a id="updateNetworkWirelessAlternateManagementInterface"></a>
# **updateNetworkWirelessAlternateManagementInterface**
> Object updateNetworkWirelessAlternateManagementInterface(networkId, updateNetworkWirelessAlternateManagementInterfaceRequest)

Update alternate management interface and device static IP

Update alternate management interface and device static IP

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkWirelessAlternateManagementInterfaceRequest updateNetworkWirelessAlternateManagementInterfaceRequest = new UpdateNetworkWirelessAlternateManagementInterfaceRequest(); // UpdateNetworkWirelessAlternateManagementInterfaceRequest | 
    try {
      Object result = apiInstance.updateNetworkWirelessAlternateManagementInterface(networkId, updateNetworkWirelessAlternateManagementInterfaceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#updateNetworkWirelessAlternateManagementInterface");
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
| **updateNetworkWirelessAlternateManagementInterfaceRequest** | [**UpdateNetworkWirelessAlternateManagementInterfaceRequest**](UpdateNetworkWirelessAlternateManagementInterfaceRequest.md)|  | [optional] |

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

<a id="updateNetworkWirelessBilling"></a>
# **updateNetworkWirelessBilling**
> Object updateNetworkWirelessBilling(networkId, updateNetworkWirelessBillingRequest)

Update the billing settings

Update the billing settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkWirelessBillingRequest updateNetworkWirelessBillingRequest = new UpdateNetworkWirelessBillingRequest(); // UpdateNetworkWirelessBillingRequest | 
    try {
      Object result = apiInstance.updateNetworkWirelessBilling(networkId, updateNetworkWirelessBillingRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#updateNetworkWirelessBilling");
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
| **updateNetworkWirelessBillingRequest** | [**UpdateNetworkWirelessBillingRequest**](UpdateNetworkWirelessBillingRequest.md)|  | [optional] |

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

<a id="updateNetworkWirelessBluetoothSettings"></a>
# **updateNetworkWirelessBluetoothSettings**
> GetNetworkWirelessBluetoothSettings200Response updateNetworkWirelessBluetoothSettings(networkId, updateNetworkWirelessBluetoothSettingsRequest)

Update the Bluetooth settings for a network

Update the Bluetooth settings for a network. See the docs page for &lt;a href&#x3D;\&quot;https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\&quot;&gt;Bluetooth settings&lt;/a&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkWirelessBluetoothSettingsRequest updateNetworkWirelessBluetoothSettingsRequest = new UpdateNetworkWirelessBluetoothSettingsRequest(); // UpdateNetworkWirelessBluetoothSettingsRequest | 
    try {
      GetNetworkWirelessBluetoothSettings200Response result = apiInstance.updateNetworkWirelessBluetoothSettings(networkId, updateNetworkWirelessBluetoothSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#updateNetworkWirelessBluetoothSettings");
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
| **updateNetworkWirelessBluetoothSettingsRequest** | [**UpdateNetworkWirelessBluetoothSettingsRequest**](UpdateNetworkWirelessBluetoothSettingsRequest.md)|  | [optional] |

### Return type

[**GetNetworkWirelessBluetoothSettings200Response**](GetNetworkWirelessBluetoothSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkWirelessRfProfile"></a>
# **updateNetworkWirelessRfProfile**
> CreateNetworkWirelessRfProfile201Response updateNetworkWirelessRfProfile(networkId, rfProfileId, updateNetworkWirelessRfProfileRequest)

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
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String rfProfileId = "rfProfileId_example"; // String | 
    UpdateNetworkWirelessRfProfileRequest updateNetworkWirelessRfProfileRequest = new UpdateNetworkWirelessRfProfileRequest(); // UpdateNetworkWirelessRfProfileRequest | 
    try {
      CreateNetworkWirelessRfProfile201Response result = apiInstance.updateNetworkWirelessRfProfile(networkId, rfProfileId, updateNetworkWirelessRfProfileRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#updateNetworkWirelessRfProfile");
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

<a id="updateNetworkWirelessSettings"></a>
# **updateNetworkWirelessSettings**
> GetNetworkWirelessSettings200Response updateNetworkWirelessSettings(networkId, updateNetworkWirelessSettingsRequest)

Update the wireless settings for a network

Update the wireless settings for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkWirelessSettingsRequest updateNetworkWirelessSettingsRequest = new UpdateNetworkWirelessSettingsRequest(); // UpdateNetworkWirelessSettingsRequest | 
    try {
      GetNetworkWirelessSettings200Response result = apiInstance.updateNetworkWirelessSettings(networkId, updateNetworkWirelessSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#updateNetworkWirelessSettings");
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
| **updateNetworkWirelessSettingsRequest** | [**UpdateNetworkWirelessSettingsRequest**](UpdateNetworkWirelessSettingsRequest.md)|  | [optional] |

### Return type

[**GetNetworkWirelessSettings200Response**](GetNetworkWirelessSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkWirelessSsid"></a>
# **updateNetworkWirelessSsid**
> Object updateNetworkWirelessSsid(networkId, number, updateNetworkWirelessSsidRequest)

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
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    UpdateNetworkWirelessSsidRequest updateNetworkWirelessSsidRequest = new UpdateNetworkWirelessSsidRequest(); // UpdateNetworkWirelessSsidRequest | 
    try {
      Object result = apiInstance.updateNetworkWirelessSsid(networkId, number, updateNetworkWirelessSsidRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#updateNetworkWirelessSsid");
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

<a id="updateNetworkWirelessSsidBonjourForwarding"></a>
# **updateNetworkWirelessSsidBonjourForwarding**
> Object updateNetworkWirelessSsidBonjourForwarding(networkId, number, updateNetworkWirelessSsidBonjourForwardingRequest)

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
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    UpdateNetworkWirelessSsidBonjourForwardingRequest updateNetworkWirelessSsidBonjourForwardingRequest = new UpdateNetworkWirelessSsidBonjourForwardingRequest(); // UpdateNetworkWirelessSsidBonjourForwardingRequest | 
    try {
      Object result = apiInstance.updateNetworkWirelessSsidBonjourForwarding(networkId, number, updateNetworkWirelessSsidBonjourForwardingRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#updateNetworkWirelessSsidBonjourForwarding");
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

<a id="updateNetworkWirelessSsidDeviceTypeGroupPolicies"></a>
# **updateNetworkWirelessSsidDeviceTypeGroupPolicies**
> Object updateNetworkWirelessSsidDeviceTypeGroupPolicies(networkId, number, updateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest)

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
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    UpdateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest updateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest = new UpdateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest(); // UpdateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest | 
    try {
      Object result = apiInstance.updateNetworkWirelessSsidDeviceTypeGroupPolicies(networkId, number, updateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#updateNetworkWirelessSsidDeviceTypeGroupPolicies");
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

<a id="updateNetworkWirelessSsidEapOverride"></a>
# **updateNetworkWirelessSsidEapOverride**
> GetNetworkWirelessSsidEapOverride200Response updateNetworkWirelessSsidEapOverride(networkId, number, updateNetworkWirelessSsidEapOverrideRequest)

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
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    UpdateNetworkWirelessSsidEapOverrideRequest updateNetworkWirelessSsidEapOverrideRequest = new UpdateNetworkWirelessSsidEapOverrideRequest(); // UpdateNetworkWirelessSsidEapOverrideRequest | 
    try {
      GetNetworkWirelessSsidEapOverride200Response result = apiInstance.updateNetworkWirelessSsidEapOverride(networkId, number, updateNetworkWirelessSsidEapOverrideRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#updateNetworkWirelessSsidEapOverride");
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

<a id="updateNetworkWirelessSsidFirewallL3FirewallRules"></a>
# **updateNetworkWirelessSsidFirewallL3FirewallRules**
> Object updateNetworkWirelessSsidFirewallL3FirewallRules(networkId, number, updateNetworkWirelessSsidFirewallL3FirewallRulesRequest)

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
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest updateNetworkWirelessSsidFirewallL3FirewallRulesRequest = new UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest(); // UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest | 
    try {
      Object result = apiInstance.updateNetworkWirelessSsidFirewallL3FirewallRules(networkId, number, updateNetworkWirelessSsidFirewallL3FirewallRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#updateNetworkWirelessSsidFirewallL3FirewallRules");
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

<a id="updateNetworkWirelessSsidFirewallL7FirewallRules"></a>
# **updateNetworkWirelessSsidFirewallL7FirewallRules**
> Object updateNetworkWirelessSsidFirewallL7FirewallRules(networkId, number, updateNetworkWirelessSsidFirewallL7FirewallRulesRequest)

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
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest updateNetworkWirelessSsidFirewallL7FirewallRulesRequest = new UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest(); // UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest | 
    try {
      Object result = apiInstance.updateNetworkWirelessSsidFirewallL7FirewallRules(networkId, number, updateNetworkWirelessSsidFirewallL7FirewallRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#updateNetworkWirelessSsidFirewallL7FirewallRules");
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

<a id="updateNetworkWirelessSsidHotspot20"></a>
# **updateNetworkWirelessSsidHotspot20**
> Object updateNetworkWirelessSsidHotspot20(networkId, number, updateNetworkWirelessSsidHotspot20Request)

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
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    UpdateNetworkWirelessSsidHotspot20Request updateNetworkWirelessSsidHotspot20Request = new UpdateNetworkWirelessSsidHotspot20Request(); // UpdateNetworkWirelessSsidHotspot20Request | 
    try {
      Object result = apiInstance.updateNetworkWirelessSsidHotspot20(networkId, number, updateNetworkWirelessSsidHotspot20Request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#updateNetworkWirelessSsidHotspot20");
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

<a id="updateNetworkWirelessSsidIdentityPsk"></a>
# **updateNetworkWirelessSsidIdentityPsk**
> Object updateNetworkWirelessSsidIdentityPsk(networkId, number, identityPskId, updateNetworkWirelessSsidIdentityPskRequest)

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
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    String identityPskId = "identityPskId_example"; // String | 
    UpdateNetworkWirelessSsidIdentityPskRequest updateNetworkWirelessSsidIdentityPskRequest = new UpdateNetworkWirelessSsidIdentityPskRequest(); // UpdateNetworkWirelessSsidIdentityPskRequest | 
    try {
      Object result = apiInstance.updateNetworkWirelessSsidIdentityPsk(networkId, number, identityPskId, updateNetworkWirelessSsidIdentityPskRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#updateNetworkWirelessSsidIdentityPsk");
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

<a id="updateNetworkWirelessSsidSchedules"></a>
# **updateNetworkWirelessSsidSchedules**
> Object updateNetworkWirelessSsidSchedules(networkId, number, updateNetworkWirelessSsidSchedulesRequest)

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
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    UpdateNetworkWirelessSsidSchedulesRequest updateNetworkWirelessSsidSchedulesRequest = new UpdateNetworkWirelessSsidSchedulesRequest(); // UpdateNetworkWirelessSsidSchedulesRequest | 
    try {
      Object result = apiInstance.updateNetworkWirelessSsidSchedules(networkId, number, updateNetworkWirelessSsidSchedulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#updateNetworkWirelessSsidSchedules");
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

<a id="updateNetworkWirelessSsidSplashSettings"></a>
# **updateNetworkWirelessSsidSplashSettings**
> GetNetworkWirelessSsidSplashSettings200Response updateNetworkWirelessSsidSplashSettings(networkId, number, updateNetworkWirelessSsidSplashSettingsRequest)

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
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    UpdateNetworkWirelessSsidSplashSettingsRequest updateNetworkWirelessSsidSplashSettingsRequest = new UpdateNetworkWirelessSsidSplashSettingsRequest(); // UpdateNetworkWirelessSsidSplashSettingsRequest | 
    try {
      GetNetworkWirelessSsidSplashSettings200Response result = apiInstance.updateNetworkWirelessSsidSplashSettings(networkId, number, updateNetworkWirelessSsidSplashSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#updateNetworkWirelessSsidSplashSettings");
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

<a id="updateNetworkWirelessSsidTrafficShapingRules"></a>
# **updateNetworkWirelessSsidTrafficShapingRules**
> Object updateNetworkWirelessSsidTrafficShapingRules(networkId, number, updateNetworkWirelessSsidTrafficShapingRulesRequest)

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
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    UpdateNetworkWirelessSsidTrafficShapingRulesRequest updateNetworkWirelessSsidTrafficShapingRulesRequest = new UpdateNetworkWirelessSsidTrafficShapingRulesRequest(); // UpdateNetworkWirelessSsidTrafficShapingRulesRequest | 
    try {
      Object result = apiInstance.updateNetworkWirelessSsidTrafficShapingRules(networkId, number, updateNetworkWirelessSsidTrafficShapingRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#updateNetworkWirelessSsidTrafficShapingRules");
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

<a id="updateNetworkWirelessSsidVpn"></a>
# **updateNetworkWirelessSsidVpn**
> Object updateNetworkWirelessSsidVpn(networkId, number, updateNetworkWirelessSsidVpnRequest)

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
import org.openapitools.client.api.WirelessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WirelessApi apiInstance = new WirelessApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    UpdateNetworkWirelessSsidVpnRequest updateNetworkWirelessSsidVpnRequest = new UpdateNetworkWirelessSsidVpnRequest(); // UpdateNetworkWirelessSsidVpnRequest | 
    try {
      Object result = apiInstance.updateNetworkWirelessSsidVpn(networkId, number, updateNetworkWirelessSsidVpnRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessApi#updateNetworkWirelessSsidVpn");
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

