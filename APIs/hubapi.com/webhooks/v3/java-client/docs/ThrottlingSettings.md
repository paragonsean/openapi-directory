

# ThrottlingSettings

Configuration details for webhook throttling.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxConcurrentRequests** | **Integer** | The maximum number of concurrent HTTP requests HubSpot will attempt to make to your app. |  |
|**period** | [**PeriodEnum**](#PeriodEnum) | Time scale for this setting. Can be either &#x60;SECONDLY&#x60; (per second) or &#x60;ROLLING_MINUTE&#x60; (per minute). |  |



## Enum: PeriodEnum

| Name | Value |
|---- | -----|
| SECONDLY | &quot;SECONDLY&quot; |
| ROLLING_MINUTE | &quot;ROLLING_MINUTE&quot; |



