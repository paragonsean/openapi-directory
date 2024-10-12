

# QueryMetadata

Query metadata.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataRange** | [**DataRangeEnum**](#DataRangeEnum) | Range of report data. |  [optional] |
|**format** | [**FormatEnum**](#FormatEnum) | Format of the generated report. |  [optional] |
|**googleCloudStoragePathForLatestReport** | **String** | The path to the location in Google Cloud Storage where the latest report is stored. |  [optional] |
|**googleDrivePathForLatestReport** | **String** | The path in Google Drive for the latest report. |  [optional] |
|**latestReportRunTimeMs** | **String** | The time when the latest report started to run. |  [optional] |
|**locale** | **String** | Locale of the generated reports. Valid values are cs CZECH de GERMAN en ENGLISH es SPANISH fr FRENCH it ITALIAN ja JAPANESE ko KOREAN pl POLISH pt-BR BRAZILIAN_PORTUGUESE ru RUSSIAN tr TURKISH uk UKRAINIAN zh-CN CHINA_CHINESE zh-TW TAIWAN_CHINESE An locale string not in the list above will generate reports in English. |  [optional] |
|**reportCount** | **Integer** | Number of reports that have been generated for the query. |  [optional] |
|**running** | **Boolean** | Whether the latest report is currently running. |  [optional] |
|**sendNotification** | **Boolean** | Whether to send an email notification when a report is ready. Default to false. |  [optional] |
|**shareEmailAddress** | **List&lt;String&gt;** | List of email addresses which are sent email notifications when the report is finished. Separate from sendNotification. |  [optional] |
|**title** | **String** | Query title. It is used to name the reports generated from this query. |  [optional] |



## Enum: DataRangeEnum

| Name | Value |
|---- | -----|
| CUSTOM_DATES | &quot;CUSTOM_DATES&quot; |
| CURRENT_DAY | &quot;CURRENT_DAY&quot; |
| PREVIOUS_DAY | &quot;PREVIOUS_DAY&quot; |
| WEEK_TO_DATE | &quot;WEEK_TO_DATE&quot; |
| MONTH_TO_DATE | &quot;MONTH_TO_DATE&quot; |
| QUARTER_TO_DATE | &quot;QUARTER_TO_DATE&quot; |
| YEAR_TO_DATE | &quot;YEAR_TO_DATE&quot; |
| PREVIOUS_WEEK | &quot;PREVIOUS_WEEK&quot; |
| PREVIOUS_HALF_MONTH | &quot;PREVIOUS_HALF_MONTH&quot; |
| PREVIOUS_MONTH | &quot;PREVIOUS_MONTH&quot; |
| PREVIOUS_QUARTER | &quot;PREVIOUS_QUARTER&quot; |
| PREVIOUS_YEAR | &quot;PREVIOUS_YEAR&quot; |
| LAST_7_DAYS | &quot;LAST_7_DAYS&quot; |
| LAST_30_DAYS | &quot;LAST_30_DAYS&quot; |
| LAST_90_DAYS | &quot;LAST_90_DAYS&quot; |
| LAST_365_DAYS | &quot;LAST_365_DAYS&quot; |
| ALL_TIME | &quot;ALL_TIME&quot; |
| LAST_14_DAYS | &quot;LAST_14_DAYS&quot; |
| TYPE_NOT_SUPPORTED | &quot;TYPE_NOT_SUPPORTED&quot; |
| LAST_60_DAYS | &quot;LAST_60_DAYS&quot; |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| CSV | &quot;CSV&quot; |
| EXCEL_CSV | &quot;EXCEL_CSV&quot; |
| XLSX | &quot;XLSX&quot; |



