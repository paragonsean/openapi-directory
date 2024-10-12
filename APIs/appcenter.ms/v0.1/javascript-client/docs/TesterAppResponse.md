# AppCenterClient.TesterAppResponse

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
**owner** | [**AppsList200ResponseInnerAllOfOwner**](AppsList200ResponseInnerAllOfOwner.md) |  | 
**releaseType** | **String** | A one-word descriptive release-type value that starts with a capital letter but is otherwise lowercase | [optional] 
**microsoftInternal** | **Boolean** | it indicates if the app is microsoft internal | [optional] 
**permissions** | **[String]** | The permissions associated with the app | [optional] 



## Enum: OsEnum


* `Android` (value: `"Android"`)

* `iOS` (value: `"iOS"`)

* `macOS` (value: `"macOS"`)

* `Tizen` (value: `"Tizen"`)

* `tvOS` (value: `"tvOS"`)

* `Windows` (value: `"Windows"`)

* `Linux` (value: `"Linux"`)

* `Custom` (value: `"Custom"`)





## Enum: [PermissionsEnum]


* `can_remove_from_app` (value: `"can_remove_from_app"`)




