# BigQueryDataTransferApi.TimeRange

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **String** | End time of the range of transfer runs. For example, &#x60;\&quot;2017-05-30T00:00:00+00:00\&quot;&#x60;. The end_time must not be in the future. Creates transfer runs where run_time is in the range between start_time (inclusive) and end_time (exclusive). | [optional] 
**startTime** | **String** | Start time of the range of transfer runs. For example, &#x60;\&quot;2017-05-25T00:00:00+00:00\&quot;&#x60;. The start_time must be strictly less than the end_time. Creates transfer runs where run_time is in the range between start_time (inclusive) and end_time (exclusive). | [optional] 


