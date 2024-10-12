

# RecoveryPlanHyperVReplicaAzureFailbackInput

Recovery plan HVR Azure failback input.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSyncOption** | [**DataSyncOptionEnum**](#DataSyncOptionEnum) | The data sync option. |  |
|**recoveryVmCreationOption** | [**RecoveryVmCreationOptionEnum**](#RecoveryVmCreationOptionEnum) | The ALR option. |  |



## Enum: DataSyncOptionEnum

| Name | Value |
|---- | -----|
| FOR_DOWN_TIME | &quot;ForDownTime&quot; |
| FOR_SYNCHRONIZATION | &quot;ForSynchronization&quot; |



## Enum: RecoveryVmCreationOptionEnum

| Name | Value |
|---- | -----|
| CREATE_VM_IF_NOT_FOUND | &quot;CreateVmIfNotFound&quot; |
| NO_ACTION | &quot;NoAction&quot; |



