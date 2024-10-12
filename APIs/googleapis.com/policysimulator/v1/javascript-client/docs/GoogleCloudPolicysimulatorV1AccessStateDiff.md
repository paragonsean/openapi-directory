# PolicySimulatorApi.GoogleCloudPolicysimulatorV1AccessStateDiff

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessChange** | **String** | How the principal&#39;s access, specified in the AccessState field, changed between the current (baseline) policies and proposed (simulated) policies. | [optional] 
**baseline** | [**GoogleCloudPolicysimulatorV1ExplainedAccess**](GoogleCloudPolicysimulatorV1ExplainedAccess.md) |  | [optional] 
**simulated** | [**GoogleCloudPolicysimulatorV1ExplainedAccess**](GoogleCloudPolicysimulatorV1ExplainedAccess.md) |  | [optional] 



## Enum: AccessChangeEnum


* `ACCESS_CHANGE_TYPE_UNSPECIFIED` (value: `"ACCESS_CHANGE_TYPE_UNSPECIFIED"`)

* `NO_CHANGE` (value: `"NO_CHANGE"`)

* `UNKNOWN_CHANGE` (value: `"UNKNOWN_CHANGE"`)

* `ACCESS_REVOKED` (value: `"ACCESS_REVOKED"`)

* `ACCESS_GAINED` (value: `"ACCESS_GAINED"`)

* `ACCESS_MAYBE_REVOKED` (value: `"ACCESS_MAYBE_REVOKED"`)

* `ACCESS_MAYBE_GAINED` (value: `"ACCESS_MAYBE_GAINED"`)




