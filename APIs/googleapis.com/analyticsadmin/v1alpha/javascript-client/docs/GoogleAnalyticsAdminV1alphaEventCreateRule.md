# GoogleAnalyticsAdminApi.GoogleAnalyticsAdminV1alphaEventCreateRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destinationEvent** | **String** | Required. The name of the new event to be created. This value must: * be less than 40 characters * consist only of letters, digits or _ (underscores) * start with a letter | [optional] 
**eventConditions** | [**[GoogleAnalyticsAdminV1alphaMatchingCondition]**](GoogleAnalyticsAdminV1alphaMatchingCondition.md) | Required. Must have at least one condition, and can have up to 10 max. Conditions on the source event must match for this rule to be applied. | [optional] 
**name** | **String** | Output only. Resource name for this EventCreateRule resource. Format: properties/{property}/dataStreams/{data_stream}/eventCreateRules/{event_create_rule} | [optional] [readonly] 
**parameterMutations** | [**[GoogleAnalyticsAdminV1alphaParameterMutation]**](GoogleAnalyticsAdminV1alphaParameterMutation.md) | Parameter mutations define parameter behavior on the new event, and are applied in order. A maximum of 20 mutations can be applied. | [optional] 
**sourceCopyParameters** | **Boolean** | If true, the source parameters are copied to the new event. If false, or unset, all non-internal parameters are not copied from the source event. Parameter mutations are applied after the parameters have been copied. | [optional] 


