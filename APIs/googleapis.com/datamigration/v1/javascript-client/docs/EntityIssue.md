# DatabaseMigrationApi.EntityIssue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **String** | Error/Warning code | [optional] 
**ddl** | **String** | The ddl which caused the issue, if relevant. | [optional] 
**entityType** | **String** | The entity type (if the DDL is for a sub entity). | [optional] 
**id** | **String** | Unique Issue ID. | [optional] 
**message** | **String** | Issue detailed message | [optional] 
**position** | [**Position**](Position.md) |  | [optional] 
**severity** | **String** | Severity of the issue | [optional] 
**type** | **String** | The type of the issue. | [optional] 



## Enum: EntityTypeEnum


* `UNSPECIFIED` (value: `"DATABASE_ENTITY_TYPE_UNSPECIFIED"`)

* `SCHEMA` (value: `"DATABASE_ENTITY_TYPE_SCHEMA"`)

* `TABLE` (value: `"DATABASE_ENTITY_TYPE_TABLE"`)

* `COLUMN` (value: `"DATABASE_ENTITY_TYPE_COLUMN"`)

* `CONSTRAINT` (value: `"DATABASE_ENTITY_TYPE_CONSTRAINT"`)

* `INDEX` (value: `"DATABASE_ENTITY_TYPE_INDEX"`)

* `TRIGGER` (value: `"DATABASE_ENTITY_TYPE_TRIGGER"`)

* `VIEW` (value: `"DATABASE_ENTITY_TYPE_VIEW"`)

* `SEQUENCE` (value: `"DATABASE_ENTITY_TYPE_SEQUENCE"`)

* `STORED_PROCEDURE` (value: `"DATABASE_ENTITY_TYPE_STORED_PROCEDURE"`)

* `FUNCTION` (value: `"DATABASE_ENTITY_TYPE_FUNCTION"`)

* `SYNONYM` (value: `"DATABASE_ENTITY_TYPE_SYNONYM"`)

* `DATABASE_PACKAGE` (value: `"DATABASE_ENTITY_TYPE_DATABASE_PACKAGE"`)

* `UDT` (value: `"DATABASE_ENTITY_TYPE_UDT"`)

* `MATERIALIZED_VIEW` (value: `"DATABASE_ENTITY_TYPE_MATERIALIZED_VIEW"`)

* `DATABASE` (value: `"DATABASE_ENTITY_TYPE_DATABASE"`)





## Enum: SeverityEnum


* `UNSPECIFIED` (value: `"ISSUE_SEVERITY_UNSPECIFIED"`)

* `INFO` (value: `"ISSUE_SEVERITY_INFO"`)

* `WARNING` (value: `"ISSUE_SEVERITY_WARNING"`)

* `ERROR` (value: `"ISSUE_SEVERITY_ERROR"`)





## Enum: TypeEnum


* `UNSPECIFIED` (value: `"ISSUE_TYPE_UNSPECIFIED"`)

* `DDL` (value: `"ISSUE_TYPE_DDL"`)

* `APPLY` (value: `"ISSUE_TYPE_APPLY"`)

* `CONVERT` (value: `"ISSUE_TYPE_CONVERT"`)




