

# DagProcessorResource

Configuration for resources used by Airflow DAG processors.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**count** | **Integer** | Optional. The number of DAG processors. If not provided or set to 0, a single DAG processor instance will be created. |  [optional] |
|**cpu** | **Float** | Optional. CPU request and limit for a single Airflow DAG processor replica. |  [optional] |
|**memoryGb** | **Float** | Optional. Memory (GB) request and limit for a single Airflow DAG processor replica. |  [optional] |
|**storageGb** | **Float** | Optional. Storage (GB) request and limit for a single Airflow DAG processor replica. |  [optional] |



