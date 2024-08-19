

# BulkCreateTeamMembersResponse

Represents a response from a bulk create request containing the created `TeamMember` objects or error messages.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errors** | [**List&lt;Error&gt;**](Error.md) | The errors that occurred during the request. |  [optional] |
|**teamMembers** | [**Map&lt;String, CreateTeamMemberResponse&gt;**](CreateTeamMemberResponse.md) | The successfully created &#x60;TeamMember&#x60; objects. Each key is the &#x60;idempotency_key&#x60; that maps to the &#x60;CreateTeamMemberRequest&#x60;. |  [optional] |



