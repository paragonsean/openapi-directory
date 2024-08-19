# GitHubV3RestApi.TeamFull

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** |  | 
**description** | **String** |  | 
**htmlUrl** | **String** |  | 
**id** | **Number** | Unique identifier of the team | 
**ldapDn** | **String** | Distinguished Name (DN) that team maps to within LDAP environment | [optional] 
**membersCount** | **Number** |  | 
**membersUrl** | **String** |  | 
**name** | **String** | Name of the team | 
**nodeId** | **String** |  | 
**organization** | [**TeamOrganization**](TeamOrganization.md) |  | 
**parent** | [**NullableTeamSimple**](NullableTeamSimple.md) |  | [optional] 
**permission** | **String** | Permission that the team will have for its repositories | 
**privacy** | **String** | The level of privacy this team should have | [optional] 
**reposCount** | **Number** |  | 
**repositoriesUrl** | **String** |  | 
**slug** | **String** |  | 
**updatedAt** | **Date** |  | 
**url** | **String** | URL for the team | 



## Enum: PrivacyEnum


* `closed` (value: `"closed"`)

* `secret` (value: `"secret"`)




