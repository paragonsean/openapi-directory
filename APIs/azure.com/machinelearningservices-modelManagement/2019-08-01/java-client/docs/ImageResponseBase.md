

# ImageResponseBase


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoDelete** | **Boolean** | Whether the image will be automatically deleted with the last service using it. |  [optional] |
|**createdTime** | **OffsetDateTime** | The time the image was created. |  [optional] |
|**creationState** | [**CreationStateEnum**](#CreationStateEnum) | The state of the operation. |  [optional] |
|**description** | **String** | The image description. |  [optional] |
|**error** | [**ModelErrorResponse**](ModelErrorResponse.md) |  |  [optional] |
|**id** | **String** | The image Id. |  [optional] |
|**imageBuildLogUri** | **String** | The Uri to the image build logs. |  [optional] |
|**imageFlavor** | [**ImageFlavorEnum**](#ImageFlavorEnum) | The flavor of the image. |  |
|**imageLocation** | **String** | The Image location string. |  [optional] |
|**imageType** | [**ImageTypeEnum**](#ImageTypeEnum) | The type of the image. |  [optional] |
|**kvTags** | **Map&lt;String, String&gt;** | The image tag dictionary. Tags are mutable. |  [optional] |
|**modelDetails** | [**List&lt;Model&gt;**](Model.md) | The list of models. |  [optional] |
|**modelIds** | **List&lt;String&gt;** | The list of model Ids. |  [optional] |
|**modifiedTime** | **OffsetDateTime** | The time the image was last modified. |  [optional] |
|**name** | **String** | The image name. |  [optional] |
|**operationId** | **String** | The ID of the asynchronous operation for this image. |  [optional] |
|**properties** | **Map&lt;String, String&gt;** | The image properties dictionary. Properties are immutable. |  [optional] |
|**version** | **Long** | The image version. |  [optional] |



## Enum: CreationStateEnum

| Name | Value |
|---- | -----|
| NOT_STARTED | &quot;NotStarted&quot; |
| RUNNING | &quot;Running&quot; |
| CANCELLED | &quot;Cancelled&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| TIMED_OUT | &quot;TimedOut&quot; |



## Enum: ImageFlavorEnum

| Name | Value |
|---- | -----|
| WEB_API_CONTAINER | &quot;WebApiContainer&quot; |
| BATCH_CONTAINER | &quot;BatchContainer&quot; |
| IO_T_CONTAINER | &quot;IoTContainer&quot; |
| ACCEL_CONTAINER | &quot;AccelContainer&quot; |
| USER_PROVIDED_CONTAINER | &quot;UserProvidedContainer&quot; |



## Enum: ImageTypeEnum

| Name | Value |
|---- | -----|
| DOCKER | &quot;Docker&quot; |



