# CloudDocumentAiApi.GoogleCloudDocumentaiV1beta3Evaluation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allEntitiesMetrics** | [**GoogleCloudDocumentaiV1beta3EvaluationMultiConfidenceMetrics**](GoogleCloudDocumentaiV1beta3EvaluationMultiConfidenceMetrics.md) |  | [optional] 
**createTime** | **String** | The time that the evaluation was created. | [optional] 
**documentCounters** | [**GoogleCloudDocumentaiV1beta3EvaluationCounters**](GoogleCloudDocumentaiV1beta3EvaluationCounters.md) |  | [optional] 
**entityMetrics** | [**{String: GoogleCloudDocumentaiV1beta3EvaluationMultiConfidenceMetrics}**](GoogleCloudDocumentaiV1beta3EvaluationMultiConfidenceMetrics.md) | Metrics across confidence levels, for different entities. | [optional] 
**kmsKeyName** | **String** | The KMS key name used for encryption. | [optional] 
**kmsKeyVersionName** | **String** | The KMS key version with which data is encrypted. | [optional] 
**name** | **String** | The resource name of the evaluation. Format: &#x60;projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processor_version}/evaluations/{evaluation}&#x60; | [optional] 


