# CloudChannelApi.GoogleCloudChannelV1Column

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columnId** | **String** | The unique name of the column (for example, customer_domain, channel_partner, customer_cost). You can use column IDs in RunReportJobRequest.filter. To see all reports and their columns, call CloudChannelReportsService.ListReports. | [optional] 
**dataType** | **String** | The type of the values for this column. | [optional] 
**displayName** | **String** | The column&#39;s display name. | [optional] 



## Enum: DataTypeEnum


* `DATA_TYPE_UNSPECIFIED` (value: `"DATA_TYPE_UNSPECIFIED"`)

* `STRING` (value: `"STRING"`)

* `INT` (value: `"INT"`)

* `DECIMAL` (value: `"DECIMAL"`)

* `MONEY` (value: `"MONEY"`)

* `DATE` (value: `"DATE"`)

* `DATE_TIME` (value: `"DATE_TIME"`)




