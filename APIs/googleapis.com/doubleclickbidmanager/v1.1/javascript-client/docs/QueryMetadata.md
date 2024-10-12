# DoubleClickBidManagerApi.QueryMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataRange** | **String** | Range of report data. | [optional] 
**format** | **String** | Format of the generated report. | [optional] 
**googleCloudStoragePathForLatestReport** | **String** | The path to the location in Google Cloud Storage where the latest report is stored. | [optional] 
**googleDrivePathForLatestReport** | **String** | The path in Google Drive for the latest report. | [optional] 
**latestReportRunTimeMs** | **String** | The time when the latest report started to run. | [optional] 
**locale** | **String** | Locale of the generated reports. Valid values are cs CZECH de GERMAN en ENGLISH es SPANISH fr FRENCH it ITALIAN ja JAPANESE ko KOREAN pl POLISH pt-BR BRAZILIAN_PORTUGUESE ru RUSSIAN tr TURKISH uk UKRAINIAN zh-CN CHINA_CHINESE zh-TW TAIWAN_CHINESE An locale string not in the list above will generate reports in English. | [optional] 
**reportCount** | **Number** | Number of reports that have been generated for the query. | [optional] 
**running** | **Boolean** | Whether the latest report is currently running. | [optional] 
**sendNotification** | **Boolean** | Whether to send an email notification when a report is ready. Default to false. | [optional] 
**shareEmailAddress** | **[String]** | List of email addresses which are sent email notifications when the report is finished. Separate from sendNotification. | [optional] 
**title** | **String** | Query title. It is used to name the reports generated from this query. | [optional] 



## Enum: DataRangeEnum


* `CUSTOM_DATES` (value: `"CUSTOM_DATES"`)

* `CURRENT_DAY` (value: `"CURRENT_DAY"`)

* `PREVIOUS_DAY` (value: `"PREVIOUS_DAY"`)

* `WEEK_TO_DATE` (value: `"WEEK_TO_DATE"`)

* `MONTH_TO_DATE` (value: `"MONTH_TO_DATE"`)

* `QUARTER_TO_DATE` (value: `"QUARTER_TO_DATE"`)

* `YEAR_TO_DATE` (value: `"YEAR_TO_DATE"`)

* `PREVIOUS_WEEK` (value: `"PREVIOUS_WEEK"`)

* `PREVIOUS_HALF_MONTH` (value: `"PREVIOUS_HALF_MONTH"`)

* `PREVIOUS_MONTH` (value: `"PREVIOUS_MONTH"`)

* `PREVIOUS_QUARTER` (value: `"PREVIOUS_QUARTER"`)

* `PREVIOUS_YEAR` (value: `"PREVIOUS_YEAR"`)

* `LAST_7_DAYS` (value: `"LAST_7_DAYS"`)

* `LAST_30_DAYS` (value: `"LAST_30_DAYS"`)

* `LAST_90_DAYS` (value: `"LAST_90_DAYS"`)

* `LAST_365_DAYS` (value: `"LAST_365_DAYS"`)

* `ALL_TIME` (value: `"ALL_TIME"`)

* `LAST_14_DAYS` (value: `"LAST_14_DAYS"`)

* `TYPE_NOT_SUPPORTED` (value: `"TYPE_NOT_SUPPORTED"`)

* `LAST_60_DAYS` (value: `"LAST_60_DAYS"`)





## Enum: FormatEnum


* `CSV` (value: `"CSV"`)

* `EXCEL_CSV` (value: `"EXCEL_CSV"`)

* `XLSX` (value: `"XLSX"`)




