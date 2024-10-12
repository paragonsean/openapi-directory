

# QueryMetadata

Query metadata.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataRange** | [**DataRange**](DataRange.md) |  |  [optional] |
|**format** | [**FormatEnum**](#FormatEnum) | Format of the generated report. |  [optional] |
|**sendNotification** | **Boolean** | Whether to send an email notification when a report is ready. Defaults to false. |  [optional] |
|**shareEmailAddress** | **List&lt;String&gt;** | List of email addresses which are sent email notifications when the report is finished. Separate from send_notification. |  [optional] |
|**title** | **String** | Query title. It is used to name the reports generated from this query. |  [optional] |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| FORMAT_UNSPECIFIED | &quot;FORMAT_UNSPECIFIED&quot; |
| CSV | &quot;CSV&quot; |
| XLSX | &quot;XLSX&quot; |



