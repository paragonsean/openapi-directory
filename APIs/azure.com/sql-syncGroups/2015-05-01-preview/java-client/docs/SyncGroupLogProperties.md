

# SyncGroupLogProperties

Properties of an Azure SQL Database sync group log.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**details** | **String** | Details of the sync group log. |  [optional] [readonly] |
|**operationStatus** | **String** | OperationStatus of the sync group log. |  [optional] [readonly] |
|**source** | **String** | Source of the sync group log. |  [optional] [readonly] |
|**timestamp** | **OffsetDateTime** | Timestamp of the sync group log. |  [optional] [readonly] |
|**tracingId** | **UUID** | TracingId of the sync group log. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the sync group log. |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ALL | &quot;All&quot; |
| ERROR | &quot;Error&quot; |
| WARNING | &quot;Warning&quot; |
| SUCCESS | &quot;Success&quot; |



