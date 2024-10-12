# WebSiteManagementClient.SiteCloneability

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockingCharacteristics** | [**[SiteCloneabilityCriterion]**](SiteCloneabilityCriterion.md) | List of blocking application characteristics | [optional] 
**blockingFeatures** | [**[SiteCloneabilityCriterion]**](SiteCloneabilityCriterion.md) | List of features enabled on web app that prevent cloning | [optional] 
**result** | **String** | Name of web app | 
**unsupportedFeatures** | [**[SiteCloneabilityCriterion]**](SiteCloneabilityCriterion.md) | List of features enabled on web app that are non-blocking but cannot be cloned. The web app can still be cloned              but the features in this list will not be set up on cloned web app. | [optional] 



## Enum: ResultEnum


* `Cloneable` (value: `"Cloneable"`)

* `PartiallyCloneable` (value: `"PartiallyCloneable"`)

* `NotCloneable` (value: `"NotCloneable"`)




