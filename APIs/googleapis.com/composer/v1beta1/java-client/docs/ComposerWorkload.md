

# ComposerWorkload

Information about a single workload.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Name of a workload. |  [optional] |
|**status** | [**ComposerWorkloadStatus**](ComposerWorkloadStatus.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of a workload. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| COMPOSER_WORKLOAD_TYPE_UNSPECIFIED | &quot;COMPOSER_WORKLOAD_TYPE_UNSPECIFIED&quot; |
| CELERY_WORKER | &quot;CELERY_WORKER&quot; |
| KUBERNETES_WORKER | &quot;KUBERNETES_WORKER&quot; |
| KUBERNETES_OPERATOR_POD | &quot;KUBERNETES_OPERATOR_POD&quot; |
| SCHEDULER | &quot;SCHEDULER&quot; |
| DAG_PROCESSOR | &quot;DAG_PROCESSOR&quot; |
| TRIGGERER | &quot;TRIGGERER&quot; |
| WEB_SERVER | &quot;WEB_SERVER&quot; |
| REDIS | &quot;REDIS&quot; |



