# AppCenterClient.AppUserPermissionResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appId** | **String** | The unique id (UUID) of the app | 
**appOrigin** | **String** | The creation origin of this app | 
**appSecret** | **String** | A unique and secret key used to identify the app in communication with the ingestion endpoint for crash reporting and analytics | 
**permissions** | **[String]** | The permissions the user has for the app | 
**userEmail** | **String** | The email of the user | 
**userId** | **String** | The unique id (UUID) of the user | 



## Enum: AppOriginEnum


* `appcenter` (value: `"appcenter"`)

* `codepush` (value: `"codepush"`)





## Enum: [PermissionsEnum]


* `manager` (value: `"manager"`)

* `developer` (value: `"developer"`)

* `viewer` (value: `"viewer"`)

* `tester` (value: `"tester"`)




