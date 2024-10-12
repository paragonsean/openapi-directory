# DataLabelingApi.GoogleCloudDatalabelingV1p1alpha1LabelOperationMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotatedDataset** | **String** | Output only. The name of annotated dataset in format \&quot;projects/_*_/datasets/_*_/annotatedDatasets/_*\&quot;. | [optional] 
**createTime** | **String** | Output only. Timestamp when labeling request was created. | [optional] 
**dataset** | **String** | Output only. The name of dataset to be labeled. \&quot;projects/_*_/datasets/_*\&quot; | [optional] 
**imageBoundingBoxDetails** | [**GoogleCloudDatalabelingV1p1alpha1LabelImageBoundingBoxOperationMetadata**](GoogleCloudDatalabelingV1p1alpha1LabelImageBoundingBoxOperationMetadata.md) |  | [optional] 
**imageBoundingPolyDetails** | [**GoogleCloudDatalabelingV1p1alpha1LabelImageBoundingPolyOperationMetadata**](GoogleCloudDatalabelingV1p1alpha1LabelImageBoundingPolyOperationMetadata.md) |  | [optional] 
**imageClassificationDetails** | [**GoogleCloudDatalabelingV1p1alpha1LabelImageClassificationOperationMetadata**](GoogleCloudDatalabelingV1p1alpha1LabelImageClassificationOperationMetadata.md) |  | [optional] 
**imageOrientedBoundingBoxDetails** | [**GoogleCloudDatalabelingV1p1alpha1LabelImageOrientedBoundingBoxOperationMetadata**](GoogleCloudDatalabelingV1p1alpha1LabelImageOrientedBoundingBoxOperationMetadata.md) |  | [optional] 
**imagePolylineDetails** | [**GoogleCloudDatalabelingV1p1alpha1LabelImagePolylineOperationMetadata**](GoogleCloudDatalabelingV1p1alpha1LabelImagePolylineOperationMetadata.md) |  | [optional] 
**imageSegmentationDetails** | [**GoogleCloudDatalabelingV1p1alpha1LabelImageSegmentationOperationMetadata**](GoogleCloudDatalabelingV1p1alpha1LabelImageSegmentationOperationMetadata.md) |  | [optional] 
**partialFailures** | [**[GoogleRpcStatus]**](GoogleRpcStatus.md) | Output only. Partial failures encountered. E.g. single files that couldn&#39;t be read. Status details field will contain standard GCP error details. | [optional] 
**progressPercent** | **Number** | Output only. Progress of label operation. Range: [0, 100]. | [optional] 
**textClassificationDetails** | [**GoogleCloudDatalabelingV1p1alpha1LabelTextClassificationOperationMetadata**](GoogleCloudDatalabelingV1p1alpha1LabelTextClassificationOperationMetadata.md) |  | [optional] 
**textEntityExtractionDetails** | [**GoogleCloudDatalabelingV1p1alpha1LabelTextEntityExtractionOperationMetadata**](GoogleCloudDatalabelingV1p1alpha1LabelTextEntityExtractionOperationMetadata.md) |  | [optional] 
**videoClassificationDetails** | [**GoogleCloudDatalabelingV1p1alpha1LabelVideoClassificationOperationMetadata**](GoogleCloudDatalabelingV1p1alpha1LabelVideoClassificationOperationMetadata.md) |  | [optional] 
**videoEventDetails** | [**GoogleCloudDatalabelingV1p1alpha1LabelVideoEventOperationMetadata**](GoogleCloudDatalabelingV1p1alpha1LabelVideoEventOperationMetadata.md) |  | [optional] 
**videoObjectDetectionDetails** | [**GoogleCloudDatalabelingV1p1alpha1LabelVideoObjectDetectionOperationMetadata**](GoogleCloudDatalabelingV1p1alpha1LabelVideoObjectDetectionOperationMetadata.md) |  | [optional] 
**videoObjectTrackingDetails** | [**GoogleCloudDatalabelingV1p1alpha1LabelVideoObjectTrackingOperationMetadata**](GoogleCloudDatalabelingV1p1alpha1LabelVideoObjectTrackingOperationMetadata.md) |  | [optional] 


