# SwaggerHubRegistryApi.CollaborationTeamMembership

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blocked** | **Boolean** |  | [optional] [readonly] 
**name** | **String** | The name of a user or team | 
**startTime** | **Date** | The date and time this user or team was added as a collaborator | [optional] [readonly] 
**uuid** | **String** | Internal ID of a user or team | [optional] [readonly] 
**donotdisturb** | **Boolean** |  | [optional] [readonly] 
**roles** | **[String]** | A list of this collaborator&#39;s roles | 
**invited** | [**[CollaborationMember]**](CollaborationMember.md) | Reserved for future use. Currently, this field is always an empty array. | [optional] [readonly] 
**members** | [**[CollaborationMember]**](CollaborationMember.md) | A list of team members | [optional] [readonly] 



## Enum: [RolesEnum]


* `EDIT` (value: `"EDIT"`)

* `COMMENT` (value: `"COMMENT"`)

* `VIEW` (value: `"VIEW"`)




