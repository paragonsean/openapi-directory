# CampaignManager360Api.DirectorySite

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **Boolean** | Whether this directory site is active. | [optional] 
**id** | **String** | ID of this directory site. This is a read-only, auto-generated field. | [optional] 
**idDimensionValue** | [**DimensionValue**](DimensionValue.md) |  | [optional] 
**inpageTagFormats** | **[String]** | Tag types for regular placements. Acceptable values are: - \&quot;STANDARD\&quot; - \&quot;IFRAME_JAVASCRIPT_INPAGE\&quot; - \&quot;INTERNAL_REDIRECT_INPAGE\&quot; - \&quot;JAVASCRIPT_INPAGE\&quot;  | [optional] 
**interstitialTagFormats** | **[String]** | Tag types for interstitial placements. Acceptable values are: - \&quot;IFRAME_JAVASCRIPT_INTERSTITIAL\&quot; - \&quot;INTERNAL_REDIRECT_INTERSTITIAL\&quot; - \&quot;JAVASCRIPT_INTERSTITIAL\&quot;  | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#directorySite\&quot;. | [optional] 
**name** | **String** | Name of this directory site. | [optional] 
**settings** | [**DirectorySiteSettings**](DirectorySiteSettings.md) |  | [optional] 
**url** | **String** | URL of this directory site. | [optional] 



## Enum: [InpageTagFormatsEnum]


* `STANDARD` (value: `"STANDARD"`)

* `IFRAME_JAVASCRIPT_INPAGE` (value: `"IFRAME_JAVASCRIPT_INPAGE"`)

* `INTERNAL_REDIRECT_INPAGE` (value: `"INTERNAL_REDIRECT_INPAGE"`)

* `JAVASCRIPT_INPAGE` (value: `"JAVASCRIPT_INPAGE"`)





## Enum: [InterstitialTagFormatsEnum]


* `IFRAME_JAVASCRIPT_INTERSTITIAL` (value: `"IFRAME_JAVASCRIPT_INTERSTITIAL"`)

* `INTERNAL_REDIRECT_INTERSTITIAL` (value: `"INTERNAL_REDIRECT_INTERSTITIAL"`)

* `JAVASCRIPT_INTERSTITIAL` (value: `"JAVASCRIPT_INTERSTITIAL"`)




