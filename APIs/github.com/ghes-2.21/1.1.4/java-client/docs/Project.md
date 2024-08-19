

# Project

Projects are a way to organize columns and cards of work.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**body** | **String** | Body of the project |  |
|**columnsUrl** | **URI** |  |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**creator** | [**NullableSimpleUser**](NullableSimpleUser.md) |  |  |
|**htmlUrl** | **URI** |  |  |
|**id** | **Integer** |  |  |
|**name** | **String** | Name of the project |  |
|**nodeId** | **String** |  |  |
|**number** | **Integer** |  |  |
|**organizationPermission** | [**OrganizationPermissionEnum**](#OrganizationPermissionEnum) | The baseline permission that all organization members have on this project. Only present if owner is an organization. |  [optional] |
|**ownerUrl** | **URI** |  |  |
|**_private** | **Boolean** | Whether or not this project can be seen by everyone. Only present if owner is an organization. |  [optional] |
|**state** | **String** | State of the project; either &#39;open&#39; or &#39;closed&#39; |  |
|**updatedAt** | **OffsetDateTime** |  |  |
|**url** | **URI** |  |  |



## Enum: OrganizationPermissionEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |
| ADMIN | &quot;admin&quot; |
| NONE | &quot;none&quot; |



