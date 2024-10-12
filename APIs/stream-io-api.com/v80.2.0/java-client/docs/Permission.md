

# Permission


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | **String** | Action name this permission is for (e.g. SendMessage) |  |
|**condition** | **Map&lt;String, Object&gt;** | MongoDB style condition which decides whether or not the permission is granted |  [optional] |
|**custom** | **Boolean** | Whether this is a custom permission or built-in |  |
|**description** | **String** | Description of the permission |  |
|**id** | **String** | Unique permission ID |  |
|**level** | [**LevelEnum**](#LevelEnum) | Level at which permission could be applied (app or channel) |  |
|**name** | **String** | Name of the permission |  |
|**owner** | **Boolean** | Whether this permission applies to resource owner or not |  |
|**sameTeam** | **Boolean** | Whether this permission applies to teammates (multi-tenancy mode only) |  |
|**tags** | **List&lt;String&gt;** | List of tags of the permission |  |



## Enum: LevelEnum

| Name | Value |
|---- | -----|
| APP | &quot;app&quot; |
| CHANNEL | &quot;channel&quot; |



