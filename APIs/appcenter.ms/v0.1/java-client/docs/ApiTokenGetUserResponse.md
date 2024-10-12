

# ApiTokenGetUserResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**tokenId** | **UUID** | The token&#39;s unique id (UUID) |  |
|**tokenScope** | [**List&lt;TokenScopeEnum&gt;**](#List&lt;TokenScopeEnum&gt;) | The token&#39;s scope. A list of allowed roles. |  |
|**userEmail** | **String** | The user email |  |
|**userId** | **UUID** | The unique id (UUID) of the user |  |
|**userOrigin** | [**UserOriginEnum**](#UserOriginEnum) | The creation origin of the user who created this api token |  |



## Enum: List&lt;TokenScopeEnum&gt;

| Name | Value |
|---- | -----|
| ALL | &quot;all&quot; |
| IN_APP_UPDATE | &quot;in_app_update&quot; |
| VIEWER | &quot;viewer&quot; |



## Enum: UserOriginEnum

| Name | Value |
|---- | -----|
| APPCENTER | &quot;appcenter&quot; |
| HOCKEYAPP | &quot;hockeyapp&quot; |
| CODEPUSH | &quot;codepush&quot; |



