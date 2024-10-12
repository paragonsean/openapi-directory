# DataLabelingApi.GoogleCloudDatalabelingV1alpha1LabelOperationMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotatedDataset** | **String** | Output only. The name of annotated dataset in format \&quot;projects/_*_/datasets/_*_/annotatedDatasets/_*\&quot;. | [optional] 
**createTime** | **String** | Output only. Timestamp when labeling request was created. | [optional] 
**dataset** | **String** | Output only. The name of dataset to be labeled. \&quot;projects/_*_/datasets/_*\&quot; | [optional] 
**imageBoundingBoxDetails** | [**GoogleCloudDatalabelingV1alpha1LabelImageBoundingBoxOperationMetadata**](GoogleCloudDatalabelingV1alpha1LabelImageBoundingBoxOperationMetadata.md) |  | [optional] 
**imageBoundingPolyDetails** | [**GoogleCloudDatalabelingV1alpha1LabelImageBoundingPolyOperationMetadata**](GoogleCloudDatalabelingV1alpha1LabelImageBoundingPolyOperationMetadata.md) |  | [optional] 
**imageClassificationDetails** | [**GoogleCloudDatalabelingV1alpha1LabelImageClassificationOperationMetadata**](GoogleCloudDatalabelingV1alpha1LabelImageClassificationOperationMetadata.md) |  | [optional] 
**imageOrientedBoundingBoxDetails** | [**GoogleCloudDatalabelingV1alpha1LabelImageOrientedBoundingBoxOperationMetadata**](GoogleCloudDatalabelingV1alpha1LabelImageOrientedBoundingBoxOperationMetadata.md) |  | [optional] 
**imagePolylineDetails** | [**GoogleCloudDatalabelingV1alpha1LabelImagePolylineOperationMetadata**](GoogleCloudDatalabelingV1alpha1LabelImagePolylineOperationMetadata.md) |  | [optional] 
**imageSegmentationDetails** | [**GoogleCloudDatalabelingV1alpha1LabelImageSegmentationOperationMetadata**](GoogleCloudDatalabelingV1alpha1LabelImageSegmentationOperationMetadata.md) |  | [optional] 
**partialFailures** | [**[GoogleRpcStatus]**](GoogleRpcStatus.md) | Output only. Partial failures encountered. E.g. single files that couldn&#39;t be read. Status details field will contain standard GCP error details. | [optional] 
**progressPercent** | **Number** | Output only. Progress of label operation. Range: [0, 100]. | [optional] 
**textClassificationDetails** | [**GoogleCloudDatalabelingV1alpha1LabelTextClassificationOperationMetadata**](GoogleCloudDatalabelingV1alpha1LabelTextClassificationOperationMetadata.md) |  | [optional] 
**textEntityExtractionDetails** | [**GoogleCloudDatalabelingV1alpha1LabelTextEntityExtractionOperationMetadata**](GoogleCloudDatalabelingV1alpha1LabelTextEntityExtractionOperationMetadata.md) |  | [optional] 
**videoClassificationDetails** | [**GoogleCloudDatalabelingV1alpha1LabelVideoClassificationOperationMetadata**](GoogleCloudDatalabelingV1alpha1LabelVideoClassificationOperationMetadata.md) |  | [optional] 
**videoEventDetails** | [**GoogleCloudDatalabelingV1alpha1LabelVideoEventOperationMetadata**](GoogleCloudDatalabelingV1alpha1LabelVideoEventOperationMetadata.md) |  | [optional] 
**videoObjectDetectionDetails** | [**GoogleCloudDatalabelingV1alpha1LabelVideoObjectDetectionOperationMetadata**](GoogleCloudDatalabelingV1alpha1LabelVideoObjectDetectionOperationMetadata.md) |  | [optional] 
**videoObjectTrackingDetails** | [**GoogleCloudDatalabelingV1alpha1LabelVideoObjectTrackingOperationMetadata**](GoogleCloudDatalabelingV1alpha1LabelVideoObjectTrackingOperationMetadata.md) |  | [optional] 


