# DialogflowApi.GoogleCloudDialogflowV2beta1IntentParameter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defaultValue** | **String** | Optional. The default value to use when the &#x60;value&#x60; yields an empty result. Default values can be extracted from contexts by using the following syntax: &#x60;#context_name.parameter_name&#x60;. | [optional] 
**displayName** | **String** | Required. The name of the parameter. | [optional] 
**entityTypeDisplayName** | **String** | Optional. The name of the entity type, prefixed with &#x60;@&#x60;, that describes values of the parameter. If the parameter is required, this must be provided. | [optional] 
**isList** | **Boolean** | Optional. Indicates whether the parameter represents a list of values. | [optional] 
**mandatory** | **Boolean** | Optional. Indicates whether the parameter is required. That is, whether the intent cannot be completed without collecting the parameter value. | [optional] 
**name** | **String** | The unique identifier of this parameter. | [optional] 
**prompts** | **[String]** | Optional. The collection of prompts that the agent can present to the user in order to collect a value for the parameter. | [optional] 
**value** | **String** | Optional. The definition of the parameter value. It can be: - a constant string, - a parameter value defined as &#x60;$parameter_name&#x60;, - an original parameter value defined as &#x60;$parameter_name.original&#x60;, - a parameter value from some context defined as &#x60;#context_name.parameter_name&#x60;. | [optional] 


