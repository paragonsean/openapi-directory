

# ListCoverageStatisticsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**filterCriteria** | [**ListCoverageRequestFilterCriteria**](ListCoverageRequestFilterCriteria.md) |  |  [optional] |
|**groupBy** | [**GroupByEnum**](#GroupByEnum) | The value to group the results by. |  [optional] |
|**nextToken** | **String** | A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the &lt;code&gt;NextToken&lt;/code&gt; value returned from the previous request to continue listing results after the first page. |  [optional] |



## Enum: GroupByEnum

| Name | Value |
|---- | -----|
| SCAN_STATUS_CODE | &quot;SCAN_STATUS_CODE&quot; |
| SCAN_STATUS_REASON | &quot;SCAN_STATUS_REASON&quot; |
| ACCOUNT_ID | &quot;ACCOUNT_ID&quot; |
| RESOURCE_TYPE | &quot;RESOURCE_TYPE&quot; |
| ECR_REPOSITORY_NAME | &quot;ECR_REPOSITORY_NAME&quot; |



