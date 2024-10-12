# AgcoApi.BuildSystemSharedDTOActivityStep

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activityID** | **Number** | The id of the activity this activity step belongs to | [optional] 
**activityStepID** | **Number** | The id of this activity step | [optional] 
**implementationID** | **String** | The implementation id which is used to look up the step implementation | [optional] 
**parameterMappings** | [**[BuildSystemSharedDTOParameterMapping]**](BuildSystemSharedDTOParameterMapping.md) | The mapping of values from a source to be used for the step parameters | [optional] [readonly] 
**runOrder** | **Number** | The order of this activity step relative to other activity steps | [optional] 
**stepID** | **Number** | The id of the step | [optional] 
**stepName** | **String** | The name of the step | [optional] 
**useConfig** | **String** | Indicates the configuration for the ActivityStep to use at runtime.  The build agent must provide this configuration | [optional] 


