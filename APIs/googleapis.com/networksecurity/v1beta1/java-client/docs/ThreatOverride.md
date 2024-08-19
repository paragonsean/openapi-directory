

# ThreatOverride

Defines what action to take for a specific threat_id match.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) | Required. Threat action override. For some threat types, only a subset of actions applies. |  [optional] |
|**threatId** | **String** | Required. Vendor-specific ID of a threat to override. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Output only. Type of the threat (read only). |  [optional] [readonly] |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| THREAT_ACTION_UNSPECIFIED | &quot;THREAT_ACTION_UNSPECIFIED&quot; |
| DEFAULT_ACTION | &quot;DEFAULT_ACTION&quot; |
| ALLOW | &quot;ALLOW&quot; |
| ALERT | &quot;ALERT&quot; |
| DENY | &quot;DENY&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| THREAT_TYPE_UNSPECIFIED | &quot;THREAT_TYPE_UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| VULNERABILITY | &quot;VULNERABILITY&quot; |
| ANTIVIRUS | &quot;ANTIVIRUS&quot; |
| SPYWARE | &quot;SPYWARE&quot; |
| DNS | &quot;DNS&quot; |



