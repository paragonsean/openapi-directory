# ServiceFabricClientApis.ChaosParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chaosTargetFilter** | [**ChaosTargetFilter**](ChaosTargetFilter.md) |  | [optional] 
**clusterHealthPolicy** | [**ClusterHealthPolicy**](ClusterHealthPolicy.md) |  | [optional] 
**context** | [**ChaosContext**](ChaosContext.md) |  | [optional] 
**enableMoveReplicaFaults** | **Boolean** | Enables or disables the move primary and move secondary faults. | [optional] [default to true]
**maxClusterStabilizationTimeoutInSeconds** | **Number** | The maximum amount of time to wait for all cluster entities to become stable and healthy. Chaos executes in iterations and at the start of each iteration it validates the health of cluster entities. During validation if a cluster entity is not stable and healthy within MaxClusterStabilizationTimeoutInSeconds, Chaos generates a validation failed event. | [optional] [default to 60]
**maxConcurrentFaults** | **Number** | MaxConcurrentFaults is the maximum number of concurrent faults induced per iteration. Chaos executes in iterations and two consecutive iterations are separated by a validation phase. The higher the concurrency, the more aggressive the injection of faults, leading to inducing more complex series of states to uncover bugs. The recommendation is to start with a value of 2 or 3 and to exercise caution while moving up. | [optional] [default to 1]
**timeToRunInSeconds** | **String** | Total time (in seconds) for which Chaos will run before automatically stopping. The maximum allowed value is 4,294,967,295 (System.UInt32.MaxValue). | [optional] [default to &#39;4294967295&#39;]
**waitTimeBetweenFaultsInSeconds** | **Number** | Wait time (in seconds) between consecutive faults within a single iteration. The larger the value, the lower the overlapping between faults and the simpler the sequence of state transitions that the cluster goes through. The recommendation is to start with a value between 1 and 5 and exercise caution while moving up. | [optional] [default to 20]
**waitTimeBetweenIterationsInSeconds** | **Number** | Time-separation (in seconds) between two consecutive iterations of Chaos. The larger the value, the lower the fault injection rate. | [optional] [default to 30]


