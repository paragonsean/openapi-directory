

# HybridRunbookWorkerGroup

Definition of hybrid runbook worker group.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**credential** | [**RunAsCredentialAssociationProperty**](RunAsCredentialAssociationProperty.md) |  |  [optional] |
|**groupType** | [**GroupTypeEnum**](#GroupTypeEnum) | Type of the HybridWorkerGroup. |  [optional] |
|**hybridRunbookWorkers** | [**List&lt;HybridRunbookWorker&gt;**](HybridRunbookWorker.md) | Gets or sets the list of hybrid runbook workers. |  [optional] |
|**id** | **String** | Gets or sets the id of the resource. |  [optional] |
|**name** | **String** | Gets or sets the name of the group. |  [optional] |



## Enum: GroupTypeEnum

| Name | Value |
|---- | -----|
| USER | &quot;User&quot; |
| SYSTEM | &quot;System&quot; |



