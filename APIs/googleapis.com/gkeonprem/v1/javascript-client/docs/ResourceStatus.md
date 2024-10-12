# AnthosOnPremApi.ResourceStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**[ResourceCondition]**](ResourceCondition.md) | ResourceCondition provide a standard mechanism for higher-level status reporting from controller. | [optional] 
**errorMessage** | **String** | Human-friendly representation of the error message from controller. The error message can be temporary as the controller controller creates a cluster or node pool. If the error message persists for a longer period of time, it can be used to surface error message to indicate real problems requiring user intervention. | [optional] 


