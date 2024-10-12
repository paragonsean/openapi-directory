

# LoggingQuery

Describes a Cloud Logging query that can be run in Logs Explorer UI or via the logging API.In addition to the query itself, additional information may be stored to capture the display configuration and other UI state used in association with analysis of query results.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**filter** | **String** | Required. An advanced query using the Logging Query Language (https://cloud.google.com/logging/docs/view/logging-query-language). The maximum length of the filter is 20000 characters. |  [optional] |
|**summaryFieldEnd** | **Integer** | Characters will be counted from the end of the string. |  [optional] |
|**summaryFieldStart** | **Integer** | Characters will be counted from the start of the string. |  [optional] |
|**summaryFields** | [**List&lt;SummaryField&gt;**](SummaryField.md) | Optional. The set of summary fields to display for this saved query. |  [optional] |



