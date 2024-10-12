

# TextConfig

Configures how to transform sensitive text `InfoTypes`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalTransformations** | [**List&lt;InfoTypeTransformation&gt;**](InfoTypeTransformation.md) | Additional transformations to apply to the detected data, overriding &#x60;profile&#x60;. |  [optional] |
|**excludeInfoTypes** | **List&lt;String&gt;** | InfoTypes to skip transforming, overriding &#x60;profile&#x60;. |  [optional] |
|**profileType** | [**ProfileTypeEnum**](#ProfileTypeEnum) | Base profile type for text transformation. |  [optional] |
|**transformations** | [**List&lt;InfoTypeTransformation&gt;**](InfoTypeTransformation.md) | The transformations to apply to the detected data. Deprecated. Use &#x60;additional_transformations&#x60; instead. |  [optional] |



## Enum: ProfileTypeEnum

| Name | Value |
|---- | -----|
| PROFILE_TYPE_UNSPECIFIED | &quot;PROFILE_TYPE_UNSPECIFIED&quot; |
| EMPTY | &quot;EMPTY&quot; |
| BASIC | &quot;BASIC&quot; |



