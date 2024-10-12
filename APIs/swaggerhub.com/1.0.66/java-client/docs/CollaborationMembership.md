

# CollaborationMembership


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blocked** | **Boolean** |  |  [optional] [readonly] |
|**name** | **String** | The name of a user or team |  |
|**startTime** | **OffsetDateTime** | The date and time this user or team was added as a collaborator |  [optional] [readonly] |
|**uuid** | **String** | Internal ID of a user or team |  [optional] [readonly] |
|**donotdisturb** | **Boolean** |  |  [optional] [readonly] |
|**roles** | [**List&lt;RolesEnum&gt;**](#List&lt;RolesEnum&gt;) | A list of this collaborator&#39;s roles |  |



## Enum: List&lt;RolesEnum&gt;

| Name | Value |
|---- | -----|
| EDIT | &quot;EDIT&quot; |
| COMMENT | &quot;COMMENT&quot; |
| VIEW | &quot;VIEW&quot; |



