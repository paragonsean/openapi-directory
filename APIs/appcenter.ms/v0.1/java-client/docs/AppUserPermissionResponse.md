

# AppUserPermissionResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appId** | **UUID** | The unique id (UUID) of the app |  |
|**appOrigin** | [**AppOriginEnum**](#AppOriginEnum) | The creation origin of this app |  |
|**appSecret** | **String** | A unique and secret key used to identify the app in communication with the ingestion endpoint for crash reporting and analytics |  |
|**permissions** | [**List&lt;PermissionsEnum&gt;**](#List&lt;PermissionsEnum&gt;) | The permissions the user has for the app |  |
|**userEmail** | **String** | The email of the user |  |
|**userId** | **UUID** | The unique id (UUID) of the user |  |



## Enum: AppOriginEnum

| Name | Value |
|---- | -----|
| APPCENTER | &quot;appcenter&quot; |
| CODEPUSH | &quot;codepush&quot; |



## Enum: List&lt;PermissionsEnum&gt;

| Name | Value |
|---- | -----|
| MANAGER | &quot;manager&quot; |
| DEVELOPER | &quot;developer&quot; |
| VIEWER | &quot;viewer&quot; |
| TESTER | &quot;tester&quot; |



