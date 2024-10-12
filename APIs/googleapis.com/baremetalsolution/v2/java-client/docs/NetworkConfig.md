

# NetworkConfig

Configuration parameters for a new network.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bandwidth** | [**BandwidthEnum**](#BandwidthEnum) | Interconnect bandwidth. Set only when type is CLIENT. |  [optional] |
|**cidr** | **String** | CIDR range of the network. |  [optional] |
|**gcpService** | **String** | The GCP service of the network. Available gcp_service are in https://cloud.google.com/bare-metal/docs/bms-planning. |  [optional] |
|**id** | **String** | A transient unique identifier to identify a volume within an ProvisioningConfig request. |  [optional] |
|**jumboFramesEnabled** | **Boolean** | The JumboFramesEnabled option for customer to set. |  [optional] |
|**name** | **String** | Output only. The name of the network config. |  [optional] [readonly] |
|**serviceCidr** | [**ServiceCidrEnum**](#ServiceCidrEnum) | Service CIDR, if any. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of this network, either Client or Private. |  [optional] |
|**userNote** | **String** | User note field, it can be used by customers to add additional information for the BMS Ops team . |  [optional] |
|**vlanAttachments** | [**List&lt;IntakeVlanAttachment&gt;**](IntakeVlanAttachment.md) | List of VLAN attachments. As of now there are always 2 attachments, but it is going to change in the future (multi vlan). |  [optional] |
|**vlanSameProject** | **Boolean** | Whether the VLAN attachment pair is located in the same project. |  [optional] |



## Enum: BandwidthEnum

| Name | Value |
|---- | -----|
| BANDWIDTH_UNSPECIFIED | &quot;BANDWIDTH_UNSPECIFIED&quot; |
| BW_1_GBPS | &quot;BW_1_GBPS&quot; |
| BW_2_GBPS | &quot;BW_2_GBPS&quot; |
| BW_5_GBPS | &quot;BW_5_GBPS&quot; |
| BW_10_GBPS | &quot;BW_10_GBPS&quot; |



## Enum: ServiceCidrEnum

| Name | Value |
|---- | -----|
| SERVICE_CIDR_UNSPECIFIED | &quot;SERVICE_CIDR_UNSPECIFIED&quot; |
| DISABLED | &quot;DISABLED&quot; |
| HIGH_26 | &quot;HIGH_26&quot; |
| HIGH_27 | &quot;HIGH_27&quot; |
| HIGH_28 | &quot;HIGH_28&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| CLIENT | &quot;CLIENT&quot; |
| PRIVATE | &quot;PRIVATE&quot; |



