

# ThrottledRequestsInput

Api request input for LogAnalytics getThrottledRequests Api.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blobContainerSasUri** | **String** | SAS Uri of the logging blob container to which LogAnalytics Api writes output logs to. |  |
|**fromTime** | **OffsetDateTime** | From time of the query |  |
|**groupByOperationName** | **Boolean** | Group query result by Operation Name. |  [optional] |
|**groupByResourceName** | **Boolean** | Group query result by Resource Name. |  [optional] |
|**groupByThrottlePolicy** | **Boolean** | Group query result by Throttle Policy applied. |  [optional] |
|**toTime** | **OffsetDateTime** | To time of the query |  |



