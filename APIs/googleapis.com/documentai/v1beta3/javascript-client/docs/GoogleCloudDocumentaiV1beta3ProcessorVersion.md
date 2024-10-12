# CloudDocumentAiApi.GoogleCloudDocumentaiV1beta3ProcessorVersion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | The time the processor version was created. | [optional] 
**deprecationInfo** | [**GoogleCloudDocumentaiV1beta3ProcessorVersionDeprecationInfo**](GoogleCloudDocumentaiV1beta3ProcessorVersionDeprecationInfo.md) |  | [optional] 
**displayName** | **String** | The display name of the processor version. | [optional] 
**documentSchema** | [**GoogleCloudDocumentaiV1beta3DocumentSchema**](GoogleCloudDocumentaiV1beta3DocumentSchema.md) |  | [optional] 
**googleManaged** | **Boolean** | Output only. Denotes that this &#x60;ProcessorVersion&#x60; is managed by Google. | [optional] [readonly] 
**kmsKeyName** | **String** | The KMS key name used for encryption. | [optional] 
**kmsKeyVersionName** | **String** | The KMS key version with which data is encrypted. | [optional] 
**latestEvaluation** | [**GoogleCloudDocumentaiV1beta3EvaluationReference**](GoogleCloudDocumentaiV1beta3EvaluationReference.md) |  | [optional] 
**modelType** | **String** | Output only. The model type of this processor version. | [optional] [readonly] 
**name** | **String** | The resource name of the processor version. Format: &#x60;projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processor_version}&#x60; | [optional] 
**state** | **String** | The state of the processor version. | [optional] 



## Enum: ModelTypeEnum


* `UNSPECIFIED` (value: `"MODEL_TYPE_UNSPECIFIED"`)

* `GENERATIVE` (value: `"MODEL_TYPE_GENERATIVE"`)

* `CUSTOM` (value: `"MODEL_TYPE_CUSTOM"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `DEPLOYED` (value: `"DEPLOYED"`)

* `DEPLOYING` (value: `"DEPLOYING"`)

* `UNDEPLOYED` (value: `"UNDEPLOYED"`)

* `UNDEPLOYING` (value: `"UNDEPLOYING"`)

* `CREATING` (value: `"CREATING"`)

* `DELETING` (value: `"DELETING"`)

* `FAILED` (value: `"FAILED"`)

* `IMPORTING` (value: `"IMPORTING"`)




