

# GoogleChromeManagementV1InstalledApp

Describes an installed app.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appId** | **String** | Output only. Unique identifier of the app. For Chrome apps and extensions, the 32-character id (e.g. ehoadneljpdggcbbknedodolkkjodefl). For Android apps, the package name (e.g. com.evernote). |  [optional] [readonly] |
|**appInstallType** | [**AppInstallTypeEnum**](#AppInstallTypeEnum) | Output only. How the app was installed. |  [optional] [readonly] |
|**appSource** | [**AppSourceEnum**](#AppSourceEnum) | Output only. Source of the installed app. |  [optional] [readonly] |
|**appType** | [**AppTypeEnum**](#AppTypeEnum) | Output only. Type of the app. |  [optional] [readonly] |
|**browserDeviceCount** | **String** | Output only. Count of browser devices with this app installed. |  [optional] [readonly] |
|**description** | **String** | Output only. Description of the installed app. |  [optional] [readonly] |
|**disabled** | **Boolean** | Output only. Whether the app is disabled. |  [optional] [readonly] |
|**displayName** | **String** | Output only. Name of the installed app. |  [optional] [readonly] |
|**homepageUri** | **String** | Output only. Homepage uri of the installed app. |  [optional] [readonly] |
|**osUserCount** | **String** | Output only. Count of ChromeOS users with this app installed. |  [optional] [readonly] |
|**permissions** | **List&lt;String&gt;** | Output only. Permissions of the installed app. |  [optional] [readonly] |



## Enum: AppInstallTypeEnum

| Name | Value |
|---- | -----|
| APP_INSTALL_TYPE_UNSPECIFIED | &quot;APP_INSTALL_TYPE_UNSPECIFIED&quot; |
| MULTIPLE | &quot;MULTIPLE&quot; |
| NORMAL | &quot;NORMAL&quot; |
| ADMIN | &quot;ADMIN&quot; |
| DEVELOPMENT | &quot;DEVELOPMENT&quot; |
| SIDELOAD | &quot;SIDELOAD&quot; |
| OTHER | &quot;OTHER&quot; |



## Enum: AppSourceEnum

| Name | Value |
|---- | -----|
| APP_SOURCE_UNSPECIFIED | &quot;APP_SOURCE_UNSPECIFIED&quot; |
| CHROME_WEBSTORE | &quot;CHROME_WEBSTORE&quot; |
| PLAY_STORE | &quot;PLAY_STORE&quot; |



## Enum: AppTypeEnum

| Name | Value |
|---- | -----|
| APP_TYPE_UNSPECIFIED | &quot;APP_TYPE_UNSPECIFIED&quot; |
| EXTENSION | &quot;EXTENSION&quot; |
| APP | &quot;APP&quot; |
| THEME | &quot;THEME&quot; |
| HOSTED_APP | &quot;HOSTED_APP&quot; |
| ANDROID_APP | &quot;ANDROID_APP&quot; |



