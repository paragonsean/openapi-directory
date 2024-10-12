

# ExportContextSqlExportOptionsMysqlExportOptions

Options for exporting from MySQL.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**masterData** | **Integer** | Option to include SQL statement required to set up replication. If set to &#x60;1&#x60;, the dump file includes a CHANGE MASTER TO statement with the binary log coordinates, and --set-gtid-purged is set to ON. If set to &#x60;2&#x60;, the CHANGE MASTER TO statement is written as a SQL comment and has no effect. If set to any value other than &#x60;1&#x60;, --set-gtid-purged is set to OFF. |  [optional] |



