# AirflowApiStable.Pool

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | The description of the pool.  *New in version 2.3.0*  | [optional] 
**name** | **String** | The name of pool. | [optional] 
**occupiedSlots** | **Number** | The number of slots used by running/queued tasks at the moment. | [optional] [readonly] 
**openSlots** | **Number** | The number of free slots at the moment. | [optional] [readonly] 
**queuedSlots** | **Number** | The number of slots used by queued tasks at the moment. | [optional] [readonly] 
**slots** | **Number** | The maximum number of slots that can be assigned to tasks. One job may occupy one or more slots.  | [optional] 
**usedSlots** | **Number** | The number of slots used by running tasks at the moment. | [optional] [readonly] 


