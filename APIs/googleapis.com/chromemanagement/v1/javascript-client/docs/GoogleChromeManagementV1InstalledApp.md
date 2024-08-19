# ChromeManagementApi.GoogleChromeManagementV1InstalledApp

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appId** | **String** | Output only. Unique identifier of the app. For Chrome apps and extensions, the 32-character id (e.g. ehoadneljpdggcbbknedodolkkjodefl). For Android apps, the package name (e.g. com.evernote). | [optional] [readonly] 
**appInstallType** | **String** | Output only. How the app was installed. | [optional] [readonly] 
**appSource** | **String** | Output only. Source of the installed app. | [optional] [readonly] 
**appType** | **String** | Output only. Type of the app. | [optional] [readonly] 
**browserDeviceCount** | **String** | Output only. Count of browser devices with this app installed. | [optional] [readonly] 
**description** | **String** | Output only. Description of the installed app. | [optional] [readonly] 
**disabled** | **Boolean** | Output only. Whether the app is disabled. | [optional] [readonly] 
**displayName** | **String** | Output only. Name of the installed app. | [optional] [readonly] 
**homepageUri** | **String** | Output only. Homepage uri of the installed app. | [optional] [readonly] 
**osUserCount** | **String** | Output only. Count of ChromeOS users with this app installed. | [optional] [readonly] 
**permissions** | **[String]** | Output only. Permissions of the installed app. | [optional] [readonly] 



## Enum: AppInstallTypeEnum


* `APP_INSTALL_TYPE_UNSPECIFIED` (value: `"APP_INSTALL_TYPE_UNSPECIFIED"`)

* `MULTIPLE` (value: `"MULTIPLE"`)

* `NORMAL` (value: `"NORMAL"`)

* `ADMIN` (value: `"ADMIN"`)

* `DEVELOPMENT` (value: `"DEVELOPMENT"`)

* `SIDELOAD` (value: `"SIDELOAD"`)

* `OTHER` (value: `"OTHER"`)





## Enum: AppSourceEnum


* `APP_SOURCE_UNSPECIFIED` (value: `"APP_SOURCE_UNSPECIFIED"`)

* `CHROME_WEBSTORE` (value: `"CHROME_WEBSTORE"`)

* `PLAY_STORE` (value: `"PLAY_STORE"`)





## Enum: AppTypeEnum


* `APP_TYPE_UNSPECIFIED` (value: `"APP_TYPE_UNSPECIFIED"`)

* `EXTENSION` (value: `"EXTENSION"`)

* `APP` (value: `"APP"`)

* `THEME` (value: `"THEME"`)

* `HOSTED_APP` (value: `"HOSTED_APP"`)

* `ANDROID_APP` (value: `"ANDROID_APP"`)




