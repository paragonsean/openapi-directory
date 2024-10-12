

# ComparedSourceImageFace

Type that describes the face Amazon Rekognition chose to compare with the faces in the target. This contains a bounding box for the selected face and confidence level that the bounding box contains a face. Note that Amazon Rekognition selects the largest face in the source image for this comparison. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**boundingBox** | [**ComparedFaceBoundingBox**](ComparedFaceBoundingBox.md) |  |  [optional] |
|**confidence** | [**Float**](Float.md) |  |  [optional] |



