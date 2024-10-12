# CampaignManager360Api.CreativeAssetSelection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defaultAssetId** | **String** | A creativeAssets[].id. This should refer to one of the parent assets in this creative, and will be served if none of the rules match. This is a required field. | [optional] 
**rules** | [**[Rule]**](Rule.md) | Rules determine which asset will be served to a viewer. Rules will be evaluated in the order in which they are stored in this list. This list must contain at least one rule. Applicable to INSTREAM_VIDEO creatives. | [optional] 


