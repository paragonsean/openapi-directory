

# ActionRuleProperties

Action rule properties defining scope, conditions, suppression logic for action rule

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**conditions** | [**Conditions**](Conditions.md) |  |  [optional] |
|**createdAt** | **OffsetDateTime** | Creation time of action rule. Date-Time in ISO-8601 format. |  [optional] [readonly] |
|**createdBy** | **String** | Created by user name. |  [optional] [readonly] |
|**description** | **String** | Description of action rule |  [optional] |
|**lastModifiedAt** | **OffsetDateTime** | Last updated time of action rule. Date-Time in ISO-8601 format. |  [optional] [readonly] |
|**lastModifiedBy** | **String** | Last modified by user name. |  [optional] [readonly] |
|**scope** | [**Scope**](Scope.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Indicates if the given action rule is enabled or disabled |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Indicates type of action rule |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SUPPRESSION | &quot;Suppression&quot; |
| ACTION_GROUP | &quot;ActionGroup&quot; |
| DIAGNOSTICS | &quot;Diagnostics&quot; |



