

# GoogleCloudChannelV1alpha1Column

The definition of a report column. Specifies the data properties in the corresponding position of the report rows.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**columnId** | **String** | The unique name of the column (for example, customer_domain, channel_partner, customer_cost). You can use column IDs in RunReportJobRequest.filter. To see all reports and their columns, call CloudChannelReportsService.ListReports. |  [optional] |
|**dataType** | [**DataTypeEnum**](#DataTypeEnum) | The type of the values for this column. |  [optional] |
|**displayName** | **String** | The column&#39;s display name. |  [optional] |



## Enum: DataTypeEnum

| Name | Value |
|---- | -----|
| DATA_TYPE_UNSPECIFIED | &quot;DATA_TYPE_UNSPECIFIED&quot; |
| STRING | &quot;STRING&quot; |
| INT | &quot;INT&quot; |
| DECIMAL | &quot;DECIMAL&quot; |
| MONEY | &quot;MONEY&quot; |
| DATE | &quot;DATE&quot; |
| DATE_TIME | &quot;DATE_TIME&quot; |



