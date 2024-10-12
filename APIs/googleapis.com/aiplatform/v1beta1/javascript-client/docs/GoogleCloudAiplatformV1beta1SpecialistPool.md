# VertexAiApi.GoogleCloudAiplatformV1beta1SpecialistPool

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | Required. The user-defined name of the SpecialistPool. The name can be up to 128 characters long and can consist of any UTF-8 characters. This field should be unique on project-level. | [optional] 
**name** | **String** | Required. The resource name of the SpecialistPool. | [optional] 
**pendingDataLabelingJobs** | **[String]** | Output only. The resource name of the pending data labeling jobs. | [optional] [readonly] 
**specialistManagerEmails** | **[String]** | The email addresses of the managers in the SpecialistPool. | [optional] 
**specialistManagersCount** | **Number** | Output only. The number of managers in this SpecialistPool. | [optional] [readonly] 
**specialistWorkerEmails** | **[String]** | The email addresses of workers in the SpecialistPool. | [optional] 


