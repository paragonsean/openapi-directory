

# GoogleCloudDatalabelingV1p2alpha1LabelOperationMetadata

Metadata of a labeling operation, such as LabelImage or LabelVideo. Next tag: 23

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotatedDataset** | **String** | Output only. The name of annotated dataset in format \&quot;projects/_*_/datasets/_*_/annotatedDatasets/_*\&quot;. |  [optional] |
|**createTime** | **String** | Output only. Timestamp when labeling request was created. |  [optional] |
|**dataset** | **String** | Output only. The name of dataset to be labeled. \&quot;projects/_*_/datasets/_*\&quot; |  [optional] |
|**imageBoundingBoxDetails** | [**GoogleCloudDatalabelingV1p2alpha1LabelImageBoundingBoxOperationMetadata**](GoogleCloudDatalabelingV1p2alpha1LabelImageBoundingBoxOperationMetadata.md) |  |  [optional] |
|**imageBoundingPolyDetails** | [**GoogleCloudDatalabelingV1p2alpha1LabelImageBoundingPolyOperationMetadata**](GoogleCloudDatalabelingV1p2alpha1LabelImageBoundingPolyOperationMetadata.md) |  |  [optional] |
|**imageClassificationDetails** | [**GoogleCloudDatalabelingV1p2alpha1LabelImageClassificationOperationMetadata**](GoogleCloudDatalabelingV1p2alpha1LabelImageClassificationOperationMetadata.md) |  |  [optional] |
|**imageOrientedBoundingBoxDetails** | [**GoogleCloudDatalabelingV1p2alpha1LabelImageOrientedBoundingBoxOperationMetadata**](GoogleCloudDatalabelingV1p2alpha1LabelImageOrientedBoundingBoxOperationMetadata.md) |  |  [optional] |
|**imagePolylineDetails** | [**GoogleCloudDatalabelingV1p2alpha1LabelImagePolylineOperationMetadata**](GoogleCloudDatalabelingV1p2alpha1LabelImagePolylineOperationMetadata.md) |  |  [optional] |
|**imageSegmentationDetails** | [**GoogleCloudDatalabelingV1p2alpha1LabelImageSegmentationOperationMetadata**](GoogleCloudDatalabelingV1p2alpha1LabelImageSegmentationOperationMetadata.md) |  |  [optional] |
|**partialFailures** | [**List&lt;GoogleRpcStatus&gt;**](GoogleRpcStatus.md) | Output only. Partial failures encountered. E.g. single files that couldn&#39;t be read. Status details field will contain standard GCP error details. |  [optional] |
|**progressPercent** | **Integer** | Output only. Progress of label operation. Range: [0, 100]. |  [optional] |
|**textClassificationDetails** | [**GoogleCloudDatalabelingV1p2alpha1LabelTextClassificationOperationMetadata**](GoogleCloudDatalabelingV1p2alpha1LabelTextClassificationOperationMetadata.md) |  |  [optional] |
|**textEntityExtractionDetails** | [**GoogleCloudDatalabelingV1p2alpha1LabelTextEntityExtractionOperationMetadata**](GoogleCloudDatalabelingV1p2alpha1LabelTextEntityExtractionOperationMetadata.md) |  |  [optional] |
|**videoClassificationDetails** | [**GoogleCloudDatalabelingV1p2alpha1LabelVideoClassificationOperationMetadata**](GoogleCloudDatalabelingV1p2alpha1LabelVideoClassificationOperationMetadata.md) |  |  [optional] |
|**videoEventDetails** | [**GoogleCloudDatalabelingV1p2alpha1LabelVideoEventOperationMetadata**](GoogleCloudDatalabelingV1p2alpha1LabelVideoEventOperationMetadata.md) |  |  [optional] |
|**videoObjectDetectionDetails** | [**GoogleCloudDatalabelingV1p2alpha1LabelVideoObjectDetectionOperationMetadata**](GoogleCloudDatalabelingV1p2alpha1LabelVideoObjectDetectionOperationMetadata.md) |  |  [optional] |
|**videoObjectTrackingDetails** | [**GoogleCloudDatalabelingV1p2alpha1LabelVideoObjectTrackingOperationMetadata**](GoogleCloudDatalabelingV1p2alpha1LabelVideoObjectTrackingOperationMetadata.md) |  |  [optional] |



