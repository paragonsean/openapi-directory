

# PolicyBundle

A bundle containing a set of policies, whitelists, and rules for mapping them to specific images

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blacklistedImages** | [**List&lt;ImageSelectionRule&gt;**](ImageSelectionRule.md) | List of mapping rules that define which images should always result in a STOP/FAIL policy result regardless of policy content or presence in whitelisted_images |  [optional] |
|**comment** | **String** | Description of the bundle, human readable |  [optional] |
|**id** | **String** | Id of the bundle |  |
|**mappings** | [**List&lt;MappingRule&gt;**](MappingRule.md) | Mapping rules for defining which policy and whitelist(s) to apply to an image based on a match of the image tag or id. Evaluated in order. |  |
|**name** | **String** | Human readable name for the bundle |  [optional] |
|**policies** | [**List&lt;Policy&gt;**](Policy.md) | Policies which define the go/stop/warn status of an image using rule matches on image properties |  |
|**version** | **String** | Version id for this bundle format |  |
|**whitelistedImages** | [**List&lt;ImageSelectionRule&gt;**](ImageSelectionRule.md) | List of mapping rules that define which images should always be passed (unless also on the blacklist), regardless of policy result. |  [optional] |
|**whitelists** | [**List&lt;Whitelist&gt;**](Whitelist.md) | Whitelists which define which policy matches to disregard explicitly in the final policy decision |  [optional] |



