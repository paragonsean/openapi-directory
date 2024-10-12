

# WorkspaceCompilationOverrides

Configures workspace compilation overrides for a repository. Primarily used by the UI (`console.cloud.google.com`). `schema_suffix` and `table_prefix` can have a special expression - `${workspaceName}`, which refers to the workspace name from which the compilation results will be created. API callers are expected to resolve the expression in these overrides and provide them explicitly in `code_compilation_config` (https://cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults#codecompilationconfig) when creating workspace-scoped compilation results.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultDatabase** | **String** | Optional. The default database (Google Cloud project ID). |  [optional] |
|**schemaSuffix** | **String** | Optional. The suffix that should be appended to all schema (BigQuery dataset ID) names. |  [optional] |
|**tablePrefix** | **String** | Optional. The prefix that should be prepended to all table names. |  [optional] |



