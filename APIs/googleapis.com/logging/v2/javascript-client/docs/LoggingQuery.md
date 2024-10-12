# CloudLoggingApi.LoggingQuery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **String** | Required. An advanced query using the Logging Query Language (https://cloud.google.com/logging/docs/view/logging-query-language). The maximum length of the filter is 20000 characters. | [optional] 
**summaryFieldEnd** | **Number** | Characters will be counted from the end of the string. | [optional] 
**summaryFieldStart** | **Number** | Characters will be counted from the start of the string. | [optional] 
**summaryFields** | [**[SummaryField]**](SummaryField.md) | Optional. The set of summary fields to display for this saved query. | [optional] 


