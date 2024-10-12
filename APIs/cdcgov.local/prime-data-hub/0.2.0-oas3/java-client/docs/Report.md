

# Report


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destinationCount** | **Integer** | total destinations recieving the report(s) |  [optional] |
|**destinations** | [**List&lt;Destination&gt;**](Destination.md) | where the report is being sent to |  [optional] |
|**errorCount** | **Integer** | total errors found during initial validation.  There may be multiple errors per item. |  [optional] |
|**errors** | [**List&lt;Detail&gt;**](Detail.md) | a list of errors in the report |  [optional] |
|**id** | **String** | the id for the report assigned by the Hub |  |
|**reportItemCount** | **Integer** | total number of individual reports sent to the Hub (in a csv, the number of data lines sent) |  [optional] |
|**routing** | [**List&lt;ItemRouting&gt;**](ItemRouting.md) | The receiver destination names for each item in the report. This is displayed when verbose&#x3D;true is present on the query string. |  [optional] |
|**timestamp** | **String** | the timestamp for this report submission |  [optional] |
|**topic** | **String** | the topic configured for the client organization sender |  [optional] |
|**warningCount** | **Integer** | total warnings found during initial validation.  There may be multiple warnings per item. |  [optional] |
|**warnings** | [**List&lt;Detail&gt;**](Detail.md) | a list of warnings in the report |  [optional] |



