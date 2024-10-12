

# FaceAttributes

Face Attributes

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessories** | [**List&lt;Accessory&gt;**](Accessory.md) | Properties describing any accessories on a given face. |  [optional] |
|**age** | **BigDecimal** | Age in years |  [optional] |
|**blur** | [**Blur**](Blur.md) |  |  [optional] |
|**emotion** | [**Emotion**](Emotion.md) |  |  [optional] |
|**exposure** | [**Exposure**](Exposure.md) |  |  [optional] |
|**facialHair** | [**FacialHair**](FacialHair.md) |  |  [optional] |
|**gender** | [**GenderEnum**](#GenderEnum) | Possible gender of the face. |  [optional] |
|**glasses** | [**GlassesEnum**](#GlassesEnum) | Glasses type if any of the face. |  [optional] |
|**hair** | [**Hair**](Hair.md) |  |  [optional] |
|**headPose** | [**HeadPose**](HeadPose.md) |  |  [optional] |
|**makeup** | [**Makeup**](Makeup.md) |  |  [optional] |
|**noise** | [**Noise**](Noise.md) |  |  [optional] |
|**occlusion** | [**Occlusion**](Occlusion.md) |  |  [optional] |
|**smile** | **BigDecimal** | A number ranging from 0 to 1 indicating the intensity level associated with a property. |  [optional] |



## Enum: GenderEnum

| Name | Value |
|---- | -----|
| MALE | &quot;male&quot; |
| FEMALE | &quot;female&quot; |



## Enum: GlassesEnum

| Name | Value |
|---- | -----|
| NO_GLASSES | &quot;noGlasses&quot; |
| READING_GLASSES | &quot;readingGlasses&quot; |
| SUNGLASSES | &quot;sunglasses&quot; |
| SWIMMING_GOGGLES | &quot;swimmingGoggles&quot; |



