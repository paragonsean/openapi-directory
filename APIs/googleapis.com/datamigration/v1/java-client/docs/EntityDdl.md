

# EntityDdl

A single DDL statement for a specific entity

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ddl** | **String** | The actual ddl code. |  [optional] |
|**ddlType** | **String** | Type of DDL (Create, Alter). |  [optional] |
|**entity** | **String** | The name of the database entity the ddl refers to. |  [optional] |
|**entityType** | [**EntityTypeEnum**](#EntityTypeEnum) | The entity type (if the DDL is for a sub entity). |  [optional] |
|**issueId** | **List&lt;String&gt;** | EntityIssues found for this ddl. |  [optional] |



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



