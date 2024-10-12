

# ListTeamMemberWagesRequest

A request for a set of `TeamMemberWage` objects.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cursor** | **String** | A pointer to the next page of &#x60;EmployeeWage&#x60; results to fetch. |  [optional] |
|**limit** | **Integer** | The maximum number of &#x60;TeamMemberWage&#x60; results to return per page. The number can range between 1 and 200. The default is 200. |  [optional] |
|**teamMemberId** | **String** | Filter the returned wages to only those that are associated with the specified team member. |  [optional] |



