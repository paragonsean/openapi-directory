

# Relation

Represents a database relation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalOptions** | **Map&lt;String, String&gt;** | Additional options that will be provided as key/value pairs into the options clause of a create table/view statement. See https://cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language for more information on which options are supported. |  [optional] |
|**clusterExpressions** | **List&lt;String&gt;** | A list of columns or SQL expressions used to cluster the table. |  [optional] |
|**dependencyTargets** | [**List&lt;Target&gt;**](Target.md) | A list of actions that this action depends on. |  [optional] |
|**disabled** | **Boolean** | Whether this action is disabled (i.e. should not be run). |  [optional] |
|**incrementalTableConfig** | [**IncrementalTableConfig**](IncrementalTableConfig.md) |  |  [optional] |
|**partitionExpirationDays** | **Integer** | Sets the partition expiration in days. |  [optional] |
|**partitionExpression** | **String** | The SQL expression used to partition the relation. |  [optional] |
|**postOperations** | **List&lt;String&gt;** | SQL statements to be executed after creating the relation. |  [optional] |
|**preOperations** | **List&lt;String&gt;** | SQL statements to be executed before creating the relation. |  [optional] |
|**relationDescriptor** | [**RelationDescriptor**](RelationDescriptor.md) |  |  [optional] |
|**relationType** | [**RelationTypeEnum**](#RelationTypeEnum) | The type of this relation. |  [optional] |
|**requirePartitionFilter** | **Boolean** | Specifies whether queries on this table must include a predicate filter that filters on the partitioning column. |  [optional] |
|**selectQuery** | **String** | The SELECT query which returns rows which this relation should contain. |  [optional] |
|**tags** | **List&lt;String&gt;** | Arbitrary, user-defined tags on this action. |  [optional] |



## Enum: RelationTypeEnum

| Name | Value |
|---- | -----|
| RELATION_TYPE_UNSPECIFIED | &quot;RELATION_TYPE_UNSPECIFIED&quot; |
| TABLE | &quot;TABLE&quot; |
| VIEW | &quot;VIEW&quot; |
| INCREMENTAL_TABLE | &quot;INCREMENTAL_TABLE&quot; |
| MATERIALIZED_VIEW | &quot;MATERIALIZED_VIEW&quot; |



