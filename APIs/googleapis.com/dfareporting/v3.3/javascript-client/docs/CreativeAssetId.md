# CampaignManager360Api.CreativeAssetId

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Name of the creative asset. This is a required field while inserting an asset. After insertion, this assetIdentifier is used to identify the uploaded asset. Characters in the name must be alphanumeric or one of the following: \&quot;.-_ \&quot;. Spaces are allowed. | [optional] 
**type** | **String** | Type of asset to upload. This is a required field. FLASH and IMAGE are no longer supported for new uploads. All image assets should use HTML_IMAGE. | [optional] 



## Enum: TypeEnum


* `IMAGE` (value: `"IMAGE"`)

* `FLASH` (value: `"FLASH"`)

* `VIDEO` (value: `"VIDEO"`)

* `HTML` (value: `"HTML"`)

* `HTML_IMAGE` (value: `"HTML_IMAGE"`)

* `AUDIO` (value: `"AUDIO"`)




