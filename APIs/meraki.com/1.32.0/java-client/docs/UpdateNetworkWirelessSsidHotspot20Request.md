

# UpdateNetworkWirelessSsidHotspot20Request


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**domains** | **List&lt;String&gt;** | An array of domain names |  [optional] |
|**enabled** | **Boolean** | Whether or not Hotspot 2.0 for this SSID is enabled |  [optional] |
|**mccMncs** | [**List&lt;UpdateNetworkWirelessSsidHotspot20RequestMccMncsInner&gt;**](UpdateNetworkWirelessSsidHotspot20RequestMccMncsInner.md) | An array of MCC/MNC pairs |  [optional] |
|**naiRealms** | [**List&lt;UpdateNetworkWirelessSsidHotspot20RequestNaiRealmsInner&gt;**](UpdateNetworkWirelessSsidHotspot20RequestNaiRealmsInner.md) | An array of NAI realms |  [optional] |
|**networkAccessType** | [**NetworkAccessTypeEnum**](#NetworkAccessTypeEnum) | The network type of this SSID (&#39;Private network&#39;, &#39;Private network with guest access&#39;, &#39;Chargeable public network&#39;, &#39;Free public network&#39;, &#39;Personal device network&#39;, &#39;Emergency services only network&#39;, &#39;Test or experimental&#39;, &#39;Wildcard&#39;) |  [optional] |
|**operator** | [**UpdateNetworkWirelessSsidHotspot20RequestOperator**](UpdateNetworkWirelessSsidHotspot20RequestOperator.md) |  |  [optional] |
|**roamConsortOis** | **List&lt;String&gt;** | An array of roaming consortium OIs (hexadecimal number 3-5 octets in length) |  [optional] |
|**venue** | [**UpdateNetworkWirelessSsidHotspot20RequestVenue**](UpdateNetworkWirelessSsidHotspot20RequestVenue.md) |  |  [optional] |



## Enum: NetworkAccessTypeEnum

| Name | Value |
|---- | -----|
| CHARGEABLE_PUBLIC_NETWORK | &quot;Chargeable public network&quot; |
| EMERGENCY_SERVICES_ONLY_NETWORK | &quot;Emergency services only network&quot; |
| FREE_PUBLIC_NETWORK | &quot;Free public network&quot; |
| PERSONAL_DEVICE_NETWORK | &quot;Personal device network&quot; |
| PRIVATE_NETWORK | &quot;Private network&quot; |
| PRIVATE_NETWORK_WITH_GUEST_ACCESS | &quot;Private network with guest access&quot; |
| TEST_OR_EXPERIMENTAL | &quot;Test or experimental&quot; |
| WILDCARD | &quot;Wildcard&quot; |



