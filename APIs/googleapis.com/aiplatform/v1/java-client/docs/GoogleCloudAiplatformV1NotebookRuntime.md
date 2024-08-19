

# GoogleCloudAiplatformV1NotebookRuntime

A runtime is a virtual machine allocated to a particular user for a particular Notebook file on temporary basis with lifetime limited to 24 hours.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Timestamp when this NotebookRuntime was created. |  [optional] [readonly] |
|**description** | **String** | The description of the NotebookRuntime. |  [optional] |
|**displayName** | **String** | Required. The display name of the NotebookRuntime. The name can be up to 128 characters long and can consist of any UTF-8 characters. |  [optional] |
|**expirationTime** | **String** | Output only. Timestamp when this NotebookRuntime will be expired: 1. System Predefined NotebookRuntime: 24 hours after creation. After expiration, system predifined runtime will be deleted. 2. User created NotebookRuntime: 6 months after last upgrade. After expiration, user created runtime will be stopped and allowed for upgrade. |  [optional] [readonly] |
|**healthState** | [**HealthStateEnum**](#HealthStateEnum) | Output only. The health state of the NotebookRuntime. |  [optional] [readonly] |
|**isUpgradable** | **Boolean** | Output only. Whether NotebookRuntime is upgradable. |  [optional] [readonly] |
|**labels** | **Map&lt;String, String&gt;** | The labels with user-defined metadata to organize your NotebookRuntime. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one NotebookRuntime (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with \&quot;aiplatform.googleapis.com/\&quot; and are immutable. Following system labels exist for NotebookRuntime: * \&quot;aiplatform.googleapis.com/notebook_runtime_gce_instance_id\&quot;: output only, its value is the Compute Engine instance id. * \&quot;aiplatform.googleapis.com/colab_enterprise_entry_service\&quot;: its value is either \&quot;bigquery\&quot; or \&quot;vertex\&quot;; if absent, it should be \&quot;vertex\&quot;. This is to describe the entry service, either BigQuery or Vertex. |  [optional] |
|**name** | **String** | Output only. The resource name of the NotebookRuntime. |  [optional] [readonly] |
|**networkTags** | **List&lt;String&gt;** | Optional. The Compute Engine tags to add to runtime (see [Tagging instances](https://cloud.google.com/vpc/docs/add-remove-network-tags)). |  [optional] |
|**notebookRuntimeTemplateRef** | [**GoogleCloudAiplatformV1NotebookRuntimeTemplateRef**](GoogleCloudAiplatformV1NotebookRuntimeTemplateRef.md) |  |  [optional] |
|**notebookRuntimeType** | [**NotebookRuntimeTypeEnum**](#NotebookRuntimeTypeEnum) | Output only. The type of the notebook runtime. |  [optional] [readonly] |
|**proxyUri** | **String** | Output only. The proxy endpoint used to access the NotebookRuntime. |  [optional] [readonly] |
|**reservationAffinity** | [**GoogleCloudAiplatformV1NotebookReservationAffinity**](GoogleCloudAiplatformV1NotebookReservationAffinity.md) |  |  [optional] |
|**runtimeState** | [**RuntimeStateEnum**](#RuntimeStateEnum) | Output only. The runtime (instance) state of the NotebookRuntime. |  [optional] [readonly] |
|**runtimeUser** | **String** | Required. The user email of the NotebookRuntime. |  [optional] |
|**serviceAccount** | **String** | Output only. The service account that the NotebookRuntime workload runs as. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. Timestamp when this NotebookRuntime was most recently updated. |  [optional] [readonly] |
|**version** | **String** | Output only. The VM os image version of NotebookRuntime. |  [optional] [readonly] |



## Enum: HealthStateEnum

| Name | Value |
|---- | -----|
| HEALTH_STATE_UNSPECIFIED | &quot;HEALTH_STATE_UNSPECIFIED&quot; |
| HEALTHY | &quot;HEALTHY&quot; |
| UNHEALTHY | &quot;UNHEALTHY&quot; |



## Enum: NotebookRuntimeTypeEnum

| Name | Value |
|---- | -----|
| NOTEBOOK_RUNTIME_TYPE_UNSPECIFIED | &quot;NOTEBOOK_RUNTIME_TYPE_UNSPECIFIED&quot; |
| USER_DEFINED | &quot;USER_DEFINED&quot; |
| ONE_CLICK | &quot;ONE_CLICK&quot; |



## Enum: RuntimeStateEnum

| Name | Value |
|---- | -----|
| RUNTIME_STATE_UNSPECIFIED | &quot;RUNTIME_STATE_UNSPECIFIED&quot; |
| RUNNING | &quot;RUNNING&quot; |
| BEING_STARTED | &quot;BEING_STARTED&quot; |
| BEING_STOPPED | &quot;BEING_STOPPED&quot; |
| STOPPED | &quot;STOPPED&quot; |
| BEING_UPGRADED | &quot;BEING_UPGRADED&quot; |



