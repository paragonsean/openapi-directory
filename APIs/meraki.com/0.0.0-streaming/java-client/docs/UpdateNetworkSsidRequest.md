

# UpdateNetworkSsidRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apTagsAndVlanIds** | [**List&lt;UpdateNetworkSsidRequestApTagsAndVlanIdsInner&gt;**](UpdateNetworkSsidRequestApTagsAndVlanIdsInner.md) | The list of tags and VLAN IDs used for VLAN tagging. This param is only valid when the ipAssignmentMode is &#39;Bridge mode&#39; or &#39;Layer 3 roaming&#39; |  [optional] |
|**authMode** | [**AuthModeEnum**](#AuthModeEnum) | The association control method for the SSID (&#39;open&#39;, &#39;open-enhanced&#39;, &#39;psk&#39;, &#39;open-with-radius&#39;, &#39;open-with-nac&#39;, &#39;8021x-meraki&#39;, &#39;8021x-nac&#39;, &#39;8021x-radius&#39;, &#39;8021x-google&#39;, &#39;8021x-localradius&#39;, &#39;ipsk-with-radius&#39; or &#39;ipsk-without-radius&#39;) |  [optional] |
|**availabilityTags** | **List&lt;String&gt;** | Accepts a list of tags for this SSID. If availableOnAllAps is false, then the SSID will only be broadcast by APs with tags matching any of the tags in this list. |  [optional] |
|**availableOnAllAps** | **Boolean** | Boolean indicating whether all APs should broadcast the SSID or if it should be restricted to APs matching any availability tags. Can only be false if the SSID has availability tags. |  [optional] |
|**bandSelection** | **String** | The client-serving radio frequencies of this SSID in the default indoor RF profile. (&#39;Dual band operation&#39;, &#39;5 GHz band only&#39; or &#39;Dual band operation with Band Steering&#39;) |  [optional] |
|**concentratorNetworkId** | **String** | The concentrator to use when the ipAssignmentMode is &#39;Layer 3 roaming with a concentrator&#39; or &#39;VPN&#39;. |  [optional] |
|**defaultVlanId** | **Integer** | The default VLAN ID used for &#39;all other APs&#39;. This param is only valid when the ipAssignmentMode is &#39;Bridge mode&#39; or &#39;Layer 3 roaming&#39; |  [optional] |
|**disassociateClientsOnVpnFailover** | **Boolean** | Disassociate clients when &#39;VPN&#39; concentrator failover occurs in order to trigger clients to re-associate and generate new DHCP requests. This param is only valid if ipAssignmentMode is &#39;VPN&#39;. |  [optional] |
|**enabled** | **Boolean** | Whether or not the SSID is enabled |  [optional] |
|**encryptionMode** | [**EncryptionModeEnum**](#EncryptionModeEnum) | The psk encryption mode for the SSID (&#39;wep&#39; or &#39;wpa&#39;). This param is only valid if the authMode is &#39;psk&#39; |  [optional] |
|**enterpriseAdminAccess** | [**EnterpriseAdminAccessEnum**](#EnterpriseAdminAccessEnum) | Whether or not an SSID is accessible by &#39;enterprise&#39; administrators (&#39;access disabled&#39; or &#39;access enabled&#39;) |  [optional] |
|**ipAssignmentMode** | **String** | The client IP assignment mode (&#39;NAT mode&#39;, &#39;Bridge mode&#39;, &#39;Layer 3 roaming&#39;, &#39;Ethernet over GRE&#39;, &#39;Layer 3 roaming with a concentrator&#39; or &#39;VPN&#39;) |  [optional] |
|**lanIsolationEnabled** | **Boolean** | Boolean indicating whether Layer 2 LAN isolation should be enabled or disabled. Only configurable when ipAssignmentMode is &#39;Bridge mode&#39;. |  [optional] |
|**minBitrate** | **Float** | The minimum bitrate in Mbps of this SSID in the default indoor RF profile. (&#39;1&#39;, &#39;2&#39;, &#39;5.5&#39;, &#39;6&#39;, &#39;9&#39;, &#39;11&#39;, &#39;12&#39;, &#39;18&#39;, &#39;24&#39;, &#39;36&#39;, &#39;48&#39; or &#39;54&#39;) |  [optional] |
|**name** | **String** | The name of the SSID |  [optional] |
|**perClientBandwidthLimitDown** | **Integer** | The download bandwidth limit in Kbps. (0 represents no limit.) |  [optional] |
|**perClientBandwidthLimitUp** | **Integer** | The upload bandwidth limit in Kbps. (0 represents no limit.) |  [optional] |
|**psk** | **String** | The passkey for the SSID. This param is only valid if the authMode is &#39;psk&#39; |  [optional] |
|**radiusAccountingEnabled** | **Boolean** | Whether or not RADIUS accounting is enabled. This param is only valid if the authMode is &#39;open-with-radius&#39;, &#39;8021x-radius&#39; or &#39;ipsk-with-radius&#39; |  [optional] |
|**radiusAccountingServers** | [**List&lt;UpdateNetworkSsidRequestRadiusAccountingServersInner&gt;**](UpdateNetworkSsidRequestRadiusAccountingServersInner.md) | The RADIUS accounting 802.1X servers to be used for authentication. This param is only valid if the authMode is &#39;open-with-radius&#39;, &#39;8021x-radius&#39; or &#39;ipsk-with-radius&#39; and radiusAccountingEnabled is &#39;true&#39; |  [optional] |
|**radiusAttributeForGroupPolicies** | **String** | Specify the RADIUS attribute used to look up group policies (&#39;Filter-Id&#39;, &#39;Reply-Message&#39;, &#39;Airespace-ACL-Name&#39; or &#39;Aruba-User-Role&#39;). Access points must receive this attribute in the RADIUS Access-Accept message |  [optional] |
|**radiusCoaEnabled** | **Boolean** | If true, Meraki devices will act as a RADIUS Dynamic Authorization Server and will respond to RADIUS Change-of-Authorization and Disconnect messages sent by the RADIUS server. |  [optional] |
|**radiusFailoverPolicy** | [**RadiusFailoverPolicyEnum**](#RadiusFailoverPolicyEnum) | This policy determines how authentication requests should be handled in the event that all of the configured RADIUS servers are unreachable (&#39;Deny access&#39; or &#39;Allow access&#39;) |  [optional] |
|**radiusLoadBalancingPolicy** | [**RadiusLoadBalancingPolicyEnum**](#RadiusLoadBalancingPolicyEnum) | This policy determines which RADIUS server will be contacted first in an authentication attempt and the ordering of any necessary retry attempts (&#39;Strict priority order&#39; or &#39;Round robin&#39;) |  [optional] |
|**radiusOverride** | **Boolean** | If true, the RADIUS response can override VLAN tag. This is not valid when ipAssignmentMode is &#39;NAT mode&#39;. |  [optional] |
|**radiusServers** | [**List&lt;UpdateNetworkSsidRequestRadiusServersInner&gt;**](UpdateNetworkSsidRequestRadiusServersInner.md) | The RADIUS 802.1X servers to be used for authentication. This param is only valid if the authMode is &#39;open-with-radius&#39;, &#39;8021x-radius&#39; or &#39;ipsk-with-radius&#39; |  [optional] |
|**secondaryConcentratorNetworkId** | **String** | The secondary concentrator to use when the ipAssignmentMode is &#39;VPN&#39;. If configured, the APs will switch to using this concentrator if the primary concentrator is unreachable. This param is optional. (&#39;disabled&#39; represents no secondary concentrator.) |  [optional] |
|**splashPage** | [**SplashPageEnum**](#SplashPageEnum) | The type of splash page for the SSID (&#39;None&#39;, &#39;Click-through splash page&#39;, &#39;Billing&#39;, &#39;Password-protected with Meraki RADIUS&#39;, &#39;Password-protected with custom RADIUS&#39;, &#39;Password-protected with Active Directory&#39;, &#39;Password-protected with LDAP&#39;, &#39;SMS authentication&#39;, &#39;Systems Manager Sentry&#39;, &#39;Facebook Wi-Fi&#39;, &#39;Google OAuth&#39;, &#39;Sponsored guest&#39;, &#39;Cisco ISE&#39; or &#39;Google Apps domain&#39;). This attribute is not supported for template children. |  [optional] |
|**useVlanTagging** | **Boolean** | Whether or not traffic should be directed to use specific VLANs. This param is only valid if the ipAssignmentMode is &#39;Bridge mode&#39; or &#39;Layer 3 roaming&#39; |  [optional] |
|**visible** | **Boolean** | Boolean indicating whether APs should advertise or hide this SSID. APs will only broadcast this SSID if set to true |  [optional] |
|**vlanId** | **Integer** | The VLAN ID used for VLAN tagging. This param is only valid when the ipAssignmentMode is &#39;Layer 3 roaming with a concentrator&#39; or &#39;VPN&#39; |  [optional] |
|**walledGardenEnabled** | **Boolean** | Allow access to a configurable list of IP ranges, which users may access prior to sign-on. |  [optional] |
|**walledGardenRanges** | **String** | Specify your walled garden by entering space-separated addresses, ranges using CIDR notation, domain names, and domain wildcards (e.g. 192.168.1.1/24 192.168.37.10/32 www.yahoo.com *.google.com). Meraki&#39;s splash page is automatically included in your walled garden. |  [optional] |
|**wpaEncryptionMode** | [**WpaEncryptionModeEnum**](#WpaEncryptionModeEnum) | The types of WPA encryption. (&#39;WPA1 only&#39;, &#39;WPA1 and WPA2&#39;, &#39;WPA2 only&#39;, &#39;WPA3 Transition Mode&#39;, &#39;WPA3 only&#39; or &#39;WPA3 192-bit Security&#39;) |  [optional] |



## Enum: AuthModeEnum

| Name | Value |
|---- | -----|
| _8021X_GOOGLE | &quot;8021x-google&quot; |
| _8021X_LOCALRADIUS | &quot;8021x-localradius&quot; |
| _8021X_MERAKI | &quot;8021x-meraki&quot; |
| _8021X_NAC | &quot;8021x-nac&quot; |
| _8021X_RADIUS | &quot;8021x-radius&quot; |
| IPSK_WITH_RADIUS | &quot;ipsk-with-radius&quot; |
| IPSK_WITHOUT_RADIUS | &quot;ipsk-without-radius&quot; |
| OPEN | &quot;open&quot; |
| OPEN_ENHANCED | &quot;open-enhanced&quot; |
| OPEN_WITH_NAC | &quot;open-with-nac&quot; |
| OPEN_WITH_RADIUS | &quot;open-with-radius&quot; |
| PSK | &quot;psk&quot; |



## Enum: EncryptionModeEnum

| Name | Value |
|---- | -----|
| WEP | &quot;wep&quot; |
| WPA | &quot;wpa&quot; |



## Enum: EnterpriseAdminAccessEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;access disabled&quot; |
| ENABLED | &quot;access enabled&quot; |



## Enum: RadiusFailoverPolicyEnum

| Name | Value |
|---- | -----|
| ALLOW_ACCESS | &quot;Allow access&quot; |
| DENY_ACCESS | &quot;Deny access&quot; |



## Enum: RadiusLoadBalancingPolicyEnum

| Name | Value |
|---- | -----|
| ROUND_ROBIN | &quot;Round robin&quot; |
| STRICT_PRIORITY_ORDER | &quot;Strict priority order&quot; |



## Enum: SplashPageEnum

| Name | Value |
|---- | -----|
| BILLING | &quot;Billing&quot; |
| CISCO_ISE | &quot;Cisco ISE&quot; |
| CLICK_THROUGH_SPLASH_PAGE | &quot;Click-through splash page&quot; |
| FACEBOOK_WI_FI | &quot;Facebook Wi-Fi&quot; |
| GOOGLE_APPS_DOMAIN | &quot;Google Apps domain&quot; |
| GOOGLE_O_AUTH | &quot;Google OAuth&quot; |
| NONE | &quot;None&quot; |
| PASSWORD_PROTECTED_WITH_ACTIVE_DIRECTORY | &quot;Password-protected with Active Directory&quot; |
| PASSWORD_PROTECTED_WITH_LDAP | &quot;Password-protected with LDAP&quot; |
| PASSWORD_PROTECTED_WITH_MERAKI_RADIUS | &quot;Password-protected with Meraki RADIUS&quot; |
| PASSWORD_PROTECTED_WITH_CUSTOM_RADIUS | &quot;Password-protected with custom RADIUS&quot; |
| SMS_AUTHENTICATION | &quot;SMS authentication&quot; |
| SPONSORED_GUEST | &quot;Sponsored guest&quot; |
| SYSTEMS_MANAGER_SENTRY | &quot;Systems Manager Sentry&quot; |



## Enum: WpaEncryptionModeEnum

| Name | Value |
|---- | -----|
| WPA1_AND_WPA2 | &quot;WPA1 and WPA2&quot; |
| WPA1_ONLY | &quot;WPA1 only&quot; |
| WPA2_ONLY | &quot;WPA2 only&quot; |
| WPA3_192_BIT_SECURITY | &quot;WPA3 192-bit Security&quot; |
| WPA3_TRANSITION_MODE | &quot;WPA3 Transition Mode&quot; |
| WPA3_ONLY | &quot;WPA3 only&quot; |



