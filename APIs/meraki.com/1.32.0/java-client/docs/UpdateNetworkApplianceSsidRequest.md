

# UpdateNetworkApplianceSsidRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authMode** | [**AuthModeEnum**](#AuthModeEnum) | The association control method for the SSID (&#39;open&#39;, &#39;psk&#39;, &#39;8021x-meraki&#39; or &#39;8021x-radius&#39;). |  [optional] |
|**defaultVlanId** | **Integer** | The VLAN ID of the VLAN associated to this SSID. This parameter is only valid if the network is in routed mode. |  [optional] |
|**dhcpEnforcedDeauthentication** | [**UpdateNetworkApplianceSsidRequestDhcpEnforcedDeauthentication**](UpdateNetworkApplianceSsidRequestDhcpEnforcedDeauthentication.md) |  |  [optional] |
|**enabled** | **Boolean** | Whether or not the SSID is enabled. |  [optional] |
|**encryptionMode** | [**EncryptionModeEnum**](#EncryptionModeEnum) | The psk encryption mode for the SSID (&#39;wep&#39; or &#39;wpa&#39;). This param is only valid if the authMode is &#39;psk&#39;. |  [optional] |
|**name** | **String** | The name of the SSID. |  [optional] |
|**psk** | **String** | The passkey for the SSID. This param is only valid if the authMode is &#39;psk&#39;. |  [optional] |
|**radiusServers** | [**List&lt;UpdateNetworkApplianceSsidRequestRadiusServersInner&gt;**](UpdateNetworkApplianceSsidRequestRadiusServersInner.md) | The RADIUS 802.1x servers to be used for authentication. This param is only valid if the authMode is &#39;8021x-radius&#39;. |  [optional] |
|**visible** | **Boolean** | Boolean indicating whether the MX should advertise or hide this SSID. |  [optional] |
|**wpaEncryptionMode** | [**WpaEncryptionModeEnum**](#WpaEncryptionModeEnum) | The types of WPA encryption. (&#39;WPA1 and WPA2&#39;, &#39;WPA2 only&#39;, &#39;WPA3 Transition Mode&#39; or &#39;WPA3 only&#39;). This param is only valid if (1) the authMode is &#39;psk&#39; &amp; the encryptionMode is &#39;wpa&#39; OR (2) the authMode is &#39;8021x-meraki&#39; OR (3) the authMode is &#39;8021x-radius&#39; |  [optional] |



## Enum: AuthModeEnum

| Name | Value |
|---- | -----|
| _8021X_MERAKI | &quot;8021x-meraki&quot; |
| _8021X_RADIUS | &quot;8021x-radius&quot; |
| OPEN | &quot;open&quot; |
| PSK | &quot;psk&quot; |



## Enum: EncryptionModeEnum

| Name | Value |
|---- | -----|
| WEP | &quot;wep&quot; |
| WPA | &quot;wpa&quot; |



## Enum: WpaEncryptionModeEnum

| Name | Value |
|---- | -----|
| WPA1_AND_WPA2 | &quot;WPA1 and WPA2&quot; |
| WPA2_ONLY | &quot;WPA2 only&quot; |
| WPA3_TRANSITION_MODE | &quot;WPA3 Transition Mode&quot; |
| WPA3_ONLY | &quot;WPA3 only&quot; |



