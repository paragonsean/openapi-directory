# CloudSpannerApi.PartitionQueryRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paramTypes** | [**{String: Type}**](Type.md) | It is not always possible for Cloud Spanner to infer the right SQL type from a JSON value. For example, values of type &#x60;BYTES&#x60; and values of type &#x60;STRING&#x60; both appear in params as JSON strings. In these cases, &#x60;param_types&#x60; can be used to specify the exact SQL type for some or all of the SQL query parameters. See the definition of Type for more information about SQL types. | [optional] 
**params** | **{String: Object}** | Parameter names and values that bind to placeholders in the SQL string. A parameter placeholder consists of the &#x60;@&#x60; character followed by the parameter name (for example, &#x60;@firstName&#x60;). Parameter names can contain letters, numbers, and underscores. Parameters can appear anywhere that a literal value is expected. The same parameter name can be used more than once, for example: &#x60;\&quot;WHERE id &gt; @msg_id AND id &lt; @msg_id + 100\&quot;&#x60; It is an error to execute a SQL statement with unbound parameters. | [optional] 
**partitionOptions** | [**PartitionOptions**](PartitionOptions.md) |  | [optional] 
**sql** | **String** | Required. The query request to generate partitions for. The request will fail if the query is not root partitionable. For a query to be root partitionable, it needs to satisfy a few conditions. For example, if the query execution plan contains a distributed union operator, then it must be the first operator in the plan. For more information about other conditions, see [Read data in parallel](https://cloud.google.com/spanner/docs/reads#read_data_in_parallel). The query request must not contain DML commands, such as INSERT, UPDATE, or DELETE. Use ExecuteStreamingSql with a PartitionedDml transaction for large, partition-friendly DML operations. | [optional] 
**transaction** | [**TransactionSelector**](TransactionSelector.md) |  | [optional] 


