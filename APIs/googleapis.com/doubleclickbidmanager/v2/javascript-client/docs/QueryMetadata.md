# DoubleClickBidManagerApi.QueryMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataRange** | [**DataRange**](DataRange.md) |  | [optional] 
**format** | **String** | Format of the generated report. | [optional] 
**sendNotification** | **Boolean** | Whether to send an email notification when a report is ready. Defaults to false. | [optional] 
**shareEmailAddress** | **[String]** | List of email addresses which are sent email notifications when the report is finished. Separate from send_notification. | [optional] 
**title** | **String** | Query title. It is used to name the reports generated from this query. | [optional] 



## Enum: FormatEnum


* `FORMAT_UNSPECIFIED` (value: `"FORMAT_UNSPECIFIED"`)

* `CSV` (value: `"CSV"`)

* `XLSX` (value: `"XLSX"`)




