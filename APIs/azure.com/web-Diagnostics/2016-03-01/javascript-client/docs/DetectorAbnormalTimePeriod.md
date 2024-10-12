# DiagnosticsApiClient.DetectorAbnormalTimePeriod

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **Date** | End time of the correlated event | [optional] 
**message** | **String** | Message describing the event | [optional] 
**metaData** | **[[AnalysisDataDataInnerInner]]** | Downtime metadata | [optional] 
**priority** | **Number** | Represents the rank of the Detector | [optional] 
**solutions** | [**[Solution]**](Solution.md) | List of proposed solutions | [optional] 
**source** | **String** | Represents the name of the Detector | [optional] 
**startTime** | **Date** | Start time of the correlated event | [optional] 
**type** | **String** | Represents the type of the Detector | [optional] 



## Enum: TypeEnum


* `ServiceIncident` (value: `"ServiceIncident"`)

* `AppDeployment` (value: `"AppDeployment"`)

* `AppCrash` (value: `"AppCrash"`)

* `RuntimeIssueDetected` (value: `"RuntimeIssueDetected"`)

* `AseDeployment` (value: `"AseDeployment"`)

* `UserIssue` (value: `"UserIssue"`)

* `PlatformIssue` (value: `"PlatformIssue"`)

* `Other` (value: `"Other"`)




