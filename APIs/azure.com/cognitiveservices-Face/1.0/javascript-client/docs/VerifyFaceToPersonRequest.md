# FaceClient.VerifyFaceToPersonRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**faceId** | **String** | FaceId of the face, comes from Face - Detect | 
**largePersonGroupId** | **String** | Using existing largePersonGroupId and personId for fast loading a specified person. largePersonGroupId is created in LargePersonGroup - Create. Parameter personGroupId and largePersonGroupId should not be provided at the same time. | [optional] 
**personGroupId** | **String** | Using existing personGroupId and personId for fast loading a specified person. personGroupId is created in PersonGroup - Create. Parameter personGroupId and largePersonGroupId should not be provided at the same time. | [optional] 
**personId** | **String** | Specify a certain person in a person group or a large person group. personId is created in PersonGroup Person - Create or LargePersonGroup Person - Create. | 


