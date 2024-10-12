# DiscoveryEngineApi.GoogleCloudDiscoveryengineV1betaCustomAttribute

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numbers** | **[Number]** | The numerical values of this custom attribute. For example, &#x60;[2.3, 15.4]&#x60; when the key is \&quot;lengths_cm\&quot;. Exactly one of CustomAttribute.text or CustomAttribute.numbers should be set. Otherwise, an &#x60;INVALID_ARGUMENT&#x60; error is returned. | [optional] 
**text** | **[String]** | The textual values of this custom attribute. For example, &#x60;[\&quot;yellow\&quot;, \&quot;green\&quot;]&#x60; when the key is \&quot;color\&quot;. Empty string is not allowed. Otherwise, an &#x60;INVALID_ARGUMENT&#x60; error is returned. Exactly one of CustomAttribute.text or CustomAttribute.numbers should be set. Otherwise, an &#x60;INVALID_ARGUMENT&#x60; error is returned. | [optional] 


