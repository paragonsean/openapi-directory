

# RuleViolationInfo

Common alert information about violated rules that are configured by Google Workspace administrators.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSource** | [**DataSourceEnum**](#DataSourceEnum) | Source of the data. |  [optional] |
|**matchInfo** | [**List&lt;MatchInfo&gt;**](MatchInfo.md) | List of matches that were found in the resource content. |  [optional] |
|**recipients** | **List&lt;String&gt;** | Resource recipients. For Drive, they are grantees that the Drive file was shared with at the time of rule triggering. Valid values include user emails, group emails, domains, or &#39;anyone&#39; if the file was publicly accessible. If the file was private the recipients list will be empty. For Gmail, they are emails of the users or groups that the Gmail message was sent to. |  [optional] |
|**resourceInfo** | [**ResourceInfo**](ResourceInfo.md) |  |  [optional] |
|**ruleInfo** | [**RuleInfo**](RuleInfo.md) |  |  [optional] |
|**suppressedActionTypes** | [**List&lt;SuppressedActionTypesEnum&gt;**](#List&lt;SuppressedActionTypesEnum&gt;) | Actions suppressed due to other actions with higher priority. |  [optional] |
|**trigger** | [**TriggerEnum**](#TriggerEnum) | Trigger of the rule. |  [optional] |
|**triggeredActionInfo** | **List&lt;Object&gt;** | Metadata related to the triggered actions. |  [optional] |
|**triggeredActionTypes** | [**List&lt;TriggeredActionTypesEnum&gt;**](#List&lt;TriggeredActionTypesEnum&gt;) | Actions applied as a consequence of the rule being triggered. |  [optional] |
|**triggeringUserEmail** | **String** | Email of the user who caused the violation. Value could be empty if not applicable, for example, a violation found by drive continuous scan. |  [optional] |



## Enum: DataSourceEnum

| Name | Value |
|---- | -----|
| DATA_SOURCE_UNSPECIFIED | &quot;DATA_SOURCE_UNSPECIFIED&quot; |
| DRIVE | &quot;DRIVE&quot; |



## Enum: List&lt;SuppressedActionTypesEnum&gt;

| Name | Value |
|---- | -----|
| ACTION_TYPE_UNSPECIFIED | &quot;ACTION_TYPE_UNSPECIFIED&quot; |
| DRIVE_BLOCK_EXTERNAL_SHARING | &quot;DRIVE_BLOCK_EXTERNAL_SHARING&quot; |
| DRIVE_WARN_ON_EXTERNAL_SHARING | &quot;DRIVE_WARN_ON_EXTERNAL_SHARING&quot; |
| DELETE_WEBPROTECT_EVIDENCE | &quot;DELETE_WEBPROTECT_EVIDENCE&quot; |
| ALERT | &quot;ALERT&quot; |
| RULE_ACTIVATE | &quot;RULE_ACTIVATE&quot; |
| RULE_DEACTIVATE | &quot;RULE_DEACTIVATE&quot; |



## Enum: TriggerEnum

| Name | Value |
|---- | -----|
| TRIGGER_UNSPECIFIED | &quot;TRIGGER_UNSPECIFIED&quot; |
| DRIVE_SHARE | &quot;DRIVE_SHARE&quot; |



## Enum: List&lt;TriggeredActionTypesEnum&gt;

| Name | Value |
|---- | -----|
| ACTION_TYPE_UNSPECIFIED | &quot;ACTION_TYPE_UNSPECIFIED&quot; |
| DRIVE_BLOCK_EXTERNAL_SHARING | &quot;DRIVE_BLOCK_EXTERNAL_SHARING&quot; |
| DRIVE_WARN_ON_EXTERNAL_SHARING | &quot;DRIVE_WARN_ON_EXTERNAL_SHARING&quot; |
| DELETE_WEBPROTECT_EVIDENCE | &quot;DELETE_WEBPROTECT_EVIDENCE&quot; |
| ALERT | &quot;ALERT&quot; |
| RULE_ACTIVATE | &quot;RULE_ACTIVATE&quot; |
| RULE_DEACTIVATE | &quot;RULE_DEACTIVATE&quot; |



