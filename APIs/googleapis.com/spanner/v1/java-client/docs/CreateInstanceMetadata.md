

# CreateInstanceMetadata

Metadata type for the operation returned by CreateInstance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cancelTime** | **String** | The time at which this operation was cancelled. If set, this operation is in the process of undoing itself (which is guaranteed to succeed) and cannot be cancelled again. |  [optional] |
|**endTime** | **String** | The time at which this operation failed or was completed successfully. |  [optional] |
|**expectedFulfillmentPeriod** | [**ExpectedFulfillmentPeriodEnum**](#ExpectedFulfillmentPeriodEnum) | The expected fulfillment period of this create operation. |  [optional] |
|**instance** | [**Instance**](Instance.md) |  |  [optional] |
|**startTime** | **String** | The time at which the CreateInstance request was received. |  [optional] |



## Enum: ExpectedFulfillmentPeriodEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;FULFILLMENT_PERIOD_UNSPECIFIED&quot; |
| NORMAL | &quot;FULFILLMENT_PERIOD_NORMAL&quot; |
| EXTENDED | &quot;FULFILLMENT_PERIOD_EXTENDED&quot; |



