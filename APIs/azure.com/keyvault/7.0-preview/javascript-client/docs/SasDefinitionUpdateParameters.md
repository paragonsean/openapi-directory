# KeyVaultClient.SasDefinitionUpdateParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**SasDefinitionAttributes**](SasDefinitionAttributes.md) |  | [optional] 
**sasType** | **String** | The type of SAS token the SAS definition will create. | [optional] 
**tags** | **{String: String}** | Application specific metadata in the form of key-value pairs. | [optional] 
**templateUri** | **String** | The SAS definition token template signed with an arbitrary key.  Tokens created according to the SAS definition will have the same properties as the template. | [optional] 
**validityPeriod** | **String** | The validity period of SAS tokens created according to the SAS definition. | [optional] 



## Enum: SasTypeEnum


* `account` (value: `"account"`)

* `service` (value: `"service"`)




