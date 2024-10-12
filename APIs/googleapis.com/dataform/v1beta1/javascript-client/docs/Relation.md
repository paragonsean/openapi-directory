# DataformApi.Relation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalOptions** | **{String: String}** | Additional options that will be provided as key/value pairs into the options clause of a create table/view statement. See https://cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language for more information on which options are supported. | [optional] 
**clusterExpressions** | **[String]** | A list of columns or SQL expressions used to cluster the table. | [optional] 
**dependencyTargets** | [**[Target]**](Target.md) | A list of actions that this action depends on. | [optional] 
**disabled** | **Boolean** | Whether this action is disabled (i.e. should not be run). | [optional] 
**incrementalTableConfig** | [**IncrementalTableConfig**](IncrementalTableConfig.md) |  | [optional] 
**partitionExpirationDays** | **Number** | Sets the partition expiration in days. | [optional] 
**partitionExpression** | **String** | The SQL expression used to partition the relation. | [optional] 
**postOperations** | **[String]** | SQL statements to be executed after creating the relation. | [optional] 
**preOperations** | **[String]** | SQL statements to be executed before creating the relation. | [optional] 
**relationDescriptor** | [**RelationDescriptor**](RelationDescriptor.md) |  | [optional] 
**relationType** | **String** | The type of this relation. | [optional] 
**requirePartitionFilter** | **Boolean** | Specifies whether queries on this table must include a predicate filter that filters on the partitioning column. | [optional] 
**selectQuery** | **String** | The SELECT query which returns rows which this relation should contain. | [optional] 
**tags** | **[String]** | Arbitrary, user-defined tags on this action. | [optional] 



## Enum: RelationTypeEnum


* `RELATION_TYPE_UNSPECIFIED` (value: `"RELATION_TYPE_UNSPECIFIED"`)

* `TABLE` (value: `"TABLE"`)

* `VIEW` (value: `"VIEW"`)

* `INCREMENTAL_TABLE` (value: `"INCREMENTAL_TABLE"`)

* `MATERIALIZED_VIEW` (value: `"MATERIALIZED_VIEW"`)




