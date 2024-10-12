

# GoogleCloudDatalabelingV1beta1Example

An Example is a piece of data and its annotation. For example, an image with label \"house\".

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotations** | [**List&lt;GoogleCloudDatalabelingV1beta1Annotation&gt;**](GoogleCloudDatalabelingV1beta1Annotation.md) | Output only. Annotations for the piece of data in Example. One piece of data can have multiple annotations. |  [optional] |
|**imagePayload** | [**GoogleCloudDatalabelingV1beta1ImagePayload**](GoogleCloudDatalabelingV1beta1ImagePayload.md) |  |  [optional] |
|**name** | **String** | Output only. Name of the example, in format of: projects/{project_id}/datasets/{dataset_id}/annotatedDatasets/ {annotated_dataset_id}/examples/{example_id} |  [optional] |
|**textPayload** | [**GoogleCloudDatalabelingV1beta1TextPayload**](GoogleCloudDatalabelingV1beta1TextPayload.md) |  |  [optional] |
|**videoPayload** | [**GoogleCloudDatalabelingV1beta1VideoPayload**](GoogleCloudDatalabelingV1beta1VideoPayload.md) |  |  [optional] |



