

# UpdateDeviceSwitchPortRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessPolicyNumber** | **Integer** | The number of a custom access policy to configure on the switch port. Only applicable when &#39;accessPolicyType&#39; is &#39;Custom access policy&#39;. |  [optional] |
|**accessPolicyType** | [**AccessPolicyTypeEnum**](#AccessPolicyTypeEnum) | The type of the access policy of the switch port. Only applicable to access ports. Can be one of &#39;Open&#39;, &#39;Custom access policy&#39;, &#39;MAC allow list&#39; or &#39;Sticky MAC allow list&#39;. |  [optional] |
|**adaptivePolicyGroupId** | **String** | The adaptive policy group ID that will be used to tag traffic through this switch port. This ID must pre-exist during the configuration, else needs to be created using adaptivePolicy/groups API. Cannot be applied to a port on a switch bound to profile. |  [optional] |
|**allowedVlans** | **String** | The VLANs allowed on the switch port. Only applicable to trunk ports. |  [optional] |
|**daiTrusted** | **Boolean** | If true, ARP packets for this port will be considered trusted, and Dynamic ARP Inspection will allow the traffic. |  [optional] |
|**enabled** | **Boolean** | The status of the switch port. |  [optional] |
|**flexibleStackingEnabled** | **Boolean** | For supported switches (e.g. MS420/MS425), whether or not the port has flexible stacking enabled. |  [optional] |
|**isolationEnabled** | **Boolean** | The isolation status of the switch port. |  [optional] |
|**linkNegotiation** | **String** | The link speed for the switch port. |  [optional] |
|**macAllowList** | **List&lt;String&gt;** | Only devices with MAC addresses specified in this list will have access to this port. Up to 20 MAC addresses can be defined. Only applicable when &#39;accessPolicyType&#39; is &#39;MAC allow list&#39;. |  [optional] |
|**name** | **String** | The name of the switch port. |  [optional] |
|**peerSgtCapable** | **Boolean** | If true, Peer SGT is enabled for traffic through this switch port. Applicable to trunk port only, not access port. Cannot be applied to a port on a switch bound to profile. |  [optional] |
|**poeEnabled** | **Boolean** | The PoE status of the switch port. |  [optional] |
|**portScheduleId** | **String** | The ID of the port schedule. A value of null will clear the port schedule. |  [optional] |
|**profile** | [**GetDeviceSwitchPorts200ResponseInnerProfile**](GetDeviceSwitchPorts200ResponseInnerProfile.md) |  |  [optional] |
|**rstpEnabled** | **Boolean** | The rapid spanning tree protocol status. |  [optional] |
|**stickyMacAllowList** | **List&lt;String&gt;** | The initial list of MAC addresses for sticky Mac allow list. Only applicable when &#39;accessPolicyType&#39; is &#39;Sticky MAC allow list&#39;. |  [optional] |
|**stickyMacAllowListLimit** | **Integer** | The maximum number of MAC addresses for sticky MAC allow list. Only applicable when &#39;accessPolicyType&#39; is &#39;Sticky MAC allow list&#39;. |  [optional] |
|**stormControlEnabled** | **Boolean** | The storm control status of the switch port. |  [optional] |
|**stpGuard** | [**StpGuardEnum**](#StpGuardEnum) | The state of the STP guard (&#39;disabled&#39;, &#39;root guard&#39;, &#39;bpdu guard&#39; or &#39;loop guard&#39;). |  [optional] |
|**tags** | **List&lt;String&gt;** | The list of tags of the switch port. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the switch port (&#39;trunk&#39; or &#39;access&#39;). |  [optional] |
|**udld** | [**UdldEnum**](#UdldEnum) | The action to take when Unidirectional Link is detected (Alert only, Enforce). Default configuration is Alert only. |  [optional] |
|**vlan** | **Integer** | The VLAN of the switch port. A null value will clear the value set for trunk ports. |  [optional] |
|**voiceVlan** | **Integer** | The voice VLAN of the switch port. Only applicable to access ports. |  [optional] |



## Enum: AccessPolicyTypeEnum

| Name | Value |
|---- | -----|
| CUSTOM_ACCESS_POLICY | &quot;Custom access policy&quot; |
| MAC_ALLOW_LIST | &quot;MAC allow list&quot; |
| OPEN | &quot;Open&quot; |
| STICKY_MAC_ALLOW_LIST | &quot;Sticky MAC allow list&quot; |



## Enum: StpGuardEnum

| Name | Value |
|---- | -----|
| BPDU_GUARD | &quot;bpdu guard&quot; |
| DISABLED | &quot;disabled&quot; |
| LOOP_GUARD | &quot;loop guard&quot; |
| ROOT_GUARD | &quot;root guard&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ACCESS | &quot;access&quot; |
| TRUNK | &quot;trunk&quot; |



## Enum: UdldEnum

| Name | Value |
|---- | -----|
| ALERT_ONLY | &quot;Alert only&quot; |
| ENFORCE | &quot;Enforce&quot; |



