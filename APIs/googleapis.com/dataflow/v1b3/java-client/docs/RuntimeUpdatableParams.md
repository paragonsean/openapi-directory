

# RuntimeUpdatableParams

Additional job parameters that can only be updated during runtime using the projects.jobs.update method. These fields have no effect when specified during job creation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxNumWorkers** | **Integer** | The maximum number of workers to cap autoscaling at. This field is currently only supported for Streaming Engine jobs. |  [optional] |
|**minNumWorkers** | **Integer** | The minimum number of workers to scale down to. This field is currently only supported for Streaming Engine jobs. |  [optional] |
|**workerUtilizationHint** | **Double** | Target worker utilization, compared against the aggregate utilization of the worker pool by autoscaler, to determine upscaling and downscaling when absent other constraints such as backlog. |  [optional] |



