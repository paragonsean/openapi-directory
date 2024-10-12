

# ClearTaskInstances


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dagRunId** | **String** | The DagRun ID for this task instance |  [optional] |
|**dryRun** | **Boolean** | If set, don&#39;t actually run this operation. The response will contain a list of task instances planned to be cleaned, but not modified in any way.  |  [optional] |
|**endDate** | **String** | The maximum execution date to clear. |  [optional] |
|**includeDownstream** | **Boolean** | If set to true, downstream tasks are also affected. |  [optional] |
|**includeFuture** | **Boolean** | If set to True, also tasks from future DAG Runs are affected. |  [optional] |
|**includeParentdag** | **Boolean** | Clear tasks in the parent dag of the subdag. |  [optional] |
|**includePast** | **Boolean** | If set to True, also tasks from past DAG Runs are affected. |  [optional] |
|**includeSubdags** | **Boolean** | Clear tasks in subdags and clear external tasks indicated by ExternalTaskMarker. |  [optional] |
|**includeUpstream** | **Boolean** | If set to true, upstream tasks are also affected. |  [optional] |
|**onlyFailed** | **Boolean** | Only clear failed tasks. |  [optional] |
|**onlyRunning** | **Boolean** | Only clear running tasks. |  [optional] |
|**resetDagRuns** | **Boolean** | Set state of DAG runs to RUNNING. |  [optional] |
|**startDate** | **String** | The minimum execution date to clear. |  [optional] |
|**taskIds** | **List&lt;String&gt;** | A list of task ids to clear.  *New in version 2.1.0*  |  [optional] |



