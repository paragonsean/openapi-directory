# FrankieFinancialApi.IssueListItems

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issueDescription** | **String** | Human readable description of the issue  | [optional] 
**issueLocation** | **String** | Where the issue occured. It will describe a location in the response structure  | [optional] 
**issueSeverity** | **String** | The impact of the issue on the process.   Is it just informational, such as a trivial different in a name match? Is it a warning to highlight something that is important, but did not prevent the process from completing? Is it a critical issue that prevented the check from completing successfully? Is it a stop condition that prevented the checks from being run at all?  | [optional] 



## Enum: IssueSeverityEnum


* `INFO` (value: `"INFO"`)

* `WARN` (value: `"WARN"`)

* `CRIT` (value: `"CRIT"`)

* `STOP` (value: `"STOP"`)




