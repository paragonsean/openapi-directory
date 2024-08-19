

# GoogleCloudAiplatformV1beta1SavedQuery

A SavedQuery is a view of the dataset. It references a subset of annotations by problem type and filters.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotationFilter** | **String** | Output only. Filters on the Annotations in the dataset. |  [optional] [readonly] |
|**annotationSpecCount** | **Integer** | Output only. Number of AnnotationSpecs in the context of the SavedQuery. |  [optional] [readonly] |
|**createTime** | **String** | Output only. Timestamp when this SavedQuery was created. |  [optional] [readonly] |
|**displayName** | **String** | Required. The user-defined name of the SavedQuery. The name can be up to 128 characters long and can consist of any UTF-8 characters. |  [optional] |
|**etag** | **String** | Used to perform a consistent read-modify-write update. If not set, a blind \&quot;overwrite\&quot; update happens. |  [optional] |
|**metadata** | **Object** | Some additional information about the SavedQuery. |  [optional] |
|**name** | **String** | Output only. Resource name of the SavedQuery. |  [optional] [readonly] |
|**problemType** | **String** | Required. Problem type of the SavedQuery. Allowed values: * IMAGE_CLASSIFICATION_SINGLE_LABEL * IMAGE_CLASSIFICATION_MULTI_LABEL * IMAGE_BOUNDING_POLY * IMAGE_BOUNDING_BOX * TEXT_CLASSIFICATION_SINGLE_LABEL * TEXT_CLASSIFICATION_MULTI_LABEL * TEXT_EXTRACTION * TEXT_SENTIMENT * VIDEO_CLASSIFICATION * VIDEO_OBJECT_TRACKING |  [optional] |
|**supportAutomlTraining** | **Boolean** | Output only. If the Annotations belonging to the SavedQuery can be used for AutoML training. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. Timestamp when SavedQuery was last updated. |  [optional] [readonly] |



