

# PrestoJob

A Dataproc job for running Presto (https://prestosql.io/) queries. IMPORTANT: The Dataproc Presto Optional Component (https://cloud.google.com/dataproc/docs/concepts/components/presto) must be enabled when the cluster is created to submit a Presto job to the cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientTags** | **List&lt;String&gt;** | Optional. Presto client tags to attach to this query |  [optional] |
|**continueOnFailure** | **Boolean** | Optional. Whether to continue executing queries if a query fails. The default value is false. Setting to true can be useful when executing independent parallel queries. |  [optional] |
|**loggingConfig** | [**LoggingConfig**](LoggingConfig.md) |  |  [optional] |
|**outputFormat** | **String** | Optional. The format in which query output will be displayed. See the Presto documentation for supported output formats |  [optional] |
|**properties** | **Map&lt;String, String&gt;** | Optional. A mapping of property names to values. Used to set Presto session properties (https://prestodb.io/docs/current/sql/set-session.html) Equivalent to using the --session flag in the Presto CLI |  [optional] |
|**queryFileUri** | **String** | The HCFS URI of the script that contains SQL queries. |  [optional] |
|**queryList** | [**QueryList**](QueryList.md) |  |  [optional] |



