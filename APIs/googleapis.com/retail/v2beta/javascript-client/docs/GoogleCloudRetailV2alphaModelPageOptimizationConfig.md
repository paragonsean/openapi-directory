# VertexAiSearchForRetailApi.GoogleCloudRetailV2alphaModelPageOptimizationConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pageOptimizationEventType** | **String** | Required. The type of UserEvent this page optimization is shown for. Each page has an associated event type - this will be the corresponding event type for the page that the page optimization model is used on. Supported types: * &#x60;add-to-cart&#x60;: Products being added to cart. * &#x60;detail-page-view&#x60;: Products detail page viewed. * &#x60;home-page-view&#x60;: Homepage viewed * &#x60;category-page-view&#x60;: Homepage viewed * &#x60;shopping-cart-page-view&#x60;: User viewing a shopping cart. &#x60;home-page-view&#x60; only allows models with type &#x60;recommended-for-you&#x60;. All other page_optimization_event_type allow all Model.types. | [optional] 
**panels** | [**[GoogleCloudRetailV2alphaModelPageOptimizationConfigPanel]**](GoogleCloudRetailV2alphaModelPageOptimizationConfigPanel.md) | Required. A list of panel configurations. Limit &#x3D; 5. | [optional] 
**restriction** | **String** | Optional. How to restrict results across panels e.g. can the same ServingConfig be shown on multiple panels at once. If unspecified, default to &#x60;UNIQUE_MODEL_RESTRICTION&#x60;. | [optional] 



## Enum: RestrictionEnum


* `RESTRICTION_UNSPECIFIED` (value: `"RESTRICTION_UNSPECIFIED"`)

* `NO_RESTRICTION` (value: `"NO_RESTRICTION"`)

* `UNIQUE_SERVING_CONFIG_RESTRICTION` (value: `"UNIQUE_SERVING_CONFIG_RESTRICTION"`)

* `UNIQUE_MODEL_RESTRICTION` (value: `"UNIQUE_MODEL_RESTRICTION"`)

* `UNIQUE_MODEL_TYPE_RESTRICTION` (value: `"UNIQUE_MODEL_TYPE_RESTRICTION"`)




