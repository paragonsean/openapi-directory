# MerakiDashboardApi.WirelessApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNetworkWirelessRfProfile**](WirelessApi.md#createNetworkWirelessRfProfile) | **POST** /networks/{networkId}/wireless/rfProfiles | Creates new RF profile for this network
[**createNetworkWirelessSsidIdentityPsk**](WirelessApi.md#createNetworkWirelessSsidIdentityPsk) | **POST** /networks/{networkId}/wireless/ssids/{number}/identityPsks | Create an Identity PSK
[**deleteNetworkWirelessRfProfile**](WirelessApi.md#deleteNetworkWirelessRfProfile) | **DELETE** /networks/{networkId}/wireless/rfProfiles/{rfProfileId} | Delete a RF Profile
[**deleteNetworkWirelessSsidIdentityPsk**](WirelessApi.md#deleteNetworkWirelessSsidIdentityPsk) | **DELETE** /networks/{networkId}/wireless/ssids/{number}/identityPsks/{identityPskId} | Delete an Identity PSK
[**getDeviceWirelessBluetoothSettings**](WirelessApi.md#getDeviceWirelessBluetoothSettings) | **GET** /devices/{serial}/wireless/bluetooth/settings | Return the bluetooth settings for a wireless device
[**getDeviceWirelessConnectionStats**](WirelessApi.md#getDeviceWirelessConnectionStats) | **GET** /devices/{serial}/wireless/connectionStats | Aggregated connectivity info for a given AP on this network
[**getDeviceWirelessLatencyStats**](WirelessApi.md#getDeviceWirelessLatencyStats) | **GET** /devices/{serial}/wireless/latencyStats | Aggregated latency info for a given AP on this network
[**getDeviceWirelessRadioSettings**](WirelessApi.md#getDeviceWirelessRadioSettings) | **GET** /devices/{serial}/wireless/radio/settings | Return the radio settings of a device
[**getDeviceWirelessStatus**](WirelessApi.md#getDeviceWirelessStatus) | **GET** /devices/{serial}/wireless/status | Return the SSID statuses of an access point
[**getNetworkWirelessAirMarshal**](WirelessApi.md#getNetworkWirelessAirMarshal) | **GET** /networks/{networkId}/wireless/airMarshal | List Air Marshal scan results from a network
[**getNetworkWirelessAlternateManagementInterface**](WirelessApi.md#getNetworkWirelessAlternateManagementInterface) | **GET** /networks/{networkId}/wireless/alternateManagementInterface | Return alternate management interface and devices with IP assigned
[**getNetworkWirelessBilling**](WirelessApi.md#getNetworkWirelessBilling) | **GET** /networks/{networkId}/wireless/billing | Return the billing settings of this network
[**getNetworkWirelessBluetoothSettings**](WirelessApi.md#getNetworkWirelessBluetoothSettings) | **GET** /networks/{networkId}/wireless/bluetooth/settings | Return the Bluetooth settings for a network. &lt;a href&#x3D;\&quot;https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\&quot;&gt;Bluetooth settings&lt;/a&gt; must be enabled on the network.
[**getNetworkWirelessChannelUtilizationHistory**](WirelessApi.md#getNetworkWirelessChannelUtilizationHistory) | **GET** /networks/{networkId}/wireless/channelUtilizationHistory | Return AP channel utilization over time for a device or network client
[**getNetworkWirelessClientConnectionStats**](WirelessApi.md#getNetworkWirelessClientConnectionStats) | **GET** /networks/{networkId}/wireless/clients/{clientId}/connectionStats | Aggregated connectivity info for a given client on this network
[**getNetworkWirelessClientConnectivityEvents**](WirelessApi.md#getNetworkWirelessClientConnectivityEvents) | **GET** /networks/{networkId}/wireless/clients/{clientId}/connectivityEvents | List the wireless connectivity events for a client within a network in the timespan.
[**getNetworkWirelessClientCountHistory**](WirelessApi.md#getNetworkWirelessClientCountHistory) | **GET** /networks/{networkId}/wireless/clientCountHistory | Return wireless client counts over time for a network, device, or network client
[**getNetworkWirelessClientLatencyHistory**](WirelessApi.md#getNetworkWirelessClientLatencyHistory) | **GET** /networks/{networkId}/wireless/clients/{clientId}/latencyHistory | Return the latency history for a client
[**getNetworkWirelessClientLatencyStats**](WirelessApi.md#getNetworkWirelessClientLatencyStats) | **GET** /networks/{networkId}/wireless/clients/{clientId}/latencyStats | Aggregated latency info for a given client on this network
[**getNetworkWirelessClientsConnectionStats**](WirelessApi.md#getNetworkWirelessClientsConnectionStats) | **GET** /networks/{networkId}/wireless/clients/connectionStats | Aggregated connectivity info for this network, grouped by clients
[**getNetworkWirelessClientsLatencyStats**](WirelessApi.md#getNetworkWirelessClientsLatencyStats) | **GET** /networks/{networkId}/wireless/clients/latencyStats | Aggregated latency info for this network, grouped by clients
[**getNetworkWirelessConnectionStats**](WirelessApi.md#getNetworkWirelessConnectionStats) | **GET** /networks/{networkId}/wireless/connectionStats | Aggregated connectivity info for this network
[**getNetworkWirelessDataRateHistory**](WirelessApi.md#getNetworkWirelessDataRateHistory) | **GET** /networks/{networkId}/wireless/dataRateHistory | Return PHY data rates over time for a network, device, or network client
[**getNetworkWirelessDevicesConnectionStats**](WirelessApi.md#getNetworkWirelessDevicesConnectionStats) | **GET** /networks/{networkId}/wireless/devices/connectionStats | Aggregated connectivity info for this network, grouped by node
[**getNetworkWirelessDevicesLatencyStats**](WirelessApi.md#getNetworkWirelessDevicesLatencyStats) | **GET** /networks/{networkId}/wireless/devices/latencyStats | Aggregated latency info for this network, grouped by node
[**getNetworkWirelessFailedConnections**](WirelessApi.md#getNetworkWirelessFailedConnections) | **GET** /networks/{networkId}/wireless/failedConnections | List of all failed client connection events on this network in a given time range
[**getNetworkWirelessLatencyHistory**](WirelessApi.md#getNetworkWirelessLatencyHistory) | **GET** /networks/{networkId}/wireless/latencyHistory | Return average wireless latency over time for a network, device, or network client
[**getNetworkWirelessLatencyStats**](WirelessApi.md#getNetworkWirelessLatencyStats) | **GET** /networks/{networkId}/wireless/latencyStats | Aggregated latency info for this network
[**getNetworkWirelessMeshStatuses**](WirelessApi.md#getNetworkWirelessMeshStatuses) | **GET** /networks/{networkId}/wireless/meshStatuses | List wireless mesh statuses for repeaters
[**getNetworkWirelessRfProfile**](WirelessApi.md#getNetworkWirelessRfProfile) | **GET** /networks/{networkId}/wireless/rfProfiles/{rfProfileId} | Return a RF profile
[**getNetworkWirelessRfProfiles**](WirelessApi.md#getNetworkWirelessRfProfiles) | **GET** /networks/{networkId}/wireless/rfProfiles | List the non-basic RF profiles for this network
[**getNetworkWirelessSettings**](WirelessApi.md#getNetworkWirelessSettings) | **GET** /networks/{networkId}/wireless/settings | Return the wireless settings for a network
[**getNetworkWirelessSignalQualityHistory**](WirelessApi.md#getNetworkWirelessSignalQualityHistory) | **GET** /networks/{networkId}/wireless/signalQualityHistory | Return signal quality (SNR/RSSI) over time for a device or network client
[**getNetworkWirelessSsid**](WirelessApi.md#getNetworkWirelessSsid) | **GET** /networks/{networkId}/wireless/ssids/{number} | Return a single MR SSID
[**getNetworkWirelessSsidBonjourForwarding**](WirelessApi.md#getNetworkWirelessSsidBonjourForwarding) | **GET** /networks/{networkId}/wireless/ssids/{number}/bonjourForwarding | List the Bonjour forwarding setting and rules for the SSID
[**getNetworkWirelessSsidDeviceTypeGroupPolicies**](WirelessApi.md#getNetworkWirelessSsidDeviceTypeGroupPolicies) | **GET** /networks/{networkId}/wireless/ssids/{number}/deviceTypeGroupPolicies | List the device type group policies for the SSID
[**getNetworkWirelessSsidEapOverride**](WirelessApi.md#getNetworkWirelessSsidEapOverride) | **GET** /networks/{networkId}/wireless/ssids/{number}/eapOverride | Return the EAP overridden parameters for an SSID
[**getNetworkWirelessSsidFirewallL3FirewallRules**](WirelessApi.md#getNetworkWirelessSsidFirewallL3FirewallRules) | **GET** /networks/{networkId}/wireless/ssids/{number}/firewall/l3FirewallRules | Return the L3 firewall rules for an SSID on an MR network
[**getNetworkWirelessSsidFirewallL7FirewallRules**](WirelessApi.md#getNetworkWirelessSsidFirewallL7FirewallRules) | **GET** /networks/{networkId}/wireless/ssids/{number}/firewall/l7FirewallRules | Return the L7 firewall rules for an SSID on an MR network
[**getNetworkWirelessSsidHotspot20**](WirelessApi.md#getNetworkWirelessSsidHotspot20) | **GET** /networks/{networkId}/wireless/ssids/{number}/hotspot20 | Return the Hotspot 2.0 settings for an SSID
[**getNetworkWirelessSsidIdentityPsk**](WirelessApi.md#getNetworkWirelessSsidIdentityPsk) | **GET** /networks/{networkId}/wireless/ssids/{number}/identityPsks/{identityPskId} | Return an Identity PSK
[**getNetworkWirelessSsidIdentityPsks**](WirelessApi.md#getNetworkWirelessSsidIdentityPsks) | **GET** /networks/{networkId}/wireless/ssids/{number}/identityPsks | List all Identity PSKs in a wireless network
[**getNetworkWirelessSsidSchedules**](WirelessApi.md#getNetworkWirelessSsidSchedules) | **GET** /networks/{networkId}/wireless/ssids/{number}/schedules | List the outage schedule for the SSID
[**getNetworkWirelessSsidSplashSettings**](WirelessApi.md#getNetworkWirelessSsidSplashSettings) | **GET** /networks/{networkId}/wireless/ssids/{number}/splash/settings | Display the splash page settings for the given SSID
[**getNetworkWirelessSsidTrafficShapingRules**](WirelessApi.md#getNetworkWirelessSsidTrafficShapingRules) | **GET** /networks/{networkId}/wireless/ssids/{number}/trafficShaping/rules | Display the traffic shaping settings for a SSID on an MR network
[**getNetworkWirelessSsidVpn**](WirelessApi.md#getNetworkWirelessSsidVpn) | **GET** /networks/{networkId}/wireless/ssids/{number}/vpn | List the VPN settings for the SSID.
[**getNetworkWirelessSsids**](WirelessApi.md#getNetworkWirelessSsids) | **GET** /networks/{networkId}/wireless/ssids | List the MR SSIDs in a network
[**getNetworkWirelessUsageHistory**](WirelessApi.md#getNetworkWirelessUsageHistory) | **GET** /networks/{networkId}/wireless/usageHistory | Return AP usage over time for a device or network client
[**getOrganizationWirelessDevicesEthernetStatuses**](WirelessApi.md#getOrganizationWirelessDevicesEthernetStatuses) | **GET** /organizations/{organizationId}/wireless/devices/ethernet/statuses | Endpoint to see power status for wireless devices
[**updateDeviceWirelessBluetoothSettings**](WirelessApi.md#updateDeviceWirelessBluetoothSettings) | **PUT** /devices/{serial}/wireless/bluetooth/settings | Update the bluetooth settings for a wireless device
[**updateDeviceWirelessRadioSettings**](WirelessApi.md#updateDeviceWirelessRadioSettings) | **PUT** /devices/{serial}/wireless/radio/settings | Update the radio settings of a device
[**updateNetworkWirelessAlternateManagementInterface**](WirelessApi.md#updateNetworkWirelessAlternateManagementInterface) | **PUT** /networks/{networkId}/wireless/alternateManagementInterface | Update alternate management interface and device static IP
[**updateNetworkWirelessBilling**](WirelessApi.md#updateNetworkWirelessBilling) | **PUT** /networks/{networkId}/wireless/billing | Update the billing settings
[**updateNetworkWirelessBluetoothSettings**](WirelessApi.md#updateNetworkWirelessBluetoothSettings) | **PUT** /networks/{networkId}/wireless/bluetooth/settings | Update the Bluetooth settings for a network
[**updateNetworkWirelessRfProfile**](WirelessApi.md#updateNetworkWirelessRfProfile) | **PUT** /networks/{networkId}/wireless/rfProfiles/{rfProfileId} | Updates specified RF profile for this network
[**updateNetworkWirelessSettings**](WirelessApi.md#updateNetworkWirelessSettings) | **PUT** /networks/{networkId}/wireless/settings | Update the wireless settings for a network
[**updateNetworkWirelessSsid**](WirelessApi.md#updateNetworkWirelessSsid) | **PUT** /networks/{networkId}/wireless/ssids/{number} | Update the attributes of an MR SSID
[**updateNetworkWirelessSsidBonjourForwarding**](WirelessApi.md#updateNetworkWirelessSsidBonjourForwarding) | **PUT** /networks/{networkId}/wireless/ssids/{number}/bonjourForwarding | Update the bonjour forwarding setting and rules for the SSID
[**updateNetworkWirelessSsidDeviceTypeGroupPolicies**](WirelessApi.md#updateNetworkWirelessSsidDeviceTypeGroupPolicies) | **PUT** /networks/{networkId}/wireless/ssids/{number}/deviceTypeGroupPolicies | Update the device type group policies for the SSID
[**updateNetworkWirelessSsidEapOverride**](WirelessApi.md#updateNetworkWirelessSsidEapOverride) | **PUT** /networks/{networkId}/wireless/ssids/{number}/eapOverride | Update the EAP overridden parameters for an SSID.
[**updateNetworkWirelessSsidFirewallL3FirewallRules**](WirelessApi.md#updateNetworkWirelessSsidFirewallL3FirewallRules) | **PUT** /networks/{networkId}/wireless/ssids/{number}/firewall/l3FirewallRules | Update the L3 firewall rules of an SSID on an MR network
[**updateNetworkWirelessSsidFirewallL7FirewallRules**](WirelessApi.md#updateNetworkWirelessSsidFirewallL7FirewallRules) | **PUT** /networks/{networkId}/wireless/ssids/{number}/firewall/l7FirewallRules | Update the L7 firewall rules of an SSID on an MR network
[**updateNetworkWirelessSsidHotspot20**](WirelessApi.md#updateNetworkWirelessSsidHotspot20) | **PUT** /networks/{networkId}/wireless/ssids/{number}/hotspot20 | Update the Hotspot 2.0 settings of an SSID
[**updateNetworkWirelessSsidIdentityPsk**](WirelessApi.md#updateNetworkWirelessSsidIdentityPsk) | **PUT** /networks/{networkId}/wireless/ssids/{number}/identityPsks/{identityPskId} | Update an Identity PSK
[**updateNetworkWirelessSsidSchedules**](WirelessApi.md#updateNetworkWirelessSsidSchedules) | **PUT** /networks/{networkId}/wireless/ssids/{number}/schedules | Update the outage schedule for the SSID
[**updateNetworkWirelessSsidSplashSettings**](WirelessApi.md#updateNetworkWirelessSsidSplashSettings) | **PUT** /networks/{networkId}/wireless/ssids/{number}/splash/settings | Modify the splash page settings for the given SSID
[**updateNetworkWirelessSsidTrafficShapingRules**](WirelessApi.md#updateNetworkWirelessSsidTrafficShapingRules) | **PUT** /networks/{networkId}/wireless/ssids/{number}/trafficShaping/rules | Update the traffic shaping settings for an SSID on an MR network
[**updateNetworkWirelessSsidVpn**](WirelessApi.md#updateNetworkWirelessSsidVpn) | **PUT** /networks/{networkId}/wireless/ssids/{number}/vpn | Update the VPN settings for the SSID



## createNetworkWirelessRfProfile

> CreateNetworkWirelessRfProfile201Response createNetworkWirelessRfProfile(networkId, createNetworkWirelessRfProfileRequest)

Creates new RF profile for this network

Creates new RF profile for this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let createNetworkWirelessRfProfileRequest = new MerakiDashboardApi.CreateNetworkWirelessRfProfileRequest(); // CreateNetworkWirelessRfProfileRequest | 
apiInstance.createNetworkWirelessRfProfile(networkId, createNetworkWirelessRfProfileRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **createNetworkWirelessRfProfileRequest** | [**CreateNetworkWirelessRfProfileRequest**](CreateNetworkWirelessRfProfileRequest.md)|  | 

### Return type

[**CreateNetworkWirelessRfProfile201Response**](CreateNetworkWirelessRfProfile201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkWirelessSsidIdentityPsk

> Object createNetworkWirelessSsidIdentityPsk(networkId, number, createNetworkWirelessSsidIdentityPskRequest)

Create an Identity PSK

Create an Identity PSK

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
let createNetworkWirelessSsidIdentityPskRequest = new MerakiDashboardApi.CreateNetworkWirelessSsidIdentityPskRequest(); // CreateNetworkWirelessSsidIdentityPskRequest | 
apiInstance.createNetworkWirelessSsidIdentityPsk(networkId, number, createNetworkWirelessSsidIdentityPskRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 
 **createNetworkWirelessSsidIdentityPskRequest** | [**CreateNetworkWirelessSsidIdentityPskRequest**](CreateNetworkWirelessSsidIdentityPskRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteNetworkWirelessRfProfile

> deleteNetworkWirelessRfProfile(networkId, rfProfileId)

Delete a RF Profile

Delete a RF Profile

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let rfProfileId = "rfProfileId_example"; // String | 
apiInstance.deleteNetworkWirelessRfProfile(networkId, rfProfileId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **rfProfileId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetworkWirelessSsidIdentityPsk

> deleteNetworkWirelessSsidIdentityPsk(networkId, number, identityPskId)

Delete an Identity PSK

Delete an Identity PSK

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
let identityPskId = "identityPskId_example"; // String | 
apiInstance.deleteNetworkWirelessSsidIdentityPsk(networkId, number, identityPskId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 
 **identityPskId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getDeviceWirelessBluetoothSettings

> GetDeviceWirelessBluetoothSettings200Response getDeviceWirelessBluetoothSettings(serial)

Return the bluetooth settings for a wireless device

Return the bluetooth settings for a wireless device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceWirelessBluetoothSettings(serial, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 

### Return type

[**GetDeviceWirelessBluetoothSettings200Response**](GetDeviceWirelessBluetoothSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeviceWirelessConnectionStats

> GetDeviceWirelessConnectionStats200Response getDeviceWirelessConnectionStats(serial, opts)

Aggregated connectivity info for a given AP on this network

Aggregated connectivity info for a given AP on this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let serial = "serial_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
  'band': "band_example", // String | Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
  'ssid': 56, // Number | Filter results by SSID
  'vlan': 56, // Number | Filter results by VLAN
  'apTag': "apTag_example" // String | Filter results by AP Tag
};
apiInstance.getDeviceWirelessConnectionStats(serial, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] 
 **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information. | [optional] 
 **ssid** | **Number**| Filter results by SSID | [optional] 
 **vlan** | **Number**| Filter results by VLAN | [optional] 
 **apTag** | **String**| Filter results by AP Tag | [optional] 

### Return type

[**GetDeviceWirelessConnectionStats200Response**](GetDeviceWirelessConnectionStats200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeviceWirelessLatencyStats

> Object getDeviceWirelessLatencyStats(serial, opts)

Aggregated latency info for a given AP on this network

Aggregated latency info for a given AP on this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let serial = "serial_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
  'band': "band_example", // String | Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
  'ssid': 56, // Number | Filter results by SSID
  'vlan': 56, // Number | Filter results by VLAN
  'apTag': "apTag_example", // String | Filter results by AP Tag
  'fields': "fields_example" // String | Partial selection: If present, this call will return only the selected fields of [\"rawDistribution\", \"avg\"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
};
apiInstance.getDeviceWirelessLatencyStats(serial, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] 
 **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information. | [optional] 
 **ssid** | **Number**| Filter results by SSID | [optional] 
 **vlan** | **Number**| Filter results by VLAN | [optional] 
 **apTag** | **String**| Filter results by AP Tag | [optional] 
 **fields** | **String**| Partial selection: If present, this call will return only the selected fields of [\&quot;rawDistribution\&quot;, \&quot;avg\&quot;]. All fields will be returned by default. Selected fields must be entered as a comma separated string. | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeviceWirelessRadioSettings

> Object getDeviceWirelessRadioSettings(serial)

Return the radio settings of a device

Return the radio settings of a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceWirelessRadioSettings(serial, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeviceWirelessStatus

> Object getDeviceWirelessStatus(serial)

Return the SSID statuses of an access point

Return the SSID statuses of an access point

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceWirelessStatus(serial, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessAirMarshal

> [Object] getNetworkWirelessAirMarshal(networkId, opts)

List Air Marshal scan results from a network

List Air Marshal scan results from a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
  'timespan': 3.4 // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
};
apiInstance.getNetworkWirelessAirMarshal(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 7 days. | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessAlternateManagementInterface

> Object getNetworkWirelessAlternateManagementInterface(networkId)

Return alternate management interface and devices with IP assigned

Return alternate management interface and devices with IP assigned

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkWirelessAlternateManagementInterface(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessBilling

> Object getNetworkWirelessBilling(networkId)

Return the billing settings of this network

Return the billing settings of this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkWirelessBilling(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessBluetoothSettings

> GetNetworkWirelessBluetoothSettings200Response getNetworkWirelessBluetoothSettings(networkId)

Return the Bluetooth settings for a network. &lt;a href&#x3D;\&quot;https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\&quot;&gt;Bluetooth settings&lt;/a&gt; must be enabled on the network.

Return the Bluetooth settings for a network. &lt;a href&#x3D;\&quot;https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\&quot;&gt;Bluetooth settings&lt;/a&gt; must be enabled on the network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkWirelessBluetoothSettings(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

[**GetNetworkWirelessBluetoothSettings200Response**](GetNetworkWirelessBluetoothSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessChannelUtilizationHistory

> [GetNetworkWirelessChannelUtilizationHistory200ResponseInner] getNetworkWirelessChannelUtilizationHistory(networkId, opts)

Return AP channel utilization over time for a device or network client

Return AP channel utilization over time for a device or network client

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
  'resolution': 56, // Number | The time resolution in seconds for returned data. The valid resolutions are: 600, 1200, 3600, 14400, 86400. The default is 86400.
  'autoResolution': true, // Boolean | Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false.
  'clientId': "clientId_example", // String | Filter results by network client to return per-device, per-band AP channel utilization metrics inner joined by the queried client's connection history.
  'deviceSerial': "deviceSerial_example", // String | Filter results by device to return AP channel utilization metrics for the queried device; either :band or :clientId must be jointly specified.
  'apTag': "apTag_example", // String | Filter results by AP tag to return AP channel utilization metrics for devices labeled with the given tag; either :clientId or :deviceSerial must be jointly specified.
  'band': "band_example" // String | Filter results by band (either '2.4', '5' or '6').
};
apiInstance.getNetworkWirelessChannelUtilizationHistory(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days. | [optional] 
 **resolution** | **Number**| The time resolution in seconds for returned data. The valid resolutions are: 600, 1200, 3600, 14400, 86400. The default is 86400. | [optional] 
 **autoResolution** | **Boolean**| Automatically select a data resolution based on the given timespan; this overrides the value specified by the &#39;resolution&#39; parameter. The default setting is false. | [optional] 
 **clientId** | **String**| Filter results by network client to return per-device, per-band AP channel utilization metrics inner joined by the queried client&#39;s connection history. | [optional] 
 **deviceSerial** | **String**| Filter results by device to return AP channel utilization metrics for the queried device; either :band or :clientId must be jointly specified. | [optional] 
 **apTag** | **String**| Filter results by AP tag to return AP channel utilization metrics for devices labeled with the given tag; either :clientId or :deviceSerial must be jointly specified. | [optional] 
 **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). | [optional] 

### Return type

[**[GetNetworkWirelessChannelUtilizationHistory200ResponseInner]**](GetNetworkWirelessChannelUtilizationHistory200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessClientConnectionStats

> Object getNetworkWirelessClientConnectionStats(networkId, clientId, opts)

Aggregated connectivity info for a given client on this network

Aggregated connectivity info for a given client on this network. Clients are identified by their MAC.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let clientId = "clientId_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
  'band': "band_example", // String | Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
  'ssid': 56, // Number | Filter results by SSID
  'vlan': 56, // Number | Filter results by VLAN
  'apTag': "apTag_example" // String | Filter results by AP Tag
};
apiInstance.getNetworkWirelessClientConnectionStats(networkId, clientId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **clientId** | **String**|  | 
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] 
 **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information. | [optional] 
 **ssid** | **Number**| Filter results by SSID | [optional] 
 **vlan** | **Number**| Filter results by VLAN | [optional] 
 **apTag** | **String**| Filter results by AP Tag | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessClientConnectivityEvents

> [Object] getNetworkWirelessClientConnectivityEvents(networkId, clientId, opts)

List the wireless connectivity events for a client within a network in the timespan.

List the wireless connectivity events for a client within a network in the timespan.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let clientId = "clientId_example"; // String | 
let opts = {
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 3 - 1000.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example", // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
  'types': ["null"], // [String] | A list of event types to include. If not specified, events of all types will be returned. Valid types are 'assoc', 'disassoc', 'auth', 'deauth', 'dns', 'dhcp', 'roam', 'connection' and/or 'sticky'.
  'includedSeverities': ["null"], // [String] | A list of severities to include. If not specified, events of all severities will be returned. Valid severities are 'good', 'info', 'warn' and/or 'bad'.
  'band': "band_example", // String | Filter results by band (either '2.4', '5', '6').
  'ssidNumber': 56, // Number | An SSID number to include. If not specified, events for all SSIDs will be returned.
  'deviceSerial': "deviceSerial_example" // String | Filter results by an AP's serial number.
};
apiInstance.getNetworkWirelessClientConnectivityEvents(networkId, clientId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **clientId** | **String**|  | 
 **perPage** | **Number**| The number of entries per page returned. Acceptable range is 3 - 1000. | [optional] 
 **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. | [optional] 
 **types** | [**[String]**](String.md)| A list of event types to include. If not specified, events of all types will be returned. Valid types are &#39;assoc&#39;, &#39;disassoc&#39;, &#39;auth&#39;, &#39;deauth&#39;, &#39;dns&#39;, &#39;dhcp&#39;, &#39;roam&#39;, &#39;connection&#39; and/or &#39;sticky&#39;. | [optional] 
 **includedSeverities** | [**[String]**](String.md)| A list of severities to include. If not specified, events of all severities will be returned. Valid severities are &#39;good&#39;, &#39;info&#39;, &#39;warn&#39; and/or &#39;bad&#39;. | [optional] 
 **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39;, &#39;6&#39;). | [optional] 
 **ssidNumber** | **Number**| An SSID number to include. If not specified, events for all SSIDs will be returned. | [optional] 
 **deviceSerial** | **String**| Filter results by an AP&#39;s serial number. | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessClientCountHistory

> [GetNetworkWirelessClientCountHistory200ResponseInner] getNetworkWirelessClientCountHistory(networkId, opts)

Return wireless client counts over time for a network, device, or network client

Return wireless client counts over time for a network, device, or network client

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
  'resolution': 56, // Number | The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400.
  'autoResolution': true, // Boolean | Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false.
  'clientId': "clientId_example", // String | Filter results by network client to return per-device client counts over time inner joined by the queried client's connection history.
  'deviceSerial': "deviceSerial_example", // String | Filter results by device.
  'apTag': "apTag_example", // String | Filter results by AP tag.
  'band': "band_example", // String | Filter results by band (either '2.4', '5' or '6').
  'ssid': 56 // Number | Filter results by SSID number.
};
apiInstance.getNetworkWirelessClientCountHistory(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days. | [optional] 
 **resolution** | **Number**| The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400. | [optional] 
 **autoResolution** | **Boolean**| Automatically select a data resolution based on the given timespan; this overrides the value specified by the &#39;resolution&#39; parameter. The default setting is false. | [optional] 
 **clientId** | **String**| Filter results by network client to return per-device client counts over time inner joined by the queried client&#39;s connection history. | [optional] 
 **deviceSerial** | **String**| Filter results by device. | [optional] 
 **apTag** | **String**| Filter results by AP tag. | [optional] 
 **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). | [optional] 
 **ssid** | **Number**| Filter results by SSID number. | [optional] 

### Return type

[**[GetNetworkWirelessClientCountHistory200ResponseInner]**](GetNetworkWirelessClientCountHistory200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessClientLatencyHistory

> [Object] getNetworkWirelessClientLatencyHistory(networkId, clientId, opts)

Return the latency history for a client

Return the latency history for a client. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP. The latency data is from a sample of 2% of packets and is grouped into 4 traffic categories: background, best effort, video, voice. Within these categories the sampled packet counters are bucketed by latency in milliseconds.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let clientId = "clientId_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 791 days from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 791 days after t0.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 791 days. The default is 1 day.
  'resolution': 56 // Number | The time resolution in seconds for returned data. The valid resolutions are: 86400. The default is 86400.
};
apiInstance.getNetworkWirelessClientLatencyHistory(networkId, clientId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **clientId** | **String**|  | 
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 791 days from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 791 days after t0. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 791 days. The default is 1 day. | [optional] 
 **resolution** | **Number**| The time resolution in seconds for returned data. The valid resolutions are: 86400. The default is 86400. | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessClientLatencyStats

> Object getNetworkWirelessClientLatencyStats(networkId, clientId, opts)

Aggregated latency info for a given client on this network

Aggregated latency info for a given client on this network. Clients are identified by their MAC.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let clientId = "clientId_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
  'band': "band_example", // String | Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
  'ssid': 56, // Number | Filter results by SSID
  'vlan': 56, // Number | Filter results by VLAN
  'apTag': "apTag_example", // String | Filter results by AP Tag
  'fields': "fields_example" // String | Partial selection: If present, this call will return only the selected fields of [\"rawDistribution\", \"avg\"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
};
apiInstance.getNetworkWirelessClientLatencyStats(networkId, clientId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **clientId** | **String**|  | 
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] 
 **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information. | [optional] 
 **ssid** | **Number**| Filter results by SSID | [optional] 
 **vlan** | **Number**| Filter results by VLAN | [optional] 
 **apTag** | **String**| Filter results by AP Tag | [optional] 
 **fields** | **String**| Partial selection: If present, this call will return only the selected fields of [\&quot;rawDistribution\&quot;, \&quot;avg\&quot;]. All fields will be returned by default. Selected fields must be entered as a comma separated string. | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessClientsConnectionStats

> [Object] getNetworkWirelessClientsConnectionStats(networkId, opts)

Aggregated connectivity info for this network, grouped by clients

Aggregated connectivity info for this network, grouped by clients

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
  'band': "band_example", // String | Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
  'ssid': 56, // Number | Filter results by SSID
  'vlan': 56, // Number | Filter results by VLAN
  'apTag': "apTag_example" // String | Filter results by AP Tag
};
apiInstance.getNetworkWirelessClientsConnectionStats(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] 
 **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information. | [optional] 
 **ssid** | **Number**| Filter results by SSID | [optional] 
 **vlan** | **Number**| Filter results by VLAN | [optional] 
 **apTag** | **String**| Filter results by AP Tag | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessClientsLatencyStats

> [Object] getNetworkWirelessClientsLatencyStats(networkId, opts)

Aggregated latency info for this network, grouped by clients

Aggregated latency info for this network, grouped by clients

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
  'band': "band_example", // String | Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
  'ssid': 56, // Number | Filter results by SSID
  'vlan': 56, // Number | Filter results by VLAN
  'apTag': "apTag_example", // String | Filter results by AP Tag
  'fields': "fields_example" // String | Partial selection: If present, this call will return only the selected fields of [\"rawDistribution\", \"avg\"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
};
apiInstance.getNetworkWirelessClientsLatencyStats(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] 
 **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information. | [optional] 
 **ssid** | **Number**| Filter results by SSID | [optional] 
 **vlan** | **Number**| Filter results by VLAN | [optional] 
 **apTag** | **String**| Filter results by AP Tag | [optional] 
 **fields** | **String**| Partial selection: If present, this call will return only the selected fields of [\&quot;rawDistribution\&quot;, \&quot;avg\&quot;]. All fields will be returned by default. Selected fields must be entered as a comma separated string. | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessConnectionStats

> GetNetworkWirelessConnectionStats200Response getNetworkWirelessConnectionStats(networkId, opts)

Aggregated connectivity info for this network

Aggregated connectivity info for this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
  'band': "band_example", // String | Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
  'ssid': 56, // Number | Filter results by SSID
  'vlan': 56, // Number | Filter results by VLAN
  'apTag': "apTag_example" // String | Filter results by AP Tag
};
apiInstance.getNetworkWirelessConnectionStats(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] 
 **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information. | [optional] 
 **ssid** | **Number**| Filter results by SSID | [optional] 
 **vlan** | **Number**| Filter results by VLAN | [optional] 
 **apTag** | **String**| Filter results by AP Tag | [optional] 

### Return type

[**GetNetworkWirelessConnectionStats200Response**](GetNetworkWirelessConnectionStats200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessDataRateHistory

> [GetNetworkWirelessDataRateHistory200ResponseInner] getNetworkWirelessDataRateHistory(networkId, opts)

Return PHY data rates over time for a network, device, or network client

Return PHY data rates over time for a network, device, or network client

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
  'resolution': 56, // Number | The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400.
  'autoResolution': true, // Boolean | Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false.
  'clientId': "clientId_example", // String | Filter results by network client.
  'deviceSerial': "deviceSerial_example", // String | Filter results by device.
  'apTag': "apTag_example", // String | Filter results by AP tag.
  'band': "band_example", // String | Filter results by band (either '2.4', '5' or '6').
  'ssid': 56 // Number | Filter results by SSID number.
};
apiInstance.getNetworkWirelessDataRateHistory(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days. | [optional] 
 **resolution** | **Number**| The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400. | [optional] 
 **autoResolution** | **Boolean**| Automatically select a data resolution based on the given timespan; this overrides the value specified by the &#39;resolution&#39; parameter. The default setting is false. | [optional] 
 **clientId** | **String**| Filter results by network client. | [optional] 
 **deviceSerial** | **String**| Filter results by device. | [optional] 
 **apTag** | **String**| Filter results by AP tag. | [optional] 
 **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). | [optional] 
 **ssid** | **Number**| Filter results by SSID number. | [optional] 

### Return type

[**[GetNetworkWirelessDataRateHistory200ResponseInner]**](GetNetworkWirelessDataRateHistory200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessDevicesConnectionStats

> [GetDeviceWirelessConnectionStats200Response] getNetworkWirelessDevicesConnectionStats(networkId, opts)

Aggregated connectivity info for this network, grouped by node

Aggregated connectivity info for this network, grouped by node

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
  'band': "band_example", // String | Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
  'ssid': 56, // Number | Filter results by SSID
  'vlan': 56, // Number | Filter results by VLAN
  'apTag': "apTag_example" // String | Filter results by AP Tag
};
apiInstance.getNetworkWirelessDevicesConnectionStats(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] 
 **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information. | [optional] 
 **ssid** | **Number**| Filter results by SSID | [optional] 
 **vlan** | **Number**| Filter results by VLAN | [optional] 
 **apTag** | **String**| Filter results by AP Tag | [optional] 

### Return type

[**[GetDeviceWirelessConnectionStats200Response]**](GetDeviceWirelessConnectionStats200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessDevicesLatencyStats

> [Object] getNetworkWirelessDevicesLatencyStats(networkId, opts)

Aggregated latency info for this network, grouped by node

Aggregated latency info for this network, grouped by node

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
  'band': "band_example", // String | Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
  'ssid': 56, // Number | Filter results by SSID
  'vlan': 56, // Number | Filter results by VLAN
  'apTag': "apTag_example", // String | Filter results by AP Tag
  'fields': "fields_example" // String | Partial selection: If present, this call will return only the selected fields of [\"rawDistribution\", \"avg\"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
};
apiInstance.getNetworkWirelessDevicesLatencyStats(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] 
 **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information. | [optional] 
 **ssid** | **Number**| Filter results by SSID | [optional] 
 **vlan** | **Number**| Filter results by VLAN | [optional] 
 **apTag** | **String**| Filter results by AP Tag | [optional] 
 **fields** | **String**| Partial selection: If present, this call will return only the selected fields of [\&quot;rawDistribution\&quot;, \&quot;avg\&quot;]. All fields will be returned by default. Selected fields must be entered as a comma separated string. | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessFailedConnections

> [GetNetworkWirelessFailedConnections200ResponseInner] getNetworkWirelessFailedConnections(networkId, opts)

List of all failed client connection events on this network in a given time range

List of all failed client connection events on this network in a given time range

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
  'band': "band_example", // String | Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
  'ssid': 56, // Number | Filter results by SSID
  'vlan': 56, // Number | Filter results by VLAN
  'apTag': "apTag_example", // String | Filter results by AP Tag
  'serial': "serial_example", // String | Filter by AP
  'clientId': "clientId_example" // String | Filter by client MAC
};
apiInstance.getNetworkWirelessFailedConnections(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] 
 **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information. | [optional] 
 **ssid** | **Number**| Filter results by SSID | [optional] 
 **vlan** | **Number**| Filter results by VLAN | [optional] 
 **apTag** | **String**| Filter results by AP Tag | [optional] 
 **serial** | **String**| Filter by AP | [optional] 
 **clientId** | **String**| Filter by client MAC | [optional] 

### Return type

[**[GetNetworkWirelessFailedConnections200ResponseInner]**](GetNetworkWirelessFailedConnections200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessLatencyHistory

> [GetNetworkWirelessLatencyHistory200ResponseInner] getNetworkWirelessLatencyHistory(networkId, opts)

Return average wireless latency over time for a network, device, or network client

Return average wireless latency over time for a network, device, or network client

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
  'resolution': 56, // Number | The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400.
  'autoResolution': true, // Boolean | Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false.
  'clientId': "clientId_example", // String | Filter results by network client.
  'deviceSerial': "deviceSerial_example", // String | Filter results by device.
  'apTag': "apTag_example", // String | Filter results by AP tag.
  'band': "band_example", // String | Filter results by band (either '2.4', '5' or '6').
  'ssid': 56, // Number | Filter results by SSID number.
  'accessCategory': "accessCategory_example" // String | Filter by access category.
};
apiInstance.getNetworkWirelessLatencyHistory(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days. | [optional] 
 **resolution** | **Number**| The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400. | [optional] 
 **autoResolution** | **Boolean**| Automatically select a data resolution based on the given timespan; this overrides the value specified by the &#39;resolution&#39; parameter. The default setting is false. | [optional] 
 **clientId** | **String**| Filter results by network client. | [optional] 
 **deviceSerial** | **String**| Filter results by device. | [optional] 
 **apTag** | **String**| Filter results by AP tag. | [optional] 
 **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). | [optional] 
 **ssid** | **Number**| Filter results by SSID number. | [optional] 
 **accessCategory** | **String**| Filter by access category. | [optional] 

### Return type

[**[GetNetworkWirelessLatencyHistory200ResponseInner]**](GetNetworkWirelessLatencyHistory200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessLatencyStats

> Object getNetworkWirelessLatencyStats(networkId, opts)

Aggregated latency info for this network

Aggregated latency info for this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
  'band': "band_example", // String | Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
  'ssid': 56, // Number | Filter results by SSID
  'vlan': 56, // Number | Filter results by VLAN
  'apTag': "apTag_example", // String | Filter results by AP Tag
  'fields': "fields_example" // String | Partial selection: If present, this call will return only the selected fields of [\"rawDistribution\", \"avg\"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
};
apiInstance.getNetworkWirelessLatencyStats(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] 
 **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information. | [optional] 
 **ssid** | **Number**| Filter results by SSID | [optional] 
 **vlan** | **Number**| Filter results by VLAN | [optional] 
 **apTag** | **String**| Filter results by AP Tag | [optional] 
 **fields** | **String**| Partial selection: If present, this call will return only the selected fields of [\&quot;rawDistribution\&quot;, \&quot;avg\&quot;]. All fields will be returned by default. Selected fields must be entered as a comma separated string. | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessMeshStatuses

> Object getNetworkWirelessMeshStatuses(networkId, opts)

List wireless mesh statuses for repeaters

List wireless mesh statuses for repeaters

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 3 - 500. Default is 50.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example" // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
};
apiInstance.getNetworkWirelessMeshStatuses(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **perPage** | **Number**| The number of entries per page returned. Acceptable range is 3 - 500. Default is 50. | [optional] 
 **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessRfProfile

> Object getNetworkWirelessRfProfile(networkId, rfProfileId)

Return a RF profile

Return a RF profile

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let rfProfileId = "rfProfileId_example"; // String | 
apiInstance.getNetworkWirelessRfProfile(networkId, rfProfileId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **rfProfileId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessRfProfiles

> [Object] getNetworkWirelessRfProfiles(networkId, opts)

List the non-basic RF profiles for this network

List the non-basic RF profiles for this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'includeTemplateProfiles': true // Boolean | If the network is bound to a template, this parameter controls whether or not the non-basic RF profiles defined on the template should be included in the response alongside the non-basic profiles defined on the bound network. Defaults to false.
};
apiInstance.getNetworkWirelessRfProfiles(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **includeTemplateProfiles** | **Boolean**| If the network is bound to a template, this parameter controls whether or not the non-basic RF profiles defined on the template should be included in the response alongside the non-basic profiles defined on the bound network. Defaults to false. | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessSettings

> GetNetworkWirelessSettings200Response getNetworkWirelessSettings(networkId)

Return the wireless settings for a network

Return the wireless settings for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkWirelessSettings(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

[**GetNetworkWirelessSettings200Response**](GetNetworkWirelessSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessSignalQualityHistory

> [GetNetworkWirelessSignalQualityHistory200ResponseInner] getNetworkWirelessSignalQualityHistory(networkId, opts)

Return signal quality (SNR/RSSI) over time for a device or network client

Return signal quality (SNR/RSSI) over time for a device or network client

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
  'resolution': 56, // Number | The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400.
  'autoResolution': true, // Boolean | Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false.
  'clientId': "clientId_example", // String | Filter results by network client.
  'deviceSerial': "deviceSerial_example", // String | Filter results by device.
  'apTag': "apTag_example", // String | Filter results by AP tag; either :clientId or :deviceSerial must be jointly specified.
  'band': "band_example", // String | Filter results by band (either '2.4', '5' or '6').
  'ssid': 56 // Number | Filter results by SSID number.
};
apiInstance.getNetworkWirelessSignalQualityHistory(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days. | [optional] 
 **resolution** | **Number**| The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400. | [optional] 
 **autoResolution** | **Boolean**| Automatically select a data resolution based on the given timespan; this overrides the value specified by the &#39;resolution&#39; parameter. The default setting is false. | [optional] 
 **clientId** | **String**| Filter results by network client. | [optional] 
 **deviceSerial** | **String**| Filter results by device. | [optional] 
 **apTag** | **String**| Filter results by AP tag; either :clientId or :deviceSerial must be jointly specified. | [optional] 
 **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). | [optional] 
 **ssid** | **Number**| Filter results by SSID number. | [optional] 

### Return type

[**[GetNetworkWirelessSignalQualityHistory200ResponseInner]**](GetNetworkWirelessSignalQualityHistory200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessSsid

> Object getNetworkWirelessSsid(networkId, number)

Return a single MR SSID

Return a single MR SSID

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
apiInstance.getNetworkWirelessSsid(networkId, number, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessSsidBonjourForwarding

> Object getNetworkWirelessSsidBonjourForwarding(networkId, number)

List the Bonjour forwarding setting and rules for the SSID

List the Bonjour forwarding setting and rules for the SSID

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
apiInstance.getNetworkWirelessSsidBonjourForwarding(networkId, number, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessSsidDeviceTypeGroupPolicies

> Object getNetworkWirelessSsidDeviceTypeGroupPolicies(networkId, number)

List the device type group policies for the SSID

List the device type group policies for the SSID

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
apiInstance.getNetworkWirelessSsidDeviceTypeGroupPolicies(networkId, number, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessSsidEapOverride

> GetNetworkWirelessSsidEapOverride200Response getNetworkWirelessSsidEapOverride(networkId, number)

Return the EAP overridden parameters for an SSID

Return the EAP overridden parameters for an SSID

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
apiInstance.getNetworkWirelessSsidEapOverride(networkId, number, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 

### Return type

[**GetNetworkWirelessSsidEapOverride200Response**](GetNetworkWirelessSsidEapOverride200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessSsidFirewallL3FirewallRules

> Object getNetworkWirelessSsidFirewallL3FirewallRules(networkId, number)

Return the L3 firewall rules for an SSID on an MR network

Return the L3 firewall rules for an SSID on an MR network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
apiInstance.getNetworkWirelessSsidFirewallL3FirewallRules(networkId, number, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessSsidFirewallL7FirewallRules

> Object getNetworkWirelessSsidFirewallL7FirewallRules(networkId, number)

Return the L7 firewall rules for an SSID on an MR network

Return the L7 firewall rules for an SSID on an MR network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
apiInstance.getNetworkWirelessSsidFirewallL7FirewallRules(networkId, number, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessSsidHotspot20

> Object getNetworkWirelessSsidHotspot20(networkId, number)

Return the Hotspot 2.0 settings for an SSID

Return the Hotspot 2.0 settings for an SSID

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
apiInstance.getNetworkWirelessSsidHotspot20(networkId, number, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessSsidIdentityPsk

> GetNetworkWirelessSsidIdentityPsks200ResponseInner getNetworkWirelessSsidIdentityPsk(networkId, number, identityPskId)

Return an Identity PSK

Return an Identity PSK

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
let identityPskId = "identityPskId_example"; // String | 
apiInstance.getNetworkWirelessSsidIdentityPsk(networkId, number, identityPskId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 
 **identityPskId** | **String**|  | 

### Return type

[**GetNetworkWirelessSsidIdentityPsks200ResponseInner**](GetNetworkWirelessSsidIdentityPsks200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessSsidIdentityPsks

> [GetNetworkWirelessSsidIdentityPsks200ResponseInner] getNetworkWirelessSsidIdentityPsks(networkId, number)

List all Identity PSKs in a wireless network

List all Identity PSKs in a wireless network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
apiInstance.getNetworkWirelessSsidIdentityPsks(networkId, number, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 

### Return type

[**[GetNetworkWirelessSsidIdentityPsks200ResponseInner]**](GetNetworkWirelessSsidIdentityPsks200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessSsidSchedules

> Object getNetworkWirelessSsidSchedules(networkId, number)

List the outage schedule for the SSID

List the outage schedule for the SSID

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
apiInstance.getNetworkWirelessSsidSchedules(networkId, number, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessSsidSplashSettings

> GetNetworkWirelessSsidSplashSettings200Response getNetworkWirelessSsidSplashSettings(networkId, number)

Display the splash page settings for the given SSID

Display the splash page settings for the given SSID

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
apiInstance.getNetworkWirelessSsidSplashSettings(networkId, number, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 

### Return type

[**GetNetworkWirelessSsidSplashSettings200Response**](GetNetworkWirelessSsidSplashSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessSsidTrafficShapingRules

> Object getNetworkWirelessSsidTrafficShapingRules(networkId, number)

Display the traffic shaping settings for a SSID on an MR network

Display the traffic shaping settings for a SSID on an MR network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
apiInstance.getNetworkWirelessSsidTrafficShapingRules(networkId, number, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessSsidVpn

> Object getNetworkWirelessSsidVpn(networkId, number)

List the VPN settings for the SSID.

List the VPN settings for the SSID.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
apiInstance.getNetworkWirelessSsidVpn(networkId, number, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessSsids

> [Object] getNetworkWirelessSsids(networkId)

List the MR SSIDs in a network

List the MR SSIDs in a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkWirelessSsids(networkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessUsageHistory

> [GetNetworkWirelessUsageHistory200ResponseInner] getNetworkWirelessUsageHistory(networkId, opts)

Return AP usage over time for a device or network client

Return AP usage over time for a device or network client

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
  'resolution': 56, // Number | The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400.
  'autoResolution': true, // Boolean | Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false.
  'clientId': "clientId_example", // String | Filter results by network client to return per-device AP usage over time inner joined by the queried client's connection history.
  'deviceSerial': "deviceSerial_example", // String | Filter results by device. Requires :band.
  'apTag': "apTag_example", // String | Filter results by AP tag; either :clientId or :deviceSerial must be jointly specified.
  'band': "band_example", // String | Filter results by band (either '2.4', '5' or '6').
  'ssid': 56 // Number | Filter results by SSID number.
};
apiInstance.getNetworkWirelessUsageHistory(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days. | [optional] 
 **resolution** | **Number**| The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400. | [optional] 
 **autoResolution** | **Boolean**| Automatically select a data resolution based on the given timespan; this overrides the value specified by the &#39;resolution&#39; parameter. The default setting is false. | [optional] 
 **clientId** | **String**| Filter results by network client to return per-device AP usage over time inner joined by the queried client&#39;s connection history. | [optional] 
 **deviceSerial** | **String**| Filter results by device. Requires :band. | [optional] 
 **apTag** | **String**| Filter results by AP tag; either :clientId or :deviceSerial must be jointly specified. | [optional] 
 **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). | [optional] 
 **ssid** | **Number**| Filter results by SSID number. | [optional] 

### Return type

[**[GetNetworkWirelessUsageHistory200ResponseInner]**](GetNetworkWirelessUsageHistory200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationWirelessDevicesEthernetStatuses

> [GetOrganizationWirelessDevicesEthernetStatuses200ResponseInner] getOrganizationWirelessDevicesEthernetStatuses(organizationId, opts)

Endpoint to see power status for wireless devices

Endpoint to see power status for wireless devices

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example", // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'networkIds': ["null"] // [String] | A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]=N_12345678&networkIds[]=L_3456
};
apiInstance.getOrganizationWirelessDevicesEthernetStatuses(organizationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **perPage** | **Number**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100. | [optional] 
 **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **networkIds** | [**[String]**](String.md)| A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]&#x3D;N_12345678&amp;networkIds[]&#x3D;L_3456 | [optional] 

### Return type

[**[GetOrganizationWirelessDevicesEthernetStatuses200ResponseInner]**](GetOrganizationWirelessDevicesEthernetStatuses200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateDeviceWirelessBluetoothSettings

> GetDeviceWirelessBluetoothSettings200Response updateDeviceWirelessBluetoothSettings(serial, opts)

Update the bluetooth settings for a wireless device

Update the bluetooth settings for a wireless device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let serial = "serial_example"; // String | 
let opts = {
  'updateDeviceWirelessBluetoothSettingsRequest': new MerakiDashboardApi.UpdateDeviceWirelessBluetoothSettingsRequest() // UpdateDeviceWirelessBluetoothSettingsRequest | 
};
apiInstance.updateDeviceWirelessBluetoothSettings(serial, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 
 **updateDeviceWirelessBluetoothSettingsRequest** | [**UpdateDeviceWirelessBluetoothSettingsRequest**](UpdateDeviceWirelessBluetoothSettingsRequest.md)|  | [optional] 

### Return type

[**GetDeviceWirelessBluetoothSettings200Response**](GetDeviceWirelessBluetoothSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDeviceWirelessRadioSettings

> Object updateDeviceWirelessRadioSettings(serial, opts)

Update the radio settings of a device

Update the radio settings of a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let serial = "serial_example"; // String | 
let opts = {
  'updateDeviceWirelessRadioSettingsRequest': new MerakiDashboardApi.UpdateDeviceWirelessRadioSettingsRequest() // UpdateDeviceWirelessRadioSettingsRequest | 
};
apiInstance.updateDeviceWirelessRadioSettings(serial, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **String**|  | 
 **updateDeviceWirelessRadioSettingsRequest** | [**UpdateDeviceWirelessRadioSettingsRequest**](UpdateDeviceWirelessRadioSettingsRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessAlternateManagementInterface

> Object updateNetworkWirelessAlternateManagementInterface(networkId, opts)

Update alternate management interface and device static IP

Update alternate management interface and device static IP

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkWirelessAlternateManagementInterfaceRequest': new MerakiDashboardApi.UpdateNetworkWirelessAlternateManagementInterfaceRequest() // UpdateNetworkWirelessAlternateManagementInterfaceRequest | 
};
apiInstance.updateNetworkWirelessAlternateManagementInterface(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkWirelessAlternateManagementInterfaceRequest** | [**UpdateNetworkWirelessAlternateManagementInterfaceRequest**](UpdateNetworkWirelessAlternateManagementInterfaceRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessBilling

> Object updateNetworkWirelessBilling(networkId, opts)

Update the billing settings

Update the billing settings

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkWirelessBillingRequest': new MerakiDashboardApi.UpdateNetworkWirelessBillingRequest() // UpdateNetworkWirelessBillingRequest | 
};
apiInstance.updateNetworkWirelessBilling(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkWirelessBillingRequest** | [**UpdateNetworkWirelessBillingRequest**](UpdateNetworkWirelessBillingRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessBluetoothSettings

> GetNetworkWirelessBluetoothSettings200Response updateNetworkWirelessBluetoothSettings(networkId, opts)

Update the Bluetooth settings for a network

Update the Bluetooth settings for a network. See the docs page for &lt;a href&#x3D;\&quot;https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\&quot;&gt;Bluetooth settings&lt;/a&gt;.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkWirelessBluetoothSettingsRequest': new MerakiDashboardApi.UpdateNetworkWirelessBluetoothSettingsRequest() // UpdateNetworkWirelessBluetoothSettingsRequest | 
};
apiInstance.updateNetworkWirelessBluetoothSettings(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkWirelessBluetoothSettingsRequest** | [**UpdateNetworkWirelessBluetoothSettingsRequest**](UpdateNetworkWirelessBluetoothSettingsRequest.md)|  | [optional] 

### Return type

[**GetNetworkWirelessBluetoothSettings200Response**](GetNetworkWirelessBluetoothSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessRfProfile

> CreateNetworkWirelessRfProfile201Response updateNetworkWirelessRfProfile(networkId, rfProfileId, opts)

Updates specified RF profile for this network

Updates specified RF profile for this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let rfProfileId = "rfProfileId_example"; // String | 
let opts = {
  'updateNetworkWirelessRfProfileRequest': new MerakiDashboardApi.UpdateNetworkWirelessRfProfileRequest() // UpdateNetworkWirelessRfProfileRequest | 
};
apiInstance.updateNetworkWirelessRfProfile(networkId, rfProfileId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **rfProfileId** | **String**|  | 
 **updateNetworkWirelessRfProfileRequest** | [**UpdateNetworkWirelessRfProfileRequest**](UpdateNetworkWirelessRfProfileRequest.md)|  | [optional] 

### Return type

[**CreateNetworkWirelessRfProfile201Response**](CreateNetworkWirelessRfProfile201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessSettings

> GetNetworkWirelessSettings200Response updateNetworkWirelessSettings(networkId, opts)

Update the wireless settings for a network

Update the wireless settings for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkWirelessSettingsRequest': new MerakiDashboardApi.UpdateNetworkWirelessSettingsRequest() // UpdateNetworkWirelessSettingsRequest | 
};
apiInstance.updateNetworkWirelessSettings(networkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **updateNetworkWirelessSettingsRequest** | [**UpdateNetworkWirelessSettingsRequest**](UpdateNetworkWirelessSettingsRequest.md)|  | [optional] 

### Return type

[**GetNetworkWirelessSettings200Response**](GetNetworkWirelessSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessSsid

> Object updateNetworkWirelessSsid(networkId, number, opts)

Update the attributes of an MR SSID

Update the attributes of an MR SSID

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
let opts = {
  'updateNetworkWirelessSsidRequest': new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest() // UpdateNetworkWirelessSsidRequest | 
};
apiInstance.updateNetworkWirelessSsid(networkId, number, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 
 **updateNetworkWirelessSsidRequest** | [**UpdateNetworkWirelessSsidRequest**](UpdateNetworkWirelessSsidRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessSsidBonjourForwarding

> Object updateNetworkWirelessSsidBonjourForwarding(networkId, number, opts)

Update the bonjour forwarding setting and rules for the SSID

Update the bonjour forwarding setting and rules for the SSID

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
let opts = {
  'updateNetworkWirelessSsidBonjourForwardingRequest': new MerakiDashboardApi.UpdateNetworkWirelessSsidBonjourForwardingRequest() // UpdateNetworkWirelessSsidBonjourForwardingRequest | 
};
apiInstance.updateNetworkWirelessSsidBonjourForwarding(networkId, number, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 
 **updateNetworkWirelessSsidBonjourForwardingRequest** | [**UpdateNetworkWirelessSsidBonjourForwardingRequest**](UpdateNetworkWirelessSsidBonjourForwardingRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessSsidDeviceTypeGroupPolicies

> Object updateNetworkWirelessSsidDeviceTypeGroupPolicies(networkId, number, opts)

Update the device type group policies for the SSID

Update the device type group policies for the SSID

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
let opts = {
  'updateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest': new MerakiDashboardApi.UpdateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest() // UpdateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest | 
};
apiInstance.updateNetworkWirelessSsidDeviceTypeGroupPolicies(networkId, number, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 
 **updateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest** | [**UpdateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest**](UpdateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessSsidEapOverride

> GetNetworkWirelessSsidEapOverride200Response updateNetworkWirelessSsidEapOverride(networkId, number, opts)

Update the EAP overridden parameters for an SSID.

Update the EAP overridden parameters for an SSID.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
let opts = {
  'updateNetworkWirelessSsidEapOverrideRequest': new MerakiDashboardApi.UpdateNetworkWirelessSsidEapOverrideRequest() // UpdateNetworkWirelessSsidEapOverrideRequest | 
};
apiInstance.updateNetworkWirelessSsidEapOverride(networkId, number, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 
 **updateNetworkWirelessSsidEapOverrideRequest** | [**UpdateNetworkWirelessSsidEapOverrideRequest**](UpdateNetworkWirelessSsidEapOverrideRequest.md)|  | [optional] 

### Return type

[**GetNetworkWirelessSsidEapOverride200Response**](GetNetworkWirelessSsidEapOverride200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessSsidFirewallL3FirewallRules

> Object updateNetworkWirelessSsidFirewallL3FirewallRules(networkId, number, opts)

Update the L3 firewall rules of an SSID on an MR network

Update the L3 firewall rules of an SSID on an MR network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
let opts = {
  'updateNetworkWirelessSsidFirewallL3FirewallRulesRequest': new MerakiDashboardApi.UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest() // UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest | 
};
apiInstance.updateNetworkWirelessSsidFirewallL3FirewallRules(networkId, number, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 
 **updateNetworkWirelessSsidFirewallL3FirewallRulesRequest** | [**UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest**](UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessSsidFirewallL7FirewallRules

> Object updateNetworkWirelessSsidFirewallL7FirewallRules(networkId, number, opts)

Update the L7 firewall rules of an SSID on an MR network

Update the L7 firewall rules of an SSID on an MR network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
let opts = {
  'updateNetworkWirelessSsidFirewallL7FirewallRulesRequest': new MerakiDashboardApi.UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest() // UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest | 
};
apiInstance.updateNetworkWirelessSsidFirewallL7FirewallRules(networkId, number, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 
 **updateNetworkWirelessSsidFirewallL7FirewallRulesRequest** | [**UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest**](UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessSsidHotspot20

> Object updateNetworkWirelessSsidHotspot20(networkId, number, opts)

Update the Hotspot 2.0 settings of an SSID

Update the Hotspot 2.0 settings of an SSID

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
let opts = {
  'updateNetworkWirelessSsidHotspot20Request': new MerakiDashboardApi.UpdateNetworkWirelessSsidHotspot20Request() // UpdateNetworkWirelessSsidHotspot20Request | 
};
apiInstance.updateNetworkWirelessSsidHotspot20(networkId, number, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 
 **updateNetworkWirelessSsidHotspot20Request** | [**UpdateNetworkWirelessSsidHotspot20Request**](UpdateNetworkWirelessSsidHotspot20Request.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessSsidIdentityPsk

> Object updateNetworkWirelessSsidIdentityPsk(networkId, number, identityPskId, opts)

Update an Identity PSK

Update an Identity PSK

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
let identityPskId = "identityPskId_example"; // String | 
let opts = {
  'updateNetworkWirelessSsidIdentityPskRequest': new MerakiDashboardApi.UpdateNetworkWirelessSsidIdentityPskRequest() // UpdateNetworkWirelessSsidIdentityPskRequest | 
};
apiInstance.updateNetworkWirelessSsidIdentityPsk(networkId, number, identityPskId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 
 **identityPskId** | **String**|  | 
 **updateNetworkWirelessSsidIdentityPskRequest** | [**UpdateNetworkWirelessSsidIdentityPskRequest**](UpdateNetworkWirelessSsidIdentityPskRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessSsidSchedules

> Object updateNetworkWirelessSsidSchedules(networkId, number, opts)

Update the outage schedule for the SSID

Update the outage schedule for the SSID

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
let opts = {
  'updateNetworkWirelessSsidSchedulesRequest': new MerakiDashboardApi.UpdateNetworkWirelessSsidSchedulesRequest() // UpdateNetworkWirelessSsidSchedulesRequest | 
};
apiInstance.updateNetworkWirelessSsidSchedules(networkId, number, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 
 **updateNetworkWirelessSsidSchedulesRequest** | [**UpdateNetworkWirelessSsidSchedulesRequest**](UpdateNetworkWirelessSsidSchedulesRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessSsidSplashSettings

> GetNetworkWirelessSsidSplashSettings200Response updateNetworkWirelessSsidSplashSettings(networkId, number, opts)

Modify the splash page settings for the given SSID

Modify the splash page settings for the given SSID

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
let opts = {
  'updateNetworkWirelessSsidSplashSettingsRequest': new MerakiDashboardApi.UpdateNetworkWirelessSsidSplashSettingsRequest() // UpdateNetworkWirelessSsidSplashSettingsRequest | 
};
apiInstance.updateNetworkWirelessSsidSplashSettings(networkId, number, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 
 **updateNetworkWirelessSsidSplashSettingsRequest** | [**UpdateNetworkWirelessSsidSplashSettingsRequest**](UpdateNetworkWirelessSsidSplashSettingsRequest.md)|  | [optional] 

### Return type

[**GetNetworkWirelessSsidSplashSettings200Response**](GetNetworkWirelessSsidSplashSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessSsidTrafficShapingRules

> Object updateNetworkWirelessSsidTrafficShapingRules(networkId, number, opts)

Update the traffic shaping settings for an SSID on an MR network

Update the traffic shaping settings for an SSID on an MR network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
let opts = {
  'updateNetworkWirelessSsidTrafficShapingRulesRequest': new MerakiDashboardApi.UpdateNetworkWirelessSsidTrafficShapingRulesRequest() // UpdateNetworkWirelessSsidTrafficShapingRulesRequest | 
};
apiInstance.updateNetworkWirelessSsidTrafficShapingRules(networkId, number, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 
 **updateNetworkWirelessSsidTrafficShapingRulesRequest** | [**UpdateNetworkWirelessSsidTrafficShapingRulesRequest**](UpdateNetworkWirelessSsidTrafficShapingRulesRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessSsidVpn

> Object updateNetworkWirelessSsidVpn(networkId, number, opts)

Update the VPN settings for the SSID

Update the VPN settings for the SSID

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
let opts = {
  'updateNetworkWirelessSsidVpnRequest': new MerakiDashboardApi.UpdateNetworkWirelessSsidVpnRequest() // UpdateNetworkWirelessSsidVpnRequest | 
};
apiInstance.updateNetworkWirelessSsidVpn(networkId, number, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **networkId** | **String**|  | 
 **number** | **String**|  | 
 **updateNetworkWirelessSsidVpnRequest** | [**UpdateNetworkWirelessSsidVpnRequest**](UpdateNetworkWirelessSsidVpnRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

