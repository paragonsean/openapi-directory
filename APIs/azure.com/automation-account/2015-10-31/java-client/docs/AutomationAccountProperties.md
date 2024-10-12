

# AutomationAccountProperties

Definition of the account property.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationTime** | **OffsetDateTime** | Gets the creation time. |  [optional] [readonly] |
|**description** | **String** | Gets or sets the description. |  [optional] |
|**lastModifiedBy** | **String** | Gets or sets the last modified by. |  [optional] |
|**lastModifiedTime** | **OffsetDateTime** | Gets the last modified time. |  [optional] [readonly] |
|**sku** | [**Sku**](Sku.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Gets status of account. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| OK | &quot;Ok&quot; |
| UNAVAILABLE | &quot;Unavailable&quot; |
| SUSPENDED | &quot;Suspended&quot; |



