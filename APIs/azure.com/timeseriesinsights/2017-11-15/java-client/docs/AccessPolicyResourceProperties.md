

# AccessPolicyResourceProperties


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | An description of the access policy. |  [optional] |
|**principalObjectId** | **String** | The objectId of the principal in Azure Active Directory. |  [optional] |
|**roles** | [**List&lt;RolesEnum&gt;**](#List&lt;RolesEnum&gt;) | The list of roles the principal is assigned on the environment. |  [optional] |



## Enum: List&lt;RolesEnum&gt;

| Name | Value |
|---- | -----|
| READER | &quot;Reader&quot; |
| CONTRIBUTOR | &quot;Contributor&quot; |



