

# ExportContextSqlExportOptions

Options for exporting data as SQL statements.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mysqlExportOptions** | [**ExportContextSqlExportOptionsMysqlExportOptions**](ExportContextSqlExportOptionsMysqlExportOptions.md) |  |  [optional] |
|**parallel** | **Boolean** | Optional. Whether or not the export should be parallel. |  [optional] |
|**schemaOnly** | **Boolean** | Export only schemas. |  [optional] |
|**tables** | **List&lt;String&gt;** | Tables to export, or that were exported, from the specified database. If you specify tables, specify one and only one database. For PostgreSQL instances, you can specify only one table. |  [optional] |
|**threads** | **Integer** | Optional. The number of threads to use for parallel export. |  [optional] |



