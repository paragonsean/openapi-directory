

# BulkUpdateTeamMembersResponse

Represents a response from a bulk update request containing the updated `TeamMember` objects or error messages.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errors** | [**List&lt;Error&gt;**](Error.md) | The errors that occurred during the request. |  [optional] |
|**teamMembers** | [**Map&lt;String, UpdateTeamMemberResponse&gt;**](UpdateTeamMemberResponse.md) | The successfully updated &#x60;TeamMember&#x60; objects. Each key is the &#x60;team_member_id&#x60; that maps to the &#x60;UpdateTeamMemberRequest&#x60;. |  [optional] |



