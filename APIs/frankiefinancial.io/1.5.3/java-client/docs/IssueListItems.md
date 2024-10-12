

# IssueListItems

A key/value pair of strings that describe the location of the issue (key) and an issue description (value). Also inclused is a severity 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**issueDescription** | **String** | Human readable description of the issue  |  [optional] |
|**issueLocation** | **String** | Where the issue occured. It will describe a location in the response structure  |  [optional] |
|**issueSeverity** | [**IssueSeverityEnum**](#IssueSeverityEnum) | The impact of the issue on the process.   Is it just informational, such as a trivial different in a name match? Is it a warning to highlight something that is important, but did not prevent the process from completing? Is it a critical issue that prevented the check from completing successfully? Is it a stop condition that prevented the checks from being run at all?  |  [optional] |



## Enum: IssueSeverityEnum

| Name | Value |
|---- | -----|
| INFO | &quot;INFO&quot; |
| WARN | &quot;WARN&quot; |
| CRIT | &quot;CRIT&quot; |
| STOP | &quot;STOP&quot; |



