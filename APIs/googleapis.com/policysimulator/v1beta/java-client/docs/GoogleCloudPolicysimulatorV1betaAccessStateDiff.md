

# GoogleCloudPolicysimulatorV1betaAccessStateDiff

A summary and comparison of the principal's access under the current (baseline) policies and the proposed (simulated) policies for a single access tuple.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessChange** | [**AccessChangeEnum**](#AccessChangeEnum) | How the principal&#39;s access, specified in the AccessState field, changed between the current (baseline) policies and proposed (simulated) policies. |  [optional] |
|**baseline** | [**GoogleCloudPolicysimulatorV1betaExplainedAccess**](GoogleCloudPolicysimulatorV1betaExplainedAccess.md) |  |  [optional] |
|**simulated** | [**GoogleCloudPolicysimulatorV1betaExplainedAccess**](GoogleCloudPolicysimulatorV1betaExplainedAccess.md) |  |  [optional] |



## Enum: AccessChangeEnum

| Name | Value |
|---- | -----|
| ACCESS_CHANGE_TYPE_UNSPECIFIED | &quot;ACCESS_CHANGE_TYPE_UNSPECIFIED&quot; |
| NO_CHANGE | &quot;NO_CHANGE&quot; |
| UNKNOWN_CHANGE | &quot;UNKNOWN_CHANGE&quot; |
| ACCESS_REVOKED | &quot;ACCESS_REVOKED&quot; |
| ACCESS_GAINED | &quot;ACCESS_GAINED&quot; |
| ACCESS_MAYBE_REVOKED | &quot;ACCESS_MAYBE_REVOKED&quot; |
| ACCESS_MAYBE_GAINED | &quot;ACCESS_MAYBE_GAINED&quot; |



