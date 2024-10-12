# MerakiDashboardApi.UpdateNetworkWirelessSsidRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activeDirectory** | [**UpdateNetworkWirelessSsidRequestActiveDirectory**](UpdateNetworkWirelessSsidRequestActiveDirectory.md) |  | [optional] 
**adultContentFilteringEnabled** | **Boolean** | Boolean indicating whether or not adult content will be blocked | [optional] 
**apTagsAndVlanIds** | [**[UpdateNetworkWirelessSsidRequestApTagsAndVlanIdsInner]**](UpdateNetworkWirelessSsidRequestApTagsAndVlanIdsInner.md) | The list of tags and VLAN IDs used for VLAN tagging. This param is only valid when the ipAssignmentMode is &#39;Bridge mode&#39; or &#39;Layer 3 roaming&#39; | [optional] 
**authMode** | **String** | The association control method for the SSID (&#39;open&#39;, &#39;open-enhanced&#39;, &#39;psk&#39;, &#39;open-with-radius&#39;, &#39;open-with-nac&#39;, &#39;8021x-meraki&#39;, &#39;8021x-nac&#39;, &#39;8021x-radius&#39;, &#39;8021x-google&#39;, &#39;8021x-localradius&#39;, &#39;ipsk-with-radius&#39; or &#39;ipsk-without-radius&#39;) | [optional] 
**availabilityTags** | **[String]** | Accepts a list of tags for this SSID. If availableOnAllAps is false, then the SSID will only be broadcast by APs with tags matching any of the tags in this list. | [optional] 
**availableOnAllAps** | **Boolean** | Boolean indicating whether all APs should broadcast the SSID or if it should be restricted to APs matching any availability tags. Can only be false if the SSID has availability tags. | [optional] 
**bandSelection** | **String** | The client-serving radio frequencies of this SSID in the default indoor RF profile. (&#39;Dual band operation&#39;, &#39;5 GHz band only&#39; or &#39;Dual band operation with Band Steering&#39;) | [optional] 
**concentratorNetworkId** | **String** | The concentrator to use when the ipAssignmentMode is &#39;Layer 3 roaming with a concentrator&#39; or &#39;VPN&#39;. | [optional] 
**defaultVlanId** | **Number** | The default VLAN ID used for &#39;all other APs&#39;. This param is only valid when the ipAssignmentMode is &#39;Bridge mode&#39; or &#39;Layer 3 roaming&#39; | [optional] 
**disassociateClientsOnVpnFailover** | **Boolean** | Disassociate clients when &#39;VPN&#39; concentrator failover occurs in order to trigger clients to re-associate and generate new DHCP requests. This param is only valid if ipAssignmentMode is &#39;VPN&#39;. | [optional] 
**dnsRewrite** | [**UpdateNetworkWirelessSsidRequestDnsRewrite**](UpdateNetworkWirelessSsidRequestDnsRewrite.md) |  | [optional] 
**dot11r** | [**UpdateNetworkWirelessSsidRequestDot11r**](UpdateNetworkWirelessSsidRequestDot11r.md) |  | [optional] 
**dot11w** | [**UpdateNetworkWirelessSsidRequestDot11w**](UpdateNetworkWirelessSsidRequestDot11w.md) |  | [optional] 
**enabled** | **Boolean** | Whether or not the SSID is enabled | [optional] 
**encryptionMode** | **String** | The psk encryption mode for the SSID (&#39;wep&#39; or &#39;wpa&#39;). This param is only valid if the authMode is &#39;psk&#39; | [optional] 
**enterpriseAdminAccess** | **String** | Whether or not an SSID is accessible by &#39;enterprise&#39; administrators (&#39;access disabled&#39; or &#39;access enabled&#39;) | [optional] 
**gre** | [**UpdateNetworkWirelessSsidRequestGre**](UpdateNetworkWirelessSsidRequestGre.md) |  | [optional] 
**ipAssignmentMode** | **String** | The client IP assignment mode (&#39;NAT mode&#39;, &#39;Bridge mode&#39;, &#39;Layer 3 roaming&#39;, &#39;Ethernet over GRE&#39;, &#39;Layer 3 roaming with a concentrator&#39; or &#39;VPN&#39;) | [optional] 
**lanIsolationEnabled** | **Boolean** | Boolean indicating whether Layer 2 LAN isolation should be enabled or disabled. Only configurable when ipAssignmentMode is &#39;Bridge mode&#39;. | [optional] 
**ldap** | [**UpdateNetworkWirelessSsidRequestLdap**](UpdateNetworkWirelessSsidRequestLdap.md) |  | [optional] 
**localRadius** | [**UpdateNetworkWirelessSsidRequestLocalRadius**](UpdateNetworkWirelessSsidRequestLocalRadius.md) |  | [optional] 
**mandatoryDhcpEnabled** | **Boolean** | If true, Mandatory DHCP will enforce that clients connecting to this SSID must use the IP address assigned by the DHCP server. Clients who use a static IP address won&#39;t be able to associate. | [optional] 
**minBitrate** | **Number** | The minimum bitrate in Mbps of this SSID in the default indoor RF profile. (&#39;1&#39;, &#39;2&#39;, &#39;5.5&#39;, &#39;6&#39;, &#39;9&#39;, &#39;11&#39;, &#39;12&#39;, &#39;18&#39;, &#39;24&#39;, &#39;36&#39;, &#39;48&#39; or &#39;54&#39;) | [optional] 
**name** | **String** | The name of the SSID | [optional] 
**oauth** | [**UpdateNetworkWirelessSsidRequestOauth**](UpdateNetworkWirelessSsidRequestOauth.md) |  | [optional] 
**perClientBandwidthLimitDown** | **Number** | The download bandwidth limit in Kbps. (0 represents no limit.) | [optional] 
**perClientBandwidthLimitUp** | **Number** | The upload bandwidth limit in Kbps. (0 represents no limit.) | [optional] 
**perSsidBandwidthLimitDown** | **Number** | The total download bandwidth limit in Kbps. (0 represents no limit.) | [optional] 
**perSsidBandwidthLimitUp** | **Number** | The total upload bandwidth limit in Kbps. (0 represents no limit.) | [optional] 
**psk** | **String** | The passkey for the SSID. This param is only valid if the authMode is &#39;psk&#39; | [optional] 
**radiusAccountingEnabled** | **Boolean** | Whether or not RADIUS accounting is enabled. This param is only valid if the authMode is &#39;open-with-radius&#39;, &#39;8021x-radius&#39; or &#39;ipsk-with-radius&#39; | [optional] 
**radiusAccountingInterimInterval** | **Number** | The interval (in seconds) in which accounting information is updated and sent to the RADIUS accounting server. | [optional] 
**radiusAccountingServers** | [**[UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner]**](UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner.md) | The RADIUS accounting 802.1X servers to be used for authentication. This param is only valid if the authMode is &#39;open-with-radius&#39;, &#39;8021x-radius&#39; or &#39;ipsk-with-radius&#39; and radiusAccountingEnabled is &#39;true&#39; | [optional] 
**radiusAttributeForGroupPolicies** | **String** | Specify the RADIUS attribute used to look up group policies (&#39;Filter-Id&#39;, &#39;Reply-Message&#39;, &#39;Airespace-ACL-Name&#39; or &#39;Aruba-User-Role&#39;). Access points must receive this attribute in the RADIUS Access-Accept message | [optional] 
**radiusAuthenticationNasId** | **String** | The template of the NAS identifier to be used for RADIUS authentication (ex. $NODE_MAC$:$VAP_NUM$). | [optional] 
**radiusCalledStationId** | **String** | The template of the called station identifier to be used for RADIUS (ex. $NODE_MAC$:$VAP_NUM$). | [optional] 
**radiusCoaEnabled** | **Boolean** | If true, Meraki devices will act as a RADIUS Dynamic Authorization Server and will respond to RADIUS Change-of-Authorization and Disconnect messages sent by the RADIUS server. | [optional] 
**radiusFailoverPolicy** | **String** | This policy determines how authentication requests should be handled in the event that all of the configured RADIUS servers are unreachable (&#39;Deny access&#39; or &#39;Allow access&#39;) | [optional] 
**radiusFallbackEnabled** | **Boolean** | Whether or not higher priority RADIUS servers should be retried after 60 seconds. | [optional] 
**radiusGuestVlanEnabled** | **Boolean** | Whether or not RADIUS Guest VLAN is enabled. This param is only valid if the authMode is &#39;open-with-radius&#39; and addressing mode is not set to &#39;isolated&#39; or &#39;nat&#39; mode | [optional] 
**radiusGuestVlanId** | **Number** | VLAN ID of the RADIUS Guest VLAN. This param is only valid if the authMode is &#39;open-with-radius&#39; and addressing mode is not set to &#39;isolated&#39; or &#39;nat&#39; mode | [optional] 
**radiusLoadBalancingPolicy** | **String** | This policy determines which RADIUS server will be contacted first in an authentication attempt and the ordering of any necessary retry attempts (&#39;Strict priority order&#39; or &#39;Round robin&#39;) | [optional] 
**radiusOverride** | **Boolean** | If true, the RADIUS response can override VLAN tag. This is not valid when ipAssignmentMode is &#39;NAT mode&#39;. | [optional] 
**radiusProxyEnabled** | **Boolean** | If true, Meraki devices will proxy RADIUS messages through the Meraki cloud to the configured RADIUS auth and accounting servers. | [optional] 
**radiusServerAttemptsLimit** | **Number** | The maximum number of transmit attempts after which a RADIUS server is failed over (must be between 1-5). | [optional] 
**radiusServerTimeout** | **Number** | The amount of time for which a RADIUS client waits for a reply from the RADIUS server (must be between 1-10 seconds). | [optional] 
**radiusServers** | [**[UpdateNetworkWirelessSsidRequestRadiusServersInner]**](UpdateNetworkWirelessSsidRequestRadiusServersInner.md) | The RADIUS 802.1X servers to be used for authentication. This param is only valid if the authMode is &#39;open-with-radius&#39;, &#39;8021x-radius&#39; or &#39;ipsk-with-radius&#39; | [optional] 
**radiusTestingEnabled** | **Boolean** | If true, Meraki devices will periodically send Access-Request messages to configured RADIUS servers using identity &#39;meraki_8021x_test&#39; to ensure that the RADIUS servers are reachable. | [optional] 
**secondaryConcentratorNetworkId** | **String** | The secondary concentrator to use when the ipAssignmentMode is &#39;VPN&#39;. If configured, the APs will switch to using this concentrator if the primary concentrator is unreachable. This param is optional. (&#39;disabled&#39; represents no secondary concentrator.) | [optional] 
**speedBurst** | [**UpdateNetworkWirelessSsidRequestSpeedBurst**](UpdateNetworkWirelessSsidRequestSpeedBurst.md) |  | [optional] 
**splashGuestSponsorDomains** | **[String]** | Array of valid sponsor email domains for sponsored guest splash type. | [optional] 
**splashPage** | **String** | The type of splash page for the SSID (&#39;None&#39;, &#39;Click-through splash page&#39;, &#39;Billing&#39;, &#39;Password-protected with Meraki RADIUS&#39;, &#39;Password-protected with custom RADIUS&#39;, &#39;Password-protected with Active Directory&#39;, &#39;Password-protected with LDAP&#39;, &#39;SMS authentication&#39;, &#39;Systems Manager Sentry&#39;, &#39;Facebook Wi-Fi&#39;, &#39;Google OAuth&#39;, &#39;Sponsored guest&#39;, &#39;Cisco ISE&#39; or &#39;Google Apps domain&#39;). This attribute is not supported for template children. | [optional] 
**useVlanTagging** | **Boolean** | Whether or not traffic should be directed to use specific VLANs. This param is only valid if the ipAssignmentMode is &#39;Bridge mode&#39; or &#39;Layer 3 roaming&#39; | [optional] 
**visible** | **Boolean** | Boolean indicating whether APs should advertise or hide this SSID. APs will only broadcast this SSID if set to true | [optional] 
**vlanId** | **Number** | The VLAN ID used for VLAN tagging. This param is only valid when the ipAssignmentMode is &#39;Layer 3 roaming with a concentrator&#39; or &#39;VPN&#39; | [optional] 
**walledGardenEnabled** | **Boolean** | Allow access to a configurable list of IP ranges, which users may access prior to sign-on. | [optional] 
**walledGardenRanges** | **[String]** | Specify your walled garden by entering an array of addresses, ranges using CIDR notation, domain names, and domain wildcards (e.g. &#39;192.168.1.1/24&#39;, &#39;192.168.37.10/32&#39;, &#39;www.yahoo.com&#39;, &#39;*.google.com&#39;]). Meraki&#39;s splash page is automatically included in your walled garden. | [optional] 
**wpaEncryptionMode** | **String** | The types of WPA encryption. (&#39;WPA1 only&#39;, &#39;WPA1 and WPA2&#39;, &#39;WPA2 only&#39;, &#39;WPA3 Transition Mode&#39;, &#39;WPA3 only&#39; or &#39;WPA3 192-bit Security&#39;) | [optional] 



## Enum: AuthModeEnum


* `8021x-google` (value: `"8021x-google"`)

* `8021x-localradius` (value: `"8021x-localradius"`)

* `8021x-meraki` (value: `"8021x-meraki"`)

* `8021x-nac` (value: `"8021x-nac"`)

* `8021x-radius` (value: `"8021x-radius"`)

* `ipsk-with-radius` (value: `"ipsk-with-radius"`)

* `ipsk-without-radius` (value: `"ipsk-without-radius"`)

* `open` (value: `"open"`)

* `open-enhanced` (value: `"open-enhanced"`)

* `open-with-nac` (value: `"open-with-nac"`)

* `open-with-radius` (value: `"open-with-radius"`)

* `psk` (value: `"psk"`)





## Enum: EncryptionModeEnum


* `wep` (value: `"wep"`)

* `wpa` (value: `"wpa"`)





## Enum: EnterpriseAdminAccessEnum


* `disabled` (value: `"access disabled"`)

* `enabled` (value: `"access enabled"`)





## Enum: RadiusAttributeForGroupPoliciesEnum


* `Airespace-ACL-Name` (value: `"Airespace-ACL-Name"`)

* `Aruba-User-Role` (value: `"Aruba-User-Role"`)

* `Filter-Id` (value: `"Filter-Id"`)

* `Reply-Message` (value: `"Reply-Message"`)





## Enum: RadiusFailoverPolicyEnum


* `Allow access` (value: `"Allow access"`)

* `Deny access` (value: `"Deny access"`)





## Enum: RadiusLoadBalancingPolicyEnum


* `Round robin` (value: `"Round robin"`)

* `Strict priority order` (value: `"Strict priority order"`)





## Enum: SplashPageEnum


* `Billing` (value: `"Billing"`)

* `Cisco ISE` (value: `"Cisco ISE"`)

* `Click-through splash page` (value: `"Click-through splash page"`)

* `Facebook Wi-Fi` (value: `"Facebook Wi-Fi"`)

* `Google Apps domain` (value: `"Google Apps domain"`)

* `Google OAuth` (value: `"Google OAuth"`)

* `None` (value: `"None"`)

* `Password-protected with Active Directory` (value: `"Password-protected with Active Directory"`)

* `Password-protected with LDAP` (value: `"Password-protected with LDAP"`)

* `Password-protected with Meraki RADIUS` (value: `"Password-protected with Meraki RADIUS"`)

* `Password-protected with custom RADIUS` (value: `"Password-protected with custom RADIUS"`)

* `SMS authentication` (value: `"SMS authentication"`)

* `Sponsored guest` (value: `"Sponsored guest"`)

* `Systems Manager Sentry` (value: `"Systems Manager Sentry"`)





## Enum: WpaEncryptionModeEnum


* `WPA1 and WPA2` (value: `"WPA1 and WPA2"`)

* `WPA1 only` (value: `"WPA1 only"`)

* `WPA2 only` (value: `"WPA2 only"`)

* `WPA3 192-bit Security` (value: `"WPA3 192-bit Security"`)

* `WPA3 Transition Mode` (value: `"WPA3 Transition Mode"`)

* `WPA3 only` (value: `"WPA3 only"`)




