# WebAppsApiClient.SiteCloneability

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockingCharacteristics** | [**[SiteCloneabilityCriterion]**](SiteCloneabilityCriterion.md) | List of blocking application characteristics. | [optional] 
**blockingFeatures** | [**[SiteCloneabilityCriterion]**](SiteCloneabilityCriterion.md) | List of features enabled on app that prevent cloning. | [optional] 
**result** | **String** | Name of app. | [optional] 
**unsupportedFeatures** | [**[SiteCloneabilityCriterion]**](SiteCloneabilityCriterion.md) | List of features enabled on app that are non-blocking but cannot be cloned. The app can still be cloned but the features in this list will not be set up on cloned app. | [optional] 



## Enum: ResultEnum


* `Cloneable` (value: `"Cloneable"`)

* `PartiallyCloneable` (value: `"PartiallyCloneable"`)

* `NotCloneable` (value: `"NotCloneable"`)




