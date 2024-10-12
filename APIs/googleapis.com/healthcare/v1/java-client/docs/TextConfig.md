

# TextConfig


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalTransformations** | [**List&lt;InfoTypeTransformation&gt;**](InfoTypeTransformation.md) | Transformations to apply to the detected data, overridden by &#x60;exclude_info_types&#x60;. |  [optional] |
|**excludeInfoTypes** | **List&lt;String&gt;** | InfoTypes to skip transforming, overriding &#x60;additional_transformations&#x60;. |  [optional] |
|**transformations** | [**List&lt;InfoTypeTransformation&gt;**](InfoTypeTransformation.md) | The transformations to apply to the detected data. Deprecated. Use &#x60;additional_transformations&#x60; instead. |  [optional] |



