# GoogleWorkspaceAlertCenterApi.RuleViolationInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataSource** | **String** | Source of the data. | [optional] 
**matchInfo** | [**[MatchInfo]**](MatchInfo.md) | List of matches that were found in the resource content. | [optional] 
**recipients** | **[String]** | Resource recipients. For Drive, they are grantees that the Drive file was shared with at the time of rule triggering. Valid values include user emails, group emails, domains, or &#39;anyone&#39; if the file was publicly accessible. If the file was private the recipients list will be empty. For Gmail, they are emails of the users or groups that the Gmail message was sent to. | [optional] 
**resourceInfo** | [**ResourceInfo**](ResourceInfo.md) |  | [optional] 
**ruleInfo** | [**RuleInfo**](RuleInfo.md) |  | [optional] 
**suppressedActionTypes** | **[String]** | Actions suppressed due to other actions with higher priority. | [optional] 
**trigger** | **String** | Trigger of the rule. | [optional] 
**triggeredActionInfo** | **[Object]** | Metadata related to the triggered actions. | [optional] 
**triggeredActionTypes** | **[String]** | Actions applied as a consequence of the rule being triggered. | [optional] 
**triggeringUserEmail** | **String** | Email of the user who caused the violation. Value could be empty if not applicable, for example, a violation found by drive continuous scan. | [optional] 



## Enum: DataSourceEnum


* `DATA_SOURCE_UNSPECIFIED` (value: `"DATA_SOURCE_UNSPECIFIED"`)

* `DRIVE` (value: `"DRIVE"`)





## Enum: [SuppressedActionTypesEnum]


* `ACTION_TYPE_UNSPECIFIED` (value: `"ACTION_TYPE_UNSPECIFIED"`)

* `DRIVE_BLOCK_EXTERNAL_SHARING` (value: `"DRIVE_BLOCK_EXTERNAL_SHARING"`)

* `DRIVE_WARN_ON_EXTERNAL_SHARING` (value: `"DRIVE_WARN_ON_EXTERNAL_SHARING"`)

* `DELETE_WEBPROTECT_EVIDENCE` (value: `"DELETE_WEBPROTECT_EVIDENCE"`)

* `ALERT` (value: `"ALERT"`)

* `RULE_ACTIVATE` (value: `"RULE_ACTIVATE"`)

* `RULE_DEACTIVATE` (value: `"RULE_DEACTIVATE"`)





## Enum: TriggerEnum


* `TRIGGER_UNSPECIFIED` (value: `"TRIGGER_UNSPECIFIED"`)

* `DRIVE_SHARE` (value: `"DRIVE_SHARE"`)





## Enum: [TriggeredActionTypesEnum]


* `ACTION_TYPE_UNSPECIFIED` (value: `"ACTION_TYPE_UNSPECIFIED"`)

* `DRIVE_BLOCK_EXTERNAL_SHARING` (value: `"DRIVE_BLOCK_EXTERNAL_SHARING"`)

* `DRIVE_WARN_ON_EXTERNAL_SHARING` (value: `"DRIVE_WARN_ON_EXTERNAL_SHARING"`)

* `DELETE_WEBPROTECT_EVIDENCE` (value: `"DELETE_WEBPROTECT_EVIDENCE"`)

* `ALERT` (value: `"ALERT"`)

* `RULE_ACTIVATE` (value: `"RULE_ACTIVATE"`)

* `RULE_DEACTIVATE` (value: `"RULE_DEACTIVATE"`)




