

# GoogleCloudDatalabelingV1beta1VideoClassificationConfig

Config for video classification human labeling task. Currently two types of video classification are supported: 1. Assign labels on the entire video. 2. Split the video into multiple video clips based on camera shot, and assign labels on each video clip.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotationSpecSetConfigs** | [**List&lt;GoogleCloudDatalabelingV1beta1AnnotationSpecSetConfig&gt;**](GoogleCloudDatalabelingV1beta1AnnotationSpecSetConfig.md) | Required. The list of annotation spec set configs. Since watching a video clip takes much longer time than an image, we support label with multiple AnnotationSpecSet at the same time. Labels in each AnnotationSpecSet will be shown in a group to contributors. Contributors can select one or more (depending on whether to allow multi label) from each group. |  [optional] |
|**applyShotDetection** | **Boolean** | Optional. Option to apply shot detection on the video. |  [optional] |



