

# IOSMAMPolicyProperties

Intune MAM iOS Policy Properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fileEncryptionLevel** | [**FileEncryptionLevelEnum**](#FileEncryptionLevelEnum) |  |  [optional] |
|**touchId** | [**TouchIdEnum**](#TouchIdEnum) |  |  [optional] |
|**accessRecheckOfflineTimeout** | **String** |  |  [optional] |
|**accessRecheckOnlineTimeout** | **String** |  |  [optional] |
|**appSharingFromLevel** | [**AppSharingFromLevelEnum**](#AppSharingFromLevelEnum) |  |  [optional] |
|**appSharingToLevel** | [**AppSharingToLevelEnum**](#AppSharingToLevelEnum) |  |  [optional] |
|**authentication** | [**AuthenticationEnum**](#AuthenticationEnum) |  |  [optional] |
|**clipboardSharingLevel** | [**ClipboardSharingLevelEnum**](#ClipboardSharingLevelEnum) |  |  [optional] |
|**dataBackup** | [**DataBackupEnum**](#DataBackupEnum) |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**deviceCompliance** | [**DeviceComplianceEnum**](#DeviceComplianceEnum) |  |  [optional] |
|**fileSharingSaveAs** | [**FileSharingSaveAsEnum**](#FileSharingSaveAsEnum) |  |  [optional] |
|**friendlyName** | **String** |  |  |
|**groupStatus** | [**GroupStatusEnum**](#GroupStatusEnum) |  |  [optional] [readonly] |
|**lastModifiedTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**managedBrowser** | [**ManagedBrowserEnum**](#ManagedBrowserEnum) |  |  [optional] |
|**numOfApps** | **Integer** |  |  [optional] [readonly] |
|**offlineWipeTimeout** | **String** |  |  [optional] |
|**pin** | [**PinEnum**](#PinEnum) |  |  [optional] |
|**pinNumRetry** | **Integer** |  |  [optional] |



## Enum: FileEncryptionLevelEnum

| Name | Value |
|---- | -----|
| DEVICE_LOCKED | &quot;deviceLocked&quot; |
| DEVICE_LOCKED_EXCEPT_FILES_OPEN | &quot;deviceLockedExceptFilesOpen&quot; |
| AFTER_DEVICE_RESTART | &quot;afterDeviceRestart&quot; |
| USE_DEVICE_SETTINGS | &quot;useDeviceSettings&quot; |



## Enum: TouchIdEnum

| Name | Value |
|---- | -----|
| ENABLE | &quot;enable&quot; |
| DISABLE | &quot;disable&quot; |



## Enum: AppSharingFromLevelEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| POLICY_MANAGED_APPS | &quot;policyManagedApps&quot; |
| ALL_APPS | &quot;allApps&quot; |



## Enum: AppSharingToLevelEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| POLICY_MANAGED_APPS | &quot;policyManagedApps&quot; |
| ALL_APPS | &quot;allApps&quot; |



## Enum: AuthenticationEnum

| Name | Value |
|---- | -----|
| REQUIRED | &quot;required&quot; |
| NOT_REQUIRED | &quot;notRequired&quot; |



## Enum: ClipboardSharingLevelEnum

| Name | Value |
|---- | -----|
| BLOCKED | &quot;blocked&quot; |
| POLICY_MANAGED_APPS | &quot;policyManagedApps&quot; |
| POLICY_MANAGED_APPS_WITH_PASTE_IN | &quot;policyManagedAppsWithPasteIn&quot; |
| ALL_APPS | &quot;allApps&quot; |



## Enum: DataBackupEnum

| Name | Value |
|---- | -----|
| ALLOW | &quot;allow&quot; |
| BLOCK | &quot;block&quot; |



## Enum: DeviceComplianceEnum

| Name | Value |
|---- | -----|
| ENABLE | &quot;enable&quot; |
| DISABLE | &quot;disable&quot; |



## Enum: FileSharingSaveAsEnum

| Name | Value |
|---- | -----|
| ALLOW | &quot;allow&quot; |
| BLOCK | &quot;block&quot; |



## Enum: GroupStatusEnum

| Name | Value |
|---- | -----|
| NOT_TARGETED | &quot;notTargeted&quot; |
| TARGETED | &quot;targeted&quot; |



## Enum: ManagedBrowserEnum

| Name | Value |
|---- | -----|
| REQUIRED | &quot;required&quot; |
| NOT_REQUIRED | &quot;notRequired&quot; |



## Enum: PinEnum

| Name | Value |
|---- | -----|
| REQUIRED | &quot;required&quot; |
| NOT_REQUIRED | &quot;notRequired&quot; |



