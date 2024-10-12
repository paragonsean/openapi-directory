

# AppAccessRiskVerdict

Contains signals about others apps on the device which could be used to access or control the requesting app.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**otherApps** | [**OtherAppsEnum**](#OtherAppsEnum) | Required. App access risk verdict related to apps that are not installed by Google Play, and are not preloaded on the system image by the device manufacturer. |  [optional] |
|**playOrSystemApps** | [**PlayOrSystemAppsEnum**](#PlayOrSystemAppsEnum) | Required. App access risk verdict related to apps that are not installed by the Google Play Store, and are not preloaded on the system image by the device manufacturer. |  [optional] |



## Enum: OtherAppsEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| UNEVALUATED | &quot;UNEVALUATED&quot; |
| NOT_INSTALLED | &quot;NOT_INSTALLED&quot; |
| INSTALLED | &quot;INSTALLED&quot; |
| CAPTURING | &quot;CAPTURING&quot; |
| CONTROLLING | &quot;CONTROLLING&quot; |



## Enum: PlayOrSystemAppsEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| UNEVALUATED | &quot;UNEVALUATED&quot; |
| NOT_INSTALLED | &quot;NOT_INSTALLED&quot; |
| INSTALLED | &quot;INSTALLED&quot; |
| CAPTURING | &quot;CAPTURING&quot; |
| CONTROLLING | &quot;CONTROLLING&quot; |



