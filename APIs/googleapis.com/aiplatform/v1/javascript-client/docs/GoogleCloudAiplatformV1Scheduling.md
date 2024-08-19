# VertexAiApi.GoogleCloudAiplatformV1Scheduling

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disableRetries** | **Boolean** | Optional. Indicates if the job should retry for internal errors after the job starts running. If true, overrides &#x60;Scheduling.restart_job_on_worker_restart&#x60; to false. | [optional] 
**restartJobOnWorkerRestart** | **Boolean** | Restarts the entire CustomJob if a worker gets restarted. This feature can be used by distributed training jobs that are not resilient to workers leaving and joining a job. | [optional] 
**timeout** | **String** | The maximum job running time. The default is 7 days. | [optional] 


