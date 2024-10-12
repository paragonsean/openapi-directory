

# CodeCompilationConfig

Configures various aspects of Dataform code compilation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assertionSchema** | **String** | Optional. The default schema (BigQuery dataset ID) for assertions. |  [optional] |
|**databaseSuffix** | **String** | Optional. The suffix that should be appended to all database (Google Cloud project ID) names. |  [optional] |
|**defaultDatabase** | **String** | Optional. The default database (Google Cloud project ID). |  [optional] |
|**defaultLocation** | **String** | Optional. The default BigQuery location to use. Defaults to \&quot;US\&quot;. See the BigQuery docs for a full list of locations: https://cloud.google.com/bigquery/docs/locations. |  [optional] |
|**defaultSchema** | **String** | Optional. The default schema (BigQuery dataset ID). |  [optional] |
|**schemaSuffix** | **String** | Optional. The suffix that should be appended to all schema (BigQuery dataset ID) names. |  [optional] |
|**tablePrefix** | **String** | Optional. The prefix that should be prepended to all table names. |  [optional] |
|**vars** | **Map&lt;String, String&gt;** | Optional. User-defined variables that are made available to project code during compilation. |  [optional] |



