

# WorkerResource

Configuration for resources used by Airflow workers.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cpu** | **Float** | Optional. CPU request and limit for a single Airflow worker replica. |  [optional] |
|**maxCount** | **Integer** | Optional. Maximum number of workers for autoscaling. |  [optional] |
|**memoryGb** | **Float** | Optional. Memory (GB) request and limit for a single Airflow worker replica. |  [optional] |
|**minCount** | **Integer** | Optional. Minimum number of workers for autoscaling. |  [optional] |
|**storageGb** | **Float** | Optional. Storage (GB) request and limit for a single Airflow worker replica. |  [optional] |



