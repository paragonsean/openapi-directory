# Inspector2.ListCoverageStatisticsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filterCriteria** | [**ListCoverageRequestFilterCriteria**](ListCoverageRequestFilterCriteria.md) |  | [optional] 
**groupBy** | **String** | The value to group the results by. | [optional] 
**nextToken** | **String** | A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the &lt;code&gt;NextToken&lt;/code&gt; value returned from the previous request to continue listing results after the first page. | [optional] 



## Enum: GroupByEnum


* `SCAN_STATUS_CODE` (value: `"SCAN_STATUS_CODE"`)

* `SCAN_STATUS_REASON` (value: `"SCAN_STATUS_REASON"`)

* `ACCOUNT_ID` (value: `"ACCOUNT_ID"`)

* `RESOURCE_TYPE` (value: `"RESOURCE_TYPE"`)

* `ECR_REPOSITORY_NAME` (value: `"ECR_REPOSITORY_NAME"`)




