

# Job

Job details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **String** | The start time. |  [optional] |
|**error** | [**ARMException**](ARMException.md) |  |  [optional] |
|**properties** | [**JobProperties**](JobProperties.md) |  |  [optional] |
|**startTime** | **String** | The start time. |  [optional] |
|**status** | **String** | The status of the Job. ARM expects the terminal status to be one of (1) Succeeded, (2) Failed or (3) Canceled. All other values imply that the operation is still running / being applied. |  [optional] |
|**id** | **String** | Resource Id |  [optional] [readonly] |
|**location** | **String** | Resource Location |  [optional] |
|**name** | **String** | Resource Name |  [optional] [readonly] |
|**type** | **String** | Resource Type |  [optional] [readonly] |



