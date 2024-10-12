

# GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessPolicyType** | [**AccessPolicyTypeEnum**](#AccessPolicyTypeEnum) | The type of the access policy of the switch port. Only applicable to access ports. Can be one of &#39;Open&#39;, &#39;Custom access policy&#39;, &#39;MAC allow list&#39; or &#39;Sticky MAC allow list&#39;. |  [optional] |
|**allowedVlans** | **String** | The VLANs allowed on the switch port. Only applicable to trunk ports. |  [optional] |
|**enabled** | **Boolean** | The status of the switch port. |  [optional] |
|**linkNegotiation** | **String** | The link speed for the switch port. |  [optional] |
|**name** | **String** | The name of the switch port. |  [optional] |
|**poeEnabled** | **Boolean** | The PoE status of the switch port. |  [optional] |
|**portId** | **String** | The identifier of the switch port. |  [optional] |
|**rstpEnabled** | **Boolean** | The rapid spanning tree protocol status. |  [optional] |
|**stickyMacAllowList** | **List&lt;String&gt;** | The initial list of MAC addresses for sticky Mac allow list. Only applicable when &#39;accessPolicyType&#39; is &#39;Sticky MAC allow list&#39;. |  [optional] |
|**stickyMacAllowListLimit** | **Integer** | The maximum number of MAC addresses for sticky MAC allow list. Only applicable when &#39;accessPolicyType&#39; is &#39;Sticky MAC allow list&#39;. |  [optional] |
|**stpGuard** | [**StpGuardEnum**](#StpGuardEnum) | The state of the STP guard (&#39;disabled&#39;, &#39;root guard&#39;, &#39;bpdu guard&#39; or &#39;loop guard&#39;). |  [optional] |
|**tags** | **List&lt;String&gt;** | The list of tags of the switch port. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the switch port (&#39;trunk&#39; or &#39;access&#39;). |  [optional] |
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



