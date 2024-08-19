

# RuleNew


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | **UUID** | The parent category id. If provided, the new rule will be in this parent category |  [optional] |
|**directives** | **List&lt;String&gt;** | Directives linked to the rule |  [optional] |
|**displayName** | **String** | Rule name |  [optional] |
|**enabled** | **Boolean** | Is the rule enabled |  [optional] |
|**id** | **UUID** | Rule id |  [optional] |
|**longDescription** | **String** | Rule documentation |  [optional] |
|**shortDescription** | **String** | One line rule description |  [optional] |
|**source** | **UUID** | The id of the rule the clone will be based onto. If this parameter if provided, the new rule will be a clone of this source. Other value will override values from the source. |  [optional] |
|**system** | **Boolean** | If true it is an internal Rudder rule |  [optional] |
|**tags** | [**List&lt;DirectiveTagsInner&gt;**](DirectiveTagsInner.md) |  |  [optional] |
|**targets** | [**List&lt;RuleTargetsInner&gt;**](RuleTargetsInner.md) | Node and special groups targeted by that rule |  [optional] |



