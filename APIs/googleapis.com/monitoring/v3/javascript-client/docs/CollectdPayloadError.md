# CloudMonitoringApi.CollectdPayloadError

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**Status**](Status.md) |  | [optional] 
**index** | **Number** | The zero-based index in CreateCollectdTimeSeriesRequest.collectd_payloads. | [optional] 
**valueErrors** | [**[CollectdValueError]**](CollectdValueError.md) | Records the error status for values that were not written due to an error.Failed payloads for which nothing is written will not include partial value errors. | [optional] 


