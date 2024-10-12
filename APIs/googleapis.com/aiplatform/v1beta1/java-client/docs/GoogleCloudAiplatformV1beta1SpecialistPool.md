

# GoogleCloudAiplatformV1beta1SpecialistPool

SpecialistPool represents customers' own workforce to work on their data labeling jobs. It includes a group of specialist managers and workers. Managers are responsible for managing the workers in this pool as well as customers' data labeling jobs associated with this pool. Customers create specialist pool as well as start data labeling jobs on Cloud, managers and workers handle the jobs using CrowdCompute console.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | Required. The user-defined name of the SpecialistPool. The name can be up to 128 characters long and can consist of any UTF-8 characters. This field should be unique on project-level. |  [optional] |
|**name** | **String** | Required. The resource name of the SpecialistPool. |  [optional] |
|**pendingDataLabelingJobs** | **List&lt;String&gt;** | Output only. The resource name of the pending data labeling jobs. |  [optional] [readonly] |
|**specialistManagerEmails** | **List&lt;String&gt;** | The email addresses of the managers in the SpecialistPool. |  [optional] |
|**specialistManagersCount** | **Integer** | Output only. The number of managers in this SpecialistPool. |  [optional] [readonly] |
|**specialistWorkerEmails** | **List&lt;String&gt;** | The email addresses of workers in the SpecialistPool. |  [optional] |



