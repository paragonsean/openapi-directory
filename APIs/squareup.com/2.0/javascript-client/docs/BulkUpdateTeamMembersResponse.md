# SquareConnectApi.BulkUpdateTeamMembersResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**[Error]**](Error.md) | The errors that occurred during the request. | [optional] 
**teamMembers** | [**{String: UpdateTeamMemberResponse}**](UpdateTeamMemberResponse.md) | The successfully updated &#x60;TeamMember&#x60; objects. Each key is the &#x60;team_member_id&#x60; that maps to the &#x60;UpdateTeamMemberRequest&#x60;. | [optional] 


