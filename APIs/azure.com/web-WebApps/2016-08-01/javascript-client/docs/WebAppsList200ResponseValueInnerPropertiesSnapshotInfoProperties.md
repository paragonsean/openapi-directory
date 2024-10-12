# WebAppsApiClient.WebAppsList200ResponseValueInnerPropertiesSnapshotInfoProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ignoreConflictingHostNames** | **Boolean** | If true, custom hostname conflicts will be ignored when recovering to a target web app. This setting is only necessary when RecoverConfiguration is enabled. | [optional] 
**overwrite** | **Boolean** | If &lt;code&gt;true&lt;/code&gt; the recovery operation can overwrite source app; otherwise, &lt;code&gt;false&lt;/code&gt;. | 
**recoverConfiguration** | **Boolean** | If true, site configuration, in addition to content, will be reverted. | [optional] 
**recoveryTarget** | [**WebAppsList200ResponseValueInnerPropertiesSnapshotInfoPropertiesRecoveryTarget**](WebAppsList200ResponseValueInnerPropertiesSnapshotInfoPropertiesRecoveryTarget.md) |  | [optional] 
**snapshotTime** | **String** | Point in time in which the app recovery should be attempted, formatted as a DateTime string. | [optional] 


