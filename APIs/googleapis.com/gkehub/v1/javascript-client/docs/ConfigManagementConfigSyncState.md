# GkeHubApi.ConfigManagementConfigSyncState

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deploymentState** | [**ConfigManagementConfigSyncDeploymentState**](ConfigManagementConfigSyncDeploymentState.md) |  | [optional] 
**errors** | [**[ConfigManagementConfigSyncError]**](ConfigManagementConfigSyncError.md) | Errors pertaining to the installation of Config Sync. | [optional] 
**reposyncCrd** | **String** | The state of the Reposync CRD | [optional] 
**rootsyncCrd** | **String** | The state of the RootSync CRD | [optional] 
**state** | **String** | The state of CS This field summarizes the other fields in this message. | [optional] 
**syncState** | [**ConfigManagementSyncState**](ConfigManagementSyncState.md) |  | [optional] 
**version** | [**ConfigManagementConfigSyncVersion**](ConfigManagementConfigSyncVersion.md) |  | [optional] 



## Enum: ReposyncCrdEnum


* `CRD_STATE_UNSPECIFIED` (value: `"CRD_STATE_UNSPECIFIED"`)

* `NOT_INSTALLED` (value: `"NOT_INSTALLED"`)

* `INSTALLED` (value: `"INSTALLED"`)

* `TERMINATING` (value: `"TERMINATING"`)

* `INSTALLING` (value: `"INSTALLING"`)





## Enum: RootsyncCrdEnum


* `CRD_STATE_UNSPECIFIED` (value: `"CRD_STATE_UNSPECIFIED"`)

* `NOT_INSTALLED` (value: `"NOT_INSTALLED"`)

* `INSTALLED` (value: `"INSTALLED"`)

* `TERMINATING` (value: `"TERMINATING"`)

* `INSTALLING` (value: `"INSTALLING"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CONFIG_SYNC_NOT_INSTALLED` (value: `"CONFIG_SYNC_NOT_INSTALLED"`)

* `CONFIG_SYNC_INSTALLED` (value: `"CONFIG_SYNC_INSTALLED"`)

* `CONFIG_SYNC_ERROR` (value: `"CONFIG_SYNC_ERROR"`)

* `CONFIG_SYNC_PENDING` (value: `"CONFIG_SYNC_PENDING"`)




