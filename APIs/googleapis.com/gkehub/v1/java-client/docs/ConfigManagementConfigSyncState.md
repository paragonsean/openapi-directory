

# ConfigManagementConfigSyncState

State information for ConfigSync

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deploymentState** | [**ConfigManagementConfigSyncDeploymentState**](ConfigManagementConfigSyncDeploymentState.md) |  |  [optional] |
|**errors** | [**List&lt;ConfigManagementConfigSyncError&gt;**](ConfigManagementConfigSyncError.md) | Errors pertaining to the installation of Config Sync. |  [optional] |
|**reposyncCrd** | [**ReposyncCrdEnum**](#ReposyncCrdEnum) | The state of the Reposync CRD |  [optional] |
|**rootsyncCrd** | [**RootsyncCrdEnum**](#RootsyncCrdEnum) | The state of the RootSync CRD |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of CS This field summarizes the other fields in this message. |  [optional] |
|**syncState** | [**ConfigManagementSyncState**](ConfigManagementSyncState.md) |  |  [optional] |
|**version** | [**ConfigManagementConfigSyncVersion**](ConfigManagementConfigSyncVersion.md) |  |  [optional] |



## Enum: ReposyncCrdEnum

| Name | Value |
|---- | -----|
| CRD_STATE_UNSPECIFIED | &quot;CRD_STATE_UNSPECIFIED&quot; |
| NOT_INSTALLED | &quot;NOT_INSTALLED&quot; |
| INSTALLED | &quot;INSTALLED&quot; |
| TERMINATING | &quot;TERMINATING&quot; |
| INSTALLING | &quot;INSTALLING&quot; |



## Enum: RootsyncCrdEnum

| Name | Value |
|---- | -----|
| CRD_STATE_UNSPECIFIED | &quot;CRD_STATE_UNSPECIFIED&quot; |
| NOT_INSTALLED | &quot;NOT_INSTALLED&quot; |
| INSTALLED | &quot;INSTALLED&quot; |
| TERMINATING | &quot;TERMINATING&quot; |
| INSTALLING | &quot;INSTALLING&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CONFIG_SYNC_NOT_INSTALLED | &quot;CONFIG_SYNC_NOT_INSTALLED&quot; |
| CONFIG_SYNC_INSTALLED | &quot;CONFIG_SYNC_INSTALLED&quot; |
| CONFIG_SYNC_ERROR | &quot;CONFIG_SYNC_ERROR&quot; |
| CONFIG_SYNC_PENDING | &quot;CONFIG_SYNC_PENDING&quot; |



