# SwaggerHubRegistryApi.Collaboration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | [**[CollaborationMembership]**](CollaborationMembership.md) | A list of users who are existing collaborators on this API | [optional] 
**owner** | **String** | Internal ID of the API owner (organization or user) | [optional] [readonly] 
**ownerName** | **String** | The name of the API owner (organization or user) | [optional] [readonly] 
**owners** | [**[OrganizationOwner]**](OrganizationOwner.md) | If the API owner is an organization, this list contains the IDs of the organization owners. If the API owner is a user, an empty array is returned.  | [optional] [readonly] 
**pendingMembers** | [**[CollaborationMembership]**](CollaborationMembership.md) | A list of pending collaborators - users who were invited to collaborate on this API but have not accepted the invitation yet | [optional] 
**teams** | [**[CollaborationTeamMembership]**](CollaborationTeamMembership.md) | A list of teams that collaborate on this API | [optional] 


