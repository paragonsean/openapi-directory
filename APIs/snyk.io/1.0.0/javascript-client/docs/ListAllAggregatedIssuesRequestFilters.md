# SnykApi.ListAllAggregatedIssuesRequestFilters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exploitMaturity** | **[Object]** | The exploit maturity levels of issues to filter the results by (Non-IaC projects only) | [optional] 
**ignored** | **Boolean** | If set to &#x60;true&#x60;, only include issues which are ignored, if set to &#x60;false&#x60;, only include issues which are not ignored | [optional] 
**patched** | **Boolean** | If set to &#x60;true&#x60;, only include issues which are patched, if set to &#x60;false&#x60;, only include issues which are not patched (Non-IaC projects only) | [optional] 
**priority** | [**ListAllAggregatedIssuesRequestFiltersPriority**](ListAllAggregatedIssuesRequestFiltersPriority.md) |  | [optional] 
**severities** | **[Object]** | The severity levels of issues to filter the results by | [optional] 
**types** | **[Object]** | The type of issues to filter the results by (Non-IaC projects only) | [optional] 


