

# GoogleCloudDocumentaiV1beta3ProcessorVersion

A processor version is an implementation of a processor. Each processor can have multiple versions, pretrained by Google internally or uptrained by the customer. A processor can only have one default version at a time. Its document-processing behavior is defined by that version.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | The time the processor version was created. |  [optional] |
|**deprecationInfo** | [**GoogleCloudDocumentaiV1beta3ProcessorVersionDeprecationInfo**](GoogleCloudDocumentaiV1beta3ProcessorVersionDeprecationInfo.md) |  |  [optional] |
|**displayName** | **String** | The display name of the processor version. |  [optional] |
|**documentSchema** | [**GoogleCloudDocumentaiV1beta3DocumentSchema**](GoogleCloudDocumentaiV1beta3DocumentSchema.md) |  |  [optional] |
|**googleManaged** | **Boolean** | Output only. Denotes that this &#x60;ProcessorVersion&#x60; is managed by Google. |  [optional] [readonly] |
|**kmsKeyName** | **String** | The KMS key name used for encryption. |  [optional] |
|**kmsKeyVersionName** | **String** | The KMS key version with which data is encrypted. |  [optional] |
|**latestEvaluation** | [**GoogleCloudDocumentaiV1beta3EvaluationReference**](GoogleCloudDocumentaiV1beta3EvaluationReference.md) |  |  [optional] |
|**modelType** | [**ModelTypeEnum**](#ModelTypeEnum) | Output only. The model type of this processor version. |  [optional] [readonly] |
|**name** | **String** | The resource name of the processor version. Format: &#x60;projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processor_version}&#x60; |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of the processor version. |  [optional] |



## Enum: ModelTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;MODEL_TYPE_UNSPECIFIED&quot; |
| GENERATIVE | &quot;MODEL_TYPE_GENERATIVE&quot; |
| CUSTOM | &quot;MODEL_TYPE_CUSTOM&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| DEPLOYED | &quot;DEPLOYED&quot; |
| DEPLOYING | &quot;DEPLOYING&quot; |
| UNDEPLOYED | &quot;UNDEPLOYED&quot; |
| UNDEPLOYING | &quot;UNDEPLOYING&quot; |
| CREATING | &quot;CREATING&quot; |
| DELETING | &quot;DELETING&quot; |
| FAILED | &quot;FAILED&quot; |
| IMPORTING | &quot;IMPORTING&quot; |



