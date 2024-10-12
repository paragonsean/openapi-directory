# RubrikRestApi.PrecheckStatusResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **Number** | The Unix epoch timestamp, in milliseconds, corresponding to the end of the last completed upgrade prechecks job instance.  | 
**failureResults** | [**[PrecheckFailureResult]**](PrecheckFailureResult.md) | The results of the failed prechecks. This includes the name of the failed prechecks and details of the error. | 
**isOnDemand** | **Boolean** | Specifies whether this result is from a user-triggered job. | 
**nextRunInfo** | [**PrecheckStatusNextRunInfo**](PrecheckStatusNextRunInfo.md) |  | [optional] 
**numPrechecksRun** | **Number** | Total number of upgrade prechecks that were run. | 
**runPeriodInMinutes** | **Number** | Time, in minutes, between consecutive runs of scheduled upgrade prechecks job instances.  | 
**startTime** | **Number** | The Unix epoch timestamp, in milliseconds, corresponding to the start of the last completed upgrade prechecks job instance.  | 


