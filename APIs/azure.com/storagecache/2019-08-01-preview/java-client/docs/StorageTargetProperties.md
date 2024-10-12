

# StorageTargetProperties

Properties of the storage target.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clfs** | [**ClfsTarget**](ClfsTarget.md) |  |  [optional] |
|**junctions** | [**List&lt;NamespaceJunction&gt;**](NamespaceJunction.md) | List of cache namespace to target namespace associations. |  [optional] |
|**nfs3** | [**Nfs3Target**](Nfs3Target.md) |  |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | ARM provisioning state, see https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property |  [optional] |
|**targetType** | [**TargetTypeEnum**](#TargetTypeEnum) | Type for storage target. |  [optional] |
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



