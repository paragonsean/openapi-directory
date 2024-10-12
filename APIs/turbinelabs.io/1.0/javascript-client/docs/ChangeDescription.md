# TurbineLabsApi.ChangeDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actorKey** | **String** | The user who made the change. | [optional] 
**at** | **Number** | When the change took place in milliseconds since the Unix epoch. | [optional] 
**comment** | **String** | A description of the change. | [optional] 
**diffs** | [**[ChangeEntry]**](ChangeEntry.md) | A collection of attribute updates that compose this change. | [optional] 
**txn** | **String** | A unique identifier for all this transaction. It is shared by all attribute updates within a change.  | [optional] 


