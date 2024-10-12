

# GoogleCloudRecommendationengineV1beta1CatalogItemLevelConfig

Configures the catalog level that users send events to, and the level at which predictions are made.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eventItemLevel** | [**EventItemLevelEnum**](#EventItemLevelEnum) | Optional. Level of the catalog at which events are uploaded. See https://cloud.google.com/recommendations-ai/docs/catalog#catalog-levels for more details. |  [optional] |
|**predictItemLevel** | [**PredictItemLevelEnum**](#PredictItemLevelEnum) | Optional. Level of the catalog at which predictions are made. See https://cloud.google.com/recommendations-ai/docs/catalog#catalog-levels for more details. |  [optional] |



## Enum: EventItemLevelEnum

| Name | Value |
|---- | -----|
| CATALOG_ITEM_LEVEL_UNSPECIFIED | &quot;CATALOG_ITEM_LEVEL_UNSPECIFIED&quot; |
| VARIANT | &quot;VARIANT&quot; |
| MASTER | &quot;MASTER&quot; |



## Enum: PredictItemLevelEnum

| Name | Value |
|---- | -----|
| CATALOG_ITEM_LEVEL_UNSPECIFIED | &quot;CATALOG_ITEM_LEVEL_UNSPECIFIED&quot; |
| VARIANT | &quot;VARIANT&quot; |
| MASTER | &quot;MASTER&quot; |



