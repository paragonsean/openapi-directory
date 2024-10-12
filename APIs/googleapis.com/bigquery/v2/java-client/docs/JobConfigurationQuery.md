

# JobConfigurationQuery

JobConfigurationQuery configures a BigQuery query job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowLargeResults** | **Boolean** | Optional. If true and query uses legacy SQL dialect, allows the query to produce arbitrarily large result tables at a slight cost in performance. Requires destinationTable to be set. For GoogleSQL queries, this flag is ignored and large results are always allowed. However, you must still set destinationTable when result size exceeds the allowed maximum response size. |  [optional] |
|**clustering** | [**Clustering**](Clustering.md) |  |  [optional] |
|**connectionProperties** | [**List&lt;ConnectionProperty&gt;**](ConnectionProperty.md) | Connection properties which can modify the query behavior. |  [optional] |
|**continuous** | **Boolean** | [Optional] Specifies whether the query should be executed as a continuous query. The default value is false. |  [optional] |
|**createDisposition** | **String** | Optional. Specifies whether the job is allowed to create new tables. The following values are supported: * CREATE_IF_NEEDED: If the table does not exist, BigQuery creates the table. * CREATE_NEVER: The table must already exist. If it does not, a &#39;notFound&#39; error is returned in the job result. The default value is CREATE_IF_NEEDED. Creation, truncation and append actions occur as one atomic update upon job completion. |  [optional] |
|**createSession** | **Boolean** | If this property is true, the job creates a new session using a randomly generated session_id. To continue using a created session with subsequent queries, pass the existing session identifier as a &#x60;ConnectionProperty&#x60; value. The session identifier is returned as part of the &#x60;SessionInfo&#x60; message within the query statistics. The new session&#39;s location will be set to &#x60;Job.JobReference.location&#x60; if it is present, otherwise it&#39;s set to the default location based on existing routing logic. |  [optional] |
|**defaultDataset** | [**DatasetReference**](DatasetReference.md) |  |  [optional] |
|**destinationEncryptionConfiguration** | [**EncryptionConfiguration**](EncryptionConfiguration.md) |  |  [optional] |
|**destinationTable** | [**TableReference**](TableReference.md) |  |  [optional] |
|**flattenResults** | **Boolean** | Optional. If true and query uses legacy SQL dialect, flattens all nested and repeated fields in the query results. allowLargeResults must be true if this is set to false. For GoogleSQL queries, this flag is ignored and results are never flattened. |  [optional] |
|**maximumBillingTier** | **Integer** | Optional. [Deprecated] Maximum billing tier allowed for this query. The billing tier controls the amount of compute resources allotted to the query, and multiplies the on-demand cost of the query accordingly. A query that runs within its allotted resources will succeed and indicate its billing tier in statistics.query.billingTier, but if the query exceeds its allotted resources, it will fail with billingTierLimitExceeded. WARNING: The billed byte amount can be multiplied by an amount up to this number! Most users should not need to alter this setting, and we recommend that you avoid introducing new uses of it. |  [optional] |
|**maximumBytesBilled** | **String** | Limits the bytes billed for this job. Queries that will have bytes billed beyond this limit will fail (without incurring a charge). If unspecified, this will be set to your project default. |  [optional] |
|**parameterMode** | **String** | GoogleSQL only. Set to POSITIONAL to use positional (?) query parameters or to NAMED to use named (@myparam) query parameters in this query. |  [optional] |
|**preserveNulls** | **Boolean** | [Deprecated] This property is deprecated. |  [optional] |
|**priority** | **String** | Optional. Specifies a priority for the query. Possible values include INTERACTIVE and BATCH. The default value is INTERACTIVE. |  [optional] |
|**query** | **String** | [Required] SQL query text to execute. The useLegacySql field can be used to indicate whether the query uses legacy SQL or GoogleSQL. |  [optional] |
|**queryParameters** | [**List&lt;QueryParameter&gt;**](QueryParameter.md) | Query parameters for GoogleSQL queries. |  [optional] |
|**rangePartitioning** | [**RangePartitioning**](RangePartitioning.md) |  |  [optional] |
|**schemaUpdateOptions** | **List&lt;String&gt;** | Allows the schema of the destination table to be updated as a side effect of the query job. Schema update options are supported in two cases: when writeDisposition is WRITE_APPEND; when writeDisposition is WRITE_TRUNCATE and the destination table is a partition of a table, specified by partition decorators. For normal tables, WRITE_TRUNCATE will always overwrite the schema. One or more of the following values are specified: * ALLOW_FIELD_ADDITION: allow adding a nullable field to the schema. * ALLOW_FIELD_RELAXATION: allow relaxing a required field in the original schema to nullable. |  [optional] |
|**scriptOptions** | [**ScriptOptions**](ScriptOptions.md) |  |  [optional] |
|**systemVariables** | [**SystemVariables**](SystemVariables.md) |  |  [optional] |
|**tableDefinitions** | [**Map&lt;String, ExternalDataConfiguration&gt;**](ExternalDataConfiguration.md) | Optional. You can specify external table definitions, which operate as ephemeral tables that can be queried. These definitions are configured using a JSON map, where the string key represents the table identifier, and the value is the corresponding external data configuration object. |  [optional] |
|**timePartitioning** | [**TimePartitioning**](TimePartitioning.md) |  |  [optional] |
|**useLegacySql** | **Boolean** | Optional. Specifies whether to use BigQuery&#39;s legacy SQL dialect for this query. The default value is true. If set to false, the query will use BigQuery&#39;s GoogleSQL: https://cloud.google.com/bigquery/sql-reference/ When useLegacySql is set to false, the value of flattenResults is ignored; query will be run as if flattenResults is false. |  [optional] |
|**useQueryCache** | **Boolean** | Optional. Whether to look for the result in the query cache. The query cache is a best-effort cache that will be flushed whenever tables in the query are modified. Moreover, the query cache is only available when a query does not have a destination table specified. The default value is true. |  [optional] |
|**userDefinedFunctionResources** | [**List&lt;UserDefinedFunctionResource&gt;**](UserDefinedFunctionResource.md) | Describes user-defined function resources used in the query. |  [optional] |
|**writeDisposition** | **String** | Optional. Specifies the action that occurs if the destination table already exists. The following values are supported: * WRITE_TRUNCATE: If the table already exists, BigQuery overwrites the data, removes the constraints, and uses the schema from the query result. * WRITE_APPEND: If the table already exists, BigQuery appends the data to the table. * WRITE_EMPTY: If the table already exists and contains data, a &#39;duplicate&#39; error is returned in the job result. The default value is WRITE_EMPTY. Each action is atomic and only occurs if BigQuery is able to complete the job successfully. Creation, truncation and append actions occur as one atomic update upon job completion. |  [optional] |



