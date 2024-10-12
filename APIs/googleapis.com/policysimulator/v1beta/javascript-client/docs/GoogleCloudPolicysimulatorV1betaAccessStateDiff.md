# PolicySimulatorApi.GoogleCloudPolicysimulatorV1betaAccessStateDiff

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessChange** | **String** | How the principal&#39;s access, specified in the AccessState field, changed between the current (baseline) policies and proposed (simulated) policies. | [optional] 
**baseline** | [**GoogleCloudPolicysimulatorV1betaExplainedAccess**](GoogleCloudPolicysimulatorV1betaExplainedAccess.md) |  | [optional] 
**simulated** | [**GoogleCloudPolicysimulatorV1betaExplainedAccess**](GoogleCloudPolicysimulatorV1betaExplainedAccess.md) |  | [optional] 



## Enum: AccessChangeEnum


* `ACCESS_CHANGE_TYPE_UNSPECIFIED` (value: `"ACCESS_CHANGE_TYPE_UNSPECIFIED"`)

* `NO_CHANGE` (value: `"NO_CHANGE"`)

* `UNKNOWN_CHANGE` (value: `"UNKNOWN_CHANGE"`)

* `ACCESS_REVOKED` (value: `"ACCESS_REVOKED"`)

* `ACCESS_GAINED` (value: `"ACCESS_GAINED"`)

* `ACCESS_MAYBE_REVOKED` (value: `"ACCESS_MAYBE_REVOKED"`)

* `ACCESS_MAYBE_GAINED` (value: `"ACCESS_MAYBE_GAINED"`)




