# CloudHealthcareApi.TextConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalTransformations** | [**[InfoTypeTransformation]**](InfoTypeTransformation.md) | Transformations to apply to the detected data, overridden by &#x60;exclude_info_types&#x60;. | [optional] 
**excludeInfoTypes** | **[String]** | InfoTypes to skip transforming, overriding &#x60;additional_transformations&#x60;. | [optional] 
**transformations** | [**[InfoTypeTransformation]**](InfoTypeTransformation.md) | The transformations to apply to the detected data. Deprecated. Use &#x60;additional_transformations&#x60; instead. | [optional] 


