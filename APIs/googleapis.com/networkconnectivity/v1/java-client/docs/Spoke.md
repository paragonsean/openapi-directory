

# Spoke

A Network Connectivity Center spoke represents one or more network connectivity resources. When you create a spoke, you associate it with a hub. You must also identify a value for exactly one of the following fields: * linked_vpn_tunnels * linked_interconnect_attachments * linked_router_appliance_instances * linked_vpc_network

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The time the spoke was created. |  [optional] [readonly] |
|**description** | **String** | An optional description of the spoke. |  [optional] |
|**group** | **String** | Optional. The name of the group that this spoke is associated with. |  [optional] |
|**hub** | **String** | Immutable. The name of the hub that this spoke is attached to. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional labels in key-value pair format. For more information about labels, see [Requirements for labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements). |  [optional] |
|**linkedInterconnectAttachments** | [**LinkedInterconnectAttachments**](LinkedInterconnectAttachments.md) |  |  [optional] |
|**linkedRouterApplianceInstances** | [**LinkedRouterApplianceInstances**](LinkedRouterApplianceInstances.md) |  |  [optional] |
|**linkedVpcNetwork** | [**LinkedVpcNetwork**](LinkedVpcNetwork.md) |  |  [optional] |
|**linkedVpnTunnels** | [**LinkedVpnTunnels**](LinkedVpnTunnels.md) |  |  [optional] |
|**name** | **String** | Immutable. The name of the spoke. Spoke names must be unique. They use the following form: &#x60;projects/{project_number}/locations/{region}/spokes/{spoke_id}&#x60; |  [optional] |
|**reasons** | [**List&lt;StateReason&gt;**](StateReason.md) | Output only. The reasons for current state of the spoke. Only present when the spoke is in the &#x60;INACTIVE&#x60; state. |  [optional] [readonly] |
|**spokeType** | [**SpokeTypeEnum**](#SpokeTypeEnum) | Output only. The type of resource associated with the spoke. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The current lifecycle state of this spoke. |  [optional] [readonly] |
|**uniqueId** | **String** | Output only. The Google-generated UUID for the spoke. This value is unique across all spoke resources. If a spoke is deleted and another with the same name is created, the new spoke is assigned a different &#x60;unique_id&#x60;. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The time the spoke was last updated. |  [optional] [readonly] |



## Enum: SpokeTypeEnum

| Name | Value |
|---- | -----|
| SPOKE_TYPE_UNSPECIFIED | &quot;SPOKE_TYPE_UNSPECIFIED&quot; |
| VPN_TUNNEL | &quot;VPN_TUNNEL&quot; |
| INTERCONNECT_ATTACHMENT | &quot;INTERCONNECT_ATTACHMENT&quot; |
| ROUTER_APPLIANCE | &quot;ROUTER_APPLIANCE&quot; |
| VPC_NETWORK | &quot;VPC_NETWORK&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| DELETING | &quot;DELETING&quot; |
| ACCEPTING | &quot;ACCEPTING&quot; |
| REJECTING | &quot;REJECTING&quot; |
| UPDATING | &quot;UPDATING&quot; |
| INACTIVE | &quot;INACTIVE&quot; |
| OBSOLETE | &quot;OBSOLETE&quot; |



