# VertexAiApi.GoogleCloudAiplatformV1beta1NasJob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Time when the NasJob was created. | [optional] [readonly] 
**displayName** | **String** | Required. The display name of the NasJob. The name can be up to 128 characters long and can consist of any UTF-8 characters. | [optional] 
**enableRestrictedImageTraining** | **Boolean** | Optional. Enable a separation of Custom model training and restricted image training for tenant project. | [optional] 
**encryptionSpec** | [**GoogleCloudAiplatformV1beta1EncryptionSpec**](GoogleCloudAiplatformV1beta1EncryptionSpec.md) |  | [optional] 
**endTime** | **String** | Output only. Time when the NasJob entered any of the following states: &#x60;JOB_STATE_SUCCEEDED&#x60;, &#x60;JOB_STATE_FAILED&#x60;, &#x60;JOB_STATE_CANCELLED&#x60;. | [optional] [readonly] 
**error** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  | [optional] 
**labels** | **{String: String}** | The labels with user-defined metadata to organize NasJobs. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. | [optional] 
**name** | **String** | Output only. Resource name of the NasJob. | [optional] [readonly] 
**nasJobOutput** | [**GoogleCloudAiplatformV1beta1NasJobOutput**](GoogleCloudAiplatformV1beta1NasJobOutput.md) |  | [optional] 
**nasJobSpec** | [**GoogleCloudAiplatformV1beta1NasJobSpec**](GoogleCloudAiplatformV1beta1NasJobSpec.md) |  | [optional] 
**startTime** | **String** | Output only. Time when the NasJob for the first time entered the &#x60;JOB_STATE_RUNNING&#x60; state. | [optional] [readonly] 
**state** | **String** | Output only. The detailed state of the job. | [optional] [readonly] 
**updateTime** | **String** | Output only. Time when the NasJob was most recently updated. | [optional] [readonly] 



## Enum: StateEnum


* `UNSPECIFIED` (value: `"JOB_STATE_UNSPECIFIED"`)

* `QUEUED` (value: `"JOB_STATE_QUEUED"`)

* `PENDING` (value: `"JOB_STATE_PENDING"`)

* `RUNNING` (value: `"JOB_STATE_RUNNING"`)

* `SUCCEEDED` (value: `"JOB_STATE_SUCCEEDED"`)

* `FAILED` (value: `"JOB_STATE_FAILED"`)

* `CANCELLING` (value: `"JOB_STATE_CANCELLING"`)

* `CANCELLED` (value: `"JOB_STATE_CANCELLED"`)

* `PAUSED` (value: `"JOB_STATE_PAUSED"`)

* `EXPIRED` (value: `"JOB_STATE_EXPIRED"`)

* `UPDATING` (value: `"JOB_STATE_UPDATING"`)

* `PARTIALLY_SUCCEEDED` (value: `"JOB_STATE_PARTIALLY_SUCCEEDED"`)




