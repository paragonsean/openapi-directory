

# WebApp

A WebApps resource represents a web app created for an enterprise. Web apps are published to managed Google Play and can be distributed like other Android apps. On a user's device, a web app opens its specified URL.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayMode** | [**DisplayModeEnum**](#DisplayModeEnum) | The display mode of the web app. Possible values include: - \&quot;minimalUi\&quot;, the device&#39;s status bar, navigation bar, the app&#39;s URL, and a refresh button are visible when the app is open. For HTTP URLs, you can only select this option. - \&quot;standalone\&quot;, the device&#39;s status bar and navigation bar are visible when the app is open. - \&quot;fullScreen\&quot;, the app opens in full screen mode, hiding the device&#39;s status and navigation bars. All browser UI elements, page URL, system status bar and back button are not visible, and the web app takes up the entirety of the available display area.  |  [optional] |
|**icons** | [**List&lt;WebAppIcon&gt;**](WebAppIcon.md) | A list of icons representing this website. If absent, a default icon (for create) or the current icon (for update) will be used. |  [optional] |
|**isPublished** | **Boolean** | A flag whether the app has been published to the Play store yet. |  [optional] |
|**startUrl** | **String** | The start URL, i.e. the URL that should load when the user opens the application. |  [optional] |
|**title** | **String** | The title of the web app as displayed to the user (e.g., amongst a list of other applications, or as a label for an icon). |  [optional] |
|**versionCode** | **String** | The current version of the app. Note that the version can automatically increase during the lifetime of the web app, while Google does internal housekeeping to keep the web app up-to-date. |  [optional] |
|**webAppId** | **String** | The ID of the application. A string of the form \&quot;app:&lt;package name&gt;\&quot; where the package name always starts with the prefix \&quot;com.google.enterprise.webapp.\&quot; followed by a random id. |  [optional] |



## Enum: DisplayModeEnum

| Name | Value |
|---- | -----|
| DISPLAY_MODE_UNSPECIFIED | &quot;displayModeUnspecified&quot; |
| MINIMAL_UI | &quot;minimalUi&quot; |
| STANDALONE | &quot;standalone&quot; |
| FULL_SCREEN | &quot;fullScreen&quot; |



