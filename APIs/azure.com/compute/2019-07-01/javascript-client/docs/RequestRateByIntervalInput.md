# ComputeManagementClient.RequestRateByIntervalInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intervalLength** | **String** | Interval value in minutes used to create LogAnalytics call rate logs. | 
**blobContainerSasUri** | **String** | SAS Uri of the logging blob container to which LogAnalytics Api writes output logs to. | 
**fromTime** | **Date** | From time of the query | 
**groupByOperationName** | **Boolean** | Group query result by Operation Name. | [optional] 
**groupByResourceName** | **Boolean** | Group query result by Resource Name. | [optional] 
**groupByThrottlePolicy** | **Boolean** | Group query result by Throttle Policy applied. | [optional] 
**toTime** | **Date** | To time of the query | 



## Enum: IntervalLengthEnum


* `ThreeMins` (value: `"ThreeMins"`)

* `FiveMins` (value: `"FiveMins"`)

* `ThirtyMins` (value: `"ThirtyMins"`)

* `SixtyMins` (value: `"SixtyMins"`)




