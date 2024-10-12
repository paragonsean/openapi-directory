# AzureMachineLearningModelManagementService.ImageResponseBase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoDelete** | **Boolean** | Whether the image will be automatically deleted with the last service using it. | [optional] 
**createdTime** | **Date** | The time the image was created. | [optional] 
**creationState** | **String** | The state of the operation. | [optional] 
**description** | **String** | The image description. | [optional] 
**error** | [**ModelErrorResponse**](ModelErrorResponse.md) |  | [optional] 
**id** | **String** | The image Id. | [optional] 
**imageBuildLogUri** | **String** | The Uri to the image build logs. | [optional] 
**imageFlavor** | **String** | The flavor of the image. | 
**imageLocation** | **String** | The Image location string. | [optional] 
**imageType** | **String** | The type of the image. | [optional] 
**kvTags** | **{String: String}** | The image tag dictionary. Tags are mutable. | [optional] 
**modelDetails** | [**[Model]**](Model.md) | The list of models. | [optional] 
**modelIds** | **[String]** | The list of model Ids. | [optional] 
**modifiedTime** | **Date** | The time the image was last modified. | [optional] 
**name** | **String** | The image name. | [optional] 
**operationId** | **String** | The ID of the asynchronous operation for this image. | [optional] 
**properties** | **{String: String}** | The image properties dictionary. Properties are immutable. | [optional] 
**version** | **Number** | The image version. | [optional] 



## Enum: CreationStateEnum


* `NotStarted` (value: `"NotStarted"`)

* `Running` (value: `"Running"`)

* `Cancelled` (value: `"Cancelled"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `TimedOut` (value: `"TimedOut"`)





## Enum: ImageFlavorEnum


* `WebApiContainer` (value: `"WebApiContainer"`)

* `BatchContainer` (value: `"BatchContainer"`)

* `IoTContainer` (value: `"IoTContainer"`)

* `AccelContainer` (value: `"AccelContainer"`)

* `UserProvidedContainer` (value: `"UserProvidedContainer"`)





## Enum: ImageTypeEnum


* `Docker` (value: `"Docker"`)




