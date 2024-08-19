# VertexAiApi.GoogleCloudAiplatformV1NotebookRuntimeTemplate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Timestamp when this NotebookRuntimeTemplate was created. | [optional] [readonly] 
**dataPersistentDiskSpec** | [**GoogleCloudAiplatformV1PersistentDiskSpec**](GoogleCloudAiplatformV1PersistentDiskSpec.md) |  | [optional] 
**description** | **String** | The description of the NotebookRuntimeTemplate. | [optional] 
**displayName** | **String** | Required. The display name of the NotebookRuntimeTemplate. The name can be up to 128 characters long and can consist of any UTF-8 characters. | [optional] 
**etag** | **String** | Used to perform consistent read-modify-write updates. If not set, a blind \&quot;overwrite\&quot; update happens. | [optional] 
**eucConfig** | [**GoogleCloudAiplatformV1NotebookEucConfig**](GoogleCloudAiplatformV1NotebookEucConfig.md) |  | [optional] 
**idleShutdownConfig** | [**GoogleCloudAiplatformV1NotebookIdleShutdownConfig**](GoogleCloudAiplatformV1NotebookIdleShutdownConfig.md) |  | [optional] 
**isDefault** | **Boolean** | Output only. The default template to use if not specified. | [optional] [readonly] 
**labels** | **{String: String}** | The labels with user-defined metadata to organize the NotebookRuntimeTemplates. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. | [optional] 
**machineSpec** | [**GoogleCloudAiplatformV1MachineSpec**](GoogleCloudAiplatformV1MachineSpec.md) |  | [optional] 
**name** | **String** | Output only. The resource name of the NotebookRuntimeTemplate. | [optional] [readonly] 
**networkSpec** | [**GoogleCloudAiplatformV1NetworkSpec**](GoogleCloudAiplatformV1NetworkSpec.md) |  | [optional] 
**networkTags** | **[String]** | Optional. The Compute Engine tags to add to runtime (see [Tagging instances](https://cloud.google.com/vpc/docs/add-remove-network-tags)). | [optional] 
**notebookRuntimeType** | **String** | Optional. Immutable. The type of the notebook runtime template. | [optional] 
**reservationAffinity** | [**GoogleCloudAiplatformV1NotebookReservationAffinity**](GoogleCloudAiplatformV1NotebookReservationAffinity.md) |  | [optional] 
**serviceAccount** | **String** | The service account that the runtime workload runs as. You can use any service account within the same project, but you must have the service account user permission to use the instance. If not specified, the [Compute Engine default service account](https://cloud.google.com/compute/docs/access/service-accounts#default_service_account) is used. | [optional] 
**shieldedVmConfig** | [**GoogleCloudAiplatformV1ShieldedVmConfig**](GoogleCloudAiplatformV1ShieldedVmConfig.md) |  | [optional] 
**updateTime** | **String** | Output only. Timestamp when this NotebookRuntimeTemplate was most recently updated. | [optional] [readonly] 



## Enum: NotebookRuntimeTypeEnum


* `NOTEBOOK_RUNTIME_TYPE_UNSPECIFIED` (value: `"NOTEBOOK_RUNTIME_TYPE_UNSPECIFIED"`)

* `USER_DEFINED` (value: `"USER_DEFINED"`)

* `ONE_CLICK` (value: `"ONE_CLICK"`)




