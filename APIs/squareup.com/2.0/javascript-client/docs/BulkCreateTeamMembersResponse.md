# SquareConnectApi.BulkCreateTeamMembersResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**[Error]**](Error.md) | The errors that occurred during the request. | [optional] 
**teamMembers** | [**{String: CreateTeamMemberResponse}**](CreateTeamMemberResponse.md) | The successfully created &#x60;TeamMember&#x60; objects. Each key is the &#x60;idempotency_key&#x60; that maps to the &#x60;CreateTeamMemberRequest&#x60;. | [optional] 


