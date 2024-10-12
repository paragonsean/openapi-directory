# DataflowApi.RuntimeUpdatableParams

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxNumWorkers** | **Number** | The maximum number of workers to cap autoscaling at. This field is currently only supported for Streaming Engine jobs. | [optional] 
**minNumWorkers** | **Number** | The minimum number of workers to scale down to. This field is currently only supported for Streaming Engine jobs. | [optional] 
**workerUtilizationHint** | **Number** | Target worker utilization, compared against the aggregate utilization of the worker pool by autoscaler, to determine upscaling and downscaling when absent other constraints such as backlog. | [optional] 


