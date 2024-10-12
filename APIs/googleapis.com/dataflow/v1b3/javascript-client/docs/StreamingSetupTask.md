# DataflowApi.StreamingSetupTask

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drain** | **Boolean** | The user has requested drain. | [optional] 
**receiveWorkPort** | **Number** | The TCP port on which the worker should listen for messages from other streaming computation workers. | [optional] 
**snapshotConfig** | [**StreamingApplianceSnapshotConfig**](StreamingApplianceSnapshotConfig.md) |  | [optional] 
**streamingComputationTopology** | [**TopologyConfig**](TopologyConfig.md) |  | [optional] 
**workerHarnessPort** | **Number** | The TCP port used by the worker to communicate with the Dataflow worker harness. | [optional] 


