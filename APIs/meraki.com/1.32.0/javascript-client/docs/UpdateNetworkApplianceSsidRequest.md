# MerakiDashboardApi.UpdateNetworkApplianceSsidRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authMode** | **String** | The association control method for the SSID (&#39;open&#39;, &#39;psk&#39;, &#39;8021x-meraki&#39; or &#39;8021x-radius&#39;). | [optional] 
**defaultVlanId** | **Number** | The VLAN ID of the VLAN associated to this SSID. This parameter is only valid if the network is in routed mode. | [optional] 
**dhcpEnforcedDeauthentication** | [**UpdateNetworkApplianceSsidRequestDhcpEnforcedDeauthentication**](UpdateNetworkApplianceSsidRequestDhcpEnforcedDeauthentication.md) |  | [optional] 
**enabled** | **Boolean** | Whether or not the SSID is enabled. | [optional] 
**encryptionMode** | **String** | The psk encryption mode for the SSID (&#39;wep&#39; or &#39;wpa&#39;). This param is only valid if the authMode is &#39;psk&#39;. | [optional] 
**name** | **String** | The name of the SSID. | [optional] 
**psk** | **String** | The passkey for the SSID. This param is only valid if the authMode is &#39;psk&#39;. | [optional] 
**radiusServers** | [**[UpdateNetworkApplianceSsidRequestRadiusServersInner]**](UpdateNetworkApplianceSsidRequestRadiusServersInner.md) | The RADIUS 802.1x servers to be used for authentication. This param is only valid if the authMode is &#39;8021x-radius&#39;. | [optional] 
**visible** | **Boolean** | Boolean indicating whether the MX should advertise or hide this SSID. | [optional] 
**wpaEncryptionMode** | **String** | The types of WPA encryption. (&#39;WPA1 and WPA2&#39;, &#39;WPA2 only&#39;, &#39;WPA3 Transition Mode&#39; or &#39;WPA3 only&#39;). This param is only valid if (1) the authMode is &#39;psk&#39; &amp; the encryptionMode is &#39;wpa&#39; OR (2) the authMode is &#39;8021x-meraki&#39; OR (3) the authMode is &#39;8021x-radius&#39; | [optional] 



## Enum: AuthModeEnum


* `8021x-meraki` (value: `"8021x-meraki"`)

* `8021x-radius` (value: `"8021x-radius"`)

* `open` (value: `"open"`)

* `psk` (value: `"psk"`)





## Enum: EncryptionModeEnum


* `wep` (value: `"wep"`)

* `wpa` (value: `"wpa"`)





## Enum: WpaEncryptionModeEnum


* `WPA1 and WPA2` (value: `"WPA1 and WPA2"`)

* `WPA2 only` (value: `"WPA2 only"`)

* `WPA3 Transition Mode` (value: `"WPA3 Transition Mode"`)

* `WPA3 only` (value: `"WPA3 only"`)




