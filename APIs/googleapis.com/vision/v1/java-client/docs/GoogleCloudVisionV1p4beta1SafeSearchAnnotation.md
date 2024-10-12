

# GoogleCloudVisionV1p4beta1SafeSearchAnnotation

Set of features pertaining to the image, computed by computer vision methods over safe-search verticals (for example, adult, spoof, medical, violence).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adult** | [**AdultEnum**](#AdultEnum) | Represents the adult content likelihood for the image. Adult content may contain elements such as nudity, pornographic images or cartoons, or sexual activities. |  [optional] |
|**medical** | [**MedicalEnum**](#MedicalEnum) | Likelihood that this is a medical image. |  [optional] |
|**racy** | [**RacyEnum**](#RacyEnum) | Likelihood that the request image contains racy content. Racy content may include (but is not limited to) skimpy or sheer clothing, strategically covered nudity, lewd or provocative poses, or close-ups of sensitive body areas. |  [optional] |
|**spoof** | [**SpoofEnum**](#SpoofEnum) | Spoof likelihood. The likelihood that an modification was made to the image&#39;s canonical version to make it appear funny or offensive. |  [optional] |
|**violence** | [**ViolenceEnum**](#ViolenceEnum) | Likelihood that this image contains violent content. Violent content may include death, serious harm, or injury to individuals or groups of individuals. |  [optional] |



## Enum: AdultEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| VERY_UNLIKELY | &quot;VERY_UNLIKELY&quot; |
| UNLIKELY | &quot;UNLIKELY&quot; |
| POSSIBLE | &quot;POSSIBLE&quot; |
| LIKELY | &quot;LIKELY&quot; |
| VERY_LIKELY | &quot;VERY_LIKELY&quot; |



## Enum: MedicalEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| VERY_UNLIKELY | &quot;VERY_UNLIKELY&quot; |
| UNLIKELY | &quot;UNLIKELY&quot; |
| POSSIBLE | &quot;POSSIBLE&quot; |
| LIKELY | &quot;LIKELY&quot; |
| VERY_LIKELY | &quot;VERY_LIKELY&quot; |



## Enum: RacyEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| VERY_UNLIKELY | &quot;VERY_UNLIKELY&quot; |
| UNLIKELY | &quot;UNLIKELY&quot; |
| POSSIBLE | &quot;POSSIBLE&quot; |
| LIKELY | &quot;LIKELY&quot; |
| VERY_LIKELY | &quot;VERY_LIKELY&quot; |



## Enum: SpoofEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| VERY_UNLIKELY | &quot;VERY_UNLIKELY&quot; |
| UNLIKELY | &quot;UNLIKELY&quot; |
| POSSIBLE | &quot;POSSIBLE&quot; |
| LIKELY | &quot;LIKELY&quot; |
| VERY_LIKELY | &quot;VERY_LIKELY&quot; |



## Enum: ViolenceEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| VERY_UNLIKELY | &quot;VERY_UNLIKELY&quot; |
| UNLIKELY | &quot;UNLIKELY&quot; |
| POSSIBLE | &quot;POSSIBLE&quot; |
| LIKELY | &quot;LIKELY&quot; |
| VERY_LIKELY | &quot;VERY_LIKELY&quot; |



