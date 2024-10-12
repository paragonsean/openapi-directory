# CloudHealthcareApi.InfoTypeTransformation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**characterMaskConfig** | [**CharacterMaskConfig**](CharacterMaskConfig.md) |  | [optional] 
**cryptoHashConfig** | [**CryptoHashConfig**](CryptoHashConfig.md) |  | [optional] 
**dateShiftConfig** | [**DateShiftConfig**](DateShiftConfig.md) |  | [optional] 
**infoTypes** | **[String]** | &#x60;InfoTypes&#x60; to apply this transformation to. If this is not specified, this transformation becomes the default transformation, and is used for any &#x60;info_type&#x60; that is not specified in another transformation. | [optional] 
**redactConfig** | **Object** | Define how to redact sensitive values. Default behaviour is erase. For example, \&quot;My name is Jane.\&quot; becomes \&quot;My name is .\&quot; | [optional] 
**replaceWithInfoTypeConfig** | **Object** | When using the INSPECT_AND_TRANSFORM action, each match is replaced with the name of the info_type. For example, \&quot;My name is Jane\&quot; becomes \&quot;My name is [PERSON_NAME].\&quot; The TRANSFORM action is equivalent to redacting. | [optional] 


