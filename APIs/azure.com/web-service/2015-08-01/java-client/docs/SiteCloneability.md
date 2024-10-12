

# SiteCloneability

Represents whether or not a web app is cloneable

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blockingCharacteristics** | [**List&lt;SiteCloneabilityCriterion&gt;**](SiteCloneabilityCriterion.md) | List of blocking application characteristics |  [optional] |
|**blockingFeatures** | [**List&lt;SiteCloneabilityCriterion&gt;**](SiteCloneabilityCriterion.md) | List of features enabled on web app that prevent cloning |  [optional] |
|**result** | [**ResultEnum**](#ResultEnum) | Name of web app |  |
|**unsupportedFeatures** | [**List&lt;SiteCloneabilityCriterion&gt;**](SiteCloneabilityCriterion.md) | List of features enabled on web app that are non-blocking but cannot be cloned. The web app can still be cloned              but the features in this list will not be set up on cloned web app. |  [optional] |



## Enum: ResultEnum

| Name | Value |
|---- | -----|
| CLONEABLE | &quot;Cloneable&quot; |
| PARTIALLY_CLONEABLE | &quot;PartiallyCloneable&quot; |
| NOT_CLONEABLE | &quot;NotCloneable&quot; |



