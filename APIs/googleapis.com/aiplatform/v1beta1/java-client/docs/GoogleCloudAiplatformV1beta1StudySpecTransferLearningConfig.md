

# GoogleCloudAiplatformV1beta1StudySpecTransferLearningConfig

This contains flag for manually disabling transfer learning for a study. The names of prior studies being used for transfer learning (if any) are also listed here.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**disableTransferLearning** | **Boolean** | Flag to to manually prevent vizier from using transfer learning on a new study. Otherwise, vizier will automatically determine whether or not to use transfer learning. |  [optional] |
|**priorStudyNames** | **List&lt;String&gt;** | Output only. Names of previously completed studies |  [optional] [readonly] |



