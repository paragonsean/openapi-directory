

# EnvironmentDetails

Contains information about the environment Play Integrity API runs in, e.g. Play Protect verdict.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appAccessRiskVerdict** | [**AppAccessRiskVerdict**](AppAccessRiskVerdict.md) |  |  [optional] |
|**playProtectVerdict** | [**PlayProtectVerdictEnum**](#PlayProtectVerdictEnum) | The evaluation of Play Protect verdict. |  [optional] |



## Enum: PlayProtectVerdictEnum

| Name | Value |
|---- | -----|
| PLAY_PROTECT_VERDICT_UNSPECIFIED | &quot;PLAY_PROTECT_VERDICT_UNSPECIFIED&quot; |
| UNEVALUATED | &quot;UNEVALUATED&quot; |
| NO_ISSUES | &quot;NO_ISSUES&quot; |
| NO_DATA | &quot;NO_DATA&quot; |
| MEDIUM_RISK | &quot;MEDIUM_RISK&quot; |
| HIGH_RISK | &quot;HIGH_RISK&quot; |
| POSSIBLE_RISK | &quot;POSSIBLE_RISK&quot; |



