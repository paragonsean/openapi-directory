# MicrocksApiV17.Operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bindings** | [**{String: Binding}**](Binding.md) | Map of protocol binding details for this operation | [optional] 
**defaultDelay** | **Number** | Default response time delay for mocks | [optional] 
**dispatcher** | **String** | Dispatcher strategy used for mocks | [optional] 
**dispatcherRules** | **String** | DispatcherRules used for mocks | [optional] 
**inputName** | **String** | Name of input parameters in case of Xml based Service | [optional] 
**method** | **String** | Represents transport method | 
**name** | **String** | Unique name of this Operation within Service scope | 
**outputName** | **String** | Name of output parameters in case of Xml based Service | [optional] 
**parameterContraints** | [**[ParameterConstraint]**](ParameterConstraint.md) | Contraints that may apply to mock invocatino on this operation | [optional] 
**resourcePaths** | **[String]** | Paths the mocks endpoints are mapped on | [optional] 


