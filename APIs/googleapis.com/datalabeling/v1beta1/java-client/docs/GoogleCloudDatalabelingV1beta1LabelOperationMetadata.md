

# GoogleCloudDatalabelingV1beta1LabelOperationMetadata

Metadata of a labeling operation, such as LabelImage or LabelVideo. Next tag: 23

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotatedDataset** | **String** | Output only. The name of annotated dataset in format \&quot;projects/_*_/datasets/_*_/annotatedDatasets/_*\&quot;. |  [optional] |
|**createTime** | **String** | Output only. Timestamp when labeling request was created. |  [optional] |
|**dataset** | **String** | Output only. The name of dataset to be labeled. \&quot;projects/_*_/datasets/_*\&quot; |  [optional] |
|**imageBoundingBoxDetails** | [**GoogleCloudDatalabelingV1beta1LabelImageBoundingBoxOperationMetadata**](GoogleCloudDatalabelingV1beta1LabelImageBoundingBoxOperationMetadata.md) |  |  [optional] |
|**imageBoundingPolyDetails** | [**GoogleCloudDatalabelingV1beta1LabelImageBoundingPolyOperationMetadata**](GoogleCloudDatalabelingV1beta1LabelImageBoundingPolyOperationMetadata.md) |  |  [optional] |
|**imageClassificationDetails** | [**GoogleCloudDatalabelingV1beta1LabelImageClassificationOperationMetadata**](GoogleCloudDatalabelingV1beta1LabelImageClassificationOperationMetadata.md) |  |  [optional] |
|**imageOrientedBoundingBoxDetails** | [**GoogleCloudDatalabelingV1beta1LabelImageOrientedBoundingBoxOperationMetadata**](GoogleCloudDatalabelingV1beta1LabelImageOrientedBoundingBoxOperationMetadata.md) |  |  [optional] |
|**imagePolylineDetails** | [**GoogleCloudDatalabelingV1beta1LabelImagePolylineOperationMetadata**](GoogleCloudDatalabelingV1beta1LabelImagePolylineOperationMetadata.md) |  |  [optional] |
|**imageSegmentationDetails** | [**GoogleCloudDatalabelingV1beta1LabelImageSegmentationOperationMetadata**](GoogleCloudDatalabelingV1beta1LabelImageSegmentationOperationMetadata.md) |  |  [optional] |
|**partialFailures** | [**List&lt;GoogleRpcStatus&gt;**](GoogleRpcStatus.md) | Output only. Partial failures encountered. E.g. single files that couldn&#39;t be read. Status details field will contain standard GCP error details. |  [optional] |
|**progressPercent** | **Integer** | Output only. Progress of label operation. Range: [0, 100]. |  [optional] |
|**textClassificationDetails** | [**GoogleCloudDatalabelingV1beta1LabelTextClassificationOperationMetadata**](GoogleCloudDatalabelingV1beta1LabelTextClassificationOperationMetadata.md) |  |  [optional] |
|**textEntityExtractionDetails** | [**GoogleCloudDatalabelingV1beta1LabelTextEntityExtractionOperationMetadata**](GoogleCloudDatalabelingV1beta1LabelTextEntityExtractionOperationMetadata.md) |  |  [optional] |
|**videoClassificationDetails** | [**GoogleCloudDatalabelingV1beta1LabelVideoClassificationOperationMetadata**](GoogleCloudDatalabelingV1beta1LabelVideoClassificationOperationMetadata.md) |  |  [optional] |
|**videoEventDetails** | [**GoogleCloudDatalabelingV1beta1LabelVideoEventOperationMetadata**](GoogleCloudDatalabelingV1beta1LabelVideoEventOperationMetadata.md) |  |  [optional] |
|**videoObjectDetectionDetails** | [**GoogleCloudDatalabelingV1beta1LabelVideoObjectDetectionOperationMetadata**](GoogleCloudDatalabelingV1beta1LabelVideoObjectDetectionOperationMetadata.md) |  |  [optional] |
|**videoObjectTrackingDetails** | [**GoogleCloudDatalabelingV1beta1LabelVideoObjectTrackingOperationMetadata**](GoogleCloudDatalabelingV1beta1LabelVideoObjectTrackingOperationMetadata.md) |  |  [optional] |



