# GoogleKeepApi.Permission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted** | **Boolean** | Output only. Whether this member has been deleted. If the member is recovered, this value is set to false and the recovered member retains the role on the note. | [optional] [readonly] 
**email** | **String** | The email associated with the member. If set on create, the &#x60;email&#x60; field in the &#x60;User&#x60; or &#x60;Group&#x60; message must either be empty or match this field. On read, may be unset if the member does not have an associated email. | [optional] 
**family** | **Object** | Describes a single Google Family. | [optional] 
**group** | [**Group**](Group.md) |  | [optional] 
**name** | **String** | Output only. The resource name. | [optional] [readonly] 
**role** | **String** | The role granted by this permission. The role determines the entity’s ability to read, write, and share notes. | [optional] 
**user** | [**User**](User.md) |  | [optional] 



## Enum: RoleEnum


* `ROLE_UNSPECIFIED` (value: `"ROLE_UNSPECIFIED"`)

* `OWNER` (value: `"OWNER"`)

* `WRITER` (value: `"WRITER"`)




