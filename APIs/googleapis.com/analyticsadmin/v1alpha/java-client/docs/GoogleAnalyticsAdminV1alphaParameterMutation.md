

# GoogleAnalyticsAdminV1alphaParameterMutation

Defines an event parameter to mutate.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**parameter** | **String** | Required. The name of the parameter to mutate. This value must: * be less than 40 characters. * be unique across across all mutations within the rule * consist only of letters, digits or _ (underscores) For event edit rules, the name may also be set to &#39;event_name&#39; to modify the event_name in place. |  [optional] |
|**parameterValue** | **String** | Required. The value mutation to perform. * Must be less than 100 characters. * To specify a constant value for the param, use the value&#39;s string. * To copy value from another parameter, use syntax like \&quot;[[other_parameter]]\&quot; For more details, see this [help center article](https://support.google.com/analytics/answer/10085872#modify-an-event&amp;zippy&#x3D;%2Cin-this-article%2Cmodify-parameters). |  [optional] |



