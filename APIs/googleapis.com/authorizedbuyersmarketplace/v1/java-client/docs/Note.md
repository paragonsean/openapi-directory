

# Note

A text note attached to the proposal to facilitate the communication between buyers and sellers.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. When this note was created. |  [optional] [readonly] |
|**creatorRole** | [**CreatorRoleEnum**](#CreatorRoleEnum) | Output only. The role who created the note. |  [optional] [readonly] |
|**note** | **String** | The text of the note. Maximum length is 1024 characters. |  [optional] |



## Enum: CreatorRoleEnum

| Name | Value |
|---- | -----|
| BUYER_SELLER_ROLE_UNSPECIFIED | &quot;BUYER_SELLER_ROLE_UNSPECIFIED&quot; |
| BUYER | &quot;BUYER&quot; |
| SELLER | &quot;SELLER&quot; |



