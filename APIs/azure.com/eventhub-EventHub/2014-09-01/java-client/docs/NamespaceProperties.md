

# NamespaceProperties

Properties of the Namespace supplied for create or update Namespace operation

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | The time the Namespace was created. |  [optional] |
|**enabled** | **Boolean** | Specifies whether this instance is enabled. |  [optional] |
|**metricId** | **String** | Identifier for Azure Insights metrics |  [optional] [readonly] |
|**provisioningState** | **String** | Provisioning state of the Namespace. |  [optional] |
|**serviceBusEndpoint** | **String** | Endpoint you can use to perform Service Bus operations. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | State of the Namespace. |  [optional] |
|**updatedAt** | **OffsetDateTime** | The time the Namespace was updated. |  [optional] |



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



