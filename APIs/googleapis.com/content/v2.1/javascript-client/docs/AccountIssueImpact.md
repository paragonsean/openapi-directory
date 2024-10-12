# ContentApiForShopping.AccountIssueImpact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breakdowns** | [**[Breakdown]**](Breakdown.md) | Detailed impact breakdown. Explains the types of restriction the issue has in different shopping destinations and territory. If present, it should be rendered to the merchant. Can be shown as a mouse over dropdown or a dialog. Each breakdown item represents a group of regions with the same impact details. | [optional] 
**message** | **String** | Optional. Message summarizing the overall impact of the issue. If present, it should be rendered to the merchant. For example: \&quot;Disapproves 90k offers in 25 countries\&quot; | [optional] 
**severity** | **String** | The severity of the issue. | [optional] 



## Enum: SeverityEnum


* `SEVERITY_UNSPECIFIED` (value: `"SEVERITY_UNSPECIFIED"`)

* `ERROR` (value: `"ERROR"`)

* `WARNING` (value: `"WARNING"`)

* `INFO` (value: `"INFO"`)




