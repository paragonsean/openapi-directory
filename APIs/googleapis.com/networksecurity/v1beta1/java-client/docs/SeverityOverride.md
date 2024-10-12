

# SeverityOverride

Defines what action to take for a specific severity match.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) | Required. Threat action override. |  [optional] |
|**severity** | [**SeverityEnum**](#SeverityEnum) | Required. Severity level to match. |  [optional] |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| THREAT_ACTION_UNSPECIFIED | &quot;THREAT_ACTION_UNSPECIFIED&quot; |
| DEFAULT_ACTION | &quot;DEFAULT_ACTION&quot; |
| ALLOW | &quot;ALLOW&quot; |
| ALERT | &quot;ALERT&quot; |
| DENY | &quot;DENY&quot; |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| SEVERITY_UNSPECIFIED | &quot;SEVERITY_UNSPECIFIED&quot; |
| INFORMATIONAL | &quot;INFORMATIONAL&quot; |
| LOW | &quot;LOW&quot; |
| MEDIUM | &quot;MEDIUM&quot; |
| HIGH | &quot;HIGH&quot; |
| CRITICAL | &quot;CRITICAL&quot; |



