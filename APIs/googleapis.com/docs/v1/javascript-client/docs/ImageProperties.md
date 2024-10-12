# GoogleDocsApi.ImageProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**angle** | **Number** | The clockwise rotation angle of the image, in radians. | [optional] 
**brightness** | **Number** | The brightness effect of the image. The value should be in the interval [-1.0, 1.0], where 0 means no effect. | [optional] 
**contentUri** | **String** | A URI to the image with a default lifetime of 30 minutes. This URI is tagged with the account of the requester. Anyone with the URI effectively accesses the image as the original requester. Access to the image may be lost if the document&#39;s sharing settings change. | [optional] 
**contrast** | **Number** | The contrast effect of the image. The value should be in the interval [-1.0, 1.0], where 0 means no effect. | [optional] 
**cropProperties** | [**CropProperties**](CropProperties.md) |  | [optional] 
**sourceUri** | **String** | The source URI is the URI used to insert the image. The source URI can be empty. | [optional] 
**transparency** | **Number** | The transparency effect of the image. The value should be in the interval [0.0, 1.0], where 0 means no effect and 1 means transparent. | [optional] 


