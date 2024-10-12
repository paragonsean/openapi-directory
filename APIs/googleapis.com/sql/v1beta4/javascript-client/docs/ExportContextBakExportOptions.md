# CloudSqlAdminApi.ExportContextBakExportOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bakType** | **String** | Type of this bak file will be export, FULL or DIFF, SQL Server only | [optional] 
**copyOnly** | **Boolean** | Deprecated: copy_only is deprecated. Use differential_base instead | [optional] 
**differentialBase** | **Boolean** | Whether or not the backup can be used as a differential base copy_only backup can not be served as differential base | [optional] 
**stripeCount** | **Number** | Option for specifying how many stripes to use for the export. If blank, and the value of the striped field is true, the number of stripes is automatically chosen. | [optional] 
**striped** | **Boolean** | Whether or not the export should be striped. | [optional] 



## Enum: BakTypeEnum


* `BAK_TYPE_UNSPECIFIED` (value: `"BAK_TYPE_UNSPECIFIED"`)

* `FULL` (value: `"FULL"`)

* `DIFF` (value: `"DIFF"`)

* `TLOG` (value: `"TLOG"`)




