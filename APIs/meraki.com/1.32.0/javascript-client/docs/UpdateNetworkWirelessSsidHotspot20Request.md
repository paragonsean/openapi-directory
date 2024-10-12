# MerakiDashboardApi.UpdateNetworkWirelessSsidHotspot20Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | **[String]** | An array of domain names | [optional] 
**enabled** | **Boolean** | Whether or not Hotspot 2.0 for this SSID is enabled | [optional] 
**mccMncs** | [**[UpdateNetworkWirelessSsidHotspot20RequestMccMncsInner]**](UpdateNetworkWirelessSsidHotspot20RequestMccMncsInner.md) | An array of MCC/MNC pairs | [optional] 
**naiRealms** | [**[UpdateNetworkWirelessSsidHotspot20RequestNaiRealmsInner]**](UpdateNetworkWirelessSsidHotspot20RequestNaiRealmsInner.md) | An array of NAI realms | [optional] 
**networkAccessType** | **String** | The network type of this SSID (&#39;Private network&#39;, &#39;Private network with guest access&#39;, &#39;Chargeable public network&#39;, &#39;Free public network&#39;, &#39;Personal device network&#39;, &#39;Emergency services only network&#39;, &#39;Test or experimental&#39;, &#39;Wildcard&#39;) | [optional] 
**operator** | [**UpdateNetworkWirelessSsidHotspot20RequestOperator**](UpdateNetworkWirelessSsidHotspot20RequestOperator.md) |  | [optional] 
**roamConsortOis** | **[String]** | An array of roaming consortium OIs (hexadecimal number 3-5 octets in length) | [optional] 
**venue** | [**UpdateNetworkWirelessSsidHotspot20RequestVenue**](UpdateNetworkWirelessSsidHotspot20RequestVenue.md) |  | [optional] 



## Enum: NetworkAccessTypeEnum


* `Chargeable public network` (value: `"Chargeable public network"`)

* `Emergency services only network` (value: `"Emergency services only network"`)

* `Free public network` (value: `"Free public network"`)

* `Personal device network` (value: `"Personal device network"`)

* `Private network` (value: `"Private network"`)

* `Private network with guest access` (value: `"Private network with guest access"`)

* `Test or experimental` (value: `"Test or experimental"`)

* `Wildcard` (value: `"Wildcard"`)




