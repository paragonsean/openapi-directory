

# GoogleCloudAiplatformV1beta1NotebookIdleShutdownConfig

The idle shutdown configuration of NotebookRuntimeTemplate, which contains the idle_timeout as required field.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**idleShutdownDisabled** | **Boolean** | Whether Idle Shutdown is disabled in this NotebookRuntimeTemplate. |  [optional] |
|**idleTimeout** | **String** | Required. Duration is accurate to the second. In Notebook, Idle Timeout is accurate to minute so the range of idle_timeout (second) is: 10 * 60 ~ 1440 * 60. |  [optional] |



