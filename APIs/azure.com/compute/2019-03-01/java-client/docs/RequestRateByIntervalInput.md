

# RequestRateByIntervalInput

Api request input for LogAnalytics getRequestRateByInterval Api.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**intervalLength** | [**IntervalLengthEnum**](#IntervalLengthEnum) | Interval value in minutes used to create LogAnalytics call rate logs. |  |
|**blobContainerSasUri** | **String** | SAS Uri of the logging blob container to which LogAnalytics Api writes output logs to. |  |
|**fromTime** | **OffsetDateTime** | From time of the query |  |
|**groupByOperationName** | **Boolean** | Group query result by Operation Name. |  [optional] |
|**groupByResourceName** | **Boolean** | Group query result by Resource Name. |  [optional] |
|**groupByThrottlePolicy** | **Boolean** | Group query result by Throttle Policy applied. |  [optional] |
|**toTime** | **OffsetDateTime** | To time of the query |  |



## Enum: IntervalLengthEnum

| Name | Value |
|---- | -----|
| THREE_MINS | &quot;ThreeMins&quot; |
| FIVE_MINS | &quot;FiveMins&quot; |
| THIRTY_MINS | &quot;ThirtyMins&quot; |
| SIXTY_MINS | &quot;SixtyMins&quot; |



