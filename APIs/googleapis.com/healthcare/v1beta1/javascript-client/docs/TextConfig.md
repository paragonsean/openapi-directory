# CloudHealthcareApi.TextConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalTransformations** | [**[InfoTypeTransformation]**](InfoTypeTransformation.md) | Additional transformations to apply to the detected data, overriding &#x60;profile&#x60;. | [optional] 
**excludeInfoTypes** | **[String]** | InfoTypes to skip transforming, overriding &#x60;profile&#x60;. | [optional] 
**profileType** | **String** | Base profile type for text transformation. | [optional] 
**transformations** | [**[InfoTypeTransformation]**](InfoTypeTransformation.md) | The transformations to apply to the detected data. Deprecated. Use &#x60;additional_transformations&#x60; instead. | [optional] 



## Enum: ProfileTypeEnum


* `PROFILE_TYPE_UNSPECIFIED` (value: `"PROFILE_TYPE_UNSPECIFIED"`)

* `EMPTY` (value: `"EMPTY"`)

* `BASIC` (value: `"BASIC"`)




