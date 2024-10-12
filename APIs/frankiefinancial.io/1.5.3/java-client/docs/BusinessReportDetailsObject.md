

# BusinessReportDetailsObject

The metadata details of the report generated . 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**reportDateTime** | **OffsetDateTime** | The ISO UTC date and time the report was generated  |  [optional] |
|**reportId** | **String** | If the report provider generated an ID or recipt number for the report, it goes here |  [optional] |
|**reportName** | **String** | The name of the requested report |  [optional] |
|**reportProvider** | **String** | The name of the service provider that generated the report.  |  [optional] |
|**reportRun** | **Boolean** | Whether the report was successfully run or not  |  [optional] |
|**reportStatus** | **String** | Any details of what is happening with the report of not run.  Will be one of:   - OK  (the report was run)   - LATER  (the report will be sent later as a response notification)   - An error message as to why the report did not work  |  [optional] |



