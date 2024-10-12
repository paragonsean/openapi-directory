

# WorkloadsConfig

The Kubernetes workloads configuration for GKE cluster associated with the Cloud Composer environment. Supported for Cloud Composer environments in versions composer-2.*.*-airflow-*.*.* and newer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dagProcessor** | [**DagProcessorResource**](DagProcessorResource.md) |  |  [optional] |
|**scheduler** | [**SchedulerResource**](SchedulerResource.md) |  |  [optional] |
|**triggerer** | [**TriggererResource**](TriggererResource.md) |  |  [optional] |
|**webServer** | [**WebServerResource**](WebServerResource.md) |  |  [optional] |
|**worker** | [**WorkerResource**](WorkerResource.md) |  |  [optional] |



