

# Spreadsheet

Resource that represents a spreadsheet.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSourceSchedules** | [**List&lt;DataSourceRefreshSchedule&gt;**](DataSourceRefreshSchedule.md) | Output only. A list of data source refresh schedules. |  [optional] [readonly] |
|**dataSources** | [**List&lt;DataSource&gt;**](DataSource.md) | A list of external data sources connected with the spreadsheet. |  [optional] |
|**developerMetadata** | [**List&lt;DeveloperMetadata&gt;**](DeveloperMetadata.md) | The developer metadata associated with a spreadsheet. |  [optional] |
|**namedRanges** | [**List&lt;NamedRange&gt;**](NamedRange.md) | The named ranges defined in a spreadsheet. |  [optional] |
|**properties** | [**SpreadsheetProperties**](SpreadsheetProperties.md) |  |  [optional] |
|**sheets** | [**List&lt;Sheet&gt;**](Sheet.md) | The sheets that are part of a spreadsheet. |  [optional] |
|**spreadsheetId** | **String** | The ID of the spreadsheet. This field is read-only. |  [optional] |
|**spreadsheetUrl** | **String** | The url of the spreadsheet. This field is read-only. |  [optional] |



