

# NamespaceProperties

Properties of the namespace.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createACSNamespace** | **Boolean** | Indicates whether to create an ACS namespace. |  [optional] |
|**createdAt** | **OffsetDateTime** | The time the namespace was created. |  [optional] [readonly] |
|**enabled** | **Boolean** | Specifies whether this instance is enabled. |  [optional] |
|**provisioningState** | **String** | Provisioning state of the namespace. |  [optional] [readonly] |
|**serviceBusEndpoint** | **String** | Endpoint you can use to perform Service Bus operations. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | State of the namespace. |  [optional] |
|**updatedAt** | **OffsetDateTime** | The time the namespace was updated. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| CREATING | &quot;Creating&quot; |
| CREATED | &quot;Created&quot; |
| ACTIVATING | &quot;Activating&quot; |
| ENABLING | &quot;Enabling&quot; |
| ACTIVE | &quot;Active&quot; |
| DISABLING | &quot;Disabling&quot; |
| DISABLED | &quot;Disabled&quot; |
| SOFT_DELETING | &quot;SoftDeleting&quot; |
| SOFT_DELETED | &quot;SoftDeleted&quot; |
| REMOVING | &quot;Removing&quot; |
| REMOVED | &quot;Removed&quot; |
| FAILED | &quot;Failed&quot; |



