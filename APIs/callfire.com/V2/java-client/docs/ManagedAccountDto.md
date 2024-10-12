

# ManagedAccountDto

~

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountHolderId** | **String** | ~ |  [optional] |
|**credits** | **BigDecimal** | ~ |  [optional] |
|**email** | **String** | ~ |  [optional] |
|**id** | **String** | ~ |  [optional] |
|**lastLogin** | **OffsetDateTime** | ~ |  [optional] |
|**name** | **String** | ~ |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | ~ |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;ACTIVE&quot; |
| PENDING | &quot;PENDING&quot; |
| PENDING_VERIFICATION | &quot;PENDING_VERIFICATION&quot; |
| IN_REVIEW | &quot;IN_REVIEW&quot; |



