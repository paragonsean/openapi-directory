

# AppsGetTeams200ResponseInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | The description of the team |  [optional] |
|**displayName** | **String** | The display name of the team |  |
|**id** | **UUID** | The internal unique id (UUID) of the team. |  |
|**name** | **String** | The name of the team |  |
|**permissions** | [**List&lt;PermissionsEnum&gt;**](#List&lt;PermissionsEnum&gt;) | The permissions the team has for the app |  [optional] |



## Enum: List&lt;PermissionsEnum&gt;

| Name | Value |
|---- | -----|
| MANAGER | &quot;manager&quot; |
| DEVELOPER | &quot;developer&quot; |
| VIEWER | &quot;viewer&quot; |
| TESTER | &quot;tester&quot; |



