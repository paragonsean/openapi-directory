

# BuildSystemSharedDTOActivityStep

A DTO for an IActivityStep

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activityID** | **Integer** | The id of the activity this activity step belongs to |  [optional] |
|**activityStepID** | **Integer** | The id of this activity step |  [optional] |
|**implementationID** | **String** | The implementation id which is used to look up the step implementation |  [optional] |
|**parameterMappings** | [**List&lt;BuildSystemSharedDTOParameterMapping&gt;**](BuildSystemSharedDTOParameterMapping.md) | The mapping of values from a source to be used for the step parameters |  [optional] [readonly] |
|**runOrder** | **Integer** | The order of this activity step relative to other activity steps |  [optional] |
|**stepID** | **Integer** | The id of the step |  [optional] |
|**stepName** | **String** | The name of the step |  [optional] |
|**useConfig** | **String** | Indicates the configuration for the ActivityStep to use at runtime.  The build agent must provide this configuration |  [optional] |



