

# TeamFull

Groups of organization members that gives permissions on specified repositories.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** |  |  |
|**description** | **String** |  |  |
|**htmlUrl** | **URI** |  |  |
|**id** | **Integer** | Unique identifier of the team |  |
|**ldapDn** | **String** | Distinguished Name (DN) that team maps to within LDAP environment |  [optional] |
|**membersCount** | **Integer** |  |  |
|**membersUrl** | **String** |  |  |
|**name** | **String** | Name of the team |  |
|**nodeId** | **String** |  |  |
|**organization** | [**TeamOrganization**](TeamOrganization.md) |  |  |
|**parent** | [**NullableTeamSimple**](NullableTeamSimple.md) |  |  [optional] |
|**permission** | **String** | Permission that the team will have for its repositories |  |
|**privacy** | [**PrivacyEnum**](#PrivacyEnum) | The level of privacy this team should have |  [optional] |
|**reposCount** | **Integer** |  |  |
|**repositoriesUrl** | **URI** |  |  |
|**slug** | **String** |  |  |
|**updatedAt** | **OffsetDateTime** |  |  |
|**url** | **URI** | URL for the team |  |



## Enum: PrivacyEnum

| Name | Value |
|---- | -----|
| CLOSED | &quot;closed&quot; |
| SECRET | &quot;secret&quot; |



