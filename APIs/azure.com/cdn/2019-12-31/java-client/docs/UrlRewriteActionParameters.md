

# UrlRewriteActionParameters

Defines the parameters for the url rewrite action.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**atOdataType** | [**AtOdataTypeEnum**](#AtOdataTypeEnum) |  |  |
|**destination** | **String** | Define the relative URL to which the above requests will be rewritten by. |  |
|**preserveUnmatchedPath** | **Boolean** | Whether to preserve unmatched path. Default value is true. |  [optional] |
|**sourcePattern** | **String** | define a request URI pattern that identifies the type of requests that may be rewritten. If value is blank, all strings are matched. |  |



## Enum: AtOdataTypeEnum

| Name | Value |
|---- | -----|
| _MICROSOFT_AZURE_CDN_MODELS_DELIVERY_RULE_URL_REWRITE_ACTION_PARAMETERS | &quot;#Microsoft.Azure.Cdn.Models.DeliveryRuleUrlRewriteActionParameters&quot; |



