# VertexAiSearchForRetailApi.GoogleCloudRetailV2betaModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Timestamp the Recommendation Model was created at. | [optional] [readonly] 
**dataState** | **String** | Output only. The state of data requirements for this model: &#x60;DATA_OK&#x60; and &#x60;DATA_ERROR&#x60;. Recommendation model cannot be trained if the data is in &#x60;DATA_ERROR&#x60; state. Recommendation model can have &#x60;DATA_ERROR&#x60; state even if serving state is &#x60;ACTIVE&#x60;: models were trained successfully before, but cannot be refreshed because model no longer has sufficient data for training. | [optional] [readonly] 
**displayName** | **String** | Required. The display name of the model. Should be human readable, used to display Recommendation Models in the Retail Cloud Console Dashboard. UTF-8 encoded string with limit of 1024 characters. | [optional] 
**filteringOption** | **String** | Optional. If &#x60;RECOMMENDATIONS_FILTERING_ENABLED&#x60;, recommendation filtering by attributes is enabled for the model. | [optional] 
**lastTuneTime** | **String** | Output only. The timestamp when the latest successful tune finished. | [optional] [readonly] 
**modelFeaturesConfig** | [**GoogleCloudRetailV2betaModelModelFeaturesConfig**](GoogleCloudRetailV2betaModelModelFeaturesConfig.md) |  | [optional] 
**name** | **String** | Required. The fully qualified resource name of the model. Format: &#x60;projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/models/{model_id}&#x60; catalog_id has char limit of 50. recommendation_model_id has char limit of 40. | [optional] 
**optimizationObjective** | **String** | Optional. The optimization objective e.g. &#x60;cvr&#x60;. Currently supported values: &#x60;ctr&#x60;, &#x60;cvr&#x60;, &#x60;revenue-per-order&#x60;. If not specified, we choose default based on model type. Default depends on type of recommendation: &#x60;recommended-for-you&#x60; &#x3D;&gt; &#x60;ctr&#x60; &#x60;others-you-may-like&#x60; &#x3D;&gt; &#x60;ctr&#x60; &#x60;frequently-bought-together&#x60; &#x3D;&gt; &#x60;revenue_per_order&#x60; This field together with optimization_objective describe model metadata to use to control model training and serving. See https://cloud.google.com/retail/docs/models for more details on what the model metadata control and which combination of parameters are valid. For invalid combinations of parameters (e.g. type &#x3D; &#x60;frequently-bought-together&#x60; and optimization_objective &#x3D; &#x60;ctr&#x60;), you receive an error 400 if you try to create/update a recommendation with this set of knobs. | [optional] 
**periodicTuningState** | **String** | Optional. The state of periodic tuning. The period we use is 3 months - to do a one-off tune earlier use the &#x60;TuneModel&#x60; method. Default value is &#x60;PERIODIC_TUNING_ENABLED&#x60;. | [optional] 
**servingConfigLists** | [**[GoogleCloudRetailV2betaModelServingConfigList]**](GoogleCloudRetailV2betaModelServingConfigList.md) | Output only. The list of valid serving configs associated with the PageOptimizationConfig. | [optional] [readonly] 
**servingState** | **String** | Output only. The serving state of the model: &#x60;ACTIVE&#x60;, &#x60;NOT_ACTIVE&#x60;. | [optional] [readonly] 
**trainingState** | **String** | Optional. The training state that the model is in (e.g. &#x60;TRAINING&#x60; or &#x60;PAUSED&#x60;). Since part of the cost of running the service is frequency of training - this can be used to determine when to train model in order to control cost. If not specified: the default value for &#x60;CreateModel&#x60; method is &#x60;TRAINING&#x60;. The default value for &#x60;UpdateModel&#x60; method is to keep the state the same as before. | [optional] 
**tuningOperation** | **String** | Output only. The tune operation associated with the model. Can be used to determine if there is an ongoing tune for this recommendation. Empty field implies no tune is goig on. | [optional] [readonly] 
**type** | **String** | Required. The type of model e.g. &#x60;home-page&#x60;. Currently supported values: &#x60;recommended-for-you&#x60;, &#x60;others-you-may-like&#x60;, &#x60;frequently-bought-together&#x60;, &#x60;page-optimization&#x60;, &#x60;similar-items&#x60;, &#x60;buy-it-again&#x60;, &#x60;on-sale-items&#x60;, and &#x60;recently-viewed&#x60;(readonly value). This field together with optimization_objective describe model metadata to use to control model training and serving. See https://cloud.google.com/retail/docs/models for more details on what the model metadata control and which combination of parameters are valid. For invalid combinations of parameters (e.g. type &#x3D; &#x60;frequently-bought-together&#x60; and optimization_objective &#x3D; &#x60;ctr&#x60;), you receive an error 400 if you try to create/update a recommendation with this set of knobs. | [optional] 
**updateTime** | **String** | Output only. Timestamp the Recommendation Model was last updated. E.g. if a Recommendation Model was paused - this would be the time the pause was initiated. | [optional] [readonly] 



## Enum: DataStateEnum


* `STATE_UNSPECIFIED` (value: `"DATA_STATE_UNSPECIFIED"`)

* `OK` (value: `"DATA_OK"`)

* `ERROR` (value: `"DATA_ERROR"`)





## Enum: FilteringOptionEnum


* `OPTION_UNSPECIFIED` (value: `"RECOMMENDATIONS_FILTERING_OPTION_UNSPECIFIED"`)

* `DISABLED` (value: `"RECOMMENDATIONS_FILTERING_DISABLED"`)

* `ENABLED` (value: `"RECOMMENDATIONS_FILTERING_ENABLED"`)





## Enum: PeriodicTuningStateEnum


* `PERIODIC_TUNING_STATE_UNSPECIFIED` (value: `"PERIODIC_TUNING_STATE_UNSPECIFIED"`)

* `PERIODIC_TUNING_DISABLED` (value: `"PERIODIC_TUNING_DISABLED"`)

* `ALL_TUNING_DISABLED` (value: `"ALL_TUNING_DISABLED"`)

* `PERIODIC_TUNING_ENABLED` (value: `"PERIODIC_TUNING_ENABLED"`)





## Enum: ServingStateEnum


* `SERVING_STATE_UNSPECIFIED` (value: `"SERVING_STATE_UNSPECIFIED"`)

* `INACTIVE` (value: `"INACTIVE"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `TUNED` (value: `"TUNED"`)





## Enum: TrainingStateEnum


* `TRAINING_STATE_UNSPECIFIED` (value: `"TRAINING_STATE_UNSPECIFIED"`)

* `PAUSED` (value: `"PAUSED"`)

* `TRAINING` (value: `"TRAINING"`)




