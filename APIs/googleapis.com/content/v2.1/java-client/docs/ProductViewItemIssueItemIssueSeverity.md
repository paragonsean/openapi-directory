

# ProductViewItemIssueItemIssueSeverity

Severity of an issue per destination in a region, and aggregated severity.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregatedSeverity** | [**AggregatedSeverityEnum**](#AggregatedSeverityEnum) | Severity of an issue aggregated for destination. |  [optional] |
|**severityPerDestination** | [**List&lt;ProductViewItemIssueIssueSeverityPerDestination&gt;**](ProductViewItemIssueIssueSeverityPerDestination.md) | Item issue severity for every destination. |  [optional] |



## Enum: AggregatedSeverityEnum

| Name | Value |
|---- | -----|
| AGGREGATED_ISSUE_SEVERITY_UNSPECIFIED | &quot;AGGREGATED_ISSUE_SEVERITY_UNSPECIFIED&quot; |
| DISAPPROVED | &quot;DISAPPROVED&quot; |
| DEMOTED | &quot;DEMOTED&quot; |
| PENDING | &quot;PENDING&quot; |



