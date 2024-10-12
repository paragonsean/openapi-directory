

# UpdateNetworkSwitchAccessPolicyRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessPolicyType** | [**AccessPolicyTypeEnum**](#AccessPolicyTypeEnum) | Access Type of the policy. Automatically &#39;Hybrid authentication&#39; when hostMode is &#39;Multi-Domain&#39;. |  [optional] |
|**dot1x** | [**GetNetworkSwitchAccessPolicies200ResponseInnerDot1x**](GetNetworkSwitchAccessPolicies200ResponseInnerDot1x.md) |  |  [optional] |
|**guestPortBouncing** | **Boolean** | If enabled, Meraki devices will periodically send access-request messages to these RADIUS servers |  [optional] |
|**guestVlanId** | **Integer** | ID for the guest VLAN allow unauthorized devices access to limited network resources |  [optional] |
|**hostMode** | [**HostModeEnum**](#HostModeEnum) | Choose the Host Mode for the access policy. |  [optional] |
|**increaseAccessSpeed** | **Boolean** | Enabling this option will make switches execute 802.1X and MAC-bypass authentication simultaneously so that clients authenticate faster. Only required when accessPolicyType is &#39;Hybrid Authentication. |  [optional] |
|**name** | **String** | Name of the access policy |  [optional] |
|**radius** | [**GetNetworkSwitchAccessPolicies200ResponseInnerRadius**](GetNetworkSwitchAccessPolicies200ResponseInnerRadius.md) |  |  [optional] |
|**radiusAccountingEnabled** | **Boolean** | Enable to send start, interim-update and stop messages to a configured RADIUS accounting server for tracking connected clients |  [optional] |
|**radiusAccountingServers** | [**List&lt;CreateNetworkSwitchAccessPolicyRequestRadiusAccountingServersInner&gt;**](CreateNetworkSwitchAccessPolicyRequestRadiusAccountingServersInner.md) | List of RADIUS accounting servers to require connecting devices to authenticate against before granting network access |  [optional] |
|**radiusCoaSupportEnabled** | **Boolean** | Change of authentication for RADIUS re-authentication and disconnection |  [optional] |
|**radiusGroupAttribute** | **String** | Acceptable values are &#x60;\&quot;\&quot;&#x60; for None, or &#x60;\&quot;11\&quot;&#x60; for Group Policies ACL |  [optional] |
|**radiusServers** | [**List&lt;CreateNetworkSwitchAccessPolicyRequestRadiusServersInner&gt;**](CreateNetworkSwitchAccessPolicyRequestRadiusServersInner.md) | List of RADIUS servers to require connecting devices to authenticate against before granting network access |  [optional] |
|**radiusTestingEnabled** | **Boolean** | If enabled, Meraki devices will periodically send access-request messages to these RADIUS servers |  [optional] |
|**urlRedirectWalledGardenEnabled** | **Boolean** | Enable to restrict access for clients to a specific set of IP addresses or hostnames prior to authentication |  [optional] |
|**urlRedirectWalledGardenRanges** | **List&lt;String&gt;** | IP address ranges, in CIDR notation, to restrict access for clients to a specific set of IP addresses or hostnames prior to authentication |  [optional] |
|**voiceVlanClients** | **Boolean** | CDP/LLDP capable voice clients will be able to use this VLAN. Automatically true when hostMode is &#39;Multi-Domain&#39;. |  [optional] |



## Enum: AccessPolicyTypeEnum

| Name | Value |
|---- | -----|
| _802_1X | &quot;802.1x&quot; |
| HYBRID_AUTHENTICATION | &quot;Hybrid authentication&quot; |
| MAC_AUTHENTICATION_BYPASS | &quot;MAC authentication bypass&quot; |



## Enum: HostModeEnum

| Name | Value |
|---- | -----|
| MULTI_AUTH | &quot;Multi-Auth&quot; |
| MULTI_DOMAIN | &quot;Multi-Domain&quot; |
| MULTI_HOST | &quot;Multi-Host&quot; |
| SINGLE_HOST | &quot;Single-Host&quot; |



