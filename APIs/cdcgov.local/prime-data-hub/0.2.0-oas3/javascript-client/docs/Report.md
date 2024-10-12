# PrimeReportStream.Report

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destinationCount** | **Number** | total destinations recieving the report(s) | [optional] 
**destinations** | [**[Destination]**](Destination.md) | where the report is being sent to | [optional] 
**errorCount** | **Number** | total errors found during initial validation.  There may be multiple errors per item. | [optional] 
**errors** | [**[Detail]**](Detail.md) | a list of errors in the report | [optional] 
**id** | **String** | the id for the report assigned by the Hub | 
**reportItemCount** | **Number** | total number of individual reports sent to the Hub (in a csv, the number of data lines sent) | [optional] 
**routing** | [**[ItemRouting]**](ItemRouting.md) | The receiver destination names for each item in the report. This is displayed when verbose&#x3D;true is present on the query string. | [optional] 
**timestamp** | **String** | the timestamp for this report submission | [optional] 
**topic** | **String** | the topic configured for the client organization sender | [optional] 
**warningCount** | **Number** | total warnings found during initial validation.  There may be multiple warnings per item. | [optional] 
**warnings** | [**[Detail]**](Detail.md) | a list of warnings in the report | [optional] 


