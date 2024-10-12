

# StreamingStragglerInfo

Information useful for streaming straggler identification and debugging.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataWatermarkLag** | **String** | The event-time watermark lag at the time of the straggler detection. |  [optional] |
|**endTime** | **String** | End time of this straggler. |  [optional] |
|**startTime** | **String** | Start time of this straggler. |  [optional] |
|**systemWatermarkLag** | **String** | The system watermark lag at the time of the straggler detection. |  [optional] |
|**workerName** | **String** | Name of the worker where the straggler was detected. |  [optional] |



