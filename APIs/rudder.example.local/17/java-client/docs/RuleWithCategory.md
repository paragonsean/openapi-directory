

# RuleWithCategory


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | **UUID** | The parent category id. |  [optional] |
|**directives** | **List&lt;String&gt;** | Directives linked to the rule |  [optional] |
|**displayName** | **String** | Rule name |  [optional] |
|**enabled** | **Boolean** | Is the rule enabled |  [optional] |
|**id** | **UUID** | Rule id |  [optional] |
|**longDescription** | **String** | Rule documentation |  [optional] |
|**shortDescription** | **String** | One line rule description |  [optional] |
|**system** | **Boolean** | If true it is an internal Rudder rule |  [optional] |
|**tags** | [**List&lt;DirectiveTagsInner&gt;**](DirectiveTagsInner.md) |  |  [optional] |
|**targets** | [**List&lt;RuleTargetsInner&gt;**](RuleTargetsInner.md) | Node and special groups targeted by that rule |  [optional] |



