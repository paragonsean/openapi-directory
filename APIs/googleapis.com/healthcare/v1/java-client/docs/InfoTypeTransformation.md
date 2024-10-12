

# InfoTypeTransformation

A transformation to apply to text that is identified as a specific info_type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**characterMaskConfig** | [**CharacterMaskConfig**](CharacterMaskConfig.md) |  |  [optional] |
|**cryptoHashConfig** | [**CryptoHashConfig**](CryptoHashConfig.md) |  |  [optional] |
|**dateShiftConfig** | [**DateShiftConfig**](DateShiftConfig.md) |  |  [optional] |
|**infoTypes** | **List&lt;String&gt;** | InfoTypes to apply this transformation to. If this is not specified, the transformation applies to any info_type. |  [optional] |
|**redactConfig** | **Object** | Define how to redact sensitive values. Default behaviour is erase. For example, \&quot;My name is Jane.\&quot; becomes \&quot;My name is .\&quot; |  [optional] |
|**replaceWithInfoTypeConfig** | **Object** | When using the INSPECT_AND_TRANSFORM action, each match is replaced with the name of the info_type. For example, \&quot;My name is Jane\&quot; becomes \&quot;My name is [PERSON_NAME].\&quot; The TRANSFORM action is equivalent to redacting. |  [optional] |



