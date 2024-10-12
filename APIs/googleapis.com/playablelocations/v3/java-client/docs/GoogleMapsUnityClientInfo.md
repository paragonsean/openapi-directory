

# GoogleMapsUnityClientInfo

Client information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**_apiClient** | **String** | API client name and version. For example, the SDK calling the API. The exact format is up to the client. |  [optional] |
|**applicationId** | **String** | Application ID, such as the package name on Android and the bundle identifier on iOS platforms. |  [optional] |
|**applicationVersion** | **String** | Application version number, such as \&quot;1.2.3\&quot;. The exact format is application-dependent. |  [optional] |
|**deviceModel** | **String** | Device model as reported by the device. The exact format is platform-dependent. |  [optional] |
|**languageCode** | **String** | Language code (in BCP-47 format) indicating the UI language of the client. Examples are \&quot;en\&quot;, \&quot;en-US\&quot; or \&quot;ja-Latn\&quot;. For more information, see http://www.unicode.org/reports/tr35/#Unicode_locale_identifier. |  [optional] |
|**operatingSystem** | **String** | Operating system name and version as reported by the OS. For example, \&quot;Mac OS X 10.10.4\&quot;. The exact format is platform-dependent. |  [optional] |
|**operatingSystemBuild** | **String** | Build number/version of the operating system. e.g., the contents of android.os.Build.ID in Android, or the contents of sysctl \&quot;kern.osversion\&quot; in iOS. |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) | Platform where the application is running. |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| PLATFORM_UNSPECIFIED | &quot;PLATFORM_UNSPECIFIED&quot; |
| EDITOR | &quot;EDITOR&quot; |
| MAC_OS | &quot;MAC_OS&quot; |
| WINDOWS | &quot;WINDOWS&quot; |
| LINUX | &quot;LINUX&quot; |
| ANDROID | &quot;ANDROID&quot; |
| IOS | &quot;IOS&quot; |
| WEB_GL | &quot;WEB_GL&quot; |



