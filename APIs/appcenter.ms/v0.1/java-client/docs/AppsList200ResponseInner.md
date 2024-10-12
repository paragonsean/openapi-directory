

# AppsList200ResponseInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | The description of the app |  [optional] |
|**displayName** | **String** | The display name of the app |  |
|**iconSource** | **String** | The string representation of the source of the app&#39;s icon |  [optional] |
|**iconUrl** | **String** | The string representation of the URL pointing to the app&#39;s icon |  [optional] |
|**id** | **UUID** | The unique ID (UUID) of the app |  |
|**name** | **String** | The name of the app used in URLs |  |
|**os** | [**OsEnum**](#OsEnum) | The OS the app will be running on |  |
|**owner** | [**AppsList200ResponseInnerAllOfOwner**](AppsList200ResponseInnerAllOfOwner.md) |  |  |
|**releaseType** | **String** | A one-word descriptive release-type value that starts with a capital letter but is otherwise lowercase |  [optional] |
|**appSecret** | **String** | A unique and secret key used to identify the app in communication with the ingestion endpoint for crash reporting and analytics |  |
|**azureSubscription** | [**AppsList200ResponseInnerAllOfAzureSubscription**](AppsList200ResponseInnerAllOfAzureSubscription.md) |  |  [optional] |
|**createdAt** | **String** | The created date of this app |  [optional] |
|**memberPermissions** | [**List&lt;MemberPermissionsEnum&gt;**](#List&lt;MemberPermissionsEnum&gt;) | The permissions of the calling user |  [optional] |
|**origin** | [**OriginEnum**](#OriginEnum) | The creation origin of this app |  |
|**platform** | [**PlatformEnum**](#PlatformEnum) | The platform of the app |  |
|**updatedAt** | **String** | The last updated date of this app |  [optional] |



## Enum: OsEnum

| Name | Value |
|---- | -----|
| ANDROID | &quot;Android&quot; |
| I_OS | &quot;iOS&quot; |
| MAC_OS | &quot;macOS&quot; |
| TIZEN | &quot;Tizen&quot; |
| TV_OS | &quot;tvOS&quot; |
| WINDOWS | &quot;Windows&quot; |
| LINUX | &quot;Linux&quot; |
| CUSTOM | &quot;Custom&quot; |



## Enum: List&lt;MemberPermissionsEnum&gt;

| Name | Value |
|---- | -----|
| MANAGER | &quot;manager&quot; |
| DEVELOPER | &quot;developer&quot; |
| VIEWER | &quot;viewer&quot; |
| TESTER | &quot;tester&quot; |



## Enum: OriginEnum

| Name | Value |
|---- | -----|
| APPCENTER | &quot;appcenter&quot; |
| HOCKEYAPP | &quot;hockeyapp&quot; |
| CODEPUSH | &quot;codepush&quot; |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| JAVA | &quot;Java&quot; |
| OBJECTIVE_C_SWIFT | &quot;Objective-C-Swift&quot; |
| UWP | &quot;UWP&quot; |
| CORDOVA | &quot;Cordova&quot; |
| REACT_NATIVE | &quot;React-Native&quot; |
| UNITY | &quot;Unity&quot; |
| ELECTRON | &quot;Electron&quot; |
| XAMARIN | &quot;Xamarin&quot; |
| WPF | &quot;WPF&quot; |
| WIN_FORMS | &quot;WinForms&quot; |
| UNKNOWN | &quot;Unknown&quot; |
| CUSTOM | &quot;Custom&quot; |



