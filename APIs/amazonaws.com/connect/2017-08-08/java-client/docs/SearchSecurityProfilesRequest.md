

# SearchSecurityProfilesRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**instanceId** | **String** | The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. |  |
|**nextToken** | **String** | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. |  [optional] |
|**maxResults** | **Integer** | The maximum number of results to return per page. |  [optional] |
|**searchCriteria** | [**SearchSecurityProfilesRequestSearchCriteria**](SearchSecurityProfilesRequestSearchCriteria.md) |  |  [optional] |
|**searchFilter** | [**SearchHoursOfOperationsRequestSearchFilter**](SearchHoursOfOperationsRequestSearchFilter.md) |  |  [optional] |



