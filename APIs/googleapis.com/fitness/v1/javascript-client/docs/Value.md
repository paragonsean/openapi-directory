# FitnessApi.Value

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fpVal** | **Number** | Floating point value. When this is set, other values must not be set. | [optional] 
**intVal** | **Number** | Integer value. When this is set, other values must not be set. | [optional] 
**mapVal** | [**[ValueMapValEntry]**](ValueMapValEntry.md) | Map value. The valid key space and units for the corresponding value of each entry should be documented as part of the data type definition. Keys should be kept small whenever possible. Data streams with large keys and high data frequency may be down sampled. | [optional] 
**stringVal** | **String** | String value. When this is set, other values must not be set. Strings should be kept small whenever possible. Data streams with large string values and high data frequency may be down sampled. | [optional] 


