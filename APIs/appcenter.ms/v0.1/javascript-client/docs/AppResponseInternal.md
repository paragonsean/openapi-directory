# AppCenterClient.AppResponseInternal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | The description of the app | [optional] 
**displayName** | **String** | The display name of the app | 
**iconSource** | **String** | The string representation of the source of the app&#39;s icon | [optional] 
**iconUrl** | **String** | The string representation of the URL pointing to the app&#39;s icon | [optional] 
**id** | **String** | The unique ID (UUID) of the app | 
**name** | **String** | The name of the app used in URLs | 
**os** | **String** | The OS the app will be running on | 
**owner** | **Object** | The information about the app&#39;s owner | 
**releaseType** | **String** | A one-word descriptive release-type value that starts with a capital letter but is otherwise lowercase | [optional] 
**appSecret** | **String** | A unique and secret key used to identify the app in communication with the ingestion endpoint for crash reporting and analytics | 
**azureSubscription** | **Object** |  | [optional] 
**createdAt** | **String** | The created date of this app | [optional] 
**memberPermissions** | **[String]** | The permissions of the calling user | [optional] 
**origin** | **String** | The creation origin of this app | 
**platform** | **String** | The platform of the app | 
**updatedAt** | **String** | The last updated date of this app | [optional] 
**cutoverFromHockeyappAt** | **String** | The cutover date of this app | [optional] 
**featureFlags** | **[String]** | The feature flags that are enabled for this app | [optional] 
**repositories** | [**[AppResponseInternalAllOfRepositories]**](AppResponseInternalAllOfRepositories.md) | The repositories associated with this app | [optional] 
**userPermissions** | [**AppResponseInternalAllOfUserPermissions**](AppResponseInternalAllOfUserPermissions.md) |  | [optional] 



## Enum: OsEnum


* `Android` (value: `"Android"`)

* `iOS` (value: `"iOS"`)

* `macOS` (value: `"macOS"`)

* `Tizen` (value: `"Tizen"`)

* `tvOS` (value: `"tvOS"`)

* `Windows` (value: `"Windows"`)

* `Linux` (value: `"Linux"`)

* `Custom` (value: `"Custom"`)





## Enum: [MemberPermissionsEnum]


* `manager` (value: `"manager"`)

* `developer` (value: `"developer"`)

* `viewer` (value: `"viewer"`)

* `tester` (value: `"tester"`)





## Enum: OriginEnum


* `appcenter` (value: `"appcenter"`)

* `hockeyapp` (value: `"hockeyapp"`)

* `codepush` (value: `"codepush"`)





## Enum: PlatformEnum


* `Java` (value: `"Java"`)

* `Objective-C-Swift` (value: `"Objective-C-Swift"`)

* `UWP` (value: `"UWP"`)

* `Cordova` (value: `"Cordova"`)

* `React-Native` (value: `"React-Native"`)

* `Unity` (value: `"Unity"`)

* `Electron` (value: `"Electron"`)

* `Xamarin` (value: `"Xamarin"`)

* `WPF` (value: `"WPF"`)

* `WinForms` (value: `"WinForms"`)

* `Unknown` (value: `"Unknown"`)

* `Custom` (value: `"Custom"`)




