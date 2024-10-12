

# AppsCreateRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | A short text describing the app |  [optional] |
|**displayName** | **String** | The descriptive name of the app. This can contain any characters |  |
|**name** | **String** | The name of the app used in URLs |  [optional] |
|**os** | [**OsEnum**](#OsEnum) | The OS the app will be running on |  |
|**platform** | [**PlatformEnum**](#PlatformEnum) | The platform of the app |  |
|**releaseType** | **String** | A one-word descriptive release-type value that starts with a capital letter but is otherwise lowercase |  [optional] |



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



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| JAVA | &quot;Java&quot; |
| OBJECTIVE_C_SWIFT | &quot;Objective-C-Swift&quot; |
| UWP | &quot;UWP&quot; |
| CORDOVA | &quot;Cordova&quot; |
| REACT_NATIVE | &quot;React-Native&quot; |
| XAMARIN | &quot;Xamarin&quot; |
| UNITY | &quot;Unity&quot; |
| ELECTRON | &quot;Electron&quot; |
| WPF | &quot;WPF&quot; |
| WIN_FORMS | &quot;WinForms&quot; |
| CUSTOM | &quot;Custom&quot; |



