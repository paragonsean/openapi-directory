# ExecutionService.RunConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_arguments** | **[String]** | Command line arguments for the python script file. | [optional] 
**communicator** | **String** | The supported communicators are None, ParameterServer, OpenMpi, and IntelMpi Keep in mind that OpenMpi requires a custom image with OpenMpi installed.  Use ParameterServer or OpenMpi for AmlCompute clusters. Use IntelMpi for distributed training jobs. | [optional] 
**dataReferences** | [**{String: DataReferenceConfiguration}**](DataReferenceConfiguration.md) | All the data sources are made available to the run during execution based on each configuration. | [optional] 
**environment** | [**EnvironmentDefinition**](EnvironmentDefinition.md) |  | [optional] 
**framework** | **String** | The supported frameworks are Python, PySpark, CNTK, TensorFlow, and PyTorch. Use Tensorflow for AmlCompute clusters, and Python for distributed training jobs. | [optional] 
**hdi** | [**HdiConfiguration**](HdiConfiguration.md) |  | [optional] 
**history** | [**HistoryConfiguration**](HistoryConfiguration.md) |  | [optional] 
**jobName** | **String** | This is primarily intended for notebooks to override the default job name.  Defaults to ArgumentVector[0] if not specified. | [optional] 
**maxRunDurationSeconds** | **Number** | Maximum allowed time for the run. The system will attempt to automatically cancel the run if it took longer than this value.  MaxRunDurationSeconds&#x3D;null means infinite duration. | [optional] 
**mpi** | [**MpiConfiguration**](MpiConfiguration.md) |  | [optional] 
**nodeCount** | **Number** | Number of compute nodes to run the job on. Only applies to AMLCompute. | [optional] 
**script** | **String** | The relative path to the python script file. The file path is relative to the source_directory passed to submit run. | [optional] 
**spark** | [**SparkConfiguration**](SparkConfiguration.md) |  | [optional] 
**target** | **String** | Target refers to compute where the job is scheduled for execution. The default target is \&quot;local\&quot; referring to the local machine. | [optional] 
**tensorflow** | [**TensorflowConfiguration**](TensorflowConfiguration.md) |  | [optional] 



## Enum: CommunicatorEnum


* `None` (value: `"None"`)

* `ParameterServer` (value: `"ParameterServer"`)

* `Gloo` (value: `"Gloo"`)

* `Mpi` (value: `"Mpi"`)

* `Nccl` (value: `"Nccl"`)





## Enum: FrameworkEnum


* `Python` (value: `"Python"`)

* `PySpark` (value: `"PySpark"`)

* `Cntk` (value: `"Cntk"`)

* `TensorFlow` (value: `"TensorFlow"`)

* `PyTorch` (value: `"PyTorch"`)




