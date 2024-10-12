# DiscoveryEngineApi.GoogleCloudDiscoveryengineV1alphaEngineRecommendationMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataState** | **String** | Output only. The state of data requirements for this engine: &#x60;DATA_OK&#x60; and &#x60;DATA_ERROR&#x60;. Engine cannot be trained if the data is in &#x60;DATA_ERROR&#x60; state. Engine can have &#x60;DATA_ERROR&#x60; state even if serving state is &#x60;ACTIVE&#x60;: engines were trained successfully before, but cannot be refreshed because the underlying engine no longer has sufficient data for training. | [optional] [readonly] 
**lastTuneTime** | **String** | Output only. The timestamp when the latest successful tune finished. Only applicable on Media Recommendation engines. | [optional] [readonly] 
**servingState** | **String** | Output only. The serving state of the engine: &#x60;ACTIVE&#x60;, &#x60;NOT_ACTIVE&#x60;. | [optional] [readonly] 
**tuningOperation** | **String** | Output only. The latest tune operation id associated with the engine. Only applicable on Media Recommendation engines. If present, this operation id can be used to determine if there is an ongoing tune for this engine. To check the operation status, send the GetOperation request with this operation id in the engine resource format. If no tuning has happened for this engine, the string is empty. | [optional] [readonly] 



## Enum: DataStateEnum


* `STATE_UNSPECIFIED` (value: `"DATA_STATE_UNSPECIFIED"`)

* `OK` (value: `"DATA_OK"`)

* `ERROR` (value: `"DATA_ERROR"`)





## Enum: ServingStateEnum


* `SERVING_STATE_UNSPECIFIED` (value: `"SERVING_STATE_UNSPECIFIED"`)

* `INACTIVE` (value: `"INACTIVE"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `TUNED` (value: `"TUNED"`)




