

# PagedDeployedApplicationInfoList

The list of deployed applications in activating, downloading, or active states on a node. The list is paged when all of the results cannot fit in a single message. The next set of results can be obtained by executing the same query with the continuation token provided in this list.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**continuationToken** | **String** | The continuation token parameter is used to obtain next set of results. The continuation token is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token is not included in the response. |  [optional] |
|**items** | [**List&lt;DeployedApplicationInfo&gt;**](DeployedApplicationInfo.md) | List of deployed application information. |  [optional] |



