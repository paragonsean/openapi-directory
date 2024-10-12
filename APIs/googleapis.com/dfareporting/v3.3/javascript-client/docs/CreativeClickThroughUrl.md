# CampaignManager360Api.CreativeClickThroughUrl

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**computedClickThroughUrl** | **String** | Read-only convenience field representing the actual URL that will be used for this click-through. The URL is computed as follows: - If landingPageId is specified then that landing page&#39;s URL is assigned to this field. - Otherwise, the customClickThroughUrl is assigned to this field.  | [optional] 
**customClickThroughUrl** | **String** | Custom click-through URL. Applicable if the landingPageId field is left unset. | [optional] 
**landingPageId** | **String** | ID of the landing page for the click-through URL. | [optional] 


