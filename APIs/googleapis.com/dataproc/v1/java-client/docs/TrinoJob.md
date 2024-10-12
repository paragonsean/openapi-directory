

# TrinoJob

A Dataproc job for running Trino (https://trino.io/) queries. IMPORTANT: The Dataproc Trino Optional Component (https://cloud.google.com/dataproc/docs/concepts/components/trino) must be enabled when the cluster is created to submit a Trino job to the cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientTags** | **List&lt;String&gt;** | Optional. Trino client tags to attach to this query |  [optional] |
|**continueOnFailure** | **Boolean** | Optional. Whether to continue executing queries if a query fails. The default value is false. Setting to true can be useful when executing independent parallel queries. |  [optional] |
|**loggingConfig** | [**LoggingConfig**](LoggingConfig.md) |  |  [optional] |
|**outputFormat** | **String** | Optional. The format in which query output will be displayed. See the Trino documentation for supported output formats |  [optional] |
|**properties** | **Map&lt;String, String&gt;** | Optional. A mapping of property names to values. Used to set Trino session properties (https://trino.io/docs/current/sql/set-session.html) Equivalent to using the --session flag in the Trino CLI |  [optional] |
|**queryFileUri** | **String** | The HCFS URI of the script that contains SQL queries. |  [optional] |
|**queryList** | [**QueryList**](QueryList.md) |  |  [optional] |



