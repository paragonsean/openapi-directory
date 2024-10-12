

# ConfigManagementConfigSyncDeploymentState

The state of ConfigSync's deployment on a cluster

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**admissionWebhook** | [**AdmissionWebhookEnum**](#AdmissionWebhookEnum) | Deployment state of admission-webhook |  [optional] |
|**gitSync** | [**GitSyncEnum**](#GitSyncEnum) | Deployment state of the git-sync pod |  [optional] |
|**importer** | [**ImporterEnum**](#ImporterEnum) | Deployment state of the importer pod |  [optional] |
|**monitor** | [**MonitorEnum**](#MonitorEnum) | Deployment state of the monitor pod |  [optional] |
|**reconcilerManager** | [**ReconcilerManagerEnum**](#ReconcilerManagerEnum) | Deployment state of reconciler-manager pod |  [optional] |
|**rootReconciler** | [**RootReconcilerEnum**](#RootReconcilerEnum) | Deployment state of root-reconciler |  [optional] |
|**syncer** | [**SyncerEnum**](#SyncerEnum) | Deployment state of the syncer pod |  [optional] |



## Enum: AdmissionWebhookEnum

| Name | Value |
|---- | -----|
| DEPLOYMENT_STATE_UNSPECIFIED | &quot;DEPLOYMENT_STATE_UNSPECIFIED&quot; |
| NOT_INSTALLED | &quot;NOT_INSTALLED&quot; |
| INSTALLED | &quot;INSTALLED&quot; |
| ERROR | &quot;ERROR&quot; |
| PENDING | &quot;PENDING&quot; |



## Enum: GitSyncEnum

| Name | Value |
|---- | -----|
| DEPLOYMENT_STATE_UNSPECIFIED | &quot;DEPLOYMENT_STATE_UNSPECIFIED&quot; |
| NOT_INSTALLED | &quot;NOT_INSTALLED&quot; |
| INSTALLED | &quot;INSTALLED&quot; |
| ERROR | &quot;ERROR&quot; |
| PENDING | &quot;PENDING&quot; |



## Enum: ImporterEnum

| Name | Value |
|---- | -----|
| DEPLOYMENT_STATE_UNSPECIFIED | &quot;DEPLOYMENT_STATE_UNSPECIFIED&quot; |
| NOT_INSTALLED | &quot;NOT_INSTALLED&quot; |
| INSTALLED | &quot;INSTALLED&quot; |
| ERROR | &quot;ERROR&quot; |
| PENDING | &quot;PENDING&quot; |



## Enum: MonitorEnum

| Name | Value |
|---- | -----|
| DEPLOYMENT_STATE_UNSPECIFIED | &quot;DEPLOYMENT_STATE_UNSPECIFIED&quot; |
| NOT_INSTALLED | &quot;NOT_INSTALLED&quot; |
| INSTALLED | &quot;INSTALLED&quot; |
| ERROR | &quot;ERROR&quot; |
| PENDING | &quot;PENDING&quot; |



## Enum: ReconcilerManagerEnum

| Name | Value |
|---- | -----|
| DEPLOYMENT_STATE_UNSPECIFIED | &quot;DEPLOYMENT_STATE_UNSPECIFIED&quot; |
| NOT_INSTALLED | &quot;NOT_INSTALLED&quot; |
| INSTALLED | &quot;INSTALLED&quot; |
| ERROR | &quot;ERROR&quot; |
| PENDING | &quot;PENDING&quot; |



## Enum: RootReconcilerEnum

| Name | Value |
|---- | -----|
| DEPLOYMENT_STATE_UNSPECIFIED | &quot;DEPLOYMENT_STATE_UNSPECIFIED&quot; |
| NOT_INSTALLED | &quot;NOT_INSTALLED&quot; |
| INSTALLED | &quot;INSTALLED&quot; |
| ERROR | &quot;ERROR&quot; |
| PENDING | &quot;PENDING&quot; |



## Enum: SyncerEnum

| Name | Value |
|---- | -----|
| DEPLOYMENT_STATE_UNSPECIFIED | &quot;DEPLOYMENT_STATE_UNSPECIFIED&quot; |
| NOT_INSTALLED | &quot;NOT_INSTALLED&quot; |
| INSTALLED | &quot;INSTALLED&quot; |
| ERROR | &quot;ERROR&quot; |
| PENDING | &quot;PENDING&quot; |



