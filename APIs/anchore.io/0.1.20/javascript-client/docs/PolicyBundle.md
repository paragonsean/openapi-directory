# AnchoreEngineApiServer.PolicyBundle

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blacklistedImages** | [**[ImageSelectionRule]**](ImageSelectionRule.md) | List of mapping rules that define which images should always result in a STOP/FAIL policy result regardless of policy content or presence in whitelisted_images | [optional] 
**comment** | **String** | Description of the bundle, human readable | [optional] 
**id** | **String** | Id of the bundle | 
**mappings** | [**[MappingRule]**](MappingRule.md) | Mapping rules for defining which policy and whitelist(s) to apply to an image based on a match of the image tag or id. Evaluated in order. | 
**name** | **String** | Human readable name for the bundle | [optional] 
**policies** | [**[Policy]**](Policy.md) | Policies which define the go/stop/warn status of an image using rule matches on image properties | 
**version** | **String** | Version id for this bundle format | 
**whitelistedImages** | [**[ImageSelectionRule]**](ImageSelectionRule.md) | List of mapping rules that define which images should always be passed (unless also on the blacklist), regardless of policy result. | [optional] 
**whitelists** | [**[Whitelist]**](Whitelist.md) | Whitelists which define which policy matches to disregard explicitly in the final policy decision | [optional] 


