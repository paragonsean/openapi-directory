

# CollectdPayloadError

Describes the error status for payloads that were not written.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**error** | [**Status**](Status.md) |  |  [optional] |
|**index** | **Integer** | The zero-based index in CreateCollectdTimeSeriesRequest.collectd_payloads. |  [optional] |
|**valueErrors** | [**List&lt;CollectdValueError&gt;**](CollectdValueError.md) | Records the error status for values that were not written due to an error.Failed payloads for which nothing is written will not include partial value errors. |  [optional] |



