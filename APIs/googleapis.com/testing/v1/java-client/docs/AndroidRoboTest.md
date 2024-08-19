

# AndroidRoboTest

A test of an android application that explores the application on a virtual or physical Android Device, finding culprits and crashes as it goes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appApk** | [**FileReference**](FileReference.md) |  |  [optional] |
|**appBundle** | [**AppBundle**](AppBundle.md) |  |  [optional] |
|**appInitialActivity** | **String** | The initial activity that should be used to start the app. |  [optional] |
|**appPackageId** | **String** | The java package for the application under test. The default value is determined by examining the application&#39;s manifest. |  [optional] |
|**maxDepth** | **Integer** | The max depth of the traversal stack Robo can explore. Needs to be at least 2 to make Robo explore the app beyond the first activity. Default is 50. |  [optional] |
|**maxSteps** | **Integer** | The max number of steps Robo can execute. Default is no limit. |  [optional] |
|**roboDirectives** | [**List&lt;RoboDirective&gt;**](RoboDirective.md) | A set of directives Robo should apply during the crawl. This allows users to customize the crawl. For example, the username and password for a test account can be provided. |  [optional] |
|**roboMode** | [**RoboModeEnum**](#RoboModeEnum) | The mode in which Robo should run. Most clients should allow the server to populate this field automatically. |  [optional] |
|**roboScript** | [**FileReference**](FileReference.md) |  |  [optional] |
|**startingIntents** | [**List&lt;RoboStartingIntent&gt;**](RoboStartingIntent.md) | The intents used to launch the app for the crawl. If none are provided, then the main launcher activity is launched. If some are provided, then only those provided are launched (the main launcher activity must be provided explicitly). |  [optional] |



## Enum: RoboModeEnum

| Name | Value |
|---- | -----|
| MODE_UNSPECIFIED | &quot;ROBO_MODE_UNSPECIFIED&quot; |
| VERSION_1 | &quot;ROBO_VERSION_1&quot; |
| VERSION_2 | &quot;ROBO_VERSION_2&quot; |



