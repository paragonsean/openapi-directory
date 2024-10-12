

# EntityIssue

Issue related to the entity.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | Error/Warning code |  [optional] |
|**ddl** | **String** | The ddl which caused the issue, if relevant. |  [optional] |
|**entityType** | [**EntityTypeEnum**](#EntityTypeEnum) | The entity type (if the DDL is for a sub entity). |  [optional] |
|**id** | **String** | Unique Issue ID. |  [optional] |
|**message** | **String** | Issue detailed message |  [optional] |
|**position** | [**Position**](Position.md) |  |  [optional] |
|**severity** | [**SeverityEnum**](#SeverityEnum) | Severity of the issue |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the issue. |  [optional] |



## Enum: EntityTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;DATABASE_ENTITY_TYPE_UNSPECIFIED&quot; |
| SCHEMA | &quot;DATABASE_ENTITY_TYPE_SCHEMA&quot; |
| TABLE | &quot;DATABASE_ENTITY_TYPE_TABLE&quot; |
| COLUMN | &quot;DATABASE_ENTITY_TYPE_COLUMN&quot; |
| CONSTRAINT | &quot;DATABASE_ENTITY_TYPE_CONSTRAINT&quot; |
| INDEX | &quot;DATABASE_ENTITY_TYPE_INDEX&quot; |
| TRIGGER | &quot;DATABASE_ENTITY_TYPE_TRIGGER&quot; |
| VIEW | &quot;DATABASE_ENTITY_TYPE_VIEW&quot; |
| SEQUENCE | &quot;DATABASE_ENTITY_TYPE_SEQUENCE&quot; |
| STORED_PROCEDURE | &quot;DATABASE_ENTITY_TYPE_STORED_PROCEDURE&quot; |
| FUNCTION | &quot;DATABASE_ENTITY_TYPE_FUNCTION&quot; |
| SYNONYM | &quot;DATABASE_ENTITY_TYPE_SYNONYM&quot; |
| DATABASE_PACKAGE | &quot;DATABASE_ENTITY_TYPE_DATABASE_PACKAGE&quot; |
| UDT | &quot;DATABASE_ENTITY_TYPE_UDT&quot; |
| MATERIALIZED_VIEW | &quot;DATABASE_ENTITY_TYPE_MATERIALIZED_VIEW&quot; |
| DATABASE | &quot;DATABASE_ENTITY_TYPE_DATABASE&quot; |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;ISSUE_SEVERITY_UNSPECIFIED&quot; |
| INFO | &quot;ISSUE_SEVERITY_INFO&quot; |
| WARNING | &quot;ISSUE_SEVERITY_WARNING&quot; |
| ERROR | &quot;ISSUE_SEVERITY_ERROR&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;ISSUE_TYPE_UNSPECIFIED&quot; |
| DDL | &quot;ISSUE_TYPE_DDL&quot; |
| APPLY | &quot;ISSUE_TYPE_APPLY&quot; |
| CONVERT | &quot;ISSUE_TYPE_CONVERT&quot; |



