# CloudComposerApi.ComposerWorkload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Name of a workload. | [optional] 
**status** | [**ComposerWorkloadStatus**](ComposerWorkloadStatus.md) |  | [optional] 
**type** | **String** | Type of a workload. | [optional] 



## Enum: TypeEnum


* `COMPOSER_WORKLOAD_TYPE_UNSPECIFIED` (value: `"COMPOSER_WORKLOAD_TYPE_UNSPECIFIED"`)

* `CELERY_WORKER` (value: `"CELERY_WORKER"`)

* `KUBERNETES_WORKER` (value: `"KUBERNETES_WORKER"`)

* `KUBERNETES_OPERATOR_POD` (value: `"KUBERNETES_OPERATOR_POD"`)

* `SCHEDULER` (value: `"SCHEDULER"`)

* `DAG_PROCESSOR` (value: `"DAG_PROCESSOR"`)

* `TRIGGERER` (value: `"TRIGGERER"`)

* `WEB_SERVER` (value: `"WEB_SERVER"`)

* `REDIS` (value: `"REDIS"`)




