# DatabaseMigrationApi.EntityDdl

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ddl** | **String** | The actual ddl code. | [optional] 
**ddlType** | **String** | Type of DDL (Create, Alter). | [optional] 
**entity** | **String** | The name of the database entity the ddl refers to. | [optional] 
**entityType** | **String** | The entity type (if the DDL is for a sub entity). | [optional] 
**issueId** | **[String]** | EntityIssues found for this ddl. | [optional] 



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




