

# HubAndSpokePeeringPolicyProperties

Properties of a Hub and Spoke Peering Policy

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hub** | [**ResourceId**](ResourceId.md) |  |  [optional] |
|**spokes** | [**List&lt;ResourceId&gt;**](ResourceId.md) | Gets or sets the spokes group IDs |  [optional] |
|**mesh** | [**List&lt;ResourceId&gt;**](ResourceId.md) | Gets or sets the mesh group IDs |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Gets or sets the connectivity type of a network structure policy |  |
|**etag** | **String** | A unique read-only string that changes whenever the resource is updated. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Provisioning state of the ManagedNetwork resource. |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| HUB_AND_SPOKE_TOPOLOGY | &quot;HubAndSpokeTopology&quot; |
| MESH_TOPOLOGY | &quot;MeshTopology&quot; |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |



