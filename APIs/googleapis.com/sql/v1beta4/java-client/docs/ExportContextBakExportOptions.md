

# ExportContextBakExportOptions

Options for exporting BAK files (SQL Server-only)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bakType** | [**BakTypeEnum**](#BakTypeEnum) | Type of this bak file will be export, FULL or DIFF, SQL Server only |  [optional] |
|**copyOnly** | **Boolean** | Deprecated: copy_only is deprecated. Use differential_base instead |  [optional] |
|**differentialBase** | **Boolean** | Whether or not the backup can be used as a differential base copy_only backup can not be served as differential base |  [optional] |
|**stripeCount** | **Integer** | Option for specifying how many stripes to use for the export. If blank, and the value of the striped field is true, the number of stripes is automatically chosen. |  [optional] |
|**striped** | **Boolean** | Whether or not the export should be striped. |  [optional] |



## Enum: BakTypeEnum

| Name | Value |
|---- | -----|
| BAK_TYPE_UNSPECIFIED | &quot;BAK_TYPE_UNSPECIFIED&quot; |
| FULL | &quot;FULL&quot; |
| DIFF | &quot;DIFF&quot; |
| TLOG | &quot;TLOG&quot; |



