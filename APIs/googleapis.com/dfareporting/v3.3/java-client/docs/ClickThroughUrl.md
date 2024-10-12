

# ClickThroughUrl

Click-through URL

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**computedClickThroughUrl** | **String** | Read-only convenience field representing the actual URL that will be used for this click-through. The URL is computed as follows: - If defaultLandingPage is enabled then the campaign&#39;s default landing page URL is assigned to this field. - If defaultLandingPage is not enabled and a landingPageId is specified then that landing page&#39;s URL is assigned to this field. - If neither of the above cases apply, then the customClickThroughUrl is assigned to this field.  |  [optional] |
|**customClickThroughUrl** | **String** | Custom click-through URL. Applicable if the defaultLandingPage field is set to false and the landingPageId field is left unset. |  [optional] |
|**defaultLandingPage** | **Boolean** | Whether the campaign default landing page is used. |  [optional] |
|**landingPageId** | **String** | ID of the landing page for the click-through URL. Applicable if the defaultLandingPage field is set to false. |  [optional] |



