

# Retry

Retries the failed job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attempts** | **String** | Required. Total number of retries. Retry is skipped if set to 0; The minimum value is 1, and the maximum value is 10. |  [optional] |
|**backoffMode** | [**BackoffModeEnum**](#BackoffModeEnum) | Optional. The pattern of how wait time will be increased. Default is linear. Backoff mode will be ignored if &#x60;wait&#x60; is 0. |  [optional] |
|**wait** | **String** | Optional. How long to wait for the first retry. Default is 0, and the maximum value is 14d. |  [optional] |



## Enum: BackoffModeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;BACKOFF_MODE_UNSPECIFIED&quot; |
| LINEAR | &quot;BACKOFF_MODE_LINEAR&quot; |
| EXPONENTIAL | &quot;BACKOFF_MODE_EXPONENTIAL&quot; |



