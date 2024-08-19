# VertexAiApi.GoogleCloudAiplatformV1beta1SafetySetting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **String** | Required. Harm category. | [optional] 
**threshold** | **String** | Required. The harm block threshold. | [optional] 



## Enum: CategoryEnum


* `UNSPECIFIED` (value: `"HARM_CATEGORY_UNSPECIFIED"`)

* `HATE_SPEECH` (value: `"HARM_CATEGORY_HATE_SPEECH"`)

* `DANGEROUS_CONTENT` (value: `"HARM_CATEGORY_DANGEROUS_CONTENT"`)

* `HARASSMENT` (value: `"HARM_CATEGORY_HARASSMENT"`)

* `SEXUALLY_EXPLICIT` (value: `"HARM_CATEGORY_SEXUALLY_EXPLICIT"`)





## Enum: ThresholdEnum


* `HARM_BLOCK_THRESHOLD_UNSPECIFIED` (value: `"HARM_BLOCK_THRESHOLD_UNSPECIFIED"`)

* `BLOCK_LOW_AND_ABOVE` (value: `"BLOCK_LOW_AND_ABOVE"`)

* `BLOCK_MEDIUM_AND_ABOVE` (value: `"BLOCK_MEDIUM_AND_ABOVE"`)

* `BLOCK_ONLY_HIGH` (value: `"BLOCK_ONLY_HIGH"`)

* `BLOCK_NONE` (value: `"BLOCK_NONE"`)




