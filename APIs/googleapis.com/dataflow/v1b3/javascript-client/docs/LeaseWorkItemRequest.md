# DataflowApi.LeaseWorkItemRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currentWorkerTime** | **String** | The current timestamp at the worker. | [optional] 
**location** | **String** | The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains the WorkItem&#39;s job. | [optional] 
**requestedLeaseDuration** | **String** | The initial lease period. | [optional] 
**unifiedWorkerRequest** | **{String: Object}** | Untranslated bag-of-bytes WorkRequest from UnifiedWorker. | [optional] 
**workItemTypes** | **[String]** | Filter for WorkItem type. | [optional] 
**workerCapabilities** | **[String]** | Worker capabilities. WorkItems might be limited to workers with specific capabilities. | [optional] 
**workerId** | **String** | Identifies the worker leasing work -- typically the ID of the virtual machine running the worker. | [optional] 


