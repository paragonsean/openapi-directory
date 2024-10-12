

# ListTeamMemberWagesResponse

The response to a request for a set of `TeamMemberWage` objects. The response contains a set of `TeamMemberWage` objects.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cursor** | **String** | The value supplied in the subsequent request to fetch the next page of &#x60;TeamMemberWage&#x60; results. |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | Any errors that occurred during the request. |  [optional] |
|**teamMemberWages** | [**List&lt;TeamMemberWage&gt;**](TeamMemberWage.md) | A page of &#x60;TeamMemberWage&#x60; results. |  [optional] |



