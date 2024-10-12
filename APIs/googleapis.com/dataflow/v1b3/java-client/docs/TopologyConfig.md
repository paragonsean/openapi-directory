

# TopologyConfig

Global topology of the streaming Dataflow job, including all computations and their sharded locations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**computations** | [**List&lt;ComputationTopology&gt;**](ComputationTopology.md) | The computations associated with a streaming Dataflow job. |  [optional] |
|**dataDiskAssignments** | [**List&lt;DataDiskAssignment&gt;**](DataDiskAssignment.md) | The disks assigned to a streaming Dataflow job. |  [optional] |
|**forwardingKeyBits** | **Integer** | The size (in bits) of keys that will be assigned to source messages. |  [optional] |
|**persistentStateVersion** | **Integer** | Version number for persistent state. |  [optional] |
|**userStageToComputationNameMap** | **Map&lt;String, String&gt;** | Maps user stage names to stable computation names. |  [optional] |



