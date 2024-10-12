# ServiceFabricClientApis.StatefulServiceDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flags** | **Number** | Flags indicating whether other properties are set. Each of the associated properties corresponds to a flag, specified below, which, if set, indicate that the property is specified. This property can be a combination of those flags obtained using bitwise &#39;OR&#39; operator. For example, if the provided value is 6 then the flags for QuorumLossWaitDuration (2) and StandByReplicaKeepDuration(4) are set.  - None - Does not indicate any other properties are set. The value is zero. - ReplicaRestartWaitDuration - Indicates the ReplicaRestartWaitDuration property is set. The value is 1. - QuorumLossWaitDuration - Indicates the QuorumLossWaitDuration property is set. The value is 2. - StandByReplicaKeepDuration - Indicates the StandByReplicaKeepDuration property is set. The value is 4.  | [optional] 
**hasPersistedState** | **Boolean** | A flag indicating whether this is a persistent service which stores states on the local disk. If it is then the value of this property is true, if not it is false. | 
**minReplicaSetSize** | **Number** | The minimum replica set size as a number. | 
**quorumLossWaitDurationSeconds** | **Number** | The maximum duration, in seconds, for which a partition is allowed to be in a state of quorum loss. | [optional] 
**replicaRestartWaitDurationSeconds** | **Number** | The duration, in seconds, between when a replica goes down and when a new replica is created. | [optional] 
**standByReplicaKeepDurationSeconds** | **Number** | The definition on how long StandBy replicas should be maintained before being removed. | [optional] 
**targetReplicaSetSize** | **Number** | The target replica set size as a number. | 


