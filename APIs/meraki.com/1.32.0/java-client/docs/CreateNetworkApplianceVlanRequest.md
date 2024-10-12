

# CreateNetworkApplianceVlanRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applianceIp** | **String** | The local IP of the appliance on the VLAN |  [optional] |
|**cidr** | **String** | CIDR of the pool of subnets. Applicable only for template network. Each network bound to the template will automatically pick a subnet from this pool to build its own VLAN. |  [optional] |
|**groupPolicyId** | **String** | The id of the desired group policy to apply to the VLAN |  [optional] |
|**id** | **String** | The VLAN ID of the new VLAN (must be between 1 and 4094) |  |
|**ipv6** | [**UpdateNetworkApplianceSingleLanRequestIpv6**](UpdateNetworkApplianceSingleLanRequestIpv6.md) |  |  [optional] |
|**mandatoryDhcp** | [**GetNetworkApplianceVlans200ResponseInnerMandatoryDhcp**](GetNetworkApplianceVlans200ResponseInnerMandatoryDhcp.md) |  |  [optional] |
|**mask** | **Integer** | Mask used for the subnet of all bound to the template networks. Applicable only for template network. |  [optional] |
|**name** | **String** | The name of the new VLAN |  |
|**subnet** | **String** | The subnet of the VLAN |  [optional] |
|**templateVlanType** | [**TemplateVlanTypeEnum**](#TemplateVlanTypeEnum) | Type of subnetting of the VLAN. Applicable only for template network. |  [optional] |



## Enum: TemplateVlanTypeEnum

| Name | Value |
|---- | -----|
| SAME | &quot;same&quot; |
| UNIQUE | &quot;unique&quot; |



