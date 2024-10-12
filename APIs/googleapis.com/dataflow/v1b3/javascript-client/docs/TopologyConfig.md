# DataflowApi.TopologyConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**computations** | [**[ComputationTopology]**](ComputationTopology.md) | The computations associated with a streaming Dataflow job. | [optional] 
**dataDiskAssignments** | [**[DataDiskAssignment]**](DataDiskAssignment.md) | The disks assigned to a streaming Dataflow job. | [optional] 
**forwardingKeyBits** | **Number** | The size (in bits) of keys that will be assigned to source messages. | [optional] 
**persistentStateVersion** | **Number** | Version number for persistent state. | [optional] 
**userStageToComputationNameMap** | **{String: String}** | Maps user stage names to stable computation names. | [optional] 


