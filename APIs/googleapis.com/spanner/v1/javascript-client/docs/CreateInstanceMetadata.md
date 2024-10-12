# CloudSpannerApi.CreateInstanceMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancelTime** | **String** | The time at which this operation was cancelled. If set, this operation is in the process of undoing itself (which is guaranteed to succeed) and cannot be cancelled again. | [optional] 
**endTime** | **String** | The time at which this operation failed or was completed successfully. | [optional] 
**expectedFulfillmentPeriod** | **String** | The expected fulfillment period of this create operation. | [optional] 
**instance** | [**Instance**](Instance.md) |  | [optional] 
**startTime** | **String** | The time at which the CreateInstance request was received. | [optional] 



## Enum: ExpectedFulfillmentPeriodEnum


* `UNSPECIFIED` (value: `"FULFILLMENT_PERIOD_UNSPECIFIED"`)

* `NORMAL` (value: `"FULFILLMENT_PERIOD_NORMAL"`)

* `EXTENDED` (value: `"FULFILLMENT_PERIOD_EXTENDED"`)




