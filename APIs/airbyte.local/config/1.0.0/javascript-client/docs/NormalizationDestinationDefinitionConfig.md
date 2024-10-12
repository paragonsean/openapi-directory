# AirbyteConfigurationApi.NormalizationDestinationDefinitionConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**normalizationIntegrationType** | **String** | a field indicating the type of integration dialect to use for normalization. | [optional] 
**normalizationRepository** | **String** | a field indicating the name of the repository to be used for normalization. If the value of the flag is NULL - normalization is not used. | [optional] 
**normalizationTag** | **String** | a field indicating the tag of the docker repository to be used for normalization. | [optional] 
**supported** | **Boolean** | whether the destination definition supports normalization. | [default to false]


