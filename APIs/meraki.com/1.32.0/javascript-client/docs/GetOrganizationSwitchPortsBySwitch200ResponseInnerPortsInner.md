# MerakiDashboardApi.GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessPolicyType** | **String** | The type of the access policy of the switch port. Only applicable to access ports. Can be one of &#39;Open&#39;, &#39;Custom access policy&#39;, &#39;MAC allow list&#39; or &#39;Sticky MAC allow list&#39;. | [optional] 
**allowedVlans** | **String** | The VLANs allowed on the switch port. Only applicable to trunk ports. | [optional] 
**enabled** | **Boolean** | The status of the switch port. | [optional] 
**linkNegotiation** | **String** | The link speed for the switch port. | [optional] 
**name** | **String** | The name of the switch port. | [optional] 
**poeEnabled** | **Boolean** | The PoE status of the switch port. | [optional] 
**portId** | **String** | The identifier of the switch port. | [optional] 
**rstpEnabled** | **Boolean** | The rapid spanning tree protocol status. | [optional] 
**stickyMacAllowList** | **[String]** | The initial list of MAC addresses for sticky Mac allow list. Only applicable when &#39;accessPolicyType&#39; is &#39;Sticky MAC allow list&#39;. | [optional] 
**stickyMacAllowListLimit** | **Number** | The maximum number of MAC addresses for sticky MAC allow list. Only applicable when &#39;accessPolicyType&#39; is &#39;Sticky MAC allow list&#39;. | [optional] 
**stpGuard** | **String** | The state of the STP guard (&#39;disabled&#39;, &#39;root guard&#39;, &#39;bpdu guard&#39; or &#39;loop guard&#39;). | [optional] 
**tags** | **[String]** | The list of tags of the switch port. | [optional] 
**type** | **String** | The type of the switch port (&#39;trunk&#39; or &#39;access&#39;). | [optional] 
**vlan** | **Number** | The VLAN of the switch port. A null value will clear the value set for trunk ports. | [optional] 
**voiceVlan** | **Number** | The voice VLAN of the switch port. Only applicable to access ports. | [optional] 



## Enum: AccessPolicyTypeEnum


* `Custom access policy` (value: `"Custom access policy"`)

* `MAC allow list` (value: `"MAC allow list"`)

* `Open` (value: `"Open"`)

* `Sticky MAC allow list` (value: `"Sticky MAC allow list"`)





## Enum: StpGuardEnum


* `bpdu guard` (value: `"bpdu guard"`)

* `disabled` (value: `"disabled"`)

* `loop guard` (value: `"loop guard"`)

* `root guard` (value: `"root guard"`)





## Enum: TypeEnum


* `access` (value: `"access"`)

* `trunk` (value: `"trunk"`)




