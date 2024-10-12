# IntuneResourceManagementClient.MAMPolicyProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessRecheckOfflineTimeout** | **String** |  | [optional] 
**accessRecheckOnlineTimeout** | **String** |  | [optional] 
**appSharingFromLevel** | **String** |  | [optional] [default to &#39;none&#39;]
**appSharingToLevel** | **String** |  | [optional] [default to &#39;none&#39;]
**authentication** | **String** |  | [optional] [default to &#39;required&#39;]
**clipboardSharingLevel** | **String** |  | [optional] [default to &#39;blocked&#39;]
**dataBackup** | **String** |  | [optional] [default to &#39;allow&#39;]
**description** | **String** |  | [optional] 
**deviceCompliance** | **String** |  | [optional] [default to &#39;enable&#39;]
**fileSharingSaveAs** | **String** |  | [optional] [default to &#39;allow&#39;]
**friendlyName** | **String** |  | 
**groupStatus** | **String** |  | [optional] [readonly] [default to &#39;notTargeted&#39;]
**lastModifiedTime** | **Date** |  | [optional] [readonly] 
**managedBrowser** | **String** |  | [optional] [default to &#39;required&#39;]
**numOfApps** | **Number** |  | [optional] [readonly] 
**offlineWipeTimeout** | **String** |  | [optional] 
**pin** | **String** |  | [optional] [default to &#39;required&#39;]
**pinNumRetry** | **Number** |  | [optional] 



## Enum: AppSharingFromLevelEnum


* `none` (value: `"none"`)

* `policyManagedApps` (value: `"policyManagedApps"`)

* `allApps` (value: `"allApps"`)





## Enum: AppSharingToLevelEnum


* `none` (value: `"none"`)

* `policyManagedApps` (value: `"policyManagedApps"`)

* `allApps` (value: `"allApps"`)





## Enum: AuthenticationEnum


* `required` (value: `"required"`)

* `notRequired` (value: `"notRequired"`)





## Enum: ClipboardSharingLevelEnum


* `blocked` (value: `"blocked"`)

* `policyManagedApps` (value: `"policyManagedApps"`)

* `policyManagedAppsWithPasteIn` (value: `"policyManagedAppsWithPasteIn"`)

* `allApps` (value: `"allApps"`)





## Enum: DataBackupEnum


* `allow` (value: `"allow"`)

* `block` (value: `"block"`)





## Enum: DeviceComplianceEnum


* `enable` (value: `"enable"`)

* `disable` (value: `"disable"`)





## Enum: FileSharingSaveAsEnum


* `allow` (value: `"allow"`)

* `block` (value: `"block"`)





## Enum: GroupStatusEnum


* `notTargeted` (value: `"notTargeted"`)

* `targeted` (value: `"targeted"`)





## Enum: ManagedBrowserEnum


* `required` (value: `"required"`)

* `notRequired` (value: `"notRequired"`)





## Enum: PinEnum


* `required` (value: `"required"`)

* `notRequired` (value: `"notRequired"`)




