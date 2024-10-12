# ServiceFabricClientApis.StatefulServiceUpdateDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minReplicaSetSize** | **Number** | The minimum replica set size as a number. | [optional] 
**quorumLossWaitDurationSeconds** | **String** | The maximum duration, in seconds, for which a partition is allowed to be in a state of quorum loss. | [optional] 
**replicaRestartWaitDurationSeconds** | **String** | The duration, in seconds, between when a replica goes down and when a new replica is created. | [optional] 
**servicePlacementTimeLimitSeconds** | **String** | The duration for which replicas can stay InBuild before reporting that build is stuck. | [optional] 
**standByReplicaKeepDurationSeconds** | **String** | The definition on how long StandBy replicas should be maintained before being removed. | [optional] 
**targetReplicaSetSize** | **Number** | The target replica set size as a number. | [optional] 


