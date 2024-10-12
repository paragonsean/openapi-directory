

# Note

A proposal may be associated to several notes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The timestamp for when this note was created. |  [optional] [readonly] |
|**creatorRole** | [**CreatorRoleEnum**](#CreatorRoleEnum) | Output only. The role of the person (buyer/seller) creating the note. |  [optional] [readonly] |
|**note** | **String** | The actual note to attach. (max-length: 1024 unicode code units) Note: This field may be set only when creating the resource. Modifying this field while updating the resource will result in an error. |  [optional] |
|**noteId** | **String** | Output only. The unique ID for the note. |  [optional] [readonly] |
|**proposalRevision** | **String** | Output only. The revision number of the proposal when the note is created. |  [optional] [readonly] |



## Enum: CreatorRoleEnum

| Name | Value |
|---- | -----|
| BUYER_SELLER_ROLE_UNSPECIFIED | &quot;BUYER_SELLER_ROLE_UNSPECIFIED&quot; |
| BUYER | &quot;BUYER&quot; |
| SELLER | &quot;SELLER&quot; |



