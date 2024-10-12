# NetworkConnectivityApi.Spoke

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The time the spoke was created. | [optional] [readonly] 
**description** | **String** | An optional description of the spoke. | [optional] 
**group** | **String** | Optional. The name of the group that this spoke is associated with. | [optional] 
**hub** | **String** | Immutable. The name of the hub that this spoke is attached to. | [optional] 
**labels** | **{String: String}** | Optional labels in key-value pair format. For more information about labels, see [Requirements for labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements). | [optional] 
**linkedInterconnectAttachments** | [**LinkedInterconnectAttachments**](LinkedInterconnectAttachments.md) |  | [optional] 
**linkedRouterApplianceInstances** | [**LinkedRouterApplianceInstances**](LinkedRouterApplianceInstances.md) |  | [optional] 
**linkedVpcNetwork** | [**LinkedVpcNetwork**](LinkedVpcNetwork.md) |  | [optional] 
**linkedVpnTunnels** | [**LinkedVpnTunnels**](LinkedVpnTunnels.md) |  | [optional] 
**name** | **String** | Immutable. The name of the spoke. Spoke names must be unique. They use the following form: &#x60;projects/{project_number}/locations/{region}/spokes/{spoke_id}&#x60; | [optional] 
**reasons** | [**[StateReason]**](StateReason.md) | Output only. The reasons for current state of the spoke. Only present when the spoke is in the &#x60;INACTIVE&#x60; state. | [optional] [readonly] 
**spokeType** | **String** | Output only. The type of resource associated with the spoke. | [optional] [readonly] 
**state** | **String** | Output only. The current lifecycle state of this spoke. | [optional] [readonly] 
**uniqueId** | **String** | Output only. The Google-generated UUID for the spoke. This value is unique across all spoke resources. If a spoke is deleted and another with the same name is created, the new spoke is assigned a different &#x60;unique_id&#x60;. | [optional] [readonly] 
**updateTime** | **String** | Output only. The time the spoke was last updated. | [optional] [readonly] 



## Enum: SpokeTypeEnum


* `SPOKE_TYPE_UNSPECIFIED` (value: `"SPOKE_TYPE_UNSPECIFIED"`)

* `VPN_TUNNEL` (value: `"VPN_TUNNEL"`)

* `INTERCONNECT_ATTACHMENT` (value: `"INTERCONNECT_ATTACHMENT"`)

* `ROUTER_APPLIANCE` (value: `"ROUTER_APPLIANCE"`)

* `VPC_NETWORK` (value: `"VPC_NETWORK"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `DELETING` (value: `"DELETING"`)

* `ACCEPTING` (value: `"ACCEPTING"`)

* `REJECTING` (value: `"REJECTING"`)

* `UPDATING` (value: `"UPDATING"`)

* `INACTIVE` (value: `"INACTIVE"`)

* `OBSOLETE` (value: `"OBSOLETE"`)




