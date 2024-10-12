

# GoogleCloudRetailV2ModelFrequentlyBoughtTogetherFeaturesConfig

Additional configs for the frequently-bought-together model type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contextProductsType** | [**ContextProductsTypeEnum**](#ContextProductsTypeEnum) | Optional. Specifies the context of the model when it is used in predict requests. Can only be set for the &#x60;frequently-bought-together&#x60; type. If it isn&#39;t specified, it defaults to MULTIPLE_CONTEXT_PRODUCTS. |  [optional] |



## Enum: ContextProductsTypeEnum

| Name | Value |
|---- | -----|
| CONTEXT_PRODUCTS_TYPE_UNSPECIFIED | &quot;CONTEXT_PRODUCTS_TYPE_UNSPECIFIED&quot; |
| SINGLE_CONTEXT_PRODUCT | &quot;SINGLE_CONTEXT_PRODUCT&quot; |
| MULTIPLE_CONTEXT_PRODUCTS | &quot;MULTIPLE_CONTEXT_PRODUCTS&quot; |



