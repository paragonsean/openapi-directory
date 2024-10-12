

# DirectorySite

DirectorySites contains properties of a website from the Site Directory. Sites need to be added to an account via the Sites resource before they can be assigned to a placement.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**active** | **Boolean** | Whether this directory site is active. |  [optional] |
|**id** | **String** | ID of this directory site. This is a read-only, auto-generated field. |  [optional] |
|**idDimensionValue** | [**DimensionValue**](DimensionValue.md) |  |  [optional] |
|**inpageTagFormats** | [**List&lt;InpageTagFormatsEnum&gt;**](#List&lt;InpageTagFormatsEnum&gt;) | Tag types for regular placements. Acceptable values are: - \&quot;STANDARD\&quot; - \&quot;IFRAME_JAVASCRIPT_INPAGE\&quot; - \&quot;INTERNAL_REDIRECT_INPAGE\&quot; - \&quot;JAVASCRIPT_INPAGE\&quot;  |  [optional] |
|**interstitialTagFormats** | [**List&lt;InterstitialTagFormatsEnum&gt;**](#List&lt;InterstitialTagFormatsEnum&gt;) | Tag types for interstitial placements. Acceptable values are: - \&quot;IFRAME_JAVASCRIPT_INTERSTITIAL\&quot; - \&quot;INTERNAL_REDIRECT_INTERSTITIAL\&quot; - \&quot;JAVASCRIPT_INTERSTITIAL\&quot;  |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#directorySite\&quot;. |  [optional] |
|**name** | **String** | Name of this directory site. |  [optional] |
|**settings** | [**DirectorySiteSettings**](DirectorySiteSettings.md) |  |  [optional] |
|**url** | **String** | URL of this directory site. |  [optional] |



## Enum: List&lt;InpageTagFormatsEnum&gt;

| Name | Value |
|---- | -----|
| STANDARD | &quot;STANDARD&quot; |
| IFRAME_JAVASCRIPT_INPAGE | &quot;IFRAME_JAVASCRIPT_INPAGE&quot; |
| INTERNAL_REDIRECT_INPAGE | &quot;INTERNAL_REDIRECT_INPAGE&quot; |
| JAVASCRIPT_INPAGE | &quot;JAVASCRIPT_INPAGE&quot; |



## Enum: List&lt;InterstitialTagFormatsEnum&gt;

| Name | Value |
|---- | -----|
| IFRAME_JAVASCRIPT_INTERSTITIAL | &quot;IFRAME_JAVASCRIPT_INTERSTITIAL&quot; |
| INTERNAL_REDIRECT_INTERSTITIAL | &quot;INTERNAL_REDIRECT_INTERSTITIAL&quot; |
| JAVASCRIPT_INTERSTITIAL | &quot;JAVASCRIPT_INTERSTITIAL&quot; |



