# GitHubV3RestApi.Project

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **String** | Body of the project | 
**columnsUrl** | **String** |  | 
**createdAt** | **Date** |  | 
**creator** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**htmlUrl** | **String** |  | 
**id** | **Number** |  | 
**name** | **String** | Name of the project | 
**nodeId** | **String** |  | 
**number** | **Number** |  | 
**organizationPermission** | **String** | The baseline permission that all organization members have on this project. Only present if owner is an organization. | [optional] 
**ownerUrl** | **String** |  | 
**_private** | **Boolean** | Whether or not this project can be seen by everyone. Only present if owner is an organization. | [optional] 
**state** | **String** | State of the project; either &#39;open&#39; or &#39;closed&#39; | 
**updatedAt** | **Date** |  | 
**url** | **String** |  | 



## Enum: OrganizationPermissionEnum


* `read` (value: `"read"`)

* `write` (value: `"write"`)

* `admin` (value: `"admin"`)

* `none` (value: `"none"`)




