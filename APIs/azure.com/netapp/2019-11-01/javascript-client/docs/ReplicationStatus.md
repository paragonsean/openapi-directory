# MicrosoftNetApp.ReplicationStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errorMessage** | **String** | Displays error message if the replication is in an error state | [optional] 
**healthy** | **Boolean** | Replication health check | [optional] 
**mirrorState** | **String** | The status of the replication | [optional] 
**relationshipStatus** | **String** | Status of the mirror relationship | [optional] 
**totalProgress** | **String** | The progress of the replication | [optional] 



## Enum: MirrorStateEnum


* `Uninitialized` (value: `"Uninitialized"`)

* `Mirrored` (value: `"Mirrored"`)

* `Broken` (value: `"Broken"`)





## Enum: RelationshipStatusEnum


* `Idle` (value: `"Idle"`)

* `Transferring` (value: `"Transferring"`)




