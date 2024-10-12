

# QueuedInvoice


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clonedFromId** | **Integer** |  |  [optional] |
|**id** | **Integer** |  |  [optional] |
|**invoice** | [**Invoice**](Invoice.md) |  |  [optional] |
|**invoiceId** | **Integer** |  |  [optional] |
|**recurringProfileId** | **Integer** |  |  [optional] |
|**scheduledFor** | **OffsetDateTime** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**userId** | **Integer** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;Pending&quot; |
| CANCELLED | &quot;Cancelled&quot; |
| FAILED | &quot;Failed&quot; |
| PROCESSED | &quot;Processed&quot; |



