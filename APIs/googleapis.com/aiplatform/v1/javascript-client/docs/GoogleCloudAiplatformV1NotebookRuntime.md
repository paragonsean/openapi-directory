# VertexAiApi.GoogleCloudAiplatformV1NotebookRuntime

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Timestamp when this NotebookRuntime was created. | [optional] [readonly] 
**description** | **String** | The description of the NotebookRuntime. | [optional] 
**displayName** | **String** | Required. The display name of the NotebookRuntime. The name can be up to 128 characters long and can consist of any UTF-8 characters. | [optional] 
**expirationTime** | **String** | Output only. Timestamp when this NotebookRuntime will be expired: 1. System Predefined NotebookRuntime: 24 hours after creation. After expiration, system predifined runtime will be deleted. 2. User created NotebookRuntime: 6 months after last upgrade. After expiration, user created runtime will be stopped and allowed for upgrade. | [optional] [readonly] 
**healthState** | **String** | Output only. The health state of the NotebookRuntime. | [optional] [readonly] 
**isUpgradable** | **Boolean** | Output only. Whether NotebookRuntime is upgradable. | [optional] [readonly] 
**labels** | **{String: String}** | The labels with user-defined metadata to organize your NotebookRuntime. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one NotebookRuntime (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with \&quot;aiplatform.googleapis.com/\&quot; and are immutable. Following system labels exist for NotebookRuntime: * \&quot;aiplatform.googleapis.com/notebook_runtime_gce_instance_id\&quot;: output only, its value is the Compute Engine instance id. * \&quot;aiplatform.googleapis.com/colab_enterprise_entry_service\&quot;: its value is either \&quot;bigquery\&quot; or \&quot;vertex\&quot;; if absent, it should be \&quot;vertex\&quot;. This is to describe the entry service, either BigQuery or Vertex. | [optional] 
**name** | **String** | Output only. The resource name of the NotebookRuntime. | [optional] [readonly] 
**networkTags** | **[String]** | Optional. The Compute Engine tags to add to runtime (see [Tagging instances](https://cloud.google.com/vpc/docs/add-remove-network-tags)). | [optional] 
**notebookRuntimeTemplateRef** | [**GoogleCloudAiplatformV1NotebookRuntimeTemplateRef**](GoogleCloudAiplatformV1NotebookRuntimeTemplateRef.md) |  | [optional] 
**notebookRuntimeType** | **String** | Output only. The type of the notebook runtime. | [optional] [readonly] 
**proxyUri** | **String** | Output only. The proxy endpoint used to access the NotebookRuntime. | [optional] [readonly] 
**reservationAffinity** | [**GoogleCloudAiplatformV1NotebookReservationAffinity**](GoogleCloudAiplatformV1NotebookReservationAffinity.md) |  | [optional] 
**runtimeState** | **String** | Output only. The runtime (instance) state of the NotebookRuntime. | [optional] [readonly] 
**runtimeUser** | **String** | Required. The user email of the NotebookRuntime. | [optional] 
**serviceAccount** | **String** | Output only. The service account that the NotebookRuntime workload runs as. | [optional] [readonly] 
**updateTime** | **String** | Output only. Timestamp when this NotebookRuntime was most recently updated. | [optional] [readonly] 
**version** | **String** | Output only. The VM os image version of NotebookRuntime. | [optional] [readonly] 



## Enum: HealthStateEnum


* `HEALTH_STATE_UNSPECIFIED` (value: `"HEALTH_STATE_UNSPECIFIED"`)

* `HEALTHY` (value: `"HEALTHY"`)

* `UNHEALTHY` (value: `"UNHEALTHY"`)





## Enum: NotebookRuntimeTypeEnum


* `NOTEBOOK_RUNTIME_TYPE_UNSPECIFIED` (value: `"NOTEBOOK_RUNTIME_TYPE_UNSPECIFIED"`)

* `USER_DEFINED` (value: `"USER_DEFINED"`)

* `ONE_CLICK` (value: `"ONE_CLICK"`)





## Enum: RuntimeStateEnum


* `RUNTIME_STATE_UNSPECIFIED` (value: `"RUNTIME_STATE_UNSPECIFIED"`)

* `RUNNING` (value: `"RUNNING"`)

* `BEING_STARTED` (value: `"BEING_STARTED"`)

* `BEING_STOPPED` (value: `"BEING_STOPPED"`)

* `STOPPED` (value: `"STOPPED"`)

* `BEING_UPGRADED` (value: `"BEING_UPGRADED"`)




