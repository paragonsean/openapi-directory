# CampaignManager360Api.CreativeOptimizationConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | ID of this creative optimization config. This field is auto-generated when the campaign is inserted or updated. It can be null for existing campaigns. | [optional] 
**name** | **String** | Name of this creative optimization config. This is a required field and must be less than 129 characters long. | [optional] 
**optimizationActivitys** | [**[OptimizationActivity]**](OptimizationActivity.md) | List of optimization activities associated with this configuration. | [optional] 
**optimizationModel** | **String** | Optimization model for this configuration. | [optional] 



## Enum: OptimizationModelEnum


* `CLICK` (value: `"CLICK"`)

* `POST_CLICK` (value: `"POST_CLICK"`)

* `POST_IMPRESSION` (value: `"POST_IMPRESSION"`)

* `POST_CLICK_AND_IMPRESSION` (value: `"POST_CLICK_AND_IMPRESSION"`)

* `VIDEO_COMPLETION` (value: `"VIDEO_COMPLETION"`)




