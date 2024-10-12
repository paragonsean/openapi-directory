# BareMetalSolutionApi.NetworkConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bandwidth** | **String** | Interconnect bandwidth. Set only when type is CLIENT. | [optional] 
**cidr** | **String** | CIDR range of the network. | [optional] 
**id** | **String** | A transient unique identifier to identify a volume within an ProvisioningConfig request. | [optional] 
**location** | **String** | Location where to deploy the network. | [optional] 
**serviceCidr** | **String** | Service CIDR, if any. | [optional] 
**type** | **String** | The type of this network. | [optional] 
**userNote** | **String** | User note field, it can be used by customers to add additional information for the BMS Ops team (b/194021617). | [optional] 
**vlanAttachments** | [**[VlanAttachment]**](VlanAttachment.md) | List of VLAN attachments. As of now there are always 2 attachments, but it is going to change in the future (multi vlan). | [optional] 



## Enum: BandwidthEnum


* `BANDWIDTH_UNSPECIFIED` (value: `"BANDWIDTH_UNSPECIFIED"`)

* `BW_1_GBPS` (value: `"BW_1_GBPS"`)

* `BW_2_GBPS` (value: `"BW_2_GBPS"`)

* `BW_5_GBPS` (value: `"BW_5_GBPS"`)

* `BW_10_GBPS` (value: `"BW_10_GBPS"`)





## Enum: ServiceCidrEnum


* `SERVICE_CIDR_UNSPECIFIED` (value: `"SERVICE_CIDR_UNSPECIFIED"`)

* `DISABLED` (value: `"DISABLED"`)

* `HIGH_26` (value: `"HIGH_26"`)

* `HIGH_27` (value: `"HIGH_27"`)

* `HIGH_28` (value: `"HIGH_28"`)





## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `CLIENT` (value: `"CLIENT"`)

* `PRIVATE` (value: `"PRIVATE"`)




