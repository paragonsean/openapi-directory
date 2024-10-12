# AppHubApi.Criticality

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **String** | Optional. Criticality level. Can contain only lowercase letters, numeric characters, underscores, and dashes. Can have a maximum length of 63 characters. | [optional] 
**missionCritical** | **Boolean** | Optional. Indicates mission-critical Application, Service, or Workload. | [optional] 
**type** | **String** | Required. Criticality Type. | [optional] 



## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `MISSION_CRITICAL` (value: `"MISSION_CRITICAL"`)

* `HIGH` (value: `"HIGH"`)

* `MEDIUM` (value: `"MEDIUM"`)

* `LOW` (value: `"LOW"`)




