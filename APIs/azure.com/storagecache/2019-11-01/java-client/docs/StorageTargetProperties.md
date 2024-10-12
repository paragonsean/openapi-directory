

# StorageTargetProperties

Properties of the Storage Target.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clfs** | [**ClfsTarget**](ClfsTarget.md) |  |  [optional] |
|**junctions** | [**List&lt;NamespaceJunction&gt;**](NamespaceJunction.md) | List of Cache namespace junctions to target for namespace associations. |  [optional] |
|**nfs3** | [**Nfs3Target**](Nfs3Target.md) |  |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | ARM provisioning state, see https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property |  [optional] |
|**targetType** | [**TargetTypeEnum**](#TargetTypeEnum) | Type of the Storage Target. |  [optional] |
|**unknown** | [**UnknownTarget**](UnknownTarget.md) |  |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELLED | &quot;Cancelled&quot; |
| CREATING | &quot;Creating&quot; |
| DELETING | &quot;Deleting&quot; |
| UPDATING | &quot;Updating&quot; |



## Enum: TargetTypeEnum

| Name | Value |
|---- | -----|
| NFS3 | &quot;nfs3&quot; |
| CLFS | &quot;clfs&quot; |
| UNKNOWN | &quot;unknown&quot; |



