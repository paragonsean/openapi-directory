

# ScopeMapProperties

The properties of a scope map.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actions** | **List&lt;String&gt;** | The list of scoped permissions for registry artifacts.  E.g. repositories/repository-name/content/read,  repositories/repository-name/metadata/write |  |
|**creationDate** | **OffsetDateTime** | The creation date of scope map. |  [optional] [readonly] |
|**description** | **String** | The user friendly description of the scope map. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Provisioning state of the resource. |  [optional] [readonly] |
|**type** | **String** | The type of the scope map. E.g. BuildIn scope map. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |



