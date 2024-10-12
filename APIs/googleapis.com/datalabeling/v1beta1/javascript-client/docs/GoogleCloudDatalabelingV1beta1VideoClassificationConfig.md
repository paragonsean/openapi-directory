# DataLabelingApi.GoogleCloudDatalabelingV1beta1VideoClassificationConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotationSpecSetConfigs** | [**[GoogleCloudDatalabelingV1beta1AnnotationSpecSetConfig]**](GoogleCloudDatalabelingV1beta1AnnotationSpecSetConfig.md) | Required. The list of annotation spec set configs. Since watching a video clip takes much longer time than an image, we support label with multiple AnnotationSpecSet at the same time. Labels in each AnnotationSpecSet will be shown in a group to contributors. Contributors can select one or more (depending on whether to allow multi label) from each group. | [optional] 
**applyShotDetection** | **Boolean** | Optional. Option to apply shot detection on the video. | [optional] 


