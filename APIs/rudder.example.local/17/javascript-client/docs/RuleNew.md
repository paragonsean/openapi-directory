# RudderApi.RuleNew

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **String** | The parent category id. If provided, the new rule will be in this parent category | [optional] 
**directives** | **[String]** | Directives linked to the rule | [optional] 
**displayName** | **String** | Rule name | [optional] 
**enabled** | **Boolean** | Is the rule enabled | [optional] 
**id** | **String** | Rule id | [optional] 
**longDescription** | **String** | Rule documentation | [optional] 
**shortDescription** | **String** | One line rule description | [optional] 
**source** | **String** | The id of the rule the clone will be based onto. If this parameter if provided, the new rule will be a clone of this source. Other value will override values from the source. | [optional] 
**system** | **Boolean** | If true it is an internal Rudder rule | [optional] 
**tags** | [**[DirectiveTagsInner]**](DirectiveTagsInner.md) |  | [optional] 
**targets** | [**[RuleTargetsInner]**](RuleTargetsInner.md) | Node and special groups targeted by that rule | [optional] 


